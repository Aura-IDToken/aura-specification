#!/usr/bin/env python3
"""Controlled draft verifier for the current FIX-001 local draft gate.

This script executes the current repository-local draft verification path for:
- CONF-001 Deterministic Evaluation
- CONF-002 Replay Verification
- CONF-006 Platform Independence
- CONF-004 Evidence Integrity
- CONF-005 Traceability
- CONF-010 Cryptographic Verification

It validates the FIX-001 working fixture, deterministically materializes the current
draft result/evidence path twice from the same request and policy, recomputes the
bound digest values, and executes one negative mutation control to prove that
Evidence tampering is detected.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

try:
    import jcs
except ImportError:  # pragma: no cover - optional dependency guard
    jcs = None

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - optional dependency guard
    Draft202012Validator = None


ROOT = Path(__file__).resolve().parents[1]


def require_runtime_dependencies() -> None:
    missing = []
    if jcs is None:
        missing.append("jcs")
    if Draft202012Validator is None:
        missing.append("jsonschema")
    if missing:
        raise RuntimeError(
            "Missing dependency: "
            + " and/or ".join(missing)
            + ". Install with `python -m pip install jcs jsonschema`."
        )
FIXTURE_PATH = ROOT / "fixtures" / "core" / "FIX-001_BASIC_EVALUATION.json"
SCHEMA_DIR = ROOT / "fixtures" / "schemas"
EXPANDED_SCHEMA_CACHE: dict[str, object] = {}
FIX001_CONF_MESSAGES = {
    "CONF-001": "identical FIX-001 inputs deterministically reproduce identical result and evidence objects",
    "CONF-002": "replay from FIX-001 evidence reproduces the identical result and a valid chained replay evidence pack",
    "CONF-004": "evidence mutation is detected by digest verification",
    "CONF-005": "execution, policy, attestation, and requirement links are coherent",
    "CONF-006": "draft platform contexts reproduce identical result and evidence artifacts",
    "CONF-010": "input, output, evidence, and pack digests recompute correctly",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def canonical_json(value: object) -> str:
    require_runtime_dependencies()
    return jcs.canonicalize(value).decode("utf-8")


def canonical_sha256(obj: object) -> str:
    return hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()


def expand_local_refs(node: object, cache: dict[str, object] | None = None) -> object:
    cache = {} if cache is None else cache

    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and not ref.startswith("#"):
            if ref not in cache:
                cache[ref] = expand_local_refs(load_json(SCHEMA_DIR / ref), cache)
            resolved = copy.deepcopy(cache[ref])
            siblings = {
                key: expand_local_refs(value, cache)
                for key, value in node.items()
                if key != "$ref"
            }
            if siblings:
                if not isinstance(resolved, dict):
                    raise TypeError(f"Referenced schema {ref} did not resolve to an object")
                resolved.update(siblings)
            return resolved
        return {key: expand_local_refs(value, cache) for key, value in node.items()}

    if isinstance(node, list):
        return [expand_local_refs(value, cache) for value in node]

    return node


def validate_schema(schema_name: str, instance: object) -> None:
    require_runtime_dependencies()
    if schema_name not in EXPANDED_SCHEMA_CACHE:
        EXPANDED_SCHEMA_CACHE[schema_name] = expand_local_refs(load_json(SCHEMA_DIR / schema_name))
    schema = copy.deepcopy(EXPANDED_SCHEMA_CACHE[schema_name])
    Draft202012Validator(
        schema, format_checker=Draft202012Validator.FORMAT_CHECKER
    ).validate(instance)


def assert_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def make_integrity_hash(obj: dict) -> str:
    return canonical_sha256({k: v for k, v in obj.items() if k != "integrity_hash"})


def reorder_mapping(source: dict, ordered_keys: list[str]) -> dict:
    if set(source) != set(ordered_keys):
        raise AssertionError("request_field_order must preserve exactly the request_fields key set")
    reordered: dict = {}
    for key in ordered_keys:
        reordered[key] = source[key]
    return reordered


def evaluate_request(request_fields: dict) -> tuple[str, str]:
    measurement_value = request_fields["measurement_value"]
    if measurement_value <= 500:
        return "ALLOW", "ALLOW when measurement_value <= 500; DENY otherwise"
    return "DENY", "ALLOW when measurement_value <= 500; DENY otherwise"


def materialize_result(fixture: dict) -> dict:
    request = fixture["input_data"]
    expected_result = fixture["expected_output"]
    policy_reference = copy.deepcopy(expected_result["policy_reference"])

    decision, matched_policy_rule = evaluate_request(request["request_fields"])
    result_fields = {
        "profile_id": request["request_fields"]["profile_id"],
        "subject_id": request["request_fields"]["subject_id"],
        "measurement_value": request["request_fields"]["measurement_value"],
        "matched_policy_rule": matched_policy_rule,
    }
    output_hash = canonical_sha256({"decision": decision, "result_fields": result_fields})
    result = {
        "object_id": expected_result["object_id"],
        "object_type": "EvaluationResult",
        "protocol_version": expected_result["protocol_version"],
        "schema_version": expected_result["schema_version"],
        "created_at": expected_result["created_at"],
        "execution_id": expected_result["execution_id"],
        "decision": decision,
        "output_hash": output_hash,
        "policy_reference": policy_reference,
        "result_fields": result_fields,
    }
    result["integrity_hash"] = make_integrity_hash(result)
    return result


def materialize_result_for_context(fixture: dict, context: dict) -> dict:
    fixture_variant = copy.deepcopy(fixture)
    order = context["request_field_order"]
    fixture_variant["input_data"]["request_fields"] = reorder_mapping(
        fixture["input_data"]["request_fields"], order
    )
    return materialize_result(fixture_variant)


def materialize_attestation(fixture: dict) -> dict:
    expected_attestation = fixture["expected_evidence"]["attestation"]
    attestation = {
        "object_id": expected_attestation["object_id"],
        "object_type": "Attestation",
        "protocol_version": expected_attestation["protocol_version"],
        "schema_version": expected_attestation["schema_version"],
        "created_at": expected_attestation["created_at"],
        "attestation_type": expected_attestation["attestation_type"],
        "attested_execution_id": fixture["expected_output"]["execution_id"],
        "evidence_reference": fixture["expected_evidence"]["pack_id"],
    }
    attestation["attestation_hash"] = canonical_sha256(
        {
            "attestation_type": attestation["attestation_type"],
            "attested_execution_id": attestation["attested_execution_id"],
            "evidence_reference": attestation["evidence_reference"],
        }
    )
    attestation["integrity_hash"] = make_integrity_hash(attestation)
    return attestation


def materialize_evidence_pack(fixture: dict, result: dict) -> dict:
    request = fixture["input_data"]
    expected_pack = fixture["expected_evidence"]
    policy_reference = copy.deepcopy(expected_pack["policy_reference"])
    attestation = materialize_attestation(fixture)

    evidence_object = {
        "evidence_id": expected_pack["evidence_object"]["evidence_id"],
        "protocol_version": expected_pack["evidence_object"]["protocol_version"],
        "schema_version": expected_pack["evidence_object"]["schema_version"],
        "implementation_id": expected_pack["evidence_object"]["implementation_id"],
        "execution_id": result["execution_id"],
        "timestamp": expected_pack["evidence_object"]["timestamp"],
        "policy_reference": policy_reference["object_id"],
        "requirement_references": list(expected_pack["evidence_object"]["requirement_references"]),
        "input_hash": request["input_hash"],
        "output_hash": result["output_hash"],
        "previous_evidence_hash": None,
        "attestation_reference": attestation["object_id"],
    }
    evidence_object["evidence_hash"] = canonical_sha256(
        {k: v for k, v in evidence_object.items() if k != "evidence_hash"}
    )

    integrity_metadata = {
        "canonicalization_profile": expected_pack["integrity_metadata"]["canonicalization_profile"],
        "digest_algorithm": expected_pack["integrity_metadata"]["digest_algorithm"],
        "request_integrity_hash": request["integrity_hash"],
        "result_integrity_hash": result["integrity_hash"],
        "policy_integrity_hash": policy_reference["integrity_hash"],
        "attestation_integrity_hash": attestation["integrity_hash"],
    }

    pack = {
        "pack_id": expected_pack["pack_id"],
        "pack_version": expected_pack["pack_version"],
        "protocol_version": expected_pack["protocol_version"],
        "schema_version": expected_pack["schema_version"],
        "evidence_profile": expected_pack["evidence_profile"],
        "requirement_references": list(expected_pack["requirement_references"]),
        "evidence_object": evidence_object,
        "evaluation_result": copy.deepcopy(result),
        "policy_reference": policy_reference,
        "attestation": attestation,
        "integrity_metadata": integrity_metadata,
    }
    pack["pack_hash"] = canonical_sha256({k: v for k, v in pack.items() if k != "pack_hash"})
    return pack


def materialize_replay_pack(fixture: dict, result: dict) -> dict:
    original_pack = fixture["expected_evidence"]
    policy_reference = copy.deepcopy(original_pack["policy_reference"])
    replay_info = fixture["_draft_replay_materialization"]
    attestation = {
        "object_id": replay_info["attestation_id"],
        "object_type": "Attestation",
        "protocol_version": original_pack["attestation"]["protocol_version"],
        "schema_version": original_pack["attestation"]["schema_version"],
        "created_at": replay_info["timestamp"],
        "attestation_type": "REPLAY",
        "attested_execution_id": result["execution_id"],
        "evidence_reference": replay_info["pack_id"],
    }
    attestation["attestation_hash"] = canonical_sha256(
        {
            "attestation_type": attestation["attestation_type"],
            "attested_execution_id": attestation["attested_execution_id"],
            "evidence_reference": attestation["evidence_reference"],
        }
    )
    attestation["integrity_hash"] = make_integrity_hash(attestation)

    evidence_object = {
        "evidence_id": replay_info["evidence_id"],
        "protocol_version": original_pack["evidence_object"]["protocol_version"],
        "schema_version": original_pack["evidence_object"]["schema_version"],
        "implementation_id": original_pack["evidence_object"]["implementation_id"],
        "execution_id": result["execution_id"],
        "timestamp": replay_info["timestamp"],
        "policy_reference": policy_reference["object_id"],
        "requirement_references": list(replay_info["evidence_requirement_references"]),
        "input_hash": fixture["input_data"]["input_hash"],
        "output_hash": result["output_hash"],
        "previous_evidence_hash": original_pack["evidence_object"]["evidence_hash"],
        "attestation_reference": attestation["object_id"],
    }
    evidence_object["evidence_hash"] = canonical_sha256(
        {k: v for k, v in evidence_object.items() if k != "evidence_hash"}
    )

    integrity_metadata = {
        "canonicalization_profile": original_pack["integrity_metadata"]["canonicalization_profile"],
        "digest_algorithm": original_pack["integrity_metadata"]["digest_algorithm"],
        "request_integrity_hash": fixture["input_data"]["integrity_hash"],
        "result_integrity_hash": result["integrity_hash"],
        "policy_integrity_hash": policy_reference["integrity_hash"],
        "attestation_integrity_hash": attestation["integrity_hash"],
    }

    replay_pack = {
        "pack_id": replay_info["pack_id"],
        "pack_version": replay_info["pack_version"],
        "protocol_version": original_pack["protocol_version"],
        "schema_version": original_pack["schema_version"],
        "evidence_profile": original_pack["evidence_profile"],
        "requirement_references": list(replay_info["pack_requirement_references"]),
        "evidence_object": evidence_object,
        "evaluation_result": copy.deepcopy(result),
        "policy_reference": policy_reference,
        "attestation": attestation,
        "integrity_metadata": integrity_metadata,
    }
    replay_pack["pack_hash"] = canonical_sha256(
        {k: v for k, v in replay_pack.items() if k != "pack_hash"}
    )
    return replay_pack


def verify_deterministic_evaluation(fixture: dict) -> None:
    first_result = materialize_result(fixture)
    second_result = materialize_result(fixture)
    assert_equal(first_result, second_result, "deterministic result replay")
    assert_equal(first_result, fixture["expected_output"], "fixture expected_output")

    first_pack = materialize_evidence_pack(fixture, first_result)
    second_pack = materialize_evidence_pack(fixture, second_result)
    assert_equal(first_pack, second_pack, "deterministic evidence replay")
    assert_equal(first_pack, fixture["expected_evidence"], "fixture expected_evidence")


def verify_replay(fixture: dict) -> None:
    request = fixture["input_data"]
    original_pack = fixture["expected_evidence"]
    original_result = original_pack["evaluation_result"]
    materialized_result = materialize_result(fixture)
    assert_equal(
        fixture["expected_output"], original_result, "fixture/original pack result parity"
    )
    assert_equal(
        materialized_result,
        original_result,
        "re-materialized replay result parity",
    )
    replay_result = copy.deepcopy(original_result)
    replay_pack = materialize_replay_pack(fixture, replay_result)

    validate_schema("evidence-pack.schema.json", replay_pack)
    verify_evidence_pack_hashes(request, replay_result, replay_pack)

    assert_equal(replay_result, original_result, "replay result parity")
    assert_equal(replay_pack["evaluation_result"], original_result, "replay pack evaluation_result")
    assert_equal(
        replay_pack["evidence_object"]["previous_evidence_hash"],
        original_pack["evidence_object"]["evidence_hash"],
        "replay chain linkage",
    )
    assert_equal(
        replay_pack["evidence_object"]["output_hash"],
        original_pack["evidence_object"]["output_hash"],
        "replay output_hash",
    )
    assert_equal(
        replay_pack["integrity_metadata"]["result_integrity_hash"],
        original_pack["integrity_metadata"]["result_integrity_hash"],
        "replay integrity_metadata.result_integrity_hash",
    )


def verify_platform_independence(fixture: dict) -> None:
    contexts = fixture["_draft_execution_contexts"]
    if len(contexts) < 2:
        raise AssertionError("At least two draft execution contexts are required for CONF-006")

    materialized = []
    for context in contexts:
        result = materialize_result_for_context(fixture, context)
        pack = materialize_evidence_pack(fixture, result)
        materialized.append((context["context_id"], result, pack))

    baseline_context, baseline_result, baseline_pack = materialized[0]
    assert_equal(baseline_result, fixture["expected_output"], f"{baseline_context} result")
    assert_equal(baseline_pack, fixture["expected_evidence"], f"{baseline_context} evidence")

    for context_id, result, pack in materialized[1:]:
        assert_equal(result, baseline_result, f"{context_id} result parity")
        assert_equal(pack, baseline_pack, f"{context_id} evidence parity")


def verify_evidence_pack_hashes(request: dict, result: dict, pack: dict) -> None:
    evidence_object = pack["evidence_object"]
    policy_reference = pack["policy_reference"]
    attestation = pack["attestation"]

    assert_equal(
        request["input_hash"],
        canonical_sha256(request["request_fields"]),
        "input_hash",
    )
    assert_equal(
        result["output_hash"],
        canonical_sha256(
            {"decision": result["decision"], "result_fields": result["result_fields"]}
        ),
        "output_hash",
    )
    assert_equal(
        request["integrity_hash"],
        canonical_sha256({k: v for k, v in request.items() if k != "integrity_hash"}),
        "request.integrity_hash",
    )
    assert_equal(
        policy_reference["integrity_hash"],
        canonical_sha256(
            {k: v for k, v in policy_reference.items() if k != "integrity_hash"}
        ),
        "policy_reference.integrity_hash",
    )
    assert_equal(
        result["integrity_hash"],
        canonical_sha256({k: v for k, v in result.items() if k != "integrity_hash"}),
        "evaluation_result.integrity_hash",
    )

    attestation_content = {
        "attestation_type": attestation["attestation_type"],
        "attested_execution_id": attestation["attested_execution_id"],
        "evidence_reference": attestation["evidence_reference"],
    }
    assert_equal(
        attestation["attestation_hash"],
        canonical_sha256(attestation_content),
        "attestation_hash",
    )
    assert_equal(
        attestation["integrity_hash"],
        canonical_sha256({k: v for k, v in attestation.items() if k != "integrity_hash"}),
        "attestation.integrity_hash",
    )
    assert_equal(
        evidence_object["evidence_hash"],
        canonical_sha256(
            {k: v for k, v in evidence_object.items() if k != "evidence_hash"}
        ),
        "evidence_hash",
    )
    assert_equal(
        pack["integrity_metadata"]["request_integrity_hash"],
        request["integrity_hash"],
        "integrity_metadata.request_integrity_hash",
    )
    assert_equal(
        pack["integrity_metadata"]["result_integrity_hash"],
        result["integrity_hash"],
        "integrity_metadata.result_integrity_hash",
    )
    assert_equal(
        pack["integrity_metadata"]["policy_integrity_hash"],
        policy_reference["integrity_hash"],
        "integrity_metadata.policy_integrity_hash",
    )
    assert_equal(
        pack["integrity_metadata"]["attestation_integrity_hash"],
        attestation["integrity_hash"],
        "integrity_metadata.attestation_integrity_hash",
    )
    assert_equal(
        pack["pack_hash"],
        canonical_sha256({k: v for k, v in pack.items() if k != "pack_hash"}),
        "pack_hash",
    )


def verify_pack_hashes(fixture: dict) -> None:
    verify_evidence_pack_hashes(
        fixture["input_data"], fixture["expected_output"], fixture["expected_evidence"]
    )


def verify_traceability(fixture: dict) -> None:
    request = fixture["input_data"]
    result = fixture["expected_output"]
    pack = fixture["expected_evidence"]
    evidence_object = pack["evidence_object"]
    policy_reference = pack["policy_reference"]
    attestation = pack["attestation"]

    assert_equal(result, pack["evaluation_result"], "pack.evaluation_result")
    assert_equal(result["policy_reference"], policy_reference, "policy_reference embedding")
    assert_equal(evidence_object["execution_id"], result["execution_id"], "execution_id linkage")
    assert_equal(
        attestation["attested_execution_id"],
        result["execution_id"],
        "attested_execution_id linkage",
    )
    assert_equal(
        evidence_object["policy_reference"],
        policy_reference["object_id"],
        "evidence_object.policy_reference linkage",
    )
    assert_equal(
        evidence_object["attestation_reference"],
        attestation["object_id"],
        "attestation_reference linkage",
    )
    assert_equal(
        attestation["evidence_reference"],
        pack["pack_id"],
        "attestation.evidence_reference linkage",
    )
    if not set(evidence_object["requirement_references"]).issubset(
        set(pack["requirement_references"])
    ):
        raise AssertionError("pack.requirement_references must include evidence_object references")
    assert_equal(
        evidence_object["input_hash"],
        request["input_hash"],
        "evidence_object.input_hash linkage",
    )
    assert_equal(
        evidence_object["output_hash"],
        result["output_hash"],
        "evidence_object.output_hash linkage",
    )


def mutate_hash_first_character(digest: str) -> str:
    """Return a deterministic, valid-hex digest string different from the input."""
    if not digest:
        raise ValueError("Digest must not be empty")
    replacement = "0" if digest[0] != "0" else "1"
    return replacement + digest[1:]


def verify_mutation_detection(fixture: dict) -> None:
    mutated = copy.deepcopy(fixture)
    original_hash = mutated["expected_evidence"]["evidence_object"]["output_hash"]
    mutated["expected_evidence"]["evidence_object"]["output_hash"] = (
        mutate_hash_first_character(original_hash)
    )
    try:
        verify_pack_hashes(mutated)
    except AssertionError:
        return
    raise AssertionError("Mutation control did not detect Evidence tampering")


def run_fix001_gate() -> dict[str, str]:
    fixture = load_json(FIXTURE_PATH)

    validate_schema("evaluation-request.schema.json", fixture["input_data"])
    validate_schema("evaluation-result.schema.json", fixture["expected_output"])
    validate_schema("evidence-pack.schema.json", fixture["expected_evidence"])

    verify_deterministic_evaluation(fixture)
    verify_replay(fixture)
    verify_platform_independence(fixture)
    verify_pack_hashes(fixture)
    verify_traceability(fixture)
    verify_mutation_detection(fixture)

    return dict(FIX001_CONF_MESSAGES)


def main() -> int:
    results = run_fix001_gate()

    for conf_id in ["CONF-001", "CONF-002", "CONF-006", "CONF-004", "CONF-005", "CONF-010"]:
        print(f"{conf_id} PASS — {results[conf_id]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

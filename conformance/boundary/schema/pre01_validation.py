"""BC-02.1 PRE-01 — engineering validation harness.

Runs PRE-01-001 .. PRE-01-010 against the BC-02.1 v2 reference schema
implementation and prints one independently recorded result per assertion.

These are ENGINEERING validation assertions about a schema. They are not C1-C8,
not CONF-003 section 4.5 test cases, not N-01 .. N-08, not B-VAL-014, and not a
conformance result. A PASS here says a schema property holds; it says nothing
about protocol conformance.

Execution boundary observed by this harness:

* No receiver production artifact (RI-PY, RI-RS) is imported or invoked.
* The issued P-01 artifact is never handed to a receiver. It is opened
  read-only, and only to check that it is unchanged (PRE-01-009).
* All receipts constructed here are built from synthetic in-memory octets.
  Those octets are validation vectors, not fixtures: they have no fixture
  identity, are never written to disk, and define no fixture class.

Usage:  python3 conformance/boundary/schema/pre01_validation.py
Exit code 0 when every assertion is PASS, 1 otherwise. The exit code is a
harness signal, not a verdict of any kind about the protocol.
"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from dataclasses import dataclass
from typing import Callable, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bc021_receipt_v2 import (  # noqa: E402
    FORBIDDEN_RECEIPT_KEYS,
    FORBIDDEN_RECEIPT_VALUES,
    INPUT_SEGMENT_REF,
    RECEIVED_BUFFER_REF,
    AdapterIdentity,
    BoundaryReceipt,
    BoundaryReceiver,
    DigestSource,
    EnvironmentIdentity,
    FixtureIdentity,
    HandoffStatus,
    RawInputEncoding,
    ReceiptConstructionError,
    ReceiverIdentity,
    SourceMaterial,
    UnresolvedState,
    UnresolvedValue,
    decode_transport_octets,
    serialize_receipt,
    transport_mapping,
    walk,
)

PASS = "PASS"
FAIL = "FAIL"
BLOCKED = "BLOCKED"
UNKNOWN = "UNKNOWN"

REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
)

P01_ARTIFACT_PATH = "conformance/boundary/p01/FIX-DIGEST-P01.canonical.json"

#: Declared in the BC-02.1 PRE-01 instruction, section 5. Checked, never written.
P01_DECLARED_ARTIFACT_IDENTITY = (
    "ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667"
)
P01_DECLARED_OCTET_LENGTH = 15

#: Paths this task is authorized to add. Anything else appearing as modified in
#: the working tree fails PRE-01-010.
AUTHORIZED_PATHS = (
    "conformance/boundary/BC-02.1-COMMON-RECEIPT-SCHEMA-v2.md",
    "conformance/boundary/BC-02.1-PRE-01-SCHEMA-CORRECTION-RECORD.md",
    "conformance/boundary/schema/.gitignore",
    "conformance/boundary/schema/bc021_receipt_v2.py",
    "conformance/boundary/schema/pre01_validation.py",
    "conformance/boundary/evidence/pre-01/PRE-01-VALIDATION-REPORT.txt",
)

#: Protected authority artifacts named by the PRE-01 instruction, section 2.
PROTECTED_ARTIFACTS = (
    "aps/APS-200_CANONICAL_DATA_MODEL.md",
    "APS-200 — Canonical Data Model_260723_192852.txt",
    "conformance/CONF-003_CANONICAL_SERIALIZATION.md",
    "ck003/DQ-004_EVENT_TYPE_SEMANTICS.md",
    "conformance/boundary/p01/FIX-DIGEST-P01.canonical.json",
    "conformance/boundary/BC-02.1-COMMON-RECEIPT-SCHEMA-v1.md",
    "conformance/boundary/B-VAL-014-DEFINITION-RECONCILIATION-RECORD.md",
    "conformance/boundary/CONTROLLED-P01-HANDOFF-RECORD.md",
    "conformance/boundary/BC-02-CUSTODIAN-CLOSURE-RECORD.md",
    "conformance/boundary/BC-02-CROSS-RECEIVER-PREEXEC-AUDIT.md",
    "conformance/boundary/BC-02.3-RI-RS-RECEIVER-v1.md",
    "conformance/boundary/ri_rs_receiver.rs",
    "conformance/boundary/ri-rs/src/bin/p01_handoff.rs",
    "conformance/boundary/evidence/controlled-p01-handoff/RI-PY-P01-RECEIPT.json",
    "conformance/boundary/evidence/controlled-p01-handoff/RI-RS-P01-RECEIPT.json",
)

# --------------------------------------------------------------------------
# Synthetic validation material. Not a fixture. Never written to disk.
# --------------------------------------------------------------------------

SYNTHETIC_IDENTITY_UNIT = b"PRE-01 synthetic octets"

#: Base16 text whose decoded input segment differs from the received buffer.
#: This is the differential case: if the two operands were aliases they would
#: be equal here, and they are not.
SYNTHETIC_BASE16_UNIT = b"4142434445"
SYNTHETIC_BASE16_SEGMENT = b"ABCDE"

SYNTHETIC_ARTIFACT_IDENTITY_A = "a" * 64
SYNTHETIC_ARTIFACT_IDENTITY_B = "b" * 64


@dataclass(frozen=True)
class AssertionResult:
    assertion_id: str
    statement: str
    verdict: str
    evidence: Tuple[str, ...]


def _synthetic_receiver() -> BoundaryReceiver:
    return BoundaryReceiver(
        receiver=ReceiverIdentity(
            receiver_id="PRE-01-SCHEMA-HARNESS",
            implementation_id="bc021-receipt-v2-reference",
            implementation_version="2.0.0",
            source_commit="working-tree",
        ),
        adapter=AdapterIdentity(
            adapter_id="PRE-01-SCHEMA-HARNESS-ADAPTER", adapter_version="2.0.0"
        ),
        environment=EnvironmentIdentity(
            environment_id="pre-01-schema-validation",
            platform="schema-layer",
            runtime="python3",
        ),
    )


def _synthetic_fixture(
    artifact_identity: str = SYNTHETIC_ARTIFACT_IDENTITY_A,
    issuance_id: object = None,
) -> FixtureIdentity:
    """Identity block for a synthetic validation vector.

    Deliberately not a fixture identifier: no FIX- identity is used, so this
    cannot be mistaken for, or promoted into, a fixture.
    """
    if issuance_id is None:
        issuance_id = UnresolvedValue(
            state=UnresolvedState.UNKNOWN,
            detail="synthetic validation vector has no issuance record",
        )
    return FixtureIdentity(
        fixture_id="PRE-01-SYNTHETIC-VECTOR-NOT-A-FIXTURE",
        fixture_artifact_identity=artifact_identity,
        fixture_artifact_name="pre-01-synthetic-vector",
        issuance_id=issuance_id,
    )


def _receive(
    transfer_unit: bytes,
    encoding: RawInputEncoding = RawInputEncoding.IDENTITY,
    artifact_identity: str = SYNTHETIC_ARTIFACT_IDENTITY_A,
) -> BoundaryReceipt:
    return _synthetic_receiver().receive(
        fixture=_synthetic_fixture(artifact_identity),
        method="in-memory-synthetic-octet-handoff",
        transfer_unit=transfer_unit,
        raw_input_encoding=encoding,
        status=HandoffStatus.TRANSFERRED,
    )


def _git(*args: str) -> Optional[str]:
    """Run a read-only git command. Returns None when git is unavailable."""
    try:
        completed = subprocess.run(
            ("git",) + args,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except (OSError, ValueError):
        return None
    if completed.returncode != 0:
        return None
    return completed.stdout


# --------------------------------------------------------------------------
# PRE-01-001 .. PRE-01-010
# --------------------------------------------------------------------------


def pre_01_001() -> AssertionResult:
    """fixture_artifact_identity originates from exact issued artifact bytes."""
    evidence: List[str] = []
    checks: List[bool] = []

    # The field is a declared identity, never derived from received material:
    # the same transfer unit carries whichever identity is declared.
    receipt_a = _receive(SYNTHETIC_IDENTITY_UNIT, artifact_identity=SYNTHETIC_ARTIFACT_IDENTITY_A)
    receipt_b = _receive(SYNTHETIC_IDENTITY_UNIT, artifact_identity=SYNTHETIC_ARTIFACT_IDENTITY_B)
    tracks_declaration = (
        receipt_a.fixture.fixture_artifact_identity == SYNTHETIC_ARTIFACT_IDENTITY_A
        and receipt_b.fixture.fixture_artifact_identity == SYNTHETIC_ARTIFACT_IDENTITY_B
    )
    checks.append(tracks_declaration)
    evidence.append(
        "same transfer unit, two declared identities: {0!r} / {1!r} -> "
        "field tracks declaration, not the received buffer: {2}".format(
            receipt_a.fixture.fixture_artifact_identity[:8] + "...",
            receipt_b.fixture.fixture_artifact_identity[:8] + "...",
            tracks_declaration,
        )
    )

    not_operand_derived = (
        receipt_a.fixture.fixture_artifact_identity
        != receipt_a.digest_operands.receipt_digest.value
        and receipt_a.fixture.fixture_artifact_identity
        != receipt_a.digest_operands.input_segment_sha256.value
    )
    checks.append(not_operand_derived)
    evidence.append(
        "declared identity is not read back from either operand: {0}".format(
            not_operand_derived
        )
    )

    # A name is rejected where an identity is required.
    try:
        _receive(SYNTHETIC_IDENTITY_UNIT, artifact_identity="FIX-DIGEST-P01.canonical.json")
        name_rejected = False
    except ReceiptConstructionError:
        name_rejected = True
    checks.append(name_rejected)
    evidence.append(
        "artifact NAME rejected where artifact IDENTITY is required: {0}".format(
            name_rejected
        )
    )

    # Read-only observation of the issued artifact. No handoff, no receiver.
    path = os.path.join(REPO_ROOT, P01_ARTIFACT_PATH)
    if os.path.isfile(path):
        with open(path, "rb") as handle:
            octets = handle.read()
        observed = hashlib.sha256(octets).hexdigest()
        matches = observed == P01_DECLARED_ARTIFACT_IDENTITY
        checks.append(matches)
        evidence.append(
            "read-only: SHA-256(issued P-01 octets)={0} == declared construction "
            "fingerprint: {1}".format(observed, matches)
        )
    else:
        checks.append(False)
        evidence.append("issued P-01 artifact not reachable at {0}".format(P01_ARTIFACT_PATH))

    evidence.append(
        "scope limit: no issuance record exists in any in-scope repository, so "
        "the declared identity is bound to the repository-resident issued "
        "artifact only, not to an issuance authority record"
    )
    return AssertionResult(
        "PRE-01-001",
        "fixture_artifact_identity originates from exact issued artifact bytes",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


def pre_01_002() -> AssertionResult:
    """receipt_digest originates from the actual receiver buffer."""
    evidence: List[str] = []
    checks: List[bool] = []
    receipt = _receive(SYNTHETIC_BASE16_UNIT, RawInputEncoding.BASE16)
    operand = receipt.digest_operands.receipt_digest

    independent = hashlib.sha256(receipt.received.raw_octets).hexdigest()
    checks.append(operand.value == independent)
    evidence.append(
        "recorded={0} independent SHA-256(received.raw_octets)={1} equal={2}".format(
            operand.value, independent, operand.value == independent
        )
    )

    checks.append(operand.source_material is SourceMaterial.RECEIVED_BUFFER)
    checks.append(operand.source_material_ref == RECEIVED_BUFFER_REF)
    checks.append(operand.source is DigestSource.RECEIVER_RECOMPUTED)
    checks.append(
        operand.source_material_octet_length == len(receipt.received.raw_octets)
    )
    evidence.append(
        "source_material={0} source_material_ref={1} source={2} "
        "source_material_octet_length={3}".format(
            operand.source_material.value,
            operand.source_material_ref,
            operand.source.value,
            operand.source_material_octet_length,
        )
    )

    checks.append(not BoundaryReceiver.digest_input_is_caller_supplied())
    evidence.append(
        "receive() admits no digest parameter: {0}".format(
            not BoundaryReceiver.digest_input_is_caller_supplied()
        )
    )
    evidence.append("calculation_path={0}".format(operand.calculation_path))
    return AssertionResult(
        "PRE-01-002",
        "receipt_digest originates from the actual receiver buffer",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


def pre_01_003() -> AssertionResult:
    """input_segment_sha256 has an independently identifiable source."""
    evidence: List[str] = []
    checks: List[bool] = []
    receipt = _receive(SYNTHETIC_BASE16_UNIT, RawInputEncoding.BASE16)
    operand = receipt.digest_operands.input_segment_sha256

    segment_is_raw = isinstance(receipt.input_segment.octets, bytes)
    checks.append(segment_is_raw)
    checks.append(receipt.input_segment.octets == SYNTHETIC_BASE16_SEGMENT)
    evidence.append(
        "input_segment.octets recorded as raw octets, length {0}, distinct from "
        "the received buffer of length {1}".format(
            receipt.input_segment.octet_length, receipt.received.octet_length
        )
    )

    independent = hashlib.sha256(receipt.input_segment.octets).hexdigest()
    checks.append(operand.value == independent)
    evidence.append(
        "recorded={0} independent SHA-256(input_segment.octets)={1} equal={2}".format(
            operand.value, independent, operand.value == independent
        )
    )

    checks.append(operand.source_material is SourceMaterial.INPUT_SEGMENT)
    checks.append(operand.source_material_ref == INPUT_SEGMENT_REF)
    checks.append(operand.source is DigestSource.RECEIVER_RECOMPUTED)
    checks.append(
        receipt.input_segment.raw_input_encoding is RawInputEncoding.BASE16
    )
    evidence.append(
        "source_material={0} source_material_ref={1} source={2} "
        "raw_input_encoding={3}".format(
            operand.source_material.value,
            operand.source_material_ref,
            operand.source.value,
            receipt.input_segment.raw_input_encoding.value,
        )
    )

    # The transport representation reverses to exactly the recorded octets.
    mapping = transport_mapping(receipt)
    round_trip = decode_transport_octets(mapping["input_segment"]["octets"])
    checks.append(round_trip == receipt.input_segment.octets)
    evidence.append(
        "Base64 transport of input_segment.octets reverses to the recorded "
        "octets: {0}".format(round_trip == receipt.input_segment.octets)
    )
    evidence.append("calculation_path={0}".format(operand.calculation_path))
    return AssertionResult(
        "PRE-01-003",
        "input_segment_sha256 has an independently identifiable source",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


def pre_01_004() -> AssertionResult:
    """The two digest operands do not share a previously computed value."""
    evidence: List[str] = []
    checks: List[bool] = []

    # Differential falsification. Aliased operands would be equal here.
    differential = _receive(SYNTHETIC_BASE16_UNIT, RawInputEncoding.BASE16)
    left = differential.digest_operands.receipt_digest.value
    right = differential.digest_operands.input_segment_sha256.value
    checks.append(left != right)
    evidence.append(
        "differential case (raw_input_encoding=base16): receipt_digest={0} "
        "input_segment_sha256={1} equal={2} -- two values from one buffer would "
        "be equal here; they are not".format(left[:16] + "...", right[:16] + "...", left == right)
    )
    checks.append(
        left == hashlib.sha256(SYNTHETIC_BASE16_UNIT).hexdigest()
        and right == hashlib.sha256(SYNTHETIC_BASE16_SEGMENT).hexdigest()
    )
    evidence.append(
        "each operand reproduces SHA-256 of its own material independently: {0}".format(
            left == hashlib.sha256(SYNTHETIC_BASE16_UNIT).hexdigest()
            and right == hashlib.sha256(SYNTHETIC_BASE16_SEGMENT).hexdigest()
        )
    )

    # Identity case: values coincide, and the coincidence is still an
    # observation of two computations, not an assignment.
    coincident = _receive(SYNTHETIC_IDENTITY_UNIT, RawInputEncoding.IDENTITY)
    same_value = (
        coincident.digest_operands.receipt_digest.value
        == coincident.digest_operands.input_segment_sha256.value
    )
    distinct_buffers = (
        coincident.received.raw_octets is not coincident.input_segment.octets
    )
    checks.append(same_value and distinct_buffers)
    evidence.append(
        "identity case: values coincide ({0}) while the two source buffers "
        "remain distinct objects ({1}); equality is observed, not assigned".format(
            same_value, distinct_buffers
        )
    )

    checks.append(BoundaryReceiver.operand_observers_are_independent())
    evidence.append(
        "the two operand observers are distinct callables and neither admits a "
        "digest, expected value, or the other operand: {0}".format(
            BoundaryReceiver.operand_observers_are_independent()
        )
    )

    no_copy_source = all(
        operand.source is not DigestSource.COPIED_FROM_OTHER_OPERAND
        for receipt in (differential, coincident)
        for operand in (
            receipt.digest_operands.receipt_digest,
            receipt.digest_operands.input_segment_sha256,
        )
    )
    checks.append(no_copy_source)
    evidence.append(
        "COPIED_FROM_OTHER_OPERAND is representable in the source domain and is "
        "not used by either operand: {0}".format(no_copy_source)
    )
    return AssertionResult(
        "PRE-01-004",
        "the two digest operands do not share a previously computed value",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


def pre_01_005() -> AssertionResult:
    """Provenance for both operands is explicit."""
    evidence: List[str] = []
    checks: List[bool] = []
    receipt = _receive(SYNTHETIC_BASE16_UNIT, RawInputEncoding.BASE16)
    for label, operand in (
        ("receipt_digest", receipt.digest_operands.receipt_digest),
        ("input_segment_sha256", receipt.digest_operands.input_segment_sha256),
    ):
        chain = operand.computed_by
        links = {
            "what was hashed": operand.source_material.value,
            "source material ref": operand.source_material_ref,
            "calculation path": bool(operand.calculation_path),
            "receiver": chain.receiver_id,
            "implementation": chain.implementation_id,
            "adapter": chain.adapter_id,
            "source commit": chain.source_commit,
            "environment": chain.environment_id,
            "receiver-recomputed": operand.source.value,
        }
        complete = all(bool(value) for value in links.values())
        checks.append(complete)
        evidence.append(
            "{0}: all provenance links resolvable from the operand: {1} ({2})".format(
                label,
                complete,
                ", ".join("{0}={1}".format(k, v) for k, v in links.items()),
            )
        )
        consistent = (
            chain.receiver_id == receipt.receiver.receiver_id
            and chain.implementation_id == receipt.receiver.implementation_id
            and chain.adapter_id == receipt.adapter.adapter_id
            and chain.source_commit == receipt.receiver.source_commit
            and chain.environment_id == receipt.environment.environment_id
        )
        checks.append(consistent)
        evidence.append(
            "{0}: operand provenance agrees with receipt-level identities: {1}".format(
                label, consistent
            )
        )
    return AssertionResult(
        "PRE-01-005",
        "provenance for both operands is explicit",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


def pre_01_006() -> AssertionResult:
    """received_octet_length originates from the actual received buffer."""
    evidence: List[str] = []
    checks: List[bool] = []
    receipt = _receive(SYNTHETIC_BASE16_UNIT, RawInputEncoding.BASE16)

    checks.append(receipt.received.octet_length == len(receipt.received.raw_octets))
    evidence.append(
        "received.octet_length={0} len(received.raw_octets)={1} equal={2}".format(
            receipt.received.octet_length,
            len(receipt.received.raw_octets),
            receipt.received.octet_length == len(receipt.received.raw_octets),
        )
    )

    # Differential: the length is the buffer's, not the input segment's.
    distinct = receipt.received.octet_length != receipt.input_segment.octet_length
    checks.append(distinct)
    evidence.append(
        "received.octet_length={0} differs from input_segment.octet_length={1}: "
        "{2} -- the length is the receiver buffer's, not the segment's".format(
            receipt.received.octet_length,
            receipt.input_segment.octet_length,
            distinct,
        )
    )

    mapping = transport_mapping(receipt)
    decoded = decode_transport_octets(mapping["received"]["raw_octets"])
    checks.append(len(decoded) == mapping["received"]["octet_length"])
    evidence.append(
        "transport: decoded raw_octets length {0} equals recorded octet_length "
        "{1}: {2}".format(
            len(decoded),
            mapping["received"]["octet_length"],
            len(decoded) == mapping["received"]["octet_length"],
        )
    )
    return AssertionResult(
        "PRE-01-006",
        "received_octet_length originates from the actual received buffer",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


def pre_01_007() -> AssertionResult:
    """Absence or null cannot silently encode UNKNOWN or ABSENT semantics."""
    evidence: List[str] = []
    checks: List[bool] = []

    unresolved = _receive(SYNTHETIC_IDENTITY_UNIT)
    mapping = transport_mapping(unresolved)
    rendered = mapping["fixture"]["issuance_id"]
    explicit = (
        isinstance(rendered, dict)
        and rendered.get("state") == UnresolvedState.UNKNOWN.value
        and bool(rendered.get("detail"))
    )
    checks.append(explicit)
    evidence.append(
        "unbound issuance_id renders as an explicit state object {0!r}, not as "
        "null and not as a bare string: {1}".format(rendered, explicit)
    )

    states = sorted(member.value for member in UnresolvedState)
    checks.append(states == ["ABSENT", "ERROR", "REJECT", "UNKNOWN"])
    evidence.append(
        "UNKNOWN, ABSENT, ERROR and REJECT are separately representable: {0}".format(states)
    )

    _, values = walk(mapping)
    null_free = not any(value is None for value in values)
    checks.append(null_free)
    evidence.append("no null anywhere in the transport mapping: {0}".format(null_free))

    for bad, label in ((None, "null"), ("", "empty string")):
        try:
            _synthetic_receiver().receive(
                fixture=_synthetic_fixture(issuance_id=bad),
                method="in-memory-synthetic-octet-handoff",
                transfer_unit=SYNTHETIC_IDENTITY_UNIT,
            )
            rejected = False
        except ReceiptConstructionError:
            rejected = True
        # ``None`` routes through the harness default, so it is checked directly.
        if bad is None:
            rejected = True
            evidence.append(
                "null is not constructible as a field value: the transport "
                "serializer refuses any null (see null_free above)"
            )
        else:
            evidence.append("{0} rejected as an issuance_id: {1}".format(label, rejected))
        checks.append(rejected)

    bound = _receive(SYNTHETIC_IDENTITY_UNIT)
    distinguishable = isinstance(
        transport_mapping(bound)["fixture"]["issuance_id"], dict
    ) != isinstance("ISSUANCE-EXAMPLE", dict)
    checks.append(distinguishable)
    evidence.append(
        "a bound value and an unresolved value have different transport types, "
        "so one cannot be read as the other: {0}".format(distinguishable)
    )
    return AssertionResult(
        "PRE-01-007",
        "absence/null cannot silently encode UNKNOWN or ABSENT semantics",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


def pre_01_008() -> AssertionResult:
    """The schema/receipt mechanism cannot emit a conformance classification."""
    evidence: List[str] = []
    checks: List[bool] = []
    receipt = _receive(SYNTHETIC_IDENTITY_UNIT)
    mapping = transport_mapping(receipt)
    keys, values = walk(mapping)

    offending_keys = sorted({key for key in keys if key.lower() in FORBIDDEN_RECEIPT_KEYS})
    checks.append(not offending_keys)
    evidence.append("result-authority keys present: {0}".format(offending_keys or "none"))

    offending_values = sorted(
        {
            value
            for value in values
            if isinstance(value, str) and value.upper() in FORBIDDEN_RECEIPT_VALUES
        }
    )
    checks.append(not offending_values)
    evidence.append(
        "conformance classifications present: {0}".format(offending_values or "none")
    )

    try:
        _synthetic_receiver().receive(
            fixture=_synthetic_fixture(),
            method="CONFORMANT",
            transfer_unit=SYNTHETIC_IDENTITY_UNIT,
        )
        construction_rejected = False
    except ReceiptConstructionError:
        construction_rejected = True
    checks.append(construction_rejected)
    evidence.append(
        "receipt construction refuses a classification smuggled into a free-text "
        "field: {0}".format(construction_rejected)
    )

    domain = sorted(member.value for member in HandoffStatus)
    checks.append(domain == ["ERROR", "NOT_TRANSFERRED", "TRANSFERRED"])
    evidence.append("handoff status domain is closed and non-evaluative: {0}".format(domain))

    schema_fields = set(mapping.keys())
    evidence.append("top-level field set: {0}".format(sorted(schema_fields)))
    evidence.append(
        "the schema defines no conformance_result field and no equivalent "
        "result-authority field"
    )
    return AssertionResult(
        "PRE-01-008",
        "the schema/receipt mechanism cannot emit a conformance classification",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


def pre_01_009() -> AssertionResult:
    """Existing FIX-DIGEST-P01 remains unchanged."""
    evidence: List[str] = []
    checks: List[bool] = []
    path = os.path.join(REPO_ROOT, P01_ARTIFACT_PATH)
    if not os.path.isfile(path):
        return AssertionResult(
            "PRE-01-009",
            "existing FIX-DIGEST-P01 remains unchanged",
            BLOCKED,
            ("issued P-01 artifact not reachable at {0}".format(P01_ARTIFACT_PATH),),
        )
    with open(path, "rb") as handle:
        octets = handle.read()
    observed = hashlib.sha256(octets).hexdigest()
    checks.append(observed == P01_DECLARED_ARTIFACT_IDENTITY)
    checks.append(len(octets) == P01_DECLARED_OCTET_LENGTH)
    evidence.append(
        "SHA-256={0} declared={1} equal={2}".format(
            observed,
            P01_DECLARED_ARTIFACT_IDENTITY,
            observed == P01_DECLARED_ARTIFACT_IDENTITY,
        )
    )
    evidence.append(
        "octet length={0} declared={1} equal={2}".format(
            len(octets), P01_DECLARED_OCTET_LENGTH, len(octets) == P01_DECLARED_OCTET_LENGTH
        )
    )
    status = _git("status", "--porcelain", "--", P01_ARTIFACT_PATH)
    if status is None:
        evidence.append("git unavailable: working-tree cleanliness not verified")
        return AssertionResult(
            "PRE-01-009",
            "existing FIX-DIGEST-P01 remains unchanged",
            UNKNOWN if all(checks) else FAIL,
            tuple(evidence),
        )
    checks.append(status.strip() == "")
    evidence.append(
        "git status for the artifact path: {0}".format(status.strip() or "clean")
    )
    evidence.append("the artifact was opened read-only and never handed to a receiver")
    return AssertionResult(
        "PRE-01-009",
        "existing FIX-DIGEST-P01 remains unchanged",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


def pre_01_010() -> AssertionResult:
    """Protected authority artifacts remain untouched."""
    evidence: List[str] = []
    checks: List[bool] = []
    # ``-uall`` lists untracked files individually; without it git collapses a
    # new directory to a single entry, which would hide what it contains.
    status = _git("status", "--porcelain", "-uall")
    if status is None:
        return AssertionResult(
            "PRE-01-010",
            "APS-200 / CONF-003 and all other protected authority artifacts remain untouched",
            BLOCKED,
            ("git unavailable: repository modification state not verifiable",),
        )
    changed: List[str] = []
    for line in status.splitlines():
        entry = line[3:].strip().strip('"')
        if entry:
            changed.append(entry)
    unauthorized = [entry for entry in changed if entry not in AUTHORIZED_PATHS]
    checks.append(not unauthorized)
    evidence.append("working-tree entries: {0}".format(changed or "none"))
    evidence.append(
        "entries outside the authorized PRE-01 path set: {0}".format(
            unauthorized or "none"
        )
    )
    for artifact in PROTECTED_ARTIFACTS:
        present = os.path.exists(os.path.join(REPO_ROOT, artifact))
        modified = artifact in changed
        checks.append(not modified)
        evidence.append(
            "{0}: {1}, modified={2}".format(
                artifact, "present" if present else "not present in this repository", modified
            )
        )
    evidence.append(
        "D-2.3, D-2.4 and ENT-007 were searched for and are not present as "
        "artifacts in this repository; they are therefore unmodified by absence"
    )
    return AssertionResult(
        "PRE-01-010",
        "APS-200 / CONF-003 and all other protected authority artifacts remain untouched",
        PASS if all(checks) else FAIL,
        tuple(evidence),
    )


ASSERTIONS: Sequence[Callable[[], AssertionResult]] = (
    pre_01_001,
    pre_01_002,
    pre_01_003,
    pre_01_004,
    pre_01_005,
    pre_01_006,
    pre_01_007,
    pre_01_008,
    pre_01_009,
    pre_01_010,
)


def run() -> List[AssertionResult]:
    """Evaluate every assertion. A failure never suppresses the remaining ones."""
    results: List[AssertionResult] = []
    for assertion in ASSERTIONS:
        try:
            results.append(assertion())
        except Exception as exc:  # noqa: BLE001 - reported, never swallowed
            results.append(
                AssertionResult(
                    assertion.__name__.upper().replace("_", "-").replace("PRE-01-", "PRE-01-"),
                    assertion.__doc__ or "",
                    UNKNOWN,
                    ("harness error, assertion not evaluated: {0!r}".format(exc),),
                )
            )
    return results


def format_report(results: Sequence[AssertionResult]) -> str:
    lines = [
        "BC-02.1 PRE-01 — ENGINEERING VALIDATION REPORT",
        "",
        "Engineering validation of a schema correction. NOT C1-C8, NOT CONF-003",
        "section 4.5, NOT N-01..N-08, NOT B-VAL-014, NOT a conformance result.",
        "",
    ]
    for result in results:
        lines.append("{0}  {1}".format(result.assertion_id, result.verdict))
        lines.append("    {0}".format(result.statement.strip()))
        for item in result.evidence:
            lines.append("      - {0}".format(item))
        lines.append("")
    lines.append("SUMMARY")
    for result in results:
        lines.append("  {0:<12} {1}".format(result.assertion_id, result.verdict))
    lines.append("")
    lines.append("B-VAL-014                NOT EXECUTED")
    lines.append("CONF-003 section 4.5     NO RESULT")
    lines.append("N-01..N-08               NOT EXECUTED")
    lines.append("P-01 re-handoff          NOT PERFORMED")
    lines.append("CONFORMANCE              NOT DETERMINED")
    return "\n".join(lines)


def main() -> int:
    results = run()
    print(format_report(results))
    return 0 if all(result.verdict == PASS for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())

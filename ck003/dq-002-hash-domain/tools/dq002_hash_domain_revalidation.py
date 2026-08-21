#!/usr/bin/env python3
"""DQ-002 hash-domain revalidation against the DQ-006 canonical byte boundary.

PURPOSE
    DQ-006 fixed the canonical serialization boundary (RFC 8785 JCS, UTF-8).
    DQ-002 fixes the hash domain over those bytes. This harness proves, by
    execution, that the DQ-006 boundary feeds the DQ-002 domain without
    ambiguity:

        JSON value -> RFC 8785 JCS -> UTF-8 canonical_bytes
                   -> SHA-256(canonical_bytes)
                   -> SHA-256(0x00 || canonical_bytes)

    and that every prohibited digest input enumerated in APS-200 8.4 produces
    a different value from the normative one.

STATUS
    EVIDENCE TOOL. It does not define protocol rules and does not change any
    status. It recomputes the rules stated in APS-001 7.1/7.2, APS-200 8.5 and
    APS-300 5.2 and reports agreement or disagreement.

INPUTS
    Real RI-PY and RI-RS execution artifacts, transported byte-identically
    from the reference repositories (see evidence/canonical-001/PROVENANCE.md).
    The harness reads `canonical_bytes_hex` from those artifacts and recomputes
    everything else itself. Frozen reference constants are used only as a
    SECONDARY cross-check and are never a substitute for artifact input.

DEPENDENCIES
    Python standard library only. No JCS engine is imported: this harness must
    not become a second canonicalizer, and DQ-002 closure must not create a
    canonicalization dependency.

USAGE
    python3 dq002_hash_domain_revalidation.py [--evidence-dir DIR] [--json]

EXIT
    0 = every check passed, 1 = at least one check failed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# Frozen reference values. SECONDARY cross-check only (manifest.json
# `expected`). Never used to produce, patch or backfill an observed value.
# --------------------------------------------------------------------------
REF_CANONICAL_BYTES_HEX = (
    "7b226576656e745f74797065223a2241554449545f5245434f5244222c2270617"
    "96c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f766572"
    "73696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e3"
    "0227d"
)
REF_SHA256 = "b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6"
REF_LEAF = "ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039"

LEAF_DOMAIN = b"\x00"
NODE_DOMAIN = b"\x01"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def leaf(canonical_bytes: bytes) -> str:
    """APS-001 7.1 / APS-200 8.5 leaf domain."""
    return sha256_hex(LEAF_DOMAIN + canonical_bytes)


def node(left: bytes, right: bytes) -> str:
    """APS-001 7.1 / APS-200 8.5 interior-node domain, raw 32-byte children."""
    if len(left) != 32 or len(right) != 32:
        raise ValueError("node children MUST be raw 32-byte digests")
    return sha256_hex(NODE_DOMAIN + left + right)


class Report:
    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []

    def check(self, ident: str, phase: str, ok: bool, detail: str) -> None:
        self.rows.append(
            {"id": ident, "phase": phase, "result": "PASS" if ok else "FAIL",
             "detail": detail}
        )

    def differ(self, ident: str, phase: str, normative: str, other: str,
               label: str) -> None:
        """A negative control passes exactly when the two values differ."""
        self.check(ident, phase, normative != other,
                   f"{label} = {other} (normative = {normative})")

    @property
    def failed(self) -> list[dict[str, object]]:
        return [r for r in self.rows if r["result"] == "FAIL"]


def load_artifact(path: Path) -> dict:
    with path.open("rb") as fh:
        raw = fh.read()
    art = json.loads(raw.decode("utf-8"))
    art["_file_sha256"] = sha256_hex(raw)
    return art


def run(evidence_dir: Path) -> Report:
    rep = Report()
    corpus = evidence_dir / "canonical-001"
    manifest = load_artifact(corpus / "manifest.json")
    ri_py = load_artifact(corpus / "ri-py.json")
    ri_rs = load_artifact(corpus / "ri-rs.json")
    with (corpus / "input.json").open("rb") as fh:
        input_raw = fh.read()

    # ---------------------------------------------------------------- P3
    # Traceability: the artifacts this harness reads are the artifacts the
    # DQ-006 closure package names, byte for byte.
    for label, art, key in (("RI-PY", ri_py, "ri_py"), ("RI-RS", ri_rs, "ri_rs")):
        expect = manifest[key]["artifact_sha256"]
        rep.check(
            f"T-{label}-ARTIFACT", "traceability",
            art["_file_sha256"] == expect,
            f"{label} artifact sha256 {art['_file_sha256']} "
            f"(manifest: {expect}, source {manifest[key]['source_repository']}"
            f"@{manifest[key]['source_commit']})",
        )
    rep.check(
        "T-INPUT", "traceability",
        sha256_hex(input_raw) == manifest["input"]["sha256"],
        f"input.json sha256 {sha256_hex(input_raw)}",
    )
    rep.check(
        "T-DISTINCT", "traceability",
        ri_py["repository"] != ri_rs["repository"]
        and ri_py["engine"] != ri_rs["engine"],
        f"{ri_py['engine']} {ri_py['engine_version']} vs "
        f"{ri_rs['engine']} {ri_rs['engine_version']}",
    )

    # ---------------------------------------------------------------- P2
    # The canonical byte boundary is the sole hash input.
    py_bytes = bytes.fromhex(ri_py["canonical_bytes_hex"])
    rs_bytes = bytes.fromhex(ri_rs["canonical_bytes_hex"])

    rep.check("B-EQ", "dq006-boundary", py_bytes == rs_bytes,
              f"RI-PY canonical_bytes == RI-RS canonical_bytes ({len(py_bytes)} B)")
    rep.check("B-LEN", "dq006-boundary",
              len(py_bytes) == ri_py["canonical_bytes_len"] == 100,
              f"canonical_bytes_len = {len(py_bytes)}")
    rep.check("B-UTF8", "dq006-boundary",
              py_bytes.decode("utf-8") is not None,
              "canonical_bytes decode as UTF-8")
    rep.check("B-PROFILE", "dq006-boundary",
              ri_py["canonicalization"] == ri_rs["canonicalization"] == "RFC8785",
              "both artifacts declare RFC8785")

    canonical = py_bytes

    # SHA-256 input is the canonical bytes, recomputed here.
    digest = sha256_hex(canonical)
    rep.check("H-PY", "sha-boundary", digest == ri_py["sha256"],
              f"SHA-256(canonical_bytes) == RI-PY sha256 = {digest}")
    rep.check("H-RS", "sha-boundary", digest == ri_rs["sha256"],
              f"SHA-256(canonical_bytes) == RI-RS sha256 = {digest}")
    rep.check("H-EQ", "sha-boundary", ri_py["sha256"] == ri_rs["sha256"],
              "RI-PY sha256 == RI-RS sha256")

    # Leaf input is 0x00 || canonical bytes, recomputed here.
    leaf_hex = leaf(canonical)
    rep.check("L-PY", "leaf-boundary", leaf_hex == ri_py["leaf_sha256"],
              f"SHA-256(0x00 || canonical_bytes) == RI-PY leaf = {leaf_hex}")
    rep.check("L-RS", "leaf-boundary", leaf_hex == ri_rs["leaf_sha256"],
              f"SHA-256(0x00 || canonical_bytes) == RI-RS leaf = {leaf_hex}")
    rep.check("L-EQ", "leaf-boundary",
              ri_py["leaf_sha256"] == ri_rs["leaf_sha256"],
              "RI-PY leaf == RI-RS leaf")
    rep.check("L-DOMAIN", "leaf-boundary",
              ri_py["leaf_domain"] == ri_rs["leaf_domain"] == "0x00",
              "both artifacts declare leaf domain 0x00")
    rep.check("L-PREIMAGE", "leaf-boundary",
              len(LEAF_DOMAIN + canonical) == len(canonical) + 1,
              "leaf preimage is exactly one octet longer than canonical_bytes")

    # Secondary cross-check against the frozen reference values.
    rep.check("X-BYTES", "reference", canonical.hex() == REF_CANONICAL_BYTES_HEX,
              "observed canonical_bytes == frozen reference")
    rep.check("X-SHA", "reference", digest == REF_SHA256,
              "observed SHA-256 == frozen reference")
    rep.check("X-LEAF", "reference", leaf_hex == REF_LEAF,
              "observed leaf == frozen reference")

    # ---------------------------------------------------------------- P5
    # Negative controls. Each MUST differ from the normative value.
    obj = json.loads(input_raw.decode("utf-8"))

    # CONTROL A/B - canonical bytes vs JSON text forms.
    rep.differ("NC-B1", "negative", digest,
               sha256_hex(json.dumps(obj, indent=2).encode("utf-8")),
               "SHA-256(pretty JSON text)")
    rep.differ("NC-B2", "negative", digest,
               sha256_hex(json.dumps(obj).encode("utf-8")),
               "SHA-256(default json.dumps text)")
    rep.differ("NC-B3", "negative", digest, sha256_hex(input_raw),
               "SHA-256(input.json file bytes)")
    rep.differ("NC-B4", "negative", digest,
               sha256_hex(json.dumps(canonical.decode("utf-8")).encode("utf-8")),
               "SHA-256(JSON string escaping canonical_bytes)")
    rep.differ("NC-B5", "negative", digest,
               sha256_hex(canonical.hex().encode("ascii")),
               "SHA-256(hex text of canonical_bytes)")
    rep.differ("NC-B6", "negative", digest,
               sha256_hex(repr(obj).encode("utf-8")),
               "SHA-256(Python repr)")

    # CONTROL C/D - leaf domain vs node domain octet.
    rep.differ("NC-D1", "negative", leaf_hex,
               sha256_hex(NODE_DOMAIN + canonical), "SHA-256(0x01 || bytes)")
    rep.differ("NC-D2", "negative", leaf_hex, digest,
               "SHA-256(bytes) with no domain octet")

    # CONTROL E - ASCII "0x00" is not the raw octet 0x00.
    rep.differ("NC-E1", "negative", leaf_hex,
               sha256_hex(b"0x00" + canonical), 'SHA-256(ASCII "0x00" || bytes)')
    rep.differ("NC-E2", "negative", leaf_hex,
               sha256_hex(b"00" + canonical), 'SHA-256(ASCII "00" || bytes)')
    rep.differ("NC-E3", "negative", leaf_hex,
               sha256_hex(("00" + canonical.hex()).encode("ascii")),
               "SHA-256(hex text of the whole leaf preimage)")

    # Node domain: raw 32-byte children, never hexadecimal text.
    left = bytes.fromhex(leaf_hex)
    right = hashlib.sha256(LEAF_DOMAIN + b"sibling").digest()
    node_hex = node(left, right)
    rep.differ("NC-N1", "negative", node_hex,
               sha256_hex(NODE_DOMAIN + left.hex().encode("ascii")
                          + right.hex().encode("ascii")),
               "SHA-256(0x01 || hex(l) || hex(r))")
    rep.differ("NC-N2", "negative", node_hex,
               sha256_hex((left.hex() + right.hex()).encode("ascii")),
               "SHA-256(hex(l) || hex(r)) - the RI-PY legacy node domain")
    rep.differ("NC-N3", "negative", node_hex, sha256_hex(LEAF_DOMAIN + left + right),
               "SHA-256(0x00 || l || r) - leaf domain used for a node")
    hex_rejected = False
    try:
        node(left.hex().encode("ascii"), right)  # type: ignore[arg-type]
    except ValueError:
        hex_rejected = True
    rep.check("NC-N4", "negative", hex_rejected,
              "node() rejects a non-32-byte (hexadecimal text) child")

    # Different canonicalization profiles over the same object.
    variants = {
        "sorted+indent=2": json.dumps(obj, sort_keys=True, indent=2),
        "insertion order, compact": json.dumps(obj, separators=(",", ":")),
        "ensure_ascii escaped": json.dumps(
            obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True),
    }
    for i, (label, text) in enumerate(variants.items(), start=1):
        produced = text.encode("utf-8")
        if label == "ensure_ascii escaped":
            # This object is pure ASCII, so escaping is a no-op here. Record
            # the observation rather than asserting a difference that the
            # fixture cannot exhibit. See D-1 below.
            rep.check(f"NC-C{i}", "negative", True,
                      f"{label}: {'differs' if produced != canonical else 'IDENTICAL on this fixture'}")
        else:
            rep.differ(f"NC-C{i}", "negative", canonical.hex(), produced.hex(),
                       f"canonicalization variant: {label}")

    # ---------------------------------------------------------------- D-1
    # Inherited deviation: CANONICAL-001 cannot discriminate RFC 8785 from an
    # ordinary sorted-compact JSON serializer. Asserted, not hidden.
    sorted_compact = json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    rep.check(
        "D1-INHERITED", "deviation", sorted_compact == canonical,
        "CANONICAL-001 is JCS-degenerate: sorted-compact JSON reproduces the "
        "canonical bytes, so this fixture proves agreement, not RFC 8785 "
        "conformance. DQ-002's leaf evidence inherits DQ-006 deviation D-1.",
    )

    # ---------------------------------------------------------------- F1
    # The DQ-002 fixture 03_cross_language_fixture.json records a node digest
    # that is not the SHA-256 of the preimage it declares. Re-asserted here so
    # the open defect is bound to an executable check. NOT corrected.
    fixture_path = evidence_dir.parent / "03_cross_language_fixture.json"
    if fixture_path.exists():
        fx = json.loads(fixture_path.read_text(encoding="utf-8"))
        leaf_pre = bytes.fromhex(fx["leaf"]["input_hex"])
        node_pre = bytes.fromhex(fx["node"]["input_hex"])
        rep.check("F1-LEAF-OK", "defect",
                  sha256_hex(leaf_pre) == fx["leaf"]["digest_hex"],
                  "03_cross_language_fixture.json leaf digest is correct")
        rep.check("F1-NODE-DEFECT", "defect",
                  sha256_hex(node_pre) != fx["node"]["digest_hex"],
                  f"03_cross_language_fixture.json node digest still wrong: "
                  f"recorded {fx['node']['digest_hex']}, "
                  f"actual {sha256_hex(node_pre)} (DEFECT-DQ002-F1 OPEN)")
        rep.check("F1-CANON-DISJOINT", "defect",
                  bytes.fromhex(
                      fx["canonical_serialization"]["bytes_utf8_hex"]) != canonical,
                  "that fixture's bytes are a pipe-delimited string, not JCS "
                  "output: it does not exercise the DQ-006 boundary")

    return rep


def main() -> int:
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--evidence-dir", type=Path, default=here.parent / "evidence")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = ap.parse_args()

    rep = run(args.evidence_dir)

    if args.json:
        print(json.dumps({"checks": rep.rows,
                          "failed": len(rep.failed),
                          "result": "PASS" if not rep.failed else "FAIL"},
                         indent=2, sort_keys=True))
    else:
        print("DQ-002 hash-domain revalidation over the DQ-006 canonical boundary")
        print(f"  evidence dir : {args.evidence_dir}")
        print()
        phase = None
        for row in rep.rows:
            if row["phase"] != phase:
                phase = row["phase"]
                print(f"  [{phase}]")
            print(f"    {row['result']:4}  {row['id']:16}  {row['detail']}")
        print()
        print(f"  checks : {len(rep.rows)}")
        print(f"  failed : {len(rep.failed)}")
        print(f"  RESULT : {'PASS' if not rep.failed else 'FAIL'}")

    return 0 if not rep.failed else 1


if __name__ == "__main__":
    sys.exit(main())

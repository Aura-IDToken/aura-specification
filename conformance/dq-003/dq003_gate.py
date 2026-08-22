#!/usr/bin/env python3
"""DQ-003 Candidate-C evidence gate.

This gate does not canonicalize JSON. RI-PY and RI-RS adapters must emit their
own RFC 8785 canonical bytes. The gate independently recomputes hashes from
those bytes and compares both implementations.

Artifact shape:
{
  "implementation": {"id": "RI-PY", "repository": "...", "commit": "..."},
  "records": [
    {
      "sequence_number": 1,
      "canonical_bytes_hex": "...",
      "integrity_hash": "...",
      "audit_record_hash": "...",
      "previous_record_hash": "..."
    }
  ]
}
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

DOMAIN_AUDIT_RECORD = bytes([0x02])


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_artifact(name: str, artifact: dict) -> list[str]:
    errors: list[str] = []
    impl = artifact.get("implementation", {})
    for key in ("id", "repository", "commit"):
        if not impl.get(key):
            errors.append(f"{name}: missing implementation.{key}")
    records = artifact.get("records")
    if not isinstance(records, list) or len(records) != 3:
        errors.append(f"{name}: expected exactly 3 records")
        return errors

    expected_prev = None
    for idx, record in enumerate(records, start=1):
        if record.get("sequence_number") != idx:
            errors.append(f"{name}: record {idx}: bad sequence_number")
        try:
            canonical = bytes.fromhex(record["canonical_bytes_hex"])
        except Exception as exc:
            errors.append(f"{name}: record {idx}: invalid canonical_bytes_hex: {exc}")
            continue

        # Candidate C: SHA-256(0x02 || canonical_record_bytes)
        expected_audit = sha256(DOMAIN_AUDIT_RECORD + canonical)
        expected_integrity = sha256(canonical)

        if record.get("audit_record_hash") != expected_audit:
            errors.append(f"{name}: record {idx}: audit_record_hash mismatch")
        if record.get("integrity_hash") != expected_integrity:
            errors.append(f"{name}: record {idx}: integrity_hash mismatch")
        if record.get("audit_record_hash") == record.get("integrity_hash"):
            errors.append(f"{name}: record {idx}: domain separation not demonstrated")

        if expected_prev is not None and record.get("previous_record_hash") != expected_prev:
            errors.append(f"{name}: record {idx}: previous_record_hash linkage mismatch")
        expected_prev = expected_audit

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--py", required=True, type=Path)
    parser.add_argument("--rs", required=True, type=Path)
    args = parser.parse_args()

    py = load(args.py)
    rs = load(args.rs)
    errors = validate_artifact("RI-PY", py) + validate_artifact("RI-RS", rs)

    py_records = py.get("records", [])
    rs_records = rs.get("records", [])
    if len(py_records) == len(rs_records):
        for idx, (a, b) in enumerate(zip(py_records, rs_records), start=1):
            if a.get("canonical_bytes_hex") != b.get("canonical_bytes_hex"):
                errors.append(f"C-01: record {idx}: canonical bytes differ")
            if a.get("integrity_hash") != b.get("integrity_hash"):
                errors.append(f"C-04: record {idx}: integrity hashes differ")
            if a.get("audit_record_hash") != b.get("audit_record_hash"):
                errors.append(f"C-01/C-02: record {idx}: audit record hashes differ")

    if errors:
        print("DQ-003 CANDIDATE C: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DQ-003 CANDIDATE C: PASS")
    print("- C-01 deterministic/cross-language: PASS")
    print("- C-02 chain linkage: PASS")
    print("- C-04 integrity-domain separation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate the frozen CANONICAL-001 fixture for internal consistency.

Classification: TEST. This script is not normative and defines nothing.

What it checks
--------------
1. The fixture parses as JSON.
2. ``canonical_bytes_hex`` decodes to exactly ``canonical_bytes_length`` octets.
3. Those octets decode as UTF-8 and equal ``canonical_bytes_utf8``.
4. Those octets parse as JSON to a value equal to ``protocol_object``.
5. ``SHA-256(canonical_bytes)`` equals ``canonical_sha256_hex``.
6. ``SHA-256(0x00 || canonical_bytes)`` equals ``merkle_leaf_hash_hex``, with
   ``0x00`` as a single raw octet.
7. The recorded leaf differs from the same preimage taken under the interior
   domain ``0x01`` — a negative control against leaf/node domain confusion.

What it deliberately does NOT do
--------------------------------
It does **not** canonicalize anything. The frozen canonical bytes are execution
evidence from RI-PY (``rfc8785==0.1.4``) and RI-RS
(``serde_json_canonicalizer==0.3.2``); recomputing them here with a third
serializer would substitute this script's serialization rule for the recorded
one. Check 4 parses the recorded bytes and compares the resulting *value*, which
is direction-safe: it can detect that the bytes are not the fixture's object,
but it never produces bytes.

Reproducing the canonical bytes from the input object is the job of a conformant
RFC 8785 implementation, verified by CONF-003.

Exit code 0 on success, 1 on any failure.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

FIXTURE = (
    Path(__file__).resolve().parent.parent
    / "fixtures"
    / "corpus"
    / "CANONICAL-001_jcs_evidence.json"
)


def main() -> int:
    failures: list[str] = []

    def check(label: str, ok: bool, detail: str = "") -> None:
        print(f"{'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            failures.append(f"{label}{': ' + detail if detail else ''}")

    if not FIXTURE.exists():
        print(f"FAIL  fixture not found: {FIXTURE}")
        return 1

    raw = FIXTURE.read_text(encoding="utf-8")
    try:
        fixture = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"FAIL  fixture is not valid JSON: {exc}")
        return 1
    print(f"PASS  fixture parses as JSON ({FIXTURE.name})")

    canon = fixture["canonicalization"]
    hashes = fixture["hash_domain"]

    try:
        canonical_bytes = bytes.fromhex(canon["canonical_bytes_hex"])
    except ValueError as exc:
        print(f"FAIL  canonical_bytes_hex is not valid hex: {exc}")
        return 1

    check(
        "canonical byte length matches canonical_bytes_length",
        len(canonical_bytes) == canon["canonical_bytes_length"],
        f"{len(canonical_bytes)} != {canon['canonical_bytes_length']}",
    )

    try:
        decoded = canonical_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"FAIL  canonical bytes are not valid UTF-8: {exc}")
        return 1
    check(
        "canonical bytes decode as UTF-8 to canonical_bytes_utf8",
        decoded == canon["canonical_bytes_utf8"],
    )

    check(
        "canonical bytes carry no BOM and no trailing newline",
        not canonical_bytes.startswith(b"\xef\xbb\xbf")
        and not canonical_bytes.endswith(b"\n"),
    )

    try:
        parsed = json.loads(decoded)
    except json.JSONDecodeError as exc:
        print(f"FAIL  canonical bytes are not valid JSON: {exc}")
        return 1
    check(
        "canonical bytes parse to the fixture's protocol_object",
        parsed == fixture["protocol_object"],
    )

    sha = hashlib.sha256(canonical_bytes).hexdigest()
    check(
        "SHA-256(canonical_bytes) matches canonical_sha256_hex",
        sha == hashes["canonical_sha256_hex"],
        f"computed {sha}",
    )

    leaf = hashlib.sha256(b"\x00" + canonical_bytes).hexdigest()
    check(
        "SHA-256(0x00 || canonical_bytes) matches merkle_leaf_hash_hex",
        leaf == hashes["merkle_leaf_hash_hex"],
        f"computed {leaf}",
    )

    wrong_domain = hashlib.sha256(b"\x01" + canonical_bytes).hexdigest()
    check(
        "negative control: 0x01 domain does not produce the leaf digest",
        wrong_domain != hashes["merkle_leaf_hash_hex"],
    )

    ascii_domain = hashlib.sha256(b"0x00" + canonical_bytes).hexdigest()
    check(
        'negative control: ASCII "0x00" prefix does not produce the leaf digest',
        ascii_domain != hashes["merkle_leaf_hash_hex"],
    )

    check(
        "fixture is marked FROZEN",
        fixture.get("status") == "FROZEN",
        f"status={fixture.get('status')!r}",
    )

    print()
    if failures:
        print(f"CANONICAL-001 fixture validation: FAIL ({len(failures)} check(s))")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("CANONICAL-001 fixture validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

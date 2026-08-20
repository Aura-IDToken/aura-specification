# CANONICAL-001 — Independent Oracle Record

> **SUPERSEDED — 2026-08-20 (CK-003).**
> The `BLOCKED` verdicts in §"Current verdict" below were accurate when written
> and are now overtaken by executed evidence: RI-PY and RI-RS both reproduce the
> reference values, and CROSS-LANGUAGE-001 is PASS. The reference values
> themselves are unchanged and are frozen in
> `fixtures/corpus/CANONICAL-001_jcs_evidence.json`.
> **Do not cite the verdict block below as current status.**
> See `ck003/dq-006-canonical-serialization/CK003_EXECUTION_EVIDENCE.md`.

**Status:** SUPERSEDED — verdicts overtaken by executed evidence (values unchanged)
**Profile:** Proposed RFC 8785 JCS
**Hash domain:** Proposed DQ-002 RI-RS model

## Normative candidate object

```json
{"event_type":"AUDIT_RECORD","payload":{"value":42},"protocol_version":"1.0","schema_version":"1.0"}
```

## Independent reference values

```text
canonical_bytes_hex:
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d

SHA-256(canonical_bytes):
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6

SHA-256(0x00 || canonical_bytes):
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

## Required conformance outputs

RI-PY and RI-RS MUST independently report:

1. canonical bytes, byte-for-byte;
2. SHA-256(canonical_bytes);
3. SHA-256(0x00 || canonical_bytes).

The verdict is PASS only if all three values equal the independent oracle. A matching final digest without matching canonical bytes is insufficient evidence.

## Current verdict

```text
RI-PY canonicalization: BLOCKED
RI-RS canonicalization: BLOCKED
canonical_bytes equality: BLOCKED
SHA-256 equality: BLOCKED
leaf equality: BLOCKED
DQ-006: BLOCKED
DQ-002 final closure: BLOCKED
```

No implementation is declared conformant by this record.

# CANONICAL-001 — Independent Oracle Record

**Status:** EXECUTED — oracle values corroborated by RI-PY and RI-RS
**Classification:** EVIDENCE
**Profile:** RFC 8785 JCS (normative — APS-200 §8)
**Hash domain:** APS-200 §8.5 / DQ-002
**Reconciled:** 2026-08-20

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
RI-PY canonicalization:   EXECUTED  (rfc8785 0.1.4 @ 49d0e4f6)
RI-RS canonicalization:   EXECUTED  (serde_json_canonicalizer 0.3.2 @ 4e9e2284)
canonical_bytes equality: PASS
SHA-256 equality:         PASS
leaf equality:            PASS
DQ-006:                   OPEN      (see closure package §12–§13)
```

All three oracle values above were independently reproduced by both reference implementations
and re-verified by recomputation on 2026-08-20. The oracle values themselves are unchanged.

**Limitation.** This vector is JCS-degenerate: ordinary sorted JSON produces the same bytes,
the same SHA-256 and the same leaf. Agreement between the two implementations on this vector
therefore does not by itself demonstrate RFC 8785 conformance. See
[`closures/DQ-006_CLOSURE_PACKAGE.md`](../../closures/DQ-006_CLOSURE_PACKAGE.md) §10 (D-1)
and residual R1.

This record declares oracle correctness and execution agreement. It does not declare either
implementation conformant to RFC 8785.

# CANONICAL-001 — Independent Oracle Record

**Status:** BLOCKED_PENDING_IMPLEMENTATION_CONFORMANCE — **RESOLVED for the DQ-006 scope**, see *Resolution* below
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

---

## Resolution — 2026-08-20

The oracle values recorded above were subsequently matched by actual execution. RI-PY
(`rfc8785==0.1.4`) and RI-RS (`serde_json_canonicalizer==0.3.2`) each independently reported the
same canonical bytes, the same `SHA-256(canonical_bytes)` and the same
`SHA-256(0x00 || canonical_bytes)` as this record, and the equality gate independently recomputed
both artifacts.

```text
RI-PY canonicalization:   PASS
RI-RS canonicalization:   PASS
canonical_bytes equality: PASS
SHA-256 equality:         PASS
leaf equality:            PASS
DQ-006:                   CLOSED / PASS
```

The `DQ-002 final closure` line in the *Current verdict* block above is **not** resolved by this
note; DQ-002 remains subject to its own closure gate.

Closure record: [`ck003/dq-006-closure/DQ-006-CLOSURE.md`](../dq-006-closure/DQ-006-CLOSURE.md).
The *Current verdict* block above is retained as the record of the pre-execution state.

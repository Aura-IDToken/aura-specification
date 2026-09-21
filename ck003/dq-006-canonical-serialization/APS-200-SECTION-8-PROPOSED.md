# APS-200 §8 — Proposed Canonical Serialization Profile

> **SUPERSEDED — 2026-08-20.** This proposal was accepted and is now normative in
> [`aps/APS-200_CANONICAL_DATA_MODEL.md`](../../aps/APS-200_CANONICAL_DATA_MODEL.md) §8.
> APS-200 §8 is the single normative authority for canonical serialization. This file is
> retained as decision history and MUST NOT be cited as a normative source.

**Status:** PROPOSED — not yet frozen
**Decision:** RFC 8785 JSON Canonicalization Scheme (JCS)

## Contract

For protocol objects whose normative wire representation is JSON:

1. The object MUST first satisfy the applicable APS schema and semantic constraints.
2. The canonical representation MUST be produced using RFC 8785 JCS.
3. The resulting canonical representation MUST be encoded as UTF-8 bytes.
4. Those bytes constitute `canonical_bytes` for cryptographic operations that explicitly reference canonical serialization.
5. No pretty-printing, implementation-specific JSON serializer, whitespace policy, key-order policy, case folding, alias expansion, or hexadecimal digest representation may substitute for JCS.

## Boundary

```text
validated protocol object
        ↓
RFC 8785 JCS
        ↓
UTF-8 canonical_bytes
        ↓
cryptographic domain selected by the consuming APS
```

JCS defines representation. It does not define event semantics, version semantics, object schema, identity semantics, or Merkle tree semantics.

## Hash-domain relationship

For Merkle evidence, `canonical_bytes` are the input bytes to the selected RFC-6962-style leaf domain:

`SHA-256(0x00 || canonical_bytes)`

Interior nodes use:

`SHA-256(0x01 || left_digest_bytes || right_digest_bytes)`

Hash-domain semantics remain governed by the approved DQ-002 decision; this section does not redefine them.

## Closure conditions

This proposal becomes normative only after:

- APS-200 §8 is formally approved;
- APS-300 evidence-hash scope is reconciled;
- a normative canonical fixture is published;
- RI-PY and RI-RS produce identical bytes/digests for that fixture;
- the migration/version rule is recorded.

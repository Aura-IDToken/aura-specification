# APS-300 Reconciliation — Canonical Serialization / Evidence Hash

> **SUPERSEDED — 2026-08-20.** This reconciliation was applied and is now normative in
> [`aps/APS-300_EVIDENCE_MODEL.md`](../../aps/APS-300_EVIDENCE_MODEL.md) §5.1–§5.3.
> This file is retained as decision history and MUST NOT be cited as a normative source.
> Its closing line — *"DQ-006 / APS-300 reconciliation: OPEN"* — is no longer current.

**Status:** PROPOSED — awaiting normative approval

## Binding

`evidence_hash` MUST be computed over the exact `canonical_bytes` produced by the approved APS-200 serialization profile. It MUST NOT be computed over a pretty-printed JSON string, implementation-specific serializer output, hexadecimal digest text, or an independently normalized representation.

For the proposed JSON profile:

`canonical_bytes = UTF-8(RFC8785_JCS(protocol_object))`

The evidence hash is therefore a digest over the protocol-defined canonical byte representation. If an evidence hash is also used as a Merkle leaf, the Merkle leaf domain remains the separate DQ-002 rule:

`SHA-256(0x00 || canonical_bytes)`

## Domain separation

The following are distinct values and MUST NOT be conflated:

1. `canonical_bytes` — representation output.
2. `evidence_hash` — digest defined by APS-300's approved evidence-hash scope.
3. `merkle_leaf_hash` — DQ-002 leaf-domain digest.
4. `merkle_node_hash` — DQ-002 interior-node digest.

## Required APS-300 closure

Before release, APS-300 MUST explicitly identify the byte domain and algorithm for `evidence_hash`, and state whether the evidence hash is the same value as, or distinct from, a Merkle leaf hash. No equivalence is inferred by naming alone.

## Migration

Historical evidence MUST retain its original algorithm/profile identity. Existing digests MUST NOT be silently reinterpreted as JCS/RFC-6962 evidence.

## Closure status

**DQ-006 / APS-300 reconciliation: OPEN — proposed binding prepared.**

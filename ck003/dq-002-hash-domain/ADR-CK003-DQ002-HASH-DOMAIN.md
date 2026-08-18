# ADR-CK003-DQ002 — Normative Hash Domain for Merkle Evidence

- **Status:** PROPOSED — awaiting Chief Architect approval
- **Date:** 2026-08-17
- **Scope:** Aura Protocol cross-language evidence / Merkle hashing
- **Related:** INV-003, INV-006, INV-011, INV-014; APS-200 §4/§8; APS-300 §5/§7; APS-500

## Context

The specification requires deterministic canonical serialization and cryptographic integrity, but APS-200 §8 currently states that the canonical serialization format for interoperability between RI-PY and RI-RS is TODO. APS-300 §5 similarly leaves the canonical `evidence_hash` algorithm TODO.

The implementations nevertheless contain concrete, incompatible Merkle contracts.

### RI-RS (Aura-Guard)

`src/merkle.rs` implements:

- leaf: `SHA-256(0x00 || raw_data_bytes)`
- interior node: `SHA-256(0x01 || left_digest_bytes || right_digest_bytes)`
- empty tree: `SHA-256(empty)`
- odd nodes: promoted unchanged using the RFC 6962 recursive tree shape

### RI-PY (Aura Core)

`audit/merkle.py` implements:

- non-hashed string leaf: `SHA-256(UTF-8(leaf_string))`
- interior node: `SHA-256(UTF-8(left_hex + right_hex))`
- odd nodes: duplicated (`right = left`)

These are different byte domains and different tree semantics. They cannot be expected to produce the same Merkle root.

## Decision

**Proposed normative rule:** Aura Protocol Merkle evidence SHALL use the RFC 6962 hash domain and tree construction:

1. Leaf hash: `SHA-256(0x00 || leaf_data_bytes)`.
2. Interior node hash: `SHA-256(0x01 || left_hash_bytes || right_hash_bytes)`.
3. Hash inputs SHALL be raw bytes, never hexadecimal text representations of digests.
4. The tree shape SHALL use the RFC 6962 recursive split at the largest power of two strictly less than `n`.
5. A single unpaired node is promoted unchanged; the last node SHALL NOT be duplicated.
6. Empty-tree semantics SHALL be explicitly specified wherever an empty tree is permitted.
7. Every cross-language implementation SHALL pass the same normative byte-level fixtures.

This ADR does **not** authorize immediate changes to RI-PY or RI-RS. Those changes require a separate remediation PR after this decision is approved.

## Rationale

The RFC 6962 domain prefixes provide explicit domain separation between leaves and interior nodes. Raw digest bytes eliminate representation ambiguity between binary hashes and their hexadecimal display form. The recursive tree construction removes the current ambiguity around odd leaf counts.

## Consequences

### Positive

- Deterministic cross-language Merkle roots.
- Explicit cryptographic byte domain.
- Independent verification without implementation-specific assumptions.
- Direct fixture-based conformance testing.

### Negative / migration cost

- Existing RI-PY Merkle roots are not compatible with the proposed contract.
- Existing evidence generated under the RI-PY contract cannot silently be reinterpreted as RFC 6962 evidence.
- A migration/version boundary and fixture update will be required.

## Compatibility and migration rule

Existing evidence MUST retain its original algorithm identity. No historical digest may be recomputed and presented as unchanged evidence. A future protocol version/profile SHALL distinguish the RFC 6962 domain from legacy Merkle evidence.

## Conformance gate

Before this ADR can be marked APPROVED:

- [ ] Chief Architect approval recorded.
- [ ] APS-200 §8 updated with the canonical byte-level rule.
- [ ] APS-300 evidence hash scope reconciled with the selected canonical serialization.
- [ ] APS-500 fixture promoted from proposal to normative fixture.
- [ ] RI-PY and RI-RS cross-language conformance tests both pass.
- [ ] Migration/version semantics documented.

## Evidence

See:

- `ck003/dq-002-hash-domain/README.md`
- `ck003/dq-002-hash-domain/fixtures/FIX-CK003-DQ002-RFC6962-2LEAF.json`

This ADR is a proposal only. Per repository governance, an AI assistant may propose and implement but may not approve or freeze canonical documents.
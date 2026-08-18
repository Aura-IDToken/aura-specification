# DQ-002 Hash-Domain Evidence Matrix

**Date:** 2026-08-17
**Baseline source:** `aura-specification` commit `62d2d6bcc1a46dd505ebfe400ad01fa3c6a25bf0`

## Specification evidence

| Source | Current statement | DQ-002 impact |
|---|---|---|
| APS-200 §4 | `integrity_hash` is SHA-256 of the canonical serialization | Hash input must ultimately have one canonical byte representation |
| APS-200 §8 | Serialization may vary, but canonical serialization for RI-PY ↔ RI-RS interoperability is **TODO** | Normative gap is confirmed |
| APS-300 §5 | `evidence_hash` is SHA-256 of Evidence excluding the field | Exact canonical algorithm is **TODO** |
| APS-500 §5 | Canonical fixture data is **TODO** pending APS-200 / APS-300 finalization | Cross-language fixture must currently remain proposed |
| INV-003 | Every protocol object MUST have an unambiguous canonical serialization | Directly implicated |
| INV-006 | Results MUST be platform-independent | Cross-language byte equality is required for the evidence domain |
| INV-011 | Evidence integrity MUST be independently verifiable | Hash domain must be explicit |
| INV-014 | Implementations MUST pass applicable reference fixtures | Fixture is the conformance mechanism |

## Implementation evidence

### RI-RS — Aura-Guard

`src/merkle.rs` defines:

- `leaf_hash(data)` = SHA-256 of `0x00 || data`.
- `node_hash(left,right)` = SHA-256 of `0x01 || left || right`.
- `merkle_root` uses the RFC 6962 recursive split.
- A lone node is promoted; the last node is not duplicated.

Source blob SHA: `658d5b51e14830b03be8a4248ac06ca9731578ae`.

### RI-PY — Aura Core

`audit/merkle.py` defines:

- `sha256(data: str)` = SHA-256 of UTF-8 text.
- ordinary string leaves are hashed directly without a domain prefix.
- interior nodes hash UTF-8 of `left_hex + right_hex`.
- odd nodes duplicate the current node.

Source blob SHA: `c0db98fbfb01eaf558c25d05e3696e78c3e5ffd5`.

## Compatibility conclusion

The two implementations are **not byte-compatible Merkle implementations** under the current source contracts.

This is not a documentation-only discrepancy. The leaf domain, node domain, and odd-tree semantics differ. Therefore a semantic event set can produce different roots and proofs.

## Independent two-leaf vector

For raw UTF-8 leaves `61` (`a`) and `62` (`b`), under the proposed RFC 6962 domain:

- leaf A = `022a6979e6dab7aa5ae4c3e5e45f7e977112a7e63593820dbec1ec738a24f93c`
- leaf B = `57eb35615d47f34ec714cacdf5fd74608a5e8e102724e80b24b287c0c27b6a31`
- root = `b137985ff484fb600db93107c77b0365c80d78f5b429ded0fd97361d077999eb`

These values are generated from the explicit byte-domain formulas, not copied from either implementation.

## Decision state

**DQ-002: OPEN — evidence sufficient to establish incompatibility; normative binding decision remains pending.**

No production repository has been modified by this evidence pack.
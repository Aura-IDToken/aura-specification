# DQ-002 Hash-Domain Evidence Matrix

> **Subordinate record — revalidated 2026-08-21.** The AS-IS findings below are
> **correct and were re-verified by execution and by source inspection** during
> the DQ-002 final closure revalidation; both cited source blob SHAs are
> unchanged at each repository's current head. The **Decision state** block at
> the end of this file is superseded: the DQ-002 status of record is
> **BLOCKED**, per [`closures/DQ-002_FINAL_CLOSURE.md`](../../closures/DQ-002_FINAL_CLOSURE.md).
> Where this file and that record differ, that record governs.

**Date:** 2026-08-17 · revalidated 2026-08-21
**Baseline source:** `aura-specification` commit `62d2d6bcc1a46dd505ebfe400ad01fa3c6a25bf0`
**Revalidation baseline:** `aura-specification` commit `ff30e166be2511b6d5684a33efb8c7da9d63a574`

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

## 2026-08-21 revalidation — what changed and what did not

The DQ-006 canonical serialization boundary (RFC 8785 JCS → UTF-8
`canonical_bytes`) is now bound in APS-200 §8.2, which closes the dependency
that `02_hash_domain_adr.md` §3.1 left open. The hash-domain contract itself is
**unchanged**: SHA-256 over `canonical_bytes`, leaf `0x00`, node `0x01`, raw
32-byte children.

Re-executed on 2026-08-21:

| Check | Result |
|---|---|
| `tools/rfc6962_oracle.sh selftest` | PASS, exit 0 |
| `tools/compare_vectors.py` RI-PY vs RI-RS | EQUAL + CONFORMANT, 0 diffs, exit 0 |
| `tools/dq002_hash_domain_revalidation.py` | 41 checks, 0 failed, exit 0 |
| RI-PY `conformance/merkle/` @ `badd0b19` | 158 passed |
| RI-PY `conformance/canonical/` @ `3e8e0e32` | 13 + 1 + 13 passed; negative controls exit 0 |
| RI-RS `hash_domains` · `byte_representations` · `ck003_dq002_ri_rs_conformance` · `golden` · `canonical_001` @ `35082d7b` | 17 + 18 + 1 + 10 + 5 passed |

Source blob SHAs cited above re-verified at each repository's current head:
RI-RS `src/merkle.rs` = `658d5b51e14830b03be8a4248ac06ca9731578ae`, RI-PY
`audit/merkle.py` = `c0db98fbfb01eaf558c25d05e3696e78c3e5ffd5`. Both unchanged.
The compatibility conclusion above therefore still holds: RI-PY's **production**
audit path is still the legacy contract, deliberately, per the ADR migration
rule. RI-PY's conformant implementation lives in the conformance-only module
`conformance/merkle/rfc6962.py`.

## Decision state

**DQ-002: BLOCKED** — the hash-domain contract is settled and cross-language
conformance re-executes clean, but closure evidence is insufficient: the
governing ADR is still `PROPOSED`, APS-001 §7.2 defers odd-node behaviour to an
"approved Aura Merkle profile" that does not exist, `DEFECT-DQ002-F1/F2/F3`
are all OPEN, no DQ-002 CI gate has ever executed successfully, and the
depended-upon DQ-006 gate is itself OPEN. Residuals R-1…R-10 and the full
criteria table are in
[`closures/DQ-002_FINAL_CLOSURE.md`](../../closures/DQ-002_FINAL_CLOSURE.md) §12, §15.

No production repository has been modified by this evidence pack or by the
2026-08-21 revalidation.
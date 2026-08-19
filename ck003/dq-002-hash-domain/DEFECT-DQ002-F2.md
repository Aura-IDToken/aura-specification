# DEFECT-DQ002-F2 — DQ-002 does not state that an audit path fails to bind tree size

- **Status:** OPEN — specification gap, awaiting Protocol Custodian resolution
- **Raised by:** CROSS-LANGUAGE-002 execution, 2026-08-18
- **Severity:** Specification completeness. **Not** an implementation divergence.
- **Artifact:** `ADR-CK003-DQ002-HASH-DOMAIN.md`, `README.md`

## Observation

An RFC 6962 audit path does not uniquely commit to the tree size it was
produced for. Verification decisions depend on the bit pattern of
`(leaf_index, tree_size - 1)`, so several tree sizes require an identical path
shape and all verify against the true root.

Measured, for leaf payloads `leaf-0 … leaf-7`, probing claimed sizes 0…9:

| True tree size | Leaf index | Claimed sizes accepted |
| --- | --- | --- |
| 5 | 0–3 | 5, 6, 7, 8 |
| 5 | 4 | 5 |
| 7 | 4–5 | 7, 8 |
| 7 | 6 | 7 |
| 8 | 0–3 | 5, 6, 7, 8 |
| 8 | 6–7 | 8 |
| 3 | 0–1 | 3, 4 |
| 3 | 2 | 3 |

**RI-PY and RI-RS accept exactly the same set in every one of the 36
(tree size, leaf index) cases measured.** This is a property of RFC 6962, not a
divergence, and not a defect in either implementation.

## Why it still matters

The root remains the binding commitment: no forgery is possible, and a leaf
cannot be shown to be in a tree whose root does not contain it. But an
implementer reading DQ-002 could reasonably assume `tree_size` is
authenticated by the audit path and build an evidence claim ("this entry was
present in a log of exactly N entries") that the proof does not support.
Binding tree size requires a signed tree head or a consistency proof, neither
of which DQ-002 currently mentions.

## Requested resolution

1. State explicitly in DQ-002 that an inclusion proof authenticates
   `(leaf, root)` and **not** `tree_size`.
2. Decide whether Aura evidence requires tree-size binding. If it does,
   specify the mechanism (signed tree head / consistency proof) as a separate
   decision — this is out of scope for DQ-002 as written.

## Regression protection already in place

The measured acceptance sets are pinned in both implementations, so any future
divergence between RI-PY and RI-RS fails a test rather than passing silently:

- RI-PY: `conformance/merkle/test_dq002_rfc6962.py::test_nc9_tree_size_acceptance_set_matches_ri_rs`
- Cross-language: `conformance/merkle/test_cross_language_002.py::test_verification_decisions_agree_for_every_tree_size`

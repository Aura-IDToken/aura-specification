# CK-003 — Canonical Serialization Re-Execution Evidence

**Classification:** EVIDENCE — INFORMATIVE
**Normative authority:** APS-200 §8 (this document defines nothing)
**Execution date:** 2026-08-20
**Fixture:** CANONICAL-001

This record exists because CK-003 must not rest on a table of numbers copied
forward. Both reference engines were run again, from their own repositories, and
the frozen values were reproduced rather than restated.

## 1. What was executed

### RI-PY — `Aura-IDToken/aura-poc-a-core-v3.3`

| Field | Value |
|---|---|
| Source | `conformance/` tree at `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| Cited execution commit | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` (verified ancestor of the above) |
| Engine | `rfc8785==0.1.4`, installed into an isolated virtual environment |
| Command | `pytest conformance/canonical -q` |
| Result | **27 passed, 0 failed** |

Direct engine invocation on `conformance/corpus/canonical-001/input.json`:

```text
canonical_bytes_hex:
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d

SHA-256(canonical_bytes):
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6

SHA-256(0x00 || canonical_bytes):
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

The RI-PY conformance tree was extracted read-only with `git archive`. No branch
was checked out and no file in the RI-PY repository was modified.

### RI-RS — `Aura-IDToken/aura-guard-v1.3`

| Field | Value |
|---|---|
| Source | default branch, `35082d7b4880dad780fb55a1a5f3ac0ef4322674` |
| Engine | `serde_json_canonicalizer==0.3.2` (`[dev-dependencies]`) |
| Command | `cargo test --test canonical_001` |
| Result | **5 passed, 0 failed** |

```text
canonical_001_canonical_bytes_are_byte_exact ... ok
canonical_001_sha256_of_canonical_bytes ... ok
canonical_001_pipeline_evidence ... ok
canonical_001_leaf_uses_raw_0x00_prefix ... ok
merkle_leaf_domain_matches_rfc6962 ... ok
```

The harness produces the canonical bytes by running the engine, then computes both
digests from the bytes it produced. It does not compare two hardcoded constants.

### Fixture self-consistency

`scripts/validate_canonical_001.py` — 10 checks, all PASS, including two negative
controls (`0x01` domain, ASCII `"0x00"` prefix). The script does not canonicalize;
see its docstring.

## 2. Provenance findings

These are recorded because they qualify the evidence, and a reader reproducing
this work will hit them.

| Finding | Detail |
|---|---|
| RI-PY evidence is not on the default branch | `49d0e4f` and `3e8e0e3` are reachable from `claude/cross-language-canonical-001-n4v2c5`, and **not** from `origin/main`. `origin/main` contains no RFC 8785 reference at all. |
| RI-RS cited evidence is not on the default branch | `4e9e228` and `420653e` are reachable from `claude/cross-language-canonical-001-n4v2c5`, and **not** from `origin/main`. |
| RI-RS default branch carries a *different* harness | PR #58 (`claude/canonical-001-conformance-vm2k69`) merged an independently authored CANONICAL-001 harness into `main` at `35082d7`. It is not the artifact the DQ-006 closure cites. Its JCS dependency sits in `[dev-dependencies]`, so the production runtime is untouched. |

The RI-RS result above is therefore **corroboration from a second, independent
harness**, not a re-run of the closure-cited artifact. It strengthens the
canonical-bytes claim; it does not retire the provenance gap.

**Open evidence gap (unchanged by CK-003):** the artifacts underlying the
DQ-006 / CROSS-LANGUAGE-001 closure remain unmerged in both implementation
repositories. A reviewer cloning either repository at its default branch cannot
reach them. This is the substance of CFL-004 and is routed to the Protocol
Custodian; CK-003 does not close it.

## 3. What this record does not establish

- It does not close DQ-002, DQ-004, APS-001, or any release gate.
- It does not authorize any production runtime change in RI-PY or RI-RS.
- It does not make either engine, or either engine version, part of the protocol
  contract (APS-200 §8.7).

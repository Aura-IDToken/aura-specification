# DQ-006 — CANONICAL-003 Technical Evidence Report

**Document ID:** DQ6-TECH-EVIDENCE-CANONICAL-003-2026-10-15  
**Date:** 2026-10-15  
**Classification:** EVIDENCE — NON-NORMATIVE  
**Purpose:** Record reproducible RI-PY / RI-RS execution evidence for CANONICAL-003 and disposition the technical evidence against the controlled DQ-006 execution order.  
**Normative effect:** NONE  
**Ratification:** NOT PERFORMED  
**Overall DQ-006 status:** **OPEN — this report does not close DQ-006 and does not alter the authoritative closure record.**

> This report follows the gate numbering in `ck003/dq-006-final-closure-execution/DQ-006_FINAL_CLOSURE_EXECUTION_ORDER.md`: R1 = JCS discriminator, R2 = authoritative RI-RS boundary, R3 = evidence reachability, R4 = Chief Architect ratification. The residual table in `closures/DQ-006_CLOSURE_PACKAGE.md` uses a different R2/R3 numbering. This report does not silently amend either record; the numbering discrepancy requires explicit reconciliation in a later controlled change.

## 1. Executive finding

CANONICAL-003 has now been independently executed through the RI-PY and RI-RS conformance paths in the `vaidt/*` working repositories. Both paths produced the same 577-byte canonical UTF-8 representation as the pinned specification oracle artifact, with no trailing LF. Both independently reproduced the same canonical SHA-256 and RFC 6962 leaf SHA-256.

**Observed result for CANONICAL-003: PASS — byte identity, canonical digest and leaf digest all match the pinned expected artifact in both implementations.** RI-PY additionally binds the expected leaf digest to the changed production `MerkleAttestor.generate_leaf` entry point. No further serializer change is indicated by the observed CANONICAL-003 result.

This is a finite conformance result for the tested fixture, not a proof over every possible RFC 8785 input. Nor does implementation success grant normative status. The technical result is recorded separately from outstanding source-of-record, reachability, scope and ratification issues.

## 2. Frozen input and oracle

| Field | Value |
|---|---|
| Specification repository used by both test workflows | `vaidt/aura-specification` |
| Fixture commit | `b3a6e784d9a6ea2e0b554310e3de80e7d13de859` |
| Input fixture | `fixtures/corpus/CANONICAL-003_jcs_full_discriminator.json` |
| Selected JSON Pointer | `/protocol_object` |
| Input fixture length | `4230 bytes` |
| Input fixture SHA-256 | `1cde8282d6df99defc16b8652cb0f43a8f327c35b8f356a8612b835ed996ec73` |
| Frozen expected bytes | `fixtures/corpus/CANONICAL-003_jcs_full_discriminator.expected.jcs` |
| Expected canonical output length | `577 bytes` |
| Trailing LF | `false` |
| Expected SHA-256(canonical bytes) | `9fb648c388c4485575d25c1d6171ba691fec51c1b433b11f4d61197bbe2a5509` |
| Expected RFC 6962 leaf SHA-256 | `38672ea2bd0ea87b2446efce8d4ba4adeb822e0baaecee4a54b73179198d2b3e` |

The canonical digest is calculated over the exact RFC 8785 UTF-8 bytes. The leaf digest is calculated over the raw preimage `0x00 || canonical_bytes`. The prefix is one raw zero octet, not the text representation `"0x00"`.

CANONICAL-003 is intentionally discriminating across three axes: ECMAScript-compatible number serialization, UTF-16 code-unit key ordering and string escaping/UTF-8 output. The oracle fixture records examples including `10.0 → 10`, `1e5 → 100000`, `1e-6 → 0.000001`, `1e-7 → 1e-7`, `1e20 → 100000000000000000000`, `1e21 → 1e+21`, and `-0.0 → 0`. Supplementary-plane keys sort ahead of `U+E000` under the required UTF-16 ordering; this is a discriminator that ordinary sorted-key JSON does not reliably satisfy.

## 3. Actual cross-implementation comparison

| Property | RI-PY — Python | RI-RS — Rust | Comparison |
|---|---|---|---|
| Tested entry point | `core/merkle.py::MerkleAttestor.generate_leaf`, also independently checks `rfc8785.dumps` bytes | `conformance/canonical/canonical_003.rs` through `conformance/canonical/jcs.rs` | Both independently execute their selected JCS path |
| Canonicalizer | `rfc8785==0.1.4` | `serde_json_canonicalizer = 0.3.2` | Different implementations/languages |
| Actual canonical bytes | 577 bytes | 577 bytes | Each is byte-identical to the frozen oracle artifact |
| Trailing LF | None | None | MATCH |
| SHA-256(canonical bytes) | `9fb648c388c4485575d25c1d6171ba691fec51c1b433b11f4d61197bbe2a5509` | `9fb648c388c4485575d25c1d6171ba691fec51c1b433b11f4d61197bbe2a5509` | MATCH |
| SHA-256(`0x00 || canonical_bytes`) | `38672ea2bd0ea87b2446efce8d4ba4adeb822e0baaecee4a54b73179198d2b3e` | `38672ea2bd0ea87b2446efce8d4ba4adeb822e0baaecee4a54b73179198d2b3e` | MATCH |
| Actual runtime hook | `MerkleAttestor.generate_leaf` returns expected leaf digest | Rust test exercises the conformance adapter; it does not claim production `src/merkle.rs` uses JCS | Deliberately different integration scope |

### 3.1 RI-PY execution evidence

- Working repository: [`vaidt/aura-poc-a-core-v3.3`](https://github.com/vaidt/aura-poc-a-core-v3.3)
- PR: [#4 — use RFC 8785 JCS and RFC 6962 leaf domain in RI-PY](https://github.com/vaidt/aura-poc-a-core-v3.3/pull/4) — **MERGED**
- Main merge commit: [`1d15ecbed8470476684951e9ff301a3cfc26a46d`](https://github.com/vaidt/aura-poc-a-core-v3.3/commit/1d15ecbed8470476684951e9ff301a3cfc26a46d)
- Pre-merge CANONICAL-003 run: [workflow 38679686272](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38679686272) — **SUCCESS, 10/10 checks PASS**
- Pre-merge Execution Checks: [workflow 38679686225](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38679686225) — **SUCCESS**
- Post-merge Docker full-suite evidence: [workflow 38680695701](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38680695701) — **SUCCESS**
- The CANONICAL-003 run executed on the PR validation merge commit `6d3cd79d924d46ba371142a68dfe2ccab76c68e0`; the resulting change was subsequently merged to `main` at `1d15ecbed8470476684951e9ff301a3cfc26a46d`.

The 10 checks cover input byte length and SHA-256, expected artifact length and SHA-256, actual canonical byte length, exact byte identity, canonical SHA-256, RFC 6962 leaf SHA-256, the production `generate_leaf` return value, and method binding. All were reported PASS.

**Scope deviation to preserve:** PR #4 changes the existing production Core hash/Merkle entry point in `core/merkle.py`, not merely a conformance adapter. The controlled DQ-006 execution order §5 says production `core/` semantics and production hash/Merkle changes are outside that gate's allowed scope. The user separately directed the merge, and it has occurred; this report records the implementation result but does not retroactively convert that scope deviation into DQ-006 authorization. The changed digest behaviour requires a separate compatibility and migration review before treating this as a production release.

### 3.2 RI-RS execution evidence

- Working repository: [`vaidt/aura-guard-v1.3`](https://github.com/vaidt/aura-guard-v1.3)
- PR: [#9 — execute CANONICAL-003 in RI-RS](https://github.com/vaidt/aura-guard-v1.3/pull/9) — **MERGED**
- Main merge commit: [`488d267f56fdb9ba58fcafc8bf4d4fe2a6149526`](https://github.com/vaidt/aura-guard-v1.3/commit/488d267f56fdb9ba58fcafc8bf4d4fe2a6149526)
- Execution commit in the PR: `0badf0c83b50e8a34f05983deba4dcbf4348ee73`
- [CI workflow 38678371494](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38678371494) — **SUCCESS**
- [Rust workflow 38678371567](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38678371567) — **SUCCESS**
- Test: `cargo test --locked --test canonical_003 -- --nocapture`
- Canonicalizer is pinned to `serde_json_canonicalizer = "=0.3.2"` in the Rust development/conformance dependency boundary; the DQ-006 change does not add it to the production `[dependencies]` or edit the production Rust Merkle implementation.

The Rust test independently loads the same pinned input object, executes its own adapter, compares the actual byte array to the unchanged oracle artifact, and independently calculates both SHA-256 values.

## 4. Gate disposition against the controlled execution order

### DQ6-R1 — JCS-discriminating fixture: **PASS**

The discriminating CANONICAL-003 object was independently executed through both implementations. Each result is byte-identical to the frozen 577-byte oracle representation and independently reproduces the same canonical digest and RFC 6962 leaf digest. This resolves the prior limitation of CANONICAL-001, whose simple object could not distinguish JCS from sorted/minified JSON.

### DQ6-R2 — authoritative RI-RS boundary: **TECHNICALLY ESTABLISHED IN THE `vaidt` WORKING REPOSITORY; GLOBAL SOURCE-OF-RECORD DISPOSITION OPEN**

In `vaidt/aura-guard-v1.3/main`, the reviewable boundary is `conformance/canonical/jcs.rs` with tests `canonical_001.rs` and `canonical_003.rs`; the engine is pinned in the conformance/development dependency scope, separate from the production Rust dependency graph. The experimental [PR #2](https://github.com/vaidt/aura-guard-v1.3/pull/2) is explicitly labelled **EXPERIMENTAL / DO NOT MERGE** and is not a second accepted production boundary.

The current governing specification's conflict register also identifies a separate, still-open [PR #59 in `Aura-IDToken/aura-guard-v1.3`](https://github.com/Aura-IDToken/aura-guard-v1.3/pull/59), whose proposed dependency placement conflicts with the production-isolation rule. The `Aura-IDToken/*` repositories and `vaidt/*` working repositories are distinct GitHub repositories; the latter are forks. Therefore the target-fork technical boundary is now identifiable, but the broader R2 requirement cannot be marked fully closed until the source-of-record conflict and competing PR are explicitly disposed of or the controlling specification formally designates the `vaidt/*` repositories as the required conformance source.

### DQ6-R3 — evidence reachability: **PASS IN THE `vaidt/*` FORK NAMESPACE; NOT YET PROVEN AGAINST THE CURRENTLY NAMED UPSTREAM TARGETS**

The RI-PY and RI-RS code/test changes are now reachable from the respective `vaidt/*` `main` branches via merge commits `1d15ecbed8470476684951e9ff301a3cfc26a46d` and `488d267f56fdb9ba58fcafc8bf4d4fe2a6149526`. The run records above link to executable CI evidence. Thus the evidence is no longer confined to the original ephemeral branches within the requested `vaidt/*` working namespace.

However, the controlling `DQ-006_FINAL_CLOSURE_EXECUTION_ORDER.md` explicitly names `Aura-IDToken/aura-poc-a-core-v3.3` and `Aura-IDToken/aura-guard-v1.3` as the repositories whose default/reviewable branches must expose the evidence. The merges recorded here were made to the different `vaidt/*` forks, not those named upstream repositories. No immutable publication mechanism accepting these fork artifacts as a substitute is identified in the current authoritative closure record. Consequently, **R3 is technically satisfied for the repositories requested in this task, but remains unproven under the exact repository identity criterion currently recorded by the specification**. This is a source-of-record reconciliation issue, not a failing CANONICAL-003 comparison.

### DQ6-R4 — Chief Architect ratification: **OPEN / NOT PERFORMED**

No ratification is asserted in this report. No edit is made to `closures/DQ-006_CLOSURE_PACKAGE.md`, APS-200, APS-300, CONF-003, the blocker register or any ratification record. The existing authoritative record remains in force:

```text
CANONICAL-003 RI-PY/RI-RS execution = PASS
DQ-006 overall                    = OPEN
DQ6-R4 ratification               = NOT PERFORMED
Normative effect of this report   = NONE
```

The report is evidence for the designated reviewer; it does not perform the reviewer’s decision.

## 5. Migration, version and compatibility controls

The canonical bytes and leaf hash are now demonstrated for the fixed CANONICAL-003 object. The merge to Core changes the value returned by `MerkleAttestor.generate_leaf`, both due to switching to RFC 8785 bytes and adding the RFC 6962 raw `0x00` leaf domain. Downstream certificate identifiers derived from the leaf may therefore change for the same semantic input.

APS-200 §8.8 and APS-300 §5.3 require profile/version-aware treatment of historical artifacts: existing evidence must retain its original serialization/hash-profile identity and must not be silently reinterpreted under a newer profile. This report does **not** claim that every historic certificate has been individually verified or migrated. Before a production release, record at least:
1. the version/profile boundary for newly generated hashes;
2. how old and new evidence are identified and verified without silently recomputing legacy hashes under the new profile;
3. the impact on ETC/certificate identifiers, stored records, proofs and consumers;
4. the authorized rollout/rollback boundary for the production Core change.

These are compatibility and implementation-governance actions; they do not change the successful CANONICAL-003 byte comparison.

## 6. Remaining record-integrity notes

1. The checked-in CANONICAL-003 fixture metadata still labels `RI-PY`, `RI-RS` and cross-language equality as `NOT_EXECUTED`, and the oracle as `INDEPENDENT_ORACLE_CALCULATED_NOT_EXECUTED_AGAINST_RECEIVERS`. The runs documented here post-date that metadata. It is intentionally not rewritten in this report: metadata/manifest reconciliation must be a separate controlled fixture change so the frozen input and expected artifact hashes remain auditable.
2. The old closure package and the later final execution-order document use different R2/R3 residual numbering. This report follows the latter controlled execution order and preserves the discrepancy for explicit reconciliation.
3. Passing a single multi-axis discriminator strongly closes the specific serializer defect exercised here; it is not exhaustive testing of all legal/illegal RFC 8785 inputs, malformed values, size boundaries or every consuming code path.
4. This report does not close DQ-002, DQ-003, DQ-004, APS-001, INV-001…INV-015, GATE C or GATE D, and does not approve Aura specification v1.0.

## 7. Final technical verdict

```text
CANONICAL-003:
  RI-PY canonical bytes / digest / leaf = PASS
  RI-RS canonical bytes / digest / leaf = PASS
  Cross-language equality to pinned oracle = PASS
  Further serializer modification indicated by this fixture = NO

DQ6-R1:
  JCS-discriminating execution = PASS

DQ6-R2:
  vaidt fork conformance boundary = TECHNICALLY IDENTIFIED
  overall repository/source-of-record disposition = OPEN

DQ6-R3:
  evidence reachable from vaidt/* main = PASS
  reachability against the repositories currently named by the controlling order = NOT PROVEN

DQ6-R4:
  Chief Architect ratification = OPEN / NOT PERFORMED

DQ-006 overall = OPEN
```

**Conclusion:** the tested RFC 8785 behaviour is now empirically demonstrated on both RI-PY and RI-RS against the same frozen, discriminating 577-byte expected representation. No additional serializer modification is indicated by this evidence. The normative barrier remains intact: neither a passing test nor this evidence report may transition DQ-006 to `CLOSED / PASS`; DQ6-R4 must remain a separate, explicit ratification act after the outstanding source-of-record and reachability criteria are reconciled.

# DQ-006 — Closure Package

**Document ID:** DQ-006-CLOSURE-001
**Status:** **OPEN** — specification closed, conformance evidence partial
**Classification:** DECISION / CLOSURE RECORD
**Authority:** APS-200 §8 · APS-300 §5 · ADR-CK003-DQ006 · CONF-003
**Original closure record:** 2026-08-19 (recorded CLOSED / PASS)
**Reconciled:** 2026-08-20 — DQ-006 CLOSURE RECONCILIATION
**Ratification:** required — GOVERNANCE.md §2 reserves status transitions to the Chief Architect

> **This is the single authoritative DQ-006 closure record.** Four earlier records
> ([`evidence/DQ-006_CLOSURE_PACKAGE.md`](../evidence/DQ-006_CLOSURE_PACKAGE.md),
> [`ck003/DQ-006_CLOSURE.md`](../ck003/DQ-006_CLOSURE.md),
> [`ck003/dq-006-closure/DQ-006-CLOSURE.md`](../ck003/dq-006-closure/DQ-006-CLOSURE.md),
> [`ck003/dq-006-closure/README.md`](../ck003/dq-006-closure/README.md))
> are SUPERSEDED by this one and retained for history. Where any of them differs from this
> record, this record governs.

---

## 1. Decision

DQ-006 asked which canonical serialization profile the Aura Protocol uses, and whether independent implementations execute it identically.

The **decision** is settled: the profile is **RFC 8785 JSON Canonicalization Scheme (JCS)** over UTF-8 bytes, with `SHA-256(canonical_bytes)` as the record digest and the RFC 6962 leaf domain `SHA-256(0x00 || canonical_bytes)`. As of this reconciliation the decision is normatively bound in **APS-200 §8** and **APS-300 §5**, and recorded in **ADR-CK003-DQ006**.

The **gate remains OPEN**. The original CROSS-LANGUAGE-001 run used CANONICAL-001, a JCS-degenerate vector; that result alone established implementation *agreement*, not profile discrimination. Supplemental CANONICAL-003 evidence recorded on 2026-10-15 now demonstrates byte-level RFC 8785 discriminator agreement for one multi-axis fixture on both RI-PY and RI-RS in the `vaidt/*` working repositories. This addresses the specific discriminator gap for that tested vector, but does not close DQ-006: evidence reachability under the currently named `Aura-IDToken/*` repository criterion, the authoritative RI-RS boundary, ratification, and the newly recorded RI-PY production-scope deviation remain unresolved. See §§4.1, 9–10, and 12–15.

---

## 2. Scope

**In scope.** The canonical byte boundary for JSON-represented protocol objects; the digest domain over those bytes; the RFC 6962 leaf domain over those bytes; cross-implementation byte identity; the evidence required to demonstrate all of it.

**Out of scope.** Production runtime behaviour in either reference implementation; the Merkle tree construction semantics beyond the leaf/node domains (DQ-002); event-type vocabulary (DQ-004); version compatibility policy (DQ-003); INV-001…INV-015 closure; CI and release gates.

No production implementation change is authorized or implied by this package.

---

## 3. Normative contract

Defined once, in APS-200 §8. Reproduced here as a reference only — APS-200 §8 governs.

```text
validated protocol object
        ↓  RFC 8785 JCS
UTF-8 canonical_bytes
        ↓
digest(B)  = SHA-256(B)
leaf(B)    = SHA-256(0x00 || B)
node(l, r) = SHA-256(0x01 || l || r)
```

`0x00` and `0x01` are raw octets. `l` and `r` are raw digest bytes. Prohibited digest inputs — pretty-printed JSON, implementation-specific serializations, escaped or hex/Base64 encodings of the canonical bytes, hex digest strings in place of digest bytes — are enumerated in APS-200 §8.4.

The evidence-hash domain is bound to the same canonical bytes by APS-300 §5.1.

| Layer | Content |
|---|---|
| **Normative protocol contract** | RFC 8785 JCS · UTF-8 canonical bytes · SHA-256 digest · RFC 6962 `0x00` leaf / `0x01` node |
| **Conformance implementation detail** | `rfc8785` 0.1.4 (RI-PY) · `serde_json_canonicalizer` 0.3.2 (RI-RS) · adapters · runners · corpus layout |

The engines are not the protocol. See ADR-CK003-DQ006 §2.

---

## 4. Evidence

Fixture **CANONICAL-001**.

Input (`input.json`, SHA-256 `649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261`), stored byte-identically in both reference repositories:

```json
{
  "event_type": "AUDIT_RECORD",
  "protocol_version": "1.0",
  "schema_version": "1.0",
  "payload": {
    "value": 42
  }
}
```

Observed values, identical on both sides:

```text
canonical_bytes_len : 100
canonical_bytes_hex : 7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
sha256              : b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
leaf_sha256 (0x00)  : ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

Independently recomputed during this reconciliation from the frozen hex alone, without reference to any recorded constant: all three values reproduce. The wrong-domain control `SHA-256(0x01 || canonical_bytes)` yields `491a8dccdaf280c90d6ce9984ecd8b067c26c994aff7144b0a7606e3119a10b1`, confirming the leaf domain is genuinely `0x00`.

### 4.1 Supplemental discriminator evidence — CANONICAL-003 (2026-10-15)

**Classification:** EVIDENCE — NON-NORMATIVE  
**Normative effect:** NONE  
**Ratification:** NOT PERFORMED  
**Disposition:** PASS for the tested discriminator in the `vaidt/*` working repositories; not a DQ-006 closure verdict.

The technical execution report is [`ck003/dq-006-final-closure-execution/DQ-006_CANONICAL-003_TECHNICAL_EVIDENCE_REPORT_2026-10-15.md`](../ck003/dq-006-final-closure-execution/DQ-006_CANONICAL-003_TECHNICAL_EVIDENCE_REPORT_2026-10-15.md), committed on `vaidt/aura-specification/main` at `d808b2d84097fa326c3ed6793f56491e58ab04e2`. The fixture and expected `.jcs` oracle were not changed by the later metadata reconciliation.

| Field | Recorded value |
|---|---|
| Fixture source commit | `b3a6e784d9a6ea2e0b554310e3de80e7d13de859` |
| Input fixture | `fixtures/corpus/CANONICAL-003_jcs_full_discriminator.json` |
| Input fixture SHA-256 | `1cde8282d6df99defc16b8652cb0f43a8f327c35b8f356a8612b835ed996ec73` |
| Canonicalized scope | JSON Pointer `/protocol_object` |
| Canonical UTF-8 output | 577 bytes, no trailing LF; byte-identical to the frozen oracle on each receiver |
| SHA-256(canonical bytes) | `9fb648c388c4485575d25c1d6171ba691fec51c1b433b11f4d61197bbe2a5509` |
| SHA-256(`0x00 || canonical_bytes`) | `38672ea2bd0ea87b2446efce8d4ba4adeb822e0baaecee4a54b73179198d2b3e` |
| Discriminators covered | ECMAScript-compatible number rendering; UTF-16 code-unit key ordering; JSON escaping and raw UTF-8 output |

**RI-PY — Python working repository**

- Repository: `vaidt/aura-poc-a-core-v3.3`; PR #4 merged to `main` at `1d15ecbed8470476684951e9ff301a3cfc26a46d`.
- CANONICAL-003 workflow `38679686272`: SUCCESS, 10/10 checks PASS. Post-merge Execution Checks `38680695757` and Docker full suite `38680695701`: SUCCESS.
- Tested entry point: `core/merkle.py::MerkleAttestor.generate_leaf`.
- **Scope deviation:** this PR changed the production Core hash/Merkle entry point, although the controlled DQ-006 execution order §5 excludes production `core/` semantic and hash/Merkle changes. The merge is recorded as an observed fact, not as retroactive DQ-006 authorization. Version/profile and historical-evidence compatibility review remains open.

**RI-RS — Rust working repository**

- Repository: `vaidt/aura-guard-v1.3`; PR #9 merged to `main` at `488d267f56fdb9ba58fcafc8bf4d4fe2a6149526`.
- CI workflow `38678371494` and Rust workflow `38678371567`: SUCCESS. Test: `cargo test --locked --test canonical_003 -- --nocapture`.
- Tested boundary: `conformance/canonical/canonical_003.rs` through `conformance/canonical/jcs.rs`, using `serde_json_canonicalizer = "=0.3.2"` in the conformance/development boundary.
- The evidence does not claim production `src/merkle.rs` or production Cargo dependencies were changed.

Both receivers independently emitted 577 bytes matching the pinned oracle and reproduced the same canonical and RFC 6962 leaf hashes. This is a finite test result for CANONICAL-003, not proof of every legal or illegal RFC 8785 input and not, by itself, full CONF-003 or DQ-006 closure. The fixture remains WORKING / EXPERIMENTAL / NON-NORMATIVE.

---

## 5. RI-PY evidence — historical CANONICAL-001 baseline

| Field | Value |
|---|---|
| Repository | `Aura-IDToken/aura-poc-a-core-v3.3` |
| Execution commit | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` (clean worktree) |
| Evidence commit | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| Branch | `claude/cross-language-canonical-001-n4v2c5` — **not merged to `main`** |
| Engine | `rfc8785` 0.1.4 |
| Adapter | `conformance/canonical/jcs.py`, SHA-256 `8f6c3b440221113721a82c6ff3ff61dcfbaccbcbe972ce7ae635d00444b8b5a4` (pure delegation to `rfc8785.dumps`) |
| Toolchain | CPython 3.11.15, Linux x86_64 |
| Artifact | `conformance/corpus/canonical-001/ri-py.json`, SHA-256 `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c` |
| Result | **PASS** |

Executed: `test_jcs_behavior.py` → 13 passed; `test_canonical_001.py` → 1 passed; `emit_ri_py_artifact` → artifact.

Artifact digest and adapter digest were re-verified against the source tree during this reconciliation; both match.

---

## 6. RI-RS evidence — historical CANONICAL-001 baseline

| Field | Value |
|---|---|
| Repository | `Aura-IDToken/aura-guard-v1.3` |
| Execution commit | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` (clean worktree) |
| Evidence commit | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |
| Branch | `claude/cross-language-canonical-001-n4v2c5` — **not merged to `main`** |
| Engine | `serde_json_canonicalizer` 0.3.2, resolved from `conformance/Cargo.lock` |
| Adapter | `conformance/canonical/jcs.rs`, SHA-256 `0dae4ef696f06a4d3248ca85284fd7db280ef3c897a96cf898ef076cd4e846f2` (pure delegation to `serde_json_canonicalizer::to_vec`) |
| Toolchain | rustc 1.94.1, Linux x86_64 |
| Artifact | `conformance/corpus/canonical-001/ri-rs.json`, SHA-256 `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` |
| Result | **PASS** |

Executed: `cargo test --locked --test canonical_001` → 4 passed, 0 failed. The engine lives in a separate `aura-guard-conformance` package with its own workspace root and lockfile, so the production `aura-guard` dependency graph gains no canonicalizer.

Artifact digest re-verified during this reconciliation; matches.

---

## 7. Cross-language equality — CROSS-LANGUAGE-001 (CANONICAL-001 baseline)

Runner: `conformance/canonical/test_cross_language_canonical_001.py` (RI-PY repository). It loads only the two artifacts; it imports no canonicalizer and never re-serializes the input.

| Check | Assertion | Result |
|---|---|---|
| C1 | RI-PY bytes == RI-RS bytes | PASS |
| C2 | Gate recomputes `SHA-256(RI-PY bytes)` == RI-PY `sha256` | PASS |
| C3 | Gate recomputes `SHA-256(RI-RS bytes)` == RI-RS `sha256` | PASS |
| C4 | RI-PY `sha256` == RI-RS `sha256` | PASS |
| C5 | Gate recomputes `SHA-256(0x00 \|\| RI-PY bytes)` == RI-PY leaf | PASS |
| C6 | Gate recomputes `SHA-256(0x00 \|\| RI-RS bytes)` == RI-RS leaf | PASS |
| C7 | RI-PY leaf == RI-RS leaf | PASS |
| C8 | Distinct implementations, repositories, engines declared | PASS |

Suite result: 13 passed. Secondary cross-check against the frozen reference values: PASS on both sides.

**CROSS-LANGUAGE-001 = PASS** for byte, digest and leaf equality on CANONICAL-001.

---

## 8. Negative controls

Each control copies the committed corpus to a temporary directory, mutates the copy, and runs the real gate against it.

| Control | Mutation | Gate exit | Checks that fired | Result |
|---|---|---|---|---|
| baseline | none | 0 | — | 13 passed |
| N1 | RI-RS `canonical_bytes_hex` final byte flipped | 1 | C1, C3, C6 | rejected |
| N2 | RI-PY `sha256` first byte corrupted | 1 | C2, C4 | rejected |
| N3 | Both leaves recomputed under domain `0x01` | 1 | C5, C6 | rejected |

N3 is the discriminating control: because both leaves were mutated consistently, C7 still passed. Only the independent recomputations in C5 and C6 caught it.

Corpus digests after the controls: unchanged. No mutation remains in either repository.

---

## 9. Production integrity and subsequent scope deviation

The checks below describe two separate execution contexts and must not be collapsed into one statement about the current repositories.

| Context | Repository | Observed production-integrity result |
|---|---|---|
| Original CROSS-LANGUAGE-001 / CANONICAL-001 baseline | RI-PY | `git diff -- core/ audit/` was empty at that historical execution point. This does not describe the later CANONICAL-003 merge. |
| Original CROSS-LANGUAGE-001 / CANONICAL-001 baseline | RI-RS | `git diff -- src/ Cargo.toml Cargo.lock` was empty at that historical execution point. |
| CANONICAL-003, 2026-10-15 | `vaidt/aura-poc-a-core-v3.3` | PR #4 changed `core/merkle.py::MerkleAttestor.generate_leaf`, including the canonical byte and RFC 6962 leaf-hash behavior. This is a recorded scope deviation from the controlled DQ-006 execution order §5. |
| CANONICAL-003, 2026-10-15 | `vaidt/aura-guard-v1.3` | Conformance adapter/test only; production `src/merkle.rs` and production Cargo dependency graph were not changed by PR #9. |

The CANONICAL-003 Python test and post-merge workflows succeeded, but passing tests do not resolve compatibility impact. The production Core change can alter digests and downstream certificate/evidence identifiers for semantically identical objects. Before any production release, a separate, reviewable version/profile and historical-evidence compatibility assessment must identify how legacy evidence continues to be verified, how old and new profiles are distinguished, downstream identifier impact, and rollout/rollback controls.

**Current criterion-10 disposition:** NOT MET for the supplemental CANONICAL-003 execution context because RI-PY production hash/Merkle behavior changed. The historical CROSS-LANGUAGE-001 check remains valid for its own execution point only. This package records the deviation; it neither authorizes it retroactively nor changes the normative contract.

---

## 10. Known deviations

### D-1 — CANONICAL-001 is JCS-degenerate · **HISTORICAL LIMITATION; DISCRIMINATOR GAP MITIGATED FOR CANONICAL-003 IN THE VAIDT SANDBOX**

The original finding remains correct for CANONICAL-001: for that object, `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` produces bytes identical to the frozen canonical bytes. CROSS-LANGUAGE-001 therefore established agreement on CANONICAL-001, but that fixture alone could not discriminate RFC 8785 from an ordinary sorted-JSON serializer.

That statement is no longer an accurate description of the complete evidence corpus. The supplemental CANONICAL-003 execution recorded in §4.1 covers ECMAScript-compatible number rendering, UTF-16 code-unit key ordering, and string escaping/raw UTF-8. RI-PY and RI-RS each independently matched the frozen 577-byte oracle and reproduced the same canonical SHA-256 and RFC 6962 leaf digest. Criterion 13 is therefore MET for this tested discriminator in the `vaidt/*` working repositories, without implying exhaustive RFC 8785 conformance or full CONF-003 PASS.

The earlier note that only RI-PY had an executed behavioral suite accurately described the prior evidence state. CANONICAL-003 now supplies a cross-language discriminator result, but does not replace comprehensive boundary testing, prohibited-input controls, upstream reachability, or RI-RS source-of-record disposition. Historical verification records remain linked at [`ck003/handover-assessment/10_INDEPENDENT_VERIFICATION.md`](../ck003/handover-assessment/10_INDEPENDENT_VERIFICATION.md) §3.2 and [`05_EVIDENCE_GAPS.md`](../ck003/handover-assessment/05_EVIDENCE_GAPS.md) EG-01.

### D-2 — Evidence is not reachable from any default branch · **SUBSTANTIVE**

The original CANONICAL-001 evidence commits cited in §§5–6 remain on branches that are unmerged in their named `Aura-IDToken/*` repositories; a reviewer cloning those repositories at `main` cannot locate that historical evidence package. The additional CANONICAL-003 result is reachable from `vaidt/aura-poc-a-core-v3.3/main` and `vaidt/aura-guard-v1.3/main`, but those are distinct working repositories/forks. The controlled execution order explicitly names `Aura-IDToken/aura-poc-a-core-v3.3` and `Aura-IDToken/aura-guard-v1.3`; no formally accepted immutable publication route substituting `vaidt/*` is recorded here. Therefore criterion 14 remains NOT MET. This is an evidence-identity/reachability issue, not a failure of the CANONICAL-003 byte comparison.

### D-3 — RI-RS conformance boundary of record is not decided · **SUBSTANTIVE**

The `vaidt/aura-guard-v1.3/main` conformance boundary used for CANONICAL-003 is now identifiable at `conformance/canonical/jcs.rs` with the `canonical_001` and `canonical_003` tests; the JCS engine remains outside the production dependency graph in that working repository. This does not settle the global source-of-record decision. The controlling record still identifies a competing open PR #59 in `Aura-IDToken/aura-guard-v1.3` whose proposed dependency placement conflicts with production isolation. The source-of-record conflict and competing implementations must be explicitly disposed of or the controlling specification must formally accept a different evidence publication route. See [`ck003/handover-assessment/04_CONFLICT_REGISTER.md`](../ck003/handover-assessment/04_CONFLICT_REGISTER.md) CFL-003 and the CANONICAL-003 report.

### D-4 — Branch naming · **PROCEDURAL**

Execution used session-designated branches rather than `ck003/cross-language-canonical-001`. No protocol-semantic impact.

### D-5 — Artifact commit identity · **PROCEDURAL**

Artifacts record the clean source commit that produced them; the publication commit is separate, avoiding self-referential commit identity. Re-running RI-RS evidence generation would update execution metadata; the canonical bytes, digest and leaf are deterministic and would not change.

### D-6 — Corpus transport · **PROCEDURAL**

The RI-RS artifact was generated in `aura-guard-v1.3` and transported byte-identically into the RI-PY corpus used by the gate. Both copies hash to `a6ebad01…59af329c`. It was not reconstructed or re-keyed.

### D-7 — Event-type interaction · **REPORTED, NOT RESOLVED**

CANONICAL-001 carries `"event_type": "AUDIT_RECORD"`. The Event-Type Registry currently registers no tokens and requires strict-mode rejection of unregistered tokens. See §14 and CFL-005. Not repaired here; DQ-004 governs.

---

## 11. Traceability

```text
DQ-006  ── closures/DQ-006_CLOSURE_PACKAGE.md  (this record)
  │
  ├─ APS-200 §8            aps/APS-200_CANONICAL_DATA_MODEL.md §8.1–8.9   NORMATIVE AUTHORITY
  │     └─ INV-003         invariants/INVARIANT_REGISTRY.md
  │
  ├─ APS-300 §5            aps/APS-300_EVIDENCE_MODEL.md §5.1–5.3         evidence-hash byte domain
  │
  ├─ ADR-CK003-DQ006       ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md
  │
  ├─ CONF-003              conformance/CONF-003_CANONICAL_SERIALIZATION.md   verdict PARTIAL
  │     └─ APS-400 §4      aps/APS-400_CONFORMANCE_TEST_MATRIX.md
  │
  └─ CANONICAL-001         fixtures/corpus/CANONICAL-001_jcs_evidence.json
        │
        ├─ RI-PY   aura-poc-a-core-v3.3 @ 49d0e4f6 (exec) / 3e8e0e32 (evidence)
        │            conformance/canonical/jcs.py
        │            conformance/canonical/test_jcs_behavior.py            13 passed
        │            conformance/canonical/test_canonical_001.py            1 passed
        │            conformance/corpus/canonical-001/ri-py.json            6b5b5ccd…5f2b856c
        │
        ├─ RI-RS   aura-guard-v1.3 @ 4e9e2284 (exec) / 420653e2 (evidence)
        │            conformance/canonical/jcs.rs
        │            conformance/canonical/test/canonical_001.rs            4 passed
        │            conformance/corpus/canonical-001/ri-rs.json            a6ebad01…59af329c
        │
        └─ CROSS-LANGUAGE-001
             conformance/canonical/test_cross_language_canonical_001.py     13 passed
             conformance/canonical/negative_controls_canonical_001.py       exit 0
             conformance/corpus/canonical-001/EXECUTION-EVIDENCE.md
                │
                ├─ canonical_bytes   100 B, 7b226576…22312e30227d
                ├─ SHA-256           b6c3660c…a139a4e6
                └─ RFC 6962 leaf     ce6b3673…6648c039
```

The graph above records the historical CANONICAL-001 baseline. Supplemental CANONICAL-003 evidence is indexed in §4.1 and in `ck003/dq-006-final-closure-execution/DQ-006_CANONICAL-003_TECHNICAL_EVIDENCE_REPORT_2026-10-15.md`; it is reachable from the `vaidt/*` working repositories and `vaidt/aura-specification/main`, but not yet proven reachable from the specifically named `Aura-IDToken/*` default/reviewable branches (deviation D-2).

---

## 12. Closure criteria

| # | Criterion | State |
|---|---|---|
| 1 | Normative canonical serialization rule exists in the specification | **MET** — APS-200 §8 |
| 2 | Evidence-hash byte domain bound to canonical bytes | **MET** — APS-300 §5.1 |
| 3 | Decision recorded in an ADR distinguishing contract from implementation detail | **MET** — ADR-CK003-DQ006 §2 |
| 4 | Conformance requirement expresses byte-level cross-implementation equality | **MET** — CONF-003 §4.2, §5 |
| 5 | A frozen normative cross-language fixture exists | **MET** — CANONICAL-001 |
| 6 | RI-PY independent execution | **MET** |
| 7 | RI-RS independent execution | **MET** |
| 8 | Canonical byte / SHA-256 / RFC 6962 leaf equality, independently recomputed | **MET** |
| 9 | Discriminating negative controls | **MET** |
| 10 | Production runtime unchanged for the executed gate | **NOT MET for the supplemental CANONICAL-003 path** — RI-PY production `core/merkle.py` changed; see §9. Original CROSS-LANGUAGE-001 baseline integrity check remains historical evidence only. |
| 11 | Version and migration semantics recorded | **MET** — APS-200 §8.8, APS-300 §5.3; implementation-specific impact review remains open before release |
| 12 | Single normative authority; no competing definition | **MET** — APS-200 §8.2; superseded records marked |
| 13 | Evidence discriminates RFC 8785 from sorted JSON, cross-language | **MET for CANONICAL-003 in `vaidt/*` only** — §4.1; this does not imply exhaustive RFC 8785 or full CONF-003 conformance |
| 14 | Evidence reachable from each reference repository's default branch or accepted immutable route | **NOT MET** — D-2; `vaidt/*` reachability does not satisfy the named `Aura-IDToken/*` criterion |
| 15 | RI-RS conformance boundary of record decided, alternatives disposed | **NOT MET** — D-3 |
| 16 | Chief Architect ratification of the verdict | **NOT MET — NOT PERFORMED** — GOVERNANCE.md §2 |

Criteria 1–9, 11 and 12 remain met. Criterion 10 is not met for the supplemental CANONICAL-003 path; criterion 13 is met for the tested discriminator in the `vaidt/*` working repositories; criteria 14–16 remain not met.

---

## 13. Residuals

Residual IDs below are aligned to the active `DQ-006_FINAL_CLOSURE_EXECUTION_ORDER.md` (R1 discriminator; R2 RI-RS boundary; R3 evidence reachability; R4 ratification). No normative contract is changed.

| ID | Item / required disposition | Current status | Owner | Criterion |
|---|---|---|---|---|
| **R1** | CANONICAL-003 discriminator execution on both RI-PY and RI-RS, recording exact bytes, canonical digest and RFC 6962 leaf digest. The tested vector and its frozen oracle remain unchanged. | **TECHNICAL PASS — `vaidt/*` working repositories only; NON-NORMATIVE** | RI-PY + RI-RS | 13 (tested vector only) |
| **R2** | Select exactly one authoritative RI-RS conformance boundary and explicitly dispose of competing implementations / the upstream dependency-placement conflict. | **OPEN** — fork-level boundary identifiable; global source-of-record disposition unresolved | Protocol Custodian / operator | 15 |
| **R3** | Make the required evidence reachable from the named `Aura-IDToken/aura-poc-a-core-v3.3` and `Aura-IDToken/aura-guard-v1.3` default/reviewable branches, or use an immutable publication route formally accepted by the controlling record. | **OPEN** — `vaidt/*` reachability does not satisfy the current repository-identity criterion | RI-PY + RI-RS / operator | 14 |
| **R4** | Chief Architect reviews the complete evidence and explicitly ratifies the DQ-006 status transition after all required prior conditions have been met. | **OPEN — NOT PERFORMED** | Chief Architect | 16 |

Separate implementation/release control (not a replacement for R1–R4): the RI-PY production hash/Merkle change recorded in §9 requires an explicit version/profile and historical-certificate/evidence compatibility review before a production release. This review must not silently reinterpret historical evidence and does not itself ratify DQ-006.

Explicitly **not** residuals of DQ-006: CFL-001 (cross-corpus governance precedence) and CFL-005 (empty event-type registry). Both are reported in §14; neither is DQ-006's to resolve.

---

## 14. Reported conflicts — not resolved by this package

- **CFL-001** — the specification corpus and the implementation corpus make incompatible statements about canonical encoding, and no cross-corpus precedence rule exists in either. Binding APS-200 §8 settles the question *within the specification corpus*; it does not adjudicate which governance ladder wins cross-corpus. Routed to the Protocol Custodian.
- **CFL-005** — CANONICAL-001 carries `event_type: "AUDIT_RECORD"`, which the Event-Type Registry does not register, while requiring strict-mode rejection of unregistered tokens. Under the registry's own rule, strict conformance would reject the object this gate rests on. Canonicalization determines representation, never event semantics (APS-200 §8.7), so DQ-006 does not repair this. DQ-004 governs.
- **DQ-002 dependency** — [`closures/DQ-002_FINAL_CLOSURE.md`](DQ-002_FINAL_CLOSURE.md) records DQ-002 as CLOSED / PASS on the stated basis that DQ-006 is PASS. This package does not modify DQ-002. Its recorded closure basis predates CANONICAL-003 and relies on the historical CANONICAL-001 evidence discussed in D-1. Whether supplemental CANONICAL-003 evidence affects DQ-002's own closure basis requires a separate review; no status transition for DQ-002 or DQ-006 is inferred here.

---

## 15. Final verdict

```text
Normative specification contract   : CLOSED / SETTLED (APS-200 §8; APS-300 §5)
CANONICAL-003 discriminator result : PASS for tested vector in `vaidt/*`
Production-integrity criterion 10  : NOT MET for supplemental RI-PY path; scope deviation recorded
Evidence reachability criterion 14 : NOT MET
RI-RS boundary criterion 15        : NOT MET
Chief Architect ratification      : NOT PERFORMED

DQ-006 = OPEN
CONF-003 = PARTIAL
```

DQ-006 remains **OPEN**. The current reason is no longer that the corpus lacks any discriminator: CANONICAL-003 demonstrates the tested RFC 8785 distinctions on both working receivers. Closure remains incomplete because the evidence is not yet reachable under the named `Aura-IDToken/*` repository criterion, the authoritative RI-RS boundary is unresolved, criterion 10's production-integrity/scope condition is not met for the supplemental RI-PY path, and Chief Architect ratification has not been performed.

The normative contract in §3 is unchanged. This update reconciles the current evidence and records a scope deviation; it does not authorize production changes retroactively, silently reinterpret historical certificates/evidence, grant normative effect to CANONICAL-003, or perform ratification.

**No production runtime change is authorized or implied by this package.**

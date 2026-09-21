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

The **gate** is not closed. The executed cross-language evidence does not discriminate RFC 8785 from an ordinary sorted-JSON serializer, so it establishes implementation *agreement* rather than *profile conformance*. See §10 and §12.

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

---

## 5. RI-PY evidence

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

## 6. RI-RS evidence

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

## 7. Cross-language equality — CROSS-LANGUAGE-001

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

## 9. Production integrity

| Repository | Check | Result |
|---|---|---|
| RI-PY | `git diff -- core/ audit/` | empty |
| RI-RS | `git diff -- src/ Cargo.toml Cargo.lock` | empty |

The JCS engines are confined to conformance-only package boundaries in both repositories. No production hash, Merkle, event-type or protocol-semantics code was changed by CROSS-LANGUAGE-001.

---

## 10. Known deviations

### D-1 — CANONICAL-001 is JCS-degenerate · **SUBSTANTIVE**

For this object, `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` produces bytes identical to the frozen canonical bytes, and therefore the identical SHA-256 and the identical leaf. Verified by execution during this reconciliation.

A fully conforming RFC 8785 engine and a non-conforming sorted-JSON serializer are indistinguishable on this vector. CROSS-LANGUAGE-001 therefore establishes that RI-PY and RI-RS agree; it does not establish that either implements RFC 8785, which is the decision it is cited for.

Partial mitigation, RI-PY only: `test_jcs_behavior.py` (13 passed) exercises discriminating behaviour — ES6 number form, non-finite rejection, minimal escaping, raw UTF-8 for non-ASCII. RI-RS has no equivalent executed behavioural suite.

Recorded independently at [`ck003/handover-assessment/10_INDEPENDENT_VERIFICATION.md`](../ck003/handover-assessment/10_INDEPENDENT_VERIFICATION.md) §3.2 and [`05_EVIDENCE_GAPS.md`](../ck003/handover-assessment/05_EVIDENCE_GAPS.md) EG-01.

### D-2 — Evidence is not reachable from any default branch · **SUBSTANTIVE**

All four cited commits live on branches that are unmerged in their repositories, with no open pull request. A reviewer cloning either reference repository at `main` cannot locate the evidence. The commits were fetched and verified directly during this reconciliation and are intact, but reachability is a release-gate requirement, not a convenience.

### D-3 — RI-RS conformance boundary of record is not decided · **SUBSTANTIVE**

Three incompatible RI-RS implementations of this gate exist. Only the one cited above isolates the engine correctly; a competing open pull request would place a conformance-only engine in the production dependency graph. Recorded at [`ck003/handover-assessment/04_CONFLICT_REGISTER.md`](../ck003/handover-assessment/04_CONFLICT_REGISTER.md) CFL-003. Disposal of the other two is required.

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

Every link above is identified by repository path plus section, test or document identifier. Evidence-side paths resolve on the branches named in §5 and §6, not on `main` (deviation D-2).

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
| 10 | Production runtime unchanged | **MET** |
| 11 | Version and migration semantics recorded | **MET** — APS-200 §8.8, APS-300 §5.3 |
| 12 | Single normative authority; no competing definition | **MET** — APS-200 §8.2; superseded records marked |
| 13 | Evidence discriminates RFC 8785 from sorted JSON, cross-language | **NOT MET** — D-1 |
| 14 | Evidence reachable from each reference repository's default branch | **NOT MET** — D-2 |
| 15 | RI-RS conformance boundary of record decided, alternatives disposed | **NOT MET** — D-3 |
| 16 | Chief Architect ratification of the verdict | **NOT MET** — GOVERNANCE.md §2 |

Criteria 1–12 are met. Criteria 13–16 are not.

---

## 13. Residuals

Each residual is executable. None requires re-deciding the contract in §3.

| ID | Residual | Owner | Closes |
|---|---|---|---|
| **R1** | Add at least one JCS-discriminating cross-language vector to the CANONICAL corpus, execute it on both `rfc8785` 0.1.4 and `serde_json_canonicalizer` 0.3.2, and record the observed bytes. Strongest candidates: UTF-16 code-unit key ordering (e.g. keys `"é"`, `"z"`, `"😀"`, `"ﬀ"`) and ES6 number form (`-0.0` → `0`, `1.0` → `1`). No expected value may be written before it has been produced by execution. | RI-PY + RI-RS | 13 |
| **R2** | Merge the CANONICAL-001 evidence to the default branch of both reference repositories, or publish an equivalent reachable evidence artifact. | RI-PY + RI-RS | 14 |
| **R3** | Decide the RI-RS conformance boundary of record; close or dispose of the two competing implementations. | Protocol Custodian | 15 |
| **R4** | Ratify this verdict. | Chief Architect | 16 |

Explicitly **not** residuals of DQ-006: CFL-001 (cross-corpus governance precedence) and CFL-005 (empty event-type registry). Both are reported in §14; neither is DQ-006's to resolve.

---

## 14. Reported conflicts — not resolved by this package

- **CFL-001** — the specification corpus and the implementation corpus make incompatible statements about canonical encoding, and no cross-corpus precedence rule exists in either. Binding APS-200 §8 settles the question *within the specification corpus*; it does not adjudicate which governance ladder wins cross-corpus. Routed to the Protocol Custodian.
- **CFL-005** — CANONICAL-001 carries `event_type: "AUDIT_RECORD"`, which the Event-Type Registry does not register, while requiring strict-mode rejection of unregistered tokens. Under the registry's own rule, strict conformance would reject the object this gate rests on. Canonicalization determines representation, never event semantics (APS-200 §8.7), so DQ-006 does not repair this. DQ-004 governs.
- **DQ-002 dependency** — [`closures/DQ-002_FINAL_CLOSURE.md`](DQ-002_FINAL_CLOSURE.md) records DQ-002 as CLOSED / PASS on the stated basis that DQ-006 is PASS. This reconciliation does not modify DQ-002, but the Custodian should note that DQ-002's evidentiary basis inherits deviation D-1.

---

## 15. Final verdict

```text
Normative specification closure  : CLOSED   (criteria 1–12)
Conformance evidence closure     : PARTIAL  (criterion 13 not met)
Procedural closure               : OPEN     (criteria 14–16 not met)

DQ-006 = OPEN
```

DQ-006 is **not BLOCKED**: no unresolved decision stands in the way, and every residual in §13 has a defined executable path. It is **not CLOSED**: the corpus behind the closure cannot distinguish the profile it certifies, and the evidence is not reachable from any default branch.

The contract in §3 is settled and normatively bound. What remains is evidence, reachability and ratification.

**No production runtime change is implied or authorized by this package.**

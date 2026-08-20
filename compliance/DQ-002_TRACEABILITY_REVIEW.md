# DQ-002 — Traceability Review

**Document ID:** COMP-TR-DQ002-002
**Classification:** EVIDENCE — NON-NORMATIVE
**Audit date:** 2026-08-20
**Audit target:** `main` @ `19ddeef5672cd3d19a1049a31d85565396783a72` + current CK-003 closure material
**Companion matrix:** [DQ-002_TRACEABILITY_MATRIX.md](DQ-002_TRACEABILITY_MATRIX.md)

> This review does not reopen DQ-002, does not alter its normative semantics, does not approve
> any ADR, and creates no competing closure document. It reports what the repository does and
> does not support.

---

## 1. Verdict

```text
DQ-002 TRACEABILITY = FAIL
```

`FAIL` is the defined outcome when "an actual contradiction or missing mandatory evidence
exists." Both conditions are met. `BLOCKED` does not apply: the repository state permitted a
complete verification, including retrieval and independent recomputation of the cited artifacts.

**What this verdict is not.** It is not a finding that the DQ-002 hash-domain semantics are
wrong. Every arithmetic value published under DQ-002 that this audit could check was
independently recomputed and **matched**. The failure is in the traceability chain around those
values, not in the values themselves.

---

## 2. Decision consistency (order §1)

| Reference | Consistent with `closures/DQ-002_FINAL_CLOSURE.md`? |
|---|---|
| APS-001 | **Partially.** §7.1/§7.2 state exactly the DQ-002 leaf/node domains and the raw-bytes rule. But APS-001 is `0.2-DRAFT / DRAFT — ARCHITECTURE REVIEW REQUIRED`, §7.1 calls the model "**proposed**", and §7.2 defers tree construction to "the approved Aura Merkle profile", which does not exist. |
| APS-200 | **No.** §8:218 is still `TODO`; document is DRAFT. The closure's §2.1 asserts a "frozen RFC 8785 JCS profile" that APS-200 does not contain. |
| APS-300 | **No.** §5:73 leaves `evidence_hash` algorithm `TODO`, and APS-300 contains **no** Merkle, RFC-6962 or `0x00`/`0x01` language whatsoever. |
| APS-400 | **No.** CONF-003 and CONF-010 are both `DRAFT`; no Merkle conformance test is assigned. |
| APS-500 | **No.** CANONICAL-001 appears **zero** times in APS-500; §5 fixture data is `TODO`. |
| DQ-006 | **Yes** for canonicalization/leaf. `closures/DQ-006_CLOSURE_PACKAGE.md` §11 names DQ-002 as the next dependent closure, and DQ-002 §6 records the dependency. The two are mutually consistent. |
| CANONICAL-001 | **Values yes, status no.** The digests are correct (§3). But `fixtures/corpus/CANONICAL-001_jcs_evidence.json` still records `"RI-PY": "PENDING_EXECUTION"`, `"RI-RS": "PENDING_EXECUTION"`, `"cross_language_equality": "PENDING_EXECUTION"` — the fixture underlying a CLOSED gate declares its own execution pending. |

---

## 3. Artifact verification (order §3) — all values confirmed

Recomputed in this audit from the published canonical bytes, using an implementation
independent of both RIs:

| Quantity | Published | Recomputed | Result |
|---|---|---|---|
| Canonical byte length | 100 | 100 | **MATCH** |
| Decoded canonical bytes | — | `{"event_type":"AUDIT_RECORD","payload":{"value":42},"protocol_version":"1.0","schema_version":"1.0"}` | consistent with the declared input object |
| `SHA-256(B)` | `b6c3660c…39a4e6` | `b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6` | **MATCH** |
| `SHA-256(0x00 ‖ B)` | `ce6b3673…48c039` | `ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039` | **MATCH** |
| `SHA-256(0x01 ‖ B)` (control) | — | `491a8dcc…9a10b1` | differs from the leaf, so the domain separator is discriminating |

These three values are byte-identical everywhere they appear: `closures/DQ-002_FINAL_CLOSURE.md`,
`closures/DQ-006_CLOSURE_PACKAGE.md`, `evidence/DQ-006_CLOSURE_PACKAGE.md`,
`ck003/DQ-006_CLOSURE.md`, `ck003/DQ-006_EVIDENCE_INDEX.md`,
`ck003/dq-006-closure/DQ-006-CLOSURE.md` and `fixtures/corpus/CANONICAL-001_jcs_evidence.json`.
**No transcription divergence was found.**

---

## 4. Cross-language chain (order §4) — verified for the leaf boundary

The four cited commits are **retrievable**, contrary to a stricter reading of `CFL-004`. All
four resolve, in both reference repositories, on branch
`claude/cross-language-canonical-001-n4v2c5`. None is reachable from any `main`.

| Side | Execution commit | Evidence/HEAD commit | Reachable from `main`? |
|---|---|---|---|
| RI-PY | `49d0e4f6…9a56f` | `3e8e0e32…8c4e` | **No** |
| RI-RS | `4e9e2284…7aaa2` | `420653e2…2bb2a0` | **No** |

Artifact hashes, recomputed from the retrieved blobs, match `ck003/DQ-006_EVIDENCE_INDEX.md`
exactly:

| Artifact | Recomputed SHA-256 | Index value | Result |
|---|---|---|---|
| `conformance/corpus/canonical-001/ri-py.json` | `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c` | same | **MATCH** |
| `conformance/corpus/canonical-001/ri-rs.json` | `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` | same | **MATCH** |

Both artifacts declare the same `input_sha256` (`649bb748…39261`), the same canonical bytes,
the same `sha256`, the same `leaf_sha256`, `worktree_clean: true`, and different engines
(`rfc8785 0.1.4` / `serde_json_canonicalizer 0.3.2`) under different toolchains. The chain
`RI-PY → engine → bytes → SHA → leaf` and `RI-RS → engine → bytes → SHA → leaf`, and the
equality `RI-PY == RI-RS`, are **established for the canonicalization and leaf boundary**.

**Two limits of that chain, both material to DQ-002:**

1. **No node, no root.** Neither artifact contains an interior-node digest or a Merkle root.
   CROSS-LANGUAGE-001 does not test the `0x01` domain at all. DQ-002 §2.6 nevertheless asserts
   it, and `closures/DQ-002_FINAL_CLOSURE.md` §4 cites **only** CANONICAL-001 and JCS-B01…B06
   as its conformance evidence — CROSS-LANGUAGE-002 is not referenced anywhere in the closure.
   The closure freezes a Merkle contract on canonicalization evidence.
2. **The vector does not discriminate the profile.** Recomputation confirms that ordinary
   sorted-key compact JSON produces byte-identical output to the RFC 8785 result for this
   object. Cross-language *agreement* is proven; conformance to RFC 8785 specifically is not.
   This reproduces the finding already recorded as `RB-04`/`EG-02`.

---

## 5. Production boundary (order §5) — consistent

No contradiction was found. Every closure artifact states the same rule, and the statements
agree with each other:

- `closures/DQ-002_FINAL_CLOSURE.md` §5 — "not a mandate to introduce JCS into production runtime".
- `closures/DQ-006_CLOSURE_PACKAGE.md` §7, §10 — JCS conformance-only; does not authorize insertion into production runtime.
- `ck003/DQ-006_EVIDENCE_INDEX.md` — "does not authorize production runtime changes".
- `ck003/dq-006-closure/DQ-006-CLOSURE.md` §0.2, §7, §10 — same.
- `ck003/README.md` operating rule — "No production implementation change is implied by a CK-003 evidence artifact."

Supporting evidence: RI-RS provenance records a separate conformance lockfile
(`conformance/Cargo.lock`, `3ff49a0f…`), so the JCS engine is outside the production
dependency graph. RI-PY `main` retains the legacy `audit/merkle.py` — which is **correct**
under the ADR's own migration rule forbidding recomputation of historical evidence as if
unchanged.

**Confirmed:** JCS = conformance-only; hash/Merkle production semantics frozen independently.

**One standing risk, not a contradiction in the closure:** `CFL-003` records RI-RS PR #59
(`ck003/canonical-001-conformance`) placing the JCS engine in the **root `Cargo.toml`
`[dependencies]`**. Merging it as-is would breach the boundary this closure asserts. It is open,
outside this audit's authority, and listed below for disposition.

---

## 6. Contradictions

**C-1 — The Merkle evidence gate carries two incompatible statuses.** *(new; not in the existing conflict register)*

| Artifact | Recorded status |
|---|---|
| `ck003/dq-002-hash-domain/CROSS-LANGUAGE-002-EVIDENCE.md` §12 | `CONDITIONAL PASS`, with full N = 0…8 root, audit-path and NC-1…NC-10 coverage |
| `ck003/cross-language-002/CROSS-LANGUAGE-002-EVIDENCE.md` §5 | `OPEN — execution gate not yet PASS`; `RI-PY actual execution: NOT PASS`; `RI-RS actual execution: NOT RUN`; `Root equality: NOT ESTABLISHED` |

Both are present at HEAD. Neither cites the other. Neither is marked `SUPERSEDED`, although
`ck003/README.md` defines that token. The second is a **preflight** document whose RI-PY
negative-preflight root (`fb8e20fc…`) was superseded by the actual execution recorded in the
first — but nothing in the repository says so.

**C-2 — The evidence ledger and the closure disagree about whether DQ-002 is closed.**

`ck003/dq-002-hash-domain/CROSS-LANGUAGE-002-EVIDENCE.md` ends: *"**DQ-002 remains OPEN. This
document does not close it.**"* `closures/DQ-002_FINAL_CLOSURE.md` §8: *"**DQ-002 = CLOSED /
PASS.** The hash-domain contract is frozen and backed by executable cross-language evidence."*
The document holding the executable cross-language Merkle evidence denies closing the gate that
the closure says it backs.

**C-3 — A frozen contract above an unapproved ADR.**

`ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` remains `PROPOSED — awaiting Chief
Architect approval`, with **all six** items in its own "Conformance gate" unchecked, including
"APS-200 §8 updated with the canonical byte-level rule" and "APS-500 fixture promoted from
proposal to normative fixture". `ck003/dq-002-hash-domain/README.md` reads `Status: Evidence /
decision proposal — NOT APPROVED`. This is the DQ-002 analogue of `CFL-002`.

**C-4 — The invariant matrix contradicts the closure.**

`ck003/APS001_INV_MATRIX/INV-001_015_CONFORMANCE_MATRIX.md` records INV-003 as
`BLOCKED — APS-200 serialization still open` and INV-011 as `OPEN — DQ-002 + canonical bytes
required`. Both are the invariants DQ-002 directly serves.

**C-5 — The fixture underlying the closure declares its own execution pending.**

`fixtures/corpus/CANONICAL-001_jcs_evidence.json` lines 27–29 remain `PENDING_EXECUTION` for
RI-PY, RI-RS and cross-language equality. `fixtures/ck003/manifest.json` records
`canonicalization_profile: UNBOUND_PENDING_APS-200_CLOSURE`, and
`fixtures/ck003/expected_digests.json` is `EXPECTED_VALUES_PENDING_CANONICAL_SERIALIZATION`.
This extends `CFL-002` to the DQ-002 corpus.

---

## 7. Gaps

| ID | Gap | Consequence |
|---|---|---|
| GAP-01 | APS-200 §8 canonical serialization is `TODO`; APS-200 is DRAFT | R-01 has no frozen normative source |
| GAP-02 | APS-300 §5 `evidence_hash` algorithm is `TODO`; APS-300 contains no Merkle/RFC-6962 language at all | R-02/R-03 have no APS-300 anchor |
| GAP-03 | CANONICAL-001 is not registered in APS-500 (0 occurrences); APS-500 §5 is `TODO` | The fixture link in the compliance chain is unbacked |
| GAP-04 | CONF-003 and CONF-010 are DRAFT, carry `TODO` preconditions, and cite `FIX-001`, not CANONICAL-001 | The conformance-requirement link is unbacked |
| GAP-05 | APS-001 is `0.2-DRAFT — ARCHITECTURE REVIEW REQUIRED`; §7.1 calls the hash-domain model "proposed"; §7.2 defers to an "approved Aura Merkle profile" that does not exist | The one APS carrying the DQ-002 domains is not approved |
| **GAP-06** | **No CONF-nnn covers the Merkle leaf domain, interior-node domain, tree shape, or inclusion proofs** | Six of ten DQ-002 requirements have no conformance requirement to trace to. Largest structural gap. |
| GAP-07 | RI-PY `conformance/merkle/` (10 files, the entire RI-PY DQ-002 suite) exists only on `claude/aura-cross-language-002-6t2kdo`; RI-PY `main` has no DQ-002 conformance test | Half the cross-language Merkle evidence is unreachable from any default branch |
| GAP-08 | All four CANONICAL-001 evidence commits live only on `claude/cross-language-canonical-001-n4v2c5` in both RIs, with no open PR | A reviewer cloning at `main` cannot reproduce the closure's evidence (`CFL-004`, `EG-01`) |
| GAP-09 | `DEFECT-DQ002-F1` OPEN — `node.digest_hex` in `03_cross_language_fixture.json` (self-designated `NORMATIVE_TEST_VECTOR`) is not the SHA-256 of the preimage the same file declares | A published normative vector carries a wrong value; correctly left for Custodian action |
| GAP-10 | `DEFECT-DQ002-F2` OPEN — DQ-002 is silent on tree-size binding; an RFC-6962 audit path does not authenticate `tree_size` | An implementer could build an unsupported evidence claim |
| GAP-11 | `DEFECT-DQ002-F3` OPEN — RI-PY's suite cannot be collected without `--ignore` | No repository-wide green run exists to cite |
| GAP-12 | No CI execution for any DQ-002 cross-language claim; `CROSS-LANGUAGE-002-EVIDENCE.md` §11 records "CI enforces any of the above: **NOT EXECUTED**" | All evidence is local-runner only |
| GAP-13 | CROSS-LANGUAGE-001's vector does not discriminate RFC 8785 from sorted-compact JSON (confirmed by recomputation) | Agreement is proven; profile conformance is not (`RB-04`) |
| GAP-14 | `CFL-005` — the event-type registry is empty, so strict conformance would reject CANONICAL-001's `AUDIT_RECORD` token | The object under the closed gate is not a registered protocol object |

---

## 8. Cleanup candidates

**Nothing was deleted, edited, or re-statused by this audit.** These are proposals for
Protocol Custodian action; status changes are a human act under `GOVERNANCE.md` §2.

### 8.1 Duplicate closure documents

Four DQ-006 closure documents coexist, all distinct, none cross-referencing the others:

| File | Lines | Suggested disposition |
|---|---|---|
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 130 | **Retain as normative** — newest, in the dedicated `closures/` hierarchy |
| `evidence/DQ-006_CLOSURE_PACKAGE.md` | 202 | Mark `SUPERSEDED` → `closures/` |
| `ck003/dq-006-closure/DQ-006-CLOSURE.md` | 258 | **Retain as the CK-003 workspace record** — this is the only one carrying the Two-Key approval record |
| `ck003/DQ-006_CLOSURE.md` | 160 | Mark `SUPERSEDED` |

> Consistency note: the GOV-001/DQ-006 integration recorded the Key 1 / Key 2 approval block in
> `ck003/dq-006-closure/DQ-006-CLOSURE.md` only. The other three carry `CLOSED — PASS` with no
> approval record. Whichever document is retained as normative should carry the approval block.

### 8.2 Duplicate DQ-002 ADRs

`ck003/dq-002-hash-domain/02_hash_domain_adr.md` and
`ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` are two distinct PROPOSED ADRs for
the same decision. They were compared clause by clause and are **semantically consistent**
(same leaf `0x00`, node `0x01`, raw-byte and RFC-6962 rules); the second is the fuller text.
Suggested: retain `ADR-CK003-DQ002-HASH-DOMAIN.md`, mark `02_hash_domain_adr.md` `SUPERSEDED`.

### 8.3 Contradicting CROSS-LANGUAGE-002 evidence

`ck003/cross-language-002/CROSS-LANGUAGE-002-EVIDENCE.md` is a **preflight** document
superseded in fact by `ck003/dq-002-hash-domain/CROSS-LANGUAGE-002-EVIDENCE.md`. Marking the
preflight `SUPERSEDED`, with a pointer to the execution ledger, resolves **C-1** without
touching any semantics. This is the single highest-value, lowest-risk cleanup available.

### 8.4 Stale fixture status fields

`fixtures/corpus/CANONICAL-001_jcs_evidence.json` (`PENDING_EXECUTION` ×3),
`fixtures/ck003/manifest.json` (`UNBOUND_PENDING_APS-200_CLOSURE`) and
`fixtures/ck003/expected_digests.json` (`EXPECTED_VALUES_PENDING_CANONICAL_SERIALIZATION`)
contradict the closed gates. These are **status fields only** — every digest in them is
correct. Reconciling them is a Custodian decision, not an agent edit, because
`expected_digests.json` carries its own rule: *"null is intentional and MUST NOT be
interpreted as zero, empty digest, or PASS."*

### 8.5 Historical, correctly retained

`ck003/handover-assessment/*` and `ck003/legacy/*` self-declare as non-normative assessments
and should be retained as the historical record. `ck003/dq-002-hash-domain/DEFECT-DQ002-F{1,2,3}.md`
are OPEN defect records and must be retained until resolved.

---

## 9. What would move DQ-002 to PASS

Ordered by dependency. None of these is an agent action.

1. Resolve **C-1** by marking the preflight CROSS-LANGUAGE-002 document `SUPERSEDED`.
2. Approve `ADR-CK003-DQ002-HASH-DOMAIN` and check off its own six-item conformance gate (**C-3**).
3. Freeze APS-200 §8 and reconcile APS-300 (**GAP-01, GAP-02**).
4. Assign a Merkle conformance requirement — leaf, node, tree shape, inclusion proof (**GAP-06**).
5. Register CANONICAL-001 and the DQ-002 fixtures in APS-500 (**GAP-03**).
6. Merge, or open PRs for, the RI-PY and RI-RS evidence branches (**GAP-07, GAP-08**).
7. Add a second cross-language vector that discriminates RFC 8785 from sorted-compact JSON (**GAP-13**).
8. Resolve `DEFECT-DQ002-F1` and state DQ-002's position on tree-size binding (**GAP-09, GAP-10**).
9. Put the equality runners under CI (**GAP-12**).
10. Reconcile the fixture status fields and the INV matrix (**C-4, C-5**).

---

## 10. Audit provenance

| Item | Value |
|---|---|
| Specification repository HEAD audited | `19ddeef5672cd3d19a1049a31d85565396783a72` (`origin/main`) |
| RI-PY repository | `Aura-IDToken/aura-poc-a-core-v3.3`, full remote fetch, 76 remote branches |
| RI-RS repository | `Aura-IDToken/aura-guard-v1.3`, full remote fetch, 45 remote branches |
| Implementations re-run | **No.** Order §4 permits re-running only to resolve evidence ambiguity; none required. Digests were recomputed from published bytes by an independent implementation, and artifact blobs were read directly from the cited commits. |
| Production code modified | **No** |
| DQ-002 semantics modified | **No** |
| Competing closure document created | **No** |

---

*This review records traceability findings and resolves none of them. It confers no normative
semantics. Status changes and defect corrections remain Protocol Custodian actions under
`GOVERNANCE.md` §2.*

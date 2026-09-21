# AURA — DOCUMENTATION NORMALIZATION AUDIT v1

**Record type:** Observational audit record — read-only normalization analysis
**Date (UTC):** 2026-08-25
**Disposition:** **AUDIT COMPLETE — DIAGNOSTIC. NOTHING RESOLVED, NOTHING REPAIRED.**

| Item | State |
|---|---|
| Document class of this record | AUDIT (observational) |
| Normative authority | **NONE** |
| Conformance authority | **NONE** |
| Execution authority | **NONE** |
| Decisions made | **NONE** |
| Artifacts modified | **NONE** |
| C-1 · C-2 | UNCHANGED — OPEN |
| Decision A · Decision B | UNCHANGED — OPEN |
| ARI semantics | UNCHANGED — UNRESOLVED |
| B-VAL-012 · B-VAL-014 · BNC-1 · §4.5 | NOT EXECUTED / NO RESULT |
| Registry · issuance · fixtures | NOT CREATED / NOT MODIFIED |

## Authority notice

This is an **observational audit record**. It is not a specification, not a
governance decision, not an authority artifact, and not a decision package. It
creates no normative semantics, promotes nothing to authority, and settles
nothing.

Where this record uses the words *observed*, *recorded*, *declared* or
*reachable*, they are statements about the corpus as read on the date above.
Where a source's own token is quoted, it is quoted verbatim and is **not**
replaced. Every normalized reading given alongside a source token is a reading
aid attached to this audit only; it does not amend the source.

**No artifact under audit was edited, renamed, moved, merged or repaired.**

---

## 1. SCOPE AND METHOD

### 1.1 Repositories in scope

| Repository | `main`/`master` at audit time | Working tree at audit time |
|---|---|---|
| `Aura-IDToken/aura-specification` | `528de0de6d34a4a7ff541db9cd93238587dac9ef` | clean |
| `Aura-IDToken/aura-poc-a-core-v3.3` | `43f054f8deb7c9644c52148d6496b493512d32b0` | clean |
| `Aura-IDToken/aura-guard-v1.3` | `35082d7b4880dad780fb55a1a5f3ac0ef4322674` | clean |
| `Aura-IDToken/.github` | `95f017a833950d77542ebcf579a8c172f9027173` | clean |
| `Aura-IDToken/cargo` | `92e3ebe…` (vendored upstream mirror) | clean |

### 1.2 Reference sets actually searched

Reachability and absence claims in this record are bounded by the ref sets
below. Where a ref set is partial, the bound is stated at the point of use.

| Repository | Remote heads | Refs fetched and searched | Coverage |
|---|---|---|---|
| `aura-specification` | 56 | **all 56 heads + 1 tag** | complete |
| `aura-poc-a-core-v3.3` | 79 | **all 79 heads** | complete |
| `aura-guard-v1.3` | not enumerated | `main` (checkout) | **partial — branch coverage NOT ESTABLISHED** |
| `.github` | not enumerated | default branch (checkout) | **partial** |
| `cargo` | not enumerated | default branch (checkout) | **partial — no Aura governance content observed** |

Token searches over `aura-specification` and `aura-poc-a-core-v3.3` were run
across `git rev-list --all` rather than over a checkout, so an absent token is
absent from every commit reachable from every fetched ref of those two
repositories. For `aura-guard-v1.3`, `.github` and `cargo`, absence is asserted
only for the checked-out branch.

### 1.3 Method

Read-only. Files were read; git objects were resolved; two digests were
recomputed (§1.4). No program under audit was executed, no receiver was
invoked, no test suite was run, no conformance procedure was entered.

### 1.4 Recomputation performed (read-only, non-authoritative)

Two integrity facts were recomputed rather than copied, so that this record does
not merely restate a claim it cannot check:

| Object | Recomputed value | Method |
|---|---|---|
| `conformance/boundary/p01/FIX-DIGEST-P01.canonical.json` (bytes) | 15 octets; content `{"a":1,"b":"x"}`; SHA-256 `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` | `wc -c`, `sha256sum` on the worktree file |
| same file (git identity) | blob `b45ffa980a1a776b6143d7fcb255fbfa8a436582` | `git ls-tree origin/main` |

Both agree with the values recorded in `BC-02-CUSTODIAN-CLOSURE-RECORD.md` §6
and in the two Decision Packages. **This is a byte-identity check only.** It is
not an issuance check, not a conformance check, and establishes nothing about
authority. See AD-N-011.

### 1.5 Identifier namespaces used by this record

The corpus already occupies several short identifier namespaces (`N-01…N-17`,
`D-1…D-10`, `DIV-01…DIV-07`, `CFL-001…005`, `C-1/C-2`, `A-1…A-8`, `B-1…B-5`,
`S-1…S-18`, `PRE-01-*`). To avoid adding to the collisions this audit is
recording, every identifier minted here carries an `AD-` prefix:

| Prefix | Meaning |
|---|---|
| `AD-I-nnn` | inventory record |
| `AD-DIV-nnn` | declaration-vs-content divergence |
| `AD-CFL-nnn` | conflict register entry |
| `AD-N-nnn` | normalization finding |
| `AD-OS-nnn` | open load-bearing surface |

The mandate for this audit specifies findings numbered `N-001…`. Those findings
appear here as `AD-N-001…`; the `AD-` prefix is a collision-avoidance measure
recorded as AD-N-021, not a renumbering of anything in the corpus.

---

## 2. DOCUMENT INVENTORY

52 load-bearing artifacts are inventoried. Each appears once in an **identity**
table (repository, path, commit, blob, reachability, class) and once in a
**status** table (declared status, content-observed status, authority claim,
authority evidence, semantic status, evidence status, execution status,
supersession evidence, dependencies, conflicts, notes).

Reachability vocabulary: `REACHABLE_FROM_MAIN` · `BRANCH_LOCAL` · `UNREACHABLE`
· `UNKNOWN`. Blob identifiers are truncated to 12 hex characters where the full
value is not load-bearing.

### 2.1 Group A — Constitutional and governance (aura-specification)

| ID | Repository | Path | Commit | Blob | Reachability | Class |
|---|---|---|---|---|---|---|
| AD-I-001 | aura-specification | `constitution/AURA_CONSTITUTION.md` | `b68181e` | `9be4bf9249d4` | REACHABLE_FROM_MAIN | GOVERNANCE |
| AD-I-002 | aura-specification | `AURA Constitution_260723_190157.txt` | `5f91167` | `bf28a0b210f5` | REACHABLE_FROM_MAIN | GOVERNANCE (duplicate representation) |
| AD-I-003 | aura-specification | `AURA Constitution_260723_190157.pdf` | `5f91167` | (binary) | REACHABLE_FROM_MAIN | GOVERNANCE (duplicate representation) |
| AD-I-004 | aura-specification | `GOVERNANCE.md` | `b68181e` | `38acf33e95a8` | REACHABLE_FROM_MAIN | GOVERNANCE |
| AD-I-005 | aura-specification | `STYLE_GUIDE.md` | `b68181e` | `711ec7ec27fd` | REACHABLE_FROM_MAIN | GOVERNANCE |
| AD-I-006 | aura-specification | `releases/v0.1.0/DOCUMENT_STATUS.md` | `b68181e` | `08f4e0ceec08` | REACHABLE_FROM_MAIN | AUTHORITY_RECORD (status snapshot) |
| AD-I-007 | aura-specification | `adrs/ADR-001_DOCUMENT_MODEL.md` | `3c68a36` | `66083e286a2f` | REACHABLE_FROM_MAIN | DECISION_RECORD |
| AD-I-008 | aura-specification | `adrs/ADR-001_REPOSITORY_STRUCTURE.md` | `b68181e` | `3df6315b5b98` | REACHABLE_FROM_MAIN | DECISION_RECORD |
| AD-I-009 | aura-specification | `docs/adr/001-document-model.md` | `c4ba215` | `340ed584082b` | REACHABLE_FROM_MAIN | DECISION_RECORD (duplicate representation) |

| ID | Declared status (verbatim) | Content-observed | Authority claim | Authority evidence | Semantic | Evidence | Execution | Supersession | Dependencies | Conflicts | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AD-I-001 | `Status: FROZEN` | English text; Art. VIII / XI cited throughout the corpus as top authority | Explicit — canonical governance document, Owner: Chief Architect | Self-declared; no external ratification artifact observed | ESTABLISHED | OBSERVED | N/A | NOT ESTABLISHED | — | AD-CFL-001, AD-CFL-002 | Cited as precedence tier 1 by `CLAUDE.md` |
| AD-I-002 | `Status: FROZEN (po zatwierdzeniu)` | **Polish** text, same Document ID `AURA-CON-001`, same Version `1.0` | Same document ID as AD-I-001 | none beyond self-declaration | NOT DETERMINED | CONFLICTING | N/A | **NOT ESTABLISHED** | AD-I-001 | AD-CFL-001 | Declared status is *conditional* (`po zatwierdzeniu` = "after approval"); AD-I-001's is unconditional |
| AD-I-003 | as AD-I-002 | binary; not machine-diffable in this audit | as AD-I-002 | none | UNKNOWN | NONE | N/A | NOT ESTABLISHED | AD-I-002 | AD-CFL-001 | Content not verified — binary |
| AD-I-004 | `1.0-DRAFT` / DRAFT (per AD-I-006) | Defines approval routes cited by ARI authority analysis | Governance process authority | DRAFT status declared | PROPOSED | PARTIAL | N/A | NOT ESTABLISHED | AD-I-001 | AD-CFL-004 | GOV-001; body "Architecture Review Board" has no established existence per core OQ-A |
| AD-I-005 | `1.0-DRAFT` | §12: *"English only in all normative documents"* | Style authority | DRAFT | PROPOSED | OBSERVED | N/A | NOT ESTABLISHED | — | AD-CFL-001 | Directly bears on AD-I-002/003 and the APS duplicates |
| AD-I-006 | table of per-document statuses, dated 2026-07-23 | Lists APS-001 as `0.1-DRAFT` / `TODO` | Snapshot, no authority claimed | — | SUPERSEDED-IN-FACT? **NOT ESTABLISHED** | CONFLICTING | N/A | **NOT ESTABLISHED** | AD-I-010…017 | AD-DIV-001 | No supersession marker anywhere |
| AD-I-007 | `Status: PROPOSED` | Document model ARC→SPEC→APS; assigns SPEC approval to Protocol Custodian | Explicit, conditional on acceptance | Not accepted | PROPOSED | PARTIAL | N/A | NOT ESTABLISHED | AD-I-009 | AD-CFL-003 | Same ID as AD-I-008 and AD-I-009 |
| AD-I-008 | `Status: ACCEPTED` | Repository structure | Explicit | `Supersedes: —`, `Superseded By: —` | ESTABLISHED | OBSERVED | N/A | NOT ESTABLISHED | — | AD-CFL-003 | Same ID `ADR-001`, different subject |
| AD-I-009 | `Status: DRAFT`, `Version: 1.0` | **Same title and body subject as AD-I-007**, different status | Explicit | — | PROPOSED | CONFLICTING | N/A | NOT ESTABLISHED | AD-I-007 | AD-CFL-003 | Two copies of one ADR at two paths with two statuses |

### 2.2 Group B — APS specification set and its duplicate representations

| ID | Repository | Path | Commit | Blob | Reachability | Class |
|---|---|---|---|---|---|---|
| AD-I-010 | aura-specification | `specification/APS-001_PROTOCOL_SPECIFICATION.md` | `ff30e16` | `bfbc7aff33a7` | REACHABLE_FROM_MAIN | SPECIFICATION |
| AD-I-011 | aura-specification | `aps/APS-000_FOUNDATION_AND_TERMINOLOGY.md` | — | — | REACHABLE_FROM_MAIN | SPECIFICATION |
| AD-I-012 | aura-specification | `aps/APS-100_PROTOCOL_INVARIANTS.md` | `b68181e` | `e1d4fa52288a` | REACHABLE_FROM_MAIN | SPECIFICATION |
| AD-I-013 | aura-specification | `aps/APS-200_CANONICAL_DATA_MODEL.md` | `9682cf5` | `0488eec04e10` | REACHABLE_FROM_MAIN | SPECIFICATION |
| AD-I-014 | aura-specification | `aps/APS-300_EVIDENCE_MODEL.md` | `ff30e16` | `347112b0aa61` | REACHABLE_FROM_MAIN | SPECIFICATION |
| AD-I-015 | aura-specification | `aps/APS-400_CONFORMANCE_TEST_MATRIX.md` | `9bbfdde` | `769dab5fae53` | REACHABLE_FROM_MAIN | CONFORMANCE |
| AD-I-016 | aura-specification | `aps/APS-500_REFERENCE_FIXTURES.md` | `b68181e` | `efeaceafcbae` | REACHABLE_FROM_MAIN | FIXTURE (specification of) |
| AD-I-017 | aura-specification | `aps/APS-950_REFERENCE_IMPLEMENTATION_REQUIREMENTS.md` | `b68181e` | `c5d7f0400292` | REACHABLE_FROM_MAIN | SPECIFICATION |
| AD-I-018 | aura-specification | `APS-200 — Canonical Data Model_260723_192852.txt` | `5f91167` | `559e0e0c0bfb` | REACHABLE_FROM_MAIN | SPECIFICATION (duplicate representation) |
| AD-I-019 | aura-specification | 7 further root-level `APS-*.txt` + 8 `*.pdf` pairs | `5f91167` | various | REACHABLE_FROM_MAIN | SPECIFICATION (duplicate representations) |
| AD-I-020 | aura-specification | `invariants/INVARIANT_REGISTRY.md` | `5917fe9` | `2bd65af771ba` | REACHABLE_FROM_MAIN | SPECIFICATION |
| AD-I-021 | aura-specification | `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | `ff30e16` | `28d474e77e7a` | REACHABLE_FROM_MAIN | CONFORMANCE |
| AD-I-022 | aura-specification | `glossary/GLOSSARY.md` | `b68181e` | `4081e042e4f4` | REACHABLE_FROM_MAIN | SPECIFICATION (terminology) |

| ID | Declared status (verbatim) | Content-observed | Authority claim | Authority evidence | Semantic | Evidence | Execution | Supersession | Dependencies | Conflicts | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AD-I-010 | `Version: 0.2-DRAFT` · `Status: DRAFT — ARCHITECTURE REVIEW REQUIRED` | Root normative specification | *"Root Normative Specification"*, Authority: Constitution | Constitution is FROZEN; APS-001 itself not approved | PROPOSED | PARTIAL | N/A | NOT ESTABLISHED | AD-I-001 | AD-DIV-001 | AD-I-006 records this document as `0.1-DRAFT` / `TODO` |
| AD-I-011…017 | each `Version: 1.0-DRAFT` · `Status: DRAFT` | each declares `Classification: Normative Specification` | Normative classification declared while DRAFT | none beyond declaration | PROPOSED | PARTIAL | N/A | NOT ESTABLISHED | AD-I-010 | AD-DIV-002 | Precedence tier 2 in `CLAUDE.md` is occupied entirely by DRAFT documents |
| AD-I-018 | `Status: DRAFT`, same ID/version as AD-I-013 | **Polish**; 2 909 octets against AD-I-013's 11 445 | Same document ID | none | NOT DETERMINED | CONFLICTING | N/A | **NOT ESTABLISHED** | AD-I-013 | AD-CFL-001 | Two documents, one ID, one declared version, two languages, 4× size difference |
| AD-I-019 | as AD-I-018 | not individually diffed in this audit | same document IDs as AD-I-011…017 | none | UNKNOWN | NONE | N/A | NOT ESTABLISHED | AD-I-011…017 | AD-CFL-001 | Recorded as a class; per-file content comparison NOT PERFORMED |
| AD-I-020 | `1.0-DRAFT` | 15 invariants INV-001…015 | Authority: APS-100 | DRAFT | PROPOSED | PARTIAL | N/A | NOT ESTABLISHED | AD-I-012 | — | Precedence tier 3 |
| AD-I-021 | `Version: 1.1-DRAFT` · `Status: DRAFT` — body: *"This document is a normative conformance requirement."* | Declares itself normative in the body while DRAFT in the header | Explicit normative claim | Authority: APS-400 §4 (itself DRAFT) | NOT DETERMINED | CONFLICTING | NOT EXECUTED (§4.5 — NO RESULT) | NOT ESTABLISHED | AD-I-015 | **AD-DIV-002** | §4.5 is the execution point every BC-02 record defers to |
| AD-I-022 | `1.0-DRAFT` | Lines 27–28: ARI *"computed by RI-PY … a measurement, not a decision"* | none | — | OPEN | OBSERVED | N/A | NOT ESTABLISHED | — | AD-CFL-006 | **The only occurrence of ARI in the entire specification corpus.** Defines by deferral to an implementation |

### 2.3 Group C — BC-02 chain, reachable from `aura-specification/main`

| ID | Path (under `conformance/boundary/`) | Commit | Blob | Reachability | Class |
|---|---|---|---|---|---|
| AD-I-023 | `BC-02.1-COMMON-RECEIPT-SCHEMA-v1.md` | `7d1977f` | `f40f7a2ea246f382d12490a6489159f9e226fd17` | REACHABLE_FROM_MAIN | ENGINEERING_CONTRACT |
| AD-I-024 | `BC-02.3-RI-RS-RECEIVER-v1.md` | `49e848a` | `e9bb28edbd87bafc05bd2f3fe1410d6abac6a77a` | REACHABLE_FROM_MAIN | ENGINEERING_CONTRACT |
| AD-I-025 | `BC-02-CROSS-RECEIVER-PREEXEC-AUDIT.md` | `5f226e6` → `528de0d` | `a9c7272ea6f64eb4ad52864cd418ec189999170e` | REACHABLE_FROM_MAIN | AUDIT |
| AD-I-026 | `CONTROLLED-P01-HANDOFF-RECORD.md` | `927e524` → `528de0d` | `fe3de6b4af0a872892cdb07b94bf0c2620c74c8f` | REACHABLE_FROM_MAIN | EVIDENCE |
| AD-I-027 | `BC-02-CUSTODIAN-CLOSURE-RECORD.md` | `68495e0` → `528de0d` | `044f16a83ef42b9c9356372bf3def805b2a43404` | REACHABLE_FROM_MAIN | AUTHORITY_RECORD (claimed) |
| AD-I-028 | `B-VAL-014-DEFINITION-RECONCILIATION-RECORD.md` | `6a76b3e` → `528de0d` | `281b29ca77dded2bbeb16ecc2fe916774ac57bb6` | REACHABLE_FROM_MAIN | DECISION_RECORD |
| AD-I-029 | `evidence/RI-PY-P01-EVIDENCE-GAP-RECORD.md` | `1ccd587` → `528de0d` | `feffc15d5587c3bebf446b6f0df419c0c5bbeaa7` | REACHABLE_FROM_MAIN | AUDIT |
| AD-I-030 | `evidence/RI-RS-P01-EVIDENCE-PACKAGE.md` (+ 4 sibling evidence files) | `528de0d` | `229d481600d55907a48b0e3e55ad06a91601b417` | REACHABLE_FROM_MAIN | EVIDENCE |
| AD-I-031 | `evidence/controlled-p01-handoff/` — 10 files (2 receipts, 2 logs, 2 timestamps, 2 manifests, comparison, …) | `528de0d` | `7bd81f08…`, `836cbf21…`, + 8 | REACHABLE_FROM_MAIN | EVIDENCE |
| AD-I-032 | `p01/FIX-DIGEST-P01.canonical.json` | `528de0d` | `b45ffa980a1a776b6143d7fcb255fbfa8a436582` | REACHABLE_FROM_MAIN | FIXTURE (contested — see notes) |
| AD-I-033 | `ri_rs_receiver.rs` | `967f179` / `49e848a` | `b2117f295902ae966e27ef99da8c574f057a7338` | REACHABLE_FROM_MAIN | REFERENCE_IMPLEMENTATION |
| AD-I-034 | `ri-rs/src/bin/p01_handoff.rs` (+ `Cargo.toml`, `Cargo.lock`) | `528de0d` | `1f963d7b3dc2…` | REACHABLE_FROM_MAIN | IMPLEMENTATION (adapter) |

| ID | Declared status (verbatim) | Content-observed | Authority claim | Authority evidence | Semantic | Evidence | Execution | Supersession | Dependencies | Conflicts | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AD-I-023 | `Status: CONSTRUCTED` · `Conformance execution: BLOCKED` · `B-VAL-014: NOT EXECUTED` · `Normative authority: NONE` | §18 gate block reads `BC-02.2 RI-PY  NOT STARTED` / `BC-02.3 RI-RS  NOT STARTED` | Explicitly disclaims authority | self-declared | ESTABLISHED (as construction) | OBSERVED | BLOCKED | **NOT ESTABLISHED** — AD-I-027 §5 claims to supersede it *as current custodian state* without editing it | AD-I-031 (parent BC-02 is AD-I-035, BRANCH_LOCAL) | AD-CFL-007, AD-DIV-003 | §18 is contradicted on `main` by AD-I-024 §7 |
| AD-I-024 | `CONSTRUCTED` | §7 gate block reads `BC-02.2 RI-PY Receiver  CONSTRUCTED` | disclaims | self-declared | ESTABLISHED (as construction) | OBSERVED | BLOCKED | NOT ESTABLISHED | AD-I-023 | AD-CFL-007 | Direct textual conflict with AD-I-023 §18, both on `main` |
| AD-I-025 | `Disposition: **BLOCKED — RI-PY source_commit provenance…**` | §9: five of six gate conditions met, condition 2 fails; §10 explicit non-execution | *"Non-normative engineering record. Creates no protocol authority"* | self-declared | ESTABLISHED (as observation) | OBSERVED | NOT EXECUTED | **NOT ESTABLISHED** — AD-I-027 §5 states it *"supersedes it as the current custodian state"* while leaving its face BLOCKED | AD-I-035 | AD-DIV-004 | Its own §7 records BC-02.1 §18 as *"stale… not modified"* |
| AD-I-026 | `COMPLETE` | Two receipts, two execution logs, cross-receiver comparison | disclaims conformance authority | self-declared | ESTABLISHED (as evidence generation) | ESTABLISHED | **EXECUTED** — handoff only, explicitly not conformance | NOT ESTABLISHED | AD-I-032, AD-I-033 | AD-DIV-004 | Sole EXECUTED item in the BC-02 chain |
| AD-I-027 | `Disposition: **CLOSED AT THE EVIDENCE-GENERATION LAYER**` | §13 gate block; §12 explicit non-execution; §15 *"does not authorize B-VAL-014"* | *"Authority created by this record: **NONE**"* — while performing *"governance reconciliation"* and declaring supersession of AD-I-025 | Issued under a named custodian authorization; **no signed or countersigned artifact observed** | ESTABLISHED (as scoped closure) | ESTABLISHED | NOT EXECUTED | Asserts supersession over AD-I-025 and AD-I-023 §18 | AD-I-025, AD-I-026 | AD-CFL-008, AD-DIV-005 | §15 note records the B-VAL-014 definition conflict as *"not been resolved"*; that conflict is separately recorded CLOSED by AD-I-028 |
| AD-I-028 | *"Definition reconciliation: **COMPLETE**"* · *"B-VAL-014: NOT EXECUTED"* | §1 state table records `BC-02  CLOSED` | *"Creates no execution authority"* | self-declared | ESTABLISHED (definition only) | OBSERVED | NOT EXECUTED | resolves the §14-vs-twelve-limb definition conflict; **does not** supersede any record | AD-I-035 §14 | AD-CFL-009 | Records `BC-02  CLOSED`; the BC-02 contract itself (AD-I-035) self-states `BLOCKED — CONSTRUCTION GAP` |
| AD-I-029 | `Disposition: **RI-PY EXECUTION BLOCKED**` | No RI-PY execution performed at that time | disclaims | self-declared | ESTABLISHED (historical) | OBSERVED | NOT EXECUTED | **NOT ESTABLISHED** — later superseded in fact by AD-I-026, unmarked | AD-I-026 | AD-DIV-004 | Head still reads BLOCKED on `main` |
| AD-I-030 | evidence package + manifest + logs | RI-RS-only earlier execution | none | — | ESTABLISHED | ESTABLISHED | EXECUTED (RI-RS only) | NOT ESTABLISHED | AD-I-032 | — | §11 records *"No P-01 issuance record exists in the repository to cross-check against"* |
| AD-I-031 | 24/24 `R-VAL-001…012 PASS` across both receipts | Receipts carry no result-authority field | none — authority isolation asserted and observed | comparison file records zero forbidden keys/values | ESTABLISHED | ESTABLISHED | EXECUTED | NOT ESTABLISHED | AD-I-032 | AD-CFL-010 | Both receipts carry `"status":"TRANSFERRED"` and `"fixture_artifact_identity":"FIX-DIGEST-P01.canonical.json"` |
| AD-I-032 | no status header — it is a data artifact | 15 octets, `{"a":1,"b":"x"}`, SHA-256 `ecf9e98e…d4e65667`, blob `b45ffa98…`; **no trailing newline**; fields `a`, `b`; **no `raw_input` member** | Referred to across the corpus as an *issued* fixture | **NOT ESTABLISHED** — no Registry entry, no issuance record, no issuer identity found on any of the 56 spec refs or 79 core refs | OPEN | OBSERVED (byte identity) / NONE (issuance) | consumed by AD-I-026 | NOT ESTABLISHED | AD-I-035 §4.1, §5.3 | AD-CFL-011 | Byte identity verified by this audit (§1.4); issuance **NOT VERIFIED and not verifiable from the corpus** |
| AD-I-033 | BC-02.3 implementation | receiver-side digest over received octets | none | — | ESTABLISHED | OBSERVED | not invoked by this audit | NOT ESTABLISHED | AD-I-023 | — | Blob identical at `49e848a`, HEAD and worktree per AD-I-027 §4; **not re-verified here** |
| AD-I-034 | adapter | AD-I-025 §4.2 records the Base64 transport conversion as adapter-side, not receiver-side | none | — | ESTABLISHED | OBSERVED | not invoked | NOT ESTABLISHED | AD-I-033 | AD-CFL-012 | AD-I-025 §4.2/A-OBS-02 records `R-VAL-002` as over-constrained relative to BC-02.1 §15 — DEFERRED, not fixed |

### 2.4 Group D — BC-02 chain, branch-local in `aura-specification`

**All 14 records below are absent from `origin/main`.** Each was verified absent
by `git cat-file -e origin/main:<path>` and present on the named branch.

| ID | Path (under `conformance/boundary/`) | Branch | Commit | Blob | Reachability | Class |
|---|---|---|---|---|---|---|
| AD-I-035 | `BC-02_IMMUTABLE_FIXTURE_HANDOFF.md` | `claude/bc-02-immutable-fixture-handoff-3s3fkp` | `e2066bd` (2026-08-23T18:37:48Z) | `9cfbc0fe66578dbb52cb6012f3ea03adcb48c40c` | **BRANCH_LOCAL** | ENGINEERING_CONTRACT |
| AD-I-036 | `BC-02_BOUNDARY_VALIDATION_RECORD.md` | `claude/bc-02-boundary-validation-q0h7yg` | `b90112b` (2026-08-23T19:10:58Z) | `e57ed4d230e90b4a1de5c22adee43c511b5dde8c` | **BRANCH_LOCAL** | AUDIT |
| AD-I-037 | `B-VAL-014-PREEXEC-CONTRACT-BINDING-RECORD.md` | `claude/ri-rs-p01-handoff-ga84l6` | `31c238b` (2026-08-23T23:33:07Z) | `52f1264d27a946ea2c64630c897156af07018890` | **BRANCH_LOCAL** | AUDIT |
| AD-I-038 | `BC-02.1-COMMON-RECEIPT-SCHEMA-v2.md` | `claude/bc-02-1-pre-01-schema-kvvm8z` | `f991dbd` (2026-08-24T15:13:21Z) | `963623a58da42ca69c9c9980a661fc59b6e8be42` | **BRANCH_LOCAL** | ENGINEERING_CONTRACT |
| AD-I-039 | `BC-02.1-PRE-01-SCHEMA-CORRECTION-RECORD.md` | `…kvvm8z` | `7b0325c` (2026-08-24T15:13:44Z) | `49807855eec1accb09c13a4c8a7ac28cb4bec047` | **BRANCH_LOCAL** | DECISION_RECORD |
| AD-I-040 | `BC-02.1-PRE-02-PRE-03-CLOSURE-RECORD.md` | `…kvvm8z` | `1301756` (2026-08-24T15:34:49Z) | `603383c1baf150b1ec7665955b26a5ffcf1904ec` | **BRANCH_LOCAL** | DECISION_RECORD |
| AD-I-041 | `BC-02.1-PRE-02-PRE-03-DEPENDENCY-CLOSURE-REPORT-v1.md` | `…kvvm8z` | `5f61e62` (2026-08-24T16:13:01Z) | `72f132b3efbfddd89438f612034f9d4220651f30` | **BRANCH_LOCAL** | AUDIT |
| AD-I-042 | `evidence/pre-01/PRE-01-VALIDATION-REPORT.txt` | `…kvvm8z` | `7b0325c` | `c1ecbb0c82e8a40fbc1dd5d154f1ee958296a740` | **BRANCH_LOCAL** | EVIDENCE |
| AD-I-043 | `schema/bc021_receipt_v2.py` | `…kvvm8z` | `f991dbd` | `0eb1ddfe4d8fc7d122d1b4e6cc051e3285cf5622` | **BRANCH_LOCAL** | IMPLEMENTATION |
| AD-I-044 | `schema/pre01_validation.py` | `…kvvm8z` | `f991dbd` | `98a5cb4ca57501a22da38285e930434c41a1e473` | **BRANCH_LOCAL** | CONFORMANCE (harness) |
| AD-I-045 | `BC-02.1-CUSTODIAN-DECISION-PACKAGE-A-B.md` | `…kvvm8z` | `66bfdb1` (2026-08-24T20:12:29Z) | `deaf6635787a970474ac8852e7f6f8e814f11f92` | **BRANCH_LOCAL** | DECISION_RECORD (package) |
| AD-I-046 | `BC-02-CUSTODIAN-DECISION-REVIEW-SURFACE-v1.md` | `…kvvm8z` | `a10ca5c` (2026-08-24T22:20:34Z) | `83681a728a6af9134fd4257ff1b41702f766700c` | **BRANCH_LOCAL** | AUDIT |
| AD-I-047 | `BC-02.1-S3-S4-S5-CONSISTENCY-DETERMINATION-RECORD-v1.md` | `claude/bc-02-1-consistency-analysis-8ewd0q` | `9bbe7ff` (2026-08-24T17:03:11Z) | `f290693c64bf17fda49720f6d111dbc4849e2d31` | **BRANCH_LOCAL** | AUDIT |
| AD-I-048 | `BC-02-CUSTODIAN-DECISION-PACKAGE-A-B-v1.md` | `…8ewd0q` | `dd11311` (2026-08-24T20:26:23Z) | `03d22a28274ddcab10184b56566e71cfcd3e5366` | **BRANCH_LOCAL** | DECISION_RECORD (package) |

| ID | Declared status (verbatim) | Content-observed | Authority claim | Authority evidence | Semantic | Evidence | Execution | Supersession | Dependencies | Conflicts | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AD-I-035 | *"BLOCKED — BC-02 CONSTRUCTION GAP"* (§19) | Sole source of `B-VAL-011…020`, `BNC-1…BNC-7`, `VE-01…VE-05`, `DEP-001…005`; classifies `CONFORMANCE_FIXTURE_REGISTRY_v1` as a **consumed authority** | *"Engineering Boundary Contract — NON-NORMATIVE / Authority created: NONE"* | none | OPEN | PARTIAL | BLOCKED | NOT ESTABLISHED | Registry (absent), BC-01 (absent), Boundary Spec v1 (absent), Core Interface Spec v1 (absent) | AD-CFL-013, AD-CFL-014 | **The most load-bearing artifact in the chain and the only source of the text Decision A and Decision B turn on. Not reachable from `main`.** |
| AD-I-036 | *"B-VAL-014 NOT EXECUTED / BLOCKED"*; `DEP-001…005` all OPEN | §8: *"No evidence of either closure or issuance is reachable in any repository in scope."* | disclaims | none | OPEN | PARTIAL | BLOCKED | NOT ESTABLISHED | AD-I-035 | AD-DIV-006 | Cited by name in AD-I-027 §15; **that citation resolves to no artifact on `main`** |
| AD-I-037 | *"PRE-01: OPEN — BINDING GAP (Outcome B)"*; gaps `PRE-01-G1…G7` | Records the binding gap between BC-02 §14 and the emitted receipts | disclaims | none | OPEN | PARTIAL | NOT EXECUTED | NOT ESTABLISHED | AD-I-028, AD-I-035 | **AD-CFL-015** | Directly contradicted on its face by AD-I-039 |
| AD-I-038 | `CONSTRUCTED` | Represents both B-VAL-014 operands separately; `DigestSource` domain includes `RECEIVER_RECOMPUTED` and `EXTERNALLY_SUPPLIED`; restricts `UnresolvedValue` to `issuance_id` | *"Normative authority: NONE"* | none | ESTABLISHED (as construction) | OBSERVED | NOT EXECUTED | **NOT ESTABLISHED** — AD-I-048 records v1 as *"superseded for new receipts by v2"*; no supersession act observed | AD-I-023 | AD-CFL-016 | **No receiver implements v2.** Both deployed receivers emit `SCHEMA_VERSION = 1` |
| AD-I-039 | **`PRE-01 — PASS`** | Scope limited in §I.1 to *"the schema layer only"* | disclaims | none | NOT DETERMINED | PARTIAL | NOT EXECUTED | NOT ESTABLISHED | AD-I-037, AD-I-038 | **AD-CFL-015**, AD-DIV-007 | Unqualified `PASS` in gate blocks; qualified *"schema layer only"* in body |
| AD-I-040 | `PRE-02 BLOCKED` · `PRE-03 BLOCKED` | Both blocked on authority, not construction | disclaims | none | BLOCKED | PARTIAL | BLOCKED | NOT ESTABLISHED | AD-I-035, AD-I-039 | — | — |
| AD-I-041 | *"Answer NO"*; four authority-level blockers | Dependency closure incomplete | disclaims | none | OPEN | PARTIAL | BLOCKED | NOT ESTABLISHED | AD-I-035, AD-I-040 | — | — |
| AD-I-042 | `PRE-01-001…010` report | AD-I-045 §7 records `PRE-01-010` failing because a later package file lies outside PRE-01's authorized path set | none | — | NOT DETERMINED | CONFLICTING | EXECUTED (harness) | NOT ESTABLISHED | AD-I-044 | AD-DIV-008 | Same harness reported PASS in AD-I-039 and FAIL in AD-I-041 §R |
| AD-I-043 | v2 schema implementation | not bound to any receiver | none | — | PROPOSED | OBSERVED | not invoked | NOT ESTABLISHED | AD-I-038 | AD-CFL-016 | — |
| AD-I-044 | validation harness | deliberately not edited to accommodate later packages | none | — | ESTABLISHED | OBSERVED | EXECUTED (historically) | NOT ESTABLISHED | AD-I-038 | AD-DIV-008 | — |
| AD-I-045 | *"TERRAIN SURVEY CLOSED — DIAGNOSTIC. DECISION A AND DECISION B OPEN, ROUTED TO CUSTODIAN."* | **A = Fixture authority** (A-1…A-8, options A-I/A-II/A-III); **B = Operand semantics / BNC-1 detectability** (B-1…B-5, options B-I/B-II/B-III); own record inventory `R1…R15`; divergences `D-1…D-10` | *"Non-normative. Creates no authority… resolves no decision"* | none | OPEN (both decisions) | OBSERVED | NOT EXECUTED | NOT ESTABLISHED | AD-I-035…044 | **AD-CFL-017**, AD-DIV-009, AD-DIV-010 | §2 asserts *"Decision A, Decision B, Decision Package and Terrain Survey occur in **no reachable commit** of any in-scope repository"* — see AD-DIV-009 |
| AD-I-046 | *"Governance-only review surface. Read-only."* | §1.1: *"**No file of that name exists in any reachable commit of any in-scope repository.** Exactly one decision package exists"* — referring to `BC-02-CUSTODIAN-DECISION-PACKAGE-A-B-v1.md` | disclaims | none | OPEN | OBSERVED | NOT EXECUTED | NOT ESTABLISHED | AD-I-045 | **AD-CFL-017**, AD-DIV-010 | AD-I-048 **is** a file of that name, committed 2026-08-24T20:26:23Z — 1h54m before this review's commit |
| AD-I-047 | *"Status: DRAFT / CONTROLLED ANALYSIS"* · **`DETERMINATION: INCOHERENT — CUSTODIAN DECISION REQUIRED`** | Nine conflicts/gaps across axes S-3 / S-4 / S-5 | *"Authority: NONE"* | none | OPEN | OBSERVED | NOT EXECUTED | NOT ESTABLISHED | AD-I-035 | AD-CFL-013 | **Earliest artifact to record a "Terrain survey CLOSED" state** (2026-08-24T17:03:11Z) |
| AD-I-048 | *"Status: DRAFT / CONTROLLED PREPARATION"* · *"TERRAIN SURVEY CLOSED — DIAGNOSTICALLY COMPLETE"* | **A = Boundary transfer semantics** (A-1…A-5, interpretation of existing text); **B = Upstream authority supply** (B-1…B-3, authority artifacts/acts); own record inventory `N-01…N-17`; divergences `DIV-01…DIV-07`; consequence matrix A×B | *"Authority: NONE · Conformance authority: NONE · Execution authority: NONE"* | none | OPEN (both decisions) | OBSERVED | NOT EXECUTED | NOT ESTABLISHED | AD-I-035…041, AD-I-047 | **AD-CFL-017** | Cites `N-11…N-14` (AD-I-038…041), which are **not reachable from this package's own branch** |

### 2.5 Group E — aura-poc-a-core-v3.3

| ID | Path | Commit | Blob | Reachability | Class |
|---|---|---|---|---|---|
| AD-I-049 | `CLAUDE.md` | `577142b` | `45eaff84763d` | REACHABLE_FROM_MAIN | GOVERNANCE |
| AD-I-050 | `AGENTS.md` | `577142b` | `b4261d0bd476` | REACHABLE_FROM_MAIN | GOVERNANCE |
| AD-I-051 | `CONSTITUTIONAL_DECREE.md` | `564f9d7` | `998e859c4bb5` | REACHABLE_FROM_MAIN | GOVERNANCE |
| AD-I-052 | `ROLE_OF_THE_PROTOCOL_CUSTODIAN.md` | `564f9d7` | `80cb95628fbe` | REACHABLE_FROM_MAIN | GOVERNANCE |
| AD-I-053 | `review/2026-08-12_OQ-A_GOVERNANCE_JURISDICTION/` (14 files) | `1da3e7f` | `92ba5073…`, `cc18175a…`, … | REACHABLE_FROM_MAIN | AUDIT |
| AD-I-054 | `review/2026-08-12_RD1_ARI_DECISION_READINESS/` (11 files) | `5888a1c` | `e2f7bd91…`, … | REACHABLE_FROM_MAIN | AUDIT |
| AD-I-055 | `review/2026-08-14_P0_6_D3_D4_DECISION_RECORD/D3_D4_DECISION_RECORD.md` | `39ecd2f` | `a695e1e09f51` | REACHABLE_FROM_MAIN | DECISION_RECORD |
| AD-I-056 | `core/evaluator.py` | `edfb10a` | `7937d089d296` | REACHABLE_FROM_MAIN | IMPLEMENTATION |
| AD-I-057 | `conformance/boundary/BC-02.2-RI-PY-RECEIVER-v1.md` + 4 evidence files + 3 code files | `d943807` / `b86a382` | `438d8f290707`, `708cc01b1f74…` | REACHABLE_FROM_MAIN | ENGINEERING_CONTRACT + EVIDENCE + IMPLEMENTATION |
| AD-I-058 | `RELEASE_CLOSURE_REPORT.md` | `93f51c8` | `8be51e729b0c` | REACHABLE_FROM_MAIN | HISTORICAL |

| ID | Declared status (verbatim) | Content-observed | Authority claim | Authority evidence | Semantic | Evidence | Execution | Supersession | Dependencies | Conflicts | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AD-I-049 | no status header | Declares a 10-level *Authority Precedence* ladder; tier 2 = Aura Protocol Specification | Explicit ordering of authority tiers | **The ladder's own authority to order tiers 1–5 is established by nothing observed** | ESTABLISHED (as instruction) | OBSERVED | N/A | NOT ESTABLISHED | AD-I-050 | **AD-CFL-004** | Corresponds to `OQ-A-CONFLICT-003`: *a tier-6 document establishes the ordering of tiers 1–5* |
| AD-I-050 | no status header | Canonical repository-level agent rules; rule 1: *"Protocol specification has authority over implementation"* | Explicit | self-declared | ESTABLISHED (as instruction) | OBSERVED | N/A | NOT ESTABLISHED | — | AD-CFL-004 | — |
| AD-I-051 | `STATUS: MANDATORY / NON-OVERRIDABLE`, `AUTHORITY: Custodian of the Protocol`, `EFFECTIVE: Immediate and Perpetual` | Art. I lists **both** `Fixed-point arithmetic (Q16.16)` **and** `Scaling factor: 100,000 (10^5)` as immutable constitutional constants, with no stated relationship | Strongest authority claim in the implementation corpus | Custodian named; **no ratification artifact observed** | ASSERTED | PARTIAL | N/A | NOT ESTABLISHED | — | **AD-CFL-005**, AD-CFL-006 | Internal contradiction Q16.16 vs decimal 10^5 recorded by AD-I-054 as `C-14`, *"Contradiction recorded, not resolved"*; **no implementation uses Q16.16** |
| AD-I-052 | `CANONICAL` (implementation corpus) | Grants Custodian FINAL AUTHORITY over `core/`, constants, layer boundaries, primitives; SOLE AUTHORITY over sealing | Explicit | self-declared | ASSERTED | OBSERVED | N/A | NOT ESTABLISHED | AD-I-051 | AD-CFL-006 | Does **not** name ARI |
| AD-I-053 | `Normative effect: NONE` | 13 conflicts `OQ-A-CONFLICT-001…013`, **0 resolved**; defines **C-1** and **C-2**; OQ-A-005 finding = `CONDITIONALLY DETERMINABLE` | disclaims | — | OPEN | ESTABLISHED | N/A | NOT ESTABLISHED | AD-I-049…052 | **AD-CFL-004, AD-CFL-006** | Records *"no source grants any role authority over ARI semantics by name"* across 10 authority grants |
| AD-I-054 | `Normative effect: NONE` | 27 ARI decisions `ARI-D-001…027`, **0 answered**; candidate register `C-1…C-n` (non-normative candidates) | disclaims | — | OPEN | ESTABLISHED | N/A | NOT ESTABLISHED | AD-I-053 | AD-CFL-006 | `ARI-D-001` — whether ARI is normatively defined at all — is **open**, and gates the other 26 |
| AD-I-055 | D-3 concrete semantic value **NOT ESTABLISHED** | Canonical byte encoding, serialization format, hash-domain representation explicitly not established | — | — | OPEN | PARTIAL | NOT EXECUTED | NOT ESTABLISHED | — | **AD-CFL-018** | Direct cross-corpus conflict with `evidence/DQ-006_CLOSURE_PACKAGE.md` (`CLOSED — PASS`) |
| AD-I-056 | code | `RAW_ARI = 0.3*SI + 0.7*SA`; `SCALING_FACTOR = 100000`; weights `30000` / `70000`; integer arithmetic | none | — | **IMPLEMENTED / OBSERVED** | OBSERVED | EXECUTED (as code, not as a conformance procedure) | N/A | AD-I-051 | AD-CFL-005 | **Recorded as implementation behaviour only. This audit records no normative, required or canonical status for any of these values.** |
| AD-I-057 | `Status: CONSTRUCTED` · `P-01: NOT EXECUTED` · `B-VAL-014: NOT EXECUTED` · `Normative authority: NONE` | Construction evidence §0 carries the `source_commit` provenance correction `64bf959` → `d943807` with the superseded value retained | disclaims | self-declared | ESTABLISHED (as construction) | ESTABLISHED | BLOCKED | §0 is an **explicit, in-place correction record** — the one clean supersession-of-a-value observed in the corpus | AD-I-023 | — | Header still reads `P-01: NOT EXECUTED` although AD-I-026 records an executed RI-PY P-01 handoff — AD-DIV-011 |
| AD-I-058 | `Classification: REGULATORY RELEASE ASSESSMENT`, `Authority: Protocol Custodian`, dated 2026-07-24 | *"All tests pass. All CI checks pass… constitutionally compliant."* | Explicit | Custodian named; no countersignature observed | HISTORICAL | OBSERVED | EXECUTED (2026-07-24) | NOT ESTABLISHED | — | AD-DIV-012 | **HISTORICAL FACT ≠ CURRENT AUTHORITY.** Predates the entire CK-003, OQ-A, RD-1 and BC-02 record set, all of which record open conflicts |

### 2.6 Group F — aura-guard-v1.3 and organization repositories

| ID | Repository | Path | Commit | Blob | Reachability | Class |
|---|---|---|---|---|---|---|
| AD-I-059 | aura-guard-v1.3 | `D3_REAL_CHAIN_EXECUTION_BLOCKER.md` | `6661982` | `6c54b06a09b2` | REACHABLE_FROM_MAIN | AUDIT |
| AD-I-060 | aura-guard-v1.3 | `D3_REAL_CHAIN_RUST_OUTPUT.json`, `D3_REAL_CHAIN_CANONICAL.bin` | `70b9881` | `3dc846bb6f7d`, `d71a3c9a7c00` | REACHABLE_FROM_MAIN | EVIDENCE |
| AD-I-061 | aura-guard-v1.3 | `D3_REAL_CHAIN_PROVENANCE.md` | `5b6d1ae` | `591573cc5f79` | REACHABLE_FROM_MAIN | EVIDENCE |
| AD-I-062 | aura-guard-v1.3 | `ck003/dq-002-hash-domain/07_DQ-002_verdict.md` | `1e45560` | `77624e53fac5` | REACHABLE_FROM_MAIN | DECISION_RECORD |
| AD-I-063 | aura-specification | `ck003/handover-assessment/04_CONFLICT_REGISTER.md` | `b4745e6` | `6bcdab38578a` | REACHABLE_FROM_MAIN | AUDIT |
| AD-I-064 | aura-specification | `reference/RI-RS_AURA_GUARD.md`, `reference/RI-PY_AURA_POC_A_CORE.md` | `b68181e` | `997b68d20af1`, `51732444b648` | REACHABLE_FROM_MAIN | REFERENCE_IMPLEMENTATION (descriptor) |
| AD-I-065 | .github | `GUIDELINES.md` | `95f017a` | `4a737a461874` | REACHABLE_FROM_MAIN | GOVERNANCE |
| AD-I-066 | cargo | vendored upstream `rust-lang/cargo` mirror | `92e3ebe` | — | REACHABLE_FROM_MASTER | OTHER |

| ID | Declared status (verbatim) | Content-observed | Authority claim | Authority evidence | Semantic | Evidence | Execution | Supersession | Dependencies | Conflicts | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AD-I-059 | *"STOPPED before Phase 3"*; STOP-6, STOP-3, STOP-2, STOP-8, partial STOP-7 | States `D3_REAL_CHAIN_RUST_OUTPUT.json` and `D3_REAL_CHAIN_CANONICAL.bin` are *"deliberately absent"* | none | — | HISTORICAL | OBSERVED | NOT EXECUTED | **NOT ESTABLISHED** | AD-I-060 | **AD-DIV-013** | Both named files **are present on `main`**, added later on a different branch. No supersession marker on this record |
| AD-I-060 | data artifacts | present on `main` | none | — | ESTABLISHED (existence) | OBSERVED | EXECUTED (CI run recorded in AD-I-061) | NOT ESTABLISHED | AD-I-061 | AD-DIV-013 | — |
| AD-I-061 | provenance record | Records CI `workflow_run_id`, artifact id, zip digest, and that `GITHUB_SHA` is an ephemeral merge commit | none | — | ESTABLISHED | ESTABLISHED | EXECUTED | NOT ESTABLISHED | — | — | Among the most complete provenance records observed in the corpus |
| AD-I-062 | **`Status: CONDITIONALLY CLOSED / CI-BLOCKED`** | §1: *"Aura adopts **RI-RS** as the canonical hash-domain model for CK-003"* | **An adoption claim of protocol-level scope, made from the implementation corpus** | none observed | NOT DETERMINED | PARTIAL | BLOCKED | NOT ESTABLISHED | — | **AD-CFL-019** | Directly material to C-2; recorded, not adjudicated |
| AD-I-063 | `Classification: EVIDENCE — NON-NORMATIVE`; *"Reconciled: 0 of 5"* | `CFL-001…005`, all routed to Custodian, none reconciled | disclaims | — | OPEN | ESTABLISHED | N/A | NOT ESTABLISHED | AD-I-055 | AD-CFL-018 | CFL-001 is the cross-corpus authority conflict; identical in kind to C-2 |
| AD-I-064 | `APS-950 Certification Status: NOT CERTIFIED` | Descriptor points at `github.com/AuraIDToken/aura-guard-v1.3`; the organization observed in scope is `Aura-IDToken` | none | — | ESTABLISHED | OBSERVED | N/A | NOT ESTABLISHED | AD-I-017 | AD-DIV-014 | Organization-name divergence recorded; not corrected |
| AD-I-065 | no status header; Polish | Names repositories `aura-protocol`, `aura-devos`, `aura-brand` — **none of which are in scope, and none observed** | Org-level governance | — | NOT DETERMINED | CONFLICTING | N/A | NOT ESTABLISHED | — | AD-DIV-015 | Describes a repository topology that does not match the observed one |
| AD-I-066 | upstream mirror | No Aura governance, specification or ARI content observed on the checked-out branch | none | — | N/A | N/A | N/A | N/A | — | — | Recorded for completeness; **branch coverage NOT ESTABLISHED** (§1.2) |

### 2.7 Artifacts referenced by the corpus but not located

Each of the following is cited by a load-bearing record as an input or an
authority, and was **not found** on any of the 56 `aura-specification` refs or
79 `aura-poc-a-core-v3.3` refs searched.

| Referenced artifact | Cited by | Reachability | Recorded as |
|---|---|---|---|
| `CONFORMANCE_FIXTURE_REGISTRY_v1` | AD-I-035 §4.1, §4.2 (as a **consumed authority**) | **UNREACHABLE** | the token appears in exactly 7 files, all of which either reference it or record its absence; **no Registry artifact exists** |
| P-01 issuance record / `issuance_id` value | AD-I-035 §5.3, §5.5, §15.2; AD-I-032 | **UNREACHABLE** | `issuance_id` appears in 13 files, in every case as a field name or an unresolved value; **no issuance record exists** |
| `BC-01` | AD-I-035 (`DEP-004`, `VE-04`) | **UNREACHABLE** | recorded `ACCEPTED` in task headers per AD-I-048 `DIV-04`; acceptance has no reachable subject |
| Boundary Specification v1 | AD-I-035 `DEP-004` | **UNREACHABLE** | — |
| Core Interface Spec v1 | AD-I-035 `DEP-004` | **UNREACHABLE** | — |
| `BoundaryHandoffRecord` instances | AD-I-035 §7.1, §14 | **UNREACHABLE** | no implementation emits this form |
| A "Terrain Survey" artifact | AD-I-045 §8, AD-I-047, AD-I-048 §3 — all three declare it **closed** | **UNREACHABLE** | **no Terrain Survey document exists in any commit of either fully-searched repository.** The token occurs only inside the four records that declare its closure |
| A "System Restore / governance-control" document | the mandate for this audit | **UNREACHABLE** | no artifact of this class located; recorded as absent, not as non-existent |
| `BC-02_BOUNDARY_VALIDATION_RECORD.md` §5.1 (as cited from `main`) | AD-I-027 §15 | **BRANCH_LOCAL** (AD-I-036) | the citation resolves, but only off `main` |

**Absence bound.** Every "UNREACHABLE" above is bounded by §1.2. It means *not
present on the refs searched*. It is **not** a finding that the artifact does
not exist, was never created, or cannot be supplied.

---

## 3. CLASSIFICATION SUMMARY

| Class | Count (inventory records) |
|---|---|
| GOVERNANCE | 9 |
| SPECIFICATION | 13 (incl. 2 duplicate-representation groups) |
| ENGINEERING_CONTRACT | 5 |
| DECISION_RECORD | 8 |
| AUTHORITY_RECORD (claimed) | 2 |
| AUDIT | 9 |
| EVIDENCE | 7 |
| CONFORMANCE | 3 |
| FIXTURE | 2 |
| IMPLEMENTATION / REFERENCE_IMPLEMENTATION | 7 |
| HISTORICAL | 1 |
| OTHER | 1 |
| **RESTORE / CONTROL** | **0 located** |

### 3.1 Records whose classification is itself ambiguous

| ID | CLASSIFICATION: AMBIGUOUS — why |
|---|---|
| AD-I-027 | Declares *"Authority created by this record: NONE"* while performing a governance act (declaring one record superseded by another as *"current custodian state"*) and issuing a *"Custodian decision"* (§14). It is either an AUTHORITY_RECORD that disclaims authority, or an AUDIT that performs one. **Not resolved here.** |
| AD-I-032 | Consumed throughout the corpus as an issued FIXTURE, but no issuance or Registry artifact exists. It is a verified data artifact whose fixture status is exactly what Decision A turns on. Recorded as `FIXTURE (contested)`. |
| AD-I-045, AD-I-048 | Each is simultaneously an AUDIT (normalization pass over prior records), a DECISION_RECORD (packages two named decisions), and a routing instrument. Both disclaim authority. |
| AD-I-051 | Declares itself `MANDATORY / NON-OVERRIDABLE` with `AUTHORITY: Custodian of the Protocol` — a constitutional claim from the implementation corpus over a protocol-level subject. Whether it is GOVERNANCE at protocol tier or at instrument tier **is C-2**, and is not answered here. |
| AD-I-062 | An implementation-corpus DECISION_RECORD stating a protocol-level adoption (*"Aura adopts RI-RS as the canonical hash-domain model"*). Class depends on C-2. |

---

## 4. STATUS NORMALIZATION

### 4.1 Source tokens observed, verbatim

The corpus uses at least the following status tokens. **Each is preserved as
written in §2. None is replaced.**

`FROZEN` · `FROZEN (po zatwierdzeniu)` · `DRAFT` · `1.0-DRAFT` · `0.2-DRAFT` ·
`TODO` · `PROPOSED` · `ACCEPTED` · `CONSTRUCTED` · `NOT STARTED` · `COMPLETE` ·
`CLOSED` · `CLOSED AT THE EVIDENCE-GENERATION LAYER` · `CONDITIONALLY CLOSED /
CI-BLOCKED` · `BLOCKED` · `BLOCKED — CONSTRUCTION GAP` · `PASS` · `FAIL` ·
`SATISFIED` · `MET` · `UNMET` · `OPEN` · `UNKNOWN` · `NOT ESTABLISHED` ·
`NOT DETERMINED` · `NOT EXECUTED` · `NO RESULT` · `NOT CERTIFIED` ·
`PENDING_EXECUTION` · `OUTCOME B` · `INCOHERENT` · `STOPPED` ·
`MANDATORY / NON-OVERRIDABLE` · `CANONICAL` · `VALIDATED` · `TRANSFERRED`

**35 distinct status tokens** across the audited set.

### 4.2 The four dimensions, kept separate

This audit records four independent dimensions per artifact (§2). They are not
collapsed, and a value in one does not imply a value in another. The two
distinctions that carry the most weight in this corpus:

```text
DECLARED STATUS        is what a document says about itself.
CONTENT-OBSERVED       is what reading the document and its referents shows.

A declared status is never converted into a semantic status here.
```

```text
EXECUTION STATUS  ≠  SEMANTIC STATUS
NOT EXECUTED      is not FAIL.
BLOCKED           is not FAIL.
PASS (engineering validation)  is not  PASS (conformance).
```

### 4.3 Worked normalizations where declaration and support diverge

Given only where the source itself supplies the distinction:

| Artifact | DECLARED STATUS (verbatim) | NORMALIZED SEMANTIC STATUS | Why the source supports the distinction |
|---|---|---|---|
| AD-I-031 | `R-VAL-001…012 — 24/24 PASS` | **NOT DETERMINED** (as to conformance) | AD-I-027 §8 states in the source itself: *"These are receipt/schema validation assertions. They are **not** conformance assertions and MUST NOT be converted into a protocol result."* |
| AD-I-039 | `PRE-01 — PASS` | **NOT DETERMINED** (as to binding) | The same record's §I.1 limits it to *"the schema layer only"*; no receiver implements v2 |
| AD-I-027 | `CLOSED AT THE EVIDENCE-GENERATION LAYER` | **ESTABLISHED** for evidence generation; **NOT DETERMINED** for conformance | The record's own §13 semantic boundary: *"REAL EVIDENCE ≠ CONFORMANCE RESULT"* |
| AD-I-028 | `BC-02  CLOSED` (state table) | **NOT DETERMINED** | The BC-02 contract itself (AD-I-035 §19) self-states `BLOCKED — BC-02 CONSTRUCTION GAP`; the source does not reconcile the two |
| AD-I-026 | `COMPLETE` | **ESTABLISHED** for the handoff event; **NOT DETERMINED** for anything downstream | The record confines itself to the handoff and disclaims conformance |
| AD-I-021 | `Status: DRAFT` + body *"normative conformance requirement"* | **NOT DETERMINED** | The source carries both statements and reconciles neither |
| AD-I-002 | `FROZEN (po zatwierdzeniu)` | **NOT DETERMINED** | The parenthetical makes the freeze conditional; the English copy (AD-I-001) makes it unconditional; no source reconciles them |

For every other artifact in §2 where declaration and support do not diverge, the
declared token stands and the normalized reading is recorded in the same row.

---

## 5. DECLARATION VS CORPUS CONTENT — DIVERGENCE REGISTER

Every entry below carries `RESOLUTION: NONE`. **No source is chosen as correct.**

---

**AD-DIV-001 — APS-001 status**
- SOURCE A: `releases/v0.1.0/DOCUMENT_STATUS.md` (AD-I-006), row *Protocol Specification*
- SOURCE B: `specification/APS-001_PROTOCOL_SPECIFICATION.md` (AD-I-010), header
- EXACT LOCATION: A — status table row `APS-001`; B — lines 2–4
- DECLARED STATE: A — `Version 0.1-DRAFT`, `Status: TODO`
- OBSERVED STATE: B — `Version: 0.2-DRAFT`, `Status: DRAFT — ARCHITECTURE REVIEW REQUIRED`
- TYPE: status-snapshot vs current document; no supersession marker on A
- **RESOLUTION: NONE**

**AD-DIV-002 — CONF-003 normativity**
- SOURCE A: `conformance/CONF-003_CANONICAL_SERIALIZATION.md` header
- SOURCE B: same file, body, first paragraph
- DECLARED STATE: A — `Status: DRAFT`; B — *"This document is a normative conformance requirement."*
- OBSERVED STATE: a DRAFT document asserting in-force normative effect over implementations
- TYPE: header-vs-body; same artifact
- **RESOLUTION: NONE**

**AD-DIV-003 — BC-02.2 / BC-02.3 gate state on `main`**
- SOURCE A: `BC-02.1-COMMON-RECEIPT-SCHEMA-v1.md` §18 (AD-I-023)
- SOURCE B: `BC-02.3-RI-RS-RECEIVER-v1.md` §7 (AD-I-024)
- DECLARED STATE: A — `BC-02.2 RI-PY  NOT STARTED`, `BC-02.3 RI-RS  NOT STARTED`; B — both `CONSTRUCTED`
- OBSERVED STATE: **both records are on `main` simultaneously and are not reconciled there.** AD-I-025 §7 and AD-I-027 §11 (`D-OBS-01`) each record A as stale and each state it was deliberately not modified
- TYPE: contradictory gate snapshots inside one reachable corpus
- **RESOLUTION: NONE**

**AD-DIV-004 — BLOCKED headers standing after the blocked event occurred**
- SOURCE A: AD-I-029 (`RI-PY EXECUTION BLOCKED`, 2026-08-23 20:18) and AD-I-025 (`BLOCKED — RI-PY source_commit provenance…`, 21:19)
- SOURCE B: AD-I-026 (`COMPLETE`, 21:40) with both receipts
- DECLARED STATE: A — BLOCKED, unqualified, on the document face
- OBSERVED STATE: the blocking conditions were subsequently closed; **neither A carries a supersession marker**
- TYPE: superseded-in-fact disposition presented as current
- **RESOLUTION: NONE** — AD-I-027 §5 asserts supersession over AD-I-025; see AD-CFL-008
- Already recorded in the corpus as `D-6` (AD-I-045) — reproduced here because it remains open

**AD-DIV-005 — "Authority created: NONE" alongside a governance act**
- SOURCE A: AD-I-027 §2: *"Authority created by this record: **NONE**. It is non-normative."*
- SOURCE B: same record, §5 (*"The present record supersedes it as the current custodian state"*), §13 (gate state), §14 (*"Custodian decision"*)
- TYPE: self-declared non-authority vs performed governance effect
- **RESOLUTION: NONE**

**AD-DIV-006 — cross-branch citation from `main`**
- SOURCE A: AD-I-027 §15, on `main`, citing *"`BC-02_BOUNDARY_VALIDATION_RECORD.md` §5.1"*
- SOURCE B: that file exists only at `b90112b` on `claude/bc-02-boundary-validation-q0h7yg`
- OBSERVED STATE: a `main`-only reader cannot resolve the citation
- TYPE: broken reference from a reachable record to a branch-local one
- **RESOLUTION: NONE**

**AD-DIV-007 — PRE-01 disposition**
- SOURCE A: AD-I-037 §1: *"PRE-01: OPEN — BINDING GAP (Outcome B)"*
- SOURCE B: AD-I-039 §I: *"PRE-01 — PASS"*
- OBSERVED STATE: on their faces the two contradict; B's own §I.1 scopes the PASS to *"the schema layer only"*; A is branch-local and B is branch-local on a **different** branch
- TYPE: contradictory status tokens for one identifier across two unreachable-from-`main` records
- **RESOLUTION: NONE** — corpus records this as `D-1` (AD-I-045) and `DIV-05` (AD-I-048), neither resolving it

**AD-DIV-008 — one harness, two verdicts**
- SOURCE A: AD-I-039 / AD-I-042 — `PRE-01-001…010` reported passing
- SOURCE B: AD-I-041 §R and AD-I-045 §7 — the same harness reports `PRE-01-010` **FAIL**
- OBSERVED STATE: the failure is attributed by both sources to a later work package adding a file outside PRE-01's authorized path set, not to a regression
- TYPE: execution result whose meaning changes with the file set, presented as a validation verdict
- **RESOLUTION: NONE**

**AD-DIV-009 — "occurs in no reachable commit"**
- SOURCE A: AD-I-045 §2 (commit `66bfdb1`, 2026-08-24T20:12:29Z): *"The terms Decision A, Decision B, Decision Package and Terrain Survey occur in **no reachable commit of any in-scope repository**"*
- SOURCE B: AD-I-047 (commit `9bbe7ff`, 2026-08-24T17:03:11Z, branch `claude/bc-02-1-consistency-analysis-8ewd0q`) contains the term *Terrain survey* in its own status table
- OBSERVED STATE: B precedes A by 3h09m. The two commits are on **disjoint branches**; B is not reachable from A's branch, and A's sentence does not state which ref set it measured
- TYPE: corpus-wide absence claim measured against an unstated ref set
- **RESOLUTION: NONE**

**AD-DIV-010 — "exactly one decision package exists"**
- SOURCE A: AD-I-046 §1.1 (commit `a10ca5c`, 2026-08-24T22:20:34Z): *"**No file of that name exists in any reachable commit of any in-scope repository.** Exactly one decision package exists"*, naming `BC-02-CUSTODIAN-DECISION-PACKAGE-A-B-v1.md` as ABSENT
- SOURCE B: AD-I-048 — a file at exactly that path, commit `dd11311`, 2026-08-24T20:26:23Z, 1h54m earlier
- OBSERVED STATE: A concludes the requested filename was a naming discrepancy and reviews AD-I-045 instead; **the requested file existed**
- TYPE: absence claim contradicted by an artifact on another branch
- **RESOLUTION: NONE**

**AD-DIV-011 — BC-02.2 header after execution**
- SOURCE A: AD-I-057 header on `main`: `**P-01:** NOT EXECUTED`
- SOURCE B: AD-I-026 and AD-I-031 record an executed RI-PY P-01 handoff at 2026-08-23T21:36:53Z with a receipt
- TYPE: contract header not updated after the event it describes; **no supersession marker**
- **RESOLUTION: NONE**

**AD-DIV-012 — release closure vs subsequent conflict record**
- SOURCE A: AD-I-058 (2026-07-24): *"internally consistent, technically reproducible, and constitutionally compliant… All tests pass."*
- SOURCE B: AD-I-053 (13 unresolved conflicts), AD-I-054 (27 unanswered ARI decisions), AD-I-063 (`Reconciled: 0 of 5`), all dated 2026-08
- TYPE: historical assessment vs later-recorded open state; A carries no supersession marker
- **RESOLUTION: NONE** — recorded per §17: HISTORICAL FACT is not CURRENT AUTHORITY

**AD-DIV-013 — "deliberately absent" artifacts that are present**
- SOURCE A: AD-I-059 lines 15–17: *"`D3_REAL_CHAIN_RUST_OUTPUT.json`, `D3_REAL_CHAIN_CANONICAL.bin`, `D3_REAL_CHAIN_RUST_PROVENANCE.md` and `D3_REAL_CHAIN_EXECUTION_REPORT.md` are deliberately absent."*
- SOURCE B: `git ls-tree origin/main` in `aura-guard-v1.3` lists `D3_REAL_CHAIN_RUST_OUTPUT.json` (blob `3dc846bb6f7d`) and `D3_REAL_CHAIN_CANONICAL.bin` (blob `d71a3c9a7c00`), both added at `70b9881`
- OBSERVED STATE: two of the four named files are present on the same branch that carries the record declaring them absent; the other two (`…RUST_PROVENANCE.md`, `…EXECUTION_REPORT.md`) are indeed not present — a differently-named `D3_REAL_CHAIN_PROVENANCE.md` is
- TYPE: stop-report statement of absence outlived by later work; no supersession marker
- **RESOLUTION: NONE**

**AD-DIV-014 — organization name in reference descriptors**
- SOURCE A: `reference/RI-RS_AURA_GUARD.md`: `https://github.com/AuraIDToken/aura-guard-v1.3`
- SOURCE B: repositories in scope are under `Aura-IDToken`
- TYPE: identifier divergence in a reachable descriptor
- **RESOLUTION: NONE**

**AD-DIV-015 — org guidelines describe a different repository set**
- SOURCE A: `.github/GUIDELINES.md` §1 names `aura-protocol`, `aura-devos`, `aura-brand`
- SOURCE B: the repositories observed are `aura-specification`, `aura-poc-a-core-v3.3`, `aura-guard-v1.3`, `.github`, `cargo`
- TYPE: organization-level governance document describing an unobserved topology
- **RESOLUTION: NONE**

**AD-DIV-016 — `DEP-001…005` declared satisfied**
- SOURCE A: task headers and gate blocks quoted by AD-I-045 (`D-7`) and AD-I-048 (`DIV-02`) as stating `DEP-001…005 SATISFIED FOR P-01`
- SOURCE B: AD-I-035 §19, AD-I-036 §8, AD-I-028 §16.3, AD-I-037 §15.1 and AD-I-040 §C.5 all record them **OPEN**; no closure artifact is reachable
- OBSERVED STATE: **the declaring headers are not themselves repository-resident artifacts** in the searched refs; the corpus side is five records, all OPEN
- TYPE: instruction-level declaration vs corpus content
- **RESOLUTION: NONE** — held UNKNOWN, not converted

**Total declaration-vs-content divergences recorded: 16.**

---

## 6. CONFLICT REGISTER

`Resolution` is `UNRESOLVED` unless the corpus itself contains an explicit
authoritative supersession or resolution.

| ID | Source A | Source B | Conflict | Reachability | Impact | Resolution |
|---|---|---|---|---|---|---|
| AD-CFL-001 | AD-I-001 / AD-I-013 / AD-I-011…017 (English, `aps/`, `constitution/`) | AD-I-002 / AD-I-003 / AD-I-018 / AD-I-019 (Polish, root `.txt` + `.pdf`) | Same Document IDs (`AURA-CON-001`, `APS-100…950`) and same declared versions carried by two document sets in two languages with materially different lengths; `STYLE_GUIDE.md` §12 requires English for normative documents but neither set is marked non-normative or superseded | both REACHABLE_FROM_MAIN | **Which text is the specification** is undetermined for every APS document and for the FROZEN Constitution | **UNRESOLVED** |
| AD-CFL-002 | AD-I-001 `Status: FROZEN` | AD-I-002 `Status: FROZEN (po zatwierdzeniu)` | One copy freezes unconditionally, the other conditionally on approval, for the same constitutional document | both REACHABLE_FROM_MAIN | Precedence tier 1 of `CLAUDE.md` rests on a document whose freeze condition differs between its two copies | **UNRESOLVED** |
| AD-CFL-003 | AD-I-007 (`ADR-001`, PROPOSED, Document Model) | AD-I-008 (`ADR-001`, ACCEPTED, Repository Structure) and AD-I-009 (`ADR-001`, DRAFT, Document Model) | One identifier, three documents, three statuses, two distinct subjects | all REACHABLE_FROM_MAIN | Any citation of "ADR-001" is ambiguous; AD-I-007 is the document that would assign SPEC approval authority | **UNRESOLVED** — corpus records the class as `OQ-A-CONFLICT-011` |
| AD-CFL-004 | AD-I-049 (`CLAUDE.md` authority ladder) | AD-I-053 `OQ-A-CONFLICT-003` | A document occupying tier 6 of the ladder is the document that establishes the ordering of tiers 1–5 | both REACHABLE_FROM_MAIN | The precedence rule this audit is conducted under is itself of unestablished authority | **UNRESOLVED** |
| AD-CFL-005 | AD-I-051 Art. I: `Fixed-point arithmetic (Q16.16)` | AD-I-051 Art. I: `Scaling factor: 100,000 (10^5)`; AD-I-056 implements decimal 10^5 and **no Q16.16** | Two incompatible fixed-point representations declared immutable in one article, with no stated relationship, and an implementation that uses only one | REACHABLE_FROM_MAIN | Gates `ARI-D-007`, `ARI-D-008`, `ARI-D-014` | **UNRESOLVED** — corpus records it as `C-14`, *"Contradiction recorded, not resolved"* |
| AD-CFL-006 | AD-I-022 (ARI defined **only** by deferral to an implementation, in the specification corpus) | AD-I-051 / AD-I-052 / AD-I-056 (ARI constants and formula fixed in the implementation corpus) | The specification corpus defers ARI to the implementation; the implementation corpus fixes it as constitutional. Neither corpus grants any role authority over ARI **by name** | both REACHABLE_FROM_MAIN | **This is C-1 and C-2.** 27 `ARI-D-*` decisions depend on it | **UNRESOLVED — OPEN. Not addressed by this audit.** |
| AD-CFL-007 | AD-I-023 §18 (`NOT STARTED`) | AD-I-024 §7 (`CONSTRUCTED`) | Contradictory gate snapshots, both on `main` | both REACHABLE_FROM_MAIN | A `main`-only reader gets two incompatible BC-02 chain states | **UNRESOLVED** — recorded as stale by AD-I-025 §7 and AD-I-027 §11 (`D-OBS-01`), deliberately not corrected in either |
| AD-CFL-008 | AD-I-027 §5: *"The present record supersedes it as the current custodian state; the audit record remains the historical record."* | AD-I-025, whose face still reads `BLOCKED` | An asserted supersession that leaves the superseded record unmarked, by a record that simultaneously declares *"Authority created… NONE"* | both REACHABLE_FROM_MAIN | Whether the supersession is effective determines the current BC-02 state | **UNRESOLVED** — the assertion exists; whether AD-I-027 holds the authority to make it is not established by any observed artifact |
| AD-CFL-009 | AD-I-028 §1: `BC-02  CLOSED` | AD-I-035 §19: `BLOCKED — BC-02 CONSTRUCTION GAP` | The contract self-states BLOCKED; a downstream reachable record states it CLOSED | A REACHABLE_FROM_MAIN, B **BRANCH_LOCAL** | The BC-02 state visible from `main` is the opposite of the contract's own | **UNRESOLVED** |
| AD-CFL-010 | AD-I-035 §13.1: mandates `HANDOFF_TRANSFERRED` / `HANDOFF_REJECTED` / `HANDOFF_ERROR`, with a stated safety rationale for the prefix | AD-I-023 §5, AD-I-038 §5, and both executed receipts: bare `TRANSFERRED` / `NOT_TRANSFERRED` / `ERROR` | Contract vocabulary vs schema vocabulary vs emitted evidence; the middle token also differs | A **BRANCH_LOCAL**, B REACHABLE_FROM_MAIN | Both existing receipts carry the non-contract vocabulary | **UNRESOLVED** — routed in the corpus as `D-3` / `B-4` (AD-I-045) |
| AD-CFL-011 | AD-I-035 §5.2: `fixture_artifact_identity` = *"SHA-256(fixture_artifact_bytes) … issuer-computed"*; AD-I-038 §4 requires the digest form and rejects a name | AD-I-023 §4 states no digest requirement; both executed receipts carry `"FIX-DIGEST-P01.canonical.json"` | Two incompatible definitions of one field, with executed evidence on one side | A **BRANCH_LOCAL**, B REACHABLE_FROM_MAIN | Determines whether the two existing receipts are identity-bearing | **UNRESOLVED** — routed as `D-4` / `A-6` (AD-I-045) and `A-4` (AD-I-048) |
| AD-CFL-012 | AD-I-035 §15 defining `R-VAL-002` as *"Fixture identity fields are present"* | AD-I-034 `p01_handoff.rs` `R-VAL-002`, which additionally requires `fixture_id == "FIX-DIGEST-P01"` | Adapter assertion is narrower than the schema assertion it claims to implement; the peer RI-PY implementation does not carry the constraint | A **BRANCH_LOCAL**, B REACHABLE_FROM_MAIN | Cross-receiver asymmetry in the validation harness | **UNRESOLVED** — recorded `A-OBS-02`, **DEFERRED / NON-BLOCKING**, not fixed |
| AD-CFL-013 | AD-I-035 §5.3: `input_segment_sha256` *"computed once by the issuer at seal time"*; §7.1 `matches_issued_digest` | AD-I-035 §7.1 inline: *"RECOMPUTED BY THIS RECEIVER"*; both receivers implement recomputation; AD-I-038 marks both operands `RECEIVER_RECOMPUTED` | **The same contract carries both readings of one field.** AD-I-047 determines the set `INCOHERENT`; AD-I-041 §L.4 records §5.3, §7.1, §14 and §15.3 as not jointly satisfiable | contract **BRANCH_LOCAL**; receipts REACHABLE_FROM_MAIN | **Decision B (in AD-I-045's partition).** Determines whether `BNC-1` is detectable by `B-VAL-014` at all | **UNRESOLVED — OPEN. Not addressed by this audit.** |
| AD-CFL-014 | AD-I-035 §4.1 classifies `CONFORMANCE_FIXTURE_REGISTRY_v1` as a consumed authority and forbids inventing Registry fields | No Registry artifact exists on any of 56 + 79 refs; no issuance record; no issuer identity | The contract's declared input does not exist | contract **BRANCH_LOCAL**; the input **UNREACHABLE** | **Decision A (in AD-I-045's partition).** `VE-01…VE-04` undischargeable; `B-VAL-011`/`B-VAL-012` terms unbindable | **UNRESOLVED — OPEN. Not addressed by this audit.** |
| AD-CFL-015 | AD-I-037: `PRE-01: OPEN — BINDING GAP (Outcome B)` | AD-I-039: `PRE-01 — PASS` | Opposite dispositions of one identifier | **both BRANCH_LOCAL, on different branches** | Neither is visible from `main`; a `main`-only reader sees no PRE-01 state at all | **UNRESOLVED** |
| AD-CFL-016 | AD-I-038 (v2 schema, two operands, `EXTERNALLY_SUPPLIED` available) | AD-I-057 and AD-I-033, both emitting `SCHEMA_VERSION = 1` with one digest field | The schema said to be required for `B-VAL-014` is implemented by no receiver | A **BRANCH_LOCAL**, B REACHABLE_FROM_MAIN | `B-VAL-014` has no evidence representation in any deployed implementation | **UNRESOLVED** |
| AD-CFL-017 | AD-I-045 — **A = Fixture authority**, **B = Operand semantics / BNC-1** | AD-I-048 — **A = Boundary transfer semantics (interpretation)**, **B = Upstream authority supply (Registry / issuance)** | **Two Custodian Decision Packages A/B exist, committed 14 minutes apart on disjoint branches, and the labels `A` and `B` denote substantially transposed question sets between them.** AD-I-046 reviews AD-I-045 while recording that a file named as AD-I-048 does not exist | **both BRANCH_LOCAL, neither reachable from `main`** | **A Custodian instructed to "decide A and B" would be deciding different questions depending on which package is read.** Both packages disclaim authority, so neither supersedes the other | **UNRESOLVED** |
| AD-CFL-018 | `evidence/DQ-006_CLOSURE_PACKAGE.md`: RFC 8785 JCS + SHA-256 + RFC-6962 leaf — `CLOSED — PASS` | AD-I-055 §4–§5: D-3 concrete semantic value **NOT ESTABLISHED** | Incompatible statements about the same canonical-encoding question, one per corpus | both REACHABLE_FROM_MAIN in their repositories | Everything downstream of canonical encoding — DQ-002, DQ-006, INV-003, INV-011, CONF-003, CONF-010, the fixture corpus | **UNRESOLVED** — recorded as `CFL-001` (AD-I-063), *"Reconciled: 0 of 5"*; **structurally identical to C-2** |
| AD-CFL-019 | AD-I-062 §1: *"Aura adopts RI-RS as the canonical hash-domain model for CK-003"*, from the implementation corpus, `Status: CONDITIONALLY CLOSED / CI-BLOCKED` | AD-I-053: no cross-corpus precedence rule exists in either corpus | A protocol-scope adoption stated from a corpus whose authority to state it is unestablished | both REACHABLE_FROM_MAIN | Direct evidence for C-2 | **UNRESOLVED** |
| AD-CFL-020 | AD-I-063 `CFL-002`: `DQ-006_CLOSURE_PACKAGE.md:4` `CLOSED — PASS` | `CANONICAL-001_INDEPENDENT_ORACLE.md:3` `BLOCKED_PENDING_IMPLEMENTATION_CONFORMANCE`; `fixtures/corpus/CANONICAL-001_jcs_evidence.json:27-29` `"PENDING_EXECUTION"` ×3 | Three contradictory statuses for DQ-006 inside one repository | all REACHABLE_FROM_MAIN | Fixture-corpus status is indeterminate | **UNRESOLVED** — reproduced from AD-I-063, still open |

**Total conflicts recorded: 20.** Resolved by this audit: **0.**

---

## 7. SUPPRESSION OF FALSE SUPERSESSION

No artifact is marked SUPERSEDED in this record on the basis of a later artifact
existing. Supersession was tested against the four acceptable evidence forms
(explicit supersession statement, explicit replacement statement, authoritative
governance act, explicit deprecation/replacement record).

| Candidate supersession | Evidence found | Recorded as |
|---|---|---|
| AD-I-026 over AD-I-025 and AD-I-029 (BLOCKED → COMPLETE) | chronology only; no marker on either superseded record | **SUPERSESSION: NOT ESTABLISHED** |
| AD-I-027 over AD-I-025 | an **explicit statement** in AD-I-027 §5: *"The present record supersedes it as the current custodian state"* — made by a record that simultaneously declares it creates no authority | **ASSERTED; NOT ESTABLISHED** (see AD-CFL-008) |
| AD-I-027 §4 over AD-I-023 §18 | explicit statement, same caveat; AD-I-023 not modified | **ASSERTED; NOT ESTABLISHED** |
| AD-I-038 (v2) over AD-I-023 (v1) | AD-I-048 §2.1 records v1 as *"superseded for new receivers by v2"*; **no supersession act, and no receiver implements v2** | **SUPERSESSION: NOT ESTABLISHED** |
| AD-I-039 (`PRE-01 — PASS`) over AD-I-037 (`PRE-01 — OPEN`) | chronology and substantive sequence; no marker on AD-I-037 | **SUPERSESSION: NOT ESTABLISHED** — this is the PRE-01 status-token history §10 of the mandate names specifically |
| AD-I-048 over AD-I-045, or AD-I-045 over AD-I-048 | **none in either direction.** Neither package mentions the other; both disclaim authority | **SUPERSESSION: NOT ESTABLISHED** |
| AD-I-046 (review surface) over AD-I-048 | AD-I-046 records AD-I-048's path as ABSENT rather than superseded | **SUPERSESSION: NOT ESTABLISHED** |
| AD-I-013 (English APS-200) over AD-I-018 (Polish APS-200), or the reverse | no marker on either; identical declared version | **SUPERSESSION: NOT ESTABLISHED** |
| AD-I-001 over AD-I-002/003 | none | **SUPERSESSION: NOT ESTABLISHED** |
| AD-I-006 (v0.1.0 status snapshot) by later document headers | none | **SUPERSESSION: NOT ESTABLISHED** |
| AD-I-060/061 over AD-I-059 (`deliberately absent` → present) | none | **SUPERSESSION: NOT ESTABLISHED** |
| AD-I-053/054/063 over AD-I-058 (release closure) | none | **SUPERSESSION: NOT ESTABLISHED** |
| AD-I-009 vs AD-I-007 (same ADR, two paths, two statuses) | none | **SUPERSESSION: NOT ESTABLISHED** |

**One correction in the corpus does carry adequate in-place evidence** and is
recorded as such, not as a supersession of a document: AD-I-057 §0, the
`source_commit` correction `64bf959` → `d943807`, which states the reason,
retains the superseded value, and names its authorization. It supersedes **a
value**, not a record.

**Total supersessions established by this audit: 0.**

---

## 8. REACHABILITY ANALYSIS

### 8.1 Counts

| Repository | Load-bearing artifacts inventoried | REACHABLE_FROM_MAIN | BRANCH_LOCAL | UNREACHABLE (referenced, not located) |
|---|---|---|---|---|
| `aura-specification` | 48 groups/records | 34 | **14** | 9 (§2.7) |
| `aura-poc-a-core-v3.3` | 10 | 10 | 0 | — |
| `aura-guard-v1.3` | 4 | 4 | UNKNOWN (branch set not enumerated) | — |
| `.github` | 1 | 1 | UNKNOWN | — |
| `cargo` | 1 | 1 | UNKNOWN | — |

**Branch-local load-bearing artifacts: 14** (AD-I-035 … AD-I-048), all in
`aura-specification/conformance/boundary/`, distributed across **five** branches:

| Branch | Branch-local load-bearing artifacts |
|---|---|
| `claude/bc-02-immutable-fixture-handoff-3s3fkp` | AD-I-035 |
| `claude/bc-02-boundary-validation-q0h7yg` | AD-I-036 |
| `claude/ri-rs-p01-handoff-ga84l6` | AD-I-037 |
| `claude/bc-02-1-pre-01-schema-kvvm8z` | AD-I-038 … AD-I-046 (9) |
| `claude/bc-02-1-consistency-analysis-8ewd0q` | AD-I-047, AD-I-048 |

### 8.2 The authority-text reachability finding

```text
AUTHORITY TEXT REACHABILITY:
BRANCH-LOCAL
```

`BC-02_IMMUTABLE_FIXTURE_HANDOFF.md` (AD-I-035) is the sole source of
`B-VAL-011…020`, `BNC-1…BNC-7`, `VE-01…VE-05` and `DEP-001…005`. Every clause
that Decision A and Decision B turn on — under **either** package's partition —
is quoted from it. It exists at exactly one commit on exactly one branch and is
not an ancestor of `origin/main`.

```text
MAIN-ONLY AUDITABILITY:
NOT ESTABLISHED
```

**This is not a finding of invalidity.** Per §11 of the mandate under which this
audit is conducted, branch-local status is recorded as a fact about reachability
and nothing is inferred from it about semantic validity.

### 8.3 Cross-branch dependency

Both Decision Packages cite records that are not reachable from their own
branches:

| Package | Cites | Reachable from the package's own branch? |
|---|---|---|
| AD-I-045 (`…kvvm8z`) | `R1` = AD-I-035 (`…3s3fkp`), `R2` = AD-I-036 (`…q0h7yg`), `R8` = AD-I-037 (`…ga84l6`) | **NO** |
| AD-I-048 (`…8ewd0q`) | `N-01` = AD-I-035, `N-02` = AD-I-036, `N-10` = AD-I-037, `N-11…N-14` = AD-I-038…041 (`…kvvm8z`) | **NO** |

**No single ref in the corpus carries the complete BC-02 record set.** A reader
must assemble it from five branches plus `main`. Recorded; not remedied.

---

## 9. AUTHORITY ANALYSIS

For each authority-bearing artifact: (1) explicit claim? (2) domain claimed?
(3) upstream evidence present? (4) established? (5) conflicting authority?
(6) reachable from `main`?

| Artifact | 1. Explicit claim | 2. Domain | 3. Upstream evidence | 4. Established | 5. Conflicting authority | 6. On `main` |
|---|---|---|---|---|---|---|
| AD-I-001 Constitution | YES | all Aura governance | self-declared FROZEN; no ratification artifact observed | **ASSERTED** | AD-I-002 (conditional freeze), AD-I-051 | YES |
| AD-I-004 GOVERNANCE (GOV-001) | YES | approval routes, status transitions | DRAFT | **CANDIDATE** | AD-I-007, AD-I-051, AD-I-052 | YES |
| AD-I-010 APS-001 | YES — *"Root Normative Specification"* | protocol semantics | Constitution (FROZEN) | **CANDIDATE** — itself DRAFT, review required | AD-I-051 | YES |
| AD-I-011…017 APS set | YES — each `Classification: Normative Specification` | protocol semantics | APS-001 (DRAFT) | **CANDIDATE** | duplicate Polish set (AD-CFL-001) | YES |
| AD-I-021 CONF-003 | YES — *"normative conformance requirement"* | canonical serialization; §4.5 is the execution gate | APS-400 §4 (DRAFT) | **CANDIDATE** — header DRAFT | AD-CFL-018, AD-CFL-020 | YES |
| AD-I-049 `CLAUDE.md` ladder | YES — orders 10 tiers | agent conduct + authority ordering | none for the ordering itself | **UNRESOLVED** | AD-CFL-004 | YES |
| AD-I-051 Constitutional Decree | YES — `MANDATORY / NON-OVERRIDABLE`, `Perpetual` | constants, arithmetic, architecture | Custodian named; no ratification artifact observed | **ASSERTED** | AD-I-001, AD-I-010, AD-CFL-005 | YES |
| AD-I-052 Custodian Role | YES — `FINAL AUTHORITY` over `core/`; `SOLE AUTHORITY` over sealing | implementation corpus | self-declared `CANONICAL` | **ASSERTED** | AD-I-004 (Chief Architect route) | YES |
| AD-I-027 BC-02 closure | **Disclaims** (*"Authority created: NONE"*) while performing supersession and issuing a *"Custodian decision"* | BC-02 chain state | cites a named custodian authorization; **no signed artifact observed** | **UNRESOLVED** | AD-CFL-008 | YES |
| AD-I-035 BC-02 contract | **Disclaims** — *"NON-NORMATIVE / Authority created: NONE"* | boundary handoff engineering | consumed authorities absent | **NONE (self-declared)** | AD-CFL-009, AD-CFL-013, AD-CFL-014 | **NO** |
| AD-I-045, AD-I-048 packages | **Both disclaim** | routing only | — | **NONE (self-declared)** | AD-CFL-017 | **NO** |
| AD-I-062 guard DQ-002 verdict | Implicit — states an adoption | hash-domain model, protocol scope | none observed | **UNRESOLVED** | AD-CFL-019 | YES |

### 9.1 Questions this section does NOT answer

Per the mandate, and stated explicitly so the boundary is unambiguous:

- Whether Chief Architect outranks Protocol Custodian — **NOT DECIDED**
- Whether ARI is protocol content or instrument content — **NOT DECIDED (C-1)**
- Which corpus's authority ladder governs — **NOT DECIDED (C-2)**
- Whether AD-I-027 held the authority to declare AD-I-025 superseded — **NOT DECIDED**
- Whether either Decision Package's A/B partition is the correct one — **NOT DECIDED**

No authority path is created, recommended, ranked or scored anywhere in this
record.

---

## 10. ARI — RECORDED SURFACE (NO NORMALIZATION)

ARI is treated as an **unresolved normative surface**. The following are
recorded strictly at the level the corpus supports, using only the vocabulary
`IMPLEMENTED` / `OBSERVED` / `PROPOSED` / `CANDIDATE` / `UNKNOWN`.

| Item | Where observed | Recorded as | Explicitly NOT recorded as |
|---|---|---|---|
| `RAW_ARI = 0.3·SI + 0.7·SA` | `core/evaluator.py:4, :97` (AD-I-056) | **IMPLEMENTED / OBSERVED** | not NORMATIVE, not REQUIRED, not CANONICAL |
| `SCALING_FACTOR = 100000`; weights `30000` / `70000` | `core/evaluator.py:12, :22–23` | **IMPLEMENTED / OBSERVED** | as above |
| `Q16.16` | AD-I-051 Art. I §1; `.github/copilot-instructions.md:20`; `.github/github/copilot-instructions.md:18` | **CANDIDATE** (declared constitutional constant; **implemented nowhere**) | as above |
| `scale = 100000` as a constitutional constant | AD-I-051 Art. I §1, §8 (`FROZEN`) | **CANDIDATE / declared** | as above |
| `RAW_ARI` as a named quantity | `core/evaluator.py`; `RD-006_ARI_OBSERVABILITY.md` | **IMPLEMENTED / OBSERVED** | as above |
| `adjusted_ari` | core implementation and tests | **IMPLEMENTED / OBSERVED** | as above |
| ARI as a protocol term | `glossary/GLOSSARY.md:27-28` — *"computed by RI-PY … a measurement, not a decision"* | **OBSERVED** — a definition by deferral to an implementation | as above |
| `B-I` / `B-II` | AD-I-045 §5.3 (options under its Decision B) | **PROPOSED** — stated options, neither selected | as above |
| `input_segment_sha256` | AD-I-035 §5.3 and §7.1 (two incompatible readings in one document) | **UNKNOWN** | as above |
| issuer-sealed interpretation | AD-I-035 §5.3; AD-I-045 `B-I`; AD-I-048 `A-2-β` | **CANDIDATE** | as above |
| receiver-recomputed interpretation | AD-I-035 §7.1; AD-I-045 `B-II`; AD-I-048 `A-2-α`; implemented by both receivers | **IMPLEMENTED / OBSERVED** as behaviour; **CANDIDATE** as semantics | as above |

**No ARI semantics are defined, selected, ranked or inferred anywhere in this
record.** No implementation behaviour is promoted to specification. No fixture,
test or reference implementation is promoted to authority.

---

## 11. C-1 / C-2 — EVIDENCE INVENTORY ONLY

```text
C-1  Is ARI protocol content or instrument content?     OPEN
C-2  Which governance corpus has precedence for ARI?    OPEN
```

Both are **defined in the corpus** at
`aura-poc-a-core-v3.3/review/2026-08-12_OQ-A_GOVERNANCE_JURISDICTION/06_ARI_DECISION_AUTHORITY.md:111-112`
(AD-I-053). That record's own finding is `CONDITIONALLY DETERMINABLE`, and it
states: *"Who may establish ARI semantics cannot be stated today."*

Evidence relevant to C-1 and C-2 located by this audit, **inventoried without
weighting**:

| Evidence | Bears on | Recorded fact |
|---|---|---|
| AD-I-022 — ARI's only occurrence in the specification corpus, defined by deferral to RI-PY | C-1 | The specification corpus does not define ARI |
| AD-I-051 Art. I — ARI constants declared constitutional constants in the implementation corpus | C-1, C-2 | The implementation corpus does fix them |
| AD-I-053 §1 — exhaustive check of 10 authority grants: **none names ARI** | C-1, C-2 | No role holds named authority over ARI |
| AD-I-053 §2 — Chief Architect route (specification ladder) vs Custodian route (implementation ladder), both explicitly documented | C-2 | Two documented routes, neither established for ARI |
| AD-I-053 `OQ-A-CONFLICT-001`, `-004`, `-010`, `-013` | C-2 | Cross-corpus and intra-corpus authority conflicts, 0 of 13 reconciled |
| AD-I-054 `ARI-D-001` — whether Aura undertakes to define ARI at all — **open**, gating 26 further decisions | C-1 | 27 decisions, 0 answered |
| AD-CFL-018 / AD-I-063 `CFL-001` — the same cross-corpus precedence question arising for canonical encoding, `Reconciled: 0 of 5` | C-2 | The C-2 question recurs outside ARI and is unresolved there too |
| AD-CFL-019 — AD-I-062 stating a protocol-scope adoption from the implementation corpus | C-2 | A precedent act exists whose authority is unestablished |
| AD-CFL-004 — the `CLAUDE.md` ladder ordering tiers 1–5 from tier 6 | C-2 | The instrument that would settle precedence is of unestablished authority |

**No answer, no candidate ranking, no authority path, and no recommendation is
produced.** C-1 and C-2 remain exactly as the corpus leaves them.

---

## 12. DECISION A / DECISION B — RECORDED STATE ONLY

**Neither A nor B is resolved, scored, ranked or recommended here.** What this
audit records is the *state of the A/B record set*, which is itself a
normalization problem.

### 12.1 Two packages, two partitions

| | AD-I-045 — `BC-02.1-CUSTODIAN-DECISION-PACKAGE-A-B.md` | AD-I-048 — `BC-02-CUSTODIAN-DECISION-PACKAGE-A-B-v1.md` |
|---|---|---|
| Commit / time | `66bfdb1` · 2026-08-24T20:12:29Z | `dd11311` · 2026-08-24T20:26:23Z |
| Branch | `claude/bc-02-1-pre-01-schema-kvvm8z` | `claude/bc-02-1-consistency-analysis-8ewd0q` |
| Blob | `deaf6635787a970474ac8852e7f6f8e814f11f92` | `03d22a28274ddcab10184b56566e71cfcd3e5366` |
| Reachable from `main` | **NO** | **NO** |
| **Decision A** | **Fixture authority** — Registry supply, `fixture_hash` rule, issuance event, issuer identity, sealed store; `A-1…A-8`; options `A-I` / `A-II` / `A-III` | **Boundary transfer semantics** — interpretation of existing contract text; `A-1…A-5`; per-question candidates `α` / `β` |
| **Decision B** | **Operand semantics / BNC-1 detectability** — `B-1…B-5`; options `B-I` / `B-II` / `B-III` | **Upstream authority supply** — Registry, `fixture_hash` rule, issuer; `B-1…B-3`; candidates `α` / `β` / `γ` |
| Own record inventory | `R1…R15` | `N-01…N-17` |
| Own divergence register | `D-1…D-10` | `DIV-01…DIV-07` |
| Terrain Survey | *"CLOSED — diagnostic"* | *"CLOSED — DIAGNOSTICALLY COMPLETE"* |
| Declared authority | NONE | NONE |

**Observation, recorded without resolution:** the two packages assign the labels
`A` and `B` to substantially **transposed** question sets. AD-I-045's Decision A
(fixture/Registry/issuance authority) corresponds closely in subject matter to
AD-I-048's Decision **B**; AD-I-045's Decision B (operand semantics) corresponds
closely to AD-I-048's Decision **A**. Neither package references the other, and
neither claims precedence.

**This audit does not determine which partition governs, does not merge them,
does not rank them, and does not select A-I, A-II, A-III, B-I, B-II or B-III
under either.** See AD-CFL-017 and AD-OS-014.

### 12.2 The reviewed-package chain

```text
AD-I-047  S-3/S-4/S-5 consistency record   17:03  branch …8ewd0q   INCOHERENT
AD-I-045  Decision Package A/B             20:12  branch …kvvm8z   A, B OPEN
AD-I-048  Decision Package A/B v1          20:26  branch …8ewd0q   A, B PREPARED
AD-I-046  Decision Review Surface v1       22:20  branch …kvvm8z   reviews AD-I-045;
                                                                   records AD-I-048's
                                                                   path as ABSENT
```

All four are branch-local. Three of the four declare a *Terrain Survey* closed;
**no Terrain Survey artifact exists** (§2.7). Recorded as AD-N-009.

### 12.3 Items explicitly not touched

`B-VAL-012`, `B-VAL-014`, `BNC-1…BNC-7`, `CONF-003 §4.5`, `N-01…N-08` and
`C1–C8` were **not executed**. No fixture, Registry entry, issuance record or
receipt was created or modified. `input_segment_sha256` semantics were **not
determined**. Issuer-sealed vs receiver-recomputed was **not determined**.
Fixture authority was **not determined**.

---

## 13. NORMALIZATION MATRIX

Descriptive only. **This matrix is not a canonical specification and creates no
normative semantics.** `Declared` quotes the source token verbatim.

| Artifact | Domain | Class | Reachability | Declared | Semantic | Authority | Evidence | Execution | Conflict |
|---|---|---|---|---|---|---|---|---|---|
| AD-I-001 Constitution (EN) | governance | GOVERNANCE | MAIN | `FROZEN` | ESTABLISHED | ASSERTED | OBSERVED | N/A | AD-CFL-001/002 |
| AD-I-002/003 Constitution (PL) | governance | GOVERNANCE | MAIN | `FROZEN (po zatwierdzeniu)` | NOT DETERMINED | ASSERTED | CONFLICTING | N/A | AD-CFL-001/002 |
| AD-I-004 GOV-001 | governance | GOVERNANCE | MAIN | `DRAFT` | PROPOSED | CANDIDATE | PARTIAL | N/A | AD-CFL-004 |
| AD-I-006 v0.1.0 status | governance | AUTHORITY_RECORD | MAIN | (table) | NOT DETERMINED | NONE | CONFLICTING | N/A | AD-DIV-001 |
| AD-I-007/008/009 ADR-001 ×3 | governance | DECISION_RECORD | MAIN | `PROPOSED` / `ACCEPTED` / `DRAFT` | NOT DETERMINED | CANDIDATE | CONFLICTING | N/A | AD-CFL-003 |
| AD-I-010 APS-001 | specification | SPECIFICATION | MAIN | `0.2-DRAFT` | PROPOSED | CANDIDATE | PARTIAL | N/A | AD-DIV-001 |
| AD-I-011…017 APS set (EN) | specification | SPECIFICATION | MAIN | `1.0-DRAFT` | PROPOSED | CANDIDATE | PARTIAL | N/A | AD-CFL-001 |
| AD-I-018/019 APS set (PL) | specification | SPECIFICATION | MAIN | `DRAFT` | NOT DETERMINED | CANDIDATE | CONFLICTING | N/A | AD-CFL-001 |
| AD-I-020 Invariant Registry | specification | SPECIFICATION | MAIN | `1.0-DRAFT` | PROPOSED | CANDIDATE | PARTIAL | N/A | — |
| AD-I-021 CONF-003 | conformance | CONFORMANCE | MAIN | `DRAFT` + *"normative"* | NOT DETERMINED | CANDIDATE | CONFLICTING | **NOT EXECUTED** (§4.5 NO RESULT) | AD-DIV-002 |
| AD-I-022 Glossary (ARI) | measurement/ARI | SPECIFICATION | MAIN | `1.0-DRAFT` | OPEN | NONE | OBSERVED | N/A | AD-CFL-006 |
| AD-I-023 BC-02.1 v1 | conformance | ENGINEERING_CONTRACT | MAIN | `CONSTRUCTED` | ESTABLISHED | NONE | OBSERVED | BLOCKED | AD-CFL-007 |
| AD-I-024 BC-02.3 | conformance | ENGINEERING_CONTRACT | MAIN | `CONSTRUCTED` | ESTABLISHED | NONE | OBSERVED | BLOCKED | AD-CFL-007 |
| AD-I-025 Pre-exec audit | evidence | AUDIT | MAIN | `BLOCKED` | ESTABLISHED (hist.) | NONE | OBSERVED | NOT EXECUTED | AD-DIV-004 |
| AD-I-026 P-01 handoff | evidence | EVIDENCE | MAIN | `COMPLETE` | ESTABLISHED | NONE | ESTABLISHED | **EXECUTED** | AD-DIV-004 |
| AD-I-027 Custodian closure | governance | AMBIGUOUS | MAIN | `CLOSED AT THE EVIDENCE-GENERATION LAYER` | ESTABLISHED (scoped) | UNRESOLVED | ESTABLISHED | NOT EXECUTED | AD-CFL-008 |
| AD-I-028 B-VAL-014 recon | conformance | DECISION_RECORD | MAIN | `COMPLETE` / `NOT EXECUTED` | ESTABLISHED (defn) | NONE | OBSERVED | NOT EXECUTED | AD-CFL-009 |
| AD-I-031 P-01 receipts | evidence | EVIDENCE | MAIN | `24/24 PASS` | **NOT DETERMINED** (conformance) | NONE | ESTABLISHED | EXECUTED | AD-CFL-010/011 |
| AD-I-032 FIX-DIGEST-P01 | fixture | FIXTURE (contested) | MAIN | — | OPEN | NONE | OBSERVED (bytes) / NONE (issuance) | consumed | AD-CFL-011/014 |
| AD-I-035 BC-02 contract | conformance | ENGINEERING_CONTRACT | **BRANCH_LOCAL** | `BLOCKED — CONSTRUCTION GAP` | OPEN | NONE | PARTIAL | BLOCKED | AD-CFL-009/013/014 |
| AD-I-036 Boundary validation | conformance | AUDIT | **BRANCH_LOCAL** | `BLOCKED` | OPEN | NONE | PARTIAL | BLOCKED | AD-DIV-006 |
| AD-I-037 PRE-01 binding | conformance | AUDIT | **BRANCH_LOCAL** | `OPEN — OUTCOME B` | OPEN | NONE | PARTIAL | NOT EXECUTED | AD-CFL-015 |
| AD-I-038 BC-02.1 v2 | conformance | ENGINEERING_CONTRACT | **BRANCH_LOCAL** | `CONSTRUCTED` | ESTABLISHED | NONE | OBSERVED | NOT EXECUTED | AD-CFL-016 |
| AD-I-039 PRE-01 correction | conformance | DECISION_RECORD | **BRANCH_LOCAL** | `PRE-01 — PASS` | **NOT DETERMINED** | NONE | PARTIAL | NOT EXECUTED | AD-CFL-015 |
| AD-I-040/041 PRE-02/03 | conformance | DECISION_RECORD / AUDIT | **BRANCH_LOCAL** | `BLOCKED` / *"Answer NO"* | BLOCKED | NONE | PARTIAL | BLOCKED | — |
| AD-I-045 Package A/B | governance | AMBIGUOUS | **BRANCH_LOCAL** | `A and B OPEN` | OPEN | NONE | OBSERVED | NOT EXECUTED | **AD-CFL-017** |
| AD-I-046 Review Surface | governance | AUDIT | **BRANCH_LOCAL** | read-only | OPEN | NONE | OBSERVED | NOT EXECUTED | AD-DIV-010 |
| AD-I-047 S-3/S-4/S-5 | conformance | AUDIT | **BRANCH_LOCAL** | `INCOHERENT` | OPEN | NONE | OBSERVED | NOT EXECUTED | AD-CFL-013 |
| AD-I-048 Package A/B v1 | governance | AMBIGUOUS | **BRANCH_LOCAL** | `PREPARED — NOT RESOLVED` | OPEN | NONE | OBSERVED | NOT EXECUTED | **AD-CFL-017** |
| AD-I-049 CLAUDE.md | governance | GOVERNANCE | MAIN | — | ESTABLISHED (instr.) | UNRESOLVED | OBSERVED | N/A | AD-CFL-004 |
| AD-I-051 Decree | governance | GOVERNANCE | MAIN | `MANDATORY / NON-OVERRIDABLE` | ASSERTED | ASSERTED | PARTIAL | N/A | AD-CFL-005/006 |
| AD-I-052 Custodian Role | governance | GOVERNANCE | MAIN | `CANONICAL` | ASSERTED | ASSERTED | OBSERVED | N/A | AD-CFL-006 |
| AD-I-053 OQ-A package | authority topology | AUDIT | MAIN | `Normative effect: NONE` | OPEN | NONE | ESTABLISHED | N/A | AD-CFL-004/006 |
| AD-I-054 RD-1 ARI register | measurement/ARI | AUDIT | MAIN | `Normative effect: NONE` · 27 decisions, 0 answered | OPEN | NONE | ESTABLISHED | N/A | AD-CFL-006 |
| AD-I-055 D3/D4 record | specification | DECISION_RECORD | MAIN | `NOT ESTABLISHED` | OPEN | NONE | PARTIAL | NOT EXECUTED | AD-CFL-018 |
| AD-I-056 evaluator.py | measurement/ARI | IMPLEMENTATION | MAIN | code | **IMPLEMENTED / OBSERVED** | NONE | OBSERVED | N/A | AD-CFL-005 |
| AD-I-057 BC-02.2 set | conformance | ENGINEERING_CONTRACT | MAIN (core) | `CONSTRUCTED` · `P-01: NOT EXECUTED` | ESTABLISHED | NONE | ESTABLISHED | BLOCKED | AD-DIV-011 |
| AD-I-058 Release closure | historical | HISTORICAL | MAIN | `REGULATORY RELEASE ASSESSMENT` | HISTORICAL | ASSERTED | OBSERVED | EXECUTED (2026-07) | AD-DIV-012 |
| AD-I-059 D3 blocker | evidence | AUDIT | MAIN (guard) | `STOPPED` | HISTORICAL | NONE | OBSERVED | NOT EXECUTED | AD-DIV-013 |
| AD-I-062 DQ-002 verdict | specification | DECISION_RECORD | MAIN (guard) | `CONDITIONALLY CLOSED / CI-BLOCKED` | NOT DETERMINED | UNRESOLVED | PARTIAL | BLOCKED | AD-CFL-019 |
| AD-I-063 CK-003 conflict reg. | authority topology | AUDIT | MAIN | `Reconciled: 0 of 5` | OPEN | NONE | ESTABLISHED | N/A | AD-CFL-018/020 |
| AD-I-065 org GUIDELINES | governance | GOVERNANCE | MAIN (.github) | — | NOT DETERMINED | NONE | CONFLICTING | N/A | AD-DIV-015 |

---

## 14. OPEN LOAD-BEARING SURFACES

Each surface states `WHY OPEN`, `SOURCE`, `DEPENDENCY`, `DOES NOT RESOLVE`.
**No solution is proposed for any of them.**

### GOVERNANCE

**AD-OS-001 — Cross-corpus precedence**
WHY OPEN: no precedence rule between the specification corpus and the implementation corpus exists in either corpus; the only text ordering them (AD-I-049) is itself of unestablished authority.
SOURCE: AD-I-053 `OQ-A-CONFLICT-001`, `-003`, `-010`; AD-I-063 `CFL-001`.
DEPENDENCY: every cross-corpus semantic question, including C-2 and AD-CFL-018.
DOES NOT RESOLVE: this audit records the conflict and answers none of it.

**AD-OS-002 — Constitutional freeze condition**
WHY OPEN: two copies of `AURA-CON-001` v1.0 declare `FROZEN` and `FROZEN (po zatwierdzeniu)` respectively.
SOURCE: AD-I-001, AD-I-002.
DEPENDENCY: precedence tier 1.
DOES NOT RESOLVE: neither copy is selected.

**AD-OS-003 — ADR-001 identifier**
WHY OPEN: one identifier, three documents, three statuses, two subjects.
SOURCE: AD-I-007, AD-I-008, AD-I-009.
DEPENDENCY: any citation of `ADR-001`, including the SPEC-approval-authority claim.
DOES NOT RESOLVE: no renumbering, no selection.

**AD-OS-004 — Authority of the governance-reconciliation act**
WHY OPEN: AD-I-027 declares a supersession and issues a "Custodian decision" while declaring it creates no authority; no signed or countersigned artifact was observed.
SOURCE: AD-I-027 §2, §5, §14; AD-CFL-008.
DEPENDENCY: the current BC-02 state as visible from `main`.
DOES NOT RESOLVE: the assertion is recorded; its effectiveness is not adjudicated.

### SPECIFICATION

**AD-OS-005 — Which text is the specification**
WHY OPEN: every APS document and the Constitution exist as two representations, in two languages, at one document ID and one declared version, with no supersession marker; `STYLE_GUIDE.md` §12 requires English for normative documents but marks neither set.
SOURCE: AD-I-001…003, AD-I-011…019, AD-I-005.
DEPENDENCY: precedence tiers 1–3 in their entirety.
DOES NOT RESOLVE: neither representation is selected.

**AD-OS-006 — Normative status of a DRAFT corpus**
WHY OPEN: every document in precedence tier 2 is `DRAFT` while declaring `Classification: Normative Specification`; CONF-003 additionally asserts in-force normative effect from a DRAFT header.
SOURCE: AD-I-010…017, AD-I-021.
DEPENDENCY: every conformance claim.
DOES NOT RESOLVE: no status transition is performed or proposed.

**AD-OS-007 — Canonical encoding**
WHY OPEN: `CLOSED — PASS` in one corpus, `NOT ESTABLISHED` in the other, and three contradictory statuses inside one repository.
SOURCE: AD-CFL-018, AD-CFL-020, AD-I-055, AD-I-063.
DEPENDENCY: DQ-002, DQ-006, INV-003, INV-011, CONF-003, CONF-010, the fixture corpus.
DOES NOT RESOLVE: no side is chosen.

### MEASUREMENT / ARI

**AD-OS-008 — C-1: is ARI protocol content or instrument content**
WHY OPEN: the specification corpus defines ARI only by deferral to an implementation; the implementation corpus fixes it as a constitutional constant; no authority grant names ARI.
SOURCE: AD-I-022, AD-I-051, AD-I-053 §1, §6.
DEPENDENCY: `ARI-D-001` and, through it, the other 26 ARI decisions.
DOES NOT RESOLVE: **explicitly not answered.**

**AD-OS-009 — C-2: which corpus's ladder governs ARI**
WHY OPEN: two documented routes (Chief Architect / Protocol Custodian), neither established for ARI; the same question recurs unresolved for canonical encoding.
SOURCE: AD-I-053 §6; AD-CFL-018, AD-CFL-019.
DEPENDENCY: C-1's operative effect; every ARI decision.
DOES NOT RESOLVE: **explicitly not answered.**

**AD-OS-010 — Q16.16 vs decimal 10^5**
WHY OPEN: both are declared immutable constitutional constants in one article with no stated relationship; the implementation uses only the decimal scale.
SOURCE: AD-I-051 Art. I §1; AD-I-056; AD-I-054 `C-14`.
DEPENDENCY: `ARI-D-007`, `ARI-D-008`, `ARI-D-014`.
DOES NOT RESOLVE: no reconciliation is offered.

### EVIDENCE

**AD-OS-011 — Superseded-in-fact dispositions carried unmarked**
WHY OPEN: at least four records (AD-I-025, AD-I-029, AD-I-057 header, AD-I-059) present dispositions that later events changed, with no supersession vocabulary available in the corpus.
SOURCE: AD-DIV-004, AD-DIV-011, AD-DIV-013.
DEPENDENCY: any reader reconstructing current state from document faces.
DOES NOT RESOLVE: nothing is marked, nothing is edited.

**AD-OS-012 — Whether the stored receipt file is the transport artifact**
WHY OPEN: both adapters append `0x0A` beyond the §12 serialization; whether the stored file or the serialization is the artifact is undetermined.
SOURCE: AD-I-025 §4.1 `A-OBS-01`; AD-I-027 §11.
DEPENDENCY: §12 compliance reading of every stored receipt.
DOES NOT RESOLVE: recorded `DEFERRED / NON-BLOCKING` in the corpus; unchanged here.

### CONFORMANCE

**AD-OS-013 — B-VAL-014 has no implemented evidence representation**
WHY OPEN: `B-VAL-014` requires two operands; both deployed receivers emit `SCHEMA_VERSION = 1` with one digest field; the v2 schema that represents both is branch-local and bound to no receiver.
SOURCE: AD-I-023, AD-I-033, AD-I-038, AD-I-057; AD-CFL-016.
DEPENDENCY: any future `B-VAL-014` execution; `CONF-003 §4.5`.
DOES NOT RESOLVE: no binding is performed; `B-VAL-014` is **NOT EXECUTED**.

**AD-OS-014 — Which A/B partition is the decision set**
WHY OPEN: two Decision Packages exist, both branch-local, both disclaiming authority, assigning transposed question sets to the labels `A` and `B`.
SOURCE: AD-I-045, AD-I-048; AD-CFL-017.
DEPENDENCY: any Custodian ruling described as "Decision A" or "Decision B".
DOES NOT RESOLVE: **neither package is selected, merged, ranked or renamed.**

**AD-OS-015 — BNC-1 detectability**
WHY OPEN: `BC-02` §5.3, §7.1, §14 and §15.3 are recorded as not jointly satisfiable without determining which value `input_segment_sha256` carries.
SOURCE: AD-I-035; AD-I-041 §L.4; AD-I-047; AD-CFL-013.
DEPENDENCY: `B-VAL-012`, `B-VAL-014`, `BNC-1`.
DOES NOT RESOLVE: **explicitly not answered; nothing executed.**

### IMPLEMENTATION

**AD-OS-016 — Adapter assertion narrower than the schema assertion**
WHY OPEN: RI-RS `R-VAL-002` adds a fixture-specific conjunct beyond BC-02.1 §15; RI-PY does not.
SOURCE: AD-I-025 §4.2 `A-OBS-02`; AD-CFL-012.
DEPENDENCY: cross-receiver symmetry of the validation harness.
DOES NOT RESOLVE: recorded `DEFERRED`; no code is changed.

**AD-OS-017 — Guard-repository branch coverage**
WHY OPEN: this audit searched only the checked-out branch of `aura-guard-v1.3`, `.github` and `cargo`.
SOURCE: §1.2.
DEPENDENCY: any corpus-wide absence claim touching those repositories.
DOES NOT RESOLVE: the gap is declared, not closed.

### REGISTRY / ISSUANCE

**AD-OS-018 — No Fixture Registry**
WHY OPEN: `CONFORMANCE_FIXTURE_REGISTRY_v1` is a declared consumed authority of `BC-02` and exists nowhere across 56 + 79 refs.
SOURCE: AD-I-035 §4.1; §2.7.
DEPENDENCY: `DEP-001`, `VE-01`, `B-VAL-011`, `B-VAL-012`.
DOES NOT RESOLVE: **no Registry is created.**

**AD-OS-019 — No issuance record and no issuer identity**
WHY OPEN: `BC-02` §5.3 and §7.1 require issuer-computed values at seal time; no issuance record, `issuance_id` value or issuer identity exists.
SOURCE: AD-I-035; AD-I-032; AD-I-030 §11.
DEPENDENCY: `DEP-003`, `VE-03`, the top two arrows of the §5.5 traceability chain.
DOES NOT RESOLVE: **no issuance record is created.** The artifact's byte identity (§1.4) is not evidence of issuance.

**AD-OS-020 — `fixture_hash` rule undeclared**
WHY OPEN: neither covered octets nor encoding is declared anywhere; `BC-02` §5.4 states that comparing a Registry's declared value against itself *"has verified nothing"*.
SOURCE: AD-I-035 §5.4; `DEP-002`, `VE-02`.
DEPENDENCY: `fixture_hash_verification`, held UNKNOWN.
DOES NOT RESOLVE: no rule is declared; UNKNOWN is preserved, not converted.

### AUTHORITY TOPOLOGY

**AD-OS-021 — Load-bearing text unreachable from `main`**
WHY OPEN: 14 load-bearing artifacts, including the BC-02 contract itself, exist only on five branches; no single ref carries the complete record set.
SOURCE: §8.
DEPENDENCY: `main`-only auditability of the entire boundary programme.
DOES NOT RESOLVE: **nothing is merged; no PR is opened; integration is a question, not an action taken here.**

**AD-OS-022 — Absence of a supersession vocabulary**
WHY OPEN: the corpus has no status token for "overtaken by a later recorded event"; both Decision Packages record this gap and neither fills it.
SOURCE: AD-I-045 §3.2 (`D-6`); §7 of this record.
DEPENDENCY: every status-token history, notably `PRE-01`.
DOES NOT RESOLVE: no vocabulary is created.

**AD-OS-023 — `DEP-001…005` held UNKNOWN**
WHY OPEN: declared `SATISFIED FOR P-01` by task headers; recorded `OPEN` by five artifacts; no closure artifact reachable.
SOURCE: AD-DIV-016.
DEPENDENCY: the BC-02 entry condition.
DOES NOT RESOLVE: **held UNKNOWN; not converted in either direction.**

**Total open load-bearing surfaces: 23.**

---

## 15. NORMALIZATION FINDINGS

Each finding is observational. `STATUS` never records a fix.

---

**AD-N-001 — Two Custodian Decision Packages A/B exist with transposed A/B partitions**
SOURCE: AD-I-045 (`66bfdb1`, blob `deaf6635…`), AD-I-048 (`dd11311`, blob `03d22a28…`).
OBSERVATION: Two artifacts, committed 14 minutes apart on disjoint branches, both titled a Custodian Decision Package A/B, both declaring the Terrain Survey closed and A and B open, assign substantially transposed question sets to the labels `A` and `B`. Neither references the other; neither claims precedence.
IMPACT: A ruling expressed as "Decision A" or "Decision B" is ambiguous until the governing package is identified. **A ruling issued against one package does not map onto the other.**
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-002 — Both Decision Packages are unreachable from `main`**
SOURCE: §8.1.
OBSERVATION: Neither package, nor the review surface reviewing one of them, nor the contract they analyse, is reachable from `origin/main` of `aura-specification`.
IMPACT: A Custodian reading `main` sees no decision package and no BC-02 contract.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-003 — The most load-bearing artifact in the boundary programme is branch-local**
SOURCE: AD-I-035 at `e2066bd`, branch `claude/bc-02-immutable-fixture-handoff-3s3fkp`.
OBSERVATION: `BC-02_IMMUTABLE_FIXTURE_HANDOFF.md` is the sole source of `B-VAL-011…020`, `BNC-1…BNC-7`, `VE-01…VE-05` and `DEP-001…005`, and is cited by every downstream record including records that are on `main`.
IMPACT: `MAIN-ONLY AUDITABILITY: NOT ESTABLISHED` for the entire boundary chain.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-004 — No single ref carries the complete BC-02 record set**
SOURCE: §8.3.
OBSERVATION: The set spans `main` plus five branches; both packages cite records unreachable from their own branches.
IMPACT: Every reading of the corpus is partial unless the reader assembles six refs.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-005 — Two absence claims are contradicted by artifacts on other branches**
SOURCE: AD-DIV-009 (AD-I-045 §2), AD-DIV-010 (AD-I-046 §1.1).
OBSERVATION: Both claims are stated as corpus-wide (*"no reachable commit of any in-scope repository"*) without naming the ref set measured. Each is contradicted by an artifact committed earlier on a different branch.
IMPACT: Corpus-wide absence claims in this corpus are not independently reproducible unless the measured ref set is stated.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-006 — Contradictory gate snapshots coexist on `main`**
SOURCE: AD-I-023 §18 vs AD-I-024 §7.
OBSERVATION: One says `NOT STARTED` for both receivers; the other says `CONSTRUCTED` for both. Two separate records identify the first as stale and each states it was deliberately not modified.
IMPACT: The `main`-visible BC-02 chain state is self-contradictory.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-007 — Supersession is asserted by a record that declares it creates no authority**
SOURCE: AD-I-027 §2 vs §5, §13, §14.
OBSERVATION: The record simultaneously disclaims authority and performs a governance act (supersession, custodian decision, gate-state declaration).
IMPACT: Whether the supersession is effective, and therefore what the current BC-02 state is, rests on an unestablished authority claim.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-008 — The corpus has no vocabulary for supersession**
SOURCE: AD-I-045 §3.2 — the normalized set contains no token for it; §7 of this record.
OBSERVATION: At least six superseded-in-fact dispositions are carried unmarked. Zero supersessions were established by this audit.
IMPACT: State must be reconstructed by chronology, which §9 and §10 of this audit's mandate forbid as a resolution method.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-009 — Three records declare a Terrain Survey closed; no Terrain Survey artifact exists**
SOURCE: AD-I-045 §8, AD-I-047, AD-I-048 §3; §2.7.
OBSERVATION: The token *Terrain Survey* occurs in exactly four files across 56 spec refs, all of which describe its closure or scope. No survey document, scope statement or evidence log bearing that name exists.
IMPACT: The closure has no artifact to be closed against; the closure statements are the only record of the thing closed.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-010 — `PRE-01` carries opposite dispositions in two branch-local records**
SOURCE: AD-I-037 (`OPEN — OUTCOME B`) vs AD-I-039 (`PASS`).
OBSERVATION: Neither is reachable from `main`; they sit on different branches; the `PASS` is scoped in its own body to the schema layer but appears unqualified in gate blocks.
IMPACT: This is the status-token history §10 of the mandate names; **SUPERSESSION: NOT ESTABLISHED** in either direction.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-011 — Byte identity of the P-01 artifact is verifiable; issuance is not**
SOURCE: §1.4; AD-I-032; §2.7.
OBSERVATION: This audit independently recomputed 15 octets and SHA-256 `ecf9e98e…d4e65667`, matching every record. No Registry entry, issuance record or issuer identity exists anywhere in 56 + 79 refs.
IMPACT: The artifact is verifiable as data and unverifiable as an *issued fixture*. **A recomputed digest is not evidence of issuance, and this audit does not treat it as such.**
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-012 — One contract carries two incompatible readings of one field**
SOURCE: AD-I-035 §5.3 (*"computed once by the issuer at seal time"*) vs §7.1 (*"RECOMPUTED BY THIS RECEIVER"*).
OBSERVATION: Recorded independently by AD-I-041, AD-I-045, AD-I-047 and AD-I-048; AD-I-047's determination is `INCOHERENT — CUSTODIAN DECISION REQUIRED`.
IMPACT: `B-VAL-014`'s discriminating power and `BNC-1`'s detectability both turn on it.
STATUS: **RECORDED — NOT RESOLVED. No reading is selected.**

**AD-N-013 — The schema required for B-VAL-014 is implemented by no receiver**
SOURCE: AD-I-038 (branch-local v2) vs AD-I-033 / AD-I-057 (both `SCHEMA_VERSION = 1`).
OBSERVATION: v2 represents both operands; v1 carries one digest field; both deployed receivers emit v1; the two executed receipts are v1.
IMPACT: `B-VAL-014` has no evidence representation in any deployed implementation.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-014 — Every APS document and the Constitution exist in two languages under one identifier**
SOURCE: AD-I-001…003, AD-I-011…019; `STYLE_GUIDE.md` §12.
OBSERVATION: Root-level `.txt`/`.pdf` copies in Polish carry the same Document IDs and declared versions as the English `aps/` and `constitution/` documents, with materially different lengths (APS-200: 2 909 vs 11 445 octets) and, for the Constitution, a **different freeze condition**. Neither set is marked superseded, non-normative, or a translation.
IMPACT: Which text constitutes the specification is undetermined for the whole of precedence tiers 1–3.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-015 — `ADR-001` denotes three documents with three statuses**
SOURCE: AD-I-007, AD-I-008, AD-I-009.
OBSERVATION: `PROPOSED` / `ACCEPTED` / `DRAFT`; two of the three share a title and subject; one is a different subject entirely.
IMPACT: Any citation of `ADR-001` — including the claim that assigns SPEC approval to the Protocol Custodian — is ambiguous.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-016 — Tier-2 precedence is occupied entirely by DRAFT documents, one of which asserts in-force normativity**
SOURCE: AD-I-010…017, AD-I-021.
OBSERVATION: Every APS document is `DRAFT` while declaring `Classification: Normative Specification`; CONF-003 declares itself *"a normative conformance requirement"* under a `DRAFT` header.
IMPACT: The authority tier that the `CLAUDE.md` ladder places above all engineering records consists of documents whose own status disclaims force.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-017 — The document that orders the authority tiers sits inside the tiers it orders**
SOURCE: AD-I-049; AD-I-053 `OQ-A-CONFLICT-003`.
OBSERVATION: `CLAUDE.md` occupies tier 6 of its own ten-tier ladder and establishes the ordering of tiers 1–5.
IMPACT: The precedence rule governing this audit is of unestablished authority. **Recorded, not resolved, and not relied on to settle anything.**
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-018 — Two incompatible fixed-point representations are declared immutable in one article**
SOURCE: AD-I-051 Art. I §1; AD-I-056.
OBSERVATION: `Q16.16` and `Scaling factor: 100,000 (10^5)` are listed together as constitutional constants with no stated relationship; the implementation uses the decimal scale and **no Q16.16 implementation was located**.
IMPACT: Gates `ARI-D-007`, `ARI-D-008`, `ARI-D-014`.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-019 — ARI is defined in the specification corpus only by deferral to an implementation**
SOURCE: AD-I-022 (`glossary/GLOSSARY.md:27-28`) — the only ARI occurrence in the entire specification corpus.
OBSERVATION: The specification defines ARI as *"computed by RI-PY"*; the implementation corpus fixes its constants as constitutional; no authority grant in either corpus names ARI.
IMPACT: This is the substrate of C-1 and C-2, and of all 27 `ARI-D-*` decisions.
STATUS: **RECORDED — NOT RESOLVED. C-1 and C-2 are untouched.**

**AD-N-020 — A protocol-scope adoption is stated from the implementation corpus**
SOURCE: AD-I-062 §1.
OBSERVATION: *"Aura adopts RI-RS as the canonical hash-domain model for CK-003"*, under `Status: CONDITIONALLY CLOSED / CI-BLOCKED`, in a repository whose authority to make protocol-scope adoptions is exactly what C-2 asks about.
IMPACT: Direct evidence for C-2; a precedent act of unestablished authority.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-021 — Identifier namespaces collide across records**
SOURCE: `N-01…N-17` (AD-I-048) vs `N-01…N-08` (AD-I-045); `D-1…D-10` vs `DIV-01…DIV-07`; `PRE-01`, `PRE-01-G1…G7`, `PRE-01-001…010`; `C-1/C-2` (governance conditions) vs `C-13/C-14` (ARI candidates) vs `C1–C8` (conformance cases); `A-1…A-8` in AD-I-045 vs `A-1…A-5` in AD-I-048 denoting different questions.
OBSERVATION: A reader encountering `N-11`, `C-14` or `A-2` cannot determine the namespace from the token. This audit avoided adding to the collision by prefixing every identifier it mints with `AD-` (§1.5).
IMPACT: Cross-record citation is unsafe without the source document named alongside every identifier.
STATUS: **RECORDED — NOT RESOLVED. No identifier in any existing record is renumbered.**

**AD-N-022 — A stop report's declared absences are contradicted by present files**
SOURCE: AD-I-059 vs AD-I-060.
OBSERVATION: Two of four files declared *"deliberately absent"* are present on the same branch as the record declaring them absent, added later by different work. No supersession marker.
IMPACT: Same class as AD-N-008, in a third repository.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-023 — A regulatory release closure predates the entire open-conflict record set**
SOURCE: AD-I-058 (2026-07-24) vs AD-I-053, AD-I-054, AD-I-063 (2026-08).
OBSERVATION: The closure declares the repository *"internally consistent… constitutionally compliant"*; later records register 13 unresolved authority conflicts, 27 unanswered ARI decisions, and `Reconciled: 0 of 5`. No supersession marker on the closure.
IMPACT: **HISTORICAL FACT ≠ CURRENT AUTHORITY.** Recorded as an evolution fact, not a current state.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-024 — Organization-level governance describes an unobserved repository topology**
SOURCE: AD-I-065; AD-I-064.
OBSERVATION: `.github/GUIDELINES.md` names `aura-protocol`, `aura-devos`, `aura-brand`; reference descriptors point at `github.com/AuraIDToken/…` while the observed organization is `Aura-IDToken`.
IMPACT: Organization-level governance and reference descriptors do not resolve against the observed corpus.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-025 — Contract headers not updated after the events they describe**
SOURCE: AD-I-057 header (`P-01: NOT EXECUTED`) vs AD-I-026 / AD-I-031.
OBSERVATION: The BC-02.2 contract on core `main` still declares P-01 not executed although a P-01 handoff through RI-PY is recorded with a receipt.
IMPACT: Contract faces and evidence disagree on `main` in two repositories simultaneously.
STATUS: **RECORDED — NOT RESOLVED**

**AD-N-026 — Absence claims in this audit are bounded and the bound is declared**
SOURCE: §1.2, AD-OS-017.
OBSERVATION: `aura-specification` (56 refs) and `aura-poc-a-core-v3.3` (79 refs) were searched exhaustively; `aura-guard-v1.3`, `.github` and `cargo` were searched only on their checked-out branches.
IMPACT: Any statement in this record that something is absent from the guard, org or cargo repositories is **branch-scoped, not corpus-scoped**.
STATUS: **RECORDED — NOT RESOLVED** (declared limitation, not a defect of the corpus)

**Total normalization findings: 26.**

---

## 16. NO-REPAIR REGISTER

Every item below was discovered and left exactly as found.

| Item | Class | NORMALIZATION ACTION REQUIRED | ACTION PERFORMED |
|---|---|---|---|
| Duplicate Constitution and APS documents in two languages | duplicate documents | YES | **NO** |
| Three `ADR-001` documents | duplicate / colliding identifiers | YES | **NO** |
| Two Decision Packages A/B with transposed partitions | competing representations | YES | **NO** |
| Root-level `_260723_HHMMSS` filename pattern vs `aps/APS-nnn_*.md` | inconsistent filenames | YES | **NO** |
| `BC-02.1-…` vs `BC-02-…` prefixes on sibling boundary records | inconsistent filenames | YES | **NO** |
| `AD-I-023` §18 vs `AD-I-024` §7 gate snapshots | conflicting status tokens | YES | **NO** |
| `PRE-01 OPEN` vs `PRE-01 PASS` | conflicting status tokens | YES | **NO** |
| 14 branch-local load-bearing artifacts | branch-local authority | YES | **NO** — nothing merged, no PR opened |
| `AD-I-058` release closure, `AD-I-059` stop report | obsolete-looking records | YES | **NO** |
| `AD-I-027` disclaiming authority while performing supersession | contradictory declarations | YES | **NO** |
| 35 status tokens across the corpus | ambiguous vocabulary | YES | **NO** |
| `N-nn`, `D-n`, `C-n`, `A-n`, `B-n`, `PRE-01-*` namespace collisions | ambiguous vocabulary | YES | **NO** — no identifier renumbered |
| Missing Registry, issuance record, BC-01, Boundary Spec v1, Core Interface Spec v1, Terrain Survey artifact | missing references | YES | **NO** — nothing created |
| `AD-I-027` §15 citing a branch-local record from `main` | broken reference | YES | **NO** |
| `AD-I-064` organization-name divergence; `AD-I-065` repository topology | broken references | YES | **NO** |
| `A-OBS-01` trailing newline; `A-OBS-02` over-constrained `R-VAL-002` | contradictory declarations | YES | **NO** — both remain DEFERRED as the corpus recorded them |
| `AD-I-057` header stating `P-01: NOT EXECUTED` after execution | contradictory declarations | YES | **NO** |
| `AD-I-059` declaring present files absent | contradictory declarations | YES | **NO** |

---

## 17. HISTORICAL FACT VS CURRENT AUTHORITY

Recorded separately, per §17 of the mandate. Nothing below is treated as
current authority, and no historical intent is converted into a normative
statement.

| Artifact | HISTORICAL FACT | CURRENT AUTHORITY |
|---|---|---|
| AD-I-058 Release Closure Report (2026-07-24) | A regulatory release assessment was produced and recorded a passing state at that date | **NOT ESTABLISHED** — no supersession, and later records register 13 + 27 + 5 open items |
| AD-I-025 Cross-receiver pre-execution audit | Recorded `BLOCKED` at `5f226e6`; that was its correct disposition then | **NOT ESTABLISHED** as current — AD-I-027 asserts supersession; the assertion's authority is unestablished |
| AD-I-029 RI-PY evidence gap record | Recorded `BLOCKED` at 20:18 on 2026-08-23 | **NOT ESTABLISHED** as current — an RI-PY receipt exists from 21:36 |
| AD-I-023 §18 gate snapshot | Accurate when written at BC-02.1 construction time | **NOT ESTABLISHED** as current — two records call it stale; neither edited it |
| AD-I-059 D3 stop report | A stop occurred and four artifacts were withheld at that point | **NOT ESTABLISHED** as current — two of the four are present on `main` |
| AD-I-006 v0.1.0 document status | A status snapshot was taken on 2026-07-23 | **NOT ESTABLISHED** as current — document headers have since moved |
| AD-I-056 `core/evaluator.py` | An ARI implementation exists with specific constants | **NOT SPECIFICATION.** Old implementation ≠ current specification; no source establishes that relationship |
| AD-I-062 DQ-002 verdict | An adoption was stated in the guard repository | **NOT ESTABLISHED** — authority to state it is exactly C-2 |

---

## 18. WHAT THIS AUDIT DID NOT DO

Stated explicitly and exhaustively:

- Did not resolve **C-1** or **C-2**.
- Did not select **Decision A** or **Decision B**, under either package's partition.
- Did not select **A-I**, **A-II**, **A-III**, **B-I**, **B-II** or **B-III**.
- Did not resolve any **ARI-D-*** decision, and did not define ARI semantics.
- Did not determine fixture authority, `input_segment_sha256` semantics, or issuer-sealed vs receiver-recomputed semantics.
- Did not infer normative semantics from implementation, fixtures, tests, RI-PY or RI-RS.
- Did not infer authority from filenames, branch position, commit chronology, comments or historical intent.
- Did not modify **BC-02**, **BC-02.1** (v1 or v2), **BC-02.2**, **BC-02.3**, **APS-100/200/300/400/500/950**, **CONF-003**, **P-01**, any receiver, any adapter, any receipt, or any existing record.
- Did not create a Registry, an issuance artifact or a fixture.
- Did not execute **B-VAL-012**, **B-VAL-014**, **BNC-1…BNC-7**, **CONF-003 §4.5**, **N-01…N-08** or any conformance procedure.
- Did not invoke any receiver implementation.
- Did not produce a conformance result.
- Did not create or modify implementation code.
- Did not rename, rewrite, renumber, merge or move any artifact under audit.
- Did not open a pull request, merge anything, or modify `main` in any repository.

---

NORMALIZATION STATUS:
AUDIT COMPLETE

NORMATIVE CHANGES:
NONE

AUTHORITY DECISIONS:
NONE

ARI DECISIONS:
NONE

C-1:
UNCHANGED — OPEN

C-2:
UNCHANGED — OPEN

DECISION A:
UNCHANGED — OPEN

DECISION B:
UNCHANGED — OPEN

IMPLEMENTATION CHANGES:
NONE

SPECIFICATION CHANGES:
NONE

EVIDENCE EXECUTION:
NONE

CONFORMANCE EXECUTION:
NONE

B-VAL-014:
NOT EXECUTED

§4.5:
NOT EXECUTED

BNC-1:
NOT EXECUTED

REGISTRY:
NOT CREATED / NOT MODIFIED

ISSUANCE:
NOT CREATED / NOT MODIFIED

P-01:
NOT MODIFIED

MAIN:
UNTOUCHED

NEXT GATE:
CUSTODIAN REVIEW OF NORMALIZATION FINDINGS

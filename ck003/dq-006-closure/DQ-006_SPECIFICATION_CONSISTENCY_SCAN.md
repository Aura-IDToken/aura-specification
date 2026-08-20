# DQ-006 — Specification Consistency Scan

**Classification:** TRACEABILITY — non-normative
**Scan date:** 2026-08-20
**Scope:** `Aura-IDToken/aura-specification`, all `*.md`, `*.json`, `*.yaml`
**Closure record:** [`closures/DQ-006_CLOSURE_PACKAGE.md`](../../closures/DQ-006_CLOSURE_PACKAGE.md)

Terms scanned: `JCS`, `RFC 8785`, `canonical`, `canonicalization`, `serialization`, `serialize`,
`SHA-256`, `SHA256`, `Merkle`, `RFC 6962`, `leaf`, `0x00`, `hash domain`, `canonical bytes`,
`protocol_version`, `schema_version`, `event_type`, `DQ-002`, `DQ-003`, `DQ-004`, `DQ-006`,
`CK003`, `CONF-003`, `APS-200`, `APS-300`.

## Classification key

| Code | Meaning |
|---|---|
| **A** | Normative and consistent |
| **B** | Informative and consistent |
| **C** | Obsolete / legacy — historically accurate at its date, superseded by current normative text |
| **D** | Contradictory — irreconcilable with current normative text |
| **E** | Ambiguous |
| **F** | Unresolved — routed to a human authority |

## Reconciliation table

| # | Location | Topic | Status | Action |
|---|---|---|---|---|
| 1 | `aps/APS-200_CANONICAL_DATA_MODEL.md` §8.1–§8.9 | Canonical serialization profile | **A** | **Amended.** Was a `TODO` stub; now binds RFC 8785 JCS, UTF-8 `canonical_bytes`, prohibited digest inputs, hash/Merkle byte domain, cross-implementation byte identity, scope boundary, migration. Declared the single normative authority. |
| 2 | `aps/APS-200_CANONICAL_DATA_MODEL.md` §4 `integrity_hash` | Digest input | **A** | **Amended.** Bound to `SHA-256(canonical_bytes)` per §8, with the self-reference exclusion made explicit and aligned to APS-300 §5. |
| 3 | `aps/APS-300_EVIDENCE_MODEL.md` §5.1–§5.3 | `evidence_hash` byte domain | **A** | **Amended.** Was a `TODO`; now binds every §5 hash field to APS-200 §8 canonical bytes, separates `canonical_bytes` / `evidence_hash` / leaf / node, and states migration. |
| 4 | `aps/APS-300_EVIDENCE_MODEL.md` §8 | Evidence chain algorithm | **D → A** | **Amended.** Previously *"does not mandate a specific cryptographic algorithm"*, which contradicted the new §5.1 binding of `previous_evidence_hash`. Now defers to §5.1. |
| 5 | `specification/APS-001_PROTOCOL_SPECIFICATION.md` §7.1 | Hash-domain model; *"serialization profile … is owned by APS-200"* | **A** | **Unchanged.** This line is the architecture's own authority resolution and confirms APS-200 §8 as the profile owner. APS-200 §8.5 now attributes the domain model back to APS-001 §7.1. |
| 6 | `specification/APS-001_PROTOCOL_SPECIFICATION.md` Appendix A items 1–2 | Open closure dependencies | **C → A** | **Amended.** Both items were half-stale. Split into the now-closed part (serialization profile; cryptographic binding) and the still-open part (machine-readable schemas; Evidence Pack schema). |
| 7 | `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | Conformance requirement | **E → A** | **Rewritten.** Previously *"serialize twice, compare bytes"*, which a single implementation could satisfy alone. Now requires independently produced RI-PY/RI-RS artifacts, gate-side recomputation of digest and leaf, negative controls, a profile-discrimination requirement, and evidence provenance. Classified Normative Conformance Requirement. Verdict recorded as PARTIAL. |
| 8 | `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-*.md` | Decision record | **E → A** | **Reconciled.** Status `PROPOSED` → `ACCEPTED`; added the NORMATIVE CONTRACT vs CONFORMANCE IMPLEMENTATION DETAIL table; added executed evidence; added the known-limitation section; closure gate re-stated against actual state. |
| 9 | `ck003/dq-006-canonical-serialization/APS-200-SECTION-8-PROPOSED.md` | Competing §8 text | **C** | **Superseded banner.** Content incorporated into APS-200 §8; retained as history, barred from normative citation. |
| 10 | `ck003/dq-006-canonical-serialization/APS-300-RECONCILIATION.md` | Competing APS-300 text; *"reconciliation: OPEN"* | **C** | **Superseded banner.** Content incorporated into APS-300 §5. |
| 11 | `ck003/dq-006-canonical-serialization/CANONICAL_SERIALIZATION_CLOSURE_STATE.md` | *"CANONICAL SERIALIZATION: OPEN"* | **C** | **Superseded banner.** Blockers resolved or reclassified; residuals now tracked in the closure package §13. |
| 12 | `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md` | *"DQ-006: BLOCKED"* | **D → A** | **Amended.** Verdict block replaced with executed status. Oracle values unchanged and re-verified. JCS-degeneracy limitation added. |
| 13 | `closures/DQ-006_CLOSURE_PACKAGE.md` | Closure record | **A** | **Rewritten** as the single authoritative DQ-006 record: 13 required sections, deviations D-1…D-7, closure criteria 1–16, residuals R1–R4, verdict OPEN. |
| 14 | `evidence/DQ-006_CLOSURE_PACKAGE.md` | Duplicate closure record, `CLOSED — PASS` | **D → C** | **Superseded banner.** |
| 15 | `ck003/DQ-006_CLOSURE.md` | Duplicate closure record, `CLOSED — PASS` | **D → C** | **Superseded banner.** |
| 16 | `ck003/dq-006-closure/DQ-006-CLOSURE.md` | Duplicate closure record, `PASS / CLOSED` | **D → C** | **Superseded banner.** |
| 17 | `ck003/dq-006-closure/README.md` | Duplicate closure summary | **D → C** | **Superseded banner.** |
| 18 | `ck003/DQ-006_EVIDENCE_INDEX.md` | Evidence index, `DQ-006 = CLOSED / PASS` | **C** | **Retained, subordinated.** Its artifact digests and paths are correct and were re-verified; its status line is superseded by the closure package. |
| 19 | `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | `implementation_status: PENDING_EXECUTION` | **D → A** | **Amended.** Status corrected to `EXECUTED_PASS` with artifact digests, commits and reachability flags; `profile_discrimination.jcs_discriminating: false` recorded. **No digest or canonical byte value was changed.** |
| 20 | `ck003/README.md` | `DQ-006 status: CLOSED` | **D → A** | **Amended** to `OPEN`, with authority pointers. |
| 21 | `ck003/gates/GATE_A_APS001_CLOSURE_MATRIX.md` | *"APS-200 §8 explicitly TODO — OPEN / BLOCKER"* | **C → A** | **Amended.** Canonical-serialization, APS-300-binding and RI-equality rows reconciled. |
| 22 | `ck003/APS001_INV_MATRIX/INV-001_015_CONFORMANCE_MATRIX.md` INV-003 | *"BLOCKED — APS-200 serialization still open"* | **C → A** | **Amended** to PARTIAL with the discrimination residual named. INV-011 row byte-domain note added. |
| 23 | `compliance/TRACEABILITY_MATRIX.md` INV-003 row | `FIX-001 (TODO)` / `NOT VERIFIED` | **C → A** | **Amended** to `APS-200 §4, §8` / `CANONICAL-001` / `PARTIAL`. |
| 24 | `invariants/INVARIANT_REGISTRY.md` INV-003 | *"Related APS: APS-200 §8"* | **A** | **Unchanged** — already correct and now resolvable to concrete normative text. |
| 25 | `aps/APS-100_PROTOCOL_INVARIANTS.md` INV-003 | *"unambiguous serialization representation"* | **A** | **Unchanged** — consistent with APS-200 §8. |
| 26 | `aps/APS-400_CONFORMANCE_TEST_MATRIX.md` §4 CONF-003 row | Status `DRAFT` | **B** | **Unchanged** — CONF-003 remains DRAFT; status transitions are a Chief Architect act. |
| 27 | `aps/EVENT_TYPE_REGISTRY.md` §7 | *"participates in canonical object serialization exactly as defined by APS-200's approved serialization profile"* | **A** | **Unchanged** — correctly defers to APS-200 §8; now resolvable. No DQ-004 regression. |
| 28 | `aps/EVENT_TYPE_REGISTRY.md` §3, §5 vs. CANONICAL-001 `event_type` | Empty registry rejects `AUDIT_RECORD` | **F** | **Reported, not repaired** — CFL-005. DQ-004 governs; canonicalization determines representation only (APS-200 §8.7). |
| 29 | `ck003/DQ-004_EVENT_TYPE_SEMANTICS.md` §3 | Canonical token in the digest domain | **A** | **Unchanged** — consistent with APS-200 §8.7. |
| 30 | `ck003/decisions/DQ-003/current_versioning_snapshot.md` | `protocol_version` / `schema_version` distinction | **A** | **Unchanged** — no DQ-003 regression; APS-200 §8.7 explicitly excludes version semantics from the canonicalization profile. |
| 31 | `aps/APS-200_CANONICAL_DATA_MODEL.md` §4 | Both version fields required, distinct | **A** | **Unchanged** — neither renamed, merged nor redefined. |
| 32 | `closures/DQ-002_FINAL_CLOSURE.md` | `DQ-002 = CLOSED / PASS`, premised on DQ-006 PASS | **F** | **Not modified** (change-control §15). Its evidentiary basis inherits deviation D-1; routed to the Protocol Custodian via the closure package §14. |
| 33 | `closures/DQ-002_FINAL_CLOSURE.md` §4 | *"JCS-B01…B06: PASS"* | **E** | **Reported.** The executed RI-PY suite is `test_jcs_behavior.py`, 13 passed. Label drift, not a substantive contradiction. |
| 34 | `ck003/dq-002-hash-domain/` — `README.md`, `ADR-CK003-DQ002-HASH-DOMAIN.md`, `02_hash_domain_adr.md`, `HASH_DOMAIN_EVIDENCE.md` | *"APS-200 §8 leaves canonical serialization as TODO"* | **C** | **Not modified.** Dated evidence/decision artifacts, accurate at their date, now historical. Change-control §15 bars editing DQ-002 material; status recorded here. |
| 35 | `ck003/evidence/CORE_EVIDENCE_CONSOLIDATION_INDEX.md` item 7 | Same stale TODO claim | **C** | **Not modified** — dated working index; status recorded here. |
| 36 | `docs/completion/01_CURRENT_STATE_MATRIX.md` APS-200 row | *"canonical serialization"* listed as missing | **C** | **Not modified** — dated working matrix; status recorded here. |
| 37 | `ck003/handover-assessment/` (10 files) | Independent assessment, conflict register, evidence gaps | **B** | **Unchanged and load-bearing.** EG-01 (JCS-degeneracy) and CFL-001…CFL-005 are carried forward into the closure package §10 and §14. Explicitly marked non-normative at source. |
| 38 | `ck003/handover-assessment/04_CONFLICT_REGISTER.md` CFL-001 | Cross-corpus authority conflict | **F** | **Reported, not resolved.** Binding APS-200 §8 settles the question inside the specification corpus only. Routed to the Protocol Custodian. |
| 39 | `ck003/handover-assessment/04_CONFLICT_REGISTER.md` CFL-003 | Three incompatible RI-RS gate implementations | **F** | **Reported, not resolved** — residual R3. |
| 40 | `aps/APS-500_REFERENCE_FIXTURES.md` §5 | *"pending APS-200 finalization"* | **E** | **Not modified.** APS-200 entity schemas (§9) remain TODO, so the statement is still partly true. Out of DQ-006 scope. |
| 41 | `aps/APS-300_EVIDENCE_MODEL.md` §6, §13 | Evidence Pack container, EPR profiles still `TODO` | **B** | **Unchanged** — out of DQ-006 scope; recorded in APS-001 Appendix A item 2. |
| 42 | `conformance/README.md` index | Lists CONF-001…CONF-010 only | **E** | **Reported, not repaired.** CONF-011…CONF-015 exist as files but are absent from the index. Pre-existing, unrelated to DQ-006. |
| 43 | `evidence/README.md` | Links `EVIDENCE_TYPES.md`, which does not exist | **E** | **Reported, not repaired.** Pre-existing broken link, unrelated to DQ-006. |
| 44 | `ck003/APS001_INV_MATRIX/INV-001_015_CONFORMANCE_MATRIX.md` | Stray `fileciteturn…` markers in *Source-grounded observations* | **E** | **Reported, not repaired.** Cosmetic artifact, unrelated to DQ-006. |

## Totals

| Class | Count |
|---|---|
| A — normative and consistent (after this reconciliation) | 17 |
| B — informative and consistent | 5 |
| C — obsolete / legacy, status documented | 11 |
| D — contradictory *remaining after reconciliation* | **0** |
| E — ambiguous | 6 |
| F — unresolved, routed to a human authority | 5 |
| **Total entries** | **44** |

Nine entries were classified **D** before this reconciliation (rows 4, 12, 14, 15, 16, 17, 19, 20, plus the CONF-003 weakness at row 7). All nine were resolved. No contradictory statement about canonical serialization or the hash domain remains in the specification corpus.

## Authority check (Phase I)

There is now exactly one normative authority per question, and the architecture resolves it without arbitration:

| Question | Sole authority | Confirmed by |
|---|---|---|
| Canonical serialization profile and `canonical_bytes` | **APS-200 §8** | APS-001 §7.1: *"The serialization profile producing `canonical bytes` is owned by APS-200."* |
| Hash and Merkle domain model | **APS-001 §7.1** | APS-001 §10 authority chain; APS-200 §8.5 attributes it back |
| Evidence-hash byte domain | **APS-300 §5.1** | APS-200 §8.5 defers to it |
| DQ-006 decision | **ADR-CK003-DQ006** | closure package §3 |
| DQ-006 conformance requirement | **CONF-003** | APS-400 §4 |
| DQ-006 closure status | **`closures/DQ-006_CLOSURE_PACKAGE.md`** | supersede banners on the four prior records |

**No NORMATIVE AUTHORITY CONFLICT remains inside the specification corpus.**

One authority conflict remains **outside** it: CFL-001, between the specification corpus and the implementation corpus, with no cross-corpus precedence rule in either. That is a governance act reserved to the Protocol Custodian and is not resolved here.

## Regression checks

| Check | Result |
|---|---|
| DQ-003 — `protocol_version` / `schema_version` remain distinct, unrenamed, unmerged | **PASS** — APS-200 §8.7 explicitly excludes version semantics from the profile |
| DQ-004 — `event_type` governed by the registry, not by canonicalization | **PASS** — APS-200 §8.7 explicitly excludes event semantics; registry §7 defers to APS-200 |
| DQ-002 — hash-domain semantics unchanged | **PASS** — no DQ-002 artifact modified; APS-200 §8.5 binds the input byte domain only |
| Canonical bytes, SHA-256, RFC 6962 leaf values | **UNCHANGED** — verified by recomputation |

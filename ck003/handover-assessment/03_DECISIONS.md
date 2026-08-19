# C / D — Open and Closed Decisions

**Classification:** EVIDENCE — NON-NORMATIVE

---

## C.1 The distinction that governs this section

The core repository's D-3/D-4 record states a distinction that must be carried verbatim
wherever these closures are cited:

> **CLOSED — DECISION DOMAIN** is **not** equivalent to
> **CLOSED — SEMANTIC VALUE ESTABLISHED.**

Most of what this program calls "closed" is the first kind. Almost none of it is the second.

## C.2 Specification-corpus decisions (`DQ-nnn`)

| ID | Subject | Recorded status | Assessment |
|---|---|---|---|
| **DQ-002** | Merkle hash domain | `ADR-…-DQ002`: **PROPOSED — awaiting Chief Architect approval**; `02_hash_domain_adr.md` §9: *"DECISION RECORDED / IMPLEMENTATION OPEN / CONFORMANCE NOT YET PROVEN"*; `HASH_DOMAIN_EVIDENCE.md`: **DQ-002: OPEN** | **OPEN.** Two ADRs exist for one decision. `03_cross_language_fixture.json` self-declares `NORMATIVE_TEST_VECTOR` while the ADR governing it is only PROPOSED. |
| **DQ-003** | Version semantics | `current_versioning_snapshot.md`: **Status: OPEN**. No ADR, no closure package. | **OPEN.** The `protocol_version` / `schema_version` distinction is stated in APS-001 §12 and APS-200 §4, but the compatibility matrix and version-binding fixtures do not exist. In the implementation, `protocol_version` does not appear in code at all. |
| **DQ-004** | Event-type semantics | `DQ-004_EVENT_TYPE_SEMANTICS.md` header: **PROPOSED CLOSURE**; its own §9: *"the correct closure state is therefore **BLOCKED FOR FINAL CLOSURE**, not PASS"* | **BLOCKED.** The approved vocabulary is the empty set. The document is internally honest; its header and its verdict disagree, and the verdict is the correct one. |
| **DQ-006** | Canonical serialization / cross-language equality | **Three live statuses.** See CFL-002. | **CONFLICT.** |
| DQ-001, DQ-005, DQ-007+ | — | Referenced nowhere in the repository | **EVIDENCE GAP.** Non-contiguous numbering means completeness of the DQ set cannot be established. |

## C.3 Implementation-corpus decisions (`D-n`, P0-6)

Source: `aura-poc-a-core-v3.3/review/2026-08-14_P0_6_D3_D4_DECISION_RECORD/D3_D4_DECISION_RECORD.md`

| ID | Subject | Status |
|---|---|---|
| D-1 | Violations belong to the integrity domain | CLOSED |
| D-2 | Integrity-domain contract | CLOSED |
| **D-3** | **Canonical representation** | **CLOSED — DECISION DOMAIN**; concrete semantic value **NOT ESTABLISHED** |
| **D-4** | **Collection semantics** | **CLOSED — DECISION DOMAIN**; concrete semantic value **NOT ESTABLISHED** |
| D-5 | — | BLOCKED |
| D-6 | — | NOT ADVANCED |
| D-7 | Version / digest discriminator | NOT CLOSED / NOT ADVANCED; blocked by EG-1 |
| EG-1 | Evidence closure for D-7 | **NOT CLOSED / GOVERNANCE EVIDENCE GAP** (Outcome B) |

The D-3/D-4 record's §5 lists explicit non-decisions. Quoted, because it is directly
load-bearing for DQ-006:

> This record does **not** establish, select, imply or authorise any of the following:
> canonical byte encoding · serialization format · ordering rule · set/multiset/ordered
> collection semantics · duplicate handling · float representation · `NaN`/±Infinity handling
> · hash-domain representation · version marker · replay semantics · migration semantics ·
> any concrete digest construction
>
> No such value has been derived, and none may be derived, from: implementation behaviour;
> the candidate lists in the preparation package; existing code comments;
> `mathematical_foundation.md`; RI-PY; ADR-0001; any previous Claude recommendation; or
> engineering judgement of any agent.
>
> **Any statement of a concrete D-3 or D-4 semantic value that cites this record as its
> authority is invalid.**

## C.4 ARI decisions (`ARI-D-nnn`)

`review/2026-08-12_RD1_ARI_DECISION_READINESS/01_ARI_DECISION_REGISTER.md`:
**27 decisions, 0 answered.** ARI-D-001 is the threshold question — whether ARI is normatively
defined by Aura at all, or remains implementation-defined and therefore outside the conformance
surface. Until it is answered, *"conformant ARI" has no referent*, and INV-001 / INV-006 —
both Critical — have no verifiable content, because the only definition of ARI in the
specification corpus (`glossary/GLOSSARY.md:27-28`) defines it *by reference to RI-PY*, i.e. by
reference to an implementation.

This is a larger hole than the canonical-serialization question and it is not on the handover's
trajectory at all.

## D.1 What is genuinely closed

| Item | Basis |
|---|---|
| AURA Constitution v1.0 | FROZEN — the only frozen artifact in the program |
| D-1, D-2 | Closed under the P0-6 process |
| D-3, D-4 *as decision domains* | Closed; semantic values explicitly not established |
| That RI-RS `src/merkle.rs` implements RFC-6962 leaf/node domains | Verified directly in source; observational fact, not a protocol decision |

## D.2 What is recorded as closed but is not

| Item | Recorded | Why it does not hold |
|---|---|---|
| DQ-006 | CLOSED — PASS | ADR PROPOSED; APS-200 §8 PROPOSED; two sibling artifacts say BLOCKED and PENDING_EXECUTION; cited evidence unmerged; no CI executed it. See CFL-002, CFL-004. |
| "RFC 8785 is frozen" (handover §21) | frozen | No approved artifact establishes it. The ADR that would is PROPOSED. The core corpus records the opposite for the same question. See CFL-001. |
| "CROSS-LANGUAGE-001 = PASS" (handover §13) | PASS | The execution is real and its artifacts exist — on unmerged branches. But the vector it uses cannot discriminate JCS from ordinary sorted JSON (see `10_`). It evidences *agreement*, not *conformance to RFC 8785*. |

---

*This document records state and confers no normative semantics. It closes nothing and reopens
nothing.*

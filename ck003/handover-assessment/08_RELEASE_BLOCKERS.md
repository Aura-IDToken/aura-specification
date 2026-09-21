# J — Release Blockers

**Classification:** EVIDENCE — NON-NORMATIVE
**Target:** `aura-specification` v1.0

Ordered by dependency, not by effort. Each blocker names the evidence that establishes it.

---

## RB-01 — No established authority can accept a cross-corpus protocol decision

**Verdict: DECISION REQUIRED** · Evidence: CFL-001, `02_NORMATIVE_GRAPH.md` §B.5

The two corpora are governance-disjoint; no cross-corpus precedence rule exists in either; the
Chief Architect is never identified; the SPEC document class has no approver; the ARB has no
roster; the RFC route has never been exercised; the Two-Key Gate has no repository-normative
basis. Recorded in the core repository's own OQ-A package: **13 conflicts, 0 reconciled; 15
evidence gaps, 0 fillable from repository material alone.**

Every remaining blocker requires a decision this program currently has no way to make. This is
the release blocker; the rest are downstream of it.

---

## RB-02 — The only closed gate is contested from three directions

**Verdict: CONFLICT** · Evidence: CFL-002, CFL-004, EG-01

DQ-006 is recorded CLOSED — PASS above a PROPOSED ADR, contradicted by two sibling artifacts in
the same repository, with all four cited evidence commits unreachable from any default branch.

---

## RB-03 — No canonical serialization profile is normatively established

**Verdict: BLOCKED** · Evidence: CFL-001, `03_DECISIONS.md` C.3

APS-200 §8 is PROPOSED. The D-3 record states the semantic value is NOT ESTABLISHED and may not
be derived from implementation behaviour. INV-003 is BLOCKED on exactly this. Until it is
resolved, the canonical fixture corpus cannot be built, RI-PY's three-way canonicalization
divergence cannot be repaired, and CONF-003 cannot be executed.

---

## RB-04 — The cross-language evidence does not discriminate the profile

**Verdict: EVIDENCE GAP** · Evidence: EG-02, `10_INDEPENDENT_VERIFICATION.md`

The single cross-language vector produces identical bytes under RFC 8785 and under ordinary
sorted JSON. Cross-language *agreement* is established; conformance to RFC 8785 is not.

---

## RB-05 — Zero of fifteen invariants have implementation evidence

**Verdict: BLOCKED** · Evidence: `01_CURRENT_STATE.md` A.3, EG-06

All fifteen are OPEN (INV-003 BLOCKED). The traceability matrix records `NOT VERIFIED` for both
implementations on every row. CONF-001…015 are all DRAFT. Assignment of a CONF identifier is not
conformance — a point the registry itself makes.

---

## RB-06 — The fixture corpus does not exist

**Verdict: BLOCKED** · Evidence: EG-03, EG-04, `06_…` G

`FIX-001` is all-`"TODO"`. `CK003-001…010` NOT RECOVERED. `FIX-DQ004-001…004` absent. Four of
five `FIX-INV-*` fixtures self-declare blocked or parametric. Five fixture category directories
referenced by APS-500 do not exist. There is no conformance runner in any repository.

---

## RB-07 — The event-type vocabulary is empty and rejects its own fixture

**Verdict: CONFLICT** · Evidence: CFL-005, EG-04

DQ-004 self-records as BLOCKED FOR FINAL CLOSURE. CONF-012 cannot pass. `AUDIT_RECORD` — the
`event_type` in the fixture under the closed gate — is unregistered and would be REJECTED under
the registry's own §3.

---

## RB-08 — The specification repository has no CI

**Verdict: BLOCKED** · Evidence: EG-05

`.github/workflows/` does not exist. No validation script exists. APS-001 §13 release-gate item
6 ("CI executes the conformance gate") is unmet, and cannot be met by prose.

---

## RB-09 — Required governance artifacts have never been produced

**Verdict: BLOCKED** · Evidence: EG-07

Zero RFCs, zero ARRs, no Custodian signature, no Architecture Review of APS-001, no
`CHECKSUMS.sha256` or `CONFORMANCE_REPORT.md` in `releases/v0.1.0/`. `ROADMAP.md` milestones 1–4
have **every checkbox unchecked**.

---

## RB-10 — ARI has no normative definition

**Verdict: DECISION REQUIRED** · Evidence: `03_DECISIONS.md` C.4

`ARI-D-001` — whether ARI is protocol content or implementation-defined — is unanswered, as are
the other 26 ARI decisions. The only definition in the specification corpus defines ARI *by
reference to RI-PY*. INV-001 and INV-006 are both Critical and both depend on it.

This blocker does not appear anywhere on the handover's trajectory. It should.

---

## Summary

| Verdict | Count |
|---|---|
| DECISION REQUIRED | 2 (RB-01, RB-10) |
| CONFLICT | 3 (RB-02, RB-07, and CFL-003 under RB-02) |
| BLOCKED | 5 |
| EVIDENCE GAP | 1 (RB-04) |

**Zero release blockers are closed.** `aura-specification` v1.0 is not reachable from the
current state by implementation work alone; RB-01 must be resolved by a human authority first.

---

*This document records blockers and clears none of them. It confers no normative semantics.*

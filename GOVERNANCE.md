# Governance

- **Document ID:** GOV-001
- **Version:** 1.0-FROZEN
- **Status:** FROZEN
- **Authority:** AURA Constitution v1.0 (FROZEN)

---

## 0. Approval Record

| Field | Value |
|---|---|
| Status | **FROZEN** |
| Key 1 — Objective Evidence | **PASS** |
| Key 2 — Normative Approval | **APPROVED** |
| Decision date | 2026-08-19 |
| Decision authority | Protocol Custodian / Chief Architect |

This record captures the approved status transition of GOV-001 from PENDING APPROVAL
to FROZEN. The substantive governance rules in §1–§11 are unchanged by this transition.

Per [VERSIONING.md](VERSIONING.md), a FROZEN document is immutable and never receives a
new version number; a revision creates a new document version.

---

## 1. Purpose

This document defines how the `aura-specification` repository is governed: who has authority over what, how decisions are made, and how the protocol evolves.

---

## 2. Authority Hierarchy

```
Chief Architect
        │
        ├── AURA Constitution (FROZEN — immutable)
        │
        ├── Architecture Review Board (ARB)
        │       └── conducts ARRs
        │
        ├── Specification Contributors
        │       └── author APS, ADRs, RFCs
        │
        └── AI Assistants
                └── may propose, implement, test; may NOT approve or freeze
```

The Chief Architect has final and sole approval authority over:
- AURA Constitution amendments
- APS document status transitions (APPROVED → FROZEN)
- Protocol Invariant additions or removals
- New reference implementation recognition

---

## 3. Governance Artifacts

| Artifact | Purpose | Owner |
|----------|---------|-------|
| ADR | Architecture Decision Record — documents a single architectural decision | Decision author |
| ARR | Architecture Review Record — records a formal review session | Chief Architect |
| RFC | Request for Comments — formal proposal for protocol change | Proposer |
| ADC | Architecture Decision Confidence — assessment of decision certainty | Chief Architect |
| ACI | Architecture Conformance Inspection — conformance assessment | Chief Architect |
| EPR | Evidence Pack Report — evidence of a conformant execution | Implementer |

Each artifact has an identifier, version, owner, and status per APS-000 §3.

---

## 4. Document Lifecycle

See [VERSIONING.md](VERSIONING.md) for the complete status lifecycle.

```
DRAFT → REVIEW → APPROVED → FROZEN
                           ↘ DEPRECATED → ARCHIVED
```

---

## 5. Change Process

### 5.1 Minor Changes (PATCH)

Typos, formatting, non-normative clarifications that do not change protocol behavior:
1. Open a pull request with description of change
2. Requires one reviewer approval
3. No RFC or ADR required
4. Chief Architect or delegate may merge

### 5.2 Major Changes (MINOR/MAJOR)

New requirements, new invariants, new conformance tests, behavioral changes:
1. Open an RFC in `/rfcs/`
2. RFC enters DRAFT status
3. Community comment period (minimum 14 days)
4. Architecture Review Board assessment
5. Chief Architect approval
6. RFC transitions to APPROVED
7. Implementation via pull request referencing RFC
8. ADR created if architectural decision is embedded

### 5.3 Constitution Amendments

Per AURA Constitution Article XI:
1. RFC submitted
2. Architecture Review conducted (ARR created)
3. Impact analysis documented
4. Dependent documents updated
5. Chief Architect approval
6. New FROZEN version published

---

## 6. ADR Process

Architecture Decision Records capture *why* a decision was made, not just what was decided.

1. Copy `templates/ADR_TEMPLATE.md`
2. Assign next sequential `ADR-NNN` identifier
3. Fill all required sections
4. Submit as pull request
5. Link to any related RFC
6. Merging the PR = accepting the ADR
7. ADR status set to ACCEPTED

See [adrs/README.md](adrs/README.md) and [templates/ADR_TEMPLATE.md](templates/ADR_TEMPLATE.md).

---

## 7. RFC Process

Requests for Comments are used for protocol changes that affect behavior.

1. Copy `templates/RFC_TEMPLATE.md`
2. Assign next sequential `RFC-NNN` identifier
3. Fill all required sections including affected invariants, evidence, and conformance tests
4. Submit as pull request — opens the comment period
5. Minimum 14-day comment period
6. Author updates RFC with responses to feedback
7. Architecture Review Board votes: ACCEPT / REJECT / DEFER
8. Chief Architect final approval
9. RFC transitions to ACCEPTED or REJECTED (both are permanently recorded)

See [rfcs/README.md](rfcs/README.md) and [templates/RFC_TEMPLATE.md](templates/RFC_TEMPLATE.md).

---

## 8. Review Meetings

Architecture Review meetings produce Architecture Review Records (ARRs):
- Held as needed, triggered by RFC acceptance or major milestone
- Chaired by Chief Architect
- ARR published to `/adrs/ARR-NNN_TITLE.md` within 5 days of meeting

---

## 9. AI Assistant Policy

Per AURA Constitution Article VIII:

AI assistants MAY:
- Analyze and propose
- Implement changes once an RFC/ADR is approved
- Prepare tests and documentation
- Flag specification gaps

AI assistants MUST NOT:
- Self-approve changes to canonical documents
- Freeze or deprecate documents
- Override the Chief Architect's decisions
- Introduce undocumented protocol behavior

---

## 10. Conflict Resolution

In case of ambiguity, the priority order is:
1. Mission of the project (open, deterministic, auditable trust layer)
2. AURA Constitution principles
3. Conformance with protocol
4. Determinism
5. Auditability

(AURA Constitution Article XII)

---

## 11. Amendment

This document may be amended via the Major Change process (§5.2) above.

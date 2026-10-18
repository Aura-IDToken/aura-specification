# RFC-001 — APS-001 Milestone 1 Execution Scope

Document ID: RFC-001  
Status: DRAFT  
Date: 2026-09-26  
Author: @vaidt  
Comment Period: 2026-09-26 – 2026-10-10  
Related ADR: —

---

## Summary

This RFC defines the first execution increment for Milestone 1 by formalizing APS-001 as the active root normative draft baseline and synchronizing dependent APS authority references and traceability links to explicit APS-001 sections.

---

## Motivation

Milestone 1 in `ROADMAP.md` identifies APS-001 as the critical blocker for normative coherence. Dependent APS documents already rely on APS-001 but use broad authority declarations and unresolved placeholder references in traceability artifacts. This RFC creates a controlled first increment with explicit section-level synchronization and documented acceptance criteria.

---

## Detailed Proposal

### Scope of Increment M1-I1

The repository MUST treat APS-001 `0.2-DRAFT` (`specification/APS-001_PROTOCOL_SPECIFICATION.md`) as the active root normative draft for synchronization.

The first increment MUST synchronize the following APS-001 sections:

- §2 Protocol Execution Model
- §5 Policy Model
- §8 Error Handling
- §9 Conformance Requirements
- §11 Traceability

### Authority Synchronization

The following documents MUST use explicit APS-001 section-level authority references in their metadata headers:

- APS-100
- APS-200
- APS-300
- APS-400
- APS-500
- APS-900
- APS-950

### Traceability Synchronization

Where `compliance/TRACEABILITY_MATRIX.md` references APS-001 section placeholders marked TODO for active invariant mappings, those references MUST be replaced with explicit section identifiers from the current APS-001 draft.

### Governance Boundary

This RFC MUST NOT be interpreted as approving APS-001. Architecture Review and Chief Architect approval remain required under governance rules before APS-001 status can be promoted beyond DRAFT.

### Acceptance Criteria

This increment is complete when all criteria are met:

1. `ROADMAP.md` records M1-I1 scope and status.
2. A formal RFC artifact exists for the increment.
3. APS-100..APS-950 authority metadata is synchronized to APS-001 sections.
4. Traceability matrix entries no longer use APS-001 TODO section placeholders for the synchronized mappings.
5. Changelog captures the increment changes.

---

## Affected APS Documents

| Document | Section | Change Type |
|----------|---------|-------------|
| [APS-001](../specification/APS-001_PROTOCOL_SPECIFICATION.md) | §2, §5, §8, §9, §11 (reference baseline) | Changed requirement linkage |
| [APS-100](../aps/APS-100_PROTOCOL_INVARIANTS.md) | Header authority metadata | Changed requirement linkage |
| [APS-200](../aps/APS-200_CANONICAL_DATA_MODEL.md) | Header authority metadata | Changed requirement linkage |
| [APS-300](../aps/APS-300_EVIDENCE_MODEL.md) | Header authority metadata | Changed requirement linkage |
| [APS-400](../aps/APS-400_CONFORMANCE_TEST_MATRIX.md) | Header authority metadata | Changed requirement linkage |
| [APS-500](../aps/APS-500_REFERENCE_FIXTURES.md) | Header authority metadata | Changed requirement linkage |
| [APS-900](../aps/APS-900_COMPLIANCE_MAPPING.md) | Header authority metadata | Changed requirement linkage |
| [APS-950](../aps/APS-950_REFERENCE_IMPLEMENTATION_REQUIREMENTS.md) | Header authority metadata | Changed requirement linkage |

---

## Affected Invariants

| Invariant | Impact |
|-----------|--------|
| [INV-001](../invariants/INVARIANT_REGISTRY.md#inv-001--deterministic-evaluation) | Unaffected (traceability section reference clarified) |
| [INV-002](../invariants/INVARIANT_REGISTRY.md#inv-002--bit-perfect-replay) | Unaffected (traceability section reference clarified) |
| [INV-006](../invariants/INVARIANT_REGISTRY.md#inv-006--platform-independence) | Unaffected (traceability section reference clarified) |
| [INV-007](../invariants/INVARIANT_REGISTRY.md#inv-007--zero-float-runtime) | Unaffected (traceability section reference clarified) |
| [INV-008](../invariants/INVARIANT_REGISTRY.md#inv-008--fail-closed) | Unaffected (traceability section reference clarified) |
| [INV-013](../invariants/INVARIANT_REGISTRY.md#inv-013--policy-determinism) | Unaffected (traceability section reference clarified) |

---

## Required Evidence Changes

No APS-300 schema/content change is introduced by this increment. Existing evidence requirements remain unchanged.

---

## Required Conformance Test Changes

No CONF-xxx content change is introduced by this increment. Existing conformance definitions remain unchanged.

---

## Required Fixture Changes

No FIX-xxx fixture content change is introduced by this increment.

---

## Implementation Impact

| Implementation | Impact |
|----------------|--------|
| RI-PY (aura-poc-a-core) | No behavioral change; authority and traceability references become clearer for future conformance mapping |
| RI-RS (aura-guard) | No behavioral change; authority and traceability references become clearer for future conformance mapping |

---

## Alternatives Considered

### Alternative 1 — Defer synchronization until APS-001 approval
Rejected because unresolved authority and TODO placeholders continue to block coherent traceability during ongoing draft work.

---

## Open Questions

1. Which ARR identifier will be assigned for APS-001 Milestone 1 review?
2. Should APS-001 header metadata be normalized to include `Last Review` in this milestone or in a dedicated formatting pass?

---

## Comment Period Feedback

Pending.

---

## Decision

**Status**: PENDING  
**Rationale**: Pending comment period and Architecture Review.  
**Decided by**: Chief Architect  
**Date**: YYYY-MM-DD

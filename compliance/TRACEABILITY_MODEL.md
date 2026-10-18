# Traceability Model

Document ID: COMP-TM-001  
Version: 1.0-DRAFT  
Authority: APS-900  
Last Review: 2026-07-23

---

## Purpose

This document describes the Aura Protocol Traceability Model — the mechanism by which every normative requirement is connected to evidence of its fulfillment.

---

## The Chain

```
AURA Constitution (Principle)
        │
        ▼
APS Requirement (section reference)
        │
        ▼
Protocol Invariant (INV-xxx)
        │
        ▼
Data Model Entity (ENT-xxx)
        │
        ▼
Evidence Requirement (EVID-xxx type)
        │
        ▼
Conformance Test (CONF-xxx)
        │
        ▼
Reference Fixture (FIX-xxx)
        │
        ▼
Implementation (RI-PY / RI-RS)
        │
        ▼
Release Artifact (REL-xxx)
```

---

## Traceability Rules

1. Every APS requirement MUST map to at least one Protocol Invariant.
2. Every Protocol Invariant MUST map to at least one Conformance Test (per INV-010).
3. Every Conformance Test MUST use at least one Reference Fixture.
4. Every Reference Fixture MUST specify Expected Output and Expected Evidence.
5. Every execution of a Reference Fixture MUST produce a verifiable Evidence Pack.
6. Every release MUST include a Conformance Report referencing all test results.

---

## Impact Analysis

When a document changes, the following MUST be assessed:

| Changed Document | Must Re-assess |
|-----------------|----------------|
| AURA Constitution | All APS documents |
| APS-001 | APS-100 through APS-950, all INV, CONF, FIX |
| APS-100 (Invariant change) | All CONF tests referencing that INV, all FIX using those CONF tests |
| APS-200 (Entity change) | CONF-003, CONF-008, CONF-009, all FIX involving changed entities |
| APS-300 (Evidence change) | CONF-004, CONF-005, CONF-009, CONF-010, all FIX-EVIDENCE |
| APS-400 (Test change) | All FIX using changed test, Conformance Reports |
| APS-500 (Fixture change) | New FIX-NNN required; old fixture deprecated |

---

## Gap Registry

Current known traceability gaps:

| Gap | Blocking | Priority |
|-----|----------|----------|
| APS-001 remains DRAFT and requires Architecture Review before approval | Yes — root normative authority remains open | Critical |
| CONF-011 through CONF-015 are assigned but not yet evidenced through an executable conformance gate | Yes — prevents objective PASS claims for INV-007 and INV-012…INV-015 | High |
| FIX-001 is now a concrete working draft fixture and supports a repository-local draft request/result/evidence/replay/platform gate for CONF-001/002/004/005/006/010, but it still lacks implementation-side controlled evidence and APS-500 promotion | Yes — blocks release-grade closure even though the draft request/result/evidence contract is now bound | High |
| APS-200 entity schemas now close the current working-profile ENT-002/ENT-003 payloads, but additional profile contracts, identity closure, and registry-bound semantics remain incomplete | Yes — still blocks CONF-003, CONF-008, CONF-009 from full objective closure | High |
| APS-300 Evidence Pack schema now closes the current draft `EPR-CORE` content contract, but additional profile vocabularies and attestation-lifecycle closure remain incomplete | Yes — still blocks CONF-004, CONF-005, CONF-009, CONF-010 from full objective closure | High |
| No Attestation (ENT-006) implementation | Yes — blocks CONF-005, CONF-009 | High |
| No repository-native CI conformance gate | Yes — blocks release-ready automated verification | High |

See [../ROADMAP.md](../ROADMAP.md) for remediation schedule.

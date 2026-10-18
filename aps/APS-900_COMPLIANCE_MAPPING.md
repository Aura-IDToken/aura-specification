# APS-900 — Compliance Mapping

Document ID: APS-900  
Version: 1.0-DRAFT  
Status: DRAFT  
Classification: Normative Governance Specification  
Authority: APS-001 §11 · APS-100 · APS-200 · APS-300 · APS-400 · APS-500
Last Review: 2026-09-26

---

## 1. Purpose

APS-900 defines the Traceability mechanism for the Aura Protocol.

Every normative requirement MUST be traceable from its source through to proof of its fulfillment.

Structural traceability readiness and executed conformance evidence are distinct. A mapped chain is necessary, but it is not by itself a PASS result.

---

## 2. Objectives

Compliance Mapping provides:
- **Full Traceability** — every requirement traces to evidence
- **Auditability** — independent verification of compliance
- **Consistency** — documentation and implementation alignment
- **Impact Analysis** — change in one document → known impact on others
- **Certification basis** — traceability chain is required for conformance

---

## 3. Mapping Model

```
AURA Constitution
        ↓
APS Requirement (APS-001 through APS-950)
        ↓
Protocol Invariant (INV-xxx)
        ↓
Canonical Data Model Entity (ENT-xxx)
        ↓
Evidence Requirement (EVID-xxx type / APS-300 contract)
        ↓
Conformance Test (CONF-xxx)
        ↓
Reference Fixture (FIX-xxx)
        ↓
Reference Implementation
        ↓
Release (REL-xxx)
```

A missing link in this chain is an incomplete compliance path.

---

## 4. Compliance Record

Each requirement has a compliance record:

| Field | Description |
|-------|-------------|
| `compliance_id` | Unique identifier |
| `aps_reference` | APS document and section |
| `invariant_reference` | INV-xxx |
| `data_model_reference` | ENT-xxx |
| `evidence_reference` | EVID-xxx type and/or evidence artifact reference |
| `conformance_test_reference` | CONF-xxx |
| `fixture_reference` | FIX-xxx |
| `implementation_reference` | RI-PY or RI-RS |
| `release_reference` | REL-xxx |
| `compliance_status` | OPEN / BLOCKED / READY / NOT VERIFIED / PASS / FAIL / PARTIAL / DEPRECATED |

---

## 5. Compliance Status

| Status | Meaning |
|--------|---------|
| OPEN | The intended compliance path exists, but one or more required links are still incomplete |
| BLOCKED | A prerequisite contract, fixture, registry entry, or approval gate is still missing |
| READY | Structural path is sufficiently defined for controlled execution, but execution evidence is not yet recorded |
| NOT VERIFIED | Structural path exists, but no objective execution evidence has been validated |
| PASS | Requirement is satisfied with objective evidence and no open mandatory gate |
| FAIL | Requirement is objectively shown not to satisfy the requirement |
| PARTIAL | Some required evidence exists, but at least one mandatory condition for PASS remains unmet |
| DEPRECATED | Requirement withdrawn |

---

## 6. Impact Analysis

Every APS document change MUST define impact on:
- Protocol Invariants
- Canonical Data Model
- Evidence Model
- Conformance Tests
- Reference Fixtures
- Reference Implementations

---

## 7. Traceability Matrix

Full machine-readable matrix: [../compliance/TRACEABILITY_MATRIX.md](../compliance/TRACEABILITY_MATRIX.md)

Example entries:

| APS | INV | CONF | FIX | EVID | STATUS |
|-----|-----|------|-----|------|--------|
| APS-001 §2 | INV-001 | CONF-001 | FIX-001 | EVID-CORE | BLOCKED |
| APS-200 §8 | INV-003 | CONF-003 | CANONICAL-001 | EVID-CORE | PARTIAL |
| APS-300 §11 / APS-200 ENT-007 | INV-012 | CONF-012 | FIX-INV-012 | EVID-AUDIT | READY |

---

## 8. Compliance Report

Each implementation generates a Compliance Report containing:
- Protocol version
- Implementation version
- Test results
- Evidence Pack identifiers
- List of satisfied and unsatisfied requirements
- Explicit records for any remaining `OPEN`, `BLOCKED`, `READY`, or `NOT VERIFIED` rows

Template: [../templates/CONFORMANCE_REPORT_TEMPLATE.md](../templates/CONFORMANCE_REPORT_TEMPLATE.md)

---

## 9. Certification Rules

An implementation MAY be marked Aura Protocol Conformant if:
- All mandatory compliance records have status PASS
- No requirements have status FAIL
- No mandatory row remains OPEN, BLOCKED, READY, PARTIAL, or NOT VERIFIED
- A complete traceability path exists for every requirement

---

## 10. Governance

APS-900 is the reference document for:
- Architecture Reviews
- Compliance Reviews
- Audits
- Certification processes

Every new APS version requires corresponding updates to the Compliance Mapping.

---

*Source: Original text preserved in [`APS-900 — Compliance Mapping_260723_194128.txt`](../APS-900%20%E2%80%94%20Compliance%20Mapping_260723_194128.txt)*

# APS-400 — Conformance Test Matrix

Document ID: APS-400  
Version: 1.0-DRAFT  
Status: DRAFT  
Classification: Normative Specification  
Authority: APS-001 · APS-100 · APS-200 · APS-300  
Last Review: 2026-07-23

---

## 1. Purpose

APS-400 defines the official set of Conformance Tests that every Aura implementation MUST pass to be considered conformant with the protocol.

## 2. Test Categories

| Category | Purpose |
|---|---|
| Functional | Correctness of protocol function |
| Determinism | Repeatability of results |
| Replay | Reproducibility of executions |
| Serialization | Conformance with Canonical Data Model |
| Evidence | Correctness of Evidence Pack |
| Integrity | Data integrity verification |
| Security | Security requirement verification |
| Compatibility | Protocol version compatibility |

## 3. Test Definition

Every test MUST define Test ID, Name, Purpose, Related APS sections, Related Invariant(s), Preconditions, Test Procedure, Expected Result, Evidence Required, and PASS / FAIL Criteria.

Full test definitions: [../conformance/](../conformance/)

## 4. Canonical Test Matrix

| Test ID | Name | Related Invariant | Category | Status |
|---|---|---|---|---|
| CONF-001 | Deterministic Evaluation | INV-001 | Determinism | DRAFT |
| CONF-002 | Replay Verification | INV-002 | Replay | DRAFT |
| CONF-003 | Canonical Serialization | INV-003 | Serialization | DRAFT |
| CONF-004 | Evidence Integrity | INV-004 | Evidence | DRAFT |
| CONF-005 | Traceability | INV-005 | Evidence | DRAFT |
| CONF-006 | Platform Independence | INV-006 | Functional | DRAFT |
| CONF-007 | Fail Closed | INV-008 | Security | DRAFT |
| CONF-008 | Version Compatibility | INV-009 | Compatibility | DRAFT |
| CONF-009 | Evidence Completeness | INV-004 · INV-005 | Evidence | DRAFT |
| CONF-010 | Cryptographic Verification | INV-011 | Integrity | DRAFT |
| CONF-011 | Zero Float Runtime | INV-007 | Determinism / Static Analysis | DRAFT |
| CONF-012 | Auditability | INV-012 | Evidence / Audit | DRAFT |
| CONF-013 | Policy Determinism | INV-013 | Determinism / Functional | DRAFT |
| CONF-014 | Reference Compatibility | INV-014 | Compatibility / Fixtures | DRAFT |
| CONF-015 | Canonical Identity | INV-015 | Identity / Data Model | DRAFT |

### CONF-001…CONF-010

The existing definitions remain authoritative for CONF-001 through CONF-010. See the corresponding files in [../conformance/](../conformance/).

### CONF-011 — Zero Float Runtime
**Related Invariant:** INV-007  
**Purpose:** Verify that the protocol execution path contains no prohibited floating-point operations where they would violate deterministic execution.  
**PASS Criterion:** static analysis identifies no prohibited runtime float operations and applicable deterministic fixtures pass.  
See [../conformance/CONF-011_ZERO_FLOAT_RUNTIME.md](../conformance/CONF-011_ZERO_FLOAT_RUNTIME.md)

### CONF-012 — Auditability
**Related Invariant:** INV-012  
**Purpose:** Verify that every protocol-governed execution leaves a conformant ENT-007 Audit Record.  
**PASS Criterion:** required Audit Record exists, validates against applicable schema and event-type semantics, and integrity/chain verification succeeds.  
See [../conformance/CONF-012_AUDITABILITY.md](../conformance/CONF-012_AUDITABILITY.md)

### CONF-013 — Policy Determinism
**Related Invariant:** INV-013  
**Purpose:** Verify identical decisions for identical inputs under the same pinned policy version.  
**PASS Criterion:** all decision and digest-domain outputs are identical.  
See [../conformance/CONF-013_POLICY_DETERMINISM.md](../conformance/CONF-013_POLICY_DETERMINISM.md)

### CONF-014 — Reference Compatibility
**Related Invariant:** INV-014  
**Purpose:** Verify that every applicable normative APS-500 Reference Fixture passes.  
**PASS Criterion:** all applicable fixtures return their normative expected results.  
See [../conformance/CONF-014_REFERENCE_COMPATIBILITY.md](../conformance/CONF-014_REFERENCE_COMPATIBILITY.md)

### CONF-015 — Canonical Identity
**Related Invariant:** INV-015  
**Purpose:** Verify valid, unique and traceable canonical identity for every applicable protocol artifact.  
**PASS Criterion:** all applicable artifacts satisfy identity syntax, semantics and uniqueness requirements.  
See [../conformance/CONF-015_CANONICAL_IDENTITY.md](../conformance/CONF-015_CANONICAL_IDENTITY.md)

## 5. Test Results

Each test returns one of: **PASS**, **FAIL**, **NOT APPLICABLE**, **ERROR**.

Assignment of a CONF identifier does not constitute a PASS result.

## 6. Conformance Report

After executing all tests, an implementation generates a report containing implementation identifier, protocol version, tests executed, results, Evidence Pack identifier and execution date.

Template: [../templates/CONFORMANCE_REPORT_TEMPLATE.md](../templates/CONFORMANCE_REPORT_TEMPLATE.md)

## 7. Certification Rules

An implementation MAY be marked Aura Protocol Conformant if all mandatory tests return PASS, no Critical violations exist, a valid Evidence Pack has been generated, and the applicable APS version is current.

## 8. Traceability Matrix

```text
APS Requirement
      ↓
Protocol Invariant
      ↓
Conformance Test (CONF-xxx)
      ↓
Evidence (EVID-xxx)
      ↓
Release (REL-xxx)
```

Full matrix: [../compliance/TRACEABILITY_MATRIX.md](../compliance/TRACEABILITY_MATRIX.md)

---

*Source: Original text preserved in [`APS-400 — Conformance Test Matrix_260723_193617.txt`](../APS-400%20—%20Conformance%20Test%20Matrix_260723_193617.txt)*
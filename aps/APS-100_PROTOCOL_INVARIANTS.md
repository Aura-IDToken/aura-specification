# APS-100 — Protocol Invariants

Document ID: APS-100  
Version: 1.0-DRAFT  
Status: DRAFT  
Classification: Normative Specification  
Authority: APS-001 — Aura Protocol Specification  
Last Review: 2026-07-23

---

## 1. Purpose

Protocol Invariants define properties that MUST be preserved by every conformant Aura Protocol implementation.

Violation of any single Invariant constitutes a conformance failure.

---

## 2. Invariant Structure

Every Invariant MUST define:
- Identifier (`INV-NNN`)
- Title
- Requirement (using MUST/SHOULD/MAY)
- Rationale
- Verification Method
- Required Evidence
- Failure Classification
- Related APS documents
- Related ADRs
- Related Conformance Tests

Full definitions: [../invariants/INVARIANT_REGISTRY.md](../invariants/INVARIANT_REGISTRY.md)

---

## 3. Invariant Catalogue v1.0

| ID | Title | Class | Conformance Test |
|----|-------|-------|-----------------|
| INV-001 | Deterministic Evaluation | Critical | CONF-001 |
| INV-002 | Bit-Perfect Replay | Critical | CONF-002 |
| INV-003 | Canonical Serialization | Critical | CONF-003 |
| INV-004 | Immutable Evidence | Critical | CONF-004 |
| INV-005 | Evidence Traceability | Critical | CONF-005 |
| INV-006 | Platform Independence | Critical | CONF-006 |
| INV-007 | Zero Float Runtime | Critical | — |
| INV-008 | Fail Closed | Critical | CONF-007 |
| INV-009 | Version Consistency | Major | CONF-008 |
| INV-010 | Conformance Completeness | Critical | CONF-009 |
| INV-011 | Cryptographic Integrity | Critical | CONF-010 |
| INV-012 | Auditability | Critical | — |
| INV-013 | Policy Determinism | Critical | — |
| INV-014 | Reference Compatibility | Critical | — |
| INV-015 | Canonical Identity | Major | — |

### INV-001 — Deterministic Evaluation
**MUST**: Identical inputs MUST produce identical outputs.

### INV-002 — Bit-Perfect Replay
**MUST**: Replay of an execution MUST reproduce an identical result on every conformant implementation.

### INV-003 — Canonical Serialization
**MUST**: Every protocol object MUST have an unambiguous serialization representation.

The canonical serialization profile that satisfies this invariant is **RFC 8785
(JCS)**, defined normatively in APS-200 §8. Two independent implementations MUST
produce byte-identical canonical bytes for the same value in the JSON data model.
Verified by CONF-003 against the CANONICAL-001 fixture.

### INV-004 — Immutable Evidence
**MUST**: Evidence MUST NOT be modified after generation.

### INV-005 — Evidence Traceability
**MUST**: Every Evidence artifact MUST reference the requirement it documents.

### INV-006 — Platform Independence
**MUST**: An implementation MUST produce conformant results regardless of hardware platform or operating system.

### INV-007 — Zero Float Runtime
**MUST NOT**: Protocol logic MUST NOT use floating-point arithmetic during execution if doing so would violate determinism as defined by the specification.

### INV-008 — Fail Closed
**MUST**: In case of error, an implementation MUST terminate execution in a safe state.

### INV-009 — Version Consistency
**MUST**: Evidence, Protocol, and Data Model MUST reference compatible document versions.

### INV-010 — Conformance Completeness
**MUST**: Every Invariant MUST have a corresponding Conformance Test.

### INV-011 — Cryptographic Integrity
**MUST**: The integrity of Evidence MUST be cryptographically verifiable.

### INV-012 — Auditability
**MUST**: Every protocol-governed execution MUST leave an audit trail conformant with APS requirements.

### INV-013 — Policy Determinism
**MUST**: The same policy version and identical inputs MUST produce an identical decision.

### INV-014 — Reference Compatibility
**MUST**: An implementation MUST pass all applicable Reference Fixtures.

### INV-015 — Canonical Identity
**MUST**: Every protocol artifact MUST have a unique identifier conformant with APS-000.

---

## 4. Failure Classification

| Class | Meaning |
|-------|---------|
| Critical | Protocol conformance violation |
| Major | Conformance impact; correction required |
| Minor | Inconsistency without output impact |
| Informational | Recommendation or observation |

---

## 5. Traceability Matrix

Every Invariant MUST have links:

```
INV
 ↓
APS Requirement
 ↓
Conformance Test (CONF-xxx)
 ↓
Evidence (EVID-xxx)
 ↓
ADR
 ↓
Release (REL-xxx)
```

Full matrix: [../compliance/TRACEABILITY_MATRIX.md](../compliance/TRACEABILITY_MATRIX.md)

---

## 6. Compliance Rules

An implementation MAY be marked Aura Protocol Conformant only when:
- All Invariants have status PASS
- All required Conformance Tests have passed
- A complete Evidence Pack has been generated
- No Critical-class violations exist

---

## 7. Extension Rules

New Invariants MUST:
- Have a unique identifier
- Define a verification method
- Have at least one Conformance Test
- Define required Evidence

Removal of an Invariant requires a new APS version and formal change process.

---

*Source: Original text preserved in [`APS-100 — Protocol Invariants_260723_192315.txt`](../APS-100%20%E2%80%94%20Protocol%20Invariants_260723_192315.txt)*

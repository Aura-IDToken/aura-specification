# Invariant Registry

Document ID: INV-REG-001  
Version: 1.0-DRAFT  
Status: DRAFT  
Authority: APS-100  
Last Review: 2026-07-23

---

## Purpose

This registry is the canonical, machine-readable source for all Protocol Invariants. It supplements APS-100 with full definitions, verification methods, and traceability links.

---

## Registry

### INV-001 — Deterministic Evaluation

| Field | Value |
|---|---|
| ID | INV-001 |
| Title | Deterministic Evaluation |
| Class | Critical |
| Related APS | APS-001 §2, APS-100 §3 |
| Conformance Test | CONF-001 |

**Requirement (MUST):** Identical inputs MUST produce identical outputs on every execution.  
**Verification:** Execute the same Evaluation Request twice and compare all output fields bit-by-bit.  
**Evidence:** EVID-CORE (output_hash identical across runs).

### INV-002 — Bit-Perfect Replay

| Field | Value |
|---|---|
| ID | INV-002 |
| Title | Bit-Perfect Replay |
| Class | Critical |
| Related APS | APS-001 §2, APS-100 §3 |
| Conformance Test | CONF-002 |

**Requirement (MUST):** Replay of an execution using its Evidence Pack MUST reproduce an identical Evaluation Result on every conformant implementation.  
**Verification:** Replay execution and compare output hash.  
**Evidence:** EVID-CORE, EVID-CHAIN.

### INV-003 — Canonical Serialization

| Field | Value |
|---|---|
| ID | INV-003 |
| Title | Canonical Serialization |
| Class | Critical |
| Related APS | APS-200 §8 |
| Conformance Test | CONF-003 |

**Requirement (MUST):** Every protocol object MUST have an unambiguous canonical serialization.  
**Verification:** Independently serialize the same object and compare bytes.  
**Evidence:** EVID-CORE.

### INV-004 — Immutable Evidence

| Field | Value |
|---|---|
| ID | INV-004 |
| Title | Immutable Evidence |
| Class | Critical |
| Related APS | APS-300 §3, §7 |
| Conformance Test | CONF-004 |

**Requirement (MUST NOT):** Evidence MUST NOT be modified after generation.  
**Verification:** Mutate an Evidence object and verify integrity failure.  
**Evidence:** EVID-CORE.

### INV-005 — Evidence Traceability

| Field | Value |
|---|---|
| ID | INV-005 |
| Title | Evidence Traceability |
| Class | Critical |
| Related APS | APS-300 §11, APS-900 |
| Conformance Test | CONF-005 |

**Requirement (MUST):** Every Evidence artifact MUST reference the APS requirement it documents.  
**Verification:** Validate required reference fields and links.  
**Evidence:** EVID-CORE.

### INV-006 — Platform Independence

| Field | Value |
|---|---|
| ID | INV-006 |
| Title | Platform Independence |
| Class | Critical |
| Related APS | APS-001 §2 |
| Conformance Test | CONF-006 |

**Requirement (MUST):** An implementation MUST produce conformant results regardless of hardware platform or operating system.  
**Verification:** Run the same fixture on different hardware architectures and compare outputs.  
**Evidence:** EVID-CORE.

### INV-007 — Zero Float Runtime

| Field | Value |
|---|---|
| ID | INV-007 |
| Title | Zero Float Runtime |
| Class | Critical |
| Related APS | APS-001 §2 |
| Conformance Test | CONF-011 |

**Requirement (MUST NOT):** Protocol logic MUST NOT use floating-point arithmetic during execution if doing so would violate determinism as defined by the specification.  
**Verification:** Code review + static analysis of the protocol execution path, followed by applicable deterministic fixtures.  
**Evidence:** EVID-CORE static-analysis report plus conformance evidence.

**Closure note:** CONF-011 is assigned; this is not yet a PASS result.

### INV-008 — Fail Closed

| Field | Value |
|---|---|
| ID | INV-008 |
| Title | Fail Closed |
| Class | Critical |
| Related APS | APS-001 §8 |
| Conformance Test | CONF-007 |

**Requirement (MUST):** In case of error, an implementation MUST terminate execution in a safe state. No partial output MUST be generated or persisted.  
**Verification:** Inject invalid input/policy and verify safe termination without partial Evidence.  
**Evidence:** EVID-CORE.

### INV-009 — Version Consistency

| Field | Value |
|---|---|
| ID | INV-009 |
| Title | Version Consistency |
| Class | Major |
| Related APS | APS-000 §9, APS-200 §9 |
| Conformance Test | CONF-008 |

**Requirement (MUST):** Evidence, Protocol, and Data Model version references MUST be mutually consistent.  
**Verification:** Validate the compatibility matrix.  
**Evidence:** EVID-CORE.

### INV-010 — Conformance Completeness

| Field | Value |
|---|---|
| ID | INV-010 |
| Title | Conformance Completeness |
| Class | Critical |
| Related APS | APS-400 |
| Conformance Test | CONF-009 |

**Requirement (MUST):** Every Invariant MUST have at least one corresponding Conformance Test.  
**Verification:** Verify every INV-xxx entry has a linked CONF-xxx in APS-400.  
**Evidence:** EVID-CONF.

### INV-011 — Cryptographic Integrity

| Field | Value |
|---|---|
| ID | INV-011 |
| Title | Cryptographic Integrity |
| Class | Critical |
| Related APS | APS-300 §7 |
| Conformance Test | CONF-010 |

**Requirement (MUST):** Evidence integrity MUST be cryptographically verifiable by an independent party.  
**Verification:** Independently compute all hashes and compare stored values.  
**Evidence:** EVID-CORE.

### INV-012 — Auditability

| Field | Value |
|---|---|
| ID | INV-012 |
| Title | Auditability |
| Class | Critical |
| Related APS | APS-300, APS-200 ENT-007 |
| Conformance Test | CONF-012 |

**Requirement (MUST):** Every protocol-governed execution MUST leave an Audit Record (ENT-007) conformant with APS requirements.  
**Verification:** Validate required Audit Record fields, registered event type, and chain/integrity state.  
**Evidence:** EVID-AUDIT.

**Closure note:** CONF-012 is assigned; final PASS depends on the normative ENT-007/event-type and hash-domain contracts.

### INV-013 — Policy Determinism

| Field | Value |
|---|---|
| ID | INV-013 |
| Title | Policy Determinism |
| Class | Critical |
| Related APS | APS-001 §5 |
| Conformance Test | CONF-013 |

**Requirement (MUST):** The same policy version and identical inputs MUST produce an identical decision.  
**Verification:** Execute twice with a pinned policy version and compare decisions/digest-domain outputs.  
**Evidence:** EVID-CORE.

### INV-014 — Reference Compatibility

| Field | Value |
|---|---|
| ID | INV-014 |
| Title | Reference Compatibility |
| Class | Critical |
| Related APS | APS-500 |
| Conformance Test | CONF-014 |

**Requirement (MUST):** An implementation MUST pass all applicable Reference Fixtures (APS-500).  
**Verification:** Run all applicable normative FIX-xxx fixtures and compare expected values.  
**Evidence:** EVID-CORE, EVID-CONF.

### INV-015 — Canonical Identity

| Field | Value |
|---|---|
| ID | INV-015 |
| Title | Canonical Identity |
| Class | Major |
| Related APS | APS-000 §4, APS-200 §4 |
| Conformance Test | CONF-015 |

**Requirement (MUST):** Every protocol artifact MUST have a unique identifier conformant with APS-000 naming conventions.  
**Verification:** Validate required `object_id`/`object_type`, identity syntax/semantics, and uniqueness within the applicable scope.  
**Evidence:** EVID-CORE.

**Closure note:** CONF-015 is assigned; final PASS depends on the resolved APS-000/APS-200 identity contract.

---

## Conformance Assignment Status

All fifteen invariants now have a CONF assignment:

| Invariant | Conformance Test | Assignment |
|---|---|---|
| INV-001 | CONF-001 | Existing |
| INV-002 | CONF-002 | Existing |
| INV-003 | CONF-003 | Existing |
| INV-004 | CONF-004 | Existing |
| INV-005 | CONF-005 | Existing |
| INV-006 | CONF-006 | Existing |
| INV-007 | CONF-011 | **New** |
| INV-008 | CONF-007 | Existing |
| INV-009 | CONF-008 | Existing |
| INV-010 | CONF-009 | Existing |
| INV-011 | CONF-010 | Existing |
| INV-012 | CONF-012 | **New** |
| INV-013 | CONF-013 | **New** |
| INV-014 | CONF-014 | **New** |
| INV-015 | CONF-015 | **New** |

Assignment satisfies the structural requirement that every invariant has a corresponding CONF identifier. It does **not** mean that any of the tests have passed.

## Closure Rule

A conformance assignment is not evidence of conformance. PASS requires execution of the assigned test, normative fixtures where applicable, required Evidence, and resolution of all upstream specification dependencies.

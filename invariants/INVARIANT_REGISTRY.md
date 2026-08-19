# Invariant Registry

Document ID: INV-REG-001  
Version: 1.0-DRAFT  
Status: DRAFT  
Authority: APS-100  
Last Review: 2026-08-19

---

## Purpose

This registry is the canonical, machine-readable source for all Protocol Invariants. It supplements APS-100 with full definitions, verification methods, and traceability links.

---

## Registry

### INV-001 — Deterministic Evaluation

| Field | Value |
|-------|-------|
| ID | INV-001 |
| Title | Deterministic Evaluation |
| Class | Critical |
| Related APS | APS-001 §2, APS-100 §3 |
| Conformance Test | CONF-001 |

**Requirement (MUST)**: Identical inputs MUST produce identical outputs on every execution.

**Rationale**: Non-deterministic output cannot be audited, replayed, or independently verified.

**Verification Method**: Execute the same Evaluation Request twice and compare all output fields bit-by-bit.

**Required Evidence**: EVID-CORE (output_hash must be identical across runs)

**Failure Classification**: Critical

---

### INV-002 — Bit-Perfect Replay

| Field | Value |
|-------|-------|
| ID | INV-002 |
| Title | Bit-Perfect Replay |
| Class | Critical |
| Related APS | APS-001 §2, APS-100 §3 |
| Conformance Test | CONF-002 |

**Requirement (MUST)**: Replay of an execution using its Evidence Pack MUST reproduce an identical Evaluation Result on every conformant implementation.

**Rationale**: Replay capability is the foundation of independent audit and regulatory verification.

**Verification Method**: Replay execution from Evidence Pack; compare output hash to stored output_hash.

**Required Evidence**: EVID-CORE, EVID-CHAIN

**Failure Classification**: Critical

---

### INV-003 — Canonical Serialization

| Field | Value |
|-------|-------|
| ID | INV-003 |
| Title | Canonical Serialization |
| Class | Critical |
| Related APS | APS-200 §8 |
| Conformance Test | CONF-003 |

**Requirement (MUST)**: Every protocol object MUST have an unambiguous canonical serialization.

**Rationale**: Cryptographic hashes require a canonical byte representation. Multiple valid serializations of the same object would produce different hashes, breaking integrity verification.

**Verification Method**: Serialize the same object twice independently; compare byte representations.

**Required Evidence**: EVID-CORE

**Failure Classification**: Critical

---

### INV-004 — Immutable Evidence

| Field | Value |
|-------|-------|
| ID | INV-004 |
| Title | Immutable Evidence |
| Class | Critical |
| Related APS | APS-300 §3, §7 |
| Conformance Test | CONF-004 |

**Requirement (MUST NOT)**: Evidence MUST NOT be modified after generation.

**Rationale**: Mutable evidence cannot be trusted. Immutability is the basis of auditability.

**Verification Method**: Modify an Evidence object and verify that the integrity check detects the modification.

**Required Evidence**: EVID-CORE

**Failure Classification**: Critical

---

### INV-005 — Evidence Traceability

| Field | Value |
|-------|-------|
| ID | INV-005 |
| Title | Evidence Traceability |
| Class | Critical |
| Related APS | APS-300 §11, APS-900 |
| Conformance Test | CONF-005 |

**Requirement (MUST)**: Every Evidence artifact MUST reference the APS requirement it documents.

**Rationale**: Evidence without traceability cannot be used to verify conformance.

**Verification Method**: Inspect Evidence object for required reference fields; validate all links resolve.

**Required Evidence**: EVID-CORE

**Failure Classification**: Critical

---

### INV-006 — Platform Independence

| Field | Value |
|-------|-------|
| ID | INV-006 |
| Title | Platform Independence |
| Class | Critical |
| Related APS | APS-001 §2 |
| Conformance Test | CONF-006 |

**Requirement (MUST)**: An implementation MUST produce conformant results regardless of hardware platform or operating system.

**Rationale**: Platform-dependent results cannot be independently verified on different hardware.

**Verification Method**: Run the same fixture on two different hardware architectures; compare outputs.

**Required Evidence**: EVID-CORE

**Failure Classification**: Critical

---

### INV-007 — Zero Float Runtime

| Field | Value |
|-------|-------|
| ID | INV-007 |
| Title | Zero Float Runtime |
| Class | Critical |
| Related APS | APS-001 §2 |
| Conformance Test | — (TODO) |

**Requirement (MUST NOT)**: Protocol logic MUST NOT use floating-point arithmetic during execution if doing so would violate determinism as defined by the specification.

**Rationale**: IEEE-754 floating-point is not associative. Results differ between hardware implementations (e.g., x86 AVX vs ARM NEON), violating INV-006.

**Verification Method**: Code review + static analysis to confirm no floating-point operations in the protocol execution path.

**Required Evidence**: EVID-CORE

**Failure Classification**: Critical

> **TODO**: Define a Conformance Test for INV-007.

---

### INV-008 — Fail Closed

| Field | Value |
|-------|-------|
| ID | INV-008 |
| Title | Fail Closed |
| Class | Critical |
| Related APS | APS-001 §8 |
| Conformance Test | CONF-007 |

**Requirement (MUST)**: In case of error, an implementation MUST terminate execution in a safe state. No partial output MUST be generated or persisted.

**Rationale**: Partial output under error conditions creates undefined state that cannot be audited.

**Verification Method**: Inject invalid input or policy; verify implementation halts cleanly without partial Evidence.

**Required Evidence**: EVID-CORE

**Failure Classification**: Critical

---

### INV-009 — Version Consistency

| Field | Value |
|-------|-------|
| ID | INV-009 |
| Title | Version Consistency |
| Class | Major |
| Related APS | APS-000 §9, APS-200 §9 |
| Conformance Test | CONF-008 |
| Closure Status | **MAPPED — CONF-008** |

**Requirement (MUST)**: Evidence, Protocol, and Data Model version references MUST be mutually consistent.

**Rationale**: Evidence referencing incompatible versions cannot be correctly interpreted.

**Verification Method**: Inspect all version fields in Evidence Pack; verify compatibility matrix.

**Required Evidence**: EVID-CORE

**Failure Classification**: Major

**Closure note**: The invariant is explicitly assigned to CONF-008 Version Compatibility. DQ-006 closure does not reopen DQ-003. Full INV-009 conformance remains subject to execution of CONF-008 against the finalized version compatibility matrix and applicable fixture corpus.

---

### INV-010 — Conformance Completeness

| Field | Value |
|-------|-------|
| ID | INV-010 |
| Title | Conformance Completeness |
| Class | Critical |
| Related APS | APS-400 |
| Conformance Test | CONF-009 |

**Requirement (MUST)**: Every Invariant MUST have at least one corresponding Conformance Test.

**Rationale**: An untested invariant is an unverifiable invariant.

**Verification Method**: Verify that every INV-xxx entry in the Invariant Registry has a linked CONF-xxx in APS-400.

**Required Evidence**: EVID-CONF

**Failure Classification**: Critical

---

### INV-011 — Cryptographic Integrity

| Field | Value |
|-------|-------|
| ID | INV-011 |
| Title | Cryptographic Integrity |
| Class | Critical |
| Related APS | APS-300 §7 |
| Conformance Test | CONF-010 |

**Requirement (MUST)**: The integrity of Evidence MUST be cryptographically verifiable by an independent party.

**Rationale**: Integrity claims without cryptographic proof are unauditable.

**Verification Method**: Independently compute all hashes in the Evidence Pack; verify they match stored values.

**Required Evidence**: EVID-CORE

**Failure Classification**: Critical

---

### INV-012 — Auditability

| Field | Value |
|-------|-------|
| ID | INV-012 |
| Title | Auditability |
| Class | Critical |
| Related APS | APS-300, APS-200 ENT-007 |
| Conformance Test | — (TODO) |

**Requirement (MUST)**: Every protocol-governed execution MUST leave an Audit Record (ENT-007) conformant with APS requirements.

**Rationale**: An execution without an audit record cannot be verified.

**Verification Method**: Inspect Audit Record after execution; verify all required fields present and chain intact.

**Required Evidence**: EVID-AUDIT

**Failure Classification**: Critical

> **TODO**: Define a Conformance Test for INV-012.

---

### INV-013 — Policy Determinism

| Field | Value |
|-------|-------|
| ID | INV-013 |
| Title | Policy Determinism |
| Class | Critical |
| Related APS | APS-001 §5 |
| Conformance Test | — (TODO) |

**Requirement (MUST)**: The same policy version and identical inputs MUST produce an identical decision.

**Rationale**: Policy changes must be versioned so their effect on decisions is traceable.

**Verification Method**: Execute with pinned policy version and same input twice; compare decisions.

**Required Evidence**: EVID-CORE

**Failure Classification**: Critical

> **TODO**: Define a Conformance Test for INV-013.

---

### INV-014 — Reference Compatibility

| Field | Value |
|-------|-------|
| ID | INV-014 |
| Title | Reference Compatibility |
| Class | Critical |
| Related APS | APS-500 |
| Conformance Test | — (TODO) |

**Requirement (MUST)**: An implementation MUST pass all applicable Reference Fixtures (APS-500).

**Rationale**: Fixtures are the cross-implementation comparability mechanism.

**Verification Method**: Run all applicable FIX-xxx fixtures; compare outputs to expected values.

**Required Evidence**: EVID-CORE, EVID-CONF

**Failure Classification**: Critical

> **TODO**: Define a Conformance Test for INV-014.

---

### INV-015 — Canonical Identity

| Field | Value |
|-------|-------|
| ID | INV-015 |
| Title | Canonical Identity |
| Class | Major |
| Related APS | APS-000 §4, APS-200 §4 |
| Conformance Test | — (TODO) |

**Requirement (MUST)**: Every protocol artifact MUST have a unique identifier conformant with APS-000 naming conventions.

**Rationale**: Unidentified artifacts cannot be referenced in traceability chains.

**Verification Method**: Inspect all output objects for required `object_id` and `object_type` fields.

**Required Evidence**: EVID-CORE

**Failure Classification**: Major

> **TODO**: Define a Conformance Test for INV-015.

---

## Missing Conformance Tests

The following invariants do not yet have assigned Conformance Tests (violates INV-010):

| Invariant | Priority |
|-----------|----------|
| INV-007 | High |
| INV-012 | High |
| INV-013 | High |
| INV-014 | Critical |
| INV-015 | High |

See [ROADMAP.md](../ROADMAP.md) Milestone 3.

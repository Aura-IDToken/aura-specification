# SPEC-002 — Constitution Artifact Contract

Document ID: SPEC-002  
Version: 0.1-DRAFT  
Status: DRAFT  
Classification: Normative Specification Contract  
Owner: Protocol Custodian  
Authority: AURA Constitution v1.0 (FROZEN) · APS-000 · APS-200 · APS-300 · APS-400 · APS-900  
Last Review: 2026-08-10

---

> **DRAFT ONLY / SPECIFICATION WORK**  
> This document defines the contract surface for a future Constitution Artifact and Constitution Vector. It MUST NOT be used to implement, generate, register, or freeze a Constitution Artifact or Constitution Vector until all blocking architectural decisions are explicitly approved.

---

## 1. Purpose

SPEC-002 defines the normative contract required for an independent implementer to later construct and verify exactly one canonical Constitution Artifact from the authoritative Constitution source.

This document does not approve any candidate algorithm, numeric encoding, dictionary, serialization format, or implementation behavior that is not already established by an existing normative source.

---

## 2. Scope and Non-Goals

### 2.1 Scope

SPEC-002 covers the required contract surface for:

- Source Identity
- Source canonicalization
- Transformation
- Normalization
- Embedding
- Dictionary identity and versioning
- Numeric representation
- Vector identity
- Canonical serialization
- Canonical byte sequence
- SHA-256 input and calculation
- Artifact identity
- Source-to-artifact binding
- Artifact-to-vector binding
- Commit/execution provenance binding
- Versioning
- Lineage
- `supersedes`
- Registration
- Freeze
- Verification
- Failure conditions

### 2.2 Non-Goals

This document MUST NOT:

- Modify `aura-poc-a-core-v3.3`
- Implement CR-007
- Generate a Constitution Vector
- Create or register `constitution.json`, `vector.json`, or any equivalent canonical artifact
- Treat any unapproved alias as equivalent to the authoritative Constitution identifier
- Promote candidate architectural decisions to normative requirements without explicit governance authority

---

## 3. Governing Constraints

1. The contract defined by SPEC-002 MUST preserve **Specification First** and **Architecture Before Implementation** per AURA Constitution Article IV.
2. The contract MUST fail closed when any required input, dependency, identity binding, or verification step is ambiguous, missing, or inconsistent.
3. Any algorithmic degree of freedom that could allow two conformant implementations to produce different vectors, different canonical bytes, or different hashes MUST be eliminated before SPEC-002 can become READY.
4. Candidate choices including `32`, `100000`, `signed int32`, `little-endian`, `Dictionary-Based Embedding`, and `round-half-to-even` are non-normative in this draft unless and until explicit architectural authority approves them.

---

## 4. Normative Contract Requirements

### 4.1 Source Identity

- **REQ-002-001**: SPEC-002 MUST identify exactly one authoritative Constitution source by immutable identifier, version, status, and repository location.
- **REQ-002-002**: Any alternate label, filename, alias, or informal name MUST be treated as distinct unless an approved governance artifact explicitly establishes equivalence.

### 4.2 Source Canonicalization, Transformation, and Normalization

- **REQ-002-003**: SPEC-002 MUST define one deterministic source canonicalization procedure, or explicitly declare that the authoritative source is already canonical.
- **REQ-002-004**: SPEC-002 MUST define the complete transformation pipeline from authoritative source to artifact-ready intermediate representation, including ordered steps and step boundaries.
- **REQ-002-005**: SPEC-002 MUST define all normalization rules that affect the intermediate representation, including whitespace, line endings, encoding, heading treatment, metadata treatment, and inclusion/exclusion boundaries.

### 4.3 Embedding, Dictionary, and Numeric Representation

- **REQ-002-006**: SPEC-002 MUST identify exactly one embedding method by immutable identifier, version, and status.
- **REQ-002-007**: SPEC-002 MUST define the dictionary or equivalent embedding dependency by immutable identifier, version, status, and integrity binding, or MUST explicitly state that no external dictionary is permitted.
- **REQ-002-008**: SPEC-002 MUST define one numeric representation for vector values, including domain, width, sign, scale, rounding behavior, overflow behavior, and byte order where applicable.

### 4.4 Vector Identity and Serialization

- **REQ-002-009**: SPEC-002 MUST define how the Constitution Vector is uniquely identified and how that identity binds to the authoritative source, embedding method, dictionary dependency, and numeric representation.
- **REQ-002-010**: SPEC-002 MUST define exactly one canonical serialization format for the Constitution Vector and Constitution Artifact, including field set, field order, encoding, and representation of absent or optional fields.
- **REQ-002-011**: SPEC-002 MUST define exactly one canonical byte sequence for every hash-bearing Constitution Artifact and Constitution Vector representation.
- **REQ-002-012**: SPEC-002 MUST define the SHA-256 input bytes, calculation procedure, and output representation used for identity and integrity values.

### 4.5 Identity and Binding

- **REQ-002-013**: SPEC-002 MUST define the immutable identity fields of the Constitution Artifact and MUST require those fields to be unique and versioned.
- **REQ-002-014**: SPEC-002 MUST define the required binding from authoritative source to Constitution Artifact, including source identifier, source version, source status, source location, and source integrity reference.
- **REQ-002-015**: SPEC-002 MUST define the required binding from Constitution Artifact to Constitution Vector, including vector identity, dependency identities, canonical bytes reference, and integrity reference.
- **REQ-002-016**: SPEC-002 MUST define the required commit/execution provenance binding for artifact construction, including the repository revision and the deterministic generation context needed for independent verification.

### 4.6 Versioning, Lineage, Registration, and Freeze

- **REQ-002-017**: SPEC-002 MUST define versioning rules for the Constitution Artifact and Constitution Vector that are consistent with repository lifecycle rules and immutable artifact principles.
- **REQ-002-018**: SPEC-002 MUST define lineage fields, including `supersedes` semantics and the conditions under which a new artifact supersedes an older artifact.
- **REQ-002-019**: SPEC-002 MUST define registration requirements, including the authoritative registry location, required registry fields, and required integrity checks at registration time.
- **REQ-002-020**: SPEC-002 MUST define freeze requirements, including who may authorize freeze, what status transition constitutes freeze, and what evidence is required to verify frozen status.

### 4.7 Verification and Failure Conditions

- **REQ-002-021**: SPEC-002 MUST define an independent verification procedure that does not require inspection of any Reference Implementation.
- **REQ-002-022**: SPEC-002 MUST define failure conditions that invalidate the Constitution Artifact, the Constitution Vector, registration, or frozen status.
- **REQ-002-023**: SPEC-002 MUST remain NOT READY if any conformant independent implementation can legitimately produce more than one vector, more than one canonical byte sequence, or more than one SHA-256 value from the same authoritative source and approved dependencies.

---

## 5. Proposed Verification Model

An independent verifier of a future Constitution Artifact MUST be able to perform all of the following using only approved normative specifications and explicitly referenced normative artifacts:

1. Resolve the one authoritative Constitution source.
2. Apply the one approved canonicalization, transformation, and normalization pipeline.
3. Resolve the one approved embedding method and every required dependency.
4. Derive exactly one Constitution Vector.
5. Serialize the vector and artifact into exactly one canonical byte sequence.
6. Reproduce the same SHA-256 values.
7. Verify artifact identity, lineage, registration, and frozen status.
8. Reject the result if any required element is missing, ambiguous, unapproved, or inconsistent.

---

## 6. Explicit Unresolved Architectural Decisions

The following items are unresolved architectural decisions. The identifiers below are local placeholders for this draft only and MUST be replaced by approved architecture decisions before SPEC-002 advances beyond DRAFT.

| Placeholder | Decision Required | Current Status | Candidate Choices Mentioned in Problem Statement | Blocking Effect |
|---|---|---|---|---|
| AD-CA-001 | Authoritative Constitution source identity and exact source scope | UNRESOLVED | None approved | Blocks REQ-002-001 through REQ-002-005 |
| AD-CA-002 | Canonicalization procedure for the authoritative Constitution source | UNRESOLVED | None approved | Blocks REQ-002-003 through REQ-002-005 |
| AD-CA-003 | Transformation pipeline from source to artifact-ready representation | UNRESOLVED | None approved | Blocks REQ-002-004 through REQ-002-005 |
| AD-CA-004 | Normalization rules affecting deterministic output | UNRESOLVED | None approved | Blocks REQ-002-005, REQ-002-010 through REQ-002-012 |
| AD-CA-005 | Embedding method identity and versioning model | UNRESOLVED | `Dictionary-Based Embedding` is candidate only | Blocks REQ-002-006, REQ-002-009, REQ-002-015 |
| AD-CA-006 | Dictionary identity, versioning, integrity, and change policy | UNRESOLVED | None approved | Blocks REQ-002-007, REQ-002-009, REQ-002-015 |
| AD-CA-007 | Numeric representation of vector values | UNRESOLVED | `32`, `100000`, `signed int32`, `little-endian`, `round-half-to-even` are candidate only | Blocks REQ-002-008 through REQ-002-012 |
| AD-CA-008 | Canonical serialization format and canonical byte sequence | UNRESOLVED | None approved | Blocks REQ-002-010 through REQ-002-012 |
| AD-CA-009 | Artifact and vector identity schema | UNRESOLVED | None approved | Blocks REQ-002-009, REQ-002-013 through REQ-002-015 |
| AD-CA-010 | Commit/execution provenance binding schema | UNRESOLVED | None approved | Blocks REQ-002-016, REQ-002-021, REQ-002-022 |
| AD-CA-011 | Registration model and authoritative registry semantics | UNRESOLVED | None approved | Blocks REQ-002-019 through REQ-002-022 |
| AD-CA-012 | Freeze evidence and frozen-status verification model | UNRESOLVED | None approved | Blocks REQ-002-020 through REQ-002-022 |

---

## 7. Traceability Matrix

| Requirement | Requirement Summary | Existing Normative Source | Requires New Architecture Decision |
|---|---|---|---|
| REQ-002-001 | One authoritative Constitution source identity | AURA Constitution Article IV Principles 8-10; APS-000 §4, §7 | AD-CA-001 |
| REQ-002-002 | Alias equivalence requires explicit approval | AURA Constitution Article IV Principle 8; APS-000 §4 | AD-CA-001 |
| REQ-002-003 | One deterministic source canonicalization procedure | AURA Constitution Article IV Principles 1, 2, 8; INV-003; APS-200 §8 | AD-CA-002 |
| REQ-002-004 | Complete ordered transformation pipeline | AURA Constitution Article IV Principles 1, 2, 8, 10 | AD-CA-003 |
| REQ-002-005 | Explicit normalization rules | AURA Constitution Article IV Principles 2, 8; INV-003 | AD-CA-004 |
| REQ-002-006 | One embedding method identity and version | AURA Constitution Article IV Principles 1, 2, 8, 9 | AD-CA-005 |
| REQ-002-007 | Dictionary identity, version, and integrity binding | AURA Constitution Article IV Principle 9; APS-000 §7 | AD-CA-006 |
| REQ-002-008 | One numeric representation | AURA Constitution Article IV Principles 2, 8; INV-006; INV-007 | AD-CA-007 |
| REQ-002-009 | Vector identity binding model | APS-000 §4; INV-015 | AD-CA-005, AD-CA-006, AD-CA-009 |
| REQ-002-010 | One canonical serialization format | INV-003; APS-200 §8 | AD-CA-008 |
| REQ-002-011 | One canonical byte sequence | INV-003; INV-011; APS-200 §4; APS-300 §5 | AD-CA-008 |
| REQ-002-012 | SHA-256 input and calculation procedure | INV-011; APS-200 §4; APS-300 §5, §9 | AD-CA-007, AD-CA-008 |
| REQ-002-013 | Artifact immutable identity fields | APS-000 TERM-011, §4, §7; INV-015 | AD-CA-009 |
| REQ-002-014 | Source-to-artifact binding | APS-900 §3-§4; INV-005; INV-015 | AD-CA-001, AD-CA-002, AD-CA-009 |
| REQ-002-015 | Artifact-to-vector binding | APS-900 §3-§4; INV-005; INV-011; INV-015 | AD-CA-005, AD-CA-006, AD-CA-007, AD-CA-009 |
| REQ-002-016 | Commit/execution provenance binding | AURA Constitution Article X; APS-900 §2, §4; APS-950 §6 | AD-CA-010 |
| REQ-002-017 | Versioning rules | AURA Constitution Article IV Principle 9; VERSIONING.md §3-§4, §9 | None beyond requirements already listed |
| REQ-002-018 | Lineage and `supersedes` semantics | VERSIONING.md §3; AURA Constitution Article XI | AD-CA-009, AD-CA-011, AD-CA-012 |
| REQ-002-019 | Registration model and registry fields | APS-000 §7; APS-900 §4 | AD-CA-011 |
| REQ-002-020 | Freeze requirements and frozen-status verification | AURA Constitution Article VIII, Article XI; VERSIONING.md §3 | AD-CA-012 |
| REQ-002-021 | Independent verification procedure | AURA Constitution Article III, Article IV Principles 2, 4, 8; APS-300 §9; APS-900 §9 | AD-CA-010, AD-CA-011, AD-CA-012 |
| REQ-002-022 | Failure conditions | AURA Constitution Article IV Principle 6; APS-300 §12; INV-008 | AD-CA-010, AD-CA-011, AD-CA-012 |
| REQ-002-023 | NOT READY until one outcome is forced | AURA Constitution Article IV Principles 1, 2, 8; INV-001; INV-002; INV-003; INV-011 | All unresolved decisions above if still open |

---

## 8. Proposed Acceptance Criteria

SPEC-002 MAY advance from DRAFT only when all of the following are true:

1. Every requirement in §4 is backed either by an existing approved normative source or by a newly approved architecture decision incorporated into the specification.
2. The authoritative Constitution source is uniquely identified and its exact source scope is normatively fixed.
3. Canonicalization, transformation, normalization, embedding, dictionary dependency, numeric representation, serialization, canonical byte sequence, and SHA-256 procedure are each normatively reduced to exactly one valid interpretation.
4. Artifact identity, vector identity, lineage, `supersedes`, registration, and frozen-status verification are completely specified and independently checkable.
5. The required independent verification procedure can be executed without inspecting any Reference Implementation.
6. A formal Independent Implementer Test is defined and its PASS condition requires that two conformant independent implementations produce the same vector, the same canonical bytes, and the same SHA-256 values from the same authoritative source and approved dependencies.
7. If any conformant independent implementation can still legitimately produce different vectors, canonical bytes, or hashes, SPEC-002 MUST remain NOT READY.

### 8.1 Independent Implementer Test

The Independent Implementer Test for SPEC-002 is satisfied only if an independent implementer, using only approved normative specifications and explicitly referenced normative artifacts, can:

1. Construct exactly one Constitution Artifact from the authoritative Constitution source.
2. Derive exactly one canonical Constitution Vector representation.
3. Serialize the result into exactly one canonical byte sequence.
4. Reproduce the same SHA-256 values.
5. Establish identity and lineage.
6. Verify registration and frozen status.
7. Complete all of the above without inspecting any Reference Implementation.

Any legitimate multi-outcome path is a FAIL condition for readiness.

---

## 9. Formal SPEC-002 Readiness Status

**SPEC-002 READINESS STATUS: NOT READY**

Rationale:

- APS-001 remains incomplete and upstream normative authority is still blocked by documented gaps.
- The architectural decisions listed in §6 are unresolved.
- Existing normative sources establish the need for determinism, traceability, versioning, integrity, and independent verification, but they do not yet establish one canonical Constitution Artifact construction procedure.
- Until the unresolved decisions are approved and folded into a complete normative contract, independent implementations could legitimately diverge.

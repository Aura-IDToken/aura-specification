# SPEC-002 — Constitution Artifact Contract

Document ID: SPEC-002
Version: 0.3-DRAFT
Status: DRAFT
Classification: Normative Contract for Constitution Artifact Specification
Owner: Protocol Custodian
Authority: AURA Constitution v1.0 (FROZEN) · APS-000 · APS-200 · APS-300 · APS-400 · APS-900
Last Review: 2026-08-10

**Normative effect: NONE until APPROVED.**
No requirement in this document, including any REQ-002-* identifier, constitutes an approved architectural or implementation decision while this document remains in DRAFT status. All requirements defined herein express what a future normative specification MUST determine; they do not themselves constitute that determination.

---

> **DRAFT ONLY / SPECIFICATION WORK**
> This document defines the contract surface for a future Constitution Artifact and Constitution Vector specification. It MUST NOT be used to implement, generate, register, or freeze a Constitution Artifact or Constitution Vector until all blocking architectural decisions are explicitly approved and this document has advanced beyond DRAFT through the proper governance mechanism.

---

## Governing Direction

The direction of authority in this specification is:

```
normative requirement
        ↓
architecture decision
        ↓
approved specification
        ↓
implementation
        ↓
conformance evidence
```

This direction MUST NOT be reversed. Implementation behaviour does not constitute normative evidence unless an approved governance artifact explicitly grants that implementation normative authority.

---

## 1. Purpose

SPEC-002 defines the normative contract surface that a future approved specification MUST address in order to make Constitution Artifact construction deterministic and independently reproducible.

This document does not itself approve any algorithm, encoding, format, numeric representation, dictionary, serialization convention, hash formula, or implementation behavior. It identifies what an approved normative source MUST decide before any Constitution Artifact construction can be considered deterministic and verifiable.

---

## 2. Scope and Non-Goals

### 2.1 Scope

SPEC-002 covers the required contract surface for:

- Source Set, Source Boundary, and Source Document Identity
- Source Version, Source Status, Source Encoding
- Source Canonicalization and Inclusion/Exclusion Boundaries
- Source Integrity Reference
- Transformation Pipeline
- Normalization Rules
- Embedding Method Identity
- Dictionary or Embedding Dependency Identity and Versioning
- Numeric Representation of Vector Values
- Constitution Document Identity
- Constitution Artifact Identity
- Constitution Vector Identity
- Execution / Commit Provenance Identity
- Inter-Identity Binding Fields
- Hash Domain Definitions
- Canonical Serialization
- Canonical Byte Sequence
- Artifact-to-Source Binding
- Artifact-to-Vector Binding
- Provenance Binding
- Versioning
- Lineage and `supersedes`
- Registration
- Freeze
- Positive Determinism Verification
- Negative Integrity Verification
- Failure Conditions

### 2.2 Non-Goals

This document MUST NOT:

- Modify `aura-poc-a-core-v3.3`
- Modify `aura-guard-v1.3`
- Implement CR-007
- Generate a Constitution Vector
- Generate a Constitution Artifact
- Create or register `constitution.json`, `vector.json`, or any equivalent canonical artifact
- Create canonical fixtures
- Calculate or publish any hash value
- Approve any hash formula, serialization format, or numeric representation
- Treat any unapproved alias as equivalent to the authoritative Constitution identifier
- Treat `AURA-CONSTITUTION-001` as equivalent to `AURA-CON-001` unless an approved governance artifact explicitly establishes that relationship
- Promote candidate architectural decisions to normative requirements without explicit governance authority
- Resolve contradictions by assumption; contradictions MUST be recorded as UNRESOLVED or EVIDENCE GAP

---

## 3. Governing Constraints

1. The contract defined by SPEC-002 MUST preserve **Specification First** and **Architecture Before Implementation** per AURA Constitution Article IV.
2. The contract MUST fail closed when any required input, dependency, identity binding, or verification step is ambiguous, missing, or inconsistent.
3. Any algorithmic degree of freedom that could allow two conformant implementations to produce different vectors, different canonical bytes, or different hashes MUST be eliminated before SPEC-002 can become READY.
4. Candidate choices including `32`, `100000`, `signed int32`, `little-endian`, `Dictionary-Based Embedding`, and `round-half-to-even` are non-normative in this draft unless and until explicit architectural authority approves them. **No candidate choice listed in this document constitutes a recommendation, preference, default, or implied architectural decision.**
5. If an existing normative source is insufficient to resolve a requirement, the gap MUST be recorded as UNRESOLVED or EVIDENCE GAP. It MUST NOT be resolved by assumption or by reference to implementation behaviour.

---

## 4. Normative Contract Requirements

### 4.1 Source Boundary

The future normative specification MUST explicitly define all of the following. SPEC-002 MUST NOT assume any particular answer to any of these questions.

- **REQ-002-001**: The future specification MUST define the exact **Source Set**: which documents, files, or data constitute the authoritative input to Constitution Artifact construction.
- **REQ-002-002**: The future specification MUST define the exact **Source Boundary**: the precise inclusion and exclusion rules that determine what is and is not part of the authoritative source.
- **REQ-002-003**: The future specification MUST define **Source Document Identity**: the immutable identifier, version, status, and repository location of each document in the Source Set.
- **REQ-002-004**: The future specification MUST define **Source Version** semantics and which version of each Source Document is authoritative.
- **REQ-002-005**: The future specification MUST define **Source Status** constraints: which document lifecycle statuses are permissible as inputs.
- **REQ-002-006**: The future specification MUST define **Source Encoding**: the source-level canonicalization rules for each source document, covering as applicable character encoding, BOM handling, line-ending normalization, Unicode normalization form, and source-to-byte conversion. Source-level encoding requirements concern source material only and MUST NOT be conflated with numeric byte-order or endianness, which belong to the numeric/vector representation contract under REQ-002-014.
- **REQ-002-007**: The future specification MUST define **Source Canonicalization**: the deterministic procedure that transforms source documents into a canonical form prior to any further processing, or MUST explicitly declare that the authoritative source is already canonical.
- **REQ-002-008**: The future specification MUST define **Source Integrity Reference**: the cryptographic or integrity-binding mechanism that ties the authoritative source identity to artifact construction.
- **REQ-002-009**: Any alternate label, filename, alias, or informal name MUST be treated as distinct from the authoritative identifier unless an approved governance artifact explicitly establishes equivalence. In particular, the identifier `AURA-CON-001` MUST NOT be silently replaced, aliased, or equated with `AURA-CONSTITUTION-001` without such explicit approval.

> **ARCHITECTURE NOTE — Source Boundary is UNRESOLVED (AD-CA-001).**
> The future normative specification MUST NOT assume that the source is: only `AURA_CONSTITUTION.md`; Constitution plus APS documents; the entire repository; or any other collection of files. The exact source boundary is an explicit architectural decision that remains unresolved.

### 4.2 Canonicalization, Transformation, and Normalization

- **REQ-002-010**: The future specification MUST define the complete ordered transformation pipeline from authoritative source to artifact-ready intermediate representation, including each step, its inputs, its outputs, and its step boundaries.
- **REQ-002-011**: The future specification MUST define all normalization rules that affect the intermediate representation, including whitespace treatment, line-ending treatment, encoding normalization, heading treatment, metadata treatment, and all inclusion/exclusion boundaries.

### 4.3 Embedding, Dictionary, and Numeric Representation

- **REQ-002-012**: The future specification MUST identify exactly one embedding method by immutable identifier, version, and status.
- **REQ-002-013**: The future specification MUST define the dictionary or equivalent embedding dependency by immutable identifier, version, status, and integrity binding, or MUST explicitly state that no external dictionary is permitted.
- **REQ-002-014**: The future specification MUST define one numeric representation for vector values, including domain, width, sign, scale, rounding behavior, overflow behavior, and byte order where applicable. Candidate values (`32`, `100000`, `signed int32`, `little-endian`, `round-half-to-even`) remain unapproved until an explicit architecture decision is made.

### 4.4 Identity Separation

The future normative specification MUST explicitly define and maintain separate identities for each of the following. These identities MUST NOT be collapsed into a single identifier without an explicit approved architecture decision.

**A. Constitution Document Identity**
The identity of the authoritative normative source document, as defined under §4.1 (Source Boundary).

**B. Constitution Artifact Identity**
The identity of the constructed artifact: the output of applying the approved transformation pipeline to the authoritative Constitution source.

**C. Constitution Vector Identity**
The identity of the Constitution Vector derived from the Constitution Artifact via the approved embedding and numeric representation procedures.

**D. Execution / Commit Provenance Identity**
The identity of the specific construction event: repository revision, execution context, and deterministic generation context required for independent reproduction.

The conceptual relationship between these identities is:

```
Constitution Document Identity
        ↓
Constitution Artifact Identity
        ↓
Constitution Vector Identity

Execution / Commit Identity
        ↓
provenance binding
```

The following terms MUST NOT be used interchangeably. Each has a distinct meaning:

- **Identity** — identifies a distinct entity (document, artifact, vector, or construction event)
- **Integrity** — verifies that a representation or content has not been altered
- **Provenance** — identifies the context in which an artifact was constructed
- **Lineage** — describes the succession relationship between artifacts (e.g., `supersedes`)
- **Status** — describes the lifecycle state of an artifact (e.g., DRAFT, FROZEN)

The future normative specification MUST define each concept independently and MUST NOT make them synonyms.

- **REQ-002-015**: The future specification MUST NOT equate or merge Constitution Document Identity, Artifact Identity, Vector Identity, and Provenance Identity (e.g., `constitution_id = artifact_id = vector_id`) unless a future approved architecture decision explicitly establishes such equivalence.
- **REQ-002-016**: The future specification MUST specify which fields bind these identities together.

### 4.5 Hash Domains

The future normative specification MUST define each hash domain completely and independently. Hash domain definitions MUST be independently reproducible without reference to any implementation.

There MUST be at minimum a Vector Hash domain and an Artifact Hash domain. However, the future specification is NOT restricted to exactly these two domains; it MUST explicitly define every hash domain it uses and MUST NOT silently rely on additional undeclared domains.

- **REQ-002-017**: The future specification MUST explicitly define the **Vector Hash** domain: the exact bytes that constitute the hash input, the serialization that precedes hashing, the hash algorithm, the output encoding, and the output representation.
- **REQ-002-018**: The future specification MUST explicitly define the **Artifact Hash** domain: the exact bytes that constitute the hash input, the serialization that precedes hashing, the hash algorithm, the output encoding, and the output representation.
- **REQ-002-019**: The future specification MUST explicitly state which fields are included in and excluded from each hash input.
- **REQ-002-020**: Hash domain definitions MUST be sufficient for an independent implementer to reproduce the exact byte sequence fed to each hash function without inspecting any Reference Implementation.

For each hash domain the future specification MUST define:

- exact input representation
- exact byte sequence within that domain
- included fields
- excluded fields
- serialization
- algorithm
- output encoding
- output representation

> **ARCHITECTURE NOTE — Hash Domains are UNRESOLVED (AD-CA-007, AD-CA-008).**
> This draft MUST NOT itself approve any concrete hash formula such as `VECTOR HASH = SHA-256(canonical_vector_bytes)` or `ARTIFACT HASH = SHA-256(canonical_artifact_bytes)`. Such formulas do not exist in any approved normative source and remain unresolved. The future architecture decision MUST define each hash domain completely.
>
> **Governing principle:** Hash domain MUST be explicitly defined and independently reproducible.

### 4.6 Canonical Serialization and Byte Sequence

- **REQ-002-021**: The future specification MUST define exactly one canonical serialization format for the Constitution Vector and Constitution Artifact, including field set, field order, encoding, and representation of absent or optional fields.
- **REQ-002-022**: The future specification MUST define exactly one canonical byte sequence for each defined hash-bearing Constitution Artifact and Constitution Vector representation within its respective hash domain. The canonical byte sequence for the Constitution Artifact and the canonical byte sequence for the Constitution Vector are SEPARATE definitions within their respective hash domains and MUST NOT be treated as a single universal byte sequence for the system.

  The future specification MUST explicitly define for each representation:
  - the representation-to-bytes transformation
  - field ordering where applicable
  - encoding
  - numeric representation where applicable
  - absent or optional field handling
  - byte-level boundaries
  - hash-domain membership

### 4.7 Artifact and Vector Binding

- **REQ-002-023**: The future specification MUST define the required binding from authoritative source to Constitution Artifact, including source identifier, source version, source status, source location, and source integrity reference.
- **REQ-002-024**: The future specification MUST define the required binding from Constitution Artifact to Constitution Vector, including vector identity, dependency identities, canonical bytes reference, and integrity reference.
- **REQ-002-025**: The future specification MUST define the required commit/execution provenance binding for artifact construction, including the repository revision and the deterministic generation context needed for independent verification.

### 4.7a Provenance / Determinism Boundary

Execution and commit provenance MUST NOT silently introduce variation into the canonical Constitution Artifact, Constitution Vector, canonical byte sequences, or hash values.

- **REQ-002-033**: The future specification MUST explicitly define whether execution / commit provenance is included in, excluded from, or externally bound to the canonical Constitution Artifact representation and its applicable hash domain(s). The future specification MUST define the exact fields and binding semantics used for provenance verification. The definition MUST prevent provenance semantics from introducing unintended non-determinism into canonical artifact, vector, canonical byte sequence, or hash reproduction.

  This requirement does NOT mandate inclusion or exclusion of provenance from any hash domain. It requires only that the future specification make the boundary explicit and independently reproducible.

> **ARCHITECTURE NOTE — Provenance boundary is UNRESOLVED (AD-CA-010).**
> The question of whether execution / commit provenance belongs to (A) canonical artifact identity / canonical bytes / hash domain, (B) external provenance evidence / binding, or (C) another explicitly defined domain is an architectural decision that remains unresolved. SPEC-002 MUST NOT choose the answer.

### 4.7b Dependency Closure

- **REQ-002-034**: The future specification MUST define the complete dependency closure of Constitution Artifact construction. Every external or auxiliary dependency capable of affecting the canonical artifact, vector, canonical byte sequence, or hash MUST be explicitly identified, versioned where applicable, integrity-bound, and included in the reproducibility contract.

  The requirement covers, where applicable:
  - embedding method
  - dictionary
  - dictionary version
  - dictionary integrity reference
  - normalization tables
  - mapping tables
  - configuration
  - constants
  - Unicode / versioned transformation data
  - any other deterministic input affecting the output

  The specification MUST NOT permit an undeclared dependency to alter the canonical result.

> **ARCHITECTURE NOTE — Dependency closure affects AD-CA-006 (dictionary identity, versioning, integrity) and AD-CA-005 (embedding method). These decisions remain UNRESOLVED.**

### 4.8 Versioning and Lineage

- **REQ-002-026**: The future specification MUST define versioning rules for the Constitution Artifact and Constitution Vector that are consistent with repository lifecycle rules and immutable artifact principles.
- **REQ-002-027**: The future specification MUST define lineage fields, including `supersedes` semantics and the conditions under which a new artifact supersedes an older artifact.

### 4.9 Registration

Registration and Freeze are separate governance concepts. Registration MUST NOT automatically imply Freeze. Freeze MUST NOT be assumed merely because an artifact is registered.

- **REQ-002-028**: The future specification MUST define registration requirements independently of freeze requirements, including:
  - The authoritative registry and its location
  - Required registry fields
  - Required integrity checks at registration time
  - Required identity checks at registration time
  - Required provenance checks at registration time

### 4.10 Freeze

- **REQ-002-029**: The future specification MUST define freeze requirements independently of registration requirements, including:
  - The authority who may authorize freeze
  - The status transition that constitutes freeze
  - The evidence required prior to freeze authorization
  - The immutability semantics of frozen status
  - The verification procedure for confirming frozen status

### 4.11 Verification and Failure Conditions

- **REQ-002-030**: The future specification MUST define an independent verification procedure that does not require inspection of any Reference Implementation, including `aura-poc-a-core-v3.3`, `aura-guard-v1.3`, or any other implementation-specific source code.
- **REQ-002-031**: The future specification MUST define failure conditions that invalidate the Constitution Artifact, the Constitution Vector, registration, or frozen status. At minimum the future specification MUST explicitly address whether each of the following conditions causes rejection, and MUST NOT permit silent fallback where that fallback could change the canonical result:

  - invalid authoritative source
  - missing source
  - ambiguous source boundary
  - unsupported encoding
  - missing dependency
  - unapproved dependency
  - dependency integrity mismatch
  - unknown dependency version
  - malformed dictionary or equivalent dependency
  - numeric overflow
  - numeric out-of-domain value
  - invalid canonicalization input
  - invalid transformation input
  - invalid provenance binding
  - hash mismatch
  - identity mismatch
  - lineage inconsistency
  - registration inconsistency
  - frozen-status inconsistency

  **The governing principle is: NO SILENT FALLBACK WHERE IT CAN ALTER THE CANONICAL RESULT.**
- **REQ-002-032**: The future specification MUST remain NOT READY if any conformant independent implementation can legitimately produce more than one vector, more than one canonical byte sequence, or more than one hash value from the same authoritative source and approved dependencies.

---

## 5. Verification Model

### 5.1 Positive Determinism Verification

An independent implementation, using only approved normative specifications and explicitly referenced normative artifacts, MUST satisfy the following chain without requiring inspection of any Reference Implementation:

```
same authoritative source
        ↓
same Constitution Artifact
        ↓
same Constitution Vector
        ↓
same canonical bytes
        ↓
same hash values
```

The PASS condition requires that any two conformant independent implementations produce identical artifacts, vectors, canonical byte sequences, and hash values from the same authoritative source and approved dependencies.

### 5.2 Negative Integrity Verification

The verification model MUST also verify the rejection of altered inputs or artifacts. The future normative specification MUST define tests covering at minimum:

1. **Modified authoritative source** → verification failure
2. **Modified Constitution Artifact** → artifact integrity/identity failure
3. **Modified Constitution Vector** → vector integrity/identity failure
4. **Modified dictionary or embedding dependency** → dependency/integrity failure
5. **Wrong provenance / repository revision / execution binding** → provenance verification failure
6. **Ambiguous or unapproved dependency** → fail closed
7. **Numeric overflow or invalid numeric value** → deterministic rejection
8. **Serialization alteration** → hash/integrity failure
9. **Lineage inconsistency** → verification failure
10. **Registration inconsistency** → registration verification failure
11. **Frozen-status inconsistency** → freeze verification failure

### 5.3 Distinction: Determinism vs. Integrity

These are separate properties and MUST NOT be conflated:

**DETERMINISM**: same valid inputs → same valid outputs

**INTEGRITY**: modified or invalid inputs → detectable verification failure

A specification that achieves determinism but not integrity, or integrity but not determinism, is incomplete. Both properties MUST be independently specified and independently verifiable.

It is an explicit requirement that the provenance boundary definition (REQ-002-033) does not make execution context a hidden source of canonical-result variation. Provenance information MUST NOT alter the canonical Constitution Artifact, canonical byte sequences, or hash values except through an explicitly defined, normatively approved mechanism.

---

## 6. Explicit Unresolved Architectural Decisions

The following items are unresolved architectural decision domains. The identifiers below are local placeholders for this draft only and MUST be replaced by approved architecture decisions before SPEC-002 advances beyond DRAFT. **No candidate choice listed in this table constitutes a recommendation, preference, default, or implied architectural decision.**

| Placeholder | Decision Domain | Current Status | Candidate Choices (Non-Normative) | Blocking Effect |
|---|---|---|---|---|
| AD-CA-001 | Authoritative Constitution source identity, Source Set, and exact Source Boundary | UNRESOLVED | None approved | Blocks REQ-002-001 through REQ-002-011 |
| AD-CA-002 | Canonicalization procedure for the authoritative Constitution source | UNRESOLVED | None approved | Blocks REQ-002-007, REQ-002-010, REQ-002-011 |
| AD-CA-003 | Transformation pipeline from source to artifact-ready representation | UNRESOLVED | None approved | Blocks REQ-002-010, REQ-002-011 |
| AD-CA-004 | Normalization rules affecting deterministic output | UNRESOLVED | None approved | Blocks REQ-002-011, REQ-002-021, REQ-002-022 |
| AD-CA-005 | Embedding method identity and versioning model | UNRESOLVED | `Dictionary-Based Embedding` is candidate only | Blocks REQ-002-012, REQ-002-016, REQ-002-024 |
| AD-CA-006 | Dictionary identity, versioning, integrity, change policy, and complete dependency closure of all external or auxiliary inputs capable of affecting canonical artifact, vector, bytes, or hash | UNRESOLVED | None approved | Blocks REQ-002-013, REQ-002-016, REQ-002-024, REQ-002-034 |
| AD-CA-007 | Numeric representation of vector values | UNRESOLVED | `32`, `100000`, `signed int32`, `little-endian`, `round-half-to-even` are candidate only | Blocks REQ-002-014, REQ-002-017 through REQ-002-022 |
| AD-CA-008 | Canonical serialization format, canonical byte sequence, and hash domain definitions | UNRESOLVED | None approved | Blocks REQ-002-017 through REQ-002-022 |
| AD-CA-009 | Constitution Document Identity, Artifact Identity, Vector Identity schema and inter-identity binding fields | UNRESOLVED | None approved | Blocks REQ-002-015, REQ-002-016, REQ-002-023, REQ-002-024 |
| AD-CA-010 | Commit/execution provenance binding schema, and explicit definition of whether provenance is included in, excluded from, or externally bound to the canonical Constitution Artifact representation and its applicable hash domain(s) | UNRESOLVED | None approved | Blocks REQ-002-025, REQ-002-030, REQ-002-031, REQ-002-033 |
| AD-CA-011 | Registration model, authoritative registry, registry fields, and registration integrity semantics | UNRESOLVED | None approved | Blocks REQ-002-028, REQ-002-030, REQ-002-031 |
| AD-CA-012 | Freeze evidence, frozen-status verification model, and immutability semantics | UNRESOLVED | None approved | Blocks REQ-002-029 through REQ-002-031 |

---

## 7. Traceability Matrix

The following matrix uses mechanically addressable references. Where a Conformance Test ID or Evidence ID does not yet exist, it is marked as FUTURE REF (not yet assigned). Broad normative source references alone are insufficient; section-level citations are required where available.

| Req ID | Requirement Summary | Source Doc ID | Source Version | Source Section / Clause | Architecture Decision ID | Conformance Test ID | Evidence ID |
|---|---|---|---|---|---|---|---|
| REQ-002-001 | Define exact Source Set | AURA-CON-001 | v1.0-FROZEN | Article IV Principles 8–10 | AD-CA-001 | FUTURE REF | FUTURE REF |
| REQ-002-002 | Define exact Source Boundary | AURA-CON-001; APS-000 | v1.0-FROZEN; current | Article IV P8; §4 | AD-CA-001 | FUTURE REF | FUTURE REF |
| REQ-002-003 | Define Source Document Identity | APS-000 | current | §4, §7 | AD-CA-001 | FUTURE REF | FUTURE REF |
| REQ-002-004 | Define Source Version semantics | VERSIONING.md | current | §3–§4 | AD-CA-001 | FUTURE REF | FUTURE REF |
| REQ-002-005 | Define Source Status constraints | VERSIONING.md | current | §3 | AD-CA-001 | FUTURE REF | FUTURE REF |
| REQ-002-006 | Define Source Encoding | AURA-CON-001 | v1.0-FROZEN | Article IV P2, P8 | AD-CA-002 | FUTURE REF | FUTURE REF |
| REQ-002-007 | Define Source Canonicalization | AURA-CON-001; APS-200 | v1.0-FROZEN; current | Article IV P1,P2,P8; §8 | AD-CA-002 | FUTURE REF | FUTURE REF |
| REQ-002-008 | Define Source Integrity Reference | APS-000 | current | §7 | AD-CA-001, AD-CA-002 | FUTURE REF | FUTURE REF |
| REQ-002-009 | Alias equivalence requires explicit approval | AURA-CON-001; APS-000 | v1.0-FROZEN; current | Article IV P8; §4 | AD-CA-001 | FUTURE REF | FUTURE REF |
| REQ-002-010 | Complete ordered transformation pipeline | AURA-CON-001 | v1.0-FROZEN | Article IV P1,P2,P8,P10 | AD-CA-003 | FUTURE REF | FUTURE REF |
| REQ-002-011 | Explicit normalization rules | AURA-CON-001; APS-200 | v1.0-FROZEN; current | Article IV P2,P8; §8 | AD-CA-004 | FUTURE REF | FUTURE REF |
| REQ-002-012 | One embedding method identity and version | AURA-CON-001 | v1.0-FROZEN | Article IV P1,P2,P8,P9 | AD-CA-005 | FUTURE REF | FUTURE REF |
| REQ-002-013 | Dictionary identity, version, and integrity binding | AURA-CON-001; APS-000 | v1.0-FROZEN; current | Article IV P9; §7 | AD-CA-006 | FUTURE REF | FUTURE REF |
| REQ-002-014 | One numeric representation | AURA-CON-001 | v1.0-FROZEN | Article IV P2,P8 | AD-CA-007 | FUTURE REF | FUTURE REF |
| REQ-002-015 | No collapse of Document / Artifact / Vector / Provenance identities | APS-000 | current | §4 | AD-CA-009 | FUTURE REF | FUTURE REF |
| REQ-002-016 | Inter-identity binding fields | APS-000 | current | §4, §7 | AD-CA-009 | FUTURE REF | FUTURE REF |
| REQ-002-017 | Vector Hash domain definition | APS-200; APS-300 | current | §4; §5, §9 | AD-CA-007, AD-CA-008 | FUTURE REF | FUTURE REF |
| REQ-002-018 | Artifact Hash domain definition | APS-200; APS-300 | current | §4; §5, §9 | AD-CA-007, AD-CA-008 | FUTURE REF | FUTURE REF |
| REQ-002-019 | Hash input field inclusion/exclusion | APS-200; APS-300 | current | §4; §5 | AD-CA-008 | FUTURE REF | FUTURE REF |
| REQ-002-020 | Hash domain independently reproducible | AURA-CON-001 | v1.0-FROZEN | Article IV P2,P8 | AD-CA-008 | FUTURE REF | FUTURE REF |
| REQ-002-021 | One canonical serialization format | APS-200 | current | §8 | AD-CA-008 | FUTURE REF | FUTURE REF |
| REQ-002-022 | One canonical byte sequence per hash domain, per representation | APS-200; APS-300 | current | §4; §5 | AD-CA-008 | FUTURE REF | FUTURE REF |
| REQ-002-023 | Source-to-artifact binding | APS-900 | current | §3–§4 | AD-CA-001, AD-CA-002, AD-CA-009 | FUTURE REF | FUTURE REF |
| REQ-002-024 | Artifact-to-vector binding | APS-900 | current | §3–§4 | AD-CA-005, AD-CA-006, AD-CA-007, AD-CA-009 | FUTURE REF | FUTURE REF |
| REQ-002-025 | Commit/execution provenance binding | AURA-CON-001; APS-900; APS-950 | v1.0-FROZEN; current; current | Article X; §2,§4; §6 | AD-CA-010 | FUTURE REF | FUTURE REF |
| REQ-002-026 | Versioning rules | AURA-CON-001; VERSIONING.md | v1.0-FROZEN; current | Article IV P9; §3–§4, §9 | — | FUTURE REF | FUTURE REF |
| REQ-002-027 | Lineage and `supersedes` semantics | VERSIONING.md; AURA-CON-001 | current; v1.0-FROZEN | §3; Article XI | AD-CA-009, AD-CA-011, AD-CA-012 | FUTURE REF | FUTURE REF |
| REQ-002-028 | Registration model, registry fields, and registration integrity | APS-000; APS-900 | current | §7; §4 | AD-CA-011 | FUTURE REF | FUTURE REF |
| REQ-002-029 | Freeze requirements and frozen-status verification | AURA-CON-001; VERSIONING.md | v1.0-FROZEN; current | Article VIII, XI; §3 | AD-CA-012 | FUTURE REF | FUTURE REF |
| REQ-002-030 | Independent verification procedure | AURA-CON-001; APS-300; APS-900 | v1.0-FROZEN; current; current | Article III, IV P2,P4,P8; §9; §9 | AD-CA-010, AD-CA-011, AD-CA-012 | FUTURE REF | FUTURE REF |
| REQ-002-031 | Failure conditions | AURA-CON-001; APS-300 | v1.0-FROZEN; current | Article IV P6; §12 | AD-CA-010, AD-CA-011, AD-CA-012 | FUTURE REF | FUTURE REF |
| REQ-002-032 | NOT READY until one outcome is forced | AURA-CON-001 | v1.0-FROZEN | Article IV P1,P2,P8 | All unresolved decisions above | FUTURE REF | FUTURE REF |
| REQ-002-033 | Provenance boundary explicitly defined relative to canonical artifact and hash domain(s) | AURA-CON-001; APS-900; APS-950 | v1.0-FROZEN; current; current | Article IV P2,P8; Article X; §2,§4; §6 | AD-CA-010 | FUTURE REF | FUTURE REF |
| REQ-002-034 | Complete dependency closure of artifact construction | AURA-CON-001; APS-000 | v1.0-FROZEN; current | Article IV P1,P2,P8,P9; §7 | AD-CA-005, AD-CA-006 | FUTURE REF | FUTURE REF |

The complete traceability chain MUST be:

```
Requirement
    ↓
Normative Source (Source Doc ID · Version · Section)
    ↓
Architecture Decision (AD-CA-xxx)
    ↓
Conformance Test (CONF-xxx — FUTURE REF where not yet assigned)
    ↓
Evidence (EVID-xxx — FUTURE REF where not yet assigned)
    ↓
Release / Artifact
```

Test IDs and Evidence IDs MUST NOT be invented to make the matrix appear complete. They are marked FUTURE REF until properly assigned through the governance process.

---

## 8. Registration vs. Freeze Distinction

Registration and Freeze are separate governance concepts governed by independent requirements (§4.9 and §4.10). This section records the governing distinction.

**REGISTRATION** is the act of recording an artifact in an authoritative registry. Registration:
- Requires defined registry fields, integrity checks, identity checks, and provenance checks (REQ-002-028)
- Does NOT automatically imply that the artifact is frozen
- Does NOT prevent subsequent modification of a non-frozen artifact in ways permitted by its current lifecycle status

**FREEZE** is the act of placing an artifact into an immutable state. Freeze:
- Requires authorized authority, a defined status transition, required evidence, and a verification procedure for confirming frozen status (REQ-002-029)
- Does NOT occur automatically as a consequence of registration
- MUST NOT be assumed merely because an artifact is registered

Both concepts MUST be independently defined in the future normative specification. The architecture decisions governing each (AD-CA-011 for registration; AD-CA-012 for freeze) are independent and MUST be resolved independently.

---

## 9. Acceptance Criteria

SPEC-002 MAY advance from DRAFT only when all of the following are true:

1. Every requirement in §4 is backed either by an existing approved normative source or by a newly approved architecture decision incorporated into this specification.
2. The authoritative Constitution source, Source Set, and Source Boundary are uniquely identified and normatively fixed (AD-CA-001 resolved).
3. Canonicalization, transformation, normalization, embedding, dictionary dependency, numeric representation, serialization, canonical byte sequence, and all hash domain definitions are each normatively reduced to exactly one valid interpretation.
4. Constitution Document Identity, Artifact Identity, Vector Identity, and Provenance Identity are separately defined, with explicit inter-identity binding fields.
5. Artifact identity, vector identity, lineage, `supersedes`, registration, and frozen-status verification are completely specified and independently checkable.
6. The independent verification procedure (§5) can be executed without inspecting any Reference Implementation.
7. A formal Independent Implementer Test is defined and its PASS condition requires that two conformant independent implementations produce the same artifact, the same vector, the same canonical bytes, and the same hash values from the same authoritative source and approved dependencies.
8. Positive Determinism Verification (§5.1) and Negative Integrity Verification (§5.2) are both fully specified as independent properties.
9. If any conformant independent implementation can still legitimately produce different vectors, canonical bytes, or hashes, SPEC-002 MUST remain NOT READY.
10. **Source Boundary** is fully resolved.
11. **Dependency Closure** is fully resolved (REQ-002-034; AD-CA-005, AD-CA-006).
12. **Provenance boundary** is fully resolved (REQ-002-033; AD-CA-010): the relationship between execution/commit provenance and the canonical artifact representation and its hash domain is explicitly defined.
13. **Hash domains** are fully resolved: every hash domain used by the future specification is completely and independently defined.
14. **Canonical byte sequence semantics** are fully resolved: exactly one canonical byte sequence is defined per hash domain per representation.
15. **Failure / rejection semantics** are fully specified: no silent fallback is permitted where that fallback could alter the canonical result.
16. **Identity separation** is preserved: identity, integrity, provenance, lineage, and status remain separately defined concepts.

The central binary criterion remains:

> Can two independent conformant implementations, using only the approved normative specification and its explicitly referenced normative dependencies, construct the same canonical artifact, derive the same vector, produce the same canonical bytes, and reproduce the same hash values?

If not: **SPEC-002 = NOT READY.**

---

## 10. Independent Implementer Test

The Independent Implementer Test for SPEC-002 is satisfied only if an independent implementer, using ONLY:

- approved normative specifications;
- explicitly referenced normative artifacts;
- approved architecture decisions;
- approved fixtures where applicable;

can satisfy ALL of the following:

```
ONE VALID INPUT SET
        ↓
ONE VALID ARTIFACT
        ↓
ONE VALID VECTOR
        ↓
ONE VALID BYTE SEQUENCE
        ↓
ONE VALID HASH SET
```

Specifically, the independent implementer MUST be able to:

1. Construct exactly one Constitution Artifact from the authoritative Constitution source.
2. Derive exactly one canonical Constitution Vector representation.
3. Serialize the result into exactly one canonical byte sequence.
4. Reproduce the same hash values.
5. Establish identity and lineage.
6. Verify registration and frozen status.
7. Complete all of the above without inspecting any Reference Implementation.

The independent implementer MUST NOT need to inspect:
- `aura-poc-a-core-v3.3`
- `aura-guard-v1.3`
- any other Reference Implementation
- implementation-specific source code

Any legitimate multi-outcome path is a FAIL condition for readiness.

---

## 11. Formal SPEC-002 Readiness Status

**SPEC-002 READINESS STATUS: NOT READY**

Rationale:

- APS-001 remains incomplete and upstream normative authority is still blocked by documented gaps.
- All twelve architectural decision domains listed in §6 (AD-CA-001 through AD-CA-012) are UNRESOLVED.
- Existing normative sources establish the need for determinism, traceability, versioning, integrity, and independent verification, but they do not yet establish one canonical Constitution Artifact construction procedure.
- Until the unresolved decisions are approved and folded into a complete normative contract, independent implementations could legitimately diverge.
- SPEC-002 will NOT advance to READY merely because this document is internally well structured. Readiness requires every architectural decision required to make the future Constitution Artifact independently reproducible to be explicitly resolved through the proper governance mechanism.
- No Constitution Artifact was created or generated as a result of this document.
- No Constitution Vector was created or generated as a result of this document.
- No implementation was modified as a result of this document.
- CR-007 remains BLOCKED.

---

## Appendix A — Required Confirmations

**A. Document Status**
SPEC-002 remains DRAFT. Version 0.3-DRAFT. No normative effect.

**B. CR-007 Status**
CR-007 remains BLOCKED. No requirement in SPEC-002 constitutes approval or unblocking of CR-007.

**C. No Artifact Created**
No Constitution Artifact and no Constitution Vector was created, generated, registered, or frozen by this document or by the revision producing version 0.3-DRAFT.

**D. No Implementation Modified**
No core implementation (`aura-poc-a-core-v3.3`) and no guard implementation (`aura-guard-v1.3`) was modified by this revision.

**E. Unresolved AD-CA Decision Domains**
The following decision domains remain explicitly unresolved:

- AD-CA-001: Authoritative Constitution source identity, Source Set, and exact Source Boundary
- AD-CA-002: Canonicalization procedure for the authoritative Constitution source
- AD-CA-003: Transformation pipeline from source to artifact-ready representation
- AD-CA-004: Normalization rules affecting deterministic output
- AD-CA-005: Embedding method identity and versioning model
- AD-CA-006: Dictionary identity, versioning, integrity, and change policy
- AD-CA-007: Numeric representation of vector values
- AD-CA-008: Canonical serialization format, canonical byte sequence, and hash domain definitions
- AD-CA-009: Constitution Document Identity, Artifact Identity, Vector Identity schema and inter-identity binding fields
- AD-CA-010: Commit/execution provenance binding schema
- AD-CA-011: Registration model, authoritative registry, registry fields, and registration integrity semantics
- AD-CA-012: Freeze evidence, frozen-status verification model, and immutability semantics

---

## Appendix B — Change Summary (v0.1-DRAFT → v0.2-DRAFT)

1. **Source Boundary tightening**: §4.1 replaced with a dedicated Source Boundary section (REQ-002-001 through REQ-002-009) explicitly requiring definition of Source Set, Source Boundary, Source Document Identity, Source Version, Source Status, Source Encoding, Source Canonicalization, and Source Integrity Reference. Added explicit prohibition against silently equating `AURA-CON-001` with `AURA-CONSTITUTION-001`.

2. **Identity separation**: §4.4 added, requiring explicit separation of Constitution Document Identity, Constitution Artifact Identity, Constitution Vector Identity, and Execution/Commit Provenance Identity (REQ-002-015, REQ-002-016). Identity collapse is explicitly prohibited without approved architecture decision.

3. **Hash-domain separation**: §4.5 added, requiring separately and completely defined hash domains for Vector Hash and Artifact Hash (REQ-002-017 through REQ-002-020). Explicit prohibition on approving concrete hash formulas within this DRAFT document.

4. **Positive verification**: §5.1 added, formalizing the Positive Determinism Verification chain.

5. **Negative verification**: §5.2 added, formalizing six Negative Integrity Verification test categories. §5.3 added, explicitly distinguishing DETERMINISM from INTEGRITY as separate required properties.

6. **Candidate-decision protection**: §3 constraint 4 and §6 table both carry explicit statement: "No candidate choice listed in this document constitutes a recommendation, preference, default, or implied architectural decision."

7. **Traceability tightening**: §7 expanded to mechanically addressable fields: Source Doc ID, Source Version, Source Section/Clause, Requirement ID, Architecture Decision ID, Conformance Test ID, Evidence ID. FUTURE REF used where test IDs and evidence IDs do not yet exist. Traceability chain added explicitly.

8. **Registration/freeze separation**: §4.9 and §4.10 separated into distinct subsections with independent requirement sets. §8 added as a dedicated section recording the governing distinction.

---

## Appendix C — Change Summary (v0.2-DRAFT → v0.3-DRAFT)

1. **Provenance / determinism boundary tightening**: §4.7a added. REQ-002-033 added, requiring the future specification to explicitly define whether execution/commit provenance is included in, excluded from, or externally bound to the canonical artifact and its hash domain(s). AD-CA-010 updated to explicitly cover this boundary. Traceability matrix updated. Acceptance criteria updated (criterion 12). §5.3 extended to prohibit provenance from being a hidden source of canonical-result variation.

2. **Canonical byte sequence semantic tightening**: REQ-002-022 reworded. Ambiguous "exactly one canonical byte sequence for every hash-bearing … representation" replaced with per-hash-domain, per-representation semantics. The requirement now explicitly states that canonical bytes for the Artifact and Vector are separate definitions within their respective hash domains and MUST NOT be treated as a single universal byte sequence. Sub-bullets added specifying required definitions. Acceptance criteria updated (criterion 14). Traceability matrix updated.

3. **Source encoding vs numeric byte-order separation**: REQ-002-006 reworded. Source-level encoding requirements are explicitly limited to source material (character encoding, BOM, line endings, Unicode normalization form, source-to-byte conversion). Numeric byte order / endianness is explicitly placed under the numeric/vector representation contract (REQ-002-014). No encoding or endianness value was selected.

4. **Dependency closure requirement**: §4.7b added. REQ-002-034 added, requiring the future specification to define the complete dependency closure of Constitution Artifact construction. AD-CA-006 updated to cover complete dependency closure. Traceability matrix updated. Acceptance criteria updated (criterion 11).

5. **Deterministic failure / rejection semantics**: REQ-002-031 strengthened with an explicit enumerated list of failure conditions the future specification MUST address. Governing principle stated: NO SILENT FALLBACK WHERE IT CAN ALTER THE CANONICAL RESULT. No error codes invented.

6. **Identity / integrity / provenance / lineage / status clarification**: §4.4 extended with a normative definitional block distinguishing identity, integrity, provenance, lineage, and status. The future specification MUST define each concept independently.

7. **Hash-domain wording tightened**: §4.5 updated to state that Vector Hash and Artifact Hash are the minimum required domains but the future specification is not restricted to exactly those two; every hash domain used MUST be explicitly defined. An explicit enumeration of per-domain required definitions added. No concrete hash formula introduced or approved.

8. **Traceability stability clarification**: Existing "current" references remain where sources do not yet expose a frozen version, consistent with v0.2 practice. The document continues to make clear that approved traceability requires stable source identity/version/revision.

9. **Acceptance criteria expanded**: §9 expanded with criteria 10–16 covering source boundary, dependency closure, provenance boundary, hash domains, canonical byte semantics, failure semantics, and identity separation.

10. **Negative integrity verification expanded**: §5.2 extended with cases 7–11: numeric overflow/invalid numeric value, serialization alteration, lineage inconsistency, registration inconsistency, frozen-status inconsistency.

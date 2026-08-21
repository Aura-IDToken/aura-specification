# APS-001 — Aura Protocol Specification

**Document ID:** APS-001  
**Version:** 0.2-DRAFT  
**Status:** DRAFT — ARCHITECTURE REVIEW REQUIRED  
**Classification:** Root Normative Specification  
**Authority:** AURA Constitution v1.0 (FROZEN)

> This is a normative draft. Its presence does not constitute approval. Approval remains a Chief Architect / Architecture Review action under the Constitution.

---

## 1. Protocol Identity and Scope

Aura Protocol is a deterministic, auditable and independently verifiable protocol for producing a defined result and associated evidence from a protocol execution. Aura is a protocol, not an application, model or framework. Implementations are realizations of the specification.

A protocol execution consists of:

1. receiving a valid Evaluation Request;
2. resolving protocol and schema versions;
3. resolving the applicable policy, where required;
4. validating input and references;
5. performing the protocol-defined deterministic evaluation;
6. constructing the canonical Evaluation Result;
7. generating required Evidence;
8. serializing normative objects into canonical bytes;
9. calculating required integrity values;
10. exposing a verifiable execution record;
11. failing closed when a mandatory condition cannot be satisfied.

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are normative.

## 2. Protocol Execution Model

```text
Request
  ↓
Identity / Version Resolution
  ↓
Structural + Type Validation
  ↓
Policy Resolution (if applicable)
  ↓
Deterministic Evaluation
  ↓
Canonical Result
  ↓
Evidence Construction
  ↓
Canonical Serialization
  ↓
Integrity / Hash Domains
  ↓
Audit Record + Evidence Pack
```

For a fixed protocol version, schema version, policy version, canonical input and execution profile, a conformant implementation MUST produce the same protocol-defined result and canonical digest inputs. Protocol semantics MUST NOT depend on CPU architecture, operating system, locale, map iteration order or implementation-specific serialization.

Protocol-critical computation MUST NOT depend on uncontrolled randomness or mutable external state. Any explicitly permitted external dependency MUST have its normative effect represented in Evidence.

## 3. Input Requirements

An Evaluation Request is APS-200 `ENT-002`. A valid request MUST satisfy the APS-200 common object contract, identify its `object_type`, contain valid `protocol_version` and `schema_version`, contain a valid `object_id`, satisfy field constraints, and contain all data required by the applicable execution profile.

Malformed, ambiguous, unsupported or version-incompatible input MUST be rejected. Invalid protocol data MUST NOT be silently coerced into a different semantic value.

Protocol-critical numeric fields MUST use the exact APS-200 representation. The default Aura conformance profile uses integer/fixed-point representations where numeric determinism is required; floating-point arithmetic MUST NOT enter the protocol execution path where it violates INV-006/INV-007.

## 4. Output Requirements

An Evaluation Result is APS-200 `ENT-003`. It MUST satisfy the APS-200 common object contract, contain deterministic normative result fields, be serializable to canonical bytes, be linked to the execution and applicable policy reference, and be suitable for the required Evidence Pack.

Normative behaviour MUST NOT depend on undocumented internal state. Closed vocabularies defined by an applicable APS/schema MUST reject unknown values in strict conformance mode.

## 5. Policy Model

A Policy Reference is APS-200 `ENT-004`. It MUST identify the policy artifact and its version or immutable content identity sufficiently to make the evaluation reproducible.

The same protocol version, policy identity/version and canonical input MUST produce the same normative result. A change capable of altering a normative result MUST produce a new policy identity/version. Where policy integrity is required, signature/hash verification MUST occur before use and failure MUST be fail-closed.

## 6. Evidence Generation Requirements

Every protocol-governed execution MUST produce the Evidence required by APS-300 and the applicable Evidence Profile.

APS-300 Evidence MUST include, where required by that specification: `evidence_id`, `protocol_version`, `schema_version`, `implementation_id`, `execution_id`, `timestamp`, `policy_reference`, `input_hash`, `output_hash`, `evidence_hash`, `previous_evidence_hash` where applicable, and `attestation_reference`.

Evidence MUST be traceable to the execution and the normative requirement(s) it demonstrates. Once generated, normative Evidence MUST NOT be modified; modification MUST invalidate its integrity value.

## 7. Cryptographic Requirements

Cryptographic operations MUST operate on explicitly defined **canonical bytes**. Textual, language-specific or implementation-specific representations MUST NOT replace canonical bytes.

### 7.1 Canonical hash-domain model

The current CK-003 architectural decision selects the **RI-RS hash-domain model** as the proposed canonical model:

```text
canonical object
      │
      ▼
canonical bytes
      │
      ├── leaf ──► SHA-256(0x00 || bytes)
      │
      └── node ──► SHA-256(0x01 || left[32] || right[32])
```

Merkle semantics are RFC 6962-style. Hash inputs are raw bytes; hexadecimal strings are presentation values and MUST NOT substitute for underlying digest bytes.

The serialization profile producing `canonical bytes` is owned by APS-200. The hash-domain contract MUST remain independent of an incidental JSON/text representation.

### 7.2 Hash and Merkle verification

SHA-256 is the canonical hash primitive for the current profile unless a later approved APS changes it with explicit version binding. A verifier MUST be able to recompute required digests independently.

For Merkle use, leaf hashes use `0x00`, internal nodes use `0x01`, child values are the 32 raw digest bytes, and tree construction/odd-node behaviour MUST follow the approved Aura Merkle profile.

## 8. Error Handling

Mandatory validation, version, policy, canonicalization, integrity or Evidence failure MUST cause fail-closed execution.

A failed execution MUST NOT emit a protocol result or Evidence Pack that can be mistaken for a successful conformant execution.

Unsupported protocol/schema versions MUST be rejected unless an explicit compatibility rule permits them. Errors MUST be classifiable according to APS-100 and applicable APS requirements.

## 9. Conformance Requirements

An implementation is Aura Protocol Conformant only when all applicable mandatory requirements are objectively evidenced. At minimum this requires:

- all applicable APS-100 invariants PASS;
- all mandatory APS-400 tests PASS;
- all applicable APS-500 fixtures PASS;
- a complete APS-900 traceability path;
- valid Evidence for the result;
- no unresolved Critical conformance failure.

RI-PY and RI-RS are reference implementations under APS-950. Their implementation behaviour does not redefine the protocol.

Where multiple implementations support the same canonical object, they MUST produce byte-identical canonical bytes and digest-identical cryptographic outputs for shared fixtures.

Conformance results are `PASS`, `FAIL`, `NOT APPLICABLE`, or `ERROR`. An execution environment MAY report `BLOCKED`, but BLOCKED MUST NOT be converted to PASS.

## 10. Normative Authority

```text
AURA Constitution v1.0 (FROZEN)
          ↓
APS-001 Protocol Specification
          ↓
APS-100 Protocol Invariants
          ↓
APS-200 Canonical Data Model
          ↓
APS-300 Evidence Model
          ↓
APS-400 Conformance Test Matrix
          ↓
APS-500 Reference Fixtures
          ↓
APS-900 Compliance Mapping
          ↓
APS-950 Reference Implementation Requirements
```

Supporting ADRs, RFCs, fixtures and implementation documents MUST NOT contradict an approved APS requirement. Higher-authority approved documents prevail in conflicts.

## 11. Traceability

Every normative APS-001 requirement MUST be traceable through:

`APS-001 → INV-xxx → CONF-xxx → FIX-xxx → Evidence → RI-PY / RI-RS → Release`.

A requirement without a verification path is OPEN and MUST NOT be represented as conformant.

## 12. Version Binding

`protocol_version` identifies the normative protocol contract. `schema_version` identifies the representation/schema contract for the relevant data object. Both MUST be carried where required by APS-200/APS-300.

Compatibility MUST be defined by an explicit version-compatibility matrix; implementations MUST NOT infer compatibility solely from numeric ordering.

Changes affecting canonical bytes, hash domains, required fields, field interpretation or conformance outcomes MUST be version-bound and accompanied by impact analysis.

## 13. Release Gate

Before a specification release is marked conformant:

1. all normative APS documents have approved or explicitly declared draft status;
2. no mandatory requirement remains without verification;
3. every applicable invariant maps to executable conformance coverage;
4. mandatory fixtures have stable expected values;
5. shared RI-PY/RI-RS fixtures agree;
6. CI executes the conformance gate;
7. release Evidence is complete;
8. Architecture Review / Chief Architect approval is recorded.

This draft does not itself grant approval.

## Appendix A — Open closure dependencies

The following must be closed before APS-001 can be approved:

1. machine-readable APS-200 entity schemas — *the canonical serialization profile itself is closed: APS-200 §8 binds RFC 8785 JCS, UTF-8 canonical bytes and the SHA-256 / RFC 6962 domains*;
2. exact APS-300 Evidence Pack schema — *the cryptographic binding is closed: APS-300 §5.1 binds `evidence_hash` to APS-200 §8 canonical bytes*;
3. DQ-004 event-type semantics;
4. conformance coverage for all 15 invariants;
5. canonical APS-500 fixture corpus;
6. executable cross-language conformance runner;
7. repository-native CI gate;
8. Architecture Review and approval of this APS-001 draft.

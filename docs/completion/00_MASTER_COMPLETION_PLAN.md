# Aura Specification — Master Completion Plan

**Status:** EXECUTION DRAFT  
**Branch:** `completion/aura-specification-conformance`  
**Baseline:** `main` @ `62d2d6bcc1a46dd505ebfe400ad01fa3c6a25bf0`  
**Purpose:** Complete the specification repository without silently converting implementation behaviour into normative requirements.

## 1. Governing rule

The AURA Constitution v1.0 is FROZEN. It explicitly establishes **Specification First**, **Explicit over Implicit**, **Version Everything**, and requires conformance against APS-001 and APS-100. AI systems may analyse, propose, implement, and prepare tests, but must not approve or modify frozen canonical documents.

Accordingly, this branch is an implementation workspace. It may contain drafts, evidence, fixtures, conformance tooling, and proposed normative text. No canonical document is treated as approved merely because it exists on this branch.

## 2. Verified starting condition

- `APS-001_PROTOCOL_SPECIFICATION.md` is currently `0.1-DRAFT`, `Status: TODO`, and explicitly states that it does not yet exist. This is the principal repository-level blocker.
- APS-100 through APS-500, APS-900 and APS-950 exist as `1.0-DRAFT` documents.
- APS-100 defines 15 invariants and requires every invariant to have a conformance test and evidence path.
- APS-400 defines CONF-001 through CONF-010, but the repository currently contains the test-definition documents rather than an end-to-end executable conformance gate.
- APS-500 defines the reference-fixture contract, but the canonical fixture set is not yet demonstrably complete against the invariant/test matrix.
- APS-900 defines the required traceability chain from Constitution → APS Requirement → Invariant → Data Model → Evidence → Conformance Test → Fixture → Implementation → Release.
- APS-950 identifies RI-PY (`aura-poc-a-core`) and RI-RS (`aura-guard`) as reference implementations and requires a full conformance process.
- The repository currently has no `.github/workflows/` directory in the default branch; therefore a repository-native CI conformance gate is not yet evidenced.
- CK-003 DQ-002 and DQ-003 work exists on separate branches and must be reviewed before integration; branch existence is not equivalent to closure.

## 3. Completion gates

### G0 — Baseline and repository hygiene

Freeze the current main SHA, inventory branches, identify unmerged CK-003 evidence, and establish one completion branch.

### G1 — Root normative specification

Draft APS-001 from first principles using the Constitution and existing APS documents as constraints. Resolve scope, execution lifecycle, inputs, outputs, policy semantics, evidence generation, cryptographic domains, errors, conformance, and normative references.

### G2 — Normative consistency

Reconcile APS-100/200/300/400/500/900/950 against APS-001. Every MUST-level requirement must have a traceability path and no document may introduce an undefined semantic dependency.

### G3 — CK-003 closure

Review and integrate only evidence that survives independent verification:
- DQ-002 hash-domain decision and cross-language fixture.
- DQ-003 version semantics and binding fixture.
- DQ-004 event-type semantics.
- Remaining DQ gates required by the current evidence program.

### G4 — Executable conformance

Turn the specification into machine-checkable contracts: fixtures, RI-PY tests, RI-RS tests, shared expected values, and a deterministic conformance runner.

### G5 — CI enforcement

Add repository-native GitHub Actions that run specification validation and conformance checks. CI must fail closed on normative regressions. Payment/plan limitations must be treated as environment evidence, not as a false PASS.

### G6 — Traceability and release readiness

Produce a complete APS → INV → CONF → FIX → Evidence → RI → Release matrix. Close only those rows with objective evidence. Publish a release-readiness report and leave unresolved items explicitly marked OPEN/BLOCKED.

## 4. Non-negotiable completion criteria

The repository is **not complete** merely because documents exist. Completion requires:

1. APS-001 is authored and formally approved by the project owner/Chief Architect.
2. No contradictory normative semantics remain across APS documents.
3. All 15 invariants have explicit verification methods and executable conformance coverage.
4. Reference fixtures have stable, versioned expected values.
5. RI-PY and RI-RS agree on all shared canonical fixtures where interoperability is required.
6. Hash-domain semantics are explicit and bound to canonical bytes.
7. Version semantics are explicit and testable.
8. Traceability is complete from requirement to release evidence.
9. CI executes the conformance gate.
10. Any external/environmental blocker is reported as BLOCKED rather than converted into PASS.

## 5. Execution discipline

No production implementation in Core or Guard is modified as a side effect of completing this specification repository. Specification closure precedes implementation remediation. Once the specification is stable, Core and Guard are brought into conformance against it.

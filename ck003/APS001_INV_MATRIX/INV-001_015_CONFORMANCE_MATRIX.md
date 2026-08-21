# APS-001 / INV-001…INV-015 Conformance Closure Matrix

**Status:** WORKING CLOSURE BASELINE — NOT A CONFORMANCE CLAIM  
**Authority:** APS-001 → APS-100 → Invariant Registry  
**Branch:** `ck003/closure-workspace`  
**Purpose:** Establish the complete verification chain before fixture and implementation work.

## Rule

No invariant is considered conformant merely because a CONF identifier exists. Closure requires an executable verification path and evidence. The repository currently marks several invariants as TODO; those remain OPEN until the required tests and evidence exist.

## Matrix

| INV | Requirement (source) | CONF | Fixture requirement | Evidence | RI-PY | RI-RS | Closure state |
|---|---|---|---|---|---|---|---|
| INV-001 | Identical inputs MUST produce identical outputs. | CONF-001 | Deterministic evaluation fixture | EVID-CORE | Required | Required | OPEN — verify |
| INV-002 | Replay MUST reproduce an identical result across conformant implementations. | CONF-002 | Replay/Evidence Pack fixture | EVID-CORE, EVID-CHAIN | Required | Required | OPEN — verify |
| INV-003 | Every protocol object MUST have unambiguous canonical serialization. | CONF-003 | Canonical-bytes corpus | EVID-CORE | CANONICAL-001 PASS | CANONICAL-001 PASS | PARTIAL — APS-200 §8 bound; corpus not yet JCS-discriminating (DQ-006 R1) |
| INV-004 | Evidence MUST NOT be modified after generation. | CONF-004 | Mutation/tamper fixture | EVID-CORE | Required | Required | OPEN — verify |
| INV-005 | Every Evidence artifact MUST reference the APS requirement it documents. | CONF-005 | Traceability fixture | EVID-CORE | Required | Required | OPEN — verify |
| INV-006 | Results MUST be independent of hardware/OS platform. | CONF-006 | Cross-platform deterministic fixture | EVID-CORE | Required | Required | OPEN — requires multi-platform evidence |
| INV-007 | Protocol logic MUST NOT use floating-point arithmetic where it violates determinism. | TODO in registry | Static/runtime zero-float fixture/gate | EVID-CORE | Required | Required | OPEN — CONF missing |
| INV-008 | Errors MUST terminate safely; no partial conformant output. | CONF-007 | Fail-closed negative fixtures | EVID-CORE | Required | Required | OPEN — verify |
| INV-009 | Evidence, Protocol and Data Model versions MUST be compatible. | CONF-008 | Version compatibility corpus | EVID-CORE | Required | Required | OPEN — DQ-003 binding required |
| INV-010 | Every invariant MUST have a corresponding Conformance Test. | CONF-009 | Registry/CONF completeness fixture | EVID-CONF | Required | Required | OPEN — currently circular until all missing CONF tests exist |
| INV-011 | Evidence integrity MUST be independently cryptographically verifiable. | CONF-010 | Hash-domain/integrity fixtures | EVID-CORE | Required | Required | OPEN — byte domain now bound (APS-200 §8.5, APS-300 §5.1); Evidence-object execution evidence still required |
| INV-012 | Every protocol execution MUST leave an APS-conformant audit trail. | TODO in registry | ENT-007 audit fixture | EVID-AUDIT | Required | Required | OPEN — CONF missing; DQ-004 relevant |
| INV-013 | Same policy version + identical inputs MUST yield identical decision. | TODO in registry | Policy determinism fixture | EVID-CORE | Required | Required | OPEN — CONF missing |
| INV-014 | Implementation MUST pass all applicable APS-500 fixtures. | TODO in registry | Full APS-500 corpus | EVID-CORE, EVID-CONF | Required | Required | OPEN — CONF missing |
| INV-015 | Every protocol artifact MUST have unique canonical identity conformant with APS-000. | TODO in registry | Identity/object-type fixture | EVID-CORE | Required | Required | OPEN — CONF missing |

## Source-grounded observations

The current Invariant Registry explicitly identifies missing conformance tests for INV-007, INV-012, INV-013, INV-014 and INV-015. fileciteturn430file0L2-L6

APS-100 requires every invariant to define requirement, rationale, verification method, evidence, failure class, related APS/ADR material and conformance tests. It also defines the release rule: all applicable invariants PASS, all required tests PASS, complete Evidence Pack, and no Critical violations. fileciteturn431file0L2-L6

APS-001 currently states that the normative traceability chain is `APS-001 → INV-xxx → CONF-xxx → FIX-xxx → Evidence → RI-PY / RI-RS → Release`, and explicitly leaves canonical serialization, DQ-004, full 15-invariant coverage, fixture corpus, cross-language runner, CI and Architecture Review as closure dependencies. fileciteturn433file0L2-L6

## Closure policy

1. Do not mark an invariant PASS from documentation alone.
2. A missing CONF assignment is an OPEN conformance gap, not a documentation defect.
3. A fixture whose expected value depends on an unresolved serialization/hash contract is not normative yet.
4. RI-PY and RI-RS are evidence-producing reference implementations; neither implementation defines protocol semantics.
5. Cross-language equality is required for shared canonical fixtures before release closure.
6. CI may report BLOCKED for unavailable infrastructure, but BLOCKED is never PASS.

## Next work package

**A. APS-001 closure dependencies:** canonical serialization + Evidence binding + DQ-004.  
**B. Assign CONF-011…CONF-015 (or repository-approved identifiers) for the five currently TODO invariants.**  
**C. Build the fixture corpus only after the normative serialization/version/event-type decisions are frozen.**  
**D. Execute RI-PY and RI-RS against the same corpus and require byte/digest equality.

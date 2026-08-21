# APS-001 / INV-001…INV-015 Conformance Closure Matrix

**Status:** WORKING CLOSURE BASELINE — NOT A CONFORMANCE CLAIM  
**Authority:** APS-001 → APS-100 → Invariant Registry  
**Branch:** `ck003/specification-integration-dq006`  
**Review date:** 2026-08-20  
**Purpose:** Maintain the executable verification chain without promoting documentation or a single fixture into full invariant conformance.

## Rule

No invariant is considered conformant merely because a CONF identifier or fixture exists. Closure requires an executable verification path, implementation evidence, and the applicable release traceability chain. A single passing fixture is not equivalent to full invariant closure unless the invariant's coverage requirement is fully exercised.

## Matrix

| INV | Requirement | CONF | Fixture requirement | Evidence | RI-PY | RI-RS | Closure state |
|---|---|---|---|---|---|---|---|
| INV-001 | Identical inputs MUST produce identical outputs. | CONF-001 | Deterministic evaluation fixture | EVID-CORE | Required | Required | OPEN — execution/evidence required |
| INV-002 | Replay MUST reproduce an identical result across conformant implementations. | CONF-002 | Replay/Evidence Pack fixture | EVID-CORE, EVID-CHAIN | Required | Required | OPEN — execution/evidence required |
| INV-003 | Every protocol object MUST have unambiguous canonical serialization. | CONF-003 | Canonical-bytes corpus | EVID-CORE | Required | Required | PARTIAL — CANONICAL-001 cross-language PASS; full object corpus open |
| INV-004 | Evidence MUST NOT be modified after generation. | CONF-004 | Mutation/tamper fixture | EVID-CORE | Required | Required | OPEN — execution/evidence required |
| INV-005 | Every Evidence artifact MUST reference the APS requirement it documents. | CONF-005 | Traceability fixture | EVID-CORE | Required | Required | OPEN — execution/evidence required |
| INV-006 | Results MUST be independent of hardware/OS platform. | CONF-006 | Cross-platform deterministic fixture | EVID-CORE | Required | Required | OPEN — multi-platform evidence required |
| INV-007 | Protocol logic MUST NOT use floating-point arithmetic where it violates determinism. | CONF-011 | `FIX-INV-007_zero_float.json` | EVID-CORE | Required | Required | OPEN — CONF/fixture defined; implementation evidence required |
| INV-008 | Errors MUST terminate safely; no partial conformant output. | CONF-007 | Fail-closed negative fixtures | EVID-CORE | Required | Required | OPEN — execution/evidence required |
| INV-009 | Evidence, Protocol and Data Model versions MUST be compatible. | CONF-008 | Version compatibility corpus | EVID-CORE | Required | Required | OPEN — DQ-003 binding required |
| INV-010 | Every invariant MUST have a corresponding Conformance Test. | CONF-009 | Registry/CONF completeness fixture | EVID-CONF | Required | Required | OPEN — completeness gate required |
| INV-011 | Evidence integrity MUST be independently cryptographically verifiable. | CONF-010 | Hash-domain/integrity fixtures | EVID-CORE | Required | Required | PARTIAL — DQ-002/DQ-006 closed; full Evidence conformance open |
| INV-012 | Every protocol execution MUST leave an APS-conformant audit trail. | CONF-012 | `FIX-INV-012_event_type.json` + DQ-004 fixtures | EVID-AUDIT | Required | Required | BLOCKED — DQ-004 vocabulary/registry approval required |
| INV-013 | Same policy version + identical inputs MUST yield identical decision. | CONF-013 | `FIX-INV-013_policy_determinism.json` | EVID-CORE | Required | Required | OPEN — implementation evidence required |
| INV-014 | Implementation MUST pass all applicable APS-500 fixtures. | CONF-014 | `FIX-INV-014_aps500_compatibility.json` + full APS-500 corpus | EVID-CORE, EVID-CONF | Required | Required | OPEN — single compatibility fixture exists; full APS-500 corpus/evidence required |
| INV-015 | Every protocol artifact MUST have unique canonical identity conformant with APS-000. | CONF-015 | `FIX-INV-015_canonical_identity.json` | EVID-CORE | Required | Required | OPEN — implementation evidence required |

## Current verified closure inputs

### DQ-006 / INV-003 input

CROSS-LANGUAGE-001 has independently verified CANONICAL-001 in RI-PY and RI-RS with byte-identical canonical bytes, equal SHA-256 digests and equal RFC 6962 leaf hashes. DQ-006 is recorded CLOSED / PASS. This proves the tested canonical boundary; it does not prove all canonical objects or all fixture cases.

### DQ-002 / INV-011 input

DQ-002 is recorded CLOSED / PASS with the frozen hash-domain contract `SHA-256(canonical_bytes)` and RFC 6962 leaf domain `SHA-256(0x00 || canonical_bytes)`. Full Evidence integrity conformance remains an INV-011 execution obligation.

## Source-grounded observations

The current repository now contains CONF-011…CONF-015 and fixtures for INV-007 and INV-012…INV-015. These identifiers therefore no longer constitute missing-definition gaps. They remain open until implementation execution and evidence close the corresponding invariant.

APS-001 requires the normative traceability chain:

`APS-001 → INV-xxx → CONF-xxx → FIX-xxx → Evidence → RI-PY / RI-RS → Release`.

A requirement without an executable verification path remains OPEN.

## Closure policy

1. Do not mark an invariant PASS from documentation alone.
2. A CONF identifier without execution evidence is an OPEN conformance gap.
3. A fixture whose expected value depends on an unresolved normative decision is not a closure fixture.
4. RI-PY and RI-RS are evidence-producing reference implementations; neither implementation defines protocol semantics.
5. Cross-language equality is required for shared canonical fixtures before release closure.
6. CI may report BLOCKED for unavailable infrastructure, but BLOCKED is never PASS.
7. Partial coverage MUST be explicitly labelled PARTIAL and MUST NOT be promoted to PASS.

## Next work package

**A. DQ-003:** complete version compatibility/binding matrix and version fixtures; execute RI-PY/RI-RS.  
**B. DQ-004:** approve the normative event vocabulary/payload registry and execute approved/unknown-token fixtures.  
**C. INV-001…015:** execute each mapped CONF against the required fixtures and produce evidence.  
**D. Complete APS-500 fixture corpus and manifest.**  
**E. Execute RI-PY and RI-RS against the common corpus and require byte/digest equality.  
**F. Convert the runner into repository-native CI gates.

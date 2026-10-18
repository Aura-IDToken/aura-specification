# CONF-008 — Version Compatibility

**Related Invariant:** INV-009
**Category:** Compatibility
**Status:** DRAFT

## Purpose
Verify that protocol, schema, fixture, and evidence version references are mutually compatible under the approved version-compatibility contract.

## Preconditions
- The repository-local draft compatibility matrix is available in human-readable form at `ck003/decisions/DQ-003/CURRENT_VERSION_COMPATIBILITY_MATRIX.md` and in machine-readable form at `ck003/decisions/DQ-003/CURRENT_VERSION_COMPATIBILITY_MATRIX.json`.
- The bound compatibility fixture `fixtures/compatibility/FIX-COMPAT-001_VERSION_MATRIX.json` is available.
- The implementation or verifier can inspect the version-bearing artifacts required by APS-200 and APS-300.

## Procedure
1. Resolve the governing compatibility matrix for the protocol version under test.
2. Load the applicable compatibility fixture set for that matrix.
3. Collect the version-bearing artifacts required by the fixture, including protocol version, schema versions, input-schema binding, evidence-profile binding, and fixture version.
4. Compare the observed combination against the explicit compatibility matrix.
5. Execute at least one negative compatibility case outside the matrix.
6. Record any missing, ambiguous, or incompatible version references.

## Expected Result
All required version references are present and the observed combination is explicitly permitted by the approved compatibility matrix.

## PASS / FAIL
- **PASS:** every required version reference is present and the observed combination is permitted by the approved matrix.
- **FAIL:** any required version reference is missing, contradictory, or outside the approved compatibility matrix.
- **ERROR:** the governing compatibility matrix or bound compatibility fixture is unresolved, unavailable, or cannot be applied deterministically.

## Evidence
EVID-CORE containing the observed version fields, the resolved compatibility matrix identifier, the fixture identifier, and the evaluation result.

## Traceability
| Field | Value |
|-------|-------|
| Test ID | CONF-008 |
| Invariant | INV-009 |
| Related Fixture | `FIX-COMPAT-001` / compatibility fixture set bound to the approved matrix |
| Evidence Type | EVID-CORE |

## Current readiness note
CONF-008 is now **READY at repository-local draft level**. The current local gate is executed by `scripts/run-draft-conformance.py` against `fixtures/compatibility/FIX-COMPAT-001_VERSION_MATRIX.json` and the machine-readable DQ-003 compatibility matrix. Implementation-side RI-PY / RI-RS evidence is still outstanding.

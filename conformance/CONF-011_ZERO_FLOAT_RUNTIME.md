# CONF-011 — Zero Float Runtime

**Related Invariant:** INV-007  
**Category:** Determinism / Static Analysis  
**Status:** DRAFT

## Purpose
Verify that the protocol execution path does not use floating-point arithmetic where it would violate deterministic execution.

## Preconditions
- Protocol execution source is available for inspection.
- Generated/vendor/test-only code is excluded from the runtime scope according to the approved scope declaration.
- Bound fixture: `fixtures/corpus/FIX-INV-007_zero_float.json`

## Procedure
1. Identify the normative protocol execution paths.
2. Run the repository's static source scan for floating-point types, literals, conversions and arithmetic in those paths.
3. Review every reported occurrence and classify it as runtime, offline normalization, test, or non-executable documentation.
4. Execute `FIX-INV-007` unchanged through the protocol path under inspection.
5. Confirm that the runtime data observed for the fixture remains in the integer-only numeric domain.

## Expected Result
No prohibited floating-point operation occurs in the protocol execution path, and applicable deterministic fixtures pass.

## PASS / FAIL
- **PASS:** zero prohibited runtime float operations and deterministic fixtures pass.
- **FAIL:** any prohibited runtime float operation is present or determinism evidence fails.
- **ERROR:** required static-analysis or fixture execution cannot be completed.

## Evidence
EVID-CORE static-analysis report plus fixture/conformance report.

## Traceability
| Field | Value |
|-------|-------|
| Test ID | CONF-011 |
| Invariant | INV-007 |
| Related Fixture | FIX-INV-007 |
| Evidence Type | EVID-CORE |

## Current readiness note
CONF-011 is currently **READY** in repository planning because `FIX-INV-007` is now explicitly bound; the remaining step is controlled execution evidence.

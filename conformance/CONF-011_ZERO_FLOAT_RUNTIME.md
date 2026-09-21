# CONF-011 — Zero Float Runtime

**Related Invariant:** INV-007  
**Category:** Determinism / Static Analysis  
**Status:** DRAFT

## Purpose
Verify that the protocol execution path does not use floating-point arithmetic where it would violate deterministic execution.

## Preconditions
- Protocol execution source is available for inspection.
- Generated/vendor/test-only code is excluded from the runtime scope according to the approved scope declaration.

## Procedure
1. Identify the normative protocol execution paths.
2. Run the repository's static source scan for floating-point types, literals, conversions and arithmetic in those paths.
3. Review every reported occurrence and classify it as runtime, offline normalization, test, or non-executable documentation.
4. Execute the applicable deterministic fixture suite.

## Expected Result
No prohibited floating-point operation occurs in the protocol execution path, and applicable deterministic fixtures pass.

## PASS / FAIL
- **PASS:** zero prohibited runtime float operations and deterministic fixtures pass.
- **FAIL:** any prohibited runtime float operation is present or determinism evidence fails.
- **ERROR:** required static-analysis or fixture execution cannot be completed.

## Evidence
EVID-CORE static-analysis report plus fixture/conformance report.

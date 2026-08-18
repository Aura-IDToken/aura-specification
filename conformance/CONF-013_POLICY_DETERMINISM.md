# CONF-013 — Policy Determinism

**Related Invariant:** INV-013  
**Category:** Determinism / Functional  
**Status:** DRAFT

## Purpose
Verify that the same pinned policy version and identical inputs produce an identical decision.

## Procedure
1. Pin an explicit policy version.
2. Execute the same input twice under that exact policy version.
3. Compare the decision and all protocol-defined decision outputs bit-for-bit.
4. Repeat with the same conformance fixture on each applicable conformant implementation.

## Expected Result
The decision and all digest-domain outputs are identical for every execution using the same policy version and identical inputs.

## PASS / FAIL
- **PASS:** all compared decision outputs are identical.
- **FAIL:** any decision or digest-domain output differs.
- **ERROR:** the policy cannot be pinned or the fixture cannot be executed.

## Evidence
EVID-CORE with policy version, input fixture identifier, output comparison and digest evidence.

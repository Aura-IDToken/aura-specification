# CONF-013 — Policy Determinism

**Related Invariant:** INV-013  
**Category:** Determinism / Functional  
**Status:** DRAFT

## Purpose
Verify that the same pinned policy version and identical inputs produce an identical decision.

## Preconditions
- Bound fixture: `fixtures/corpus/FIX-INV-013_policy_determinism.json`
- The policy identified by the fixture can be pinned without substitution.
- The fixture input can be replayed unchanged for at least two executions on the same implementation.

## Procedure
1. Load `FIX-INV-013` and pin the exact `policy_id` / `policy_version` pair defined by the fixture.
2. Execute the same canonical input twice under that exact policy version on one implementation.
3. Compare the decision token and all protocol-defined digest-domain outputs bit-for-bit.
4. Repeat with the same fixture on each additional applicable conformant implementation.
5. Record any divergence in decision token, output hash, or policy binding.

## Expected Result
The decision and all digest-domain outputs are identical for every execution using the same policy version and identical inputs.

## PASS / FAIL
- **PASS:** all compared decision outputs are identical.
- **FAIL:** any decision or digest-domain output differs.
- **ERROR:** the policy cannot be pinned or the fixture cannot be executed.

## Evidence
EVID-CORE with policy version, input fixture identifier, output comparison and digest evidence.

## Traceability
| Field | Value |
|-------|-------|
| Test ID | CONF-013 |
| Invariant | INV-013 |
| Related Fixture | FIX-INV-013 |
| Evidence Type | EVID-CORE |

## Current readiness note
CONF-013 is currently **READY** in repository planning because `FIX-INV-013` now binds one concrete policy/input pair; the remaining step is controlled execution evidence.

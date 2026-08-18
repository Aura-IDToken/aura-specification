# CONF-014 — Reference Compatibility

**Related Invariant:** INV-014  
**Category:** Compatibility / Fixtures  
**Status:** DRAFT

## Purpose
Verify that an implementation passes every applicable normative APS-500 Reference Fixture.

## Preconditions
- The normative fixture corpus is versioned and available.
- Applicability rules for the target protocol/version are defined.

## Procedure
1. Resolve the applicable fixture set for the protocol and implementation version.
2. Execute every applicable fixture.
3. Compare the implementation output with the fixture's normative expected result.
4. Record fixture identifier, implementation identifier, result and evidence digest.

## Expected Result
Every applicable normative fixture returns the expected result.

## PASS / FAIL
- **PASS:** all applicable fixtures pass.
- **FAIL:** any applicable fixture fails.
- **ERROR:** a required fixture cannot be executed or its applicability cannot be resolved.

## Evidence
EVID-CONF fixture execution report and per-fixture evidence hashes.

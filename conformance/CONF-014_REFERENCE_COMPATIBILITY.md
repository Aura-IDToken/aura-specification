# CONF-014 — Reference Compatibility

**Related Invariant:** INV-014  
**Category:** Compatibility / Fixtures  
**Status:** DRAFT

## Purpose
Verify that an implementation passes every applicable normative APS-500 Reference Fixture.

## Preconditions
- The normative APS-500 fixture corpus is versioned and available.
- Applicability rules for the target protocol/version are defined.
- Any working-corpus artifacts used during closure work have been explicitly excluded from PASS accounting unless they were promoted into APS-500.

## Procedure
1. Resolve the applicable fixture set for the protocol and implementation version.
2. Verify that each selected fixture is part of the normative APS-500 corpus rather than only a working-corpus artifact.
3. Execute every applicable normative fixture unchanged.
4. Compare the implementation output and required evidence against the fixture's normative expected result.
5. Record fixture identifier, corpus version, implementation identifier, result, and evidence digest.

## Expected Result
Every applicable normative fixture returns the expected result.

## PASS / FAIL
- **PASS:** all applicable fixtures pass.
- **FAIL:** any applicable fixture fails.
- **ERROR:** a required fixture cannot be executed, its applicability cannot be resolved, or the normative APS-500 corpus version is not yet fixed.

## Evidence
EVID-CONF fixture execution report and per-fixture evidence hashes.

## Current readiness note
CONF-014 is currently **BLOCKED** in repository planning because the normative APS-500 corpus version is not yet frozen.

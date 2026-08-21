# CONF-015 — Canonical Identity

**Related Invariant:** INV-015  
**Category:** Identity / Data Model  
**Status:** DRAFT

## Purpose
Verify that every protocol artifact has a unique canonical identity conformant with the applicable APS-000 and APS-200 identity rules.

## Procedure
1. Enumerate the protocol artifacts produced by the conformance execution.
2. Validate required `object_id` and `object_type` fields where applicable.
3. Validate identity syntax and object-type semantics against the applicable specification.
4. Verify that canonical serialization preserves the identity fields without ambiguity.
5. Verify that two distinct canonical artifacts do not resolve to the same canonical identity within the applicable identity scope.

## Expected Result
Every applicable artifact has a valid, unique and traceable canonical identity.

## PASS / FAIL
- **PASS:** all applicable artifacts satisfy identity and uniqueness requirements.
- **FAIL:** any artifact lacks required identity, violates syntax/semantics, or collides within scope.
- **ERROR:** identity rules required for evaluation are unresolved or unavailable.

## Evidence
EVID-CORE containing the artifact inventory, identity validation results and canonical identifiers.

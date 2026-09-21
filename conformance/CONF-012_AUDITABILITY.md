# CONF-012 — Auditability

**Related Invariant:** INV-012  
**Category:** Evidence / Audit  
**Status:** DRAFT

## Purpose
Verify that every protocol-governed execution leaves an ENT-007 Audit Record conformant with the applicable APS requirements.

## Preconditions
- A valid protocol execution fixture exists.
- The applicable ENT-007 schema and event-type registry are available.

## Procedure
1. Execute the protocol using the conformance input.
2. Locate the resulting Audit Record.
3. Validate all mandatory ENT-007 fields and their types.
4. Validate `event_type` against the approved registry.
5. Validate the audit-chain/integrity fields against the applicable hash-domain contract.

## Expected Result
A complete, schema-valid and semantically valid Audit Record exists and its integrity/chain verification succeeds.

## PASS / FAIL
- **PASS:** required Audit Record exists and all applicable validations pass.
- **FAIL:** missing, malformed, unregistered or integrity-invalid audit evidence.
- **ERROR:** required execution or validation cannot be completed.

## Evidence
EVID-AUDIT containing the Audit Record and validation result.

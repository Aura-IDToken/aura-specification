# CONF-012 — Auditability

**Related Invariant:** INV-012  
**Category:** Evidence / Audit  
**Status:** DRAFT

## Purpose
Verify that every protocol-governed execution leaves an ENT-007 Audit Record conformant with the applicable APS requirements.

## Preconditions
- A valid protocol execution fixture exists.
- The applicable ENT-007 schema is available.
- The repository-local draft event-type registry is available in human-readable form at `ck003/decisions/DQ-004/CURRENT_EVENT_TYPE_REGISTRY.md` and in machine-readable form at `ck003/decisions/DQ-004/CURRENT_EVENT_TYPE_REGISTRY.json`.
- The bound auditability fixture `fixtures/corpus/FIX-INV-012_event_type.json` is available.

## Procedure
1. Load `FIX-INV-012` and the current machine-readable DQ-004 event-type registry.
2. Validate the registered token set and confirm that the positive token is present while the negative token remains unregistered.
3. Validate the concrete draft Audit Record against the ENT-007 schema.
4. Recompute `event_payload_hash` from the bound payload and verify `integrity_hash` on the Audit Record.
5. Confirm that the draft-local first-record sentinel (`previous_record_hash = 64 zero hex characters`, `sequence_number = 0`) is preserved for this controlled gate.

## Expected Result
A complete, schema-valid and semantically valid Audit Record exists, the registered token is accepted while unregistered/alias tokens are rejected, and the draft-local payload/integrity hashes recompute correctly.

## PASS / FAIL
- **PASS:** required Audit Record exists and all applicable validations pass.
- **FAIL:** missing, malformed, unregistered or integrity-invalid audit evidence.
- **ERROR:** required execution or validation cannot be completed.

## Evidence
EVID-AUDIT containing the Audit Record and validation result.

## Traceability
| Field | Value |
|-------|-------|
| Test ID | CONF-012 |
| Invariant | INV-012 |
| Related Fixture | `FIX-INV-012` |
| Evidence Type | EVID-AUDIT |

## Current readiness note
CONF-012 is now **READY at repository-local draft level** through `scripts/run-draft-conformance.py`. Final release-grade closure still requires a broader approved event vocabulary plus RI-PY / RI-RS execution evidence.

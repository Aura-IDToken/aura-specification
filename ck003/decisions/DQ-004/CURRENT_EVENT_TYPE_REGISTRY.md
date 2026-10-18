# DQ-004 — Current Event-Type Registry

**Classification:** WORKING / CONTROLLED CLOSURE ARTIFACT  
**Status:** READY FOR CONTROLLED EXECUTION  
**Review date:** 2026-09-26

## Purpose

This registry is the current repository-local draft answer to DQ-004 for `CONF-012`. It closes one controlled vocabulary slice for auditability without claiming that the full release-grade event vocabulary is finished.

## Governing machine-readable form

- `ck003/decisions/DQ-004/CURRENT_EVENT_TYPE_REGISTRY.json`

## Current repository-local draft token

| event_type | producer | payload_schema | introduced_protocol_version | Status |
|---|---|---|---|---|
| `AUDIT_RECORD` | `AURA-DRAFT-AUDIT-001` | `AURA-DRAFT-AUDIT-001` | `1.0-DRAFT` | repository-local draft gate token |

## Scope boundary

This token is sufficient for the current local `CONF-012` gate because:

1. it is already present in the repository's canonicalization source material;
2. it is now explicitly registered in machine-readable form;
3. `FIX-INV-012` binds the token to one concrete audit-record example plus negative membership checks.

This artifact does **not** claim that the final normative protocol event vocabulary is complete. Additional event tokens still require explicit versioned specification changes and compatibility analysis.

## Current closure posture

DQ-004 is now **READY at repository-local draft level**:

- `aps/EVENT_TYPE_REGISTRY.md` defines the governing token contract;
- this file and its JSON counterpart define the current draft-local registered token;
- `fixtures/corpus/FIX-INV-012_event_type.json` binds the token to a concrete auditability fixture;
- `scripts/run-draft-conformance.py` executes the local `CONF-012` gate.

Remaining work before release-grade closure:

- extend the registry beyond the single local draft token where required by the protocol;
- settle the broader audit-chain/domain decisions still called out elsewhere in the repository;
- execute the same gate on RI-PY / RI-RS and promote the results into implementation evidence.

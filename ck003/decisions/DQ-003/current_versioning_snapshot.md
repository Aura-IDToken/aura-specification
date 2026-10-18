# DQ-003 — Current Versioning Snapshot

**Classification:** EVIDENCE
**Status:** READY
**Review date:** 2026-08-18

## Verified current contract

APS-001 §12 states:

- `protocol_version` identifies the normative protocol contract;
- `schema_version` identifies the representation/schema contract for the relevant data object;
- both MUST be carried where required by APS-200/APS-300;
- compatibility MUST be defined by an explicit compatibility matrix;
- implementations MUST NOT infer compatibility solely from numeric ordering;
- changes affecting canonical bytes, hash domains, required fields, field interpretation or conformance outcomes MUST be version-bound and accompanied by impact analysis.

APS-200 §4 independently requires both `protocol_version` and `schema_version` in the Common Object Contract.

## Closure status

The semantic distinction is present and therefore no longer undefined at the top-level protocol layer. The repository now also contains:

- an explicit compatibility matrix in `CURRENT_VERSION_COMPATIBILITY_MATRIX.md` and `CURRENT_VERSION_COMPATIBILITY_MATRIX.json`;
- a bound compatibility fixture in `fixtures/compatibility/FIX-COMPAT-001_VERSION_MATRIX.json`;
- a repo-native draft conformance runner that executes `CONF-008` locally.

This is sufficient to move DQ-003 to **READY** at repository-local draft level. Cross-implementation execution evidence and approval/promotion remain outstanding.

## Decision boundary

This snapshot now points to the active compatibility policy artifact, but the final matrix still requires approval and RI evidence before APS-001 v1.0 approval.

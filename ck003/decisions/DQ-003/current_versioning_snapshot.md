# DQ-003 — Current Versioning Snapshot

**Classification:** EVIDENCE
**Status:** OPEN
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

The semantic distinction is present and therefore no longer undefined at the top-level protocol layer. However, the repository still needs the executable compatibility matrix and version-binding fixtures required to demonstrate that the distinction is enforceable across implementations.

## Decision boundary

This evidence does not introduce a compatibility policy. The final matrix must be approved as part of DQ-003 closure before APS-001 v1.0 approval.

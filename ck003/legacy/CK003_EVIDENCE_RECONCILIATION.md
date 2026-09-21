# CK003 Evidence Reconciliation — CK003-001…010

**Status:** UNRESOLVED / LEGACY REFERENCE CANDIDATES  
**Branch:** `ck003/closure-workspace`

## Finding

A repository-wide search on the current `aura-specification` branch did not locate files or registry entries with the identifiers `CK003-001` through `CK003-010`.

The current repository does contain CK-003 evidence under other explicit paths, including `ck003/dq-002-hash-domain/`, and current closure artifacts under `ck003/`. Those artifacts do not establish that the missing numeric identifiers correspond to a recoverable ten-fixture corpus.

## Decision

Until source provenance is recovered, `CK003-001…010` MUST NOT be treated as normative fixtures and MUST NOT be assigned expected digests.

They are classified as:

`LEGACY_REFERENCE_UNRESOLVED`

This is an evidence-management classification, not a deletion or repudiation of historical work.

## Recovery conditions

A CK003-001…010 item may be restored to the normative corpus only when at least one of the following is available:

1. the original committed file/path in a repository history;
2. a commit/tree/archive containing the exact artifact;
3. a signed/exported evidence pack with stable identifier and digest;
4. a documented mapping from the identifier to an existing canonical fixture.

Recovered artifacts MUST be hash-checked and provenance recorded before promotion.

## Corpus rule

The canonical fixture manifest MUST distinguish:

- `NORMATIVE` — current, source-backed fixture;
- `PROPOSED` — authored but not frozen;
- `LEGACY_REFERENCE_UNRESOLVED` — referenced historically but not recoverable from current source;
- `DEPRECATED` — recovered but superseded;
- `INVALID` — provenance/integrity failure.

`LEGACY_REFERENCE_UNRESOLVED` entries MUST NOT participate in RI-PY/RI-RS PASS calculations.

## Current gate

**CK003-001…010: NOT RECOVERED.**

No claim is made that the artifacts never existed; only that they are not independently recoverable from the currently inspected `aura-specification` branch.

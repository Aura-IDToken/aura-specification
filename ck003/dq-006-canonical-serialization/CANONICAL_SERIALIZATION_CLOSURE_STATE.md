# Canonical Serialization Closure State

> **SUPERSEDED — 2026-08-20 (CK-003).**
> This document recorded the profile as OPEN because APS-200 §8 was TODO. It is
> no longer. Of the six blockers it lists: (2) APS-200 §8 amendment, (3) APS-300
> reconciliation, (4) normative fixture, (5) RI-PY/RI-RS equality and (6)
> version/migration rule are met; (1) Chief Architect approval is a merge-time
> act under GOVERNANCE.md §2.
> Current state: `ck003/CK003_CANONICAL_SERIALIZATION_RECONCILIATION.md`.

## Current source finding

`APS-200 §8` currently requires deterministic serialization but explicitly leaves the canonical serialization format for RI-PY / RI-RS interoperability as TODO. Therefore the normative specification is not yet closed.

## Proposed target

`RFC 8785 JSON Canonicalization Scheme (JCS) → UTF-8 canonical bytes`.

This is a proposed architecture decision, not yet a frozen normative rule.

## Closure blockers

1. Chief Architect approval of the proposed profile.
2. APS-200 §8 normative amendment.
3. APS-300 reconciliation of evidence/hash scope.
4. Normative fixture with canonical bytes and expected digest.
5. RI-PY / RI-RS equality against the same fixture.
6. Version/migration rule for pre-JCS evidence.

## Gate status

**CANONICAL SERIALIZATION: SUPERSEDED — see APS-200 §8 (enacted)**

No PASS is claimed until the normative APS documents and cross-language evidence are updated.

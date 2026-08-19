# Canonical Serialization Closure State

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

**CANONICAL SERIALIZATION: OPEN / PROPOSED PROFILE READY**

No PASS is claimed until the normative APS documents and cross-language evidence are updated.

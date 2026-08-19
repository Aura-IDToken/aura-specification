# Canonical Serialization Closure State

## Current source finding

`APS-200 §8` currently requires deterministic serialization but explicitly leaves the canonical serialization format for RI-PY / RI-RS interoperability as TODO. Therefore the normative specification is not yet closed.

## Proposed target

`RFC 8785 JSON Canonicalization Scheme (JCS) → UTF-8 canonical bytes`.

This is a proposed architecture decision, not yet a frozen normative rule.

## Closure blockers

1. Chief Architect approval of the proposed profile. — **OPEN**
2. APS-200 §8 normative amendment. — **OPEN**
3. APS-300 reconciliation of evidence/hash scope. — **OPEN**
4. Normative fixture with canonical bytes and expected digest. — **SATISFIED** by `CANONICAL-001` (DQ-006).
5. RI-PY / RI-RS equality against the same fixture. — **SATISFIED** by CROSS-LANGUAGE-001 (DQ-006); see `evidence/DQ-006_CLOSURE_PACKAGE.md`.
6. Version/migration rule for pre-JCS evidence. — **OPEN**

## Gate status

**CANONICAL SERIALIZATION: OPEN / PROPOSED PROFILE READY — CROSS-LANGUAGE EVIDENCE SUPPLIED**

The cross-language evidence blocker is discharged for `CANONICAL-001` by DQ-006 (CLOSED). The normative blockers 1, 2, 3 and 6 remain open, so no normative PASS is claimed for canonical serialization here.

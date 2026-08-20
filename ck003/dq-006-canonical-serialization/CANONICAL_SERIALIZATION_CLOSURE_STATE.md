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

---

## Relationship to DQ-006

DQ-006 is **CLOSED — PASS** as a *conformance/evidence* gate: RI-PY and RI-RS independently
executed CANONICAL-001 and produced identical canonical bytes, digest and RFC-6962 leaf. See
[`ck003/dq-006-closure/DQ-006-CLOSURE.md`](../dq-006-closure/DQ-006-CLOSURE.md).

The *specification* gate recorded above remains **OPEN**: blockers 1 (Chief Architect approval),
2 (APS-200 §8 normative amendment), 3 (APS-300 reconciliation) and 6 (version/migration rule) are
unaffected by DQ-006. Blockers 4 and 5 are satisfied by the frozen CANONICAL-001 fixture and the
CROSS-LANGUAGE-001 equality evidence for that fixture.

The two statuses are not in conflict: DQ-006 closes what was executed and verified; it does not
amend normative APS text.

# GATE A — APS-001 Specification Closure Matrix

**Classification:** DECISION / WORKING  
**Status:** OPEN — EXECUTION CONTROL  
**Review date:** 2026-08-20  
**Branch:** `ck003/specification-integration-dq006`

## Authority baseline

Current APS-001 is `0.2-DRAFT`, `DRAFT — ARCHITECTURE REVIEW REQUIRED`. It defines the protocol execution lifecycle, fail-closed model, canonical-byte requirement, hash-domain model, conformance requirements, version binding and release gate.

The CK-003 execution state has materially advanced since the original Gate A snapshot. DQ-006 has a recorded PASS/CLOSED decision based on independent RI-PY/RI-RS CANONICAL-001 evidence, and DQ-002 has a recorded PASS/CLOSED hash-domain decision. APS-200 §8 is now being reconciled with that evidence on this branch.

## Closure matrix

| Item | Current evidence | Gate A status | Required next action |
|---|---|---|---|
| APS-001 scope/execution lifecycle | APS-001 §1–2 | SUBSTANTIALLY DEFINED | Architecture review |
| DQ-002 hash-domain | `closures/DQ-002_FINAL_CLOSURE.md`; CK-003 evidence | CLOSED / PASS | Preserve closure; trace into APS-001/APS-200 |
| DQ-003 version semantics | `ck003/decisions/DQ-003/current_versioning_snapshot.md`; APS-001 §12 | OPEN | Final compatibility matrix + version-binding fixtures + RI-PY/RI-RS conformance |
| DQ-004 event semantics | `ck003/DQ-004_EVENT_TYPE_SEMANTICS.md`; registry contract | BLOCKED FOR FINAL CLOSURE | Approve normative event vocabulary + payload registry + fixtures + RI-PY/RI-RS tests |
| Canonical serialization | DQ-006 closure; CROSS-LANGUAGE-001 PASS; APS-200 §8 reconciliation on this branch | DECIDED / VERIFIED; INCORPORATION IN REVIEW | Review/merge APS-200 §8 update; keep JCS conformance-only |
| APS-300 evidence cryptographic binding | APS-300 + DQ-006 closure evidence | OPEN | Reconcile evidence binding with frozen canonical/hash contract |
| INV-001…INV-015 coverage | `ck003/APS001_INV_MATRIX/INV-001_015_CONFORMANCE_MATRIX.md`; CONF-001…015 | OPEN | Close missing executable mappings/evidence one invariant at a time |
| Canonical fixture corpus | `fixtures/corpus/` contains FIX-INV-007…015 + CANONICAL-001 | PARTIAL | Reconcile all mandatory APS-500 fixtures and produce complete manifest/digests |
| RI-PY / RI-RS equality | CROSS-LANGUAGE-001 evidence under DQ-006 | PASS for CANONICAL-001 only | Generalize to full shared corpus |
| CI gate | No repository-native specification CI gate evidenced in current tree | OPEN | Build specification conformance runner + CI gate |
| Architecture Review | APS-001 explicitly requires approval | OPEN | Final review after Gate A/B/C evidence is complete |

## Blocking rule

APS-001 MUST NOT be promoted to approved v1.0 while any mandatory semantic dependency remains unresolved or lacks an executable verification path.

A decision recorded as CLOSED in CK-003 is not sufficient by itself to mark APS-001 approved: the decision MUST also be incorporated into the normative APS layer where the contract belongs and remain traceable to executable evidence.

## Current execution state

```text
DQ-006 canonical serialization
        PASS / CLOSED
              ↓
DQ-002 hash-domain
        PASS / CLOSED
              ↓
APS-200 §8 incorporation
        IN REVIEW ON THIS BRANCH
              ↓
DQ-003 version semantics
        OPEN
              ↓
DQ-004 event semantics
        BLOCKED FOR FINAL CLOSURE
              ↓
INV-001…INV-015
        OPEN / PARTIAL EVIDENCE
              ↓
fixture corpus
        PARTIAL
              ↓
full RI-PY / RI-RS corpus
        OPEN
              ↓
CI
        OPEN
              ↓
Release / Architecture Review
        BLOCKED
```

## Execution order

`APS-200 canonical incorporation → DQ-003 → DQ-004 → INV-001…015 → complete fixture corpus → RI-PY → RI-RS → cross-language corpus equality → CI → Release Gate`.

The already-completed CANONICAL-001 equality gate is retained as the first verified cross-language canonical fixture and MUST NOT be treated as proof of full corpus conformance.

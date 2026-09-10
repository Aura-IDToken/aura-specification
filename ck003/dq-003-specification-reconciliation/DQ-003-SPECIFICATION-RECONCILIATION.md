# DQ-003 — Specification Reconciliation Control Record

**Classification:** CUSTODIAN / TRACEABILITY — non-normative control artifact  
**Status:** OPEN — reconciliation in progress  
**Scope:** APS-200 §6–§10, canonical serialization authority, ENT-007 event vocabulary, session semantics, chain-link semantics  
**Branch boundary:** `dq-003/specification-reconciliation` → `main`  
**Rule:** This document records evidence and gates. It does not create or amend normative protocol semantics.

## 1. Purpose

This record is the control boundary between DQ-003 conformance evidence and specification authority.

No implementation work for ENT-007 composition, RI-RS production composition, RI-PY remediation, or C4 may use this record as authority to infer missing protocol semantics.

The governing principle is:

```text
normative specification
        ↓
Custodian decision
        ↓
contract freeze
        ↓
implementation
```

and not implementation → protocol interpretation.

## 2. Current APS-200 baseline

The current `main` copy of `aps/APS-200_CANONICAL_DATA_MODEL.md` contains §6 Relationships, §7 Validation Rules, §8 Serialization Requirements, §9 JSON Schema, and §10 Traceability.

ENT-007 is defined with `event_type`, `sequence_number`, `previous_record_hash`, and `event_payload_hash`. The `event_type` vocabulary is delegated to `aps/EVENT_TYPE_REGISTRY.md`.

APS-200 §8 makes RFC 8785 JCS the normative JSON canonicalization profile and defines canonical UTF-8 bytes as the cryptographic serialization boundary.

## 3. Authority map

| Question | Authority | Status |
|---|---|---|
| Canonical JSON serialization | APS-200 §8 | **ESTABLISHED** |
| Hash/Merkle domain model | APS-001 §7.1; APS-200 §8 binds canonical bytes | **ESTABLISHED** |
| Evidence hash byte domain | APS-300 §5 | **VERIFY BEFORE C4** |
| ENT-007 event vocabulary | Event-Type Registry / DQ-004 | **CUSTODIAN INPUT** |
| Session semantics | APS-200 / DQ-003 corpus | **CUSTODIAN INPUT** |
| `previous_record_hash` relation | ENT-007 + approved fixture | **ESTABLISHED; diagram audit OPEN** |
| C4 | DQ-003 Custodian gate | **NOT AUTHORIZED** |

## 4. G-1 — APS-200 §6–§10 integrity

Commit `9682cf53956f27c18821ac29531a356c5ed4afa5` explicitly reconciled the DQ-006 canonical serialization contract into APS-200 and consolidated the former §8.1–§8.9 proposal into the current normative §8.

The current `main` APS-200 file contains §6–§10. Reconciliation MUST therefore audit reference integrity against current `main`, not reconstruct historical text.

**G-1: OPEN — reference-integrity audit required. No normative rewrite authorized.**

## 5. G-1b — §8.1–§8.x references

The historical DQ-006 scan records the former §8.1–§8.9 structure as reconciled into current §8. The superseded proposal explicitly says it must not be cited as normative.

Required work:

1. inventory live references to `APS-200 §8.1`, `§8.2`, etc.;
2. classify each as current, historical, or broken/ambiguous;
3. update only broken live references;
4. preserve historical artifacts;
5. do not recreate obsolete subsection structure merely to satisfy stale references.

**G-1b: OPEN — reference reconciliation.**

## 6. G-3 — `AUDIT_DECISION`

The current Event-Type Registry states that no individual event token has final normative status and that strict conformance MUST reject an event type absent from an approved registry.

Therefore `AUDIT_DECISION` cannot become normative by changing a fixture or verifier. Custodian must decide whether it is a protocol event and, if so, approve its complete registry entry.

**G-3: BLOCKED — CUSTODIAN INPUT REQUIRED.**

## 7. G-5 — session semantics

APS-200 defines `sequence_number` as monotonically increasing within a session, but the reconciliation gate requires explicit session boundaries sufficient for chain, replay, genesis and verification semantics.

No implementation is authorized to infer those semantics.

Custodian decision must define at minimum:

- session identity/boundary;
- genesis condition;
- first-record sequence semantics;
- chain termination/restart semantics;
- verification boundary between sessions.

**G-5: BLOCKED — CUSTODIAN INPUT REQUIRED.**

## 8. G-6 — chain-link documentation

The DQ-003 evidence distinguishes `audit_record_hash` from `integrity_hash`. The approved fixture semantics use the previous Audit Record's `audit_record_hash` as the next record's `previous_record_hash`.

Any diagram showing `integrity_hash → next.previous_record_hash` is inconsistent if it claims to describe the normative chain relation.

Required action is documentation reconciliation only. The established hash preimage/domain MUST NOT be changed.

**G-6: OPEN — documentation reconciliation.**

## 9. Explicit non-actions

Until the Custodian gates above are resolved, this workstream MUST NOT:

- implement ENT-007 production composition;
- change `0x02 || JCS(R_AR)`;
- redefine `audit_record_hash` or `integrity_hash`;
- modify the Golden Fixture solely to satisfy implementation behaviour;
- add `AUDIT_DECISION` without Custodian approval;
- define session semantics in RI-RS or RI-PY;
- begin RI-PY remediation;
- authorize C4;
- close DQ-003.

## 10. Exit criteria

C4 authorization may be requested only when all are evidenced:

- [ ] APS-200 §6–§10 intact on the approved baseline;
- [ ] all live §8.x references resolve to current §8 or are explicitly historical;
- [ ] no superseded §8 proposal is treated as normative;
- [ ] `AUDIT_DECISION` registry status resolved by Custodian;
- [ ] session semantics explicitly resolved;
- [ ] chain-link documentation agrees with `audit_record_hash → previous_record_hash`;
- [ ] hash domains remain unchanged from approved DQ-002/DQ-003 decisions;
- [ ] Golden Fixture is accepted or rejected on normative grounds;
- [ ] no unresolved Critical specification contradiction remains.

Only then:

```text
SPECIFICATION RECONCILED
        ↓
CUSTODIAN SIGN-OFF
        ↓
C4 AUTHORIZED
```

## 11. Evidence references

- `aps/APS-200_CANONICAL_DATA_MODEL.md`
- `specification/APS-001_PROTOCOL_SPECIFICATION.md`
- `aps/EVENT_TYPE_REGISTRY.md`
- `ck003/dq-006-canonical-serialization/APS-200-SECTION-8-PROPOSED.md` — historical/superseded only
- `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` — historical reconciliation evidence
- commit `9682cf53956f27c18821ac29531a356c5ed4afa5` — CK-003 APS-200 reconciliation

# DQ-003 — Specification Reconciliation Control Record

**Classification:** CUSTODIAN / TRACEABILITY — non-normative control artifact
**Status:** OPEN — reconciliation in progress
**Scope:** APS-200 §6–§10, canonical serialization authority, ENT-007 event vocabulary, session semantics, chain-link semantics
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

and not:

```text
implementation
        ↓
protocol interpretation
```

## 2. Current APS-200 baseline

The current `main` copy of `aps/APS-200_CANONICAL_DATA_MODEL.md` is a DRAFT normative specification and currently contains §6 Relationships, §7 Validation Rules, §8 Serialization Requirements, §9 JSON Schema, and §10 Traceability.

ENT-007 is defined with `event_type`, `sequence_number`, `previous_record_hash`, and `event_payload_hash`. The `event_type` vocabulary is explicitly delegated to `aps/EVENT_TYPE_REGISTRY.md`.

APS-200 §8 currently makes RFC 8785 JCS the normative JSON canonicalization profile and defines canonical UTF-8 bytes as the cryptographic serialization boundary.

## 3. Authority map

| Question | Current authority | Reconciliation status |
|---|---|---|
| Canonical JSON serialization | APS-200 §8 | **ESTABLISHED** |
| Hash/Merkle domain model | APS-001 §7.1, with APS-200 §8 binding canonical bytes | **ESTABLISHED** |
| Evidence hash byte domain | APS-300 §5 | **VERIFY BEFORE C4** |
| ENT-007 event vocabulary | Event-Type Registry / DQ-004 | **CUSTODIAN INPUT REQUIRED** |
| Session semantics | APS-200 / DQ-003 corpus | **CUSTODIAN INPUT REQUIRED** |
| `previous_record_hash` chain relation | ENT-007 contract + approved fixture | **ESTABLISHED FOR CURRENT FIXTURE; DIAGRAM AUDIT OPEN** |
| C4 authorization | DQ-003 Custodian gate | **NOT AUTHORIZED** |

## 4. G-1 — APS-200 §6–§10 integrity

### Observation

Historical CK-003 material shows that commit `9682cf5...` explicitly reconciled DQ-006 canonical serialization into APS-200 and replaced the former §8.1–§8.9 serialization structure with a consolidated normative §8. The commit message identifies this as incorporation of the DQ-006 canonical serialization contract into APS-200.

The current `main` APS-200 file contains §6–§10, including the current §8 JCS profile.

### Control conclusion

The historical deletion/regression must **not** be reconstructed by inventing missing text. Current `main` is the baseline to be audited for reference integrity.

**G-1 status: RECONCILIATION REQUIRED — no normative edit authorized by this record.**

Closure requires a reference scan proving that current references to APS-200 §6–§10 resolve to existing, authoritative sections and that no higher-authority document is silently relying on the superseded §8 structure.

## 5. G-1b — §8.1–§8.x reference integrity

The historical DQ-006 consistency scan recorded the pre-reconciliation §8.1–§8.9 structure as reconciled into the current APS-200 §8. The superseded proposal explicitly states that it was accepted into APS-200 §8 and must not be cited as normative.

Therefore this gate is **not** permission to recreate §8.1–§8.9 headings from the historical proposal.

Required action:

1. inventory all live references to `APS-200 §8.1`, `§8.2`, …;
2. classify each as valid current reference, historical reference, or broken/ambiguous reference;
3. update only broken references to point to the current normative §8 text;
4. preserve historical artifacts as historical evidence;
5. do not alter normative semantics solely to satisfy a stale subsection citation.

**G-1b status: OPEN — reference reconciliation.**

## 6. G-3 — `AUDIT_DECISION` event vocabulary

Current `aps/EVENT_TYPE_REGISTRY.md` explicitly states that no individual event token has yet been promoted to final normative status. It also requires strict conformance implementations to reject event types absent from an approved registry.

Therefore a fixture containing `AUDIT_DECISION` cannot be made normatively valid merely by changing the verifier or copying the token from implementation behaviour.

Custodian must decide whether `AUDIT_DECISION` is a normative Aura event type and, if so, approve its registry entry including semantic meaning, producer, payload schema, introduced protocol version, and lifecycle status.

**G-3 status: BLOCKED — CUSTODIAN INPUT REQUIRED.**

## 7. G-5 — session semantics

`sequence_number` is currently defined as monotonically increasing within a session. The current specification corpus does not provide a sufficiently explicit, closed definition of session boundaries for all chain/replay/genesis cases needed by C4.

No implementation is authorized to infer session semantics from existing code.

Custodian decision must define at minimum:

- session identity/boundary;
- genesis condition;
- first-record sequence semantics;
- chain termination/restart semantics;
- verification boundary between sessions.

**G-5 status: BLOCKED — CUSTODIAN INPUT REQUIRED.**

## 8. G-6 — chain-link diagram consistency

The current DQ-003 evidence distinguishes `audit_record_hash` from `integrity_hash`. The approved fixture semantics use the previous Audit Record's `audit_record_hash` as the next record's `previous_record_hash`.

Any diagram showing `integrity_hash → next.previous_record_hash` is therefore a documentation inconsistency if it purports to describe the normative chain relation.

Required action is a diagram/text reconciliation only. It must not redefine the established hash preimage or domain.

**G-6 status: OPEN — documentation reconciliation.**

## 9. Explicit non-actions

Until the Custodian gates above are resolved, this workstream MUST NOT:

- implement ENT-007 production composition;
- change `0x02 || JCS(R_AR)`;
- redefine `audit_record_hash` or `integrity_hash`;
- modify the Golden Fixture solely to satisfy implementation behaviour;
- add `AUDIT_DECISION` to the registry without Custodian approval;
- define session semantics in RI-RS or RI-PY;
- begin RI-PY remediation;
- authorize C4;
- close DQ-003.

## 10. Exit criteria for specification reconciliation

The reconciliation workstream may request C4 authorization only when all of the following are evidenced:

- [ ] APS-200 §6–§10 are intact on the approved baseline;
- [ ] all live §8.x references resolve to the current normative §8 or are explicitly historical;
- [ ] no superseded §8 proposal is treated as normative;
- [ ] `AUDIT_DECISION` registry status is resolved by Custodian;
- [ ] session semantics are explicitly resolved;
- [ ] chain-link documentation agrees with `audit_record_hash → previous_record_hash`;
- [ ] hash domains remain unchanged from the approved DQ-002 / DQ-003 decisions;
- [ ] Golden Fixture is accepted or rejected on normative grounds, not implementation convenience;
- [ ] no unresolved Critical specification contradiction remains.

Only after these checks may the status transition to:

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

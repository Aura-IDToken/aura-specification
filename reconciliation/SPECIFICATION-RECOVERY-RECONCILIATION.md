# Specification Recovery & Reconciliation — APS-200 §6–§10

**Scope:** read-only recovery audit against `origin/main`
**Baseline:** `main` @ `8a2706969f65707817486a865af356f2398cf275`
**Branch:** `specification-recovery/reconciliation-aps200`
**Status:** IN PROGRESS — no normative or implementation remediation applied
**Decision boundary:** specification integrity / reference integrity only

## 1. Executive decision

The current `origin/main` APS-200 is the recovery baseline. It contains §§6–10 and therefore remains the authoritative reference for this reconciliation.

This work does **not** authorize:

- ENT-007 implementation;
- RI-PY remediation;
- RI-RS adapter work;
- Golden Fixture modification;
- hash-domain reinterpretation;
- C4 execution;
- DQ-003 closure.

The objective is to classify existing references and dependent artifacts as `CURRENT`, `HISTORICAL`, `BROKEN`, or `AMBIGUOUS`, and to surface Custodian decisions without inventing missing normative content.

## 2. APS-200 recovery baseline

`origin/main` contains:

- §1 Purpose
- §2 Design Principles
- §3 Core Entities
- §4 Common Object Contract
- §5 Entity Definitions
- §6 Relationships
- §7 Validation Rules
- §8 Serialization Requirements
- §9 JSON Schema
- §10 Traceability

ENT-007 is explicitly defined as `Audit Record`. Its current fields include `event_type`, `sequence_number`, `previous_record_hash`, and `event_payload_hash`; the common object contract supplies `object_id`, `object_type`, `protocol_version`, `schema_version`, `created_at`, and `integrity_hash`.

## 3. Recovery finding G-1 — §6–§10

**Status: BLOCKED / recovery integrity issue**

`origin/main` contains the complete top-level sections §6–§10. Earlier DQ-003 work identified a branch commit (`bf33eb4`, `spec(dq-003): define EP-001 event payload contract`) that removed the tail containing §§6–10 while adding EP-001 material. This report does not restore or rewrite that branch history; it records `origin/main` as the baseline against which recovery must be performed.

### Required action

Perform a byte/content comparison between the affected DQ-003 branch and `origin/main`, then determine the minimal intentional restoration. Do not reconstruct §6–§10 from downstream references.

## 4. §8 authority

`origin/main` §8 states that the normative JSON interoperability profile uses RFC 8785 JCS and defines the canonical boundary as UTF-8 bytes emitted by that profile. It also defines the existing `0x00` leaf and `0x01` interior-node domains.

This recovery audit therefore treats §8 as normative authority for canonical serialization. DQ-003's `0x02 || JCS(R_AR)` audit-record domain remains a separate later addition and must not be conflated with the §8 Merkle domains.

## 5. G-1b — §8.x references

**Status: CUSTODIAN INPUT / AMBIGUOUS**

The current `origin/main` APS-200 has a top-level §8 but no numbered §8.1–§8.9 subdivisions in the file itself. Nevertheless, the repository contains artifacts referring to `APS-200 §8.1`, `§8.2`, etc., including DQ-006 closure material.

Classification rule:

- a reference that accurately means the current §8 but uses stale subdivision numbering → `HISTORICAL/BROKEN REFERENCE`;
- a reference whose intended subsection cannot be established from primary sources → `AMBIGUOUS`;
- do not invent §8.1–§8.x normative structure solely to satisfy references.

### Custodian decision required

Either author a deliberate subsection structure for §8, or reconcile the affected references to the existing top-level §8. This is a normative structuring decision and is not performed by this audit.

## 6. G-3 — Event-Type Registry

**Status: CUSTODIAN INPUT / OPEN**

`aps/EVENT_TYPE_REGISTRY.md` is explicitly marked `DRAFT — DQ-004 closure artifact`. It states that no individual event token is currently promoted to final normative status, while strict conformance must reject unregistered tokens.

Therefore an `AUDIT_DECISION` or `AUDIT_RECORD` token appearing in a fixture cannot be promoted to normative vocabulary by inference from implementation evidence.

### Required Custodian action

Determine the normative vocabulary and register the required event token(s), including the registry fields required by the current registry contract. Resolve any fixture that depends on an unregistered token only after the vocabulary decision. Do not change Golden Fixture bytes merely to bypass registry validation.

## 7. G-5 — session semantics

**Status: CUSTODIAN INPUT / OPEN**

APS-200 currently requires `sequence_number` to be monotonically increasing within a session. The recovery audit finds no single closed session lifecycle contract sufficient to define, without inference, all of:

- session boundary/start;
- genesis ownership;
- sequence-number scope;
- restart semantics;
- chain verification boundary;
- session termination.

This is not currently a hash-preimage ambiguity. The existing hash domains must not be altered to solve it.

### Required Custodian action

Define the minimum normative session lifecycle required for replay and verification. Do not infer a new session model from RI-PY or RI-RS implementation behaviour.

## 8. G-6 — chain-link documentation

**Status: OPEN / non-byte-bearing documentation correction**

The recovery target is:

```text
record[n].audit_record_hash
        ↓
record[n+1].previous_record_hash
```

and not:

```text
record[n].integrity_hash
        ↓
record[n+1].previous_record_hash
```

The correction must align the diagram with the normative chain rule and the Golden Fixture. It must not redefine `integrity_hash`, `audit_record_hash`, or `chain_hash`.

## 9. Stable decisions carried forward

The following are treated as frozen for this recovery pass:

- RFC 8785 JCS is the canonical JSON serialization profile;
- canonical bytes are UTF-8 JCS output;
- `event_payload_hash` is computed from canonical Event Payload bytes;
- `audit_record_hash` uses the DQ-003 domain `SHA-256(0x02 || JCS(R_AR))`;
- `integrity_hash` excludes itself from its preimage;
- `previous_record_hash[n+1] = audit_record_hash[n]`;
- `audit_record_hash`, `integrity_hash`, and legacy `chain_hash` are not interchangeable absent an explicit normative rule;
- Golden Fixture is not modified during specification recovery.

## 10. Blast-radius map

```text
APS-200 §6–§10
      │
      ├── §6 Relationships
      │      └── ENT-002 → ENT-003 → ENT-005 → ENT-006 → ENT-007
      │
      ├── §7 Validation Rules
      │      └── structure / type / required / integrity / invariants
      │
      ├── §8 Serialization
      │      ├── RFC 8785 JCS
      │      ├── SHA-256(B)
      │      ├── 0x00 leaf
      │      └── 0x01 interior node
      │
      ├── §9 JSON Schema
      │      ├── fixtures/schemas/
      │      └── EVENT_TYPE_REGISTRY
      │
      └── §10 Traceability
             ├── INV-003 / INV-012
             ├── EVID-AUDIT
             └── CONF-003 / CONF-012

            ↓
     DQ-006 / DQ-003 / DQ-004
            ↓
     Golden Fixture / RI-PY / RI-RS
            ↓
           C4
```

## 11. Current decision matrix

| Finding | Classification | Byte-bearing | Normative | Action | C4 |
|---|---|---:|---:|---|---|
| G-1 §6–§10 | BROKEN/REGRESSION ON AFFECTED BRANCH | No | Yes | recover from `origin/main` | BLOCK |
| G-1b §8.x | AMBIGUOUS | No | Yes | Custodian structure/reconciliation decision | BLOCK |
| G-3 registry | OPEN / CUSTODIAN INPUT | No | Yes | approve/register vocabulary | BLOCK |
| G-5 session | OPEN / CUSTODIAN INPUT | No under current contract | Yes | define session lifecycle | BLOCK |
| G-6 diagram | OPEN | No | documentation | correct chain-link depiction | no direct block after proof |
| G-2 0x02 | CLOSED | Yes | Yes | no semantic change | — |
| G-9 normalization | CLOSED | Potentially | Yes | no semantic change | — |
| C1 JCS | PASS | Yes | Yes | freeze | — |
| C2-1 input boundary | PASS | Yes | Yes | freeze | — |

## 12. Recovery rule

This document is a reconciliation control record. It does not amend APS-200 and does not create new protocol semantics.

Where the current corpus is insufficient to decide a normative point, the result is explicitly `CUSTODIAN INPUT REQUIRED` rather than an inferred resolution.

## 13. Exit criteria

Specification recovery may advance to normative freeze only when:

1. G-1 is closed against `origin/main` with no silent loss of §6–§10;
2. all §8.x references are classified and either reconciled or explicitly retained as historical;
3. G-3 event vocabulary is normatively resolved;
4. G-5 session semantics are defined;
5. G-6 chain-link documentation is corrected;
6. the resulting reference graph has no unresolved normative contradiction affecting ENT-007.

Only after those criteria are met may C4 authorization be considered.

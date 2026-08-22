# P0-2 — ENT-007 Audit Record Field-by-Field Hash Domain Matrix

**Status:** REVIEW GATE — NOT FROZEN  
**Branch:** `dq/dq-003-audit-record-hash-domain`  
**Contract:** APS-200 ENT-007 / Audit Record Contract v0  
**Purpose:** Resolve the field-level canonical and hash-domain contract before implementation remediation and Golden Fixture freeze.

> **Important:** This matrix records only what is currently supported by the specification and explicitly marks unresolved semantics as `TBD`. A `TBD` is a specification gap, not an implementation assumption.

## 1. Authority and current baseline

APS-200 currently defines ENT-007 as an immutable auditable event record with the Common Object Contract plus `event_type`, `sequence_number`, `previous_record_hash`, and `event_payload_hash`. fileciteturn122file0L2-L2

APS-200 §4 currently requires the Common Object Contract fields `object_id`, `object_type`, `protocol_version`, `schema_version`, `created_at`, and `integrity_hash`; `integrity_hash` is defined as SHA-256 of the object's canonical bytes excluding itself. fileciteturn122file0L2-L2

APS-200 §8 establishes RFC 8785 JCS as the normative JSON canonicalization profile and defines the canonical boundary as the UTF-8 byte sequence emitted by JCS. It also defines `0x00`/`0x01` for RFC 6962-style Merkle leaf/interior hashing. fileciteturn122file0L2-L2

The current P0-2 Candidate C decision additionally proposes a dedicated Audit Record domain `0x02` and an `audit_record_hash`, but the exact ENT-007 field inclusion/exclusion and the complete `integrity_hash` preimage remain a review item. This matrix therefore does **not** silently promote those unresolved points to frozen normative text.

## 2. Status vocabulary

| Mark | Meaning |
|---|---|
| **NORMATIVE** | Already explicitly supported by the current specification. |
| **CANDIDATE** | Proposed by the current DQ-003 Contract v0 work, but not yet frozen in APS-200. |
| **TBD** | Insufficient normative definition; must be resolved before P0-2 freeze. |
| **N/A** | Field is not itself part of that hash's input by definition. |

## 3. ENT-007 field matrix

| Field | Type | Required / Optional | Canonical encoding | In `event_payload_hash`? | In `audit_record_hash`? | In `integrity_hash`? | Derived allowed? | Genesis behavior | Verification rule | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `object_id` | string | MUST | JCS string value | N/A | **YES — candidate** | YES, unless excluded by future integrity profile | NO; supplied identity | Normal object identity; no special genesis value defined | Validate canonical identity and uniqueness scope | CANDIDATE |
| `object_type` | string | MUST | JCS string value | N/A | **YES — candidate** | YES | NO | `AuditRecord` (canonical type name) | Must equal registered ENT-007 type | CANDIDATE |
| `protocol_version` | string | MUST | JCS string value | N/A | **YES — candidate** | YES | NO | Contract-defined version | Must match supported APS/protocol profile | CANDIDATE |
| `schema_version` | string | MUST | JCS string value | N/A | **YES — candidate** | YES | NO | Contract-defined schema version | Must match ENT-007 schema profile | CANDIDATE |
| `created_at` | string (ISO 8601 UTC) | MUST | JCS string value; exact timestamp grammar still subject to upstream contract | N/A | **YES — candidate** | YES | NO | Not applicable; genesis is represented by predecessor sentinel | Validate syntax and UTC requirement | CANDIDATE |
| `integrity_hash` | string | MUST | JCS string value when represented in the object | N/A | **NO — Candidate C** | **NO — self excluded by APS-200** | YES; derived | Not applicable | Recompute using the separately defined integrity preimage | CANDIDATE / GAP |
| `event_type` | string | MUST | JCS string value; vocabulary from `aps/EVENT_TYPE_REGISTRY.md` | N/A | **YES — candidate** | YES | NO | Not applicable | Validate registry membership | CANDIDATE |
| `sequence_number` | integer | MUST | JCS integer representation | N/A | **YES — candidate** | YES | NO | Genesis record is sequence `0` only if that is explicitly adopted; otherwise TBD | Validate monotonicity within session | TBD |
| `previous_record_hash` | string | MUST | JCS string value containing canonical hash representation | N/A | **YES — candidate** | YES | NO | **Candidate:** 32 zero bytes represented according to the final hash-string encoding rule | Verify equals predecessor `audit_record_hash`; genesis must equal sentinel | CANDIDATE / GAP |
| `event_payload_hash` | string | MUST | JCS string value containing canonical hash representation | **NO — candidate** (the payload hash is the result of hashing the payload) | **YES — candidate** | YES | YES, but only as deterministic derivation from payload | Not applicable | Recompute from event payload and compare | CANDIDATE |

## 4. Critical dependency matrix

### 4.1 `audit_record_hash`

**Candidate C definition:**

```text
AuditRecordHashPreimage =
    0x02 ||
    JCS(
        ENT-007 record
        excluding:
            audit_record_hash
            integrity_hash
    )

 audit_record_hash = SHA-256(AuditRecordHashPreimage)
```

This creates the required non-circular dependency:

```text
source fields
   ├───────────────┐
   ▼               ▼
event_payload_hash  audit_record_hash
                       │
                       ▼
               previous_record_hash
```

**Decision status:** CANDIDATE. The `0x02` domain and exact exclusion list must be accepted as the frozen P0-2 contract before Golden Fixture creation.

### 4.2 `integrity_hash`

APS-200 currently defines:

```text
integrity_hash = SHA-256(canonical_bytes(object excluding integrity_hash))
```

and explicitly states that a digest field cannot cover its own value. fileciteturn122file0L2-L2

For ENT-007, the exact relationship between this existing Common Object Contract and Candidate C `audit_record_hash` is **not yet fully specified**.

The following must be resolved before freeze:

1. Whether `integrity_hash` is computed over the full ENT-007 object excluding itself, including `audit_record_hash`.
2. Whether `audit_record_hash` is excluded from the `integrity_hash` preimage as well.
3. Whether `integrity_hash` has a dedicated domain separator.
4. Whether `integrity_hash` is intended to be a general object integrity digest while `audit_record_hash` is the chain identity digest.

**Current safe interpretation for the DQ-003 experiment:** `integrity_hash` MUST NOT be an input to `audit_record_hash`. The reverse dependency remains **TBD** until the P0-2 contract explicitly resolves it.

### 4.3 `previous_record_hash`

Candidate chain rule:

```text
record[n].previous_record_hash
    = record[n-1].audit_record_hash
```

Genesis:

```text
record[0].previous_record_hash
    = 32-byte zero sentinel
```

The exact textual/byte encoding of the stored hash string and the formal genesis encoding must be frozen before fixture generation.

## 5. Hash-domain separation

Current APS-200 already defines RFC 6962-style Merkle domains:

```text
leaf       = SHA-256(0x00 || canonical_bytes)
interior   = SHA-256(0x01 || left_digest || right_digest)
```

The proposed DQ-003 record domain is distinct:

```text
Audit Record = SHA-256(0x02 || canonical_record_preimage)
```

This is a **domain separation rule**, not a replacement of the Merkle profile. The three domains must remain semantically distinct:

```text
0x00 → Merkle leaf
0x01 → Merkle interior node
0x02 → Audit Record hash
```

**Status:** Candidate pending P0-2 approval.

## 6. Event payload boundary

APS-200 ENT-007 currently requires `event_payload_hash`, but the current ENT-007 section does not itself define the exact payload object/field boundary or the canonical payload serialization input. fileciteturn122file0L2-L2

Therefore the matrix intentionally records:

```text
event_payload_hash = SHA-256(JCS(event_payload))
```

as the **Candidate C rule**, not yet frozen normative text.

Before P0-2 freeze, the contract must define:

- what constitutes `event_payload`;
- whether `event_payload` is an explicit ENT-007 field or a projection of other fields;
- whether `event_payload_hash` itself is included in the Audit Record hash preimage;
- whether payload canonicalization uses exactly the same JCS profile/version as the record.

## 7. Derived-field policy

| Field | May be derived? | Rule |
|---|---|---|
| `object_id` | NO | Identity supplied by producer; must be validated. |
| `object_type` | NO | Must be the canonical ENT-007 type. |
| `protocol_version` | NO | Contract metadata. |
| `schema_version` | NO | Contract metadata. |
| `created_at` | NO | Event/object creation value; not recomputed from hash. |
| `integrity_hash` | YES | Must be reproducible from its final normative preimage. |
| `event_type` | NO | Must come from the registered event vocabulary. |
| `sequence_number` | NO | Producer/session state; verifier checks monotonicity. |
| `previous_record_hash` | YES for verifier/reconstruction | Must equal predecessor `audit_record_hash`; genesis uses sentinel. |
| `event_payload_hash` | YES | Must recompute exactly from the defined payload. |

## 8. Verification contract required for P0-2 closure

A conformant verifier must be able to independently recompute at minimum:

```text
1. event_payload_hash
2. audit_record_hash
3. integrity_hash
4. previous_record_hash relationship
5. genesis condition
6. sequence monotonicity
7. canonical-byte equality
```

The verifier must reject:

- changed canonical source fields;
- changed event payload;
- changed `event_payload_hash`;
- changed `previous_record_hash`;
- changed `audit_record_hash`;
- changed `integrity_hash` when integrity validation is in scope;
- wrong hash domain prefix;
- non-canonical serialization.

These checks support INV-003 Canonical Serialization, INV-011 Cryptographic Integrity, and INV-012 Auditability. INV-012 explicitly requires required Audit Record fields, registered event type, and chain/integrity state. fileciteturn123file0L2-L2

## 9. P0-2 freeze blockers

P0-2 MUST NOT be frozen until all of the following are resolved with normative wording:

- [ ] Exact ENT-007 field set.
- [ ] Exact canonical inclusion/exclusion list.
- [ ] Exact `event_payload` boundary.
- [ ] Exact `event_payload_hash` preimage.
- [ ] Exact `audit_record_hash` preimage.
- [ ] Acceptance of `0x02` as the Audit Record domain separator.
- [ ] Exact `integrity_hash` preimage for ENT-007.
- [ ] Explicit `audit_record_hash` ↔ `integrity_hash` dependency direction.
- [ ] Exact `previous_record_hash` encoding.
- [ ] Exact genesis sentinel representation.
- [ ] Genesis sequence-number rule.
- [ ] Exact recomputation and verification failure conditions.
- [ ] Explicit compatibility relationship to RFC 6962 Merkle domains.

## 10. Gate

**Current decision: P0-2 remains OPEN.**

This matrix is the review instrument immediately before freeze. It is deliberately conservative: no unresolved field/domain rule is converted into an implementation requirement merely because it appears in an adapter design.

### Next gate

After all `TBD`/`CANDIDATE` rows are resolved:

```text
P0-2 field matrix
        ↓
Normative Contract update
        ↓
DQ-003-AUDIT-CHAIN-001 regeneration if required
        ↓
Golden Fixture freeze
        ↓
RI-PY conformance adapter
RI-RS conformance adapter
        ↓
Cross-language DQ-003
```

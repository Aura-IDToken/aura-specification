# P0-2 — ENT-007 Audit Record Field-by-Field Hash Domain Matrix

**Status:** REVIEW GATE — HASH DEPENDENCY RESOLVED / NOT YET FROZEN  
**Branch:** `dq/dq-003-audit-record-hash-domain`  
**Contract:** APS-200 ENT-007 / Audit Record Contract v0  
**Purpose:** Resolve the field-level canonical and hash-domain contract before implementation remediation and Golden Fixture freeze.

> **Important:** This matrix distinguishes current APS-200 normative text from DQ-003 Candidate C decisions. The hash dependency resolved below is a proposed normative clarification and is not considered frozen until the corresponding APS-200 contract text is approved.

## 1. Authority and current baseline

APS-200 currently defines ENT-007 as an immutable auditable event record with the Common Object Contract plus `event_type`, `sequence_number`, `previous_record_hash`, and `event_payload_hash`.

APS-200 §4 currently requires the Common Object Contract fields `object_id`, `object_type`, `protocol_version`, `schema_version`, `created_at`, and `integrity_hash`; `integrity_hash` is defined as SHA-256 of the object's canonical bytes excluding itself.

APS-200 §8 establishes RFC 8785 JCS as the normative JSON canonicalization profile and defines the canonical boundary as the UTF-8 byte sequence emitted by JCS. It also defines `0x00`/`0x01` for RFC 6962-style Merkle leaf/interior hashing.

The current DQ-003 Candidate C work proposes a dedicated Audit Record domain `0x02` and an `audit_record_hash`. The exact ENT-007 field inclusion/exclusion and the relationship between `audit_record_hash` and the existing Common Object Contract `integrity_hash` are therefore the critical P0-2 review points.

## 2. Status vocabulary

| Mark | Meaning |
|---|---|
| **NORMATIVE** | Already explicitly supported by the current specification. |
| **CANDIDATE** | Proposed by the current DQ-003 Contract v0 work and awaiting freeze in APS-200. |
| **RESOLVED-CANDIDATE** | Architectural decision made in DQ-003, but still requires normative specification update before freeze. |
| **TBD** | Insufficient normative definition; must be resolved before P0-2 freeze. |
| **N/A** | Field is not itself part of that hash's input by definition. |

## 3. ENT-007 field matrix

| Field | Type | Required / Optional | Canonical encoding | In `event_payload_hash`? | In `audit_record_hash`? | In `integrity_hash`? | Derived allowed? | Genesis behavior | Verification rule | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `object_id` | string | MUST | JCS string value | N/A | YES | YES | NO; supplied identity | Normal object identity; no special genesis value | Validate canonical identity and uniqueness scope | CANDIDATE |
| `object_type` | string | MUST | JCS string value | N/A | YES | YES | NO | `AuditRecord` | Must equal registered ENT-007 type | CANDIDATE |
| `protocol_version` | string | MUST | JCS string value | N/A | YES | YES | NO | Contract-defined version | Must match supported APS/protocol profile | CANDIDATE |
| `schema_version` | string | MUST | JCS string value | N/A | YES | YES | NO | Contract-defined schema version | Must match ENT-007 schema profile | CANDIDATE |
| `created_at` | string (ISO 8601 UTC) | MUST | JCS string value; exact timestamp grammar still subject to upstream contract | N/A | YES | YES | NO | Not applicable; genesis is represented by predecessor sentinel | Validate syntax and UTC requirement | CANDIDATE |
| `integrity_hash` | string | MUST | JCS string value when represented in the object | N/A | **NO** | **NO — self excluded** | YES | Not applicable | Recompute from the integrity preimage and compare | RESOLVED-CANDIDATE |
| `event_type` | string | MUST | JCS string value; vocabulary from `aps/EVENT_TYPE_REGISTRY.md` | N/A | YES | YES | NO | Not applicable | Validate registry membership | CANDIDATE |
| `sequence_number` | integer | MUST | JCS integer representation | N/A | YES | YES | NO | **Candidate:** genesis is `0` | Validate monotonicity within session | RESOLVED-CANDIDATE |
| `previous_record_hash` | string | MUST | JCS string value containing canonical hash representation | N/A | YES | YES | YES for verifier/reconstruction | **Candidate:** 32-byte zero sentinel for genesis | Verify equals predecessor `audit_record_hash`; genesis must equal sentinel | RESOLVED-CANDIDATE |
| `event_payload_hash` | string | MUST | JCS string value containing canonical hash representation | N/A — it is the digest output, not an input to its own computation | **YES** | YES | YES, from the defined payload | Not applicable | Recompute from event payload and compare | RESOLVED-CANDIDATE |

## 4. Resolved critical dependency: `audit_record_hash` ↔ `integrity_hash`

### 4.1 Normative direction

The DQ-003 decision is:

```text
canonical source fields
        │
        ├──────────────────────────┐
        ▼                          ▼
 audit_record_hash            integrity_hash
        │                          ▲
        │                          │
        └──────────────────────────┘
             integrity_hash commits
             to audit_record_hash
```

More precisely:

```text
A = ENT-007 record

A_without_derived_hashes =
    A excluding:
        audit_record_hash
        integrity_hash

B = JCS(A_without_derived_hashes)

C = 0x02 || B

audit_record_hash = SHA-256(C)
```

Then, after `audit_record_hash` has been computed:

```text
I = ENT-007 record

I_without_integrity_hash =
    I excluding:
        integrity_hash

integrity_hash = SHA-256(JCS(I_without_integrity_hash))
```

Because `audit_record_hash` is present in `I_without_integrity_hash`, **`integrity_hash` commits to the final `audit_record_hash` value**.

### 4.2 Dependency graph

The resulting dependency graph is deliberately one-way and acyclic:

```text
                    source fields
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
     event_payload_hash      audit_record_hash
              │                     │
              └──────────┬──────────┘
                         ▼
                 integrity_hash
                         │
                         ▼
                  next record's
              previous_record_hash
```

The critical asymmetry is:

```text
audit_record_hash  ──X──> integrity_hash
integrity_hash     ──X──> audit_record_hash
```

with the **only allowed dependency** being:

```text
audit_record_hash → integrity_hash
```

This is achieved by excluding `integrity_hash` from the `audit_record_hash` preimage while retaining `audit_record_hash` in the `integrity_hash` preimage.

### 4.3 Exact preimages

#### Audit Record hash

```text
canonical_audit_record_hash_input =
    JCS(
        ENT-007
        excluding audit_record_hash
        excluding integrity_hash
    )

audit_record_hash =
    SHA-256(
        0x02 || canonical_audit_record_hash_input
    )
```

`0x02` is one raw octet. It MUST NOT be represented as the ASCII characters `0x02`, the string `"02"`, or any other textual wrapper.

#### Integrity hash

The existing APS-200 Common Object Contract rule is retained:

```text
canonical_integrity_input =
    JCS(
        ENT-007
        excluding integrity_hash
    )

integrity_hash =
    SHA-256(canonical_integrity_input)
```

There is **no additional domain prefix proposed for `integrity_hash` at this stage**, because APS-200 currently defines it as the generic Common Object Contract integrity digest. Introducing a new prefix would be a separate protocol decision and is not required to solve DQ-003 dependency ordering.

### 4.4 Why this direction is preferred

This preserves two distinct semantics:

- `audit_record_hash` = **record identity / chain-link digest**, domain-separated with `0x02`;
- `integrity_hash` = **generic object integrity digest**, committing to the complete record including the already-computed `audit_record_hash` but excluding itself.

It also prevents a circular definition:

```text
integrity_hash → audit_record_hash → integrity_hash
```

and prevents the chain from depending on a mutable integrity field.

### 4.5 What is explicitly forbidden

The following are not conformant to this Candidate C decision:

```text
SHA-256(JCS(record including integrity_hash))
```

for `audit_record_hash`;

```text
SHA-256(JCS(record excluding audit_record_hash and integrity_hash))
```

for `integrity_hash` if the intent is to retain the APS-200 Common Object Contract rule;

or any adapter-level transformation that treats `integrity_hash`, certificate fingerprints, Merkle hashes, or legacy `chain_hash` as an alias for `audit_record_hash`.

## 5. `event_payload_hash`

Candidate C rule:

```text
event_payload_hash =
    SHA-256(
        JCS(event_payload)
    )
```

The `event_payload` boundary remains a separate P0-2 item. Once defined, the resulting `event_payload_hash` is included in the `audit_record_hash` preimage as a field of ENT-007. The raw payload itself is **not duplicated into the audit-record hash preimage** unless ENT-007 explicitly defines it as a field.

## 6. `previous_record_hash`

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

The stored representation is a canonical hash string; its exact encoding convention must be fixed in the normative contract before fixture freeze.

## 7. Hash-domain separation

Current APS-200 defines RFC 6962-style Merkle domains:

```text
leaf       = SHA-256(0x00 || canonical_bytes)
interior   = SHA-256(0x01 || left_digest || right_digest)
```

The DQ-003 Audit Record domain is distinct:

```text
Audit Record = SHA-256(0x02 || canonical_record_preimage)
```

Therefore:

```text
0x00 → Merkle leaf
0x01 → Merkle interior node
0x02 → Audit Record hash
```

These domains MUST remain semantically distinct.

## 8. Verification contract

A conformant verifier must independently recompute:

```text
1. event_payload_hash
2. audit_record_hash
3. integrity_hash
4. previous_record_hash relationship
5. genesis condition
6. sequence monotonicity
7. canonical-byte equality
```

The verifier must reject at minimum:

- changed canonical source fields;
- changed event payload;
- changed `event_payload_hash`;
- changed `previous_record_hash`;
- changed `audit_record_hash`;
- changed `integrity_hash`;
- wrong `0x02` domain prefix;
- non-canonical serialization.

## 9. Remaining P0-2 freeze blockers

The hash dependency is now **RESOLVED-CANDIDATE**, but P0-2 remains open until the normative contract is updated and the following are explicitly frozen:

- [ ] Exact ENT-007 field set including `audit_record_hash`.
- [ ] Exact canonical inclusion/exclusion list.
- [ ] Exact `event_payload` boundary.
- [ ] Exact `event_payload_hash` preimage.
- [ ] Acceptance of `0x02` as the Audit Record domain separator.
- [ ] Exact `previous_record_hash` string/byte encoding.
- [ ] Exact genesis sentinel representation.
- [ ] Genesis sequence-number rule.
- [ ] Exact recomputation and verification failure conditions.
- [ ] Explicit compatibility relationship to RFC 6962 Merkle domains.

## 10. Gate

**Current decision: P0-2 remains OPEN.**

The specific dependency question is resolved as a Candidate C architectural decision:

> **`audit_record_hash` is computed first from the canonical ENT-007 record excluding both derived hashes; `integrity_hash` is then computed over the canonical ENT-007 record excluding only `integrity_hash`, thereby committing to the already-computed `audit_record_hash`. There is no reverse dependency and no cycle.**

This decision must be promoted into normative APS-200 text before the Golden Fixture is frozen.

Next sequence:

```text
resolve remaining P0-2 fields
        ↓
update normative APS-200
        ↓
regenerate DQ-003-AUDIT-CHAIN-001 if required
        ↓
freeze Golden Fixture
        ↓
RI-PY conformance adapter
RI-RS conformance adapter
        ↓
Cross-language DQ-003
```

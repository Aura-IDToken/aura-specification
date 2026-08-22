# P0-2 — ENT-007 Audit Record Field-by-Field Hash Domain Matrix

**Status:** REVIEW GATE — HASH DEPENDENCY PROMOTED / NOT YET FROZEN  
**Branch:** `dq/dq-003-audit-record-hash-domain`  
**Contract:** APS-200 ENT-007 / Audit Record Contract v0  
**Purpose:** Resolve the field-level canonical and hash-domain contract before implementation remediation and Golden Fixture freeze.

> **Important:** The hash dependency has now been promoted into the APS-200 draft on this branch, but P0-2 remains open until all remaining field/domain gaps are resolved and the contract is explicitly frozen.

## 1. Current authority

APS-200 defines ENT-007 as an immutable auditable event record with the Common Object Contract plus `event_type`, `sequence_number`, `previous_record_hash`, `event_payload_hash`, and now `audit_record_hash`.

APS-200 §4 requires `integrity_hash` as the Common Object Contract digest excluding itself. APS-200 §5.1 now defines the `0x02` Audit Record hash domain and §5.2 defines the one-way dependency in which `integrity_hash` commits to the already-computed `audit_record_hash`.

## 2. ENT-007 field matrix

| Field | Type | Required | In `audit_record_hash`? | In `integrity_hash`? | Derived | Status |
|---|---|---:|---:|---:|---:|---|
| `object_id` | string | MUST | YES | YES | NO | OPEN detail review |
| `object_type` | string | MUST | YES | YES | NO | OPEN detail review |
| `protocol_version` | string | MUST | YES | YES | NO | OPEN detail review |
| `schema_version` | string | MUST | YES | YES | NO | OPEN detail review |
| `created_at` | string (ISO 8601 UTC) | MUST | YES | YES | NO | OPEN grammar review |
| `integrity_hash` | string | MUST | **NO** | **NO — self excluded** | YES | PROMOTED |
| `event_type` | string | MUST | YES | YES | NO | OPEN registry/profile review |
| `sequence_number` | integer | MUST | YES | YES | NO | PROMOTED: genesis `0` |
| `previous_record_hash` | string | MUST | YES | YES | verifier reconstruction | PROMOTED: predecessor `audit_record_hash` |
| `event_payload_hash` | string | MUST | YES | YES | YES | OPEN: payload boundary |
| `audit_record_hash` | string | MUST | **NO — self excluded** | YES | YES | PROMOTED |

All fields are JCS-encoded when present in a canonical ENT-007 object. Exact hash-string encoding and extension-field policy remain open until fixture freeze.

## 3. Resolved dependency: `audit_record_hash` ↔ `integrity_hash`

### 3.1 Audit Record hash preimage

For ENT-007 record `R`, define:

```text
R_AR = R excluding:
       audit_record_hash
       integrity_hash

AuditRecordHashPreimage(R) =
    0x02 || JCS(R_AR)

audit_record_hash(R) =
    SHA-256(AuditRecordHashPreimage(R))
```

`0x02` is one raw octet. It MUST NOT be represented as ASCII text, a hexadecimal string, or another textual wrapper.

### 3.2 Integrity hash preimage

The existing Common Object Contract rule remains:

```text
R_I = R excluding:
      integrity_hash

IntegrityPreimage(R) = JCS(R_I)

integrity_hash(R) = SHA-256(IntegrityPreimage(R))
```

Because `R_I` contains `audit_record_hash`, the integrity digest commits to the final Audit Record identity.

### 3.3 Dependency graph

```text
source fields
     │
     ├───────────────┐
     ▼               ▼
event_payload_hash  audit_record_hash
                         │
                         ▼
                  integrity_hash
                         │
                         ▼
          next.previous_record_hash
```

The only allowed hash dependency between the two digests is:

```text
audit_record_hash → integrity_hash
```

There is no reverse dependency and no cycle.

### 3.4 Explicit prohibitions

The following are non-conformant:

- including `integrity_hash` in the `audit_record_hash` preimage;
- excluding `audit_record_hash` from the ENT-007 `integrity_hash` preimage while claiming the Common Object Contract rule;
- treating `integrity_hash`, certificate fingerprints, Merkle hashes, or legacy `chain_hash` as aliases for `audit_record_hash`;
- allowing an adapter to invent a different hash domain.

## 4. Chain rule and genesis

For non-genesis record `R[n]`:

```text
R[n].previous_record_hash = R[n-1].audit_record_hash
```

Genesis uses a 32-byte all-zero digest sentinel. The first record uses `sequence_number = 0`; subsequent records increment monotonically within the session.

The exact stored string/byte encoding of the sentinel and digest fields remains a fixture-level freeze item.

## 5. Event payload boundary

Candidate rule:

```text
event_payload_hash = SHA-256(JCS(event_payload))
```

The exact `event_payload` boundary remains open. Once defined, `event_payload_hash` is included as an ENT-007 field in the `audit_record_hash` preimage; the raw payload is not duplicated unless explicitly defined as an ENT-007 field.

## 6. Domain separation

```text
0x00 → RFC 6962-style Merkle leaf
0x01 → RFC 6962-style Merkle interior node
0x02 → Audit Record hash
```

These domains are semantically distinct and MUST NOT be substituted for one another.

## 7. Verification contract

A conformant verifier must recompute:

```text
1. event_payload_hash
2. audit_record_hash
3. integrity_hash
4. predecessor linkage
5. genesis condition
6. sequence monotonicity
7. canonical-byte equality
```

It must reject modified source fields, payload/hash mismatch, incorrect predecessor linkage, incorrect derived hashes, incorrect `0x02` domain, or non-canonical serialization.

## 8. Remaining P0-2 freeze blockers

- [ ] Exact final ENT-007 field semantics and extension policy.
- [ ] Exact canonical inclusion/exclusion list.
- [ ] Exact `event_payload` boundary.
- [ ] Exact `event_payload_hash` preimage.
- [x] `audit_record_hash` preimage promoted to APS-200 §5.1.
- [x] `0x02` Audit Record domain promoted to APS-200 §5.1.
- [x] `integrity_hash` preimage/dependency promoted to APS-200 §5.2.
- [x] predecessor dependency on `audit_record_hash` promoted to APS-200 §5.3.
- [ ] Exact hash string/byte encoding.
- [x] Genesis sentinel defined as 32-byte zero digest; stored encoding remains open.
- [x] Genesis sequence-number rule defined as `0`.
- [ ] Exact machine-readable verification failure semantics.
- [x] Merkle `0x00`/`0x01` relationship retained and separated from `0x02`.

## 9. Gate

**P0-2 remains OPEN.**

The dependency decision is now promoted into the APS-200 draft on this branch:

> `audit_record_hash` is computed first from the canonical ENT-007 record excluding both derived hashes; `integrity_hash` is then computed over the canonical ENT-007 record excluding only `integrity_hash`, thereby committing to the already-computed `audit_record_hash`. There is no reverse dependency and no cycle.

This does not freeze the Golden Fixture and does not authorize RI-PY/RI-RS remediation yet.

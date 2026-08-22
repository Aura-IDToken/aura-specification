# P0-2 — ENT-007 Audit Record Field-by-Field Hash Domain Matrix

**Status:** FROZEN  
**Branch:** `dq/dq-003-audit-record-hash-domain`  
**Authority:** APS-200 §4, §5, §5.1–§5.7  
**Purpose:** Normative field inclusion/exclusion contract for ENT-007 and EP-001 conformance.

## 1. Frozen authority and scope

This matrix is derived directly from APS-200 on this branch and is frozen for the P0-2 conformance profile.

ENT-007 consists of the Common Object Contract fields plus:

- `event_type`
- `sequence_number`
- `previous_record_hash`
- `event_payload_hash`
- `audit_record_hash`

`integrity_hash` is inherited from the Common Object Contract and is a derived field.

The matrix distinguishes three concepts:

1. **Audit Record hash preimage** — `R_AR`, used only for `audit_record_hash`.
2. **Integrity hash preimage** — `R_I`, used only for `integrity_hash`.
3. **Event Payload preimage** — `JCS(P)`, used only for `event_payload_hash`.

## 2. Frozen ENT-007 inclusion/exclusion matrix

| Field | Type | Required | Event Payload Hash | Audit Record Hash | Integrity Hash | Derived? | Genesis behavior | Verification |
|---|---|---:|---|---|---|---|---|---|
| `object_id` | string | MUST | OUTSIDE payload | INCLUDE | INCLUDE | NO | ordinary | exact canonical value |
| `object_type` | string | MUST | OUTSIDE payload | INCLUDE | INCLUDE | NO | ordinary | exact canonical value |
| `protocol_version` | string | MUST | OUTSIDE payload | INCLUDE | INCLUDE | NO | ordinary | exact canonical value |
| `schema_version` | string | MUST | OUTSIDE payload | INCLUDE | INCLUDE | NO | ordinary | exact canonical value |
| `created_at` | string (ISO 8601 UTC) | MUST | OUTSIDE payload | INCLUDE | INCLUDE | NO | ordinary | exact canonical value |
| `integrity_hash` | string | MUST | OUTSIDE payload | EXCLUDE — self | EXCLUDE — self | YES | derived after record hash | recompute and compare |
| `event_type` | string | MUST | EXCLUDE | INCLUDE | INCLUDE | NO | ordinary | registry + exact canonical value |
| `sequence_number` | integer | MUST | EXCLUDE | INCLUDE | INCLUDE | NO | MUST be `0` for first record | monotonicity |
| `previous_record_hash` | string | MUST | EXCLUDE | INCLUDE | INCLUDE | YES / verifier-linked | 64 lowercase hex zero digest for first record | predecessor linkage |
| `event_payload_hash` | string | MUST | EXCLUDE | INCLUDE | INCLUDE | YES | ordinary; payload hash still required | recompute from EP-001 |
| `audit_record_hash` | string | MUST | EXCLUDE | EXCLUDE — self | INCLUDE | YES | derived from record preimage | recompute using `0x02` |

### 2.1 Interpretation rules

- **INCLUDE** means the field/value is present in the canonical JCS object used for that digest.
- **EXCLUDE** means the field/value MUST NOT occur in that digest's canonical preimage.
- **OUTSIDE payload** means the field belongs to the Audit Record envelope and is not part of `event_payload`.
- `event_payload_hash` is a derived ENT-007 field but is an input to `audit_record_hash` and `integrity_hash`.
- `audit_record_hash` is an input to `integrity_hash` but not to itself.
- `integrity_hash` is not an input to `audit_record_hash` or itself.

## 3. Frozen Event Payload contract alignment

EP-001 (§5.5) defines the Event Payload as application/event data associated with one Audit Record and explicitly excludes the entire Audit Record envelope.

The top-level Event Payload MUST be a JSON object. Member values MAY use JSON object, array, string, number, boolean, or null subject to the event-specific schema.

The payload is canonicalized with RFC 8785 JCS and encoded as UTF-8 before hashing:

```text
EventPayloadHashPreimage(P) = JCS(P)
event_payload_hash(P) = SHA-256(JCS(P))
```

Duplicate object member names are invalid and MUST be rejected before hashing.

The raw Event Payload is not duplicated inside ENT-007 hash preimages. Its commitment enters ENT-007 through `event_payload_hash`.

## 4. Frozen Audit Record hash preimage

For ENT-007 record `R`:

```text
R_AR = R excluding:
       audit_record_hash
       integrity_hash

AuditRecordHashPreimage(R) =
    0x02 || JCS(R_AR)

audit_record_hash(R) =
    SHA-256(AuditRecordHashPreimage(R))
```

`0x02` MUST be one raw octet. It MUST NOT be encoded as ASCII `0x02`, as a hexadecimal string, or as another textual wrapper.

Because `event_payload_hash` is included in `R_AR`, the Audit Record identity commits to the Event Payload commitment without embedding the raw payload.

## 5. Frozen Integrity hash preimage

For ENT-007 record `R`:

```text
R_I = R excluding:
      integrity_hash

IntegrityPreimage(R) = JCS(R_I)

integrity_hash(R) = SHA-256(IntegrityPreimage(R))
```

Therefore `R_I` contains `audit_record_hash` and `event_payload_hash`.

The dependency is strictly:

```text
Event Payload
     ↓
event_payload_hash
     ↓
audit_record_hash
     ↓
integrity_hash
```

There is no reverse dependency and no cycle.

## 6. Frozen chain and genesis rules

For non-genesis record `R[n]`:

```text
R[n].previous_record_hash = R[n-1].audit_record_hash
```

The first record MUST have:

```text
sequence_number = 0
previous_record_hash =
0000000000000000000000000000000000000000000000000000000000000000
```

The sentinel represents exactly 32 zero bytes. All digest fields use the canonical representation defined in APS-200 §4.1: exactly 64 lowercase hexadecimal ASCII characters.

Subsequent records MUST increment `sequence_number` by one within the session and MUST reference the immediately preceding record's `audit_record_hash`.

## 7. Frozen canonical representation

All fields included in `R_AR` and `R_I` MUST be serialized according to RFC 8785 JCS and the canonical result MUST be UTF-8 encoded before SHA-256 input.

All SHA-256 digest fields MUST be represented as exactly 64 lowercase hexadecimal ASCII characters. Uppercase hexadecimal, `0x` prefixes, base64, whitespace, or alternate textual encodings are non-conformant.

For the Event Payload, RFC 8785 JCS + UTF-8 applies identically.

The following are non-conformant:

- language-native object serialization;
- pretty-printed JSON;
- implementation-specific map ordering;
- locale-dependent serialization;
- non-JCS JSON serialization;
- textual encoding of the `0x02` domain separator.

## 8. Frozen domain separation

```text
0x00 → RFC 6962-style Merkle leaf
0x01 → RFC 6962-style Merkle interior node
0x02 → Audit Record hash
```

`event_payload_hash` uses no additional domain separator under EP-001.

Certificate, Merkle, and legacy chain digests MUST NOT be substituted for `audit_record_hash`.

## 9. Frozen verification semantics

A conformant verifier MUST perform checks in dependency order:

```text
1. Parse Event Payload.
2. Reject malformed JSON.
3. Reject duplicate object member names.
4. Reject non-object top-level payload.
5. Validate the applicable event-specific payload schema, when declared.
6. JCS-canonicalize the Event Payload.
7. UTF-8 encode the canonical payload.
8. Compute event_payload_hash.
9. Compare event_payload_hash.
10. Construct R_AR and compute audit_record_hash using 0x02.
11. Compare audit_record_hash.
12. Construct R_I and compute integrity_hash.
13. Compare integrity_hash.
14. Verify previous_record_hash against the predecessor audit_record_hash, except genesis.
15. Verify genesis sentinel and sequence_number rules.
16. Verify canonical serialization and required field presence.
17. Reject undeclared ENT-007 fields.
```

The first applicable verification failure MUST be surfaced using the normative error codes in APS-200 §5.7.

## 10. Frozen extension policy

For the P0-2 conformance profile, ENT-007 is a **closed canonical hash surface**. An implementation MUST NOT add undeclared fields.

A future extension MUST use a later `schema_version`, explicitly declare the field and its hash-domain treatment, update this matrix, and provide new Golden Fixtures before claiming conformance to that version.

Unknown or undeclared fields MUST therefore be rejected in the P0-2 conformance profile.

## 11. Frozen machine-readable verification codes

| Code | Condition |
|---|---|
| `E_REQUIRED_FIELD_MISSING` | Required ENT-007 field is absent |
| `E_UNEXPECTED_FIELD` | Undeclared ENT-007 field is present |
| `E_PAYLOAD_INVALID_JSON` | Event Payload is not valid JSON |
| `E_PAYLOAD_DUPLICATE_KEY` | Event Payload contains duplicate object member names |
| `E_PAYLOAD_TOP_LEVEL_TYPE` | Event Payload top-level value is not an object |
| `E_PAYLOAD_SCHEMA` | Event Payload violates the applicable event schema |
| `E_PAYLOAD_HASH_MISMATCH` | Recomputed `event_payload_hash` differs |
| `E_AUDIT_RECORD_HASH_MISMATCH` | Recomputed `audit_record_hash` differs |
| `E_INTEGRITY_HASH_MISMATCH` | Recomputed `integrity_hash` differs |
| `E_PREVIOUS_RECORD_HASH_MISMATCH` | `previous_record_hash` does not equal predecessor `audit_record_hash` |
| `E_GENESIS_INVALID` | Genesis sentinel or genesis position is invalid |
| `E_SEQUENCE_INVALID` | Sequence number violates session ordering |
| `E_CANONICALIZATION_INVALID` | Required canonical representation cannot be produced or verified |
| `E_DIGEST_ENCODING_INVALID` | Digest field is not 64 lowercase hexadecimal characters representing 32 bytes |

The verifier MUST report the first applicable normative code. Implementations MAY provide additional diagnostic data, but MUST NOT replace these codes with implementation-specific codes for covered conditions.

## 12. APS-200 consistency check

| APS-200 rule | Matrix result | Status |
|---|---|---|
| Common Object Contract fields | included in both ENT-007 digest domains except self-excluded `integrity_hash` | PASS |
| Digest field representation | 64 lowercase hexadecimal ASCII characters | PASS |
| `integrity_hash` excludes itself | excluded from `R_I` | PASS |
| `audit_record_hash` field | included in ENT-007 | PASS |
| `audit_record_hash` excludes itself | excluded from `R_AR` | PASS |
| `audit_record_hash` excludes `integrity_hash` | excluded from `R_AR` | PASS |
| `integrity_hash` includes `audit_record_hash` | included in `R_I` | PASS |
| `previous_record_hash` | links to predecessor `audit_record_hash` | PASS |
| Genesis | zero digest + sequence `0` + frozen textual encoding | PASS |
| Event Payload | EP-001 boundary and JCS hash | PASS |
| RFC 8785 JCS | used for all canonical preimages | PASS |
| `0x02` | raw Audit Record domain separator | PASS |
| Merkle `0x00` / `0x01` | remains separate | PASS |
| Extension policy | closed for P0-2; versioned future extension required | PASS |
| Verification error codes | normative P0-2 vocabulary | PASS |

## 13. P0-2 Gate Decision

**P0-2 = FROZEN for the DQ-003 conformance profile.**

The semantic and representation-level blockers listed in the previous review have been explicitly resolved by APS-200 §4.1, §5.3, §5.6, and §5.7.

No implementation-specific behavior may be used to reinterpret this contract during DQ-003 conformance testing.

The next permitted artifact is `DQ-003-AUDIT-CHAIN-001`, which MUST be generated from this frozen contract. Golden Fixture values MUST be calculated independently and MUST NOT be reverse-engineered from RI-PY or RI-RS output.

# P0-2 — ENT-007 Audit Record Field-by-Field Hash Domain Matrix

**Status:** FINAL REVIEW GATE — NOT YET FROZEN  
**Branch:** `dq/dq-003-audit-record-hash-domain`  
**Authority:** APS-200 §4, §5, §5.1–§5.5  
**Purpose:** Establish the final field inclusion/exclusion contract for ENT-007 before P0-2 freeze and Golden Fixture creation.

## 1. Authority and scope

This matrix is derived directly from the current APS-200 draft on this branch.

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

## 2. Final ENT-007 inclusion/exclusion matrix

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
| `previous_record_hash` | string | MUST | EXCLUDE | INCLUDE | INCLUDE | YES / verifier-linked | genesis sentinel for first record | predecessor linkage |
| `event_payload_hash` | string | MUST | EXCLUDE | INCLUDE | INCLUDE | YES | ordinary; payload hash still required | recompute from EP-001 |
| `audit_record_hash` | string | MUST | EXCLUDE | EXCLUDE — self | INCLUDE | YES | derived from record preimage | recompute using `0x02` |

### 2.1 Interpretation rules

- **INCLUDE** means the field/value is present in the canonical JCS object used for that digest.
- **EXCLUDE** means the field/value MUST NOT occur in that digest's canonical preimage.
- **OUTSIDE payload** means the field belongs to the Audit Record envelope and is not part of `event_payload`.
- `event_payload_hash` is a derived ENT-007 field but is an input to `audit_record_hash` and `integrity_hash`.
- `audit_record_hash` is an input to `integrity_hash` but not to itself.
- `integrity_hash` is not an input to either `audit_record_hash` or itself.

## 3. Event Payload contract alignment

EP-001 (§5.5) defines the Event Payload as application/event data associated with one Audit Record and explicitly excludes the entire Audit Record envelope:

```text
Common Object Contract fields
object_id
object_type
protocol_version
schema_version
created_at
integrity_hash

event_type
sequence_number
previous_record_hash
event_payload_hash
audit_record_hash
```

The top-level Event Payload MUST be a JSON object. Member values MAY use JSON object, array, string, number, boolean, or null subject to the event-specific schema.

The payload is canonicalized with RFC 8785 JCS and encoded as UTF-8 before hashing:

```text
EventPayloadHashPreimage(P) = JCS(P)
event_payload_hash(P) = SHA-256(JCS(P))
```

Duplicate object member names are invalid and MUST be rejected before hashing.

Therefore the raw Event Payload is **not duplicated** inside ENT-007 hash preimages. Its commitment enters ENT-007 through `event_payload_hash`.

## 4. Audit Record hash preimage

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

`0x02` MUST be one raw octet. It MUST NOT be encoded as the ASCII characters `0x02`, as a hexadecimal string, or as another textual wrapper.

Because `event_payload_hash` is included in `R_AR`, the Audit Record identity commits to the Event Payload commitment without embedding the raw payload.

## 5. Integrity hash preimage

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

## 6. Chain and genesis

For non-genesis record `R[n]`:

```text
R[n].previous_record_hash = R[n-1].audit_record_hash
```

The first record MUST have:

```text
sequence_number = 0
previous_record_hash = 32-byte all-zero digest sentinel
```

Subsequent records MUST increment `sequence_number` by one within the session and MUST reference the immediately preceding record's `audit_record_hash`.

The exact canonical textual encoding of digest fields remains a representation-level freeze item and is intentionally not invented by this matrix.

## 7. Canonical representation

All fields included in `R_AR` and `R_I` MUST be serialized according to the RFC 8785 JCS profile referenced by APS-200 §8.

The canonical JCS result MUST be UTF-8 encoded before SHA-256 input.

For the Event Payload, the same RFC 8785 JCS + UTF-8 rule applies.

The following are therefore non-conformant:

- language-native object serialization;
- pretty-printed JSON;
- implementation-specific map ordering;
- locale-dependent serialization;
- non-JCS JSON serialization;
- textual encoding of the `0x02` domain separator.

## 8. Domain separation

The currently defined hash domains remain distinct:

```text
0x00 → RFC 6962-style Merkle leaf
0x01 → RFC 6962-style Merkle interior node
0x02 → Audit Record hash
```

`event_payload_hash` uses no additional domain separator under EP-001.

Certificate, Merkle, and legacy chain digests MUST NOT be substituted for `audit_record_hash`.

## 9. Verification semantics

A conformant verifier MUST perform the following dependency-ordered checks:

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
```

The verifier MUST reject when any required derived value differs, a required field is absent, an excluded field contaminates a hash preimage, canonicalization differs, the predecessor link is invalid, or the genesis/sequence rule is violated.

Machine-readable error-code names are still a freeze item; this matrix intentionally specifies rejection conditions rather than inventing an unapproved error vocabulary.

## 10. APS-200 consistency check

| APS-200 rule | Matrix result | Status |
|---|---|---|
| Common Object Contract fields | included in both ENT-007 digest domains except self-excluded `integrity_hash` | PASS |
| `integrity_hash` excludes itself | excluded from `R_I` | PASS |
| `audit_record_hash` field | added to ENT-007 | PASS |
| `audit_record_hash` excludes itself | excluded from `R_AR` | PASS |
| `audit_record_hash` excludes `integrity_hash` | excluded from `R_AR` | PASS |
| `integrity_hash` includes `audit_record_hash` | included in `R_I` | PASS |
| `previous_record_hash` | links to predecessor `audit_record_hash` | PASS |
| Genesis | zero digest + sequence `0` | PASS, encoding still open |
| Event Payload | EP-001 boundary and JCS hash | PASS |
| RFC 8785 JCS | used for all canonical preimages | PASS |
| `0x02` | raw Audit Record domain separator | PASS |
| Merkle `0x00` / `0x01` | remains separate | PASS |

## 11. Remaining freeze blockers

Only representation/verification items remain:

- [ ] exact digest field encoding (`hex` vs another already-authorized canonical representation);
- [ ] exact genesis sentinel stored representation;
- [ ] exact machine-readable verification error codes;
- [ ] final extension-field policy for ENT-007, if extensions are permitted;
- [ ] final cross-document reference check for APS-200 §8 and the event type registry.

No unresolved semantic dependency remains between `event_payload_hash`, `audit_record_hash`, and `integrity_hash` in the current DQ-003 contract.

## 12. Gate

**P0-2 remains OPEN — FINAL REVIEW.**

The field inclusion/exclusion semantics are now aligned with the current APS-200 draft. Freeze is blocked only by the representation-level items listed in §11. No implementation remediation and no Golden Fixture freeze should occur before those items are explicitly resolved.

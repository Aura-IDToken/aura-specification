# APS-200 — Canonical Data Model

Document ID: APS-200  
Version: 1.0-DRAFT  
Status: DRAFT  
Classification: Normative Specification  
Authority: APS-001 · APS-100  
Last Review: 2026-08-22

---

## 1. Purpose

APS-200 defines the canonical data model of the Aura Protocol.

Every conformant implementation MUST represent information in accordance with this document. Internal structures MAY differ, but data semantics and contract MUST be equivalent.

---

## 2. Design Principles

The data model MUST be:
- **Deterministic** — same data → same representation
- **Unambiguous** — no field has multiple valid interpretations
- **Extensible** — new fields MAY be added without breaking existing contracts
- **Versionable** — every object carries version information
- **Language-independent** — the model is not tied to any programming language
- **Serialization-independent** — the model is not tied to any wire format

---

## 3. Core Entities

| ID | Entity | Description |
|----|--------|-------------|
| ENT-001 | Protocol Header | Execution metadata |
| ENT-002 | Evaluation Request | Input data |
| ENT-003 | Evaluation Result | Output of evaluation |
| ENT-004 | Policy Reference | Reference to the policy used |
| ENT-005 | Evidence | Execution proof |
| ENT-006 | Attestation | Formal conformance confirmation |
| ENT-007 | Audit Record | Immutable auditable event record |
| ENT-008 | Implementation Metadata | Information about the implementation |

---

## 4. Common Object Contract

Every entity MUST contain the following fields:

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `object_id` | string | MUST | Globally unique identifier (UUID v4 or canonical format) |
| `object_type` | string | MUST | APS-000 canonical type name (e.g., `EvaluationRequest`) |
| `protocol_version` | string | MUST | APS version this object conforms to (e.g., `1.0`) |
| `schema_version` | string | MUST | Schema version of this entity definition |
| `created_at` | string (ISO 8601) | MUST | Timestamp of object creation (UTC) |
| `integrity_hash` | string | MUST | `SHA-256(canonical_bytes(object))` of this object, excluding `integrity_hash` itself. Canonical bytes are defined by §8. |

> **Note on self-reference.** A digest field cannot cover its own value. `integrity_hash` therefore excludes itself from the canonicalized object, matching the rule already stated for `evidence_hash` in APS-300 §5. This makes an existing implicit constraint explicit; it does not introduce a new one.

For ENT-007, the common `integrity_hash` rule is further constrained by §5 ENT-007: the `audit_record_hash` field is included in the integrity preimage. Thus `integrity_hash` commits to the complete Audit Record hash identity while remaining non-self-referential.

---

## 5. Entity Definitions

### ENT-001 — Protocol Header

**Purpose**: Carries metadata about a single protocol execution.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `execution_id` | string | MUST | Unique identifier for this execution |
| `implementation_id` | string | MUST | Identifier of the implementation (see ENT-008) |
| `policy_reference` | ENT-004 | MUST | Policy used in this execution |
| `started_at` | string (ISO 8601) | MUST | Execution start timestamp (UTC) |
| `completed_at` | string (ISO 8601) | MUST | Execution completion timestamp (UTC) |

> **TODO**: Define `execution_id` format precisely.

---

### ENT-002 — Evaluation Request

**Purpose**: The input to a protocol execution.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `input_hash` | string | MUST | SHA-256 hash of the canonical input payload |
| `input_schema` | string | MUST | Identifier of the input schema version |
| `request_fields` | object | MUST | Validated, schema-conformant input payload |

> **TODO**: Define the canonical schema for `request_fields`.

---

### ENT-003 — Evaluation Result

**Purpose**: The output of evaluation.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `execution_id` | string | MUST | References ENT-001 `execution_id` |
| `decision` | string | MUST | Canonical decision value (e.g., `ALLOW`, `DENY`, `MEASURE`) |
| `output_hash` | string | MUST | SHA-256 hash of the canonical output payload |
| `policy_reference` | ENT-004 | MUST | Policy used to produce this result |

> **TODO**: Define the canonical set of `decision` values.

---

### ENT-004 — Policy Reference

**Purpose**: Identifies the policy used in an execution.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `policy_id` | string | MUST | Unique identifier for the policy |
| `policy_version` | string | MUST | Version of the policy |
| `policy_hash` | string | MUST | SHA-256 hash of the policy content |

---

### ENT-005 — Evidence

**Purpose**: Cryptographically verifiable proof of execution.

See APS-300 for the full Evidence Model. The canonical Evidence object fields are defined in APS-300 §5.

---

### ENT-006 — Attestation

**Purpose**: Formal confirmation of conformance.

| Field | Type | Requirement | Description |
|-------|--------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `attestation_type` | string | MUST | Type (e.g., `CONFORMANCE`, `EXECUTION`) |
| `attested_execution_id` | string | MUST | The execution_id this attests |
| `evidence_reference` | string | MUST | object_id of the Evidence Pack |
| `attestation_hash` | string | MUST | SHA-256 hash of attestation content |

> **TODO**: Define the full Attestation lifecycle and authority.

---

### ENT-007 — Audit Record

**Purpose**: Immutable record of a single auditable event.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `event_type` | string | MUST | Canonical event type; normative vocabulary is governed by `aps/EVENT_TYPE_REGISTRY.md` |
| `sequence_number` | integer | MUST | Monotonically increasing sequence number within a session |
| `previous_record_hash` | string | MUST | Hash of the previous Audit Record (chain link) |
| `event_payload_hash` | string | MUST | SHA-256 hash of the canonical Event Payload defined by EP-001 (§5.5) |
| `audit_record_hash` | string | MUST | Domain-separated SHA-256 hash defined by §5.1; derived and MUST NOT be supplied as an independent semantic input |

### 5.1 ENT-007 Audit Record Hash Contract

The `audit_record_hash` is the normative cryptographic identity used for Audit Record chain linkage. It is distinct from `integrity_hash`, certificate fingerprints, and RFC 6962-style Merkle hashes.

For an ENT-007 record `R`, define the Audit Record hash preimage object `R_AR` as the canonical ENT-007 object containing all fields required by the ENT-007 contract **except**:

- `audit_record_hash`; and
- `integrity_hash`.

The canonical bytes MUST be produced using the RFC 8785 JCS profile defined in §8.

```text
AuditRecordHashPreimage(R) =
    0x02 || JCS(R_AR)

audit_record_hash(R) =
    SHA-256(AuditRecordHashPreimage(R))
```

`0x02` is one raw octet. It MUST NOT be represented as the ASCII characters `0x02`, a hexadecimal string, or another textual wrapper.

The `audit_record_hash` MUST NOT depend on `integrity_hash`. This exclusion prevents a circular dependency and makes the Audit Record hash independently recomputable from the normative source fields.

### 5.2 ENT-007 Integrity Hash Contract

The Common Object Contract `integrity_hash` rule applies to ENT-007 with one explicit dependency rule:

```text
IntegrityPreimage(R) =
    JCS(R_I)

integrity_hash(R) =
    SHA-256(IntegrityPreimage(R))
```

where `R_I` is the complete canonical ENT-007 object **excluding only `integrity_hash` itself**.

Therefore `R_I` includes the derived `audit_record_hash`.

The dependency is intentionally one-directional:

```text
ENT-007 source fields
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

Normative dependency rules:

1. `audit_record_hash` MUST NOT include `integrity_hash` in its preimage.
2. `integrity_hash` MUST include `audit_record_hash` in its preimage.
3. Neither digest may include its own field value.
4. `previous_record_hash` MUST refer to the preceding record's `audit_record_hash`, not its `integrity_hash`.
5. Certificate and Merkle digests MUST NOT be substituted for `audit_record_hash`.

### 5.3 ENT-007 Chain and Genesis Rule

For a non-genesis record `R[n]`:

```text
R[n].previous_record_hash = R[n-1].audit_record_hash
```

The genesis record MUST use the all-zero 32-byte digest as its `previous_record_hash` sentinel. The exact canonical textual encoding of the stored digest value is governed by the approved fixture profile and MUST be identical across conformant implementations.

The first Audit Record in a session MUST have `sequence_number = 0`. Subsequent records MUST increase monotonically by one within that session.

### 5.4 ENT-007 Derived-Field Rules

The following fields are derived and MUST be independently recomputable by a conformant verifier:

- `event_payload_hash` — from EP-001;
- `audit_record_hash` — from §5.1;
- `integrity_hash` — from §5.2;
- `previous_record_hash` — from the predecessor's `audit_record_hash`, except for genesis.

A conformant implementation MUST reject an Audit Record when recomputation produces a different value for any in-scope derived digest, when canonical bytes differ, when the predecessor link is incorrect, or when the genesis/sequence rule is violated.

### 5.5 EP-001 — Event Payload Contract

**Purpose**: Defines the canonical payload committed by `event_payload_hash` for ENT-007.

**Boundary and ownership**

The Event Payload is the application/event data associated with one Audit Record. It is **not** the Audit Record envelope. The payload MUST exclude:

- all Common Object Contract fields;
- `event_type`;
- `sequence_number`;
- `previous_record_hash`;
- `event_payload_hash`;
- `audit_record_hash`;
- `integrity_hash`.

The payload is therefore owned by the event semantics, while ENT-007 owns the immutable audit envelope and its derived hashes. The payload MAY be persisted or transported separately; `event_payload_hash` is the normative commitment that binds it to the Audit Record.

**Payload type**

For conformance purposes, an Event Payload MUST be a JSON object. JSON arrays, strings, numbers, booleans, and `null` MUST NOT be used as the top-level Event Payload.

Payload member values MAY use the JSON value types permitted by RFC 8785 JCS: object, array, string, number, boolean, and `null`, subject to the event-specific schema. Event-specific schemas MAY constrain these values further.

**Canonicalization**

The canonical bytes of the Event Payload MUST be produced using RFC 8785 JSON Canonicalization Scheme (JCS), encoded as UTF-8. The payload MUST be canonicalized before hashing. Implementations MUST NOT hash implementation-specific in-memory serialization, pretty-printed JSON, language-native object representations, or non-JCS JSON serialization.

**UTF-8 requirements**

The Event Payload MUST be valid Unicode JSON and its canonical JCS representation MUST be encoded as UTF-8. Invalid UTF-8 byte sequences are not a valid payload representation. Implementations MUST NOT perform locale-dependent transcoding or normalization outside the JCS processing defined by RFC 8785.

**Duplicate keys**

Duplicate member names in a JSON object are invalid for conformance. An implementation MUST reject a payload containing duplicate object member names before calculating `event_payload_hash`. It MUST NOT silently apply first-key-wins, last-key-wins, merge, or implementation-specific duplicate-key behavior.

**Hash preimage**

For Event Payload `P`:

```text
EventPayloadHashPreimage(P) = JCS(P)

event_payload_hash(P) =
    SHA-256(EventPayloadHashPreimage(P))
```

No domain separator is added to the Event Payload hash in EP-001. Domain separation for the Audit Record identity is provided independently by `0x02` in §5.1.

**Verification and rejection**

A conformant verifier MUST:

1. parse the supplied Event Payload as JSON;
2. reject malformed JSON;
3. reject duplicate object member names;
4. reject a non-object top-level payload;
5. validate the payload against the applicable event-specific schema, if one is declared by the event contract;
6. canonicalize the payload using RFC 8785 JCS;
7. encode the canonical representation as UTF-8;
8. compute `SHA-256(JCS(P))`;
9. compare the result with `event_payload_hash`.

The verifier MUST reject the Audit Record if any required step fails or if the recomputed hash differs from the supplied `event_payload_hash`.

**Normative dependency**

The resulting dependency is:

```text
Event Payload
      │
      ▼
    JCS(P)
      │
      ▼
SHA-256
      │
      ▼
event_payload_hash
      │
      ▼
    ENT-007
      │
      ▼
audit_record_hash
      │
      ▼
integrity_hash
```

EP-001 does not make `event_payload_hash` depend on `audit_record_hash` or `integrity_hash`.

---

### ENT-008 — Implementation Metadata

**Purpose**: Identifies and describes a specific implementation.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |

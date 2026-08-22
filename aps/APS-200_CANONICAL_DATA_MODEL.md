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
| `integrity_hash` | string | MUST | `SHA-256(canonical_bytes)` of this object, excluding `integrity_hash` itself. Canonical bytes are defined by §8. |

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
|-------|------|-------------|-------------|
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
| `event_payload_hash` | string | MUST | Hash of the event payload |
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

- `event_payload_hash` — from the precisely defined event payload;
- `audit_record_hash` — from §5.1;
- `integrity_hash` — from §5.2;
- `previous_record_hash` — from the predecessor's `audit_record_hash`, except for genesis.

A conformant implementation MUST reject an Audit Record when recomputation produces a different value for any in-scope derived digest, when canonical bytes differ, when the predecessor link is incorrect, or when the genesis/sequence rule is violated.

---

### ENT-008 — Implementation Metadata

**Purpose**: Identifies and describes a specific implementation.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `implementation_id` | string | MUST | Canonical ID (e.g., `RI-PY`, `RI-RS`) |
| `implementation_name` | string | MUST | Human-readable name |
| `implementation_version` | string | MUST | Semantic version of the implementation |
| `aps_version` | string | MUST | APS version this implementation claims conformance with |
| `conformance_report_id` | string | SHOULD | Reference to Conformance Report |

---

## 6. Relationships

```
Evaluation Request (ENT-002)
        │
        ▼
Evaluation Result (ENT-003)
        │
        ▼
Evidence (ENT-005)
        │
        ▼
Attestation (ENT-006)
        │
        ▼
Audit Record (ENT-007)
```

Every relationship MUST be traceable via object_id references.

---

## 7. Validation Rules

Every object MUST pass:
1. Structure validation (required fields present)
2. Type validation (field types match schema)
3. Required field validation
4. Integrity validation (integrity_hash matches computed hash)
5. APS-100 invariant validation

For ENT-007, validation additionally MUST include:
6. `event_payload_hash` recomputation against the defined event payload;
7. `audit_record_hash` recomputation using §5.1;
8. `previous_record_hash` linkage to the predecessor's `audit_record_hash`, or the genesis sentinel;
9. `sequence_number` validation under §5.3;
10. canonical-byte equality under §8.

---

## 8. Serialization Requirements

For the current normative JSON interoperability profile, implementations MUST use **RFC 8785 JSON Canonicalization Scheme (JCS)** when canonical JSON serialization is required by this specification.

The canonical serialization boundary is the UTF-8 byte sequence emitted by the JCS profile. Semantic JSON equivalence, map insertion order, implementation-specific serializers, whitespace conventions, or textual/hexadecimal representations MUST NOT be used as substitutes for canonical-byte equality.

For a canonical object `O`:

```text
JCS(O) = canonical UTF-8 bytes B
SHA-256(B) = record/integrity digest where applicable
SHA-256(0x00 || B) = RFC 6962-style leaf hash where applicable
```

The leaf prefix `0x00` is one raw octet. It MUST NOT be represented as the ASCII characters `0x00`, a hexadecimal string, or another textual wrapper. RFC 6962-style interior-node hashing uses `0x01` followed by the two raw 32-byte child digests.

For ENT-007, §5.1 additionally defines the Audit Record hash domain `0x02`. The `0x02` prefix is one raw octet and is reserved for the normative Audit Record hash domain.

The canonicalization/hash boundary is implementation-independent. RI-PY and RI-RS have independently executed CANONICAL-001 under CK-003 DQ-006 and produced byte-identical canonical bytes, SHA-256 digests and leaf digests. The corresponding closure evidence is normative decision evidence, not a production dependency requirement.

Conformance engines used for this verification are:

- RI-PY: `rfc8785==0.1.4` — conformance-only;
- RI-RS: `serde_json_canonicalizer==0.3.2` — conformance-only.

These implementation dependencies do not mandate insertion of either library into production runtime code. Production implementations MUST satisfy the RFC 8785 semantics; the named engines are reference conformance tools.

The canonical serialization profile is version-bound. A change affecting canonical bytes, number/string serialization, field inclusion, hash-domain inputs, or conformance outcomes MUST be treated as a versioned protocol change and MUST undergo compatibility and fixture impact analysis.

### CANONICAL-001 reference vector

Input object:

```json
{"event_type":"AUDIT_RECORD","payload":{"value":42},"protocol_version":"1.0","schema_version":"1.0"}
```

Canonical byte length: `100`.

Canonical bytes (hex):

```text
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
```

SHA-256:

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

RFC 6962 leaf:

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

The executable cross-language evidence and provenance are maintained under `ck003/dq-006-closure/` and the reference implementation conformance repositories.

---

## 9. JSON Schema

Machine-readable schema definitions for canonical fixtures and shared object contracts are maintained under `fixtures/schemas/`. Entity-specific schemas remain subject to APS-200 completion and MUST be added before APS-001 v1.0 approval where required by the relevant entity contract.

The event-type vocabulary and validation contract are governed by `aps/EVENT_TYPE_REGISTRY.md`. That registry MUST be incorporated into the approved APS-200 profile before DQ-004 can be closed.

---

## 10. Traceability

| Entity | Related Invariants | Related Evidence | Related CONF |
|--------|-------------------|------------------|--------------|
| ENT-001 | INV-009, INV-015 | EVID-CORE | CONF-008 |
| ENT-002 | INV-001, INV-003 | EVID-CORE | CONF-001, CONF-003 |
| ENT-003 | INV-001, INV-003, INV-013 | EVID-CORE | CONF-001, CONF-003 |
| ENT-004 | INV-013 | EVID-CORE | — |
| ENT-005 | INV-004, INV-005, INV-011 | EVID-CORE | CONF-004, CONF-009 |
| ENT-006 | INV-005 | EVID-CONF | CONF-005 |
| ENT-007 | INV-003, INV-011, INV-012 | EVID-AUDIT | CONF-003, CONF-012 |
| ENT-008 | INV-009, INV-015 | EVID-CORE | CONF-008 |

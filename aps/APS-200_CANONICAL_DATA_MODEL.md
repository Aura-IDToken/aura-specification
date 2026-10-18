# APS-200 — Canonical Data Model

Document ID: APS-200  
Version: 1.0-DRAFT  
Status: DRAFT  
Classification: Normative Specification  
Authority: APS-001 §3, §4, §7, §12 · APS-100
Last Review: 2026-09-26

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
| `object_id` | string | MUST | Unique canonical identifier conformant with APS-000 and the applicable entity profile/schema; the exact syntax MUST be version-bound and MUST NOT be inferred from storage location or incidental serialization |
| `object_type` | string | MUST | APS-000 canonical type name bound to the applicable entity contract (e.g., `EvaluationRequest`) |
| `protocol_version` | string | MUST | APS version this object conforms to (e.g., `1.0`) |
| `schema_version` | string | MUST | Schema version of this entity definition |
| `created_at` | string (ISO 8601) | MUST | Timestamp of object creation (UTC) |
| `integrity_hash` | string | MUST | `SHA-256(canonical_bytes)` of this object, excluding `integrity_hash` itself. Canonical bytes are defined by §8. |

> **Note on self-reference.** A digest field cannot cover its own value. `integrity_hash` therefore excludes itself from the canonicalized object, matching the rule already stated for `evidence_hash` in APS-300 §5. This makes an existing implicit constraint explicit; it does not introduce a new one.
>
> **Identity note.** The common object contract requires every entity to expose a stable `object_id` and `object_type`. Entity-specific schemas MUST define the exact `object_id` syntax and uniqueness scope so that identity validation can be executed objectively under INV-015 / CONF-015.

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

`execution_id` MUST be stable for the lifetime of the protocol execution and MUST be reused unchanged across all artifacts produced from that execution. The exact syntax is schema-bound, but the value MUST be unique within the applicable protocol scope and MUST NOT be regenerated when Evidence, Audit Records, or Attestations are derived from the same execution.

---

### ENT-002 — Evaluation Request

**Purpose**: The input to a protocol execution.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `input_hash` | string | MUST | SHA-256 hash of the canonical input payload |
| `input_schema` | string | MUST | Identifier of the input schema version |
| `request_fields` | object | MUST | Validated, schema-conformant input payload |

The base APS-200 schema requires `request_fields` to be a JSON object.

For the current repository working profile `AURA-DRAFT-CORE-001`, `input_schema` MUST equal `AURA-DRAFT-CORE-001` and `request_fields` MUST contain exactly:

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `profile_id` | string | MUST | MUST equal `AURA-DRAFT-CORE-001` |
| `subject_id` | string | MUST | Canonical subject identifier under the active draft identity rules |
| `measurement_value` | integer | MUST | Deterministic integer/fixed-point input value bound to the current working profile |
| `actor_tier` | string | MUST | Profile-scoped actor tier token carried as input, not inferred implicitly |

Additional request payload members require a version-bound profile/schema update. Other future execution profiles MAY define a different `input_schema` and payload contract, but they are not closed by this draft.

---

### ENT-003 — Evaluation Result

**Purpose**: The output of evaluation.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `execution_id` | string | MUST | References ENT-001 `execution_id` |
| `decision` | string | MUST | Canonical decision value |
| `output_hash` | string | MUST | SHA-256 hash of the canonical output payload |
| `policy_reference` | ENT-004 | MUST | Policy used to produce this result |
| `result_fields` | object | MUST | Validated, schema-conformant result payload |

For the current repository working profile `AURA-DRAFT-CORE-001`, a successful `decision` MUST be one of:

- `ALLOW`
- `DENY`
- `MEASURE`
- `NOT_APPLICABLE`

Invalid, ambiguous, blocked, or fail-closed executions MUST NOT emit `ENT-003`; they MUST halt per APS-001 §8 instead of inventing an out-of-band decision token.

For the same current working profile, `result_fields` MUST contain exactly:

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `profile_id` | string | MUST | MUST equal `AURA-DRAFT-CORE-001` |
| `subject_id` | string | MUST | Echoes the canonical subject identifier used in the request |
| `measurement_value` | integer | MUST | Deterministic integer/fixed-point value used by the current working profile |
| `matched_policy_rule` | string | MUST | Human-readable identifier or text for the rule branch that produced the decision |

In strict conformance mode, an implementation MUST reject an unknown decision token or malformed `result_fields` payload rather than silently coerce it into another semantic value.

---

### ENT-004 — Policy Reference

**Purpose**: Identifies the policy used in an execution.

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| Common Object Contract fields | — | MUST | See §4 |
| `policy_id` | string | MUST | Unique identifier for the policy |
| `policy_version` | string | MUST | Version of the policy |
| `policy_hash` | string | MUST | SHA-256 hash of the policy content |

`policy_id` and `policy_version` together define the canonical policy identity used for reproducibility and version compatibility checks. A change capable of altering a normative result MUST produce either a new `policy_version` or a new immutable `policy_id`.

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
| `evidence_reference` | string | MUST | `pack_id` of the Evidence Pack |
| `attestation_hash` | string | MUST | SHA-256 hash of attestation content |

The full Attestation lifecycle and approval authority remain version-bound specification work. Until that lifecycle is fully closed, conformant artifacts MUST still preserve a stable `attested_execution_id` and `evidence_reference` so that attestation linkage can be validated objectively once the final authority model is approved.

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

In strict conformance mode, `event_type` MUST be validated against an approved versioned registry entry. Unknown, malformed, aliased, or implementation-local tokens MUST be rejected rather than normalized.

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

---

## 8. Serialization Requirements

### 8.1 Normative JSON interoperability profile

For the current normative JSON interoperability profile, implementations MUST use **RFC 8785 JSON Canonicalization Scheme (JCS)** when canonical JSON serialization is required by this specification.

### 8.2 Canonicalization boundary

The canonical serialization boundary is the UTF-8 byte sequence emitted by the JCS profile after the applicable object has been validated against the relevant entity/schema contract.

Semantic JSON equivalence, map insertion order, implementation-specific serializers, whitespace conventions, or textual/hexadecimal representations MUST NOT be used as substitutes for canonical-byte equality.

For a canonical object `O`:

```text
JCS(O) = canonical UTF-8 bytes B
SHA-256(B) = record/integrity digest where applicable
SHA-256(0x00 || B) = RFC 6962-style leaf hash where applicable
```

### 8.3 Canonical JCS semantics

The JCS profile governs object-member ordering, insignificant whitespace elimination, string encoding, and number serialization. Protocol objects MUST be schema-valid before canonicalization, and numbers that violate the approved deterministic profile MUST be rejected rather than normalized.

### 8.4 Prohibited digest inputs

The following MUST NOT be accepted as digest inputs in place of canonical bytes:

- pretty-printed or implementation-formatted JSON
- alternate object serializations that are not the approved canonical bytes
- escaped, Base64, or hexadecimal encodings of the canonical bytes
- hexadecimal digest strings used where raw digest bytes are required

### 8.5 Hash-domain inputs

The leaf prefix `0x00` is one raw octet. It MUST NOT be represented as the ASCII characters `0x00`, a hexadecimal string, or another textual wrapper. RFC 6962-style interior-node hashing uses `0x01` followed by the two raw 32-byte child digests.

### 8.6 Conformance evidence

The canonicalization/hash boundary is implementation-independent. RI-PY and RI-RS have independently executed CANONICAL-001 under CK-003 DQ-006 and produced byte-identical canonical bytes, SHA-256 digests and leaf digests. The corresponding closure evidence is normative decision evidence, not a production dependency requirement.

Conformance engines used for this verification are:

- RI-PY: `rfc8785==0.1.4` — conformance-only;
- RI-RS: `serde_json_canonicalizer==0.3.2` — conformance-only.

These implementation dependencies do not mandate insertion of either library into production runtime code. Production implementations MUST satisfy the RFC 8785 semantics; the named engines are reference conformance tools.

### 8.7 Scope boundary

Canonical serialization determines representation only. It does **not** by itself define event semantics, version semantics, identity semantics, policy semantics, or Merkle construction semantics beyond the raw byte-domain inputs defined above.

### 8.8 Version and migration semantics

The canonical serialization profile is version-bound. A change affecting canonical bytes, number/string serialization, field inclusion, hash-domain inputs, or conformance outcomes MUST be treated as a versioned protocol change and MUST undergo compatibility and fixture impact analysis.

Historical artifacts generated before a version-bound profile change MUST retain their original serialization/hash-profile identity and MUST NOT be silently reinterpreted under the newer profile.

### 8.9 CANONICAL-001 reference vector

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

## 9. Version Binding

`protocol_version` identifies the normative protocol contract. `schema_version` identifies the representation/schema contract for the specific entity.

The two version fields MUST be carried independently where the relevant entity contract requires them. Implementations MUST NOT infer compatibility solely from numeric ordering, string similarity, or the presence of shared fields.

Compatibility decisions MUST be governed by an explicit version-compatibility matrix and the approved semantics of the affected entity, policy, fixture, or Evidence Profile. A change to identity rules, event-type rules, canonical bytes, or required fields is version-significant and MUST be accompanied by impact analysis.

---

## 10. JSON Schema

Machine-readable schema definitions for canonical fixtures and shared object contracts are maintained under `fixtures/schemas/`.

Current draft schemas published from this APS:

- `fixtures/schemas/common-object-contract.schema.json`
- `fixtures/schemas/protocol-header.schema.json`
- `fixtures/schemas/evaluation-request.schema.json`
- `fixtures/schemas/evaluation-result.schema.json`
- `fixtures/schemas/policy-reference.schema.json`
- `fixtures/schemas/attestation.schema.json`
- `fixtures/schemas/audit-record.schema.json`
- `fixtures/schemas/implementation-metadata.schema.json`

These schemas close the **top-level structural contract** for the APS-200 entities: required fields, top-level types, hash-field encoding, object identity/version envelope, and the current repository working-profile payloads for `ENT-002` / `ENT-003`.

They do **not** yet close every profile-specific semantic dependency. The following remain explicitly open and version-bound:

1. additional execution-profile payload schemas beyond `AURA-DRAFT-CORE-001`;
2. the final identity syntax/uniqueness rules needed for full `INV-015` closure;
3. the approved `ENT-007.event_type` registry tokens and machine-readable registry closure required by DQ-004.

The event-type vocabulary and validation contract are governed by `aps/EVENT_TYPE_REGISTRY.md`. That registry MUST be incorporated into the approved APS-200 profile before DQ-004 can be closed.

---

## 11. Traceability

| Entity | Related Invariants | Related Evidence | Related CONF |
|--------|-------------------|------------------|--------------|
| ENT-001 | INV-009, INV-015 | EVID-CORE | CONF-008 |
| ENT-002 | INV-001, INV-003 | EVID-CORE | CONF-001, CONF-003 |
| ENT-003 | INV-001, INV-003, INV-013 | EVID-CORE | CONF-001, CONF-003 |
| ENT-004 | INV-009, INV-013 | EVID-CORE | CONF-008, CONF-013 |
| ENT-005 | INV-004, INV-005, INV-011 | EVID-CORE | CONF-004, CONF-005, CONF-009, CONF-010 |
| ENT-006 | INV-005 | EVID-CONF | CONF-005 |
| ENT-007 | INV-003, INV-012 | EVID-AUDIT | CONF-003, CONF-012 |
| ENT-008 | INV-009, INV-015 | EVID-CORE | CONF-008, CONF-015 |

# APS-200 — Canonical Data Model

Document ID: APS-200  
Version: 1.0-DRAFT  
Status: DRAFT  
Classification: Normative Specification  
Authority: APS-001 · APS-100  
Last Review: 2026-08-20

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

**Purpose**: The output of a protocol execution.

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
| `event_type` | string | MUST | Canonical event type |
| `sequence_number` | integer | MUST | Monotonically increasing sequence number within a session |
| `previous_record_hash` | string | MUST | Hash of the previous Audit Record (chain link) |
| `event_payload_hash` | string | MUST | Hash of the event payload |

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

### 8.1 Transport representations

Implementations MAY use different transport formats (JSON, CBOR, Protocol Buffers), provided:
- Full model semantics are preserved
- The transport representation round-trips to the same semantic object
- INV-003 (Canonical Serialization) is not violated

A transport representation is never itself the canonical representation.

### 8.2 Canonical serialization profile

**This section is the single normative authority for canonical serialization in the Aura Protocol.** No other document may define a conflicting canonical serialization profile. Other documents MAY reference, interpret, test or trace this section; they MUST NOT restate it as an independent definition.

Wherever this specification requires the *canonical serialization* of a protocol object:

1. The object MUST first satisfy the applicable APS schema and semantic constraints (§7).
2. The canonical representation MUST be produced by applying the **JSON Canonicalization Scheme (JCS), RFC 8785**, to the semantic object.
3. The result MUST be encoded as **UTF-8**.
4. The exact byte sequence produced by that operation is the object's **`canonical_bytes`**.

`canonical_bytes` is the sole input to every cryptographic operation that this specification defines over canonical serialization.

### 8.3 Properties fixed by the profile

Because RFC 8785 is normative, the following are fixed by it and MUST NOT be redefined by an implementation or by a subordinate document:

| Property | Rule |
|----------|------|
| Object member ordering | Determined by JCS (UTF-16 code-unit ordering of member names), never by insertion order |
| Insignificant whitespace | Absent from `canonical_bytes` |
| String representation | JCS/JSON string form, UTF-8 encoded, minimal escaping |
| Non-ASCII characters | Emitted as raw UTF-8, not as `\uXXXX` escapes |
| Number serialization | RFC 8785 (ECMAScript `Number::toString`) rules |
| Non-finite numbers | `NaN` and `Infinity` are not JSON values; they MUST be rejected, never coerced |
| Array element ordering | Preserved exactly as given by the semantic object |

### 8.4 Prohibited digest inputs

An implementation MUST NOT compute a protocol digest over any of the following:

- pretty-printed or indented JSON;
- an implementation-specific or parser-preserving JSON serialization;
- a JSON string containing an escaped copy of `canonical_bytes`;
- a hexadecimal, Base64 or other textual encoding of `canonical_bytes`;
- a hexadecimal digest string used in place of raw digest bytes;
- a language-specific debug or `repr` form of the object.

### 8.5 Hash and Merkle domains

For a protocol object with canonical byte sequence `B`:

```text
digest(B)  = SHA-256(B)
leaf(B)    = SHA-256(0x00 || B)
node(l, r) = SHA-256(0x01 || l || r)
```

`0x00` and `0x01` are raw octets, not the ASCII texts `"0x00"` / `"0x01"`. `l` and `r` are raw digest bytes, not hexadecimal strings.

The hash-domain model itself is owned by **APS-001 §7.1** and governed by the DQ-002 hash-domain decision; the formulas are reproduced here only so that the byte boundary is unambiguous. This section binds their **input byte domain** to `canonical_bytes`; it does not define, extend or vary the domains themselves. Where this table and APS-001 §7.1 could be read differently, APS-001 §7.1 governs.

Correspondingly, APS-001 §7.1 states that the serialization profile producing `canonical bytes` is owned by APS-200 — that profile is §8.2 above.

The evidence-hash domain is defined by APS-300 §5 and is bound to `canonical_bytes` there.

### 8.6 Cross-implementation requirement

For the same semantic protocol object, every conformant implementation MUST produce identical `canonical_bytes`. In particular, RI-PY and RI-RS MUST be byte-identical. Verification is defined by CONF-003.

### 8.7 Scope boundary

Canonical serialization determines **representation only**. It does not define, and MUST NOT be read as defining:

- event semantics or the `event_type` vocabulary — see the [Event-Type Registry](EVENT_TYPE_REGISTRY.md) and DQ-004;
- version semantics, or the distinction between `protocol_version` and `schema_version` — see §4 and DQ-003;
- object identity semantics — see §4 and INV-015;
- entity schemas — see §5 and §9;
- Merkle tree construction semantics beyond the domains stated in §8.5.

### 8.8 Compatibility and migration

Binding or changing the canonical serialization profile is a protocol compatibility event and MUST be version-bound with explicit impact analysis.

Evidence generated before this profile was bound MUST retain its original serialization and hash-profile identity. Such evidence MUST NOT be silently reinterpreted as RFC 8785 / RFC 6962 evidence.

### 8.9 Reference engines (informative)

The reference implementations use the following conformance-scoped engines:

| Implementation | Engine |
|----------------|--------|
| RI-PY | `rfc8785` 0.1.4 |
| RI-RS | `serde_json_canonicalizer` 0.3.2 |

These engines are **conformance implementation detail, not protocol contract**. The normative contract is RFC 8785 together with §8.5. Naming an engine here does not authorize introducing it into any production runtime dependency graph, and an implementation using a different RFC 8785-conformant engine is not thereby non-conformant.

> **Traceability**: INV-003 · CONF-003 · CANONICAL-001 · ADR-CK003-DQ006 · DQ-006 closure package.

---

## 9. JSON Schema

> **TODO**: Publish JSON Schema definitions for each entity at a stable URL. Schemas belong in `fixtures/schemas/`.

---

## 10. Traceability

| Entity | Related Invariants | Related Evidence | Related CONF |
|--------|-------------------|-----------------|--------------|
| ENT-001 | INV-009, INV-015 | EVID-CORE | CONF-008 |
| ENT-002 | INV-001, INV-003 | EVID-CORE | CONF-001, CONF-003 |
| ENT-003 | INV-001, INV-003, INV-013 | EVID-CORE | CONF-001, CONF-003 |
| ENT-004 | INV-013 | EVID-CORE | — |
| ENT-005 | INV-004, INV-005, INV-011 | EVID-CORE | CONF-004, CONF-009 |
| ENT-006 | INV-005 | EVID-CONF | CONF-005 |
| ENT-007 | INV-012 | EVID-AUDIT | — |
| ENT-008 | INV-009, INV-015 | EVID-CORE | CONF-008 |

---

*Source: Original text preserved in [`APS-200 — Canonical Data Model_260723_192852.txt`](../APS-200%20%E2%80%94%20Canonical%20Data%20Model_260723_192852.txt)*

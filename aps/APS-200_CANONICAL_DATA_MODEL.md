# APS-200 — Canonical Data Model

Document ID: APS-200  
Version: 1.0-DRAFT  
Status: DRAFT  
Classification: Normative Specification  
Authority: APS-001 · APS-100  
Last Review: 2026-07-23

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
| `integrity_hash` | string | MUST | SHA-256 hash of the canonical serialization of this object |

"Canonical serialization" in this table means the canonical bytes defined by
§8. `integrity_hash` is `SHA-256(canonical_bytes)` over those bytes, rendered as
lower-case hexadecimal for presentation; the digest itself is the 32 raw octets.
The rule for excluding the self-referential `integrity_hash` member from its own
input is an open APS-200 decision — see §8.2.

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

**Classification: NORMATIVE.** This section is the single authoritative source of
the Aura Protocol canonical serialization contract. Any other document in this
repository that describes canonicalization is subordinate to this section, and
where it disagrees, this section governs.

### 8.1 Canonical serialization profile

The canonical serialization profile of the Aura Protocol is
**RFC 8785 — JSON Canonicalization Scheme (JCS)**.

For any value in the canonicalization input domain (§8.2), the canonical
representation is the output of RFC 8785, encoded as UTF-8. Those octets, and
only those octets, are the value's **canonical bytes**.

```text
value in the canonicalization input domain
                    │
                    ▼
          RFC 8785 (JCS)
                    │
                    ▼
      canonical bytes  =  UTF-8 octets
```

Implementations MUST produce canonical bytes that are byte-identical to the
RFC 8785 output for the same input value. Implementations MUST NOT introduce any
transformation of the canonical bytes after canonicalization.

The following MUST NOT occur in, or be applied to, canonical bytes:

- pretty-printing, indentation, line breaks, or any insignificant whitespace;
- a trailing newline or any other framing octet;
- an implementation-specific or language-native JSON serializer in place of
  RFC 8785;
- an ad-hoc key-ordering rule in place of the RFC 8785 ordering rule;
- re-parsing and re-serializing the canonical bytes;
- a byte order mark;
- any text encoding other than UTF-8;
- substitution of a hexadecimal, Base64, or other textual rendering of the
  canonical bytes for the canonical bytes themselves.

### 8.2 Canonicalization input domain

**The canonicalization input domain is the JSON data model**: the value space of
RFC 8259 as constrained by RFC 8785 §3.

Canonicalization is defined over that value space alone. It is a pure function
of the abstract JSON value. In particular, canonicalization is **not** defined
over, and MUST NOT be applied to:

- a JSON *document* as received (source text, byte stream, or file contents);
- a language-native object, struct, class instance, or map;
- an already-serialized string, whether or not it is valid JSON;
- a partially validated or unvalidated wire payload treated as text.

An implementation that receives JSON source text MUST first parse it into the
JSON data model, and MUST canonicalize the parsed value. Any two inputs that
parse to the same JSON value MUST produce identical canonical bytes; key order,
whitespace, and number spelling in the source text are therefore not observable
in the canonical bytes.

Two consequences are normative and MUST NOT be conflated:

1. **Canonicalization is total over the JSON data model.** It asserts nothing
   about whether the value is a well-formed Aura protocol object, whether its
   `object_type` exists, or whether its `event_type` is registered.
2. **Protocol operations are not.** Where a protocol operation canonicalizes an
   Aura entity (§3, §4), that entity MUST be validated per §7 *before*
   canonicalization, and a validation failure MUST be fail-closed per APS-001 §8.
   Canonicalizing an invalid object does not make it valid.

> **Gap (OPEN, non-blocking for this section):** §4 requires `integrity_hash` to
> be "SHA-256 hash of the canonical serialization of this object" without stating
> how the self-referential `integrity_hash` member is excluded from its own
> input. §8.4 fixes the *byte domain*; the *member-exclusion rule* for
> `integrity_hash` remains an open APS-200 entity-model decision and is not
> settled by this section. The same open question applies to APS-300
> `evidence_hash`.

### 8.3 Delegated rules

The following are **delegated in full to RFC 8785** and MUST NOT be redefined,
narrowed, or extended by any Aura document, implementation, or fixture:

| Rule | Authority |
|---|---|
| Object member ordering | RFC 8785 §3.2.3 (sort on UTF-16 code units of the member name) |
| Number serialization | RFC 8785 §3.2.2.3 (ECMAScript `Number::toString`) |
| String escaping and control-character handling | RFC 8785 §3.2.2.2 |
| Literal representation of `true`, `false`, `null` | RFC 8785 §3.2.2 |
| Structural characters and absence of whitespace | RFC 8785 §3.2.2 |

Two further rules are stated here because they are protocol constraints on what
may be presented to the canonicalizer, not redefinitions of RFC 8785:

1. **No non-JSON numeric values.** `NaN`, `+Infinity`, and `-Infinity` are not
   values of the JSON data model. An implementation MUST fail closed rather than
   emit or accept any encoding of them. This is consistent with INV-007
   (zero-float runtime); INV-007 remains the governing rule for whether a float
   may appear at all.
2. **Duplicate member names.** The JSON data model admits no duplicate member
   names. An implementation MUST reject an input whose source text contains a
   duplicate member name rather than silently retaining the first or last
   occurrence.

**Unicode normalization is NOT performed.** Aura does not apply NFC, NFD, NFKC,
NFKD, case folding, alias expansion, or any other normalization to member names
or string values, either before or after canonicalization. RFC 8785 does not
require it, and no Aura document may introduce it. Two strings that differ in
code points are different strings and produce different canonical bytes, even if
they are canonically equivalent under Unicode normalization.

### 8.4 Hash domain

Every cryptographic operation that this specification defines over an Aura object
consumes the object's **canonical bytes** as raw octets.

```text
canonical bytes
      │
      ├── record digest ──► SHA-256(canonical_bytes)
      │
      └── Merkle leaf   ──► SHA-256(0x00 || canonical_bytes)
```

Normative constraints:

1. The digest input MUST be the canonical bytes of §8.1, and nothing else.
2. `0x00` in the leaf preimage is a single raw octet with value zero. It is not
   the four-character ASCII string `"0x00"`, not the two-character string `"00"`,
   and not a UTF-8 encoding of anything.
3. The following MUST NOT be hashed in place of canonical bytes: JSON source text
   as received; a pretty-printed rendering; a hexadecimal or Base64 rendering of
   the canonical bytes; a sequence of Unicode code points; a language-native
   object; or the hexadecimal text of a previously computed digest.
4. Where a digest is an input to a further cryptographic operation, its 32 raw
   digest octets are the input. A hexadecimal digest string is a presentation
   value only.

Merkle tree semantics, including the interior-node domain
`SHA-256(0x01 || left[32] || right[32])`, odd-node handling, and tree
construction, are owned by APS-001 §7 and the approved DQ-002 hash-domain
decision. This section does not define them and does not modify them. It defines
only which bytes enter the leaf.

### 8.5 Alternate wire encodings

An implementation MAY transport protocol objects in another encoding (for
example CBOR or Protocol Buffers), provided that:

- full model semantics are preserved;
- the encoding round-trips to the same JSON data model value; and
- every canonical byte sequence and every digest required by this specification
  is computed from the RFC 8785 canonical bytes of that value, never from the
  alternate encoding.

An alternate encoding is a transport representation. It is never the canonical
byte domain, and it never participates in a hash domain.

### 8.6 Version binding

The canonical serialization profile is bound to `protocol_version`, per the
version semantics of APS-001 §12.

- `protocol_version` identifies the normative protocol contract, which includes
  this section. A change to the canonicalization profile changes canonical bytes
  and therefore every dependent digest; per APS-001 §12 such a change MUST be
  version-bound and accompanied by impact analysis, and it is a `protocol_version`
  change.
- `schema_version` identifies the representation/schema contract of an individual
  entity. It does not select a canonicalization profile. Two objects with
  different `schema_version` values and the same `protocol_version` are
  canonicalized under the same profile.
- The profile is **not independently versioned.** There is no separate
  "canonicalization profile version" field, and implementations MUST NOT infer
  one.

Historical evidence retains the serialization profile identity under which it was
produced. Digests produced before this section became effective MUST NOT be
reinterpreted as RFC 8785 digests, and MUST NOT be compared against RFC 8785
digests as though the profiles were equivalent.

### 8.7 Conformance

An implementation is conformant with this section if, for every fixture in the
canonical corpus, it independently produces canonical bytes that are byte-identical
to the fixture's recorded canonical bytes, together with the recorded
`SHA-256(canonical_bytes)` and `SHA-256(0x00 || canonical_bytes)`.

The normative requirement is the **behaviour defined by RFC 8785 and the resulting
byte sequence**. This specification does not require any particular programming
language, library, package, or package version. The engines used by the reference
implementations are conformance evidence and provenance; they are not part of the
protocol contract, and an implementation MUST NOT be judged non-conformant for
using a different RFC 8785 implementation that produces the same bytes.

A digest that matches without matching canonical bytes is not evidence of
conformance and MUST NOT be recorded as a pass.

The frozen conformance vector for this section is **CANONICAL-001**
(`fixtures/corpus/CANONICAL-001_jcs_evidence.json`), verified by CONF-003.
CANONICAL-001 is a serialization-profile vector over the JSON data model per
§8.2; it is not an instance of an ENT-001…ENT-008 entity and asserts nothing
about entity admissibility.

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

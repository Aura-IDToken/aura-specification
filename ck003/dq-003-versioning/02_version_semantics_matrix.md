# DQ-003 — 02_version_semantics_matrix

**Status:** EVIDENCE MATRIX — NO BINDING DECISION
**Captured:** 2026-08-17
**Basis:** `01_current_versioning_snapshot` and the repository evidence identified there.
**Purpose:** Separate the version namespaces actually present in Aura, define what each namespace is allowed to mean from current evidence, and identify the unresolved normative bindings before any production change.

---

## 1. Decision rule

This matrix deliberately distinguishes:

1. **Observed semantics** — directly supported by the current evidence snapshot.
2. **Compatibility semantics** — what the versioning policy explicitly assigns to the namespace.
3. **Digest/evidence role** — whether current evidence establishes that the version participates in canonical bytes or a digest.
4. **Binding status** — whether the namespace has a normative mapping to `protocol_version`.

No value is assigned to `protocol_version` by this artifact.

---

## 2. Master version-semantics matrix

| Namespace / field | Current value / example | Semantic owner | Scope | Version change meaning supported by evidence | Runtime field? | Digest-domain role established? | Can equal `protocol_version` today? | Status / required action |
|---|---|---|---|---|---|---|---|---|
| **Specification repository release** | `0.1.0` | `aura-specification` release metadata | Whole specification repository/release | Repository follows SemVer; `MAJOR` = breaking protocol change, `MINOR` = new APS/invariant/conformance test/backward-compatible extension, `PATCH` = errata/clarification without normative behavioral change | No | **Not established** | **Not established** | Existing release namespace; requires explicit normative binding before reuse as protocol version |
| **Versioning policy** | `POL-VER-001` `1.0-DRAFT` | `VERSIONING.md` | Governance/policy document | Document itself is versioned as an APS/policy artifact | No | No evidence of digest role | **No** — document version is not established as protocol version | Keep separate from protocol identity |
| **APS-200 document version** | `1.0-DRAFT` | APS-200 | Canonical Data Model specification | APS documents use `MAJOR.MINOR[-STATUS]`; frozen documents retain version and revisions create new documents | No | **Not established** | **No** — document version ≠ protocol version absent explicit rule | Must remain document identity unless a future normative rule binds it |
| **APS-300 document version** | `1.0-DRAFT` | APS-300 | Evidence Model specification | Same APS document-versioning model | No | **Not established** | **No** — document version ≠ protocol version absent explicit rule | Must remain document identity unless a future normative rule binds it |
| **APS-100 / invariant version** | Versioned with APS-100 | APS-100 | Invariant registry/contract | Invariants are versioned with APS-100 | No | **Not established** | **No** | Conformance/invariant identity; not protocol identity |
| **APS-400 / conformance-test version** | Versioned with APS-400 | APS-400 | Conformance tests | Conformance tests are versioned with APS-400 | No | No evidence | **No** | Test-suite identity; must not be overloaded into protocol identity |
| **Fixture version** | `fixture_version` | Fixture specification | Individual cross-language/test fixture | Fixtures carry their own version | No | Fixture-specific; not protocol digest semantics | **No** | Test-vector identity; keep independent |
| **Core instrument lineage** | `v3.3` | Aura Core | Frozen measurement instrument lineage | Core README explicitly distinguishes frozen instrument identity from software/protocol version | No separate field established | **Not established** | **No** — snapshot explicitly warns against equating it with protocol version | Preserve as instrument lineage |
| **Guard package version** | `1.3.0` | Rust/Cargo package metadata | Aura-Guard implementation/package | Package release identity | Yes, package metadata | No evidence that package version is protocol digest input | **No** — implementation/package version is not protocol version | Keep as implementation version |
| **Core `schema_version`** | `1.0.0` | Core certificate representation | Schema/representation contract | Existing runtime field; current evidence does not define full compatibility policy for its values | Yes | **Potentially relevant**, because the field is part of the certificate object; exact digest inclusion rule is not established by current DQ-003 evidence | **No** — it is explicitly a separate required namespace | Needs formal schema-version semantics and compatibility rules |
| **Guard `schema`** | String field | Guard `AuditEntry` DTO | Guard audit-entry representation | Current evidence shows one `schema` field, not separate protocol/schema fields | Yes | **Not established** | **No** — insufficient evidence to equate it with either namespace | Needs mapping to the canonical contract or an explicit compatibility adapter |
| **`protocol_version`** | **No authoritative runtime value established** | Aura protocol specification | Protocol semantic contract | APS-200 and APS-300 require the field; exact value-selection and lifecycle rule remain unresolved | Required by normative model, not consistently represented in current implementations | **Not yet bound** by current DQ-003 evidence | **N/A** — this is the target namespace | **OPEN — requires normative binding decision** |
| **`implementation_version`** | Not currently explicit in Core certificate | Implementation | Concrete implementation release | Not defined as a normative protocol namespace in current evidence | Not consistently present | Not established | **No** | If needed, define separately rather than overloading protocol/schema versions |

---

## 3. SemVer semantics currently supported by `VERSIONING.md`

The repository-level versioning policy assigns the following meanings:

```text
MAJOR  -> breaking protocol change
MINOR  -> new APS / invariant / conformance test / backward-compatible extension
PATCH  -> errata or clarification without normative behavioural change
```

This is important because it makes the **specification release namespace protocol-related**, but it does **not by itself establish that the repository release string is the runtime value of `protocol_version`**.

That final mapping is a separate normative decision and must not be inferred from the existence of SemVer alone.

---

## 4. APS document versions are not protocol versions

The current evidence explicitly distinguishes APS document versions from the protocol as a whole:

```text
APS-200 1.0-DRAFT  ─┐
APS-300 1.0-DRAFT  ─┼──> individual normative documents
APS-100 ...        ─┤
APS-400 ...        ─┘

                    != automatically == protocol_version
```

The same applies to `POL-VER-001` and fixture versions.

A future protocol release may change several APS documents simultaneously. Therefore using an APS document number as the protocol identity would collapse two different versioning layers unless the specification explicitly says otherwise.

---

## 5. Core `v3.3` is an instrument lineage, not protocol identity

The Core README explicitly describes `v3.3` as a frozen/canonical instrument lineage and states that it is not a software version.

Therefore:

```text
Core v3.3
    !=
protocol_version
```

unless a future specification revision explicitly establishes such a mapping.

This distinction is operationally important: changing the implementation of a frozen instrument and changing the protocol contract are not automatically the same event.

---

## 6. Guard `1.3.0` is implementation/package identity

`Cargo.toml` provides:

```text
package.name    = aura-guard
package.version = 1.3.0
```

That identifies the released Rust implementation/package. It does not establish the semantic version of the Aura protocol.

Therefore:

```text
Guard 1.3.0
    !=
protocol_version
```

A future Guard release may implement the same protocol version, and one protocol release may be implemented by multiple Guard package versions.

---

## 7. `schema_version` semantics

The current Core certificate has:

```text
schema_version = "1.0.0"
```

APS-200 and APS-300 separately require `schema_version` alongside `protocol_version`.

The current evidence therefore supports this conceptual separation:

```text
protocol_version  -> semantic protocol contract
schema_version    -> representation/schema contract
```

However, the evidence does **not yet define**:

- whether schema versions are SemVer or another controlled format;
- what constitutes a MAJOR/MINOR/PATCH schema change;
- compatibility guarantees between schema versions;
- whether a schema-only change may occur without a protocol-version change;
- whether `schema_version` is included in the canonical digest domain;
- whether changing `schema_version` necessarily changes `evidence_hash` / `integrity_hash`.

Those are DQ-003 closure questions, not assumptions to be made in implementation.

---

## 8. Digest-domain impact — current evidence boundary

The version fields are normative fields of the canonical/evidence objects, but the current DQ-003 evidence does **not** provide a sufficiently explicit statement that resolves all of the following:

```text
Is protocol_version part of canonical bytes?       OPEN
Is schema_version part of canonical bytes?         OPEN
Is implementation_id part of canonical bytes?     OPEN
Does changing schema_version change evidence_hash? OPEN
Does changing protocol_version change evidence_hash? OPEN
```

This must be reconciled with the already-approved DQ-002 hash-domain model. DQ-002 chose the **RI-RS raw-byte + domain-separation model**, but that decision defines how bytes are hashed; it does not by itself define which version fields are included in the canonical object.

Therefore DQ-002 and DQ-003 remain cleanly separated:

```text
DQ-002 = HOW canonical bytes are hashed
DQ-003 = WHAT version semantics and bindings those bytes carry
```

---

## 9. Compatibility matrix

| Change | Current evidence permits classification? | Expected protocol impact | Required before implementation |
|---|---|---|---|
| Repository patch release for typo/errata | Yes | No normative protocol change | Existing SemVer policy sufficient |
| New APS document | Yes | May be backward-compatible extension under policy | Protocol impact statement still required |
| Change to existing APS field semantics | Partially | Potentially breaking | Explicit compatibility/migration decision |
| Change to JSON/schema representation only | **No complete rule** | Unknown | Define `schema_version` compatibility policy |
| Change `protocol_version` value | **No lifecycle rule** | Potentially protocol-level | Define exact release/binding rule |
| Change Core instrument lineage `v3.3` | Yes as implementation lineage | Not automatically protocol-breaking | Keep separate from protocol version |
| Change Guard package `1.3.0` | Yes as package release | Not automatically protocol-breaking | Keep separate from protocol version |
| Change fixture version | Yes | Test-vector evolution | Must not alter protocol identity by implication |

---

## 10. Required normative binding questions

DQ-003 cannot be closed until the specification answers these questions explicitly:

### Q1 — What is `protocol_version`?

Candidate interpretations currently visible in the evidence:

```text
A. aura-specification repository release
B. independently assigned protocol release
C. APS aggregate/version line
D. another explicit protocol identifier
```

The evidence does **not** currently select one.

### Q2 — Who owns it?

The owner must be the normative protocol governance layer, not Core or Guard package metadata.

### Q3 — What changes it?

The specification must define which normative changes require a protocol MAJOR/MINOR/PATCH increment.

### Q4 — What is `schema_version`?

The specification must define its scope and compatibility semantics independently of `protocol_version`.

### Q5 — What is the relation between them?

At minimum, the protocol should explicitly define whether:

```text
schema_version may change while protocol_version stays constant
```

and under what compatibility constraints.

### Q6 — Are they digest-bound?

The canonical serialization specification must explicitly establish whether these fields participate in canonical bytes and therefore in the relevant digest.

### Q7 — How do Core and Guard expose them?

The implementations must eventually expose the normative fields without overloading:

```text
Core v3.3
Guard 1.3.0
schema_version 1.0.0
protocol_version ?
```

---

## 11. Proposed target separation — NOT YET NORMATIVE

The following is a **design proposal only**, not a specification decision:

```text
                         AURA PROTOCOL
                              │
                    protocol_version = P
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
       APS-100             APS-200             APS-300
      invariants        canonical model       evidence model
          │                   │                   │
       own doc             own doc             own doc
       version             version             version

Implementation layer:

Core instrument lineage = v3.3
Guard implementation    = 1.3.0
Canonical schema        = schema_version 1.0.0
```

This model preserves independent evolution while allowing the protocol contract to bind them explicitly.

It must not be treated as adopted until the corresponding normative ADR/specification change is approved.

---

## 12. DQ-003 matrix verdict

**Evidence status:** SUFFICIENT to identify the version namespaces and the exact unresolved semantic boundary.

**Binding status:** OPEN.

**Production changes:** NONE.

**Safe conclusions:**

- `Core v3.3` is not automatically `protocol_version`.
- `Guard 1.3.0` is not automatically `protocol_version`.
- APS document versions are not automatically `protocol_version`.
- `schema_version` and `protocol_version` are distinct normative fields.
- The specification currently requires both fields but does not yet provide enough evidence for a unique runtime binding of `protocol_version`.
- DQ-002 hash-domain selection does not by itself resolve DQ-003 field/version semantics.

**Next artifact:** `03_version_binding_adr` — an explicit decision document that selects the ownership, value source, lifecycle, compatibility semantics, and digest-binding rules for `protocol_version` and `schema_version`.

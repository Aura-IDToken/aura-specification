# DQ-003 — 01_current_versioning_snapshot

**Status:** EVIDENCE SNAPSHOT — NO ARCHITECTURAL DECISION
**Captured:** 2026-08-17
**Purpose:** Record the versioning state actually present in the three Aura repositories before DQ-003 remediation.

## 1. Evidence boundary

This snapshot records repository state and normative text only. It does not choose a value for `protocol_version`, does not change Core or Guard, and does not reconcile conflicting or incomplete semantics.

### Repositories

| Repository | Default branch | Snapshot HEAD | Relevant implementation/version evidence |
|---|---|---|---|
| `Aura-IDToken/aura-specification` | `main` | `62d2d6bcc1a46dd505ebfe400ad01fa3c6a25bf0` | repository release `0.1.0`; VERSIONING policy `1.0-DRAFT` |
| `Aura-IDToken/aura-poc-a-core-v3.3` | `main` | `64bf959b1d23fbd5433723476c611ab66d423953` | Iron Core `v3.3`; README explicitly distinguishes frozen instrument version from protocol version |
| `Aura-IDToken/aura-guard-v1.3` | `main` | `cd3494b91bf61db060ca5d57f02d061e7ac22da5` | Cargo package version `1.3.0` |

## 2. Specification versioning model

`VERSIONING.md` is `POL-VER-001`, version `1.0-DRAFT`. It states:

- the repository follows Semantic Versioning `MAJOR.MINOR.PATCH`;
- MAJOR means a breaking protocol change;
- MINOR means a new APS document, invariant, conformance test, or backward-compatible extension;
- PATCH means errata/clarification without normative behavioral change;
- individual APS documents use `MAJOR.MINOR[-STATUS]`;
- frozen APS documents retain their version and a revision creates a new document;
- invariants are versioned with APS-100;
- conformance tests are versioned with APS-400;
- fixtures carry their own `fixture_version`.

Source: `VERSIONING.md`, blob SHA `636119d7d13b485c81805f874dd618d8dc56cc74`.

## 3. Current specification release state

`CHANGELOG.md` records:

- `0.1.0` dated 2026-07-23 as the initial import/release;
- `Unreleased` containing subsequent canonical structure and governance additions.

Therefore the repository has a release version `0.1.0`, while `main` is currently ahead of that release at commit `62d2d6b...`.

Source: `CHANGELOG.md`, blob SHA `73656247d7021ac2f469f0412dd8dab2219ce5cc`.

## 4. APS-200 current contract

`APS-200 — Canonical Data Model`, version `1.0-DRAFT`, status `DRAFT`, defines the common object contract. Every canonical entity MUST contain:

- `object_id`
- `object_type`
- `protocol_version`
- `schema_version`
- `created_at`
- `integrity_hash`

APS-200 also states that data-model changes are subject to semantic versioning and must specify compatibility impact, migration requirements, and backward compatibility where applicable.

Source: `APS-200 — Canonical Data Model_260723_192852.txt`, blob SHA `559e0e0c0bfb4f47588b3d0c6fdc8145eaa6b313`.

## 5. APS-300 current contract

`APS-300 — Evidence Model`, version `1.0-DRAFT`, status `DRAFT`, defines the Canonical Evidence Object. It requires at minimum:

- `evidence_id`
- `protocol_version`
- `schema_version`
- `implementation_id`
- `execution_id`
- `timestamp`
- `policy_reference`
- `input_hash`
- `output_hash`
- `evidence_hash`
- `previous_evidence_hash` when applicable
- `attestation_reference`

APS-300 therefore independently confirms that both `protocol_version` and `schema_version` are normative Evidence fields.

Source: `APS-300 — Evidence Model_260723_193234.txt`, blob SHA `c498639a242107c57d78039fe927e0e55c9d084a`.

## 6. Current Core implementation state

The current Core certificate implementation (`compliance/certificate.py`) contains:

```text
schema_version = "1.0.0"
```

but the certificate representation contains no `protocol_version` field and no explicit `implementation_version` field.

The same file currently represents `ari_score` and `drift` as Python `float`, despite its documentation describing the underlying measurement as int32 fixed-point. This is recorded here only as adjacent evidence; it is not a DQ-003 decision.

Source: `compliance/certificate.py`, blob SHA `823bb743eda461ce54bdf666360135e000eb0a3a`.

Core README identifies the repository as `AURA PROTOCOL — IRON CORE v3.3`, describes v3.3 as a frozen/canonical instrument, and explicitly states that `v3.3 Iron Core refers to a frozen instrument, not a software version`; changes require a new lineage. This is evidence that `v3.3` must not automatically be equated with `protocol_version`.

Source: Core `README.md`, blob SHA `6a8200081562d77b3a6467f6bc01931b2f82046c`.

## 7. Current Guard implementation state

`Cargo.toml` declares:

```text
package.name = "aura-guard"
package.version = "1.3.0"
```

`src/models.rs` defines `AuditEntry.schema: String`, but the DTO does not currently expose separate `protocol_version` and `schema_version` fields under those names.

Source: `Cargo.toml`, blob SHA `2c0c0ce0e62ad1d7e193f35feab457e7bafc0382`.
Source: `src/models.rs`, blob SHA `02c7b528e3ba5586b2e29933fa24ad4d28f379a6`.

Therefore `aura-guard` package version `1.3.0` is implementation/package metadata, not evidence that the protocol itself is version `1.3.0`.

## 8. Version namespaces observed at snapshot time

The repositories currently expose at least these distinct version concepts:

| Namespace | Observed value/example | Source | Status |
|---|---|---|---|
| Specification repository release | `0.1.0` | CHANGELOG | Existing release metadata |
| Versioning policy document | `1.0-DRAFT` | VERSIONING.md | Draft governance policy |
| APS document version | `1.0-DRAFT` | APS-200 / APS-300 | Draft normative documents |
| Core instrument lineage | `v3.3` | Core README | Frozen instrument identity |
| Guard package/implementation | `1.3.0` | Cargo.toml | Implementation/package metadata |
| Evidence `schema_version` | `1.0.0` | Core certificate.py | Existing implementation field |
| Protocol `protocol_version` | **No single authoritative value established in implementation** | Core/Guard inspection | OPEN |

## 9. Normative gap captured by DQ-003

The evidence establishes that the protocol requires both `protocol_version` and `schema_version`, but this snapshot does not establish a single authoritative mapping from the specification repository's release/document versions to the runtime value of `protocol_version`.

The following equivalences are therefore **NOT established by this snapshot**:

```text
protocol_version == repository release version
protocol_version == APS-200 version
protocol_version == APS-300 version
protocol_version == Core v3.3
protocol_version == Guard 1.3.0
```

No such equivalence is to be inferred without an explicit normative decision.

## 10. Integrity references

| Artifact | SHA recorded by GitHub |
|---|---|
| VERSIONING.md | `636119d7d13b485c81805f874dd618d8dc56cc74` |
| CHANGELOG.md | `73656247d7021ac2f469f0412dd8dab2219ce5cc` |
| APS-200 TXT | `559e0e0c0bfb4f47588b3d0c6fdc8145eaa6b313` |
| APS-300 TXT | `c498639a242107c57d78039fe927e0e55c9d084a` |
| Core README.md | `6a8200081562d77b3a6467f6bc01931b2f82046c` |
| Core compliance/certificate.py | `823bb743eda461ce54bdf666360135e000eb0a3a` |
| Guard Cargo.toml | `2c0c0ce0e62ad1d7e193f35feab457e7bafc0382` |
| Guard src/models.rs | `02c7b528e3ba5586b2e29933fa24ad4d28f379a6` |

## 11. Snapshot verdict

**DQ-003 / 01_current_versioning_snapshot: COMPLETE.**

**Evidence verdict:** version namespaces are present and distinguishable, but the authoritative semantics and binding of `protocol_version` remain unresolved.

**No production remediation performed.**

**Next artifact:** `02_version_semantics_matrix`.

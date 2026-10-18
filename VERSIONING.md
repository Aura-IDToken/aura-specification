# Versioning Policy

Document ID: POL-VER-001  
Version: 1.0-DRAFT  
Authority: AURA Constitution Article XI

---

## 1. Scope

This document defines the versioning model for all artifacts in the `aura-specification` repository, including APS documents, Protocol Invariants, Conformance Tests, Reference Fixtures, and releases.

---

## 2. Repository Release Versioning

The repository itself follows **Semantic Versioning** (`MAJOR.MINOR.PATCH`):

| Segment | Meaning |
|---------|---------|
| MAJOR | Breaking change to the protocol (incompatible Evidence Pack, Invariant removal, etc.) |
| MINOR | New APS document, new Invariant, new Conformance Test, or backward-compatible extension |
| PATCH | Errata, clarifications, typo corrections that do not change normative behavior |

---

## 3. Document Status Lifecycle

Every APS document and governance artifact passes through the following lifecycle:

```
DRAFT → REVIEW → APPROVED → FROZEN
                           ↘ DEPRECATED → ARCHIVED
```

| Status | Meaning | Mutable? |
|--------|---------|----------|
| DRAFT | Under active authoring; may change freely | Yes |
| REVIEW | Under Architecture Review; changes require justification | With justification |
| APPROVED | Formally approved; changes require RFC + ADR | Via RFC/ADR only |
| FROZEN | Immutable; content cannot change | No |
| DEPRECATED | Superseded; retained for reference | No |
| ARCHIVED | No longer active; historical record only | No |

Draft-stage authoring MAY use explicit draft-only placeholder digest/checksum values inside working fixtures or unpublished contracts when the final publication boundary is not yet approved. Such placeholders MUST be replaced or superseded before approval, freeze, or release evidence publication.

### Transition Rules

- `DRAFT → REVIEW`: Author submits document for review via pull request
- `REVIEW → APPROVED`: Chief Architect approves after Architecture Review
- `APPROVED → FROZEN`: Explicit freeze decision by Chief Architect; requires Amendment Procedure (Constitution Article XI)
- `APPROVED/FROZEN → DEPRECATED`: Requires new version of superseding document and formal deprecation notice
- `DEPRECATED → ARCHIVED`: After defined sunset period (minimum 2 major versions)

---

## 4. Document Version Numbers

Individual APS documents use `MAJOR.MINOR[-STATUS]` notation:

- `1.0-DRAFT`
- `1.0-REVIEW`
- `1.0`
- `1.0-FROZEN`
- `2.0-DRAFT` (if revised after approval)

A FROZEN document **never receives a new version number**. A revision creates a new document (e.g., APS-200 v2.0-DRAFT).

---

## 5. Protocol Invariant Versioning

- Invariants are versioned with the APS-100 document that defines them.
- A new Invariant is a MINOR change to APS-100.
- Removing or relaxing an Invariant is a MAJOR change to APS-100 and to the repository.
- Invariant IDs (INV-xxx) are **never reused**.

---

## 6. Conformance Test Versioning

- Conformance Tests are versioned with the APS-400 document.
- Adding a new CONF-xxx test is a MINOR change.
- Changing the PASS/FAIL criteria of an existing test is a MAJOR change.
- Test IDs (CONF-xxx) are **never reused**.

---

## 7. Reference Fixture Versioning

- Each fixture carries its own `fixture_version` field.
- A fixture whose Expected Output changes is a new fixture (new ID).
- Old fixture IDs are deprecated, not overwritten.
- Fixture IDs (FIX-xxx) are **never reused**.

### 7.1 Current draft compatibility matrix

Compatibility decisions are explicit and version-bound. They MUST NOT be inferred from numeric ordering, lexical ordering, or partial field overlap.

The current repository-local draft compatibility matrix is maintained in:

- `ck003/decisions/DQ-003/CURRENT_VERSION_COMPATIBILITY_MATRIX.md`
- `ck003/decisions/DQ-003/CURRENT_VERSION_COMPATIBILITY_MATRIX.json`

For the current draft working path:

| Protocol version | Allowed schema versions | Allowed input schema | Allowed evidence profile | Allowed fixture bindings |
|---|---|---|---|---|
| `1.0-DRAFT` | `EvaluationRequest=1.0-DRAFT`, `EvaluationResult=1.0-DRAFT`, `PolicyReference=1.0-DRAFT`, `Attestation=1.0-DRAFT`, `EvidencePack=1.0-DRAFT` | `AURA-DRAFT-CORE-001` | `EPR-CORE` | `FIX-001@0.2-DRAFT`, `FIX-COMPAT-001@0.1-DRAFT` |

Any combination outside the matrix is incompatible in strict conformance mode until explicitly added by a versioned specification change with impact analysis.

---

## 8. Identifier Reuse Policy

Per APS-000 §4:

> One identifier MUST never be reused.

This applies to: APS-xxx, INV-xxx, CONF-xxx, FIX-xxx, EVID-xxx, ADR-xxx, RFC-xxx, REL-xxx.

---

## 9. Release Artifacts

Each repository release MUST include:
- A `releases/vX.Y.Z/` directory
- `RELEASE_NOTES.md`
- `CONFORMANCE_REPORT.md` (linking to applicable test results)
- `DOCUMENT_STATUS.md` (snapshot of all document statuses)
- SHA-256 checksums for all canonical documents

---

## 10. Amendment

Changes to this versioning policy require an RFC per [CONTRIBUTING.md](CONTRIBUTING.md) and approval by the Chief Architect.

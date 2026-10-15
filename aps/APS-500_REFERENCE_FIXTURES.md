# APS-500 — Reference Fixtures

Document ID: APS-500  
Version: 1.0-DRAFT  
Status: DRAFT  
Classification: Normative Test Specification  
Authority: APS-001 §9 · APS-100 · APS-200 · APS-300 · APS-400
Last Review: 2026-09-26

---

## 1. Purpose

APS-500 defines the canonical set of Reference Fixtures used to validate Aura Protocol implementations.

Every conformant implementation MUST pass the **normative APS-500 fixture corpus** unchanged.

Working fixtures and closure artifacts may exist elsewhere in the repository before they are promoted into the normative APS-500 corpus. Their presence alone does not make them certification-ready fixtures.

---

## 2. Objectives

Reference Fixtures provide:
- **Comparability** — all implementations tested against identical data
- **Repeatability** — tests produce identical results over time
- **Deterministic validation** — no ambiguity in pass/fail
- **Certification basis** — fixtures are the foundation of conformance certification

---

## 3. Fixture Structure

Each **normative APS-500 fixture** MUST contain:

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `fixture_id` | string | MUST | Unique identifier (`FIX-NNN`) |
| `fixture_version` | string | MUST | Semantic version |
| `protocol_version` | string | MUST | Target APS version |
| `description` | string | MUST | Human-readable description |
| `input_data` | object | MUST | Canonical input (APS-200 ENT-002 structure) |
| `expected_output` | object | MUST | Expected Evaluation Result (APS-200 ENT-003 structure) |
| `expected_evidence` | object | MUST | Expected Evidence Pack (APS-300) structure |
| `related_invariants` | array | MUST | List of INV-xxx identifiers |
| `related_conformance_tests` | array | MUST | List of CONF-xxx identifiers |

Working corpus artifacts used during closure work MAY be structurally incomplete while the underlying APS-200 / APS-300 contracts are still open. Such artifacts are non-normative until explicitly promoted.

---

## 4. Fixture Categories

| Category | Purpose |
|----------|---------|
| `FIX-CORE` | Baseline operation scenarios |
| `FIX-BOUNDARY` | Boundary value testing |
| `FIX-ERROR` | Error handling |
| `FIX-REPLAY` | Replay verification |
| `FIX-EVIDENCE` | Evidence Pack validation |
| `FIX-COMPAT` | Cross-version compatibility |

---

## 5. Current Corpus Posture

The repository currently contains three distinct kinds of fixture artifacts:

1. **PLACEHOLDER**
   - file exists, but canonical test content is still TODO-bound
2. **WORKING**
   - useful closure or development artifact, but not yet fit for normative APS-500 promotion
3. **CANDIDATE NORMATIVE**
   - concrete fixture content exists and can be promoted once the remaining explicit gate closes

### 5.1 Fixture Promotion Register

| Artifact | Class | Related CONF | Current posture | Explicit promotion gate |
|---|---|---|---|---|
| `fixtures/core/FIX-001_BASIC_EVALUATION.json` | WORKING | `CONF-001`, `CONF-002`, `CONF-004`, `CONF-005`, `CONF-006`, `CONF-010` | request/result payload and current draft `EPR-CORE` evidence content are now concrete, and a repository-local verifier executes the current draft request/result/evidence/replay/platform gate | controlled implementation-side evidence + explicit APS-500 promotion |
| `fixtures/compatibility/FIX-COMPAT-001_VERSION_MATRIX.json` | WORKING | `CONF-008` | concrete repository-local compatibility fixture bound to the current DQ-003 matrix and draft runner | implementation-side RI evidence + explicit APS-500 promotion |
| `fixtures/corpus/FIX-INV-007_zero_float.json` | CANDIDATE NORMATIVE | `CONF-011` | concrete fixture content exists and is explicitly bound to `CONF-011` | controlled execution evidence + explicit APS-500 promotion |
| `fixtures/corpus/FIX-INV-012_event_type.json` | WORKING | `CONF-012` | fixture now binds one concrete draft Audit Record and the current local DQ-004 registry token | broader approved event vocabulary + implementation-side evidence |
| `fixtures/corpus/FIX-INV-013_policy_determinism.json` | CANDIDATE NORMATIVE | `CONF-013` | fixture now binds one concrete policy/input pair | controlled execution evidence + explicit APS-500 promotion |
| `fixtures/corpus/FIX-INV-014_aps500_compatibility.json` | WORKING | `CONF-014` | structurally present but blocked on corpus versioning | finalized normative APS-500 corpus version |
| `fixtures/corpus/FIX-INV-015_canonical_identity.json` | WORKING | `CONF-015` | identity semantics not yet finally bound | APS-000 / APS-200 identity closure |
| `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | WORKING | `CONF-003` | strong evidence vector exists | discriminating RFC 8785 vector for final CONF-003 PASS |
| `fixtures/corpus/CANONICAL-002_jcs_discriminating.json` | WORKING | `CONF-003` | first discriminating candidate fixture is prepared for cross-language execution | execute on RI-PY + RI-RS and record observed bytes |
| `fixtures/corpus/CANONICAL-003_jcs_full_discriminator.json` | WORKING | `CONF-003` | [2026-10-15 technical evidence report](../ck003/dq-006-final-closure-execution/DQ-006_CANONICAL-003_TECHNICAL_EVIDENCE_REPORT_2026-10-15.md) records both receivers matching the frozen 577-byte oracle and matching canonical/leaf digests; fixture is non-normative and DQ-006 remains OPEN | reconcile source-of-record/reachability and explicitly promote through APS-500 |
| `fixtures/ck003/manifest.json` | WORKING | working corpus index | orchestration/support artifact only | promote referenced fixtures individually |
| `fixtures/ck003/expected_digests.json` | WORKING | serialization support | unresolved digest slots intentionally preserved | freeze canonical-byte / registry / identity dependencies |

### 5.2 Minimum early execution package

Before the full APS-500 corpus is frozen, the first meaningful conformance wave should focus on:

1. `FIX-INV-007` with `CONF-011`
2. `FIX-INV-013` with `CONF-013`
3. `CANONICAL-001` and `CANONICAL-002` with `CONF-003`, using the recorded CANONICAL-003 RI-PY/RI-RS execution as additional DQ-006 evidence; source-of-record/reachability and ratification gaps remain open, so DQ-006 is not closed.

### 5.3 Placeholder baseline fixture

**FIX-001 — Basic Evaluation**
**Category:** FIX-CORE
**Related Test:** CONF-001
**Related Invariants:** INV-001, INV-014
**Status:** WORKING — current draft input/output payload and `EPR-CORE` evidence content are bound, but controlled execution evidence is still pending
See [../fixtures/core/FIX-001_BASIC_EVALUATION.json](../fixtures/core/FIX-001_BASIC_EVALUATION.json)

---

## 6. Fixture Versioning

Each fixture carries:
- `fixture_id` — permanent, never reused
- `fixture_version` — semantic version
- `protocol_version` — APS version this fixture targets

A fixture whose Expected Output changes becomes a new fixture with a new ID. Old fixtures are deprecated, not modified.

---

## 7. Validation Rules

An implementation MUST:
- Use **normative APS-500 fixtures** unmodified
- Produce the expected output
- Produce the expected Evidence Pack
- Pass all related Conformance Tests

Working corpus artifacts may be used during closure work, but they MUST NOT be reported as normative PASS evidence until they are promoted into the APS-500 corpus.

---

## 8. Traceability

```
Protocol Requirement
        ↓
Protocol Invariant
        ↓
Conformance Test (CONF-xxx)
        ↓
Reference Fixture (FIX-xxx)
        ↓
Evidence Pack
```

---

## 9. Certification

Reference Fixtures are the mandatory basis of the certification process. Failure on a required **normative** fixture = failure of the related Conformance Test.

---

## 10. Repository Organization

Fixtures are stored in [`../fixtures/`](../fixtures/):

```
fixtures/
├── README.md
├── ck003/                working manifests and expected digests for closure work
├── compatibility/        FIX-COMPAT fixtures
├── corpus/               working fixture corpus for open closure items
├── schemas/              JSON Schema definitions for APS-200 entities
├── core/                 FIX-CORE fixtures
├── boundary/             FIX-BOUNDARY fixtures
├── error/                FIX-ERROR fixtures
├── replay/               FIX-REPLAY fixtures
└── evidence/             FIX-EVIDENCE fixtures
```

Only fixtures explicitly promoted into the normative APS-500 corpus are certification-grade fixtures.

---

*Source: Original text preserved in [`APS-500 Reference Fixtures_260723_194023.txt`](../APS-500%20Reference%20Fixtures_260723_194023.txt)*

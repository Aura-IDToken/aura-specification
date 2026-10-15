# Fixtures

This directory contains Reference Fixtures as defined in APS-500.

## Directory Structure

```
fixtures/
├── README.md               This file
├── ck003/                  CK-003 manifests and expected digests
├── corpus/                 Working fixture corpus for open closure items
├── schemas/                JSON Schema definitions for APS-200 entities
├── compatibility/          FIX-COMPAT — explicit version-compatibility fixtures
├── core/                   FIX-CORE — baseline operation scenarios
└── ...                     Additional APS-500 categories added as they are stabilized
```

## Status

> **Current state**: The canonical APS-500 fixture corpus is not yet finalized. Draft machine-readable APS-200/APS-300 schemas now exist under `/fixtures/schemas/`; `FIX-001` now binds the current draft ENT-002/ENT-003 working-profile payload and the current draft `EPR-CORE` evidence pack content, while `/fixtures/corpus/` and `/fixtures/ck003/` still contain working fixtures and manifests for closure work that do not by themselves constitute release-ready APS-500 coverage.

## Fixture Index

| Fixture ID | Name | Category | CONF Test | Status |
|------------|------|----------|-----------|--------|
| FIX-001 | Basic Evaluation | CORE | CONF-001, CONF-002, CONF-004, CONF-005, CONF-006, CONF-010 | WORKING |
| FIX-COMPAT-001 | Version Compatibility Matrix | COMPATIBILITY | CONF-008 | WORKING |
| FIX-INV-007 | Zero Float Runtime | CORPUS | CONF-011 | READY |
| FIX-INV-012 | Event Type / Auditability | CORPUS | CONF-012 | WORKING |
| FIX-INV-013 | Policy Determinism | CORPUS | CONF-013 | READY |
| FIX-INV-014 | APS-500 Compatibility | CORPUS | CONF-014 | APS500_VERSION_BLOCKED |
| FIX-INV-015 | Canonical Identity | CORPUS | CONF-015 | APS000_BINDING_BLOCKED |
| `CANONICAL-002` | JCS Discriminator (UTF-16 ordering) | CORPUS | CONF-003 | WORKING — NOT EXECUTED |
| `CANONICAL-003` | Multi-axis JCS Discriminator | CORPUS | CONF-003 | WORKING — NOT EXECUTED |

## Promotion Classes

Use the following promotion classes when deciding whether an artifact belongs in the normative APS-500 corpus:

| Class | Meaning |
|-------|---------|
| `PLACEHOLDER` | File exists, but canonical input/output/evidence content is still TODO-bound |
| `WORKING` | Closure fixture or support artifact exists and is useful operationally, but is not yet ready for normative APS-500 promotion |
| `CANDIDATE NORMATIVE` | Concrete fixture content exists and can be promoted once the remaining explicit gate is closed |

## Fixture Promotion Register

| Artifact | Class | Reason | Explicit promotion gate |
|----------|-------|--------|-------------------------|
| `core/FIX-001_BASIC_EVALUATION.json` | `WORKING` | Current draft request/result payload and current draft `EPR-CORE` evidence content are concrete, and a repository-local verifier now executes CONF-001/002/004/005/006/010 against it | controlled implementation-side evidence + APS-500 promotion |
| `compatibility/FIX-COMPAT-001_VERSION_MATRIX.json` | `WORKING` | Binds the current DQ-003 matrix to executable positive/negative compatibility cases for CONF-008 | implementation-side RI evidence + APS-500 promotion |
| `corpus/FIX-INV-007_zero_float.json` | `CANDIDATE NORMATIVE` | Fixture is now explicitly bound to `CONF-011` and marked ready for controlled execution | controlled execution evidence + APS-500 promotion |
| `corpus/FIX-INV-012_event_type.json` | `WORKING` | Binds one concrete draft Audit Record and the current local DQ-004 registry token for CONF-012 | broader approved event vocabulary + implementation-side evidence |
| `corpus/FIX-INV-013_policy_determinism.json` | `CANDIDATE NORMATIVE` | Fixture now binds one concrete policy/input pair for `CONF-013` | controlled execution evidence + APS-500 promotion |
| `corpus/FIX-INV-014_aps500_compatibility.json` | `WORKING` | Fixture is present but explicitly blocked on corpus/version binding | finalized APS-500 corpus version |
| `corpus/FIX-INV-015_canonical_identity.json` | `WORKING` | Identity expectations exist, but canonical fields are not yet normatively fixed | APS-000 / APS-200 identity closure |
| `corpus/CANONICAL-001_jcs_evidence.json` | `WORKING` | Strong evidence vector, but not yet discriminating enough for final profile closure | discriminating RFC 8785 vector (DQ-006 residual R1) |
| `corpus/CANONICAL-002_jcs_discriminating.json` | `WORKING` | First JCS-discriminating candidate fixture is prepared for cross-language execution | execute on RI-PY + RI-RS and record observed bytes |
| `corpus/CANONICAL-003_jcs_full_discriminator.json` | `WORKING` | Multi-axis discriminator for ECMAScript number form, UTF-16 member ordering and string escaping; output bytes and digest are pinned independently | Execute on RI-PY + RI-RS, compare emitted bytes, then record evidence |
| `ck003/manifest.json` | `WORKING` | Useful working-corpus inventory, not a normative fixture by itself | promote referenced fixtures individually |
| `ck003/expected_digests.json` | `WORKING` | Explicitly preserves unresolved digest slots without false PASS claims | freeze remaining canonical-byte / registry / identity dependencies |

## Minimum Early Conformance Package

The minimum fixture set worth executing before the full APS-500 corpus is frozen is:

1. `FIX-INV-007` with `CONF-011`
2. `FIX-INV-013` with `CONF-013`
3. `CANONICAL-001`, `CANONICAL-002` and `CANONICAL-003` with `CONF-003`, with the DQ-002 hash-domain vectors as supporting serialization evidence

This package supports the first meaningful controlled conformance wave for:

- `INV-007`
- `INV-013`
- `INV-003`

## Authoring New Fixtures

1. Copy [`../templates/FIXTURE_TEMPLATE.json`](../templates/FIXTURE_TEMPLATE.json)
2. Assign the next sequential `FIX-NNN` identifier
3. Place in the appropriate category subdirectory
4. Link to related CONF-xxx test(s) and INV-xxx invariants
5. Submit via pull request with a reference to the related APS-500 section

Working corpus fixtures in `/fixtures/corpus/` MAY evolve during closure work; only fixtures promoted into the approved APS-500 corpus are normative.

## Important Rules

- Fixture IDs are NEVER reused
- A fixture whose Expected Output changes becomes a NEW fixture (new ID)
- Old fixtures are deprecated, not modified
- Fixtures MUST be used unmodified by implementations

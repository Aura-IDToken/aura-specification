# DQ-003 — Current Version Compatibility Matrix

**Classification:** WORKING / CONTROLLED CLOSURE ARTIFACT  
**Status:** READY FOR CONTROLLED EXECUTION  
**Review date:** 2026-09-26

## Purpose

This matrix is the current repository-local answer to APS-001 §12 and APS-200 §9: compatibility is explicit, version-bound, and MUST NOT be inferred from numeric ordering.

## Governing machine-readable form

- `ck003/decisions/DQ-003/CURRENT_VERSION_COMPATIBILITY_MATRIX.json`

## Current draft rule set

| Protocol version | Allowed entity / pack schema versions | Allowed input schema | Allowed evidence profile | Allowed fixture bindings |
|---|---|---|---|---|
| `1.0-DRAFT` | `EvaluationRequest=1.0-DRAFT`, `EvaluationResult=1.0-DRAFT`, `PolicyReference=1.0-DRAFT`, `Attestation=1.0-DRAFT`, `EvidencePack=1.0-DRAFT` | `AURA-DRAFT-CORE-001` | `EPR-CORE` | `FIX-001@0.2-DRAFT`, `FIX-COMPAT-001@0.1-DRAFT` |

## Negative rule

Any version combination outside the matrix MUST be rejected in strict conformance mode, including:

- unapproved `schema_version` for any bound entity or Evidence Pack component;
- unapproved `input_schema`;
- unapproved `evidence_profile`;
- a fixture version not explicitly listed for the target `protocol_version`.

## Current closure posture

DQ-003 is now closed far enough for repository-local controlled execution of `CONF-008` because:

1. the `protocol_version` / `schema_version` distinction is already stated in APS-001 §12 and APS-200 §4 / §9;
2. the explicit compatibility matrix now exists in both human-readable and machine-readable form;
3. `fixtures/compatibility/FIX-COMPAT-001_VERSION_MATRIX.json` binds the matrix to executable cases;
4. `scripts/run-draft-conformance.py` executes the draft compatibility gate.

Remaining work before release-grade closure:

- run the same matrix against RI-PY and RI-RS;
- promote the matrix from repository-local draft use to approved release evidence;
- extend the matrix when additional profiles, schemas, or normative fixture versions are introduced.

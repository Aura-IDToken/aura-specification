# CK-003 Core v3.3 — As-Is Evidence Baseline

**Classification:** EVIDENCE
**Status:** VERIFIED BASELINE
**Source artifact:** `aura-poc-a-core-v3.3-main (8).zip`
**Source SHA-256:** `15dc7938da2d723248351fb6daa364ea36912ee35d64fe50c47798cb53f516b3`
**Review date:** 2026-08-18

## 1. Scope

This document records only observations directly verified against the supplied Core v3.3 source archive. It does not promote implementation behaviour to normative protocol semantics.

## 2. Verified implementation facts

### 2.1 Mathematical evaluator

`core/evaluator.py` implements ARI measurement using integer/fixed-point arithmetic with `SCALING_FACTOR = 100000`, structural weight `30000`, and semantic weight `70000`. The evaluator explicitly validates vector dimension before computation and raises `ValueError` rather than relying on `assert`.

The evaluator therefore provides direct evidence for the existing fixed-point measurement path and the fail-closed dimension guard.

### 2.2 Merkle implementation currently present

`core/merkle.py` currently computes a leaf as:

`SHA-256(UTF-8(json.dumps(data, sort_keys=True)))`

and returns the hexadecimal digest. This is an implementation fact, not the selected CK-003 canonical hash-domain contract.

### 2.3 Certificate representation currently present

`compliance/certificate.py` documents the Layer 0 integer result as the normative measurement but stores `ari_score` and `drift` as Python `float` in the external certificate representation. `fingerprint()` serializes the certificate with `json.dumps(..., sort_keys=True)` and hashes the resulting UTF-8 bytes.

This is therefore a verified representation boundary and a CK-003 conformance gap, not evidence that the current certificate serialization is normative.

### 2.4 Test collection baseline

Running `python3 -m pytest -q` against the supplied archive fails during collection in `core/test_ari_observability.py` because `unittest` is referenced without being imported. The observed failure is:

`NameError: name 'unittest' is not defined`

This is an environment-independent test-collection defect and must be classified separately from protocol-logic failures.

## 3. Relation to current specification

Current `APS-001_PROTOCOL_SPECIFICATION.md` is version `0.2-DRAFT`, status `DRAFT — ARCHITECTURE REVIEW REQUIRED`, and explicitly states that the RI-RS hash-domain model is the current CK-003 architectural decision candidate. Its release gate also requires complete invariant coverage, stable fixtures, RI-PY/RI-RS agreement, CI execution, evidence completeness, and Architecture Review.

Current APS-001 source SHA-1: `51fde2452f90e3daacd8ddb7fd49c76dafef7f8f`.

## 4. Evidence classification

| Area | Verified state | CK-003 status |
|---|---|---|
| Fixed-point ARI measurement | Present | EVIDENCED |
| Dimension fail-closed guard | Present | EVIDENCED |
| Existing Merkle serialization | JSON/sorted-key UTF-8 | NON-NORMATIVE / MIGRATION REQUIRED |
| Existing certificate numeric representation | float at presentation boundary | OPEN CONFORMANCE GAP |
| Existing certificate fingerprint | sorted JSON UTF-8 | OPEN CONFORMANCE GAP |
| Full pytest collection | Blocked by missing `unittest` import | TEST BASELINE BLOCKED |

## 5. Architectural rule

No Core implementation behaviour recorded here changes the normative specification. The specification defines the canonical contract; Core v3.3 must subsequently conform to that contract.

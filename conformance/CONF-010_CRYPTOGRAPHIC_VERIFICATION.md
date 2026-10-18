# CONF-010 CRYPTOGRAPHIC VERIFICATION

Document ID: CONF-010
Version: 1.0-DRAFT
Status: DRAFT
Classification: Normative Conformance Test
Authority: APS-400
Related Invariant: INV-011
Last Review: 2026-09-26

---

## 1. Purpose

Verify that all cryptographic hashes in the Evidence Pack are independently computable and correct.

---

## 2. Related APS

- APS-100: INV-011
- APS-400 §4: CONF-010
- APS-300: Evidence requirements
- APS-500: Reference Fixtures

---

## 3. Preconditions

- The draft working fixture `fixtures/core/FIX-001_BASIC_EVALUATION.json` is available
- Python 3 is available with `jsonschema`
- The repository-local verifier `scripts/check-fix001-evidence.py` is available

---

## 4. Test Procedure

1. Load `FIX-001` and validate its Evidence Pack against the APS-300 draft schema.
2. Independently recompute:
   - `input_hash` from `ENT-002.request_fields`
   - `output_hash` from `{ decision, result_fields }`
   - `integrity_hash` for the enclosed request, result, policy, and attestation objects
   - `evidence_hash` for the Evidence object
   - `pack_hash` for the enclosing Evidence Pack
3. Compare each recomputed digest to the stored fixture value.
4. Confirm that `integrity_metadata` mirrors the enclosed object-level `integrity_hash` values exactly.

---

## 5. Expected Result

All independently computed digest values MUST match the stored fixture values exactly. Any mismatch is a FAIL.

---

## 6. Evidence Required

EVID-CORE

---

## 7. PASS / FAIL Criteria

| Outcome | Condition |
|---------|-----------|
| PASS | Expected result achieved with no deviations |
| FAIL | Any required field missing, any hash mismatch, or any deviation from expected result |
| NOT APPLICABLE | Implementation does not support this feature (requires justification) |
| ERROR | Test infrastructure failure — result not recorded |

---

## 8. Traceability

| Field | Value |
|-------|-------|
| Test ID | CONF-010 |
| Invariant | INV-011 |
| Related Fixture | `fixtures/core/FIX-001_BASIC_EVALUATION.json` |
| Evidence Type | EVID-CORE |

---

Current controlled draft execution path: `scripts/check-fix001-evidence.py`

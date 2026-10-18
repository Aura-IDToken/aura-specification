# CONF-004 EVIDENCE INTEGRITY

Document ID: CONF-004
Version: 1.0-DRAFT
Status: DRAFT
Classification: Normative Conformance Test
Authority: APS-400
Related Invariant: INV-004
Last Review: 2026-09-26

---

## 1. Purpose

Verify that any modification of an Evidence object is detectable.

---

## 2. Related APS

- APS-100: INV-004
- APS-400 §4: CONF-004
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
2. Recompute the published `input_hash`, `output_hash`, `evidence_hash`, and `pack_hash`.
3. Execute the repository-local negative control in `scripts/check-fix001-evidence.py`, which mutates one Evidence-object field without updating the stored digest values.
4. Confirm that the mutated object is rejected while the original object still passes.

---

## 5. Expected Result

Integrity check MUST fail for the mutated Evidence object. The original unmodified `FIX-001` Evidence Pack MUST pass the same verification run.

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
| Test ID | CONF-004 |
| Invariant | INV-004 |
| Related Fixture | `fixtures/core/FIX-001_BASIC_EVALUATION.json` |
| Evidence Type | EVID-CORE |

---

Current controlled draft execution path: `scripts/check-fix001-evidence.py`

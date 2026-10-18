# CONF-001 DETERMINISTIC EVALUATION

Document ID: CONF-001
Version: 1.0-DRAFT
Status: DRAFT
Classification: Normative Conformance Test
Authority: APS-400
Related Invariant: INV-001
Last Review: 2026-09-26

---

## 1. Purpose

Verify that identical inputs produce identical Evaluation Results.

---

## 2. Related APS

- APS-100: INV-001
- APS-400 §4: CONF-001
- APS-300: Evidence requirements
- APS-500: Reference Fixtures

---

## 3. Preconditions

- The draft working fixture `fixtures/core/FIX-001_BASIC_EVALUATION.json` is available
- Python 3 is available with `jsonschema`
- The repository-local verifier `scripts/check-fix001-evidence.py` is available

---

## 4. Test Procedure

1. Load `FIX-001` and validate the request, result, and Evidence Pack against the current draft schemas.
2. Execute the repository-local deterministic materialization path in `scripts/check-fix001-evidence.py` twice using the same `ENT-002.request_fields` and the same bound policy reference.
3. Compare the two generated `ENT-003` objects byte-for-byte.
4. Compare the two generated `EPR-CORE` Evidence Packs byte-for-byte.
5. Compare the generated artifacts to the published `FIX-001` expected result and expected evidence objects.

---

## 5. Expected Result

Both executions MUST produce byte-identical Evaluation Result objects and byte-identical Evidence Pack objects. `output_hash`, `evidence_hash`, and `pack_hash` values MUST be identical across both executions and match the published `FIX-001` draft fixture.

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
| Test ID | CONF-001 |
| Invariant | INV-001 |
| Related Fixture | `fixtures/core/FIX-001_BASIC_EVALUATION.json` |
| Evidence Type | EVID-CORE |

---

Current controlled draft execution path: `scripts/check-fix001-evidence.py`

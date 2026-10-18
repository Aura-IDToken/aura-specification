# CONF-005 TRACEABILITY

Document ID: CONF-005
Version: 1.0-DRAFT
Status: DRAFT
Classification: Normative Conformance Test
Authority: APS-400
Related Invariant: INV-005
Last Review: 2026-09-26

---

## 1. Purpose

Verify the complete traceability chain from APS requirement to Evidence.

---

## 2. Related APS

- APS-100: INV-005
- APS-400 §4: CONF-005
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
2. Verify that `evidence_object.execution_id`, `evaluation_result.execution_id`, and `attestation.attested_execution_id` resolve to the same execution.
3. Verify that `evidence_object.policy_reference` resolves to the enclosed Policy Reference object and that the Evaluation Result embeds the same Policy Reference.
4. Verify that `evidence_object.attestation_reference` resolves to the enclosed Attestation object and that `attestation.evidence_reference` resolves to the enclosing `pack_id`.
5. Verify that pack-level `requirement_references` include every requirement reference asserted by the enclosed Evidence object.

---

## 5. Expected Result

Every required reference field in the Evidence object and Evidence Pack MUST be present and resolve to the correct enclosed object or execution identity with no broken links.

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
| Test ID | CONF-005 |
| Invariant | INV-005 |
| Related Fixture | `fixtures/core/FIX-001_BASIC_EVALUATION.json` |
| Evidence Type | EVID-CORE |

---

Current controlled draft execution path: `scripts/check-fix001-evidence.py`

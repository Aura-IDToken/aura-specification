# CONF-002 REPLAY VERIFICATION

Document ID: CONF-002
Version: 1.0-DRAFT
Status: DRAFT
Classification: Normative Conformance Test
Authority: APS-400
Related Invariant: INV-002
Last Review: 2026-09-26

---

## 1. Purpose

Verify that an execution can be replayed from its Evidence Pack to produce an identical result.

---

## 2. Related APS

- APS-100: INV-002
- APS-400 §4: CONF-002
- APS-300: Evidence requirements
- APS-500: Reference Fixtures

---

## 3. Preconditions

- The draft working fixture `fixtures/core/FIX-001_BASIC_EVALUATION.json` is available
- Python 3 is available with `jsonschema`
- The repository-local verifier `scripts/check-fix001-evidence.py` is available
- `FIX-001` declares `_draft_replay_materialization` for the replay evidence-chain derivative

---

## 4. Test Procedure

1. Load `FIX-001` and validate the request, result, and original Evidence Pack against the current draft schemas.
2. Using the original `FIX-001` Evidence Pack and its bound replay metadata, execute the repository-local replay path in `scripts/check-fix001-evidence.py`.
3. Re-materialize the `ENT-003` result from the same bound request/policy inputs and verify byte-identical parity with the original Evidence Pack result.
4. Materialize a replay `EPR-CORE` Evidence Pack from the original Evidence Pack result and bound replay metadata, with `previous_evidence_hash` pointing to the original Evidence object hash.
5. Compare the replayed Evaluation Result to the original result byte-for-byte and verify the replay chain linkage.

---

## 5. Expected Result

Replayed Evaluation Result MUST be byte-identical to the original. `output_hash` MUST match, and the replay Evidence Pack MUST carry a valid `previous_evidence_hash` chain link to the original Evidence object.

---

## 6. Evidence Required

EVID-CORE, EVID-CHAIN

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
| Test ID | CONF-002 |
| Invariant | INV-002 |
| Related Fixture | `fixtures/core/FIX-001_BASIC_EVALUATION.json` |
| Evidence Type | EVID-CORE, EVID-CHAIN |

---

Current controlled draft execution path: `scripts/check-fix001-evidence.py`

# CONF-006 PLATFORM INDEPENDENCE

Document ID: CONF-006
Version: 1.0-DRAFT
Status: DRAFT
Classification: Normative Conformance Test
Authority: APS-400
Related Invariant: INV-006
Last Review: 2026-09-26

---

## 1. Purpose

Verify that results are identical on different hardware platforms.

---

## 2. Related APS

- APS-100: INV-006
- APS-400 §4: CONF-006
- APS-300: Evidence requirements
- APS-500: Reference Fixtures

---

## 3. Preconditions

- The draft working fixture `fixtures/core/FIX-001_BASIC_EVALUATION.json` is available
- Python 3 is available with `jsonschema`
- The repository-local verifier `scripts/check-fix001-evidence.py` is available
- `FIX-001` declares at least two `_draft_execution_contexts` representing distinct platform contexts

---

## 4. Test Procedure

1. Load `FIX-001` and validate the request, result, and Evidence Pack against the current draft schemas.
2. Read the fixture's `_draft_execution_contexts`, which model distinct artifact-level platform contexts (for example `linux-x86_64` and `linux-aarch64`) with different request-field insertion orders and environment labels.
3. Execute the repository-local deterministic materialization path in `scripts/check-fix001-evidence.py` once per context using the same semantic request payload and the same bound policy reference.
4. Compare the generated `ENT-003` objects byte-for-byte across contexts.
5. Compare the generated `EPR-CORE` Evidence Packs byte-for-byte across contexts.

---

## 5. Expected Result

`output_hash`, `evidence_hash`, and `pack_hash` MUST be identical across all declared draft execution contexts. The generated `ENT-003` and `EPR-CORE` artifacts MUST remain byte-identical even when platform labels and object-member insertion order differ.

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
| Test ID | CONF-006 |
| Invariant | INV-006 |
| Related Fixture | `fixtures/core/FIX-001_BASIC_EVALUATION.json` |
| Evidence Type | EVID-CORE |

---

Current controlled draft execution path: `scripts/check-fix001-evidence.py`

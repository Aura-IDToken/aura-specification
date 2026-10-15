# CONF-007 FAIL CLOSED

Document ID: CONF-007
Version: 1.0-DRAFT
Status: DRAFT
Classification: Normative Conformance Test
Authority: APS-400
Related Invariant: INV-008
Last Review: 2026-07-23

---

## 1. Purpose

Verify that the implementation halts safely on invalid input or policy failure.

---

## 2. Related APS

- APS-100: INV-008
- APS-400 §4: CONF-007
- APS-300: Evidence requirements
- APS-500: Reference Fixtures

---

## 3. Preconditions

- A conformant implementation is available and running
- Reference fixture FIX-001 (or applicable fixture) is loaded
- No prior state from a different test run exists

> **TODO**: Specify exact preconditions once APS-200 schemas and APS-500 fixtures are finalized.

---

## 4. Test Procedure

Submit an Evaluation Request with malformed input; submit a request referencing a missing policy.

---

## 5. Expected Result

Implementation MUST return a safe-state response. No partial Evidence MUST be persisted. Safe-state exit code or error response MUST be returned.

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
| Test ID | CONF-007 |
| Invariant | INV-008 |
| Related Fixture | FIX-001 (historical draft reference); supplemental non-normative execution vector: [FIX-ERROR v0.1](https://github.com/vaidt/aura-guard-v1.3/blob/017d771613d2c0d7fe652aa6108dbc88f2ffe219/tests/fixtures/FIX-ERROR.json). FIX-ERROR is not an APS-500 canonical fixture. |
| Evidence Type | EVID-CORE |

---

## 9. Supplemental Execution Record — NON-NORMATIVE

A bounded execution of `FIX-ERROR` v0.1 was recorded on `vaidt/aura-guard-v1.3`, merged commit `017d771613d2c0d7fe652aa6108dbc88f2ffe219`. The external HTTP/TCP run passed the four tested malformed-request / missing-policy cases with no change to the persisted JSONL bytes. Separate integrated tests passed the invalid-action loader and fail-fast startup probes.

Execution report: [CONF-007 / FIX-ERROR — Supplemental Execution Report](evidence/CONF-007_FIX-ERROR_EXECUTION_REPORT_2026-10-15.md).  
CI run: [38685728376](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38685728376).  
Preserved run artifact: [gate4-external-e2e-evidence](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38685728376/artifacts/11950640032).

**Observed result:** PASS for the cases listed in the report.  
**Overall CONF-007 disposition:** PARTIAL / OPEN; the full conformance test is not declared PASS.  
**Evidence classification:** NON-NORMATIVE. **Normative effect:** NONE. **Ratification:** NOT PERFORMED.

The replay result explicitly reported `verified_lineage=false`. Segment verification succeeded, but lineage verification was not demonstrated. The execution resides in `vaidt/aura-guard-v1.3`; authoritative reachability in the upstream `Aura-IDToken/*` source-of-record repositories has not been established by this report.

This supplemental record does not amend the normative expected result or PASS/FAIL criteria and must not be used as automatic ratification, release authorization, or production certification.

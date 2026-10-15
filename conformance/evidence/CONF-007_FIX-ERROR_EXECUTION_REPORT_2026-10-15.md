# CONF-007 / FIX-ERROR — Supplemental Execution Report

**Record date:** 2026-10-15  
**Record classification:** EVIDENCE — NON-NORMATIVE  
**Conformance item:** CONF-007 — Fail Closed / INV-008  
**Observed outcome:** PASS for the explicitly listed cases only  
**Overall CONF-007 status:** PARTIAL / OPEN — full conformance is not claimed  
**Normative effect:** NONE  
**Ratification:** NOT PERFORMED

## 1. Purpose and evidence boundary

This record summarizes the FIX-ERROR v0.1 tests executed against the `vaidt/aura-guard-v1.3` sandbox repository. The test implementation was merged into that repository's `main` branch at commit:

`017d771613d2c0d7fe652aa6108dbc88f2ffe219`

The test-bearing pull-request head was `f6fed43a6ab1d107d2fa5ebfc527de46aef3b95d`. CI run: [38685728376](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38685728376). The external E2E job preserved an artifact at [gate4-external-e2e-evidence](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38685728376/artifacts/11950640032).

This is supplemental, non-normative implementation evidence. It is not an APS-500 canonical fixture, it is not independent authority/source-of-record evidence for the upstream `Aura-IDToken/*` repositories, and it does not create a conformance certificate, protocol release, or automatic ratification. The normative CONF-007 definition remains DRAFT.

## 2. Fixture identity

| Field | Value |
|---|---|
| Fixture | `FIX-ERROR` |
| Fixture version | `0.1` |
| Fixture classification | `TEST VECTOR — NON-NORMATIVE` |
| Source | [tests/fixtures/FIX-ERROR.json](https://github.com/vaidt/aura-guard-v1.3/blob/017d771613d2c0d7fe652aa6108dbc88f2ffe219/tests/fixtures/FIX-ERROR.json) |
| SHA-256 of fixture bytes recorded by execution | `788a6469f2885a9b6eac6bee9053cdb22ed1af452fc5903f73a0532b97dfd9c4` |

The fixture defines four HTTP rejection cases and one invalid-policy startup case.

## 3. External HTTP/TCP execution

The Gate 4 script started the real Aura-Guard listener and sent the negative requests through the external HTTP/TCP boundary. Its positive control traversed the configured, pinned Python AURA Core adapter before the failure probes.

| Case | Fault injected | Observed result | Audit file after request | Result |
|---|---|---|---|---|
| FIX-ERROR-001 | Malformed JSON | HTTP 400; no decision response | Unchanged | PASS |
| FIX-ERROR-002 | Required `payload.response` missing | HTTP 422; no decision response | Unchanged | PASS |
| FIX-ERROR-003 | Empty measurement vector | HTTP 400; no decision response | Unchanged | PASS |
| FIX-ERROR-004 | Unregistered `policy_set` | HTTP 400; no decision response | Unchanged | PASS |

For every negative request, the JSONL record count remained `1 → 1`, and the SHA-256 of the persisted file remained unchanged. The one existing record was the successful positive-control request, not a partial record for a rejected request.

### Raw execution values

- Valid positive control: `core_measurement.status=COMPLETED`, ARI `100000`, drift `0`.
- Persisted positive-control JSONL entries after all four negative requests: `1`.
- Persisted JSONL SHA-256 after all four rejections: `219bc2e7dc1f14580a791ae316df328168e7ad13dab69546c90a5aaf74dd89c1`.
- External execution: `CONF-007 FIX-ERROR E2E: PASS`.
- Independent replay: `status=ok`, `entries=1`, `core_measurements=1`, `segments=1`, `verified_segments=true`.

**Lineage limitation:** replay reported `verified_lineage=false`. This run does not establish verification of evidence lineage, nor may segment verification be interpreted as lineage verification.

## 4. Invalid policy / startup tests

The integrated Rust test suite executed two further relevant checks:

| Case | Test path | Observed result |
|---|---|---|
| FIX-ERROR-005 | `load_policy` given a policy declaring `grant-everything` | Explicit invalid-action error; no compiled policy returned — PASS |
| FIX-ERROR-005 | Real `aura-guard` binary bootstrap with invalid policy | Startup terminated with `EX_CONFIG` (exit code `78`); test asserted the audit log contains no records — PASS |

Defense in depth was also tested at the decision engine boundary: an unknown action that bypasses policy loading maps to `DENY`, not `ALLOW` (`engine::tests::unknown_action_fails_closed_as_deny`).

These results close the previously observed unknown-action-to-implicit-ALLOW behavior for the tested code paths. They do not establish coverage of every possible runtime, I/O, policy-signature, storage, or process failure.

## 5. CI disposition

The GitHub Actions run for the PR head completed successfully. Relevant checks include:

- `build + test`: SUCCESS
- `rustfmt`: SUCCESS
- `clippy`: SUCCESS
- `cargo-deny`: SUCCESS
- `cargo-audit`: SUCCESS
- `Semgrep scan`: SUCCESS
- Gate 3 real Core API/hash/replay integration: SUCCESS
- Gate 4 external-client black-box E2E including FIX-ERROR HTTP probes: SUCCESS
- RI-RS conformance and other repository workflows: SUCCESS

The test log recorded both new integration tests as passed and the invalid-policy startup test as passed.

## 6. Disposition and remaining limits

**Result:** PASS for FIX-ERROR-001 through FIX-ERROR-005 as executed on the identified sandbox commit.

**Overall CONF-007:** PARTIAL / OPEN. Do not promote the conformance-test definition from DRAFT based on this record. Do not treat the green CI result as automatic ratification.

Remaining limitations include:

1. The fixture and run reside in `vaidt/aura-guard-v1.3`, not a proven authoritative execution path in the upstream `Aura-IDToken/*` repositories.
2. `verified_lineage=false`; lineage verification was not demonstrated.
3. The cases are a bounded set, not an exhaustive fault-injection campaign.
4. No separate protocol ratification, release authorization, or production certification was performed.

No change to the normative protocol contract is proposed by this execution report.

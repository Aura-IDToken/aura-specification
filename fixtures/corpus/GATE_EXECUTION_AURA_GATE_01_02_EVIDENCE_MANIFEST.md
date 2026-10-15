# AURA Gate Execution Evidence Manifest — GATE-01 / GATE-02

**Status:** EXECUTION RECORD — NON-NORMATIVE  
**Repository:** `vaidt/aura-specification`  
**Execution branch:** `execution/b-val-014-conf003-dq006-2026-09-26`  
**Scope:** GATE-01 governance reconciliation; GATE-02 B-VAL-014 / BNC-1 readiness

> This artifact records execution evidence only. It does not create protocol authority, authorize B-VAL-014 by itself, alter constitutional constants, or establish protocol conformance. M1 closure-state reconciliation is recorded separately in `AURA_GOVERNANCE_CONFLICT_RESOLUTION_M1_v1.0.md`.

## GATE-01 — Governance namespace reconciliation

### Observed sources

1. `AURA_M1_CLOSURE_RECORD_v1.0.md`
   - Status: `RATIFIED`
   - Ratification_Status: `EXECUTED`
   - Declares `M1_Governance_Gate: CLOSED`
   - Declares `Authority_Continuity: PROVEN`

2. `AURA_NORMATIVE_CONTRACT_CONFLICT_REGISTER_v1.3.md`
   - Status: `PROPOSED DECISION REQUEST — NOT APPROVED — NOT EFFECTIVE`
   - Records M1 owner authority as `NOT_PROVEN`
   - Records authority continuity as `NOT_PROVEN`
   - Records normative contract closure as `NOT_PROVEN`
   - Explicitly states that the register does not close M1 or establish authority.

### Reconciliation result

**GATE-01A = RESOLVED — M1 CLOSURE STATE**

A formal resolution record has been added on this execution branch: `AURA_GOVERNANCE_CONFLICT_RESOLUTION_M1_v1.0.md`. It applies the existing governance rules without changing them. The M1 closure record is marked `RATIFIED / EXECUTED`; the conflict register is explicitly `NOT APPROVED / NOT EFFECTIVE` and disclaims authority to close M1. Therefore the narrow M1 closure-state question resolves to the repository-recorded state `M1 = CLOSED`.

**GATE-01B = BLOCKED — AG-001 PROTOCOL AUTHORITY**

The broader authority-model question remains unresolved. The governance-resolution matrix treats AG-001 as requiring a new explicit decision and prohibits selection by recency, completeness, implementation state, or test state. The M1 closure-state reconciliation does not resolve that broader question.

## GATE-02 — B-VAL-014 / BNC-1

### Repository-local evidence search

Search target: `B-VAL-014` in `vaidt/aura-specification`.

Result: **NO MATCH**.

Direct fetch attempts for:
- `conformance/B-VAL-014-DEFINITION-RECONCILIATION-RECORD.md`
- `conformance/BC-02-CUSTODIAN-CLOSURE-RECORD.md`

Result: **NOT FOUND (404)**.

### Cross-repository evidence

A B-VAL-014 definition reconciliation record exists in the related `Aura-IDToken/aura-specification` corpus, but that record is not repository-local evidence for `vaidt/aura-specification`. It therefore cannot be promoted here to a PASS condition without an explicit authoritative cross-repository binding.

The related record itself states:
- B-VAL-014: `NOT EXECUTED`
- execution: `NOT AUTHORIZED BY THIS RECORD`
- PRE-01 schema binding: unmet
- PRE-02 BNC-1: not executed
- PRE-03 registry binding: unresolved
- no receiver invocation, fixture consumption, receipt regeneration, or implementation change occurred under that record.

### Execution result

**GATE-02 = BLOCKED HARD GATE**

No B-VAL-014 PASS or BNC-1 PASS is claimed.

### Next admissible evidence

Before execution can be closed:
1. establish the authoritative repository/corpus boundary for B-VAL-014;
2. bind the BC-02 §14 vocabulary to the actual receipt fields (PRE-01);
3. execute BNC-1 under the controlling authorization;
4. execute B-VAL-014 under explicit authorization;
5. preserve the generated receipt/digest evidence and gate outputs;
6. keep B-VAL-011, B-VAL-012, B-VAL-013 and B-VAL-019 as separate gates.

## Custodian disposition

`M1_CLOSURE_STATE = CLOSED`

`AG-001_PROTOCOL_AUTHORITY = BLOCKED`

`GATE-02 = BLOCKED HARD GATE`

`CUSTODIAN_GATE = BLOCKED`

No sealing, release, conformance declaration, or constitutional change is performed by this artifact.

## aura-guard-v1.3 — Gate 1b execution evidence

- **Commit SHA:** `1165547204b38cd705e91eaa286d5ad9ff6555cd`
- **Evidence environment:** GitHub Actions (CI — build, tests and Gate 1b)
- **Technical result:** 500/500 successful HTTP requests; 500 JSONL entries; 10 Merkle segments
- **aura-replay verification:** `status=ok`; `verified_lineage=true`; `verified_segments=true`
- **Tag:** `TECHNICAL_EVIDENCE_ONLY / EXECUTION_UNAUTHORIZED`


## aura-poc-a-core-v3.3 — Core Gate 2 technical execution evidence

- **Repository:** `vaidt/aura-poc-a-core-v3.3`
- **Execution branch:** `validation/core-full-suite-128-docker-2026-10-14`
- **Source revision:** `efc3a26e6e2fb4ec3238336ffb5452092c9a555d`
- **Evidence environment:** GitHub Actions; native x86_64 and ARM64 runners; Python 3.12.15
- **CI run:** [38629005599](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38629005599)
- **Full test suite:** 162 collected; 162 passed; 8 warnings; 17 subtests passed
- **Architecture jobs:** x86_64 PASS; aarch64 PASS; ARI/drift comparison PASS
- **Compared observations:** OBS-1 through OBS-5; 5/5 actual ARI/drift output pairs equal
- **Common evaluator source SHA-256:** `0e57b68cb5d1f6418542446b41c9d50a2fab1fc61bf8b54e511bd94ffe394eff`
- **Comparison artifact:** [core-003-cross-architecture-comparison](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38629005599/artifacts/11924877790)
- **Full-suite artifact:** [core-full-suite-docker-evidence](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38629005599/artifacts/11925411485)
- **Technical result:** CORE Gate 2 criteria 2.1–2.4 passed on the execution branch
- **Integration status at record time:** validation branch only; source revision not merged into `main`
- **Tag:** `TECHNICAL_EVIDENCE_ONLY / EXECUTION_UNAUTHORIZED`

This entry records observed test execution and architecture-comparison results only. It does not authorize implementation, ratify arithmetic semantics, establish protocol conformance, close the specification repository's separate GATE-02 (B-VAL-014 / BNC-1), or claim that the source branch was integrated.

The source repository's governing `CONSTITUTIONAL_DECREE.md` and `.github/copilot-tasks.md` were reviewed before integration. The requested source merge was not performed because the proposed core changes affect the frozen measurement instrument while the repository's task allowlist does not include CORE-001–CORE-004, and the project record does not establish the constitutive authority needed to override that gate. The CI evidence is retained as technical-only evidence pending the appropriate authority decision.


## aura-poc-a-core-v3.3 — post-merge main validation (2026-10-14)

- **Pull request:** [#2 — CORE: integrate Gate 2 fixes and native x86_64/ARM64 evidence](https://github.com/vaidt/aura-poc-a-core-v3.3/pull/2)
- **Merge commit:** [cdf9bbf2b8420732f85a77197ea753809edbb029](https://github.com/vaidt/aura-poc-a-core-v3.3/commit/cdf9bbf2b8420732f85a77197ea753809edbb029)
- **Post-merge source revision:** `cdf9bbf2b8420732f85a77197ea753809edbb029` on `main`
- **Docker-backed full-suite CI:** [run 38637889001](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38637889001) — PASS
- **Full test result:** 162 tests passed; 8 warnings; 17 subtests passed. The workflow's explicit gate observed 162 collected / 162 passed.
- **Native architecture evidence:** x86_64 PASS; aarch64 PASS; comparison PASS; five observations (OBS-1–OBS-5) produced equal ARI/drift pairs.
- **Evaluator source SHA-256 recorded by the comparison job:** `82183bc556a75d644c6b9940adf1970df29a0baa0c25cca522b0f97c3d840cc7`
- **Comparison artifact:** [core-003-cross-architecture-comparison](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38637889001/artifacts/11928044223)
- **Full-suite artifact:** [core-full-suite-docker-evidence](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38637889001/artifacts/11928946793)
- **Architecture records:** [x86_64](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38637889001/artifacts/11928463163); [aarch64](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38637889001/artifacts/11929291463)
- **Mandatory execution checks on the merged commit:** [run 38637888845](https://github.com/vaidt/aura-poc-a-core-v3.3/actions/runs/38637888845) — PASS for x86_64, ARM64, WASM compatibility, and cross-platform determinism comparison.
- **Technical status:** merged into `main`; post-merge CI PASS
- **Tag:** `TECHNICAL_EVIDENCE_ONLY / NORMATIVE_EFFECT_NONE`

This entry records post-merge execution facts for the stated main commit. It does not ratify the selected signed-division semantics, establish protocol conformance, authorize deployment, or close the specification repository's separate GATE-02 / B-VAL-014 / BNC-1. The earlier entry's “not merged into main” wording describes the state at that earlier evidence-recording point and is retained as historical context; this entry records the later integration and validation result.


## aura-guard-v1.3 — Gate 3 post-merge technical validation (2026-10-14)

- **Pull request:** [#6 — Gate 3: bind AURA Core measurements into audit chain](https://github.com/vaidt/aura-guard-v1.3/pull/6)
- **Merge commit:** [ff14f58c6b984653763e9c2e5dea0ba3e51d3826](https://github.com/vaidt/aura-guard-v1.3/commit/ff14f58c6b984653763e9c2e5dea0ba3e51d3826)
- **Post-merge CI:** [run 38643480694](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38643480694) — PASS; all nine jobs completed successfully, including build + test, real Core API/hash/replay integration, D-3 evidence export, concurrent HTTP stress + replay, rustfmt, clippy, cargo-audit, cargo-deny, and CycloneDX SBOM generation.
- **Post-merge Docker Image CI:** [run 38643480715](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38643480715) — PASS.
- **Post-merge Rust build:** [run 38643480803](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38643480803) — PASS.
- **Post-merge coverage:** [run 38643480655](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38643480655) — PASS.
- **Post-merge Semgrep:** [run 38643480659](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38643480659) — PASS.
- **Exact revision verified:** each listed post-merge run reports head SHA `ff14f58c6b984653763e9c2e5dea0ba3e51d3826`.
- **Core dependency used by CI:** `vaidt/aura-poc-a-core-v3.3@cdf9bbf2b8420732f85a77197ea753809edbb029`.
- **Observed integrity result:** the real-Core integration test mutates persisted `core_measurement.ari` from `100000` to `99999` while retaining the original `chain_hash`; `aura-replay` exits with code `2` and reports `CHAIN BREAK DETECTED at entry #1`.
- **Technical disposition:** Gate 3 implementation and specified post-merge CI checks — PASS for the stated commit.
- **Tag:** `TECHNICAL_EVIDENCE_ONLY / NORMATIVE_EFFECT_NONE`.

This entry records observed technical execution for the stated merge commit only. It does not ratify any protocol contract, prove authority continuity, grant implementation or deployment authorization, establish full protocol conformance, declare production readiness, or claim completion of Gate 4's external-client black-box end-to-end scenario. The existing Gate 3 integration test drives the API router in-process; Gate 4 must separately exercise the listening HTTP service from an external client and verify the persisted log and Merkle segment through the independent `aura-replay` CLI.


## aura-guard-v1.3 — Gate 4 external-client E2E candidate evidence (2026-10-14)

- **Implementation PR:** [#7 — Gate 4: external-client black-box end-to-end validation](https://github.com/vaidt/aura-guard-v1.3/pull/7).
- **Candidate source branch:** `gate4/external-client-e2e-2026-10-15`.
- **Exact candidate revision tested:** `7e6581a2d480308fbd230636e66544f32220f7a8`.
- **Integration status at recording time:** candidate PR branch; not merged to `main`. These results must not be interpreted as post-merge main validation.
- **Gate 4 CI run:** [run 38645708854](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38645708854) — PASS for the exact candidate revision; all ten jobs completed successfully, including build + test, the Gate 3 real-Core regression, Gate 4 external-client E2E, concurrency stress + replay, D-3 evidence export, rustfmt, clippy, cargo-audit, cargo-deny, and CycloneDX SBOM generation.
- **Additional candidate checks:** [Docker Image CI run 38645708851](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38645708851) — PASS; [Rust run 38645708890](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38645708890) — PASS; [coverage run 38645708874](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38645708874) — PASS; [Semgrep run 38645708807](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38645708807) — PASS; [CK-003 DQ-002 Hash Domain run 38645708812](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38645708812) — PASS.
- **Pinned Core revision:** `vaidt/aura-poc-a-core-v3.3@cdf9bbf2b8420732f85a77197ea753809edbb029`.
- **External HTTP result:** actual listening `aura-guard` TCP service; external client POSTed to `/v1/audit`; HTTP 200; `decision=ALLOW`; `core_measurement.status=COMPLETED`; `ari=100000`; `drift=0`.
- **Persistence result:** one `aura-guard.audit.v2` JSONL record; HTTP response matched the persisted record; prompt/response text was not present in the persisted entry.
- **Independent replay result:** [CI evidence artifact](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38645708854/artifacts/11932496569) contains the request, HTTP response, JSONL log, Merkle manifest, replay summary, and runtime logs. The replay summary reports `status=ok`, `entries=1`, `core_measurements=1`, `segments=1`, `verified_segments=true`. The scenario does not claim policy-lineage verification (`verified_lineage=false`).
- **Technical disposition:** Gate 4 black-box fixture — PASS on the specified candidate branch and revision.
- **Tag:** `TECHNICAL_EVIDENCE_ONLY / NORMATIVE_EFFECT_NONE`.

This entry records an observed run on a proposed source revision only. It does not establish that Gate 4 is merged into `main`, authorize deployment, establish full security or protocol conformance, prove authority continuity, ratify a normative contract, or declare AURA production-ready. A subsequent post-merge run on the actual merge commit is required before claiming Gate 4 validation on `main`.


## aura-guard-v1.3 — Gate 4 external-client E2E post-merge validation (2026-10-14)

- **Implementation PR:** [#7 — Gate 4: external-client black-box end-to-end validation](https://github.com/vaidt/aura-guard-v1.3/pull/7) — merged.
- **Merge commit on `main`:** [`386e6c7c4df3a8d29299d9966736705fe6d59e54`](https://github.com/vaidt/aura-guard-v1.3/commit/386e6c7c4df3a8d29299d9966736705fe6d59e54).
- **PR source revision:** `7e6581a2d480308fbd230636e66544f32220f7a8`; post-merge evidence below is specifically bound to the separate merge commit stated above.
- **Post-merge main CI:** [run 38646914930](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38646914930) — PASS. All ten jobs completed successfully: build + test; Gate 3 real Core API/hash/replay integration; Gate 4 external-client black-box E2E; D-3 chain evidence export; concurrent HTTP stress + replay (GUARD-RS-001); rustfmt; clippy; cargo-audit; cargo-deny; and CycloneDX SBOM generation.
- **Post-merge Docker Image CI:** [run 38646914781](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38646914781) — PASS.
- **Post-merge Rust:** [run 38646914611](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38646914611) — PASS.
- **Post-merge coverage:** [run 38646914724](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38646914724) — PASS.
- **Post-merge Semgrep:** [run 38646914839](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38646914839) — PASS.
- **Exact-revision binding:** all five post-merge workflow runs above report head SHA `386e6c7c4df3a8d29299d9966736705fe6d59e54`.
- **Pinned Core source:** `vaidt/aura-poc-a-core-v3.3@cdf9bbf2b8420732f85a77197ea753809edbb029`.
- **External-client result:** real `aura-guard` TCP listener; external `POST /v1/audit`; HTTP 200; Rust policy decision `ALLOW`; `core_measurement.status=COMPLETED`; `ari=100000`; `drift=0`.
- **Persistence/privacy result:** one `aura-guard.audit.v2` JSONL entry; HTTP response exactly matches the persisted entry; original prompt/response text are absent from the persisted record.
- **Independent Gate 4 replay:** [post-merge evidence artifact](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38646914930/artifacts/11932323392) contains request, response, JSONL log, Merkle manifest, replay summary, and runtime logs. Replay summary: `status=ok`; `entries=1`; `core_measurements=1`; `segments=1`; `verified_segments=true`; `verified_lineage=false`. The verifier accepted the sole Merkle segment manifest. The absence of policy-lineage verification is explicitly retained as a limitation of this Gate 4 scenario.
- **Concurrent-write/replay evidence:** within the same successful CI, GUARD-RS-001 reports 500/500 HTTP requests succeeded, 500 JSONL entries, and `aura-replay status=ok` across 10 Merkle segments with `verified_segments=true` and `verified_lineage=true`.
- **Technical disposition:** Gate 4 external-client E2E and the specified post-merge technical checks — PASS for the stated `main` merge commit.
- **Tag:** `TECHNICAL_EVIDENCE_ONLY / NORMATIVE_EFFECT_NONE`.

This record binds observed technical execution to the stated merge commit only. It does not prove exhaustive security, general production readiness, full protocol conformance, authority continuity, governance closure, normative ratification, or implementation/deployment authorization. It does not change any governance or normative status. The Gate 4 fixture verifies one representative external-client scenario; it is not a substitute for broader failure-mode, operational-readiness, load-boundary, or governance gates.


## aura-guard-v1.3 — Gate 4.1 Hardening Suite — Stage 1 (2026-10-15)

- **Implementation PR:** [#8 — Gate 4.1 Core failure and JSONL privacy probes](https://github.com/vaidt/aura-guard-v1.3/pull/8) — merged to `main`.
- **Exact tested PR-head revision:** [`6667413d34a46ea0dfdb9f5c80cc425ddc30aab5`](https://github.com/vaidt/aura-guard-v1.3/commit/6667413d34a46ea0dfdb9f5c80cc425ddc30aab5).
- **Merge commit on `main`:** [`08aa63db0e4fae09289cdbb442c34caabe8e6d5b`](https://github.com/vaidt/aura-guard-v1.3/commit/08aa63db0e4fae09289cdbb442c34caabe8e6d5b).
- **Pre-merge CI:** [run 38660515574](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38660515574) — PASS for the tested PR-head revision; `build + test`, Gate 3 real-Core integration, Gate 4 external-client E2E, D-3 chain evidence export, concurrent stress/replay, rustfmt, clippy, cargo-audit, cargo-deny, and SBOM jobs completed successfully.
- **Pre-merge Docker Image CI:** [run 38660515511](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38660515511) — PASS for the tested PR-head revision.
- **Pre-merge coverage / Gate 4.1 test:** [run 38660516833](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38660516833) — PASS. The log explicitly reports `gate41_core_failures_are_passive_and_raw_jsonl_excludes_prompt_response ... ok`; result: 1 passed, 0 failed.
- **Post-merge main coverage:** [run 38661076111](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38661076111) — PASS on exact merge SHA `08aa63db0e4fae09289cdbb442c34caabe8e6d5b`. The Gate 4.1 test passed again on `main` (1 passed, 0 failed); all coverage workflow tests completed successfully.
- **Post-merge Rust workflow:** [run 38661076085](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38661076085) — PASS on the merge SHA.
- **Post-merge Semgrep:** [run 38661076039](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38661076039) — PASS on the merge SHA.
- **Post-merge general CI:** [run 38661076127](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38661076127) — IN PROGRESS at the time this entry was recorded; individual jobs already successful included Gate 3, Gate 4 E2E, D-3 evidence export, rustfmt, clippy, cargo-audit, and cargo-deny. The `build + test` release build was still running.
- **Post-merge Docker Image CI:** [run 38661075975](https://github.com/vaidt/aura-guard-v1.3/actions/runs/38661075975) — IN PROGRESS at the time this entry was recorded. No post-merge Docker PASS is claimed here.
- **Test scope and observed result:** deterministic local Core-adapter process timeout using the existing 2-second timeout; process spawn failure; malformed JSON; missing required field; wrong field type; preservation of a policy `DENY` on Core timeout; serviceability of `/health` during the pending measurement; raw-byte JSONL scan for `G41_SECRET_PROMPT_7F31` and `G41_SECRET_RESPONSE_9A62`; absence of persisted `"prompt"`/`"response"` fields; deserialization of all 9 entries and successful chain verification.
- **Timeout scope limitation:** the suite exercises the existing 2-second adapter timeout. It does not verify an injected 200 ms threshold; that remains outside this Stage 1 change.
- **Production delta:** test-only addition at `tests/gate41_core_failure.rs`; no production source or policy file was modified by PR #8.
- **Technical disposition:** Gate 4.1 Hardening Suite, Stage 1 — the implemented Core failure and JSONL privacy scenarios PASS on the PR head and again on the merged `main` revision, as evidenced by the coverage runs stated above.
- **Classification:** `TECHNICAL_EVIDENCE_ONLY / NORMATIVE_EFFECT_NONE`.

This append-only entry records only the observed scope and exact revisions/runs named above. It does not establish exhaustive security, general production readiness, complete External Integration Hardening, full protocol conformance, authority continuity, governance closure, normative ratification, or implementation/deployment authorization. Governance M1 remains BLOCKED. The post-merge general CI and Docker workflows were still in progress when this record was written; this entry does not recast them as successful.

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

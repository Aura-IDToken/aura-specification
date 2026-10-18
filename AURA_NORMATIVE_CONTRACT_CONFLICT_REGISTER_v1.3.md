# AURA_NORMATIVE_CONTRACT_CONFLICT_REGISTER_v1.3

## 1. Metadata

- **Artifact:** `AURA_NORMATIVE_CONTRACT_CONFLICT_REGISTER_v1.3.md`
- **Document class:** Evidence-linked proposed decision register
- **Status:** PROPOSED DECISION REQUEST — NOT APPROVED — NOT EFFECTIVE
- **Prepared from repository state:** branch `copilot/prepare-v1-3-decision-register` @ commit `71133de047c71e0bc1156d58c20396fe593ace70`
- **Primary repository assessed:** `vaidt/aura-specification`
- **Related repositories assessed where traceable evidence was available:** `vaidt/Aura-Guard`, `vaidt/Aura-vNEXT`
- **Requested baseline:** `AURA_NORMATIVE_CONTRACT_CONFLICT_REGISTER_v1.2.md`
- **Baseline availability result:** **NOT_LOCATED** in the assessed working tree, current git history name scan, or GitHub code search over the visible `vaidt` repositories at assessment time
- **Assessment rule:** existence of a document, branch, fixture, test, implementation, commit, or execution result is not by itself proof of approval, ratification, authority, competence, conformance, M1 closure, or TCK authorization
- **Final control statement:** This register is an evidence-linked proposed decision register. It does **not** create normative authority, establish governance competence, ratify a protocol contract, close M1, authorize TCK implementation, authorize repository merging, or authorize code migration.

> Navigation: for the current repository-level routing of governance/status artifacts, see [`GOVERNANCE_STATUS_INDEX.md`](GOVERNANCE_STATUS_INDEX.md).

### Enumerations used in this register

| Field | Values used here |
|---|---|
| `role_status` | `ROLE_DEFINED`, `ROLE_REFERENCED_ONLY`, `CONFLICTING_SOURCES`, `NOT_DEFINED` |
| `holder_verification_status` | `VERIFIED`, `NOT_VERIFIED`, `INCONCLUSIVE`, `NOT_APPLICABLE` |
| `competence_status` | `PROVEN`, `PARTIALLY_SUPPORTED`, `NOT_PROVEN`, `CONFLICTING_SOURCES`, `UNDERSPECIFIED`, `INCONCLUSIVE` |
| `decision_status` | `PROPOSED`, `OPEN`, `PARTIAL`, `BLOCKED`, `CONFLICTING_SOURCES`, `NOT_PROVEN` |
| `closure_status` | `CLOSED`, `OPEN`, `BLOCKED`, `PARTIAL`, `NOT_CLOSABLE_FROM_REPO_EVIDENCE` |
| `normative_effectiveness` | `EFFECTIVE`, `NOT_EFFECTIVE`, `NOT_PROVEN` |

## 2. Control statuses

| Control | Status | Evidence / note |
|---|---|---|
| 1. Implementation behavior MUST NOT silently become protocol law | SATISFIED_IN_REGISTER | APS-001 states RI behavior does not redefine protocol; this register does not elevate implementation behavior (`E-003`, `E-012`, `E-030`) |
| 2. Existence is not proof of approval/ratification/conformance | SATISFIED_IN_REGISTER | GOV-001 and the Constitution separate authoring from approval; this register treats all such claims as evidence-dependent only (`E-001`, `E-002`) |
| 3. Role definition vs holder identity preserved | SATISFIED_IN_REGISTER | Explicit split retained in §§3, 5, 6, 7 |
| 4. As-Is vs To-Be separation preserved | SATISFIED_IN_REGISTER | Draft/spec text, proposed closure text, and missing approval evidence are kept distinct throughout (`E-003`–`E-027`) |
| 5. Contradictions not silently resolved | SATISFIED_IN_REGISTER | Conflicts remain recorded as `CONFLICTING_SOURCES`, `UNDERSPECIFIED`, or `NOT_PROVEN` |
| 6. Frozen constitutional artifacts not modified | SATISFIED_IN_REGISTER | Constitution only cited as evidence (`E-002`) |
| 7. No approval/freeze/ratification by this artifact | SATISFIED_IN_REGISTER | Document status remains `PROPOSED DECISION REQUEST — NOT APPROVED — NOT EFFECTIVE` |
| 8. No TCK implementation, repo merge, code migration, or protocol behavior change | SATISFIED_IN_REGISTER | No such act is performed or authorized |
| 9. Chief Architect identity not inferred from ownership/authorship | SATISFIED_IN_REGISTER | Holder identity remains `NOT_VERIFIED` |
| 10. Material claims require evidence or explicit uncertainty | SATISFIED_IN_REGISTER | Every material row cites evidence or states `NOT_PROVEN` / `INCONCLUSIVE` |

## 3. Competence and closure statuses

### 3.1 Role / holder / authority model

| Subject | role_defined | holder_identity_verified | authority_continuity_proven | decision_competence_proven | ratification_evidence_present | normative_effective | Evidence |
|---|---|---|---|---|---|---|---|
| Chief Architect | ROLE_DEFINED | NOT_VERIFIED | NOT_PROVEN | PARTIALLY_SUPPORTED | NOT_PROVEN | NOT_PROVEN | Constitution and GOV-001 define the role and reserve approvals/status transitions, but no repository artifact verifies the current holder or continuity (`E-001`, `E-002`, `E-020`) |
| Architecture Review Board | ROLE_DEFINED | NOT_APPLICABLE | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | GOV-001 names the ARB, but no roster, charter artifact, or ARR record was verified in the assessed tree (`E-001`) |
| Protocol Custodian | ROLE_REFERENCED_ONLY | NOT_VERIFIED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | The role is referenced in handover/conflict material and SPEC-002 ownership, but GOV-001 does not establish it in the authority hierarchy (`E-021`, `E-022`, `E-027`) |
| M1 owner | NOT_DEFINED | NOT_VERIFIED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | Milestone 1 tasks are listed in `aura-specification`, and an Aura-Guard M1-named branch exists, but no owner-authentication or closure artifact was verified and branch existence is not competence evidence (`E-020`, `E-031`) |

### 3.2 Overall closure / authorization status

| Question | Result | Why |
|---|---|---|
| M1 owner authority established? | **NOT_PROVEN** | Milestone 1 is a checklist in the roadmap, not an authority record; Aura-Guard exposes an M1-named branch but no authority or closure proof; Aura-vNEXT explicitly says M1 is not yet defined (`E-020`, `E-031`, `E-032`) |
| Authority continuity proven? | **NOT_PROVEN** | Role descriptions exist, but no holder continuity record was verified (`E-001`, `E-002`) |
| Formal ratification mechanism exists? | **PARTIALLY_SUPPORTED** | Governance process exists in draft text, but no executed ratification artifact for the disputed decisions was verified (`E-001`, `E-020`) |
| P-008 ratification competence proven? | **NOT_PROVEN** | Related-repo Phase 3 materials label P-008 as owner-decision-required, non-binding analysis only (`E-029`, `E-030`) |
| Normative contract closure proven? | **NOT_PROVEN** | APS corpus remains draft/open in key areas; conflicting closure records remain (`E-003`–`E-018`, `E-021`–`E-026`) |
| TCK implementation authorized? | **NOT_PROVEN / NOT AUTHORIZED** | No repository-local TCK artifact, approval, scope document, or authorization record was verified; Aura-vNEXT has M0 conformance gates and vectors, but its own report says no M1 TCK is defined, which does not transfer authority to `aura-specification` (`E-017`, `E-020`, `E-028`, `E-033`, `E-034`) |

## 4. Governing principles

1. **Specification first; implementation follows specification.** (`E-002`, `E-003`)
2. **A higher-authority approved artifact prevails only where approval/effectiveness is proven.** Draft/proposed text is not auto-effective. (`E-001`, `E-002`, `E-026`)
3. **Traceability gaps and draft status block conformance claims.** (`E-016`, `E-018`, `E-025`)
4. **Cross-language agreement is not identical to normative closure or RFC-8785 conformance.** (`E-012`, `E-024`)
5. **Repository evidence presently supports proposed rules, partial closures, and open blockers more often than approved/effective normative decisions.** (`E-021`, `E-022`, `E-023`, `E-025`)

## 5. ND decisions

| decision_id | topic | category | required_role | role_status | current_holder | holder_verification_status | competence_status | decision_status | closure_status | normative_effectiveness | evidence_references | unresolved_questions | blocking_conditions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ND-001 | Canonical serialization profile and canonical bytes | ND | Chief Architect | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | PARTIALLY_SUPPORTED | PARTIAL | PARTIAL | NOT_EFFECTIVE | `E-003`, `E-004`, `E-012`, `E-024`, `E-026` | Is the APS-200 §8 draft text approved/effective, and has RFC-8785-discriminating cross-language evidence been executed? | Draft status of APS documents; missing holder verification; DQ-006 ratification and discriminating evidence not complete |
| ND-002 | Merkle/hash domain contract | ND | Chief Architect | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | CONFLICTING_SOURCES | CONFLICTING_SOURCES | NOT_CLOSABLE_FROM_REPO_EVIDENCE | NOT_EFFECTIVE | `E-013`, `E-014`, `E-015`, `E-021`, `E-025` | Does DQ-002 stand as CLOSED/PASS or OPEN/proposed? Which record is competent and ratified? | DQ-002 closure record conflicts with the still-proposed ADR/evidence state; no ratification evidence verified |
| ND-003 | Event-type semantics and vocabulary closure | ND | Chief Architect | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | PARTIALLY_SUPPORTED | BLOCKED | BLOCKED | NOT_EFFECTIVE | `E-010`, `E-011`, `E-016`, `E-019`, `E-023` | Which event tokens are approved, and under what payload contracts? | Registry contains no approved tokens; DQ-004 explicitly remains open/blocking |
| ND-004 | Numeric domain and float boundary | ND | Chief Architect | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | UNDERSPECIFIED | OPEN | OPEN | NOT_EFFECTIVE | `E-003`, `E-024`, `E-027`, `E-029`, `E-030` | Exact numeric representation, fixed-point/integer domain, non-finite handling, and cross-language fixture set | APS-200 does not yet define the exact numeric representation; related-repo analysis remains non-binding |
| ND-005 | Version binding and compatibility semantics | ND | Chief Architect | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | PARTIALLY_SUPPORTED | OPEN | OPEN | NOT_EFFECTIVE | `E-003`, `E-018`, `E-019`, `E-020`, `E-025` | What is the explicit compatibility matrix and version-binding fixture set? | DQ-003 remains open; compatibility matrix and execution evidence not verified |
| ND-006 | Evidence Pack contract | ND | Chief Architect | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | UNDERSPECIFIED | OPEN | OPEN | NOT_EFFECTIVE | `E-005`, `E-007`, `E-027` | Exact Evidence Pack container, schema, hash coverage, and null/absence semantics | APS-300 §6 remains TODO; APS-500 says canonical fixture data depends on unresolved APS-200/300 finalization |

## 6. AD decisions

| decision_id | topic | category | required_role | role_status | current_holder | holder_verification_status | competence_status | decision_status | closure_status | normative_effectiveness | evidence_references | unresolved_questions | blocking_conditions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AD-001 | Conformance-only canonicalizer boundary vs production dependency graph | AD | Chief Architect / implementation maintainer | CONFLICTING_SOURCES | NOT_VERIFIED | NOT_VERIFIED | PARTIALLY_SUPPORTED | PARTIAL | OPEN | NOT_EFFECTIVE | `E-012`, `E-021`, `E-028` | Which RI-RS conformance boundary is the boundary of record? | DQ-006 residual R3 remains open; competing RI-RS paths are recorded in the conflict register |
| AD-002 | Independent oracle as evidence method | AD | Chief Architect / reviewer | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | PARTIALLY_SUPPORTED | PARTIAL | OPEN | NOT_EFFECTIVE | `E-012`, `E-015`, `E-024` | Is the oracle method merely evidentiary, or itself part of an approved conformance contract? | Oracle artifacts exist, but no approved repository-wide oracle contract was verified |
| AD-003 | Single authoritative DQ-006 closure record | AD | Chief Architect | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | PARTIALLY_SUPPORTED | PARTIAL | OPEN | NOT_EFFECTIVE | `E-012`, `E-021`, `E-026` | Is the supersession claim itself ratified and universally adopted? | Status transitions are reserved to the Chief Architect; superseded artifacts remain present |
| AD-004 | Executable conformance runner / CI gate as the automation boundary | AD | Chief Architect / repository maintainer | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | NOT_PROVEN | OPEN | OPEN | NOT_EFFECTIVE | `E-017`, `E-020`, `E-025`, `E-028` | What exact runner, CI gate, and evidence path define protocol-level conformance automation? | Repository-native CI is absent; RI references record the conformance runner as missing |

## 7. GD prerequisites

| decision_id | topic | category | required_role | role_status | current_holder | holder_verification_status | competence_status | decision_status | closure_status | normative_effectiveness | evidence_references | unresolved_questions | blocking_conditions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GD-001 | Chief Architect role exists and is the approval authority | GD | Constitution / GOV-001 | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | PARTIALLY_SUPPORTED | PARTIAL | OPEN | NOT_PROVEN | `E-001`, `E-002` | Who currently holds the role, and since when? | No holder-identity artifact verified |
| GD-002 | Protocol Custodian role and competence | GD | Governance corpus | CONFLICTING_SOURCES | NOT_VERIFIED | NOT_VERIFIED | NOT_PROVEN | OPEN | OPEN | NOT_PROVEN | `E-021`, `E-022`, `E-027` | Is Protocol Custodian a formally governed role in this repository corpus? | Role is referenced but not coherently established in GOV-001/Constitution |
| GD-003 | Architecture Review Board existence and operative competence | GD | GOV-001 | ROLE_DEFINED | NOT_APPLICABLE | NOT_APPLICABLE | NOT_PROVEN | OPEN | OPEN | NOT_PROVEN | `E-001` | Does the ARB have roster, continuity, and recorded review acts? | No ARR record or ARB-instance evidence was verified |
| GD-004 | Ratification mechanism for disputed ND/AD closures | GD | GOV-001 lifecycle | ROLE_DEFINED | NOT_VERIFIED | NOT_VERIFIED | PARTIALLY_SUPPORTED | OPEN | OPEN | NOT_PROVEN | `E-001`, `E-012`, `E-014` | What artifact proves ratification for DQ-002/DQ-006 and related closures? | Process text exists, but executed ratification evidence was not verified |
| GD-005 | M1 ownership and closure competence | GD | Repository milestone process | NOT_PROVEN | NOT_VERIFIED | NOT_VERIFIED | NOT_PROVEN | OPEN | OPEN | NOT_PROVEN | `E-020`, `E-031`, `E-032` | Who owns M1 and what artifact closes it? | `aura-specification` roadmap contains checklist items only; Aura-Guard has an M1-named branch; Aura-vNEXT says M1 is not yet defined; no owner/closure artifact verified |
| GD-006 | TCK scope and implementation authorization | GD | Governance / conformance corpus | NOT_DEFINED | NOT_VERIFIED | NOT_VERIFIED | NOT_PROVEN | NOT_PROVEN | NOT_CLOSABLE_FROM_REPO_EVIDENCE | NOT_PROVEN | `E-017`, `E-020`, `E-028`, `E-033`, `E-034` | Is TCK a defined artifact, runner, certification layer, or future program? | No TCK artifact or authorization record was verified in the assessed corpus; Aura-vNEXT M0 gates are repository-specific and explicitly stop short of defining an M1 TCK |

## 8. Conflict inventory

| conflict_id | topic | current classification | repository evidence | assessment |
|---|---|---|---|---|
| C-001 | Canonicalization and canonical bytes | `PARTIALLY_SUPPORTED` | APS-200 §8 and APS-300 §5 now bind JCS/UTF-8/canonical bytes, but DQ-006 remains OPEN because the evidence does not discriminate RFC 8785 from sorted JSON and ratification is missing (`E-004`, `E-005`, `E-012`, `E-024`) | A proposed/implemented contract is present; final normative closure is not proven |
| C-002 | Numeric domain and float boundary | `UNDERSPECIFIED` | APS-001 bars float use where it breaks determinism; SPEC-002 says exact numeric representation still requires an explicit decision; related-repo Phase 3 material keeps P-002 non-binding (`E-003`, `E-027`, `E-029`, `E-030`) | The rule surface exists, but the exact numeric contract is not closed |
| C-003 | Unicode handling | `UNDERSPECIFIED` | JCS/UTF-8 is stated; cross-language discriminating Unicode vectors remain candidate-only; SPEC-002 still lists source encoding/Unicode normalization as future decisions (`E-004`, `E-012`, `E-024`, `E-027`) | Unicode byte/ordering behavior is proposed in part, but not fully evidenced across the corpus |
| C-004 | Key ordering | `PARTIALLY_SUPPORTED` | APS-200 via JCS implies ordering; CONF-003 and independent verification say UTF-16-discriminating fixtures are still required (`E-004`, `E-012`, `E-024`) | Proposed ordering rule exists, but executed proof against alternative sort behaviors is incomplete |
| C-005 | Optionality and null | `UNDERSPECIFIED` | SPEC-002 requires a future decision on absent/optional fields; protocol-level APS documents do not yet define a repository-wide null/absence rule, while boundary artifacts do for a narrower contract (`E-027`, `E-005`) | Narrow artifacts exist; protocol-wide normative closure does not |
| C-006 | Timestamp semantics | `UNDERSPECIFIED` | APS-200 and APS-300 require ISO 8601 UTC timestamps, but no precise normalization/precision/ordering rule or approval artifact was verified; related-repo Phase 3 marks timestamp semantics as discovered/deferred (`E-004`, `E-005`, `E-029`, `E-030`) | Field presence is specified; exact semantics remain open |
| C-007 | `canonical.bin` status | `NOT_PROVEN` | No `canonical.bin` artifact or governing specification path was verified in the assessed tree | The repository evidence does not prove existence, status, or normative role for `canonical.bin` |
| C-008 | Hash domain | `CONFLICTING_SOURCES` | `closures/DQ-002_FINAL_CLOSURE.md` declares CLOSED/PASS/frozen, while the DQ-002 ADR and evidence matrix still record the decision as proposed/open/pending approval (`E-013`, `E-014`, `E-015`) | The contradiction is real and unresolved from repository evidence alone |
| C-009 | Oracle contract | `PARTIALLY_SUPPORTED` | Independent oracle records exist for DQ-002 and DQ-006, but they establish corroboration/evidence method, not an approved normative oracle contract (`E-015`, `E-012`, `E-024`) | Oracle use is evidenced; oracle authority is not |
| C-010 | Evidence Pack contract | `UNDERSPECIFIED` | APS-300 §6 still contains a TODO for container format; APS-500 defers canonical fixture data until APS-200/300 finalization (`E-005`, `E-007`) | The contract surface is incomplete and cannot be treated as normatively closed |
| C-011 | TCK scope | `NOT_PROVEN` | No TCK artifact was verified in `aura-specification`; current corpus records missing conformance runner and missing CI gate, while Aura-vNEXT exposes M0 gates but explicitly says no M1 TCK is defined (`E-017`, `E-020`, `E-028`, `E-033`, `E-034`) | TCK scope/authorization cannot be inferred from runner, tests, implementation evidence, or another repository's M0-only gate set |
| C-012 | Authority, ratification, M1 closure, and TCK authorization | `NOT_PROVEN` | Governance roles are only partly defined; holders/continuity are unverified; Milestone 1 remains an open checklist; no TCK authorization record was found (`E-001`, `E-002`, `E-020`) | Repository evidence does not prove competence to close M1 or authorize TCK work |

## 9. Decision closure criteria

A decision in this register is eligible for `CLOSED` only when **all** of the following are evidenced in-repository or by explicitly linked approved artifacts:

1. the governing role is defined by an authoritative artifact;
2. the current holder identity is verified, or the competent collective body is evidenced;
3. authority continuity is proven;
4. the decision text is identifiable by document ID, version, status, and scope;
5. required review / approval / ratification acts are evidenced;
6. conflicting sibling records are superseded by a competent, evidenced act;
7. every material technical claim is supported by discriminating evidence, not merely implementation agreement;
8. draft/proposed text is not treated as effective merely because it exists;
9. conformance automation and fixture evidence, where required, are present and reachable from the referenced repository state;
10. closure does not depend on inference from repository ownership, commit authorship, branch existence, or passing tests alone.

## 10. Final disposition

### Concise audit summary

- **Files inspected:** governance, constitution, APS-001/200/300/400/500/900/950, event-type registry, DQ-002/DQ-004/DQ-006 records, completion matrices, roadmap, traceability, invariant registry, handover conflict/evidence-gap material, and limited traceable related-repository Phase 3 documents (`E-001`–`E-034`).
- **Baseline / branch:** assessment performed on `copilot/prepare-v1-3-decision-register` @ `71133de047c71e0bc1156d58c20396fe593ace70`.
- **Evidence added relative to the requested v1.2 baseline:** repository-state evidence index, explicit competence fields, explicit `NOT_PROVEN` handling for holder identity / continuity / ratification / M1 / TCK, and updated conflict classifications tied to current APS/DQ records.
- **Evidence gaps remaining:** current holder identity, authority continuity, ARB instantiation, DQ-002 competence path, DQ-006 ratification, discriminating cross-language JCS evidence, approved event vocabulary, exact numeric contract, exact Evidence Pack contract, M1 owner authority, and any TCK authorization artifact.
- **Status changes evidenced here:** DQ-006 is treated as `OPEN` per the current closure record; DQ-002 remains `CONFLICTING_SOURCES`; DQ-004 remains `BLOCKED`; M1 remains `OPEN`; TCK authorization remains `NOT_PROVEN`.
- **M1 status:** **OPEN / NOT PROVEN CLOSED**.
- **TCK authorization status:** **NOT PROVEN / NOT AUTHORIZED FROM REPOSITORY EVIDENCE**.
- **Mutation statement:** this artifact records evidence and blockers only; it performs no governance act.

### Disposition

`AURA_NORMATIVE_CONTRACT_CONFLICT_REGISTER_v1.3.md` should be treated as an **evidence-linked proposed decision register only**.

- No ND row in this register is evidenced as `EFFECTIVE`.
- No AD row in this register is evidenced as fully closed and ratified.
- GD blockers remain material and unresolved.
- Repository evidence does **not** prove M1 closure.
- Repository evidence does **not** prove authority continuity.
- Repository evidence does **not** prove P-008 ratification competence.
- Repository evidence does **not** authorize TCK implementation.

## 11. Evidence and traceability index

| Ref | Artifact | Type / status observed | Traceability locator |
|---|---|---|---|
| E-001 | GOV-001 / `GOVERNANCE.md` | `1.0-DRAFT` governance process | `GOVERNANCE.md` |
| E-002 | AURA Constitution | `1.0` / `FROZEN` | `constitution/AURA_CONSTITUTION.md` |
| E-003 | APS-001 | `0.2-DRAFT` / root normative specification draft | `specification/APS-001_PROTOCOL_SPECIFICATION.md` |
| E-004 | APS-200 | `1.0-DRAFT` / canonical data model | `aps/APS-200_CANONICAL_DATA_MODEL.md` |
| E-005 | APS-300 | `1.0-DRAFT` / evidence model | `aps/APS-300_EVIDENCE_MODEL.md` |
| E-006 | APS-400 | `1.0-DRAFT` / conformance matrix | `aps/APS-400_CONFORMANCE_TEST_MATRIX.md` |
| E-007 | APS-500 | `1.0-DRAFT` / fixtures | `aps/APS-500_REFERENCE_FIXTURES.md` |
| E-008 | APS-900 | `1.0-DRAFT` / compliance mapping | `aps/APS-900_COMPLIANCE_MAPPING.md` |
| E-009 | APS-950 | `1.0-DRAFT` / RI requirements | `aps/APS-950_REFERENCE_IMPLEMENTATION_REQUIREMENTS.md` |
| E-010 | Event-Type Registry | `DRAFT — DQ-004 closure artifact` | `aps/EVENT_TYPE_REGISTRY.md` |
| E-011 | DQ-004 event-type semantics | `PROPOSED CLOSURE` with verdict `BLOCKED FOR FINAL CLOSURE` | `ck003/DQ-004_EVENT_TYPE_SEMANTICS.md` |
| E-012 | DQ-006 closure package | current local DQ-006 closure record; the file self-describes as the single authoritative DQ-006 record, but this register treats that claim as evidence to assess rather than authority automatically conferred | `closures/DQ-006_CLOSURE_PACKAGE.md` |
| E-013 | DQ-002 final closure | local closure record says `CLOSED — PASS` | `closures/DQ-002_FINAL_CLOSURE.md` |
| E-014 | DQ-002 ADR | `PROPOSED — awaiting Chief Architect approval` | `ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` |
| E-015 | DQ-002 evidence matrix | says `DQ-002: OPEN` | `ck003/dq-002-hash-domain/HASH_DOMAIN_EVIDENCE.md` |
| E-016 | Current-state matrix | completion-state evidence | `docs/completion/01_CURRENT_STATE_MATRIX.md` |
| E-017 | Master completion plan | execution-draft baseline and conformance-runner/CI requirements | `docs/completion/00_MASTER_COMPLETION_PLAN.md` |
| E-018 | Traceability matrix | draft matrix with broad `NOT VERIFIED` / `PARTIAL` state | `compliance/TRACEABILITY_MATRIX.md` |
| E-019 | Invariant registry | draft registry with closure notes | `invariants/INVARIANT_REGISTRY.md` |
| E-020 | Roadmap | Milestone 1 open checklist | `ROADMAP.md` |
| E-021 | CK-003 handover conflict register | non-normative conflict evidence | `ck003/handover-assessment/04_CONFLICT_REGISTER.md` |
| E-022 | CK-003 decisions assessment | non-normative decisions status audit | `ck003/handover-assessment/03_DECISIONS.md` |
| E-023 | CK-003 evidence gaps | non-normative gap register | `ck003/handover-assessment/05_EVIDENCE_GAPS.md` |
| E-024 | CK-003 independent verification | recomputation and JCS-degeneracy evidence | `ck003/handover-assessment/10_INDEPENDENT_VERIFICATION.md` |
| E-025 | Architecture execution audit | release-readiness / blocker assessment | `ck003/audit/2026-08-20_ARCHITECTURE_EXECUTION_AUDIT.md` |
| E-026 | Changelog | records DQ-006 reconciliation from closed to open | `CHANGELOG.md` |
| E-027 | SPEC-002 Constitution Artifact Contract | draft future-decision surface for encoding/numeric/optionality | `specification/SPEC-002_CONSTITUTION_ARTIFACT_CONTRACT.md` |
| E-028 | RI reference summaries | both RI references record missing conformance runner | `reference/RI-PY_AURA_POC_A_CORE.md`, `reference/RI-RS_AURA_GUARD.md` |
| E-029 | Aura-Guard Phase 3 protocol decision matrix | non-binding analysis; P-007/P-008 remain owner decision required | `github://vaidt/Aura-Guard/docs/PHASE_3_PROTOCOL_DECISION_MATRIX.md@7d2f5746ae61a66edcd11d75bff0787bed854363` |
| E-030 | Aura-Guard Phase 3 architecture pack | non-binding analysis; `protocol_version` remains `unspecified` | `github://vaidt/Aura-Guard/docs/PHASE_3_ARCHITECTURE_PACK.md@7d2f5746ae61a66edcd11d75bff0787bed854363` |
| E-031 | Aura-Guard branch inventory | related-repository branch evidence only; includes `copilot/aura-m1-primary-authority-recovery` on `main` SHA `7d2f5746ae61a66edcd11d75bff0787bed854363` | `github://vaidt/Aura-Guard@7d2f5746ae61a66edcd11d75bff0787bed854363` |
| E-032 | Aura-vNEXT M1/open-questions summary | related-repository evidence says `M1 Status: NOT YET DEFINED` and OQ-1/OQ-5/OQ-8/OQ-9 remain open | `github://vaidt/Aura-vNEXT@bdec831c165b3a5465bc25f325ed801558cbf81a` |
| E-033 | Aura-vNEXT TCK / conformance gate summary | related-repository evidence lists M0-only gates (`make structure/register/fixtures/test/independence/product/check`) | `github://vaidt/Aura-vNEXT@bdec831c165b3a5465bc25f325ed801558cbf81a` |
| E-034 | Aura-vNEXT governance / ADR summary | related-repository evidence lists ADR-0001..0006 as accepted within Aura-vNEXT M0 scope; not treated here as authority for `aura-specification` | `github://vaidt/Aura-vNEXT@bdec831c165b3a5465bc25f325ed801558cbf81a` |

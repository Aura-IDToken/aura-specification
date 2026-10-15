# AURA Protocol → Implementation Binding Matrix v1.0

**Artifact ID:** AURA-PIBM-001  
**Version:** 1.0-draft  
**Status:** DRAFT · NON-CONSTITUTIVE · NOT A RATIFICATION INSTRUMENT  
**Classification:** Traceability / evidence-control artifact  
**Proposed repository of record:** `vaidt/aura-specification`  
**Prepared:** 2026-10-11  
**Normative effect:** NONE  
**Protocol-version assignment:** NONE  
**Implementation authorization created by this artifact:** NO

---

## 1. Purpose

This matrix binds protocol requirements and invariants to a versioned profile, fixture, exact runner entrypoint, execution result, provenance evidence, and authorization supporting a claim about an implementation.

It prevents the conflation of:

1. **Protocol requirement** — a requirement whose normative status must be established by the current authoritative governance record.
2. **Profile contract** — a versioned, deliberately bounded product or test-campaign contract.
3. **Implementation behavior** — behavior observed in a specific source snapshot and execution environment.
4. **Fixture** — an input/expected-result artifact exercising a defined portion of behavior.
5. **Execution result** — a result tied to exact inputs, code, toolchain, runner, and environment.
6. **Provenance evidence** — immutable references and digests permitting audit or reproduction.
7. **Authorization** — a separately established act permitting a particular normative or implementation action.

A populated row does not, by itself, establish that a requirement is normative or that an implementation is conformant.

## 2. Status and interpretation rules

### 2.1 Evidence vocabulary

- **NORMATIVE-BOUND** — the applicable governance/authority chain establishes the exact clause, scope, and effective normative force for the claim being made.
- **REPORTED-NORMATIVE-BOUND** — the current record of reference expressly describes a decision as normatively bound, but this matrix does not independently adjudicate any separate ratification/effect condition. This is a qualified report of source status, not an independent finding of constitutive effectiveness.
- **DRAFT-SOURCE** — source exists but is labelled draft/proposed, or normative effect is not established for the exact clause.
- **PROFILE-BOUND** — versioned product/test profile is explicit; this does not elevate it to protocol-wide norm.
- **SOURCE-OBSERVED** — source behavior inspected at a pinned commit; no execution claim implied.
- **EXECUTED-OBSERVED** — execution bound to exact source, runner, inputs, environment, and outputs.
- **HISTORICAL-OBSERVATION** — prior observed behavior whose original corpus/runner/context may not be fully recoverable.
- **PARTIAL-COVERAGE** — test covers a documented subset, not the whole requirement/profile.
- **UNBOUND** — one or more required linkage fields are missing.
- **BLOCKED** — required precondition, gate, or authorization is unsatisfied.
- **NOT-RUN** — no execution result exists for the binding claimed.
- **CONFLICT** — controlled sources disagree; no silent precedence inference is permitted by this matrix.
- **NOT-APPLICABLE** — permitted only with recorded rationale and scope; never a synonym for missing evidence.

These labels classify evidence in this matrix. They do not replace or amend protocol result algebra (including P-008) or the APS test-result taxonomy.

### 2.2 Binding rule

A conformance claim requires an explicit path:

`Requirement → Invariant → Profile → Fixture → Runner → Source Snapshot → Execution → Result → Evidence → Authorization / Release Decision`

Each edge must have a resolvable reference or be marked UNBOUND/BLOCKED. Never infer a missing edge from similar names, matching digests, a passing isolated test, or the existence of a file.

### 2.3 Non-equivalences

**EXISTS ≠ REACHABLE ≠ CURRENT ≠ AUTHORITATIVE ≠ NORMATIVE ≠ EFFECTIVE.**

Also: **EXHAUSTED ≠ RESOLVED.** Complete reconstruction does not resolve an authority or protocol decision gap.

### 2.4 Scope of one test

A passing narrow test demonstrates only behaviors covered by its assertions, inputs, and runner path. It must not be presented as proof of:
- the entire canonicalization domain based on a degenerate fixture;
- cross-language or cross-architecture determinism without the corresponding independent runs;
- protocol-wide conformance based on a profile-local verifier;
- historical reproduction when original corpus, runner, or runtime is not bound;
- authority, ratification, or release authorization.

### 2.5 Authorization is an independent binding

A code commit or green CI check does not grant normative effect. A governance record does not prove execution. Authorization is scoped to its recorded repositories, branches, paths, baseline commit, and acceptance criteria; it must not be extended to another repository or workstream by analogy.

## 3. Required row schema

Every **complete requirement-to-implementation binding record** MUST use the following fields. Unknown values must be UNBOUND, NOT-RUN, BLOCKED, or another defined status—not guessed. The summary table in §5 is an initial gap inventory, not a set of complete schema-conformant binding records. Its rows are summaries only; they do not satisfy this schema and must not be represented as fully bound records or as proof of conformance.

| Field | Meaning / minimum acceptable value |
|---|---|
| `binding_id` | Stable identifier for this exact mapping |
| `requirement_id` | APS clause / protocol requirement identifier |
| `source_artifact` | Exact repository path + immutable commit SHA + relevant section/line |
| `source_status` | Current record-of-reference, draft, historical, diagnostic, or conflict status |
| `normative_effect` | Proven / not proven / none / conflict, with authority reference |
| `invariant_id` | Invariant ID, or explicit not assigned |
| `profile_id` | Exact profile name and version/digest; protocol version separately recorded |
| `profile_scope` | Included and excluded behavior/domain |
| `implementation_id` | Product/repository and implementation version |
| `source_commit` | Full immutable source commit SHA actually examined/executed |
| `runner_entrypoint` | Exact path, command, arguments, and runner commit/blob SHA |
| `runtime_binding` | OS/architecture, runtime/container digest, dependencies/toolchain lock |
| `fixture_id` | Exact fixture identifier, version, immutable path/ref |
| `fixture_digest` | Digest algorithm and digest of exact fixture bytes |
| `expected_oracle` | Expected behavior/result and its authoritative basis |
| `execution_id` | Unique execution identifier; UNBOUND until recorded |
| `execution_result` | Test-level result using the declared result vocabulary |
| `coverage_limit` | Specific domains/branches not exercised |
| `evidence_refs` | Logs, reports, outputs, attestation, artifact digests and immutable locations |
| `provenance` | Source acquisition, generating tool/version, process, timestamps, derivation record |
| `authorization_ref` | Exact constitutive authorization and scope, or NOT-GRANTED |
| `release_binding` | Release/manifest and approved commit digest, or UNBOUND |
| `matrix_disposition` | BOUND / PARTIAL-COVERAGE / UNBOUND / BLOCKED / CONFLICT |
| `review_record` | Independent reviewer, decision, date, immutable review reference |

**No silent nulls:** every missing value needs a reason and the next required evidence. Digests MUST identify algorithm and byte domain. A digest over parsed/re-serialized JSON is not interchangeable with a digest over raw file bytes.

### 3.1 Complete binding-record template

The following is a template, not a populated record. Replace each placeholder only with source-bound evidence; otherwise retain an explicit unresolved status. A summary row in §5 does not become complete merely because this template is documented.

```yaml
binding_record:
  binding_id: "<stable-id>"
  requirement_id: UNBOUND
  source_artifact: UNBOUND
  source_status: UNBOUND
  normative_effect: UNBOUND
  invariant_id: UNBOUND
  profile_id: UNBOUND
  profile_scope: UNBOUND
  implementation_id: UNBOUND
  source_commit: UNBOUND
  runner_entrypoint: UNBOUND
  runtime_binding: UNBOUND
  fixture_id: UNBOUND
  fixture_digest: UNBOUND
  expected_oracle: UNBOUND
  execution_id: NOT-RUN
  execution_result: NOT-RUN
  coverage_limit: UNBOUND
  evidence_refs: UNBOUND
  provenance: UNBOUND
  authorization_ref: NOT-GRANTED
  release_binding: UNBOUND
  matrix_disposition: UNBOUND
  review_record: UNASSIGNED
```

## 4. Repository and profile boundary register

This register captures known roles and unresolved boundaries from the review baseline. It is not a repository-wide authority declaration.

| ID | Repository / source | Observed role | Binding disposition | Boundary |
|---|---|---|---|---|
| RB-001 | `vaidt/aura-specification` | Protocol/specification and governance records. The current DQ-006 record states that the RFC 8785 JCS decision is settled and normatively bound to APS-200 §8 / APS-300 §5; APS-200/300/400 document headers retain DRAFT labels | **REPORTED-NORMATIVE-BOUND** for the specific JCS decision as reported by DQ-006; no broader clause status is inferred and this matrix does not independently adjudicate any ratification/effect condition | Keep decision status, any applicable ratification/effect condition, and implementation/conformance-gate status separate. DQ-006 remains OPEN |
| RB-002 | `vaidt/Aura-vNEXT` | Product M0 implementation with its own restricted `AURA-CANON/1` profile | PROFILE-BOUND | Product contract is not automatically equivalent to a legacy or protocol-wide canonicalization contract |
| RB-003 | `vaidt/Aura-Guard` | Node ESM + Python verifier demonstrator; implementation-scoped JCS-lite behavior; protocol version observed as `unspecified` | SOURCE-OBSERVED / PARTIAL-COVERAGE | Not interchangeable with Rust `aura-guard-v1.3`; full RFC 8785 equivalence is not established by name or one fixture |
| RB-004 | `vaidt/aura-guard-v1.3` | Rust middleware, chain logic and canonical-001 conformance test | EXECUTED-OBSERVED only for exact recorded CI attempt | Current-main and tested source commit differ in the recorded review; fixture does not discriminate full JCS behavior |
| RB-005 | `vaidt/Aura-Conformance-Kit` | Fixture/helper and structural test-kit work | DRAFT-SOURCE / PARTIAL-COVERAGE | Not established as a complete independent protocol TCK |
| RB-006 | `vaidt/Aura-Release-Management` | Intended release-manifest / provenance source; the specific manifest candidate cited in BM-006 was not source-verified during this audit | UNBOUND / SOURCE VERIFICATION REQUIRED for BM-006 until the primary manifest is immutably located and bound | `AURA-RM-CANON/1`, if established in the primary source, is metadata-specific and must not be substituted for the protocol payload profile |
| RB-007 | `vaidt/Authority` | Constitutional change/authority records | SOURCE-OBSERVED | Repository existence alone does not establish an operative governance engine |
| RB-008 | `vaidt/Crystal-panel-Aura-Protection` | System map / forensic traceability | NON-CONSTITUTIVE | Navigation and diagrams are not normative acts |
| RB-009 | `vaidt/aura-l2-1-b-runtime-lab` | Private L2.1-B runtime/corpus scaffolding | BLOCKED / NOT-RUN | Runtime, runner and original corpus bindings are not established; repository presence does not authorize execution |

## 5. Initial binding summaries — current evidence disposition

The following table is a **summary-only evidence/gap inventory**, not a set of complete binding records under §3. Every BM row remains incomplete unless and until a corresponding record implements every field in the §3.1 schema and binds the referenced evidence immutably. The statuses below must be read only within their stated limitations; no summary row is a complete conformance claim.

| Binding ID | Requirement / invariant | Profile / fixture | Runner + source snapshot | Execution / result | Provenance + authorization | Disposition |
|---|---|---|---|---|---|---|
| BM-001 | **Decision status reported by DQ-006:** RFC 8785 JCS → UTF-8 `canonical_bytes`; `SHA-256(canonical_bytes)`; RFC 6962 leaf `SHA-256(0x00 concatenated with canonical_bytes)` and node `SHA-256(0x01 concatenated with left digest bytes and right digest bytes)`. DQ-006 §1 states the decision is settled and normatively bound to APS-200 §8 / APS-300 §5; this summary does not independently adjudicate any separate ratification/effect condition. CONF-003 / INV-003 are listed in APS-400, whose document header is DRAFT | `CANONICAL-001` at `aura-guard-v1.3/conformance/canonical/CANONICAL-001.json`; fixture is **not JCS-discriminating** | Rust test `conformance/canonical/canonical_001.rs`; tested commit `06a1d804e553f5c421c3ddaa133b6893bc2334e8`; CI run `35688714581`, job `114317737913`, attempt 5 | Five canonical tests passed in that job. Overall workflow was FAILURE due to other jobs (rustfmt/clippy/audit/deny). The run does **not** establish full RFC 8785 conformance; it establishes only that the recorded test path passed on its pinned source | CI evidence: https://github.com/vaidt/aura-guard-v1.3/actions/runs/35688714581. Current main was recorded as `c96377ac678151e5fef5756dbc31a3fff94de186`, two commits beyond the tested SHA. DQ-006 Closure Package at `vaidt/aura-specification@5ba3567b79c7ac7ff37e0508219c12dab349ca2d`, path `closures/DQ-006_CLOSURE_PACKAGE.md`, Git blob SHA `b72b8b10a49def105e822a917d7e277bd8cc094c`, §§1–3, is the source for the reported decision status; it reports the overall gate OPEN | REPORTED-NORMATIVE-BOUND (status reported by DQ-006; not independently adjudicated here) / PARTIAL-COVERAGE (implementation evidence) |
| BM-002 | Cross-implementation agreement / INV-XIM-01 (implementation-level; not automatically protocol-normative) | Existing Node↔Python verifier cases; complete profile and corpus digest not bound in this row | Node CLI invokes `py_verifier/aura_verify.py` from the verifier runtime root; exact source and command bundle must be pinned per execution | Historical report recorded Node 61/61, Python 39/39, CLI 10/10 PASS for a prior campaign; not asserted for current HEAD | Secondary report until raw logs, commits, runner command, dependency/runtime and fixture digests are attached | HISTORICAL-OBSERVATION / UNBOUND |
| BM-003 | Historical source-corpus reproduction; L2.1-B target (exact normative clause still needs binding) | Reconstructed 17-vector corpus SHA-256 `453a1302823340c3673e7fd3bd4760c07e4af172ba9293211c075f793f265bdb`; original corpus not recovered and original digest unknown | Python `json.dumps(... sort_keys=True, separators=(',', ':'))` matched 17/17 observed/reconstructed canonical strings in historical analysis; historical Node runner invocation/raw input route not bound | 17/17 is a behavior fingerprint, not source attribution and does not recover the lost original corpus; V2 remains experimental/non-binding | Exact source input bytes, derivation history and runner evidence are needed. L2.1-B execution authorization remains false/blocked in the campaign records | BLOCKED / HISTORICAL-OBSERVATION |
| BM-004 | L2.1-B experimental raw/typed stage separation | Experimental V2: 19 vectors (12 RAW / 7 TYPED); manifest length 28,256 bytes; SHA-256 `e3cf2a8856025ae89fd9f9d4870a3ee047f70d16133b8324b2a8011ab048e2cf` | No runner commit SHA bound; runner entrypoints were candidates/proposals, not a recorded committed-runner execution | `PASS_PHYSICAL_INTEGRITY_SCHEMA; FAIL_FOR_GATE_E_READINESS`; `EXPERIMENTAL_NON_BINDING`; original corpus NOT_RECOVERED; observations NOT_RUN | Generator audit found typed schema-invalid descriptors, prior wrong 1e21 binary64 bits, missing direct typed NaN/lone-surrogate cases, raw surrogate stage expectation errors, ambiguous embedded/final manifest digests and stale-directory risk | BLOCKED / NOT-RUN |
| BM-005 | Aura-vNEXT local `AURA-CANON/1` profile | Profile specifies integer-only, rejects null/floats/lone surrogates, UTF-8 output, UTF-16 key ordering, no Unicode normalization; profile/source digest must be pinned per claim | Exact runner entrypoint, commit, fixture digest and environment required per execution | Product M0 record/package/verify loop is documented as operational; this row has no raw run bundle of its own | Product-local evidence remains separate from protocol-wide authority and legacy compatibility | PROFILE-BOUND; execution bindings required |
| BM-006 | Release provenance: bind a primary manifest to the exact source commit it claims to measure | `AURA_SYSTEM_STATE_MANIFEST_M0_RC0.yaml` is an **unverified candidate path** carried forward from review context; its current existence and contents were not established by this matrix audit | Verifier command/entrypoint and validation commit remain UNBOUND | A prior review context cited a `release_control.commit_sha` value, but this matrix has not verified the primary manifest, its current value, or a source-to-release mismatch | First locate and immutably bind the primary manifest by repository, path, version, commit SHA, and blob digest. Do not assert a current manifest defect until that record is verified; any corrective change requires separate authorization and re-verification | UNBOUND / SOURCE VERIFICATION REQUIRED |
| BM-007 | DQ-006 residual criteria: a JCS-discriminating vector, evidence reachable from a default branch, a single RI-RS conformance boundary, and any remaining closure/ratification requirement | **Decision status as stated by DQ-006 §1:** SETTLED / described as NORMATIVELY BOUND to APS-200 §8 / APS-300 §5. **Conformance/procedural gate:** OPEN; DQ-006 §12 marks criteria 13–16 NOT MET, including conformance discrimination, default-branch reachability, RI-RS boundary disposition, and Chief Architect ratification of the verdict | No single runner closes this composite gate; each residual requires its own immutable source/evidence binding | DQ-006 §10 records the JCS-degenerate fixture; §10–§12 describe reachability, RI-RS boundary, and ratification gaps. This matrix records those statements and does not independently decide the effect of any ratification requirement | Record of reference inspected for this draft: `vaidt/aura-specification@5ba3567b79c7ac7ff37e0508219c12dab349ca2d`, path `closures/DQ-006_CLOSURE_PACKAGE.md`, Git blob SHA `b72b8b10a49def105e822a917d7e277bd8cc094c`; its recorded status is OPEN. This matrix cannot close or ratify DQ-006 | OPEN (gate) / REPORTED-NORMATIVE-BOUND (decision status as reported by DQ-006; not independently adjudicated here) |
| BM-008 | P-008 result aggregation / empty-set / schema-invalid boundaries | Current status must be read through M1 closure and Wave 1 authorization; standalone P-008 file is listed as historical by Governance Status Index | Product-specific aggregator, fixtures and runner entrypoints need separate rows | Status index points to the M1 consolidated state, while APS-400 DRAFT §5 names `PARTIAL`, `NOT APPLICABLE`, `ERROR`. Any mapping between those vocabularies needs an explicit decision rather than silent substitution | Wave 1 authorization scopes permitted mutation to one repository and named path families; it is not automatically authorization for other repos or L2.1-B runtime execution | CONFLICT / SCOPE-BOUND |

## 6. Canonicalization profiles remain separate

**Decision status and gate status must be recorded separately.** The current [DQ-006 Closure Package](https://github.com/vaidt/aura-specification/blob/5ba3567b79c7ac7ff37e0508219c12dab349ca2d/closures/DQ-006_CLOSURE_PACKAGE.md) §1 states that the RFC 8785 JCS decision is settled and describes it as normatively bound to APS-200 §8 / APS-300 §5. The same record states that DQ-006 remains OPEN because its evidence does not discriminate RFC 8785 from ordinary sorted JSON; §§12–15 list additional unmet conformance/procedural criteria, including ratification of the verdict. This matrix records the source's stated position; it does not independently determine whether any ratification or authority precondition affects effectiveness. Do not infer implementation conformance from the decision statement, and do not use the open gate alone to negate the decision statement.

Do not use the generic label “AURA canonicalization” without a versioned profile and exact byte-domain contract.

| Profile / mechanism | What may be asserted | What must not be inferred |
|---|---|---|
| APS-200 §8 / RFC 8785 JCS references | DQ-006 §1 states that the JCS decision is settled and normatively bound to APS-200 §8 / APS-300 §5; the matrix records this as REPORTED-NORMATIVE-BOUND without independently adjudicating any ratification/effect condition | The OPEN DQ-006 gate does not, by itself, negate the decision statement. Conversely, that statement does not prove that a given implementation conforms. Other APS clauses must be evaluated separately |
| `AURA-CANON/1` in Aura-vNEXT | Behavior within the exact profile if profile, source and execution are bound | No automatic equivalence to RFC 8785, older repos, or an unbound protocol version |
| Aura-Guard Node/Python JCS-lite | Specific behavior found in pinned source and exercised tests | Not automatically standards-complete or equivalent to Rust/JCS |
| Rust `serde_json_canonicalizer` in conformance-only scope | Package exists and may be used by the conformance test path | Dependency presence does not prove the production serialization path uses it |
| `AURA-RM-CANON/1` | Release-manifest canonicalization under its own contract | Not interchangeable with protocol payload canonicalization |
| Historical Python `json.dumps(sort_keys=True, separators=(',', ':'))` | The tested values matched that behavior under recorded conditions | Not source provenance, normative specification, or general equivalence to JCS |

## 7. Minimum evidence package for an executed row

An EXECUTED-OBSERVED row is invalid unless it binds, at minimum:

1. Full source commit SHA and exact relevant file/blob digests.
2. Exact fixture bytes, digest, generator/version and derivation history when generated.
3. Runner source commit/blob SHA and exact invocation, including behavior-affecting arguments and environment variables.
4. Runtime identity: OS, architecture, runtime/compiler version, dependency lock digest, and container image digest when applicable.
5. UTC start/finish time, unique execution ID, exit status, stdout/stderr or immutable logs, generated outputs and their digests.
6. Expected-result oracle and its source. For negative cases, expected failure stage (parser, domain validator, canonicalizer, adapter representability, or protocol layer).
7. Coverage limits: what the run establishes and does not establish.
8. Independent review reference where required.
9. Applicable authorization record and scope check.
10. Release/manifest binding to the exact tested commit if a release claim is made.

If any item is missing, use a narrower disposition: HISTORICAL-OBSERVATION, PARTIAL-COVERAGE, UNBOUND, NOT-RUN or BLOCKED.

## 8. Change control

This matrix may document evidence and mappings, but MUST NOT by itself:
- ratify or amend protocol clauses;
- alter APS, invariant or result semantics;
- assign an effective protocol version;
- grant implementation, runtime, release or migration authorization;
- turn draft fixtures into normative vectors;
- close DQ-006 or any other governance gate;
- declare a product conformant;
- rewrite or supersede historical evidence.

A changed source requirement must cite a competent normative-change record. A changed implementation authorization must cite separate authorization for the exact repository/branch/path scope. The matrix must not expand either scope.

Until independently reviewed, this is a non-constitutive traceability artifact. Any later normative adoption must follow the governance process and produce a separate explicit decision.

## 9. Completion gates

Do not promote beyond draft until:

- [ ] Each claimed normative requirement points to a current record of reference and exact clause; draft material remains DRAFT-SOURCE.
- [ ] Protocol obligations are separated from product profiles and historical behavior.
- [ ] Each fixture has immutable ID, byte-domain definition and digest.
- [ ] Each runner has a committed entrypoint, exact command, source SHA and runtime/toolchain binding.
- [ ] Each PASS binds to the exact invocation and immutable output/log evidence.
- [ ] Partial-domain tests declare coverage limits; canonicalization includes a vector that discriminates competing algorithms.
- [ ] Historical observations do not claim reproduction without original corpus and runner bindings.
- [ ] Authorization and release-provenance refs resolve to immutable records with matching scope.
- [ ] Taxonomy conflicts are dispositioned by an authorized decision, not normalized here.
- [ ] DQ-006 is closed only through its own explicit closure record.
- [ ] Independent review records accepted scope, unresolved conflicts and residual blockers.

## 10. Source index

- [Governance & Status Index](https://github.com/vaidt/aura-specification/blob/main/GOVERNANCE_STATUS_INDEX.md)
- [M1 Closure Record v1.0](https://github.com/vaidt/aura-specification/blob/main/AURA_M1_CLOSURE_RECORD_v1.0.md)
- [Wave 1 Implementation Authorization v1.2](https://github.com/vaidt/aura-specification/blob/main/AURA_IMPLEMENTATION_AUTHORIZATION_WAVE1_v1.2.md)
- [APS-200 Canonical Data Model](https://github.com/vaidt/aura-specification/blob/main/aps/APS-200_CANONICAL_DATA_MODEL.md) — inspected header says v1.0-DRAFT
- [APS-300 Evidence Model](https://github.com/vaidt/aura-specification/blob/main/aps/APS-300_EVIDENCE_MODEL.md) — inspected header says v1.0-DRAFT
- [APS-400 Conformance Test Matrix](https://github.com/vaidt/aura-specification/blob/main/aps/APS-400_CONFORMANCE_TEST_MATRIX.md) — inspected header says v1.0-DRAFT
- [P-008 Ratification Record v1.0](https://github.com/vaidt/aura-specification/blob/main/AURA_P008_RATIFICATION_RECORD_v1.0.md) — listed as historical by current Governance Status Index; do not interpret standalone
- [DQ-006 Closure Package — inspected source snapshot](https://github.com/vaidt/aura-specification/blob/5ba3567b79c7ac7ff37e0508219c12dab349ca2d/closures/DQ-006_CLOSURE_PACKAGE.md) — repo commit `5ba3567b79c7ac7ff37e0508219c12dab349ca2d`; file blob SHA `b72b8b10a49def105e822a917d7e277bd8cc094c`. §1 reports the JCS decision as SETTLED / NORMATIVELY BOUND to APS-200 §8 / APS-300 §5; status is OPEN and §§12–15 record unmet conformance/procedural criteria, including verdict ratification. This matrix records the source's stated status and does not independently adjudicate effectiveness.
- [Rust Aura-Guard canonical fixture](https://github.com/vaidt/aura-guard-v1.3/blob/main/conformance/canonical/CANONICAL-001.json)
- [Aura-Guard canonical test source](https://github.com/vaidt/aura-guard-v1.3/blob/main/conformance/canonical/canonical_001.rs)
- [Recorded workflow run](https://github.com/vaidt/aura-guard-v1.3/actions/runs/35688714581)
- [Aura-vNEXT profile repository](https://github.com/vaidt/Aura-vNEXT/tree/claude/aura-vnext-genesis-xerti8)
- [Release Management repository](https://github.com/vaidt/Aura-Release-Management)

**Baseline warning:** branch URLs are navigational only. A definitive binding must use immutable commit SHA plus exact artifact blob SHA/digest.

---

*End of non-constitutive draft artifact.*

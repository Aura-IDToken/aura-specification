# Aura Specification — Master Completion Plan

**Status:** EXECUTION DRAFT  
**Branch:** `completion/aura-specification-conformance`  
**Baseline:** `main` @ `62d2d6bcc1a46dd505ebfe400ad01fa3c6a25bf0`  
**Purpose:** Complete the specification repository without silently converting implementation behaviour into normative requirements.

## 1. Governing rule

The AURA Constitution v1.0 is FROZEN. It explicitly establishes **Specification First**, **Explicit over Implicit**, **Version Everything**, and requires conformance against APS-001 and APS-100. AI systems may analyse, propose, implement, and prepare tests, but must not approve or modify frozen canonical documents.

Accordingly, this branch is an implementation workspace. It may contain drafts, evidence, fixtures, conformance tooling, and proposed normative text. No canonical document is treated as approved merely because it exists on this branch.

## 2. Verified starting condition

- `specification/APS-001_PROTOCOL_SPECIFICATION.md` is currently `0.2-DRAFT`, `Status: DRAFT — ARCHITECTURE REVIEW REQUIRED`. It now exists as the root normative draft, but remains the principal repository-level blocker until review and approval.
- APS-100 through APS-500, APS-900 and APS-950 exist as `1.0-DRAFT` documents.
- APS-100 defines 15 invariants and requires every invariant to have a conformance test and evidence path.
- APS-400 defines CONF-001 through CONF-015, but the repository currently contains draft test-definition documents rather than an end-to-end executable conformance gate.
- APS-500 defines the reference-fixture contract, but the canonical fixture set is not yet demonstrably complete against the invariant/test matrix.
- APS-900 defines the required traceability chain from Constitution → APS Requirement → Invariant → Data Model → Evidence → Conformance Test → Fixture → Implementation → Release.
- APS-950 identifies RI-PY (`aura-poc-a-core`) and RI-RS (`aura-guard`) as reference implementations and requires a full conformance process.
- The repository now has a draft repository-native conformance workflow at `.github/workflows/draft-conformance.yml`, but it still executes only the current repository-local subset and is not yet equivalent to RI-PY / RI-RS certification evidence.
- CK-003 closure material exists in-repository, but evidence presence is not equivalent to normative closure; DQ-003/DQ-004 and release-gate promotion still require explicit review and acceptance.

## 3. Completion gates

### G0 — Baseline and repository hygiene

Freeze the current main SHA, inventory branches, identify unmerged CK-003 evidence, and establish one completion branch.

### G1 — Root normative specification

Draft APS-001 from first principles using the Constitution and existing APS documents as constraints. Resolve scope, execution lifecycle, inputs, outputs, policy semantics, evidence generation, cryptographic domains, errors, conformance, and normative references.

### G2 — Normative consistency

Reconcile APS-100/200/300/400/500/900/950 against APS-001. Every MUST-level requirement must have a traceability path and no document may introduce an undefined semantic dependency.

### G3 — CK-003 closure

Review and integrate only evidence that survives independent verification:
- DQ-002 hash-domain decision and cross-language fixture.
- DQ-003 version semantics and binding fixture.
- DQ-004 event-type semantics.
- Remaining DQ gates required by the current evidence program.

### G4 — Executable conformance

Turn the specification into machine-checkable contracts: fixtures, RI-PY tests, RI-RS tests, shared expected values, and a deterministic conformance runner.

### G5 — CI enforcement

Add repository-native GitHub Actions that run specification validation and conformance checks. CI must fail closed on normative regressions. Payment/plan limitations must be treated as environment evidence, not as a false PASS.

### G6 — Traceability and release readiness

Produce a complete APS → INV → CONF → FIX → Evidence → RI → Release matrix. Close only those rows with objective evidence. Publish a release-readiness report and leave unresolved items explicitly marked OPEN/BLOCKED.

## 4. Non-negotiable completion criteria

The repository is **not complete** merely because documents exist. Completion requires:

1. APS-001 is authored and formally approved by the project owner/Chief Architect.
2. No contradictory normative semantics remain across APS documents.
3. All 15 invariants have explicit verification methods and executable conformance coverage.
4. Reference fixtures have stable, versioned expected values.
5. RI-PY and RI-RS agree on all shared canonical fixtures where interoperability is required.
6. Hash-domain semantics are explicit and bound to canonical bytes.
7. Version semantics are explicit and testable.
8. Traceability is complete from requirement to release evidence.
9. CI executes the conformance gate.
10. Any external/environmental blocker is reported as BLOCKED rather than converted into PASS.

## 5. Execution discipline

No production implementation in Core or Guard is modified as a side effect of completing this specification repository. Specification closure precedes implementation remediation. Once the specification is stable, Core and Guard are brought into conformance against it.

## 6. Immediate execution backlog — NOW

The following backlog defines the work that is actionable **now**, before full schema closure, conformance automation, or release work.

### WP-1 — APS-001 gap list

**Status:** CLOSED
**Goal:** make APS-001 the stable reference point for every downstream correction.

Tasks:
1. Review APS-001 section-by-section against the Constitution and existing APS dependencies.
2. Mark each section as `READY FOR REVIEW`, `OPEN`, or `BLOCKED`.
3. Record where APS-001 depends on unresolved APS-200 / APS-300 contracts, DQ-003 version semantics, or DQ-004 event-type semantics.
4. Produce one consolidated gap list rather than rewriting the full document.

Expected output:
- a concise APS-001 gap register with per-section status
- explicit list of unresolved contract dependencies

#### WP-1 deliverable — APS-001 section gap register

| APS-001 section | Status | Current assessment | Primary dependency / blocker |
|---|---|---|---|
| §1 Protocol Identity and Scope | READY FOR REVIEW | Mission, protocol identity, and scope boundary are consistent with the Constitution. | Architecture Review / approval only |
| §2 Protocol Execution Model | OPEN | Execution flow is coherent, but the binding between execution profile, audit record, and evidence lifecycle still needs tighter downstream reconciliation. | APS-200 / APS-300 cross-references |
| §3 Input Requirements | BLOCKED | Request validity depends on exact `ENT-002` schema, field constraints, numeric contract, and version-compatibility behaviour that are not fully closed. | APS-200 schemas; DQ-003 |
| §4 Output Requirements | BLOCKED | Result requirements are directionally clear, but the exact `ENT-003` contract and canonical decision vocabulary are still unresolved. | APS-200 `ENT-003` closure |
| §5 Policy Model | OPEN | Reproducibility and fail-closed semantics are stable, but canonical policy identity/version semantics need tighter binding. | DQ-003; APS-200 `ENT-004` |
| §6 Evidence Generation Requirements | BLOCKED | Required evidence fields are listed, but exact Evidence Pack structure, attestation contract, and profile boundaries remain incomplete. | APS-300 pack schema; `ENT-006`; Evidence Profiles |
| §7 Cryptographic Requirements | OPEN | Canonical-byte and hash-domain wording is materially stable, but full Merkle-profile closure and conformance evidence promotion remain incomplete. | DQ-002 scope; DQ-006 residuals |
| §8 Error Handling | OPEN | Fail-closed behaviour is defined, but compatibility exceptions and error classification still depend on downstream harmonization. | APS-100 / APS-200 / version rules |
| §9 Conformance Requirements | BLOCKED | The conformance gate is defined, but mandatory PASS evidence does not yet exist for fixtures, runner, and full matrix execution. | APS-400 / APS-500 / runner / CI |
| §10 Normative Authority | READY FOR REVIEW | Hierarchy is explicit and consistent with the Constitution. | Downstream citation cleanup only |
| §11 Traceability | OPEN | The required chain is correct, but APS-001 requirements are not yet exhaustively mapped to invariant-level verification rows. | APS-900 traceability completion |
| §12 Version Binding | BLOCKED | The section requires an explicit compatibility matrix that does not yet exist as a settled normative contract. | DQ-003 |
| §13 Release Gate | BLOCKED | The release gate is directionally correct, but fixtures, runner, CI, release evidence, and approval records are not yet in place. | APS-500 corpus; runner; CI; review evidence |
| Appendix A — Open closure dependencies | OPEN | The blocker list is substantially correct and should remain the single short list for APS-001 approval gating. | Must stay synchronized with DQ-003 / DQ-004 / APS-200 / APS-300 / CI state |

#### WP-1 — stable vs unresolved areas

Stable enough for review:
- §1 Protocol Identity and Scope
- §10 Normative Authority
- the core constitutional posture of APS-001 as a normative draft

Open but not fully blocked:
- §2 Protocol Execution Model
- §5 Policy Model
- §7 Cryptographic Requirements
- §8 Error Handling
- §11 Traceability
- Appendix A maintenance and synchronization

Blocked by unresolved downstream contracts:
- §3 Input Requirements
- §4 Output Requirements
- §6 Evidence Generation Requirements
- §9 Conformance Requirements
- §12 Version Binding
- §13 Release Gate

#### WP-1 — immediate dependency set

The smallest dependency set now controlling APS-001 approval readiness is:

1. machine-readable APS-200 entity schemas
2. exact APS-300 Evidence Pack schema and Evidence Profile boundaries
3. DQ-003 version-compatibility semantics
4. DQ-004 event-type semantics and approved registry entries
5. canonical APS-500 fixture corpus
6. executable cross-language conformance runner
7. repository-native CI gate
8. Architecture Review / Chief Architect approval record

#### WP-1 — next correction queue triggered by this register

1. APS-200 — close `ENT-002`, `ENT-003`, `ENT-004`, `ENT-006`, `ENT-007`, version-binding, and machine-readable schema gaps
2. APS-300 — close Evidence Pack structure, attestation linkage, and Evidence Profile definitions
3. APS-100 / APS-400 / APS-500 — align conformance language with the real fixture and execution state
4. APS-900 — complete APS-001 requirement-to-traceability mapping
5. CK-003 DQ-003 / DQ-004 blocker records — settle version and event-type semantics needed by APS-001 approval

### WP-2 — APS reconciliation pass

**Status:** OPEN
**Goal:** identify the first downstream documents that must change once APS-001 gaps are agreed.

Priority order, based on the dependency findings below:
1. APS-200 — closes the entity, identity, version-binding, and event-record contracts used by APS-001.
2. APS-300 — closes the Evidence Pack, attestation, and profile contracts that depend on APS-200.
3. APS-100 — aligns the invariant catalogue and verification detail after those contracts stabilize.
4. APS-400 — align detailed procedures and evidence states with the stabilized invariant contracts.
5. APS-500 — promote fixtures against the closed schemas and procedures.
6. APS-900 — complete requirement-to-release traceability using the resulting contracts and evidence.
7. APS-950 — align reference-implementation certification requirements with the completed conformance path.

Tasks:
1. Check each document's authority chain and APS-001 references.
2. Find MUST-level requirements without a single clear path to `INV / CONF / FIX / EVID`.
3. Record semantic conflicts in versioning, canonical bytes, evidence, identity, audit record, and policy semantics.
4. Produce an ordered correction list for the next edit wave.

Expected output:
- ordered reconciliation queue for APS-100/200/300/400/500/900/950
- list of must-fix semantic conflicts

#### WP-2 deliverable — initial reconciliation pass for APS-100 / APS-200 / APS-300

This first WP-2 pass covers the highest-priority normative dependencies reviewed directly against APS-001.

| Document | Authority-chain assessment | Missing or weak traceability path | Must-fix semantic conflicts | Correction priority |
|---|---|---|---|---|
| APS-100 | Authority citation to APS-001 is correct, but the document body no longer matches the current APS-400 / registry state. | `§3` still shows no CONF assignment for `INV-007`, `INV-012`, `INV-013`, `INV-014`, `INV-015`; `§5` traceability order differs from APS-001 / APS-900; the catalogue entries do not carry the verification/evidence detail that `§2` says every invariant MUST define. | stale invariant-to-CONF catalogue; APS-100's own structure requirements are satisfied only in the registry, not in the APS-100 body; compliance wording assumes invariant PASS status without defining a canonical invariant-status model. | HIGH |
| APS-200 | Authority chain is directionally correct and now carries the DQ-006 serialization closure, but several required contracts are still only partial. | No exact machine-readable schema set for `ENT-001…ENT-008`; `ENT-004` has no CONF mapping in `§10`; attestation lifecycle and additional profile contracts remain open even though the current draft `ENT-002`/`ENT-003` working profile is now closed. | `object_id` allows `UUID v4 or canonical format`, which is too loose for INV-015 / APS-001 identity semantics; `ENT-007.event_type` depends on a registry with no approved tokens yet (DQ-004 blocker); evidence / attestation / audit relationships remain under-specified for APS-001 approval. | CRITICAL |
| APS-300 | Authority chain is correct and cryptographic byte-domain binding is materially aligned with APS-200 §8. | The current draft `EPR-CORE` pack contract and requirement-reference linkage are now explicit, but attestation authority/lifecycle and additional Evidence Profile vocabularies remain open. | `evidence_id` is fixed to UUID v4, which may conflict with the unresolved canonical-identity contract; `attestation_reference` is mandatory while `ENT-006` lifecycle/authority is unresolved in APS-200; verification claims conformance/invariant verification without fully executed pack/linkage evidence. | CRITICAL |

#### WP-2 — reconciliation conclusions from this first pass

1. **APS-200 is the first correction target.**
   APS-001 blockers for input, output, policy-reference, audit-record, identity, and version-binding semantics all terminate in APS-200 gaps.

2. **APS-300 is the second correction target.**
   APS-001 evidence-generation and release-gate blockers cannot close until the Evidence Pack, attestation linkage, and Evidence Profile boundaries are explicit.

3. **APS-100 needs alignment after APS-200 / APS-300 stabilization.**
   Its largest issues are catalogue staleness and mismatch with the current registry / APS-400 state, not the absence of an authority chain.

#### WP-2 — ordered correction queue triggered by these findings

1. APS-200
   - tighten canonical identity semantics for `object_id` / `object_type`
   - close `execution_id`, `request_fields`, decision vocabulary, and attestation lifecycle contracts
   - complete entity-to-CONF traceability, especially `ENT-004` and `ENT-007`
   - convert entity contracts into machine-readable schemas
2. APS-300
   - define the Evidence Pack container and linkage model
   - add the missing requirement-to-evidence traceability field/contract needed by INV-005
   - define Evidence Profiles and attestation expectations
3. APS-100
   - reconcile the invariant catalogue with CONF-011…CONF-015
   - align APS-100 traceability wording with APS-001 / APS-900
   - decide whether APS-100 itself or the registry is the authoritative home for invariant verification/evidence detail

#### WP-2 deliverable — second correction wave for APS-400 / APS-500 / APS-900

This second WP-2 pass aligns the downstream execution, fixture, and compliance documents with the current repository state after the APS-100 / APS-200 / APS-300 corrections and the WP-4 / WP-5 / WP-6 planning work.

| Document | Main correction applied | Resolved inconsistency | Remaining open dependency |
|---|---|---|---|
| APS-400 | corrected `CONF-009` to `INV-010`, added readiness posture, and restored `CONF → FIX → EVID → RI → REL` traceability order | removes the stale mapping where `CONF-009` was described as an evidence test for `INV-004 / INV-005` instead of the invariant-completeness gate for `INV-010` | executable evidence is still broadly absent; readiness states are not PASS |
| APS-500 | distinguished normative APS-500 fixtures from working corpus artifacts and recorded the promotion register | removes the false implication that all current fixture files are already canonical certification fixtures | APS-200 schemas, APS-300 pack contract, DQ-004, corpus versioning, and identity closure still block broader promotion |
| APS-900 | expanded the compliance-status model and replaced stale examples with current mappings | removes example rows that referenced nonexistent or obsolete fixture/evidence identifiers | complete machine-readable requirement mapping and release-ready evidence still remain open |

#### WP-2 — next correction priority after this wave

After APS-400 / APS-500 / APS-900 alignment, the active WP-2 stream should focus on:

1. targeted correction of the underlying `conformance/CONF-008`, `CONF-009`, `CONF-014`, and `CONF-015` definitions where their detailed procedures still lag the APS-level contract
2. promotion or binding work for `FIX-INV-007`, `FIX-INV-013`, and the first discriminating `CONF-003` vector
3. completion of the remaining APS-001-dependent normative closures (`DQ-003`, `DQ-004`, identity binding, APS-500 corpus freeze)

#### WP-2 deliverable — execution-document correction wave for CONF-008 / CONF-009 / CONF-014 / CONF-015

This follow-up pass corrected the lower-level execution documents so they no longer contradict the APS-level reconciliation:

- `CONF-008` now depends on an approved compatibility matrix and bound compatibility fixtures instead of the stale `FIX-001` placeholder path
- `CONF-009` now correctly defines **Conformance Completeness** for `INV-010` and records it as structural traceability validation
- `CONF-014` now distinguishes normative APS-500 fixtures from working-corpus artifacts before PASS accounting
- `CONF-015` now records explicit identity-contract prerequisites and current blocked posture
- coupled indexes/templates were updated so the conformance corpus and reporting template use the corrected `CONF-009` title and full `CONF-011…CONF-015` list

### WP-3 — CK-003 blocker register

**Status:** CLOSED
**Goal:** separate normative decisions from working evidence and unresolved closure gates.

Tasks:
1. List all DQ items still blocking release-readiness.
2. Separate already-bound normative decisions from working evidence and unresolved closure requirements.
3. Treat DQ-003, DQ-004, and DQ-006 residuals as the immediate blocker set.
4. Keep DQ-002 in scope only where it changes the normative contract.

Expected output:
- one CK-003 blocker register using only `OPEN / BLOCKED / READY / CLOSED`
- explicit minimum DQ set required before schema + conformance promotion

#### WP-3 deliverable — CK-003 blocker register

Recorded in:

- `/home/runner/work/aura-specification/aura-specification/ck003/CK003_BLOCKER_REGISTER.md`

Current minimal set controlling further specification stabilization:

1. DQ-003 — version semantics
2. DQ-004 — event-type semantics
3. DQ-006 residuals — R1 through R4

DQ-002 remains closed and is not part of the minimum active workset for continued specification stabilization.

### WP-4 — Traceability gap pass

**Status:** CLOSED
**Goal:** make every invariant traceability state explicit before claiming closure progress.

Tasks:
1. Walk `INV-001` through `INV-015`.
2. Confirm for each invariant: APS source, CONF assignment, fixture status, expected evidence type, and RI relevance.
3. Mark the weakest missing link as exactly one of: `OPEN`, `BLOCKED`, `READY`, `NOT VERIFIED`.

Expected output:
- a working traceability gap register with one row per invariant
- no unstated assumptions about fixture or evidence readiness

#### WP-4 deliverable — invariant traceability gap register

Status model used here:

- `BLOCKED` — a prerequisite contract, fixture, or registry is still missing
- `OPEN` — the semantic path exists, but required closure work is still incomplete
- `READY` — the prerequisite contract and fixture path are sufficiently defined for controlled execution
- `NOT VERIFIED` — the path exists but lacks objective implementation evidence

| INV | APS source | CONF | FIX | Evidence | RI relevance | Status | Weakest missing link / reason |
|---|---|---|---|---|---|---|---|
| INV-001 | APS-001 §2 | CONF-001 | FIX-001 | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | READY | Repository-local deterministic request/result/evidence verification now runs against `FIX-001`, but implementation-side controlled evidence is still missing. |
| INV-002 | APS-001 §2 | CONF-002 | FIX-001 | EVID-CORE, EVID-CHAIN | RI-PY / RI-RS `NOT VERIFIED` | READY | Repository-local replay verification now runs against `FIX-001`, but implementation-side replay evidence is still missing. |
| INV-003 | APS-200 §4, §8 | CONF-003 | CANONICAL-001 | EVID-CORE | RI-PY / RI-RS `PARTIAL` | OPEN | Canonical serialization contract is settled, but DQ-006 remains open because discriminating cross-language closure evidence is incomplete. |
| INV-004 | APS-300 §3, §7 | CONF-004 | FIX-001 | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | READY | Repository-local draft execution path exists via `scripts/check-fix001-evidence.py`, but implementation-side controlled evidence is still missing. |
| INV-005 | APS-300 §11, APS-900 | CONF-005 | FIX-001 | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | READY | Repository-local traceability verification now runs against `FIX-001`, but implementation-side attestation-linked evidence is still missing. |
| INV-006 | APS-001 §2 | CONF-006 | FIX-001 | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | READY | Repository-local artifact-level platform-independence verification now runs against `FIX-001`, but implementation-side cross-platform evidence is still missing. |
| INV-007 | APS-001 §3 | CONF-011 | FIX-INV-007 | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | READY | Working fixture and test assignment exist; the remaining gap is controlled execution and evidence, not unresolved contract semantics. |
| INV-008 | APS-001 §8 | CONF-007 | FIX-ERROR (TODO) | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | BLOCKED | Error-handling fixture coverage is still missing. |
| INV-009 | APS-001 §12, APS-200 §9 | CONF-008 | FIX-COMPAT-001 | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | READY | Repository-local DQ-003 compatibility matrix and bound fixture now execute through the draft runner, but implementation-side evidence is still missing. |
| INV-010 | APS-400 | CONF-009 | all FIX | EVID-CONF | RI-PY / RI-RS `NOT VERIFIED` | OPEN | Structural CONF assignment is complete, but objective execution evidence for the full invariant matrix is still absent. |
| INV-011 | APS-300 §7 | CONF-010 | FIX-001 | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | READY | Repository-local digest verification now runs against `FIX-001`, but implementation-side cryptographic evidence is still missing. |
| INV-012 | APS-300, APS-200 ENT-007 | CONF-012 | FIX-INV-012 | EVID-AUDIT | RI-PY / RI-RS `NOT VERIFIED` | READY | Repository-local DQ-004 registry token, bound fixture, and draft CONF-012 gate now exist, but broader vocabulary and implementation-side evidence are still missing. |
| INV-013 | APS-001 §5 | CONF-013 | FIX-INV-013 | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | READY | Policy-determinism semantics are defined and the fixture path exists, but execution evidence is still outstanding. |
| INV-014 | APS-500 | CONF-014 | FIX-INV-014 | EVID-CORE, EVID-CONF | RI-PY / RI-RS `NOT VERIFIED` | BLOCKED | APS-500 corpus is not yet finalized; fixture is explicitly `APS500_VERSION_BLOCKED`. |
| INV-015 | APS-000 §4, APS-200 §4 | CONF-015 | FIX-INV-015 | EVID-CORE | RI-PY / RI-RS `NOT VERIFIED` | BLOCKED | Canonical identity still depends on final APS-000 / APS-200 binding and fixture promotion. |

#### WP-4 — dominant blocker summary

The traceability pass shows four dominant blocker classes:

1. **missing canonical fixtures**
   - INV-001, INV-002, INV-004, INV-005, INV-006, INV-008, INV-011
2. **event-type and remaining closure dependencies**
   - INV-012 depends on DQ-004
   - INV-003 still depends on DQ-006 residual execution evidence
3. **APS-500 corpus immaturity**
   - INV-014 remains blocked until the normative fixture corpus is finalized
4. **identity-contract incompleteness**
   - INV-015 remains blocked until APS-000 / APS-200 identity binding is fully closed

#### WP-4 — immediately executable subset

The invariants currently closest to controlled execution are:

- `INV-007` — `READY`
- `INV-009` — `READY`
- `INV-013` — `READY`

The invariant with the strongest existing semantic contract but still-open cross-language evidence is:

- `INV-003` — `OPEN`

### WP-5 — Fixture promotion plan

**Status:** CLOSED
**Goal:** distinguish placeholders and working corpus artifacts from candidate normative fixtures.

Tasks:
1. Classify each current fixture as `PLACEHOLDER`, `WORKING`, or `CANDIDATE NORMATIVE`.
2. Identify the minimum fixture set needed for a first meaningful conformance run.
3. Record fixture dependencies on APS-200 schemas, APS-300 pack structure, and specific CONF procedures.

Expected output:
- fixture promotion table covering `FIX-001`, `/fixtures/corpus/`, and `/fixtures/ck003/`
- explicit minimum fixture set for early conformance execution

#### WP-5 deliverable — fixture promotion register

Classification model used here:

- `PLACEHOLDER` — structure exists, but canonical test content is still TODO-bound
- `WORKING` — usable closure artifact or draft fixture, but not yet fit for normative APS-500 promotion
- `CANDIDATE NORMATIVE` — concrete fixture content exists and can be promoted once the remaining explicit gate is satisfied

| Artifact | Scope | Related INV / CONF | Classification | Current basis | Promotion gate |
|---|---|---|---|---|---|
| `fixtures/core/FIX-001_BASIC_EVALUATION.json` | baseline evaluation | `INV-001`, `INV-014` / `CONF-001` | WORKING | canonical request, result, and current draft `EPR-CORE` evidence content are now concrete | controlled execution evidence + APS-500 promotion |
| `fixtures/corpus/FIX-INV-007_zero_float.json` | zero-float runtime | `INV-007` / `CONF-011` | CANDIDATE NORMATIVE | fixture is explicitly bound to `CONF-011` and marked ready for controlled execution | controlled execution evidence and promotion into APS-500 corpus |
| `fixtures/corpus/FIX-INV-012_event_type.json` | audit/event-type semantics | `INV-012` / `CONF-012` | WORKING | fixture structure exists and captures strict rejection semantics | DQ-004 closure + approved registry entries |
| `fixtures/corpus/FIX-INV-013_policy_determinism.json` | policy determinism | `INV-013` / `CONF-013` | CANDIDATE NORMATIVE | one concrete policy/input pair is now bound for controlled execution | controlled execution evidence and promotion into APS-500 corpus |
| `fixtures/corpus/FIX-INV-014_aps500_compatibility.json` | corpus compatibility | `INV-014` / `CONF-014` | WORKING | fixture is structurally present, but explicitly blocked on APS-500 corpus/version binding | finalized normative APS-500 corpus version |
| `fixtures/corpus/FIX-INV-015_canonical_identity.json` | canonical identity | `INV-015` / `CONF-015` | WORKING | fixture intent is clear, but required identity fields are not yet normatively bound | final APS-000 / APS-200 identity contract |
| `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | canonical serialization evidence vector | `INV-003` / `CONF-003` | WORKING | explicit canonical bytes, digest, and cross-language evidence exist | discriminating RFC 8785 vector to close DQ-006 residual R1 |
| `fixtures/corpus/CANONICAL-002_jcs_discriminating.json` | canonical serialization discriminating vector | `INV-003` / `CONF-003` | WORKING | first discriminating candidate is prepared for RI-PY / RI-RS execution | record observed bytes, SHA-256, and leaf outputs from both implementations |
| `fixtures/ck003/manifest.json` | CK-003 working corpus index | `INV-007`, `INV-012`, `INV-013`, `INV-014`, `INV-015` | WORKING | inventory and per-entry status are explicit | promote referenced fixtures individually; keep manifest as working orchestration metadata |
| `fixtures/ck003/expected_digests.json` | expected digest registry | `INV-003` support, CK-003 closure work | WORKING | explicit `null` semantics prevent false PASS assumptions while contracts remain open | freeze canonical bytes / registry / policy / identity dependencies before filling unresolved digest slots |

#### WP-5 — minimum fixture set for a first meaningful conformance run

The smallest execution package that can advance conformance without waiting for the full APS-500 corpus is:

1. **`FIX-INV-007` + `CONF-011`**
   - first direct candidate for controlled execution
   - no unresolved event-type, APS-500 corpus, or identity binding dependency
2. **`FIX-INV-013` + `CONF-013`**
   - concrete policy/input binding now exists
   - should be the second controlled run
3. **`CANONICAL-001` + `CANONICAL-002` + `CONF-003` + DQ-002 fixture vectors**
   - sufficient for continued serialization/hash-domain evidence work
   - not enough for final normative closure until `CANONICAL-002` is executed cross-language and the resulting artifacts become reachable evidence

This means the first meaningful conformance wave should target:

- `INV-007`
- `INV-013`
- then `INV-003`

#### WP-5 — dependency gates revealed by the promotion pass

The promotion pass reduces the remaining blockers to four fixture-gate classes:

1. **schema / Evidence Pack incompleteness**
   - blocks `FIX-001`
2. **event-type governance closure**
   - blocks normative promotion of `FIX-INV-012`
3. **APS-500 corpus and version binding**
   - blocks `FIX-INV-014`
4. **identity-contract closure**
   - blocks `FIX-INV-015`

### WP-6 — Minimum automation plan

**Status:** CLOSED
**Goal:** sequence safe automation work without freezing unstable contracts too early.

Implement now:
1. `check-doc-headers.sh`
2. `check-ids.sh`
3. `check-traceability.sh`

Defer until schemas and canonical formats stabilize:
- `validate-fixtures.sh`
- `generate-traceability-matrix.py`

Expected output:
- phased automation order with prerequisites
- explicit defer list for schema-dependent tooling

#### WP-6 deliverable — phased minimum automation plan

Automation is split into two waves:

1. **safe-now repository validators**
   - can be implemented without freezing unresolved schemas or fixture payload contracts
2. **schema-bound automation**
   - must wait until APS-200 / APS-300 / APS-500 contracts are explicitly stable

#### WP-6 — immediate automation wave

| Script | Primary purpose | Inputs / scope | Safe now because | Required prerequisite |
|---|---|---|---|---|
| `check-doc-headers.sh` | verify required metadata headers on normative documents | Constitution, APS, INV, CONF, compliance, reference, closure records | depends only on document structure already used throughout the repo | stable header convention per current documents |
| `check-ids.sh` | detect accidental ID reuse across controlled namespaces | `INV`, `CONF`, `FIX`, `ADR`, `RFC`, related document identifiers | works on textual identifiers and does not require finalized schemas | stable identifier prefixes already exist |
| `check-traceability.sh` | verify minimum structural links `INV → CONF` and `CONF → FIX` | invariant registry, conformance index/docs, fixture indexes/manifests | structural linkage can be checked before full PASS evidence exists | current registry + conformance catalog + fixture inventory |

These three scripts form the **minimum safe automation baseline** because they validate repository integrity without interpreting unresolved protocol payload semantics.

#### WP-6 — execution order and dependency logic

1. **`check-doc-headers.sh` first**
   - establishes that the repository metadata surface is parseable and consistent
   - reduces false negatives in later ID / traceability checks
2. **`check-ids.sh` second**
   - validates identifier hygiene before link-graph checks
   - prevents ambiguous traceability results caused by duplicate IDs
3. **`check-traceability.sh` third**
   - runs only after documents and IDs are stable enough to support deterministic graph traversal

#### WP-6 — deferred automation set

| Script | Why deferred | Explicit gate to unblock |
|---|---|---|
| `validate-fixtures.sh` | fixture payloads and expected evidence remain partially placeholder- or working-only, so schema validation would freeze unstable contracts too early | APS-200 machine-readable schemas + APS-300 Evidence Pack contract + promoted APS-500 fixture corpus |
| `generate-traceability-matrix.py` | automatic matrix generation would encode unresolved semantics and maturity assumptions into generated outputs | stable APS requirement mapping + settled fixture promotion set + clearer release-evidence model |

#### WP-6 — minimum implementation contract for each immediate script

All immediate scripts should share the same operating contract:

- read-only execution
- deterministic output ordering
- exit `0` on success and non-zero on failure
- concise summary plus per-finding detail
- no PASS claims about implementation conformance, only repository-structure validation

#### WP-6 — next implementation wave after NOW

Once the safe-now scripts exist, the next automation wave should be:

1. implement `validate-fixtures.sh`
2. implement `generate-traceability-matrix.py`
3. then connect all of the above into repository-native CI

#### WP-6 — NOW stage completion note

With WP-6 recorded, the **NOW stage backlog is fully defined and closed as a planning tranche**:

- WP-1 — CLOSED
- WP-3 — CLOSED
- WP-4 — CLOSED
- WP-5 — CLOSED
- WP-6 — CLOSED

WP-2 remains the active normative-reconciliation stream that feeds the next execution wave.

## 7. Immediate execution order

WP-1 and WP-3 through WP-6 are **closed planning deliverables**, not the next work to execute. WP-2 remains active. Proceed in this order:

1. Resolve any required authority ruling before making normative changes that depend on it; the handover assessment identifies cross-corpus precedence (CFL-001) as such a decision, but is non-constitutive.
2. Close DQ-004's remaining registry/evidence work, then execute DQ-006 residuals in their prescribed R1–R4 order; promote DQ-003 from its local gate to RI-backed evidence. See `ck003/CK003_BLOCKER_REGISTER.md`.
3. Apply the WP-2 corrections in dependency order: APS-200, APS-300, APS-100, then remaining APS-400/500/900/950 and CONF-document alignment.
4. Promote the candidate fixtures and extend the invariant/conformance matrix; begin controlled execution with INV-007 and INV-013, followed by INV-003.
5. Expand the existing draft runner and CI gate to cover the approved fixture/matrix scope, then collect RI-PY / RI-RS evidence.
6. Complete APS-001 Architecture Review and approval, release traceability, and release readiness only after mandatory gates have objective evidence.

## 8. Exit criteria for the NOW stage

The NOW stage is complete only when:

1. APS-001 has a concrete per-section gap list.
2. The next APS correction queue is ordered and justified.
3. CK-003 has an explicit blocker register.
4. Every invariant has an explicit traceability state.
5. Fixtures are separated into placeholder / working / candidate normative sets.
6. Automation order is defined without prematurely locking unstable schemas or formats.

**Current assessment:** all six NOW-stage exit criteria are now explicitly satisfied in repository planning documents. The next execution focus should remain APS reconciliation plus the first controlled conformance wave.

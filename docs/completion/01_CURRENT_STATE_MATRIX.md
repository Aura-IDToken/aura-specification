# Aura Specification — Current-State Conformance Matrix

**Baseline:** `main` @ `62d2d6bcc1a46dd505ebfe400ad01fa3c6a25bf0`  
**Assessment branch:** `completion/aura-specification-conformance`  
**Assessment rule:** existence of a document is not evidence of conformance.

| Domain | Current state | Evidence | Closure requirement |
|---|---|---|---|
| Constitution | **FROZEN / PASS** | `constitution/AURA_CONSTITUTION.md` | No content change; amendments only through constitutional process |
| APS-000 | **DRAFT** | `aps/APS-000_FOUNDATION_AND_TERMINOLOGY.md` | Complete review + approval |
| APS-001 | **DRAFT / CRITICAL** | `specification/APS-001_PROTOCOL_SPECIFICATION.md` exists as `0.2-DRAFT — ARCHITECTURE REVIEW REQUIRED` | Reconcile dependent APS documents + complete Architecture Review / approval path |
| APS-100 | **DRAFT / OPEN** | 15 invariants defined and mapped to CONF-001…015 | Align authority, verification language and execution evidence with APS-001 |
| APS-200 | **DRAFT / OPEN** | Canonical entities + common object contract; draft machine-readable schemas now close the current working-profile ENT-002/ENT-003 payloads under `fixtures/schemas/`, and the current DQ-003 compatibility matrix is now explicit | Additional profile schemas, identity closure, approved event-type registry tokens |
| APS-300 | **DRAFT / OPEN** | Evidence model exists; draft machine-readable Evidence Object / Evidence Pack schemas now publish a concrete current draft `EPR-CORE` content contract for `FIX-001` under `fixtures/schemas/` | Attestation lifecycle closure beyond the current draft working path, additional profile vocabularies, executable fixture/evidence path |
| APS-400 | **DRAFT / INCOMPLETE** | CONF-001/002/004/005/006/010 run via `scripts/check-fix001-evidence.py`, and CONF-008 plus CONF-012 now run through `scripts/run-draft-conformance.py` against explicit local DQ artifacts | Expand executable coverage beyond the current draft-local subset and gather implementation-side PASS/FAIL evidence |
| APS-500 | **DRAFT / INCOMPLETE** | Fixture contract exists; `FIX-001` supports the current draft request/result/evidence/replay/platform gate and `FIX-COMPAT-001` now binds the current DQ-003 compatibility matrix | Publish canonical machine-readable fixture set and expected outputs |
| APS-900 | **DRAFT / INCOMPLETE** | Traceability model exists | Every normative requirement must resolve to test, fixture, evidence, implementation and release |
| APS-950 | **DRAFT / OPEN** | RI requirements exist | Reference implementation certification after conformance gate |
| Invariant Registry | **DRAFT / OPEN** | `INVARIANT_REGISTRY.md` maps all invariants to CONF identifiers | Validate assignments against executable evidence and finalized normative contracts |
| Traceability Matrix | **DRAFT / INCOMPLETE** | `compliance/TRACEABILITY_MATRIX.md` contains current mappings but mixed status maturity | Populate objective statuses; no unsupported PASS claims |
| CK-003 DQ-002 | **PARTIAL / EVIDENCE PRESENT** | `ck003/dq-002-hash-domain` | Keep only the accepted hash-domain contract as normative and preserve the rest as evidence/history |
| CK-003 DQ-003 | **READY / LOCAL GATE** | versioning snapshot, explicit compatibility matrix, bound fixture, and repo-local CONF-008 gate now exist | Run the same matrix against RI-PY / RI-RS and promote it from local draft use to release-grade evidence |
| CK-003 DQ-004 | **READY / LOCAL GATE** | event-type semantics, a current draft registry token, a bound fixture, and a repo-local CONF-012 gate now exist | Extend the registry beyond the local draft token and promote the gate with RI evidence |
| CI | **DRAFT / READY** | `.github/workflows/draft-conformance.yml` now runs the repo-native draft conformance runner and publishes a JSON report artifact | Extend the gate beyond the current draft-local subset and bind it to RI evidence |
| Release v1.0 | **NOT READY** | Roadmap Milestone 4 remains unchecked | Only release after all mandatory gates are evidenced |

## Immediate blockers

1. **APS-001** is the root normative blocker.
2. **CK-003 closure/promotion:** DQ-004 still needs broader approved registry coverage and RI evidence; DQ-006 is OPEN with residuals R1–R4; DQ-003 is ready only for local draft use pending RI evidence.
3. **APS-200 → APS-300 → APS-100 reconciliation:** current draft schemas close only working-profile payloads; identity, attestation/profile, and broader contract gaps remain. APS-100 alignment follows stabilization of APS-200/300.
4. **Conformance evidence:** the full INV/CONF matrix remains unverified. The runner covers only a repository-local subset, so no structural mapping or local PASS substitutes for implementation evidence.
5. **Fixtures and release traceability:** APS-500 still lacks the complete promoted canonical fixture corpus needed for full APS-400/950 certification and release evidence.
6. **CI expansion:** the draft workflow exists, but must be expanded to the approved full matrix and bound to RI evidence.

## Execution order

CFL-001 is a prerequisite for work that depends on selecting a governing authority ladder across the specification and implementation corpora. It is **not presented by this completion plan as a prerequisite for every evidence-preparation activity**. The work split below is a planning distinction, not an authority ruling.

**A CFL-001 ruling is required before:**

- selecting or adopting the precedence rule for a conflict between the specification corpus and the implementation corpus;
- approving, promoting, or superseding a normative decision or requirement whose meaning or effect depends on which corpus governs;
- treating cross-corpus semantic reconciliation, a conformance conclusion, DQ closure/status transition, APS-001 approval, or release-readiness claim as authoritative where that conclusion depends on the unresolved precedence question.

**Before that ruling, the following may only be prepared or recorded as non-constitutive evidence work, within any separately applicable authorization:**

- DQ-006 R1/R3 evidence preparation: execute candidate discriminating vectors and make already-produced evidence reachable, while recording observations without promoting an unapproved expected-value oracle or claiming normative closure;
- DQ-003 RI runs against the existing local compatibility matrix, with results recorded as observations pending any required approval;
- DQ-004 local draft-gate and fixture work, without treating draft registry entries as approved protocol vocabulary;
- APS-200/APS-300 draft schema work, fixture/runner/CI expansion, and traceability-gap recording, provided they remain draft/local and do not silently settle cross-corpus semantics.

These activities do not resolve CFL-001, select an RI-RS authority boundary, ratify a DQ decision, or authorize a normative change. Work that cannot be separated from a cross-corpus normative choice remains blocked pending the ruling. DQ-006 R2/R4 and other approval/status transitions must be assessed against their actual authority dependency rather than inferred to be cleared by successful execution.

For planning, the non-constitutive evidence/preparation stream is:

`DQ-004 local evidence work ∥ DQ-006 R1/R3 evidence work ∥ DQ-003 RI observations ∥ draft schemas / fixtures / runner / CI / traceability`.

The authority-dependent stream is:

`CFL-001 ruling → apply the ruling to affected cross-corpus normative questions → required DQ/APS approval or status transitions → APS-001 approval → release-readiness decision`.

This order is consistent with the dependency findings in `00_MASTER_COMPLETION_PLAN.md` and the active DQ execution order in `ck003/CK003_BLOCKER_REGISTER.md`, while making explicit which activities are preparatory and which require authority. The handover assessment's own recommended sequence sets CFL-001 as Step 0 and says it “Blocks: everything” (`ck003/handover-assessment/09_RECOMMENDED_SEQUENCE.md`). This completion plan does not revise that finding or resolve CFL-001; the assessment is non-constitutive and does not itself create authority. Its broader stop recommendation remains a recorded position, and this plan does not claim authority to override it.

## Immediate backlog — NOW

| Work package | Status | Immediate output |
|---|---|---|
| WP-1 APS-001 gap list | CLOSED | Per-section `READY FOR REVIEW / OPEN / BLOCKED` list for APS-001 recorded in `docs/completion/00_MASTER_COMPLETION_PLAN.md` |
| WP-2 APS reconciliation | OPEN | Initial reconciliation recorded for APS-100 / APS-200 / APS-300 and second-wave corrections recorded for APS-400 / APS-500 / APS-900 |
| WP-3 CK-003 blocker register | CLOSED | CK-003 register recorded with explicit states for DQ-002 / DQ-003 / DQ-004 / DQ-006 and a minimal active DQ set |
| WP-4 Traceability gap pass | CLOSED | One explicit `OPEN / BLOCKED / READY / NOT VERIFIED` state recorded for each invariant in the completion plan |
| WP-5 Fixture promotion plan | CLOSED | Fixture promotion register and minimum early conformance fixture set recorded in the completion plan |
| WP-6 Minimum automation plan | CLOSED | Phased automation order, immediate script scope, and deferred schema-bound tooling recorded in the completion plan |

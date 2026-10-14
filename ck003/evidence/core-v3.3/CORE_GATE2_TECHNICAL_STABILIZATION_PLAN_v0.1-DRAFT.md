# G2-CORE — AURA Core Technical Requirements Stabilization Plan

**Artifact ID:** AURA-G2-CORE-TECH-PLAN-v0.1  
**Status:** WORKING DRAFT / EVIDENCE-PREPARATION ONLY / NON-NORMATIVE  
**Created:** 2026-10-14  
**Repository of record:** `vaidt/aura-specification`  
**Preparation branch:** `work/g2-core-technical-stabilization-2026-10-14`

> This is a program-level technical workstream named **G2-CORE**. It is **not** the repository's formal **GATE-02** for B-VAL-014 / BNC-1. The formal GATE-02 authority assessment records that specific execution authority as NOT ESTABLISHED and GATE-02 as BLOCKED. This plan does not authorize those tests.

## 1. Objective

Build a reviewable technical acceptance matrix for AURA Core v3.3 that separates:

1. behavior directly observed in a pinned source revision;
2. requirements recorded in the current APS corpus;
3. discrepancies between observed behavior and the draft contract;
4. evidence and tests needed to establish conformance;
5. decisions that cannot be made through engineering observations alone.

The immediate output is a stable, source-bound requirements baseline. This plan does not declare conformance or production readiness.

## 2. Non-negotiable scope boundaries

- The AURA Core v3.3 source repository is a frozen measurement instrument. **No implementation code is changed by this workstream.**
- No constitutional constant, frozen specification, canonical APS document, protocol semantic, fixture oracle, or golden vector is changed or promoted by this plan.
- Implementation behavior is evidence of what a particular revision does; it is not, by itself, evidence of what the protocol requires.
- Expected values are not to be inferred from current outputs and then relabelled as normative.
- Any unresolved authority or cross-corpus precedence question remains OPEN/BLOCKED. Engineering observations do not resolve it.
- No release, certification, sealing, deployment, or production-readiness claim is authorized by this artifact.

The existing Core repository decree permits only listed tasks and describes v3.3 as frozen. Changes to that repository require a separate, explicitly authorized task under its governing controls.

## 3. Pinned starting references

This is a documentation-based source inspection, not a claim that all tests were executed.

| Source | Ref / SHA | Use |
|---|---|---|
| `vaidt/aura-specification` | `main @ e722d5c161c5f3451b47b4848f56fc29137d5750` | APS and current completion / blocker records |
| `vaidt/aura-poc-a-core-v3.3` | `main @ 43f054f8deb7c9644c52148d6496b493512d32b0` | Source-observation target; no mutation |
| `core/evaluator.py` | blob `7937d089d296361e440108227f2e938828c3865a` | Fixed-point evaluation and dimension guard |
| `core/merkle.py` | blob `2c8d81dc4c07a890bf42163e4b74e414582edae2` | Legacy Core leaf construction |
| `audit/merkle.py` | blob `c0db98fbfb01eaf558c25d05e3696e78c3e5ffd5` | Audit-layer Merkle/hash behavior |
| `compliance/certificate.py` | blob `823bb743eda461ce54bdf666360135e000eb0a3a` | External certificate representation and fingerprint |
| `core/test_ari_observability.py` | blob `418f3606db89e49bcb9ce1bcd45184d59d231e20` | Non-normative ARI observation harness |
| `core/test_bitwise_replay.py` | blob `f2590d3c023d9d7df070faf3317f465d188663be` | Existing determinism tests |
| `.github/workflows/execution-checks.yml` | revision `43f054f8deb7c9644c52148d6496b493512d32b0` | Current x86_64 / ARM64 and WASM-compat workflow shape |

Normative starting point: `APS-001` is recorded as `0.2-DRAFT — ARCHITECTURE REVIEW REQUIRED`; APS-100 through APS-950 remain drafts in the repository's current status matrix. Therefore the matrix below is traceability and gap preparation, not a promotion of draft statements to approved requirements.

## 4. Initial technical requirements / gap matrix

Status meanings in this matrix: **OBSERVED** = visible in the pinned source; **PARTIAL** = some evidence exists but does not establish the full claim; **GAP** = a concrete implementation/evidence discrepancy is recorded; **NOT VERIFIED** = no sufficient result is cited here; **BLOCKED** = a required decision or authority is missing.

| ID | Technical contract area | Starting observation / gap | Existing traceability target | Required evidence to stabilize the requirement | Initial state |
|---|---|---|---|---|---|
| G2C-01 | Fixed-point ARI measurement | `core/evaluator.py` defines scale 100000 and weights 30000 / 70000, computes a fixed-point dot product, and returns integer `ari` / `drift`. | APS-001 §2; APS-100 INV-001 / INV-006 / INV-007 | Pinned input/output vectors; test reports from the exact Core ref; demonstrate what computation the cross-platform CI actually measures. | OBSERVED / FULL CONFORMANCE NOT VERIFIED |
| G2C-02 | Integer-division semantics | `core/evaluator.py` uses Python `//`; the RD-006 harness labels a negative-dividend case CORE-P0-002 and explicitly warns that other languages may truncate differently. | APS-001 execution/numeric contract; APS-200 numeric representation; RI-PY / RI-RS interoperability | An approved numeric contract and cross-language vectors covering negative, fractional-rescale, and boundary cases. Do not select floor versus truncation from a single implementation output. | GAP / DECISION-DEPENDENT |
| G2C-03 | Drift range and comments | The evaluator's comments describe a clamp to [0, 100000], while its executable expression permits up to 200000. Treat this as a comment/code discrepancy to characterize, not as permission to pick a new range. | APS-001 output requirements; APS-200 result schema; relevant invariant/CONF mapping to be confirmed | Pin the intended range to an approved source, then add tests for aligned, orthogonal, anti-aligned, and invalid-schema cases. | GAP / AUTHORITY-DEPENDENT |
| G2C-04 | Fail-closed vector dimensions | The pinned evaluator explicitly raises `ValueError` when vector dimensions differ, before dot-product calculation. | APS-001 §2 / §8; APS-100 INV-008 | Focused positive and negative tests, including execution under any required optimized interpreter modes and retained output evidence. | OBSERVED / REGRESSION TEST REQUIRED |
| G2C-05 | Canonical event bytes and leaf domain | `core/merkle.py` hashes UTF-8 `json.dumps(data, sort_keys=True)`. The existing Core gap matrix records a different target involving canonical bytes and an explicit leaf domain prefix. | APS-001 §7; APS-200 canonical serialization; CK-003 DQ-002 / DQ-006 where applicable | Trace to the current controlling APS text and accepted decision records; compare emitted bytes, not only digest labels; keep candidate values non-normative until the contract and authority dependencies are confirmed. | GAP / NORMATIVE BINDING REQUIRED |
| G2C-06 | Merkle node / proof construction | `audit/merkle.py` constructs parents through `sha256(left + right)` over textual hex values and duplicates an odd final leaf. This is distinct from the `core/merkle.py` leaf helper. | APS-001 §7; APS-200; APS-300; APS-400 / APS-500 | A single documented byte-level contract, vectors for 1 / 2 / odd leaf counts, proof verification tests, and cross-language comparison. Do not silently treat the two implementations as interchangeable. | GAP / IMPLEMENTATION DIVERGENCE OBSERVED |
| G2C-07 | Certificate numeric domain | `compliance/certificate.py` represents `ari_score` and `drift` as float fields even though the evaluator returns fixed-point integers. The source comments describe this as a presentation boundary. | APS-200 canonical data model; APS-300 evidence pack; CORE gap matrix | Exact distinction between measurement-domain integers and presentation fields; canonical digest-domain representation; serialization and round-trip vectors. | GAP / CONTRACT CLOSURE REQUIRED |
| G2C-08 | Certificate fingerprint | `fingerprint()` hashes UTF-8 `json.dumps(to_dict(), sort_keys=True)`; the code shown does not itself bind that representation to the APS canonical-byte contract. | APS-200 / APS-300; CK-003 DQ-002 / DQ-006 as applicable | Compare actual bytes to the contract; prove that serialization, field omission/inclusion, ordering, and numeric encoding are unambiguous. | GAP / NORMATIVE BINDING REQUIRED |
| G2C-09 | Timestamp format | The certificate accepts a timestamp string; the supplied Core gap matrix flags exact timestamp handling as requiring separate review. | APS-001 / APS-200 / APS-300; the recorded D-TIME-001 / DQ-004 workstream | Establish the current authoritative timestamp requirements and build format/boundary vectors only against that source. | NOT VERIFIED / DEPENDENCY OPEN |
| G2C-10 | Bitwise replay meaning | `core/test_bitwise_replay.py` contains deterministic arithmetic/replay tests. The RD-006 harness itself states that the existing determinism report does not invoke `core.evaluator` and thus does not measure ARI arithmetic. | APS-100 INV-002 / INV-006; APS-400 / APS-500 | Demonstrate that the production evaluator path is run on each target architecture and compare pinned output bytes/hashes across reports. Keep WASM compatibility-pattern tests distinct from evidence of a full WASM runtime. | PARTIAL |
| G2C-11 | Observation test collection | The pinned `core/test_ari_observability.py` uses `unittest.TestCase` but its displayed imports include `from unittest import mock`, not `import unittest`. This indicates a likely collection-time defect that must be verified by an actual run against the pinned ref. | APS-400 conformance execution; APS-100 INV-010 | Reproduce the collection result read-only at the exact SHA; record command, Python version, exit status and raw output. Any fix to the frozen source requires separate task authorization. | SUSPECTED TEST DEFECT / REVALIDATION REQUIRED |
| G2C-12 | RI-PY / RI-RS compatibility | The Core evidence baseline records cross-language equality as not established and points to the need for a shared canonical fixture set. | APS-400 / APS-500 / APS-950; APS-900 traceability | Use a controlled, shared fixture corpus; record exact source revisions for both implementations; compare canonical bytes, numeric outputs, leaf hashes, roots, and verifier results independently. | NOT VERIFIED |
| G2C-13 | Requirements-to-release traceability | Existing `CORE_TO_SPEC_TRACEABILITY.md` is marked INITIAL and “to be completed at Gate B”; APS-950 requires conformance evidence and a report for releases. | APS-400 / APS-500 / APS-900 / APS-950 | Every requirement row must link to invariant, CONF, fixture, evidence artifact, RI revision, and release consequence. Unknown links remain NOT VERIFIED. | OPEN |

This matrix records the starting evidence and verification work. It does not determine that the proposed target contracts are approved, nor does it select an implementation as authoritative where the repository records a competing or unresolved boundary.

## 5. Execution phases

### G2-CORE-A — Read-only source revalidation

- Re-run targeted tests and baseline checks against Core `43f054f8deb7c9644c52148d6496b493512d32b0` in an isolated checkout or CI job.
- Record exact tool versions, command, exit status, raw outputs, artifact hashes and architecture.
- Validate whether the suspected observability test collection defect reproduces.
- Do not make source changes during this phase.

### G2-CORE-B — Requirement binding

- For each row, cite the exact APS section and invariant/conformance target.
- Mark any mismatch between source behavior and APS text as an explicit gap.
- Where APS text is draft, record that fact; do not describe the mapping as an approved norm.
- Preserve distinct states for source existence, test reachability, evidence currency, authority, normative status, and effective status.

### G2-CORE-C — Testability specification

- Define cases and evidence needed to demonstrate each requirement.
- Use existing approved fixtures where their applicability is proven.
- For unresolved numeric/hash/timestamp semantics, document the required decision before freezing expected values.
- Separate tests of one implementation's repeatability from cross-implementation conformance.

### G2-CORE-D — Decision routing and independent review

- Prepare a list of semantic conflicts and their controlling authority dependencies.
- Do not resolve cross-corpus precedence, promote DQ closure, approve APS documents, or issue execution authority through the technical matrix.
- Route each human-only decision with its source conflict, impact, and minimum evidence request.

## 6. Relationship to other gates

### Program-level G2-CORE

G2-CORE is a technical requirements-stabilization workstream. It may prepare read-only evidence, traceability, test plans and draft conformance mappings within applicable authorization.

### Repository formal GATE-02

`fixtures/corpus/GATE_02_AUTHORITY_COVERAGE_ASSESSMENT_v1.0.md` concerns B-VAL-014 / BNC-1 execution authorization. It records:

- independent GATE-02 authority coverage: NOT ESTABLISHED;
- B-VAL-014: NOT AUTHORIZED;
- BNC-1: NOT AUTHORIZED;
- formal GATE-02: BLOCKED.

The draft `governance/AURA_GATE_02_EXECUTION_AUTHORIZATION_v1.0-DRAFT.md` marks the proposed act NOT APPROVED / NOT EFFECTIVE and states that authorization is HUMAN-ONLY. This plan does not execute or override that gate.

## 7. Entry criteria and exit criteria

### Entry criteria met for this preparation increment

- Source revisions pinned.
- Existing Core as-is evidence and gap matrix identified.
- Working/non-normative status made explicit.
- No source, frozen document, or governance record mutated.

### Exit criteria for G2-CORE-A/B planning

- Each row cites pinned source and current APS document/section.
- Each observed behavior is distinguished from a requirement.
- Each gap has a reproducible verification method and evidence format.
- Test results are bound to exact commit/toolchain/architecture.
- No expected value or protocol rule is silently invented.
- All authority-dependent items stay OPEN/BLOCKED until the required decision exists.
- A reviewer can reproduce or challenge each observation from the linked evidence.

Passing these preparation criteria does **not** mean G2-CORE is closed, the formal GATE-02 is authorized, the Core is certified, or production is approved.

## 8. Initial state

| Item | State |
|---|---|
| G2-CORE planning / evidence preparation | STARTED |
| Technical requirements matrix | DRAFT — this artifact |
| Pinned Core source | `43f054f8deb7c9644c52148d6496b493512d32b0` |
| Normative promotion / APS approval | NOT AUTHORIZED BY THIS ARTIFACT |
| Frozen Core source mutation | NOT IN SCOPE |
| Formal GATE-02 (B-VAL-014 / BNC-1) | BLOCKED / NOT AUTHORIZED |
| Production readiness | BLOCKED / NOT CLAIMED |

**End of non-normative preparation plan.**

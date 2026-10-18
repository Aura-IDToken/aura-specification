# AURA — WAVE 1 — CONTRACT DECISION PACKAGE v1.0

## NOT_APPLICABLE & TAXONOMY IMPACT ANALYSIS

**Artifact:** `NOT_APPLICABLE_IMPACT_ANALYSIS_v1.0.md`  
**Repository:** `vaidt/aura-specification`  
**Artifact Class:** CONTRACT DECISION PACKAGE / DECISION GAP  
**Status:** DECISION PENDING / OPEN  
**Date:** 2026-09-24  
**Effect:** NON-CONSTITUTIVE

> Navigation: this is a non-constitutive analysis artifact; see [`GOVERNANCE_STATUS_INDEX.md`](GOVERNANCE_STATUS_INDEX.md) for the current routing of governance/status records.

## 1. Formal Disposition

This artifact records an unresolved contract decision gap. It does not select an option or authorize implementation.

- Conflict: CONFIRMED / OPEN
- Option A (Integrate): PROPOSED / NOT AUTHORIZED
- Option B (Explicitly Retire): PROPOSED / NOT AUTHORIZED
- Schema Change: NOT AUTHORIZED
- Source Contract Amendment: NOT AUTHORIZED
- Implementation Authorization: NOT GRANTED
- Normative Effect: NONE
- M1 (Governance): OPEN / BLOCKED

## 2. Description of the Contract Conflict — NOT_APPLICABLE

The source WAVE 1 Contract Closure Addendum v1.0 includes `NOT_APPLICABLE` among the defined Verification Result values.

The current validated operational schema domain uses `MATCHED`, `MISMATCHED`, `REJECTED`, and `UNDETERMINED`, and does not currently include `NOT_APPLICABLE`.

This artifact records the resulting contract-domain discrepancy. It does not resolve it.

## 3. Options for Resolution

Selection between the following options remains OPEN pending competent contractual/governance authorization.

### Option A — Proposed Integration

Reintegrate `NOT_APPLICABLE` into the operational JSON Schema domain.

Post-authorization engineering work would include:

- define the process-exit semantics for `NOT_APPLICABLE`;
- define any associated error/reason semantics;
- update affected schemas;
- add or revise positive and negative fixtures;
- re-run full corpus validation;
- re-run Single Reason of Failure validation;
- perform independent review of the resulting contract surface.

No such schema mutation is authorized by this artifact.

### Option B — Proposed Explicit Retirement

Propose retirement or deferral of `NOT_APPLICABLE` from the operational WAVE 1 domain.

**Precondition:** competent contractual/governance decision.

Only after authorization:

1. amend the source Addendum;
2. update affected schemas and documentation;
3. update fixtures and test matrix;
4. perform fresh meta-validation;
5. perform fresh SROF validation;
6. conduct an independent review of the resulting contract surface.

Until those conditions are satisfied:

`NOT_APPLICABLE` remains OPEN and no schema mutation is authorized.

## 4. Parallel Decision Gap — Error Taxonomy

The source Addendum defines a broader technical error taxonomy than the current Phase-1 operational subset.

The current operational subset is:

- `E_SCHEMA_INVALID`
- `E_DIGEST_MISMATCH`
- `E_CANONICAL_BYTES_MISMATCH`
- `E_FIXTURE_NOT_FOUND`
- `E_INTERNAL_VERIFIER_ERROR`

Other identifiers present in the source taxonomy are not removed or deprecated by this artifact. Their future integration, retirement, or change of meaning requires separate contractual disposition.

## 5. Evidence Boundary

The current schema/meta-validation evidence establishes:

- 45/45 expected validity matches;
- 33/33 negative vectors satisfying the current Single Reason of Failure criterion for the current corpus.

Those results establish properties of the current schema and corpus only. They do not resolve the `NOT_APPLICABLE` contract decision and do not constitute governance ratification or implementation authorization.

## 6. Non-Constitutive Boundary

This Decision Package is an analytical and evidentiary artifact.

It does not:

- select Option A or Option B;
- amend the source contract;
- mutate the operational schema;
- grant implementation authorization;
- establish authority continuity;
- close M1;
- create normative protocol effect.

## 7. Current Status

```
NOT_APPLICABLE conflict   = CONFIRMED / OPEN
Taxonomy gap              = OPEN / PENDING DECISION

Option A                  = PROPOSED / NOT AUTHORIZED
Option B                  = PROPOSED / NOT AUTHORIZED

Schema mutation           = NOT AUTHORIZED
Source amendment          = NOT AUTHORIZED
Implementation Auth.      = NOT GRANTED
Normative Effect          = NONE

A2 Meta-Validation        = PASS / CLOSED
A2 Overall                = OPEN / REASSESSMENT REQUIRED
M1 Governance             = OPEN / BLOCKED
```

## 8. Disposition

This artifact is suitable for registration as a **NON-CONSTITUTIVE DECISION-GAP RECORD**.

Registration records the existence and boundaries of the unresolved decision. It does not resolve the decision.

**End of Decision Package v1.0**

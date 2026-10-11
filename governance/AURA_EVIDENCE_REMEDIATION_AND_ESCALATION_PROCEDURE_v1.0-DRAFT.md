# AURA — Evidence Remediation and Escalation Procedure

**Artifact ID:** AURA-ERM-001  
**Version:** 1.0-DRAFT  
**Status:** DRAFT · NON-CONSTITUTIVE · NOT RATIFIED  
**Classification:** Governance process proposal / evidence-control procedure  
**Repository of record (proposed):** `vaidt/aura-specification`  
**Normative effect:** NONE  
**Implementation / runtime authorization created:** NO  
**Prepared:** 2026-10-11

---

## 1. Purpose

This procedure proposes a controlled process for registering evidence blockers, requesting remediation, escalating missed deadlines, and recording an explicit disposition. Its purpose is to make evidence remediation trackable without conflating protocol decisions, implementation behavior, gate status, repository permissions, or authorization.

This draft does not itself establish a binding obligation, alter any protocol requirement, grant implementation authority, close any conformance gate, or impose a certification sanction.

## 2. Identity, provenance, and authority boundaries

The current project workspace is `vaidt`, including the proposed record-of-reference repository `vaidt/aura-specification`.

`Aura-IDToken` is treated in this procedure as a historical project attribution and interpretation context. Historical repository names, files, branches, commits, identities, or statements must not be interpreted as automatically equivalent to the current project's authoritative source, nor as automatically invalid. Their relevance must be established through explicit source, provenance, and authority bindings.

The following concepts remain distinct and must not be inferred from one another:

- GitHub account or repository ownership;
- human identity;
- role or office;
- authority-binding record;
- competence and scope for a particular decision;
- normative source and effective status;
- implementation or runtime authorization;
- evidence execution and its result.

Any claim that a historical Aura-IDToken record constitutes current authority must cite the current applicable authority-binding record and establish issuer, holder, scope, effective date, and validity. This draft does not adjudicate that question.

## 3. Governing principles

1. **Evidence states do not ratify protocol decisions.** A technical result cannot create normative effect.
2. **Normative decisions and conformance gates are separate axes.** A settled decision may have an open evidence gate; an open gate does not silently unsettle the decision.
3. **Missing evidence stays missing.** Use explicit statuses such as `UNBOUND`, `NOT-RUN`, `BLOCKED`, `PARTIAL-COVERAGE`, or `CONFLICT`; never infer a pass.
4. **Historical reconstruction is not an original artifact.** Reconstructed data must remain separately identified and cannot be substituted for a lost original corpus without an explicit authorization and provenance record.
5. **Authorization is scope-bound.** Wave 1 authorization applies only to its recorded repository, baseline, branch, and path scope. It must not be extended by analogy to another repository, historical corpus, or runtime campaign.
6. **A deadline cannot change technical truth.** Expiration can trigger escalation and maintain a block; it cannot make an implementation conformant or non-conformant by itself.
7. **No automatic permanent exclusion.** Permanent or campaign-level certification disposition requires a separate, explicit decision by a competent authority under an approved process.

## 4. Evidence remediation register

Each blocker entered into the register SHOULD contain:

| Field | Required content |
|---|---|
| `remediation_id` | Stable identifier |
| `gate_or_binding_id` | Gate / matrix binding, e.g. BM-001 |
| `requirement_ref` | Exact requirement, profile, or decision reference |
| `baseline_ref` | Immutable repository, commit SHA, and artifact/blob digest where available |
| `blocker_statement` | Specific unproven or failed criterion |
| `required_evidence` | Exact deliverables and evidence byte domain |
| `acceptance_criteria` | Objective, testable conditions for acceptance |
| `owner` | Named remediation owner; role alone is insufficient if no individual is assigned |
| `reviewer` | Independent reviewer or explicit `UNASSIGNED` |
| `opened_at` | Timestamp and time zone |
| `due_at` | Approved deadline and time zone, or `NOT-SET` |
| `authorization_ref` | Applicable authorization and scope, or `NOT-GRANTED` |
| `status` | `OPEN`, `IN-REMEDIATION`, `READY-FOR-REVIEW`, `OVERDUE`, `ACCEPTED`, `REJECTED`, or `DISPOSITIONED` |
| `evidence_refs` | Immutable evidence references, logs, digests, and execution identifiers |
| `decision_ref` | Explicit disposition record or `NONE` |

Unknown fields must be marked explicitly; they must not be guessed or left silently blank.

## 5. Proposed remediation clock

The following periods are proposals for approval, not existing binding deadlines:

- **T0 — Registration:** the authorized process owner records the blocker and the baseline.
- **Within 5 business days of a formally issued remediation notice:** the owner supplies a remediation plan, owner assignment, evidence plan, and delivery estimate.
- **Within 10 business days of that notice:** the required evidence package is delivered, or a reasoned extension request is submitted before the due time.
- **At due-time expiry:** if the acceptance criteria have not been met and no valid extension has been approved, the register transitions to `OVERDUE`. The gate remains at its existing `OPEN` / `BLOCKED` disposition.
- **Escalation review:** a competent decision-maker records extension, scope restriction, campaign closure without certification, or another explicitly authorized disposition.

A deadline becomes operative only after the competent authority approves this procedure or an individual notice under an already approved procedure. No clock is considered started merely because this draft was created or published.

For reproducibility, business-day calculations must state the time zone, applicable calendar, start event, and treatment of holidays. The default proposal is Europe/Warsaw, with counting starting on the next business day after the recorded notice; this default requires approval before it is binding.

## 6. Escalation stages

### Stage 1 — Register

Record the blocker, evidence gap, pinned baseline, owner, reviewer, acceptance criteria, authorization boundary, and proposed due date.

### Stage 2 — Issue remediation notice

The competent process owner issues a durable notice identifying required artifacts and objective acceptance conditions. The notice must distinguish required source changes from required evidence production; it must not authorize a change outside an existing scope.

### Stage 3 — Mark overdue and escalate

On expiry, record `OVERDUE`, the missed criterion, current evidence state, and escalation timestamp. Notify the designated decision-maker. The escalation record is administrative and does not alter normative protocol status.

The transition may be automated only after an approved source of truth for deadlines, a deterministic clock rule, access controls, and a durable audit log exist. Until then, `OVERDUE` must be marked by an accountable operator and must not be represented as automated.

### Stage 4 — Record an explicit disposition

A competent decision-maker records one of the following, with rationale and scope:

- **EXTENSION-GRANTED** — new due date, reason, and approval reference;
- **REMEDIATION-ACCEPTED** — evidence passed the stated acceptance criteria after review;
- **SCOPE-RESTRICTED** — the unsupported claim or campaign scope is removed, without misrepresenting the residual status;
- **CAMPAIGN-CLOSED-NO-CERTIFICATION** — this campaign ends without certification;
- **REJECTED** — evidence does not meet the criteria, with precise reasons;
- **OTHER-AUTHORIZED-DISPOSITION** — only where an applicable approved rule permits it.

No outcome may assert permanent ineligibility unless an approved governing instrument explicitly defines that consequence and the competent authority issues the corresponding decision.

## 7. Provisional remediation topics — source verification required

**Evidence status: UNVERIFIED PROPOSALS.** The `BM-001` through `BM-008` identifiers and their associations in this section are carried forward from review context. This pull request does not establish that they are rows in a matrix checked into the base branch, and this procedure does not nominate them as a source of record. Before any item is treated as a verified binding, its owner MUST attach the exact source repository, artifact path, version, immutable commit SHA, and artifact/blob digest, plus the relevant row or section.

Until that source binding is added, the items below are proposed remediation topics only. They must not be used to assert that an external matrix is current, authoritative, or reachable from the checked-in repository.

| Provisional topic | Proposed evidence / action | Acceptance boundary |
|---|---|---|
| **BM-001 / DQ-006 — unverified binding association** | Consider adding and executing a JCS-discriminating vector against the declared RFC 8785 implementations; record exact input, observed canonical bytes, source commits, runner invocations, runtime, logs, and digests. The BM-001 association remains unverified until its source row is immutably bound. | A naive sorted-JSON implementation must not pass the discriminating assertions. Expected bytes must be established through a justified and independently checked oracle, not copied from an unexecuted assumption. DQ-006 itself must be read from its current record of reference; this draft does not close it. |
| **BM-005 — unverified binding association** | Consider binding each `AURA-CANON/1` claim to its exact profile version/digest, implementation commit, fixture bytes, runner, runtime, execution output, and limitations. Verify the source row before treating BM-005 as a controlled identifier. | Product-local profile conformance remains separate from protocol-wide JCS conformance. |
| **BM-004 — unverified binding association** | Consider recording generator source commit, invocation, dependency/runtime bindings, input corpus, generated outputs, raw logs, and all digests; examine schema validity, numeric edge cases, surrogate handling, and manifest digest-domain ambiguity. Verify the source row and corpus authorization before acting on the identifier. | The package must be explicitly classified experimental or authorized for a specified campaign. A reconstructed corpus must never be claimed as the recovered original. Execution is prohibited unless the required campaign authorization is established. |
| **BM-006 — unverified release-provenance concern** | Verify the primary release-manifest file in its own repository and cite its exact repository, path, version, immutable commit SHA, and blob digest before asserting a manifest defect. Any correction must be separately authorized and followed by re-verification. | **No specific `release_control.commit_sha` value is asserted here as a current blocker.** Any value quoted in prior review context remains unverified by this procedure until tied to the primary manifest record. |
| **BM-008 — unverified binding association** | If the cited taxonomy conflict is confirmed in the applicable primary records, propose an explicit authorized disposition with source references and mapping tests. First verify that BM-008 is a controlled identifier in the immutable matrix source. | No silent substitution or normalization of P-008 / APS result vocabularies by this matrix or this procedure. |
| **DQ-006 residuals — source record exists; association requires separate binding** | Consult the current DQ-006 Closure Package in `vaidt/aura-specification` and verify its immutable commit/blob identity before using it in a formal remediation notice. | The current record describes the RFC 8785 decision separately from the still-open evidence / procedural gate. This draft does not close that gate. |

## 8. Required evidence package

Where execution evidence is required, the record should bind at least:

1. full source commit and relevant file/blob digests;
2. exact fixture bytes and digest algorithm/domain;
3. generator source/version and derivation history, where applicable;
4. exact runner path, source digest, command, arguments, and relevant environment;
5. operating system, architecture, runtime/toolchain, dependency lock, and container digest where applicable;
6. unique execution ID, UTC timestamps, exit status, immutable stdout/stderr or logs, output bytes, and output digests;
7. expected-result oracle and its authoritative or independently justified basis;
8. explicit coverage limits and negative-control behavior;
9. independent review record;
10. applicable authorization, its exact scope, and release/manifest binding when a release claim is made.

If any mandatory element is absent, the claim must be downgraded to an evidence status appropriate to the gap; it must not be represented as a fully bound executed result.

## 9. Independence and conflict-of-interest controls

The person producing evidence must not be the sole person accepting it where independent review is required. A reviewer must record identity, decision, date, scope, and immutable reference. If no independent reviewer is assigned, the state remains `READY-FOR-REVIEW` or `BLOCKED`, as applicable.

The procedure itself cannot decide who holds a constitutional role. If authority, holder continuity, or competence is disputed, processing pauses at that decision boundary and the dispute is routed to the applicable authority-binding process. Repository write access is not by itself proof of normative competence.

## 10. Relationship to existing records

This draft is subordinate to current authoritative governance and authorization records. In particular:

- the Governance & Status Index governs selection of current record-of-reference documents;
- the current DQ-006 Closure Package distinguishes the settled RFC 8785 decision from its still-open evidence / procedural closure;
- Wave 1 authorization remains restricted to its expressly listed repository, baseline, and paths;
- the PIBM matrix remains a non-constitutive evidence-control artifact unless separately adopted through the applicable governance process;
- historical Aura-IDToken records remain historical context unless their current role is explicitly established by applicable authoritative records.

If this draft conflicts with a current authoritative record, this draft has no effect and must be revised or rejected; the conflict must not be resolved by silently changing precedence.

## 11. Adoption gates

Before this procedure can be treated as binding:

- [ ] An independent review of the full procedure is recorded.
- [ ] Competent authority for adopting the process is established by the current authority-binding record.
- [ ] The 5-day / 10-day clock and calendar rules are explicitly accepted or replaced.
- [ ] Escalation recipients and their decision scope are named.
- [ ] The meaning and allowed use of `OVERDUE` are approved.
- [ ] The distinction between campaign closure without certification and permanent certification ineligibility is explicit.
- [ ] Automation design, audit logging, permissions, and failure modes are reviewed before enabling automatic transitions.
- [ ] The adopted version is recorded by an explicit constitutive act, separate from this draft.
- [ ] Any implementation authorization cites the exact repository, branch, baseline, and permitted paths.

Until every applicable adoption gate is satisfied by competent action, the status remains:

```text
AURA-ERM-001
Version                 : 1.0-DRAFT
Normative effect        : NONE
Procedure adopted       : NO
Automated enforcement   : NOT-AUTHORIZED
Certification sanction  : NONE CREATED
```

---

*End of non-constitutive draft.*

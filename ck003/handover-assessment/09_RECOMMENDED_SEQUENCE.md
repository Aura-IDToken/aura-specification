# K — Recommended Execution Sequence

**Classification:** EVIDENCE / RECOMMENDATION — NON-NORMATIVE
**Nothing in this document authorises any change. It proposes an order.**

---

## K.1 Why the handover's Priority 0 is superseded

The handover names Priority 0 as *"formal DQ-006 closure package in `aura-specification`"*.

That package already exists and is already merged (`evidence/DQ-006_CLOSURE_PACKAGE.md`, PR
#21). Producing another one would compound the problem rather than address it. What DQ-006
needs is not more closure. It needs its evidence to become reachable, its three contradictory
statuses reduced to one, its governing ADR approved by an authority that exists, and a vector
that actually discriminates RFC 8785.

The sequence below reflects that.

---

## Step 0 — Custodian ruling on cross-corpus precedence  ·  **DECISION REQUIRED**

**Blocks:** everything.

Put CFL-001 to the Protocol Custodian / Chief Architect: which authority ladder governs a
decision that is recorded in the specification corpus and constrains the implementation corpus?

The question is already fully prepared — the core repository's OQ-A package documents the
conflict, the candidate ladders, the missing actors and the missing artifact classes. No further
analysis is needed. What is needed is a person.

**Do not** proceed past this step by picking a ladder. An agent selecting a precedence rule is
precisely the failure mode the D-3 record forbids.

**Deliverable:** one artifact, acknowledged by both corpora, naming the governing ladder and the
approver for the SPEC/APS document class.

---

## Step 1 — Make the DQ-006 evidence reachable  ·  mechanical, no semantics

1. Open pull requests for `claude/cross-language-canonical-001-n4v2c5` in **both**
   `aura-poc-a-core-v3.3` and `aura-guard-v1.3`. These carry the execution and evidence commits
   the closure cites (`49d0e4f`, `3e8e0e3`, `4e9e228`, `420653e`).
2. Dispose of the competing RI-RS attempts (CFL-003). **PR #59 must not be merged as written** —
   it puts `serde_json_canonicalizer` in the production `[dependencies]` of the audit component,
   which the handover lists as frozen-isolated and which its own `JCS_DEPENDENCY_DECISION.md`
   forbids. Close it or rewrite it against the isolated-package form.
3. Once merged, update the closure package's provenance to cite commits reachable from `main`.

This step changes no semantics and closes no gate. It makes the evidence auditable, which is
the minimum condition for anyone to review the claim at all.

---

## Step 2 — Reduce DQ-006 to one status  ·  **human act**

Under `GOVERNANCE.md` §2, status transitions are the Chief Architect's. Three artifacts must end
up consistent: the closure package, `CANONICAL-001_INDEPENDENT_ORACLE.md` (currently BLOCKED),
and `fixtures/corpus/CANONICAL-001_jcs_evidence.json` (currently PENDING_EXECUTION). Whichever
survives, the others get `SUPERSEDED` — a status `ck003/README.md` already defines and nobody
has applied.

This cannot precede Step 0: approving the ADR beneath the closure requires an approver.

---

## Step 3 — Add discriminating cross-language vectors  ·  before DQ-006 means anything

CANONICAL-001 cannot tell RFC 8785 from `json.dumps(sort_keys=True, separators=(",",":"))` —
demonstrated by execution in `10_INDEPENDENT_VERIFICATION.md`. Until at least one vector
separates them, the cross-language result evidences agreement, not conformance.

Candidate discriminators are listed in `10_` §4. They are **candidates**: each must be executed
against both engines and its output recorded, never asserted from the specification text.

Preserve the existing negative-control methodology when extending — independent recomputation of
`SHA-256(bytes)` and `SHA-256(0x00 || bytes)`, plus mutation controls. That pattern is the best
methodological asset the program has.

---

## Step 4 — Populate the event-type registry  ·  after Step 0

DQ-004 cannot close and CONF-012 cannot pass against an empty vocabulary — and today the
registry's own §3 would reject `AUDIT_RECORD`, the token inside the fixture under the closed
gate (CFL-005). Registering tokens is a normative act and needs the approver Step 0 identifies.

---

## Step 5 — Stand up specification CI  ·  mechanical, high leverage

`aura-specification` has no `.github/workflows/` at all. The first workflow does not need to
verify protocol semantics; it needs to verify the things that are currently wrong and unnoticed:

- document-header/status validation
- identifier uniqueness (three files currently claim `ADR-001`)
- link integrity (README points at `aps/APS-001…`, which lives in `specification/`)
- fixture schema validation
- INV→CONF mapping consistency across the three tables that presently disagree

The five scripts `scripts/README.md` already names are the right scope. Also fix
`aura-guard-v1.3/.github/workflows/docker-image.yml`, which cannot succeed (no root
`Dockerfile`).

---

## Step 6 — Resolve the CK003 legacy corpus  ·  classification, not reconstruction

`CK003-001…010` are NOT RECOVERED. Classify each as `LEGACY`, `SUPERSEDED` or `UNRESOLVED` and
record the basis. **Do not reconstruct their content.** A fabricated historical fixture is worse
than a missing one, and the handover is explicit on this point.

---

## Step 7 — Answer ARI-D-001  ·  **DECISION REQUIRED**, and currently invisible

Is ARI protocol content or implementation-defined? Twenty-seven ARI decisions are unanswered,
INV-001 and INV-006 are Critical and depend on the answer, and the only definition in the
specification corpus defines ARI by reference to RI-PY.

This is not on the handover's trajectory. On the evidence it belongs near the top of it: a
protocol whose central measurement is defined by pointing at one implementation cannot have
independent implementations, which is the program's stated objective.

---

## Steps 8+ — Only then

INV matrix closure → canonical fixture corpus → unified conformance runner → CI enforcement
across all three repositories → traceability matrix regeneration → protocol-level threat model →
regulatory mapping → architecture review → freeze → v1.0.

The handover's Gate B/C/D ordering is sound. It is the entry condition that is missing.

---

## K.2 What must not be done in the meantime

- Do not select a canonical encoding, unify RI-PY's three `json.dumps` forms, or change the
  Merkle construction. Each is reserved by D-3 and by the Constitutional Decree's Entropy
  Principle.
- Do not merge PR #59 as written.
- Do not mark DQ-002, DQ-003 or DQ-004 closed on the strength of DQ-006.
- Do not reconstruct missing fixtures.
- Do not record any status as PASS without merged, reachable, executed evidence.

---

*This document proposes an order. It authorises nothing and confers no normative semantics.*

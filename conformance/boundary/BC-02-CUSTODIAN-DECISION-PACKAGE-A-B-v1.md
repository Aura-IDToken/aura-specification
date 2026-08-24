# BC-02 / BC-02.1 — CUSTODIAN DECISION PACKAGE A/B v1

**Document class:** Decision-preparation package. Preparation and routing only —
no decision analysis is resolved, no semantics are selected.
**Prepared by:** Claude, in the architectural/conformance audit role defined by
`CLAUDE.md`. Claude is neither the Protocol Custodian nor an Independent
Reviewer, and **entered no key**.
**Status:** DRAFT / CONTROLLED PREPARATION
**Authority:** NONE · **Conformance authority:** NONE · **Execution authority:** NONE
**Date (UTC):** 2026-08-24

## 0. Disposition summary

| Item | State |
|---|---|
| **Terrain Survey** | **CLOSED — DIAGNOSTICALLY COMPLETE** (§3) |
| **DECISION A** — boundary transfer semantics | **PREPARED — NOT RESOLVED** (§5) |
| **DECISION B** — upstream authority supply | **PREPARED — NOT RESOLVED** (§6) |
| Custodian referrals R-1, R-2 | **RAISED — NOT RESOLVED** (§10) |
| Unrouted residue | **NONE** (§11) |
| S-3 / S-4 / S-5 | OPEN — routed to A-1, A-2, A-3 |
| Registry binding · Issuance authority | UNRESOLVED — routed to B-1, B-3 |
| B-VAL-012 · B-VAL-014 · BNC-1 | NOT EXECUTED |
| CONF-003 §4.5 | NO RESULT |
| Conformance | BLOCKED |
| Normative change | **NONE** |
| Recovery / reconciliation | **NOT OPENED** |

This package **prepares** two decisions and routes them, with everything they
depend on, exclusively to the Protocol Custodian. It resolves neither.

---

## 1. SCOPE AND GOVERNING CONTEXT

### 1.1 Purpose

Review the existing BC-02 / BC-02.1 governance records, normalize their status
vocabulary into one register, close the Terrain Survey diagnostically, and
express the remaining unresolved questions as a formal two-decision package for
the Custodian.

### 1.2 The preparation boundary

Adopted verbatim in substance from the house Two-Key protocol already
established in this programme (`aura-poc-a-core-v3.3` →
`review/2026-08-12_RD1_ARI_DECISION_READINESS/08_TWO_KEY_DECISION_PROTOCOL.md`
§1):

**This package MAY:** discover decision points · classify existing evidence ·
identify candidate semantics · identify consequences · identify dependencies ·
identify evidence requirements · identify contradictions · prepare decision
questions.

**This package MAY NOT:** choose an answer · declare a semantics authoritative ·
convert a candidate into a requirement · create normative fixtures · modify an
implementation to match a candidate · amend a specification · create an
approving ADR.

This package was produced entirely within the first list. Its compliance with
the second is confirmed in §14.

### 1.3 Explicit non-scope

Not performed and not authorized here: resolution of Decision A or Decision B;
modification of BC-02, the BC-02.1 schema (v1 or v2), APS-200, CONF-003, the
P-01 artifact, either receiver implementation, or any existing receipt; creation
of a Registry, an issuance record or a fixture; execution of B-VAL-012,
B-VAL-014, BNC-1…BNC-7, CONF-003 §4.5, N-01…N-08, C1–C8, P-01 as a conformance
case, a controlled re-handoff, or any other conformance procedure.

### 1.4 Authority precedence applied

`CLAUDE.md` precedence governs. Two consequences carry through the package:

1. **BC-02 and BC-02.1 are engineering-layer artifacts.** BC-02 states its own
   classification as *"Engineering Boundary Contract — NON-NORMATIVE"* and
   *"Authority created: **NONE**"*; BC-02.1 v1 and v2 both state *"Normative
   authority: NONE"*. Nothing here promotes them.
2. **Declarations carried by task instructions are level-8 inputs.** Where a
   declaration and the corpus diverge, both are recorded (§2.3) and neither is
   silently preferred.

### 1.5 Sources

This package is a normalization of records already surveyed. It introduces no
new source. The record set is inventoried at §2.1; the underlying per-axis
analysis is `BC-02.1-S3-S4-S5-CONSISTENCY-DETERMINATION-RECORD-v1.md` @
`9bbe7ff`, and the underlying dependency survey is
`BC-02.1-PRE-02-PRE-03-DEPENDENCY-CLOSURE-REPORT-v1.md` @ `5f61e62`.

---

## 2. NORMALIZATION PASS

### 2.1 Record register

Reachability: **M** = on `main` · **F** = feature branch only.
Class: **ENG** engineering contract/schema · **OBS** observation record ·
**EVID** evidence input · **ART** artifact.

| ID | Record | Ref | Reach | Class | Normalized state |
|---|---|---|---|---|---|
| **N-01** | BC-02 — Immutable Fixture Handoff | `e2066bd` | F | ENG | **CONSTRUCTED — NOT VALIDATED**; §17 items 12–14 NOT MET; §19 DEP-001…005 blocking |
| **N-02** | BC-02 Boundary Validation Record | `b90112b` | F | OBS | **BLOCKED** — validation not entered; DEP-001…005 observed OPEN |
| **N-03** | BC-02 Cross-Receiver Pre-Execution Audit | `5f226e6` | M | OBS | **CLOSED** — six gate conditions, B-BLOCK-01 closed at `b86a382` |
| **N-04** | BC-02.1 Common Receipt Schema v1 | `7d1977f` | M | ENG | **CONSTRUCTED**; superseded for new receipts by v2; one digest field |
| **N-05** | BC-02.2 RI-PY Receiver v1 | `d943807` / `b86a382` | M | ENG | **CONSTRUCTED**; `SCHEMA_VERSION = 1` |
| **N-06** | BC-02.3 RI-RS Receiver v1 | `49e848a` | M | ENG | **CONSTRUCTED**; `SCHEMA_VERSION = 1` |
| **N-07** | Controlled P-01 Handoff Record | `927e524` | M | OBS + EVID | **COMPLETE** — evidence-generation event; conformance NOT DETERMINED |
| **N-08** | BC-02 Custodian Closure Record | `68495e0` | M | OBS | **CLOSED AT THE EVIDENCE-GENERATION LAYER** — scoped closure |
| **N-09** | B-VAL-014 Definition Reconciliation Record | `6a76b3e` | M | OBS | **DEFINITION RECONCILED** (BC-02 §14 controlling); execution NOT AUTHORIZED; raises PRE-01/02/03 |
| **N-10** | B-VAL-014 Pre-Execution Contract Binding Record | `31c238b` | F | OBS | **PRE-01 OPEN — OUTCOME B (binding gap)**; gaps G1…G7 |
| **N-11** | BC-02.1 Common Receipt Schema v2 | `f991dbd` | F | ENG | **CONSTRUCTED** — two operands representable; receivers not bound |
| **N-12** | BC-02.1 PRE-01 Schema Correction Record | `f991dbd` / `7b0325c` | F | OBS | **PRE-01 PASS — SCHEMA LAYER ONLY** |
| **N-13** | BC-02.1 PRE-02 / PRE-03 Closure Record | `1301756` | F | OBS | **PRE-02 BLOCKED · PRE-03 BLOCKED** |
| **N-14** | BC-02.1 PRE-02 / PRE-03 Dependency Closure Report v1 | `5f61e62` | F | OBS | **DEPENDENCY CLOSURE INCOMPLETE** — answer NO; four authority blockers |
| **N-15** | BC-02.1 S-3/S-4/S-5 Consistency Determination Record v1 | `9bbe7ff` | F | OBS | **INCOHERENT — CUSTODIAN DECISION REQUIRED**; nine conflicts/gaps |
| **N-16** | `FIX-DIGEST-P01.canonical.json`, blob `b45ffa98…` | `528de0d` | M | ART | **ARTIFACT VERIFIED / ISSUANCE UNPROVEN** |
| **N-17** | Both P-01 receipts + logs + comparison | `927e524` | M | EVID | **VALID v1 RECEIPTS** — evidence inputs, not results |

### 2.2 Normalized status vocabulary

The records use overlapping words for non-identical states. This package fixes
one vocabulary for its own use and maps the historical terms onto it. **No
historical record is rewritten**; the mapping is a reading aid, not a
correction.

| Normalized term | Means | Does **not** mean |
|---|---|---|
| **CONSTRUCTED** | the artifact exists and is internally complete | that any authority has accepted it |
| **ACCEPTED** | an authority competent to do so has accepted it | that its dependencies are discharged |
| **CLOSED-AT-LAYER** | closure scoped to a named layer, layer stated | closure of the work package as a whole |
| **ESTABLISHED** | demonstrated from reachable evidence | declared, asserted, or inherited from an instruction |
| **OPEN** | identified, unmet, closable in principle at this layer | failed |
| **BLOCKED** | unmet and **not** closable at this layer | failed |
| **UNRESOLVED / NOT REACHABLE** | the source cannot be resolved in scope | that it does not exist |
| **UNKNOWN-PRESERVED** | epistemic state that MUST NOT be converted (BC-02 §11.2) | ABSENT, `null`, or PASS |
| **NOT EXECUTED / NO RESULT** | the procedure did not run | that it ran and failed |

Two distinctions are load-bearing and are carried forward verbatim wherever
these states are cited — the second is adopted from the house form already used
for D-3/D-4 in this programme:

> **BLOCKED is not FAIL. NO EXECUTION is not CONFORMANCE FAILURE.**

> **CLOSED — DIAGNOSTICALLY COMPLETE** is **not** equivalent to
> **CLOSED — QUESTION RESOLVED.**

### 2.3 Divergence register — recorded, not repaired

Each row is a divergence between a **declaration** (level 8, or a scoped
statement read out of scope) and the **corpus**. None is reconciled here.

| ID | Subject | Declaration | Corpus | Normalized reading |
|---|---|---|---|---|
| **DIV-01** | BC-02 | `ACCEPTED` (task headers, gate blocks) | N-01 self-states *CONSTRUCTION — NOT VALIDATED*, disposition *BLOCKED — BC-02 CONSTRUCTION GAP*; N-08 closes it *at the evidence-generation layer*; N-09 §1 lists it `CLOSED` | **CONSTRUCTED — NOT VALIDATED**, with a CLOSED-AT-LAYER evidence-generation closure. Contract acceptance: **not evidenced** |
| **DIV-02** | DEP-001…005 | `SATISFIED FOR P-01` (task headers; carried into N-12 §I.2 gate block) | five artifacts record them **OPEN**; no artifact declares closure | **UNKNOWN — NOT REACHABLE**; not converted to satisfied |
| **DIV-03** | P-01 | `ISSUED / IMMUTABLE` | N-14 §S.3: *ARTIFACT VERIFIED / ISSUANCE UNPROVEN*; no issuance record | **Artifact identity ESTABLISHED; issuance UNRESOLVED** |
| **DIV-04** | BC-01 | `ACCEPTED` | no BC-01 artifact resolvable on any ref of any in-scope repository | **UNRESOLVED / NOT REACHABLE** — acceptance has no reachable subject |
| **DIV-05** | PRE-01 | `PASS` (unqualified, in gate blocks) | N-12 §I.1 states the scope explicitly: *"at the schema layer only"*; receivers remain v1 | **PASS — SCHEMA LAYER ONLY** |
| **DIV-06** | B-VAL-014 | one status word used for two objects | N-09 reconciles the **definition**; N-10 blocks the **execution** | Two states, never one: **definition RECONCILED**, **execution BLOCKED** |
| **DIV-07** | PRE-01-010 | `PASS` (N-12) | the same harness later reports `FAIL` (N-14 §R) because a later task's file lies outside PRE-01's authorized path set | **Scope artifact, not a regression**; harness deliberately not edited |

DIV-01…DIV-07 are **not** conflicts between authorities. They are divergences
between what was declared and what is reachable. They are routed to the
Custodian as part of the package context, not as decisions.

---

## 3. TERRAIN SURVEY — DIAGNOSTIC CLOSURE

### 3.1 What the survey covered

All refs of five in-scope repositories (`aura-specification`,
`aura-poc-a-core-v3.3`, `aura-guard-v1.3`, `.github`, `cargo`), read-only: the
BC-02 chain contracts and schemas, every boundary governance record, the P-01
artifact and its evidence, both receiver implementations and adapters, and the
reachable normative corpus (Constitution, APS-000…950, CONF-001…015).

### 3.2 What the survey established

| # | Established | Basis |
|---|---|---|
| **T-1** | The P-01 artifact exists, is reachable, and its content identity and exact octets are verifiable: 15 octets, `7b22…227d`, SHA-256 `ecf9e98e…d4e65667`, blob `b45ffa98…` | N-14 §I.1; N-15 §D.1 |
| **T-2** | A real handoff occurred and was recorded: two independent receivers, two independent digest computations, full receiver/implementation/adapter/environment provenance, no result-authority field in either receipt | N-07; N-17 |
| **T-3** | Both receivers emit `SCHEMA_VERSION = 1`, which carries **one** digest field where B-VAL-014 requires two operands | N-04; N-13 §L.1 |
| **T-4** | BC-02.1 v2 makes the two operands representable, with per-operand source material, calculation path and provenance, and prohibits aliasing | N-11; N-12 |
| **T-5** | Four sources BC-02 declares as consumed authorities are not reachable on any ref: the Fixture Registry, Boundary Specification v1, Core Interface Spec v1, BC-01 — as is any P-01 issuance record | N-14 §B.1, §C.4 of N-15 |
| **T-6** | No fixture in any reachable commit carries `raw_input` or `raw_input_encoding`; the P-01 artifact carries fields `a` and `b` only | N-14 §F; N-15 §E.1 |
| **T-7** | BC-02 §5.3, §7.1, §14 and §15.3 are not jointly satisfiable without determining which value one operand carries | N-14 §L.4; N-15 §F.5 |
| **T-8** | The S-3/S-4/S-5 vocabulary appears nowhere in APS-400 / APS-300 / APS-100 — it is engineering-layer only | N-15 §C.5 |
| **T-9** | The executed handoff was a single shared repository read, not delivery from a sealed store down two independent paths | N-15 §D.2 |
| **T-10** | Every load-bearing artifact of the BC-02 chain is branch-local; `main` does not carry the contract its records cite | N-14 §O; N-15 GAP-09 |

### 3.3 What the survey did **not** establish

| # | Not established | Consequence |
|---|---|---|
| **U-1** | That an issuance event occurred over the P-01 octets, or who could have performed it | Top two rows of the BC-02 §5.5 chain have no artifact behind them |
| **U-2** | That any storage in use satisfies §6.4 write-denial | Seal property undecided |
| **U-3** | Whether the artifact octets are the input segment | S-3 binding undeclared |
| **U-4** | Which value `input_segment_sha256` carries | S-4 provenance undeclared |
| **U-5** | Any value or rule for `fixture_hash` | B-VAL-012's first conjunct unbound; UNKNOWN-PRESERVED |
| **U-6** | That the Registry, BC-01, Boundary Spec v1 or Core Interface Spec v1 do not exist | Their absence is a **reachability** finding only |

### 3.4 Closure statement

```text
TERRAIN SURVEY:  CLOSED — DIAGNOSTICALLY COMPLETE
```

The survey is closed because it has reached its diagnostic limit, not because
its questions are answered. Every further step depends on a determination or an
authority act that no amount of additional surveying can supply: re-surveying
cannot produce a Registry, cannot produce an issuer, and cannot choose between
two readings of a contract sentence.

**Diagnostic completeness means:** every open question has been located, bound
to an exact source, classified by the layer competent to answer it, and routed.
It does **not** mean any question is resolved, and it does not license entry to
any gate.

Nothing further is asked of the survey. The remaining questions are the content
of §5, §6 and §10.

---

## 4. DERIVATION OF THE A/B PARTITION

### 4.1 Basis

The partition is not invented for this package; it reproduces a distinction the
corpus already draws. N-14 §S.1 separates its four blockers into authority-level
items (Registry, `fixture_hash` rule, issuer) and one contract-interpretation
item; §S.2 prices S-3/S-4/S-5 as *"Low — interpretation of existing text"*
against S-1/S-2/S-6 as authority artifacts and acts. N-15 §N.3 records the
incoherence as being of exactly two kinds: missing upstream authority, and
internal non-joint-satisfiability.

```text
DECISION A   questions answerable by ruling on text that already exists.
             No new artifact is required. Answering them changes no authority.

DECISION B   questions not answerable by any ruling, because the material
             they need does not exist in scope. Answering them requires an
             authority to supply an artifact or perform an act.
```

The two are **independent in kind and coupled in effect**: A can be answered
without B, B can be discharged without A, and no execution path exists until
both are settled (§7).

### 4.2 Status of the labelling

Assigning the labels **A** and **B**, and sorting nine previously recorded
questions into them, is a **packaging act performed by this record**. It creates
no authority, changes no question's content, and does not rank the questions.
Each routed question below carries its originating identifier so the packaging
can be undone by inspection. The Custodian may repartition freely.

---

## 5. DECISION A — BOUNDARY TRANSFER SEMANTICS

**Class:** interpretation of existing text · **Artifact required:** none ·
**State:** PREPARED — NOT RESOLVED

### 5.1 Register

| ID | Question | Exact locus | Origin |
|---|---|---|---|
| **A-1** | For an artifact-only fixture with no `raw_input` field, are the artifact octets the input segment under `raw_input_encoding = identity`, or does §6.3's FIXTURE GAP clause apply and the handoff be refused? | BC-02 §5.3, §6.1, §6.3 @ `e2066bd` | PRE-01-G7 (N-10 §9); N-14 §N.4; N-15 CG-1 |
| **A-2** | Does `raw_input_reference.input_segment_sha256` carry the issuer-sealed value or the receiver's recomputation — and under the answer, how is §15.3's *"MUST be caught by B-VAL-014"* satisfied? | BC-02 §5.3 vs §7.1, read against §14 and §15.3 @ `e2066bd` | N-14 §L.4; N-15 CONFLICT-01, CG-2 |
| **A-3** | What constitutes §6.4 write-denied storage for a git-resident artifact, and what satisfies §15.2 step 5's delivery from the sealed store down two independent paths? | BC-02 §6.4, §15.2 step 5, §15.1 VE-05 @ `e2066bd` | N-14 §I.6, §M.5; N-15 CONFLICT-03, CG-3 |
| **A-4** | Which definition of `fixture_artifact_identity` governs at this boundary — the issuer-computed SHA-256, or the artifact label — and how are the two executed v1 receipts read under the answer? | BC-02 §5.2, §7.1 vs BC-02.1 v1 §4; values in both receipts @ `927e524`; BC-02.1 v2 §4, §4.1 | PRE-01-G3 (N-10 §12.1); N-15 CONFLICT-02, CG-6 |
| **A-5** | Does BC-02.1 supersede `BoundaryHandoffRecord` as the B-VAL-014 evidence representation, or must a `BoundaryHandoffRecord` be produced? | BC-02 §7.1, §14 vs BC-02.1 v2 §14.2 (row: *NOT BOUND*) | N-10 §15; N-15 CONFLICT-05, CG-7 |

### 5.2 Candidates and consequences

Candidates are stated as the sources state them. **No candidate is preferred,
recommended, or scored by this package.**

**A-1**

| Candidate | Source position | Consequence if selected |
|---|---|---|
| **A-1-α** — reading (a): the artifact has no `raw_input`; §6.3's FIXTURE GAP clause applies | Direct application of existing §6.3 text; BC-02 states the boundary *"MUST refuse the handoff"* with `HANDOFF_REJECTED` / `ENCODING_INVALID` | No P-01 re-handoff is admissible; DEP-003 / VE-03 remain unmet by P-01; a conforming fixture must come from B-1 |
| **A-1-β** — reading (b): the artifact **is** the `raw_input` under `identity`, so artifact ≡ input segment | Not stated by §6.3, which operates on a `raw_input` field; adding the degenerate case extends the contract | Handoff admissible; `raw_input_encoding = identity` for P-01; and, combined with A-2-α, B-VAL-014 degenerates per §K of N-15 |

**A-2**

| Candidate | Source position | Consequence if selected |
|---|---|---|
| **A-2-α** — receiver-recomputed | BC-02 §7.1 inline: *"RECOMPUTED BY THIS RECEIVER"*; implemented by both receivers; BC-02.1 v2 marks both operands `RECEIVER_RECOMPUTED` | With an already-decoded intake buffer (§8), both operands digest the same buffer per side; B-VAL-014 holds by construction on a corrupted side, so §15.3's acceptance criterion for BNC-1 needs a separate disposition |
| **A-2-β** — issuer-sealed | BC-02 §5.3: *"computed once by the issuer at seal time"*; §7.1 carries `matches_issued_digest` | B-VAL-014 regains discriminating power and catches BNC-1 as §15.3 requires; requires an issuer-side value, hence **depends on B-3**; contradicts §7.1's own inline annotation, which would need disposition. BC-02.1 v2's `EXTERNALLY_SUPPLIED` source can carry it without schema redesign |

**A-3**

| Candidate | Source position | Consequence if selected |
|---|---|---|
| **A-3-α** — the committed content-addressed blob is the sealed artifact; the worktree path is a materialisation of it | §6.4 admits a *"content-addressed store"*; the blob cannot be changed in place | Seal property satisfiable without new storage; the two-path delivery of §15.2 step 5 still requires a delivery construction, since the observed handoff was one shared read (T-9) |
| **A-3-β** — an external write-denied store is required | §6.4 requires storage *"the boundary cannot write to"*, enforced *"structurally, not by convention"*; the path actually read is writable | Requires the issuance store to be separated from both implementation trees, which also disposes of VE-05 and the B-VAL-019 falsifiability observation; engineering work, separately authorized |

**A-4**

| Candidate | Consequence if selected |
|---|---|
| **A-4-α** — the BC-02 §5.2 digest definition governs | Both executed v1 receipts carry a name in the identity field and are, under that reading, not identity-bearing for B-VAL-013; their disposition (recorded-as-is vs superseded by a future v2 receipt) must be stated in the same ruling |
| **A-4-β** — the BC-02.1 v1 §4 label definition governs at this boundary | B-VAL-013's comparison is over filenames; BC-02.1 v2 §4, which rejects a non-digest identity, would need reconciling |

**A-5**

| Candidate | Consequence if selected |
|---|---|
| **A-5-α** — BC-02.1 supersedes `BoundaryHandoffRecord` for B-VAL-014 | The v2 field bindings in §14.2 become the evidence vocabulary; the rows v2 marks *NOT BOUND* (`fixture_hash`) remain open under B-2 |
| **A-5-β** — `BoundaryHandoffRecord` must be produced | A record form no implementation emits becomes a construction requirement, additional to the v2 receiver binding |

### 5.3 What Decision A does not reach

A resolves no dependency of Decision B, closes no DEP item, issues nothing, and
by itself authorizes no execution.

---

## 6. DECISION B — UPSTREAM AUTHORITY SUPPLY

**Class:** authority artifact / authority act · **Interpretation cannot
substitute** · **State:** PREPARED — NOT RESOLVED

### 6.1 Register

| ID | Question | Exact locus | Origin |
|---|---|---|---|
| **B-1** | Is `CONFORMANCE_FIXTURE_REGISTRY_v1` supplied with its §4.2 field mapping, or is BC-02 declared unenterable without it — and does APS-500 stand in any relation to it? | BC-02 §4.1, §4.2, §15.1 VE-01 @ `e2066bd`; APS-500 @ `main` | DEP-001; N-14 §D, §J; N-15 CG-4 |
| **B-2** | Is the `fixture_hash` rule declared — covered octets and encoding — or is the verification limb declared permanently UNKNOWN, and if so where is that UNKNOWN recorded given v1 has no presence tag and v2 restricts `UnresolvedValue` to `issuance_id`? | BC-02 §5.4, §11.4, VE-02; BC-02.1 v1 §10, v2 §10.2 | DEP-002; PRE-01-G5; N-15 GAP-07, CG-4/CG-6 |
| **B-3** | Who is the issuing authority, and is an issuance event over the existing octets authorized — producing `issuance_id` and the issuer-computed values §5.3 and §7.1 require? | BC-02 §5.3, §5.5, §7.1, §15.2 steps 1–3 | DEP-001/003; N-14 §I.5, §S.1.3; N-15 CG-5 |

### 6.2 Candidates and consequences

**B-1**

| Candidate | Consequence if selected |
|---|---|
| **B-1-α** — supply the Registry contract | VE-01 dischargeable; B-VAL-011's `Registry.fixture_id` term and B-VAL-012's `fixture_hash` conjunct become bindable |
| **B-1-β** — declare BC-02 unenterable without it | The BC-02 chain terminates at construction; no boundary validation is entered, and the question of P-01 conformance does not arise at this layer |
| **B-1-γ** — bind an existing normative artifact (APS-500) as the Registry | APS-500 is reachable and normative (Status: DRAFT), but its field set does not intersect BC-02 §4.2 on any load-bearing element — no `fixture_hash`, no `raw_input`, no issuance concept, and its canonical fixture data is marked TODO. Selecting this requires declaring the missing fields, i.e. it collapses into B-1-α in substance |

**B-2**

| Candidate | Consequence if selected |
|---|---|
| **B-2-α** — declare the rule | VE-02 dischargeable; `fixture_hash_verification` becomes evaluable |
| **B-2-β** — declare the limb permanently UNKNOWN | UNKNOWN must be **preserved, never converted** (§11.2); a representation for it must be named, since neither schema version can currently carry it — this is the subordinate item GAP-07 |

**B-3**

| Candidate | Consequence if selected |
|---|---|
| **B-3-α** — name the issuer and authorize an issuance over the existing octets | The top of the §5.5 chain gains an artifact; `issuance_id` becomes bindable; enables A-2-β; issues **the octets that already exist** — no replacement fixture |
| **B-3-β** — decline to authorize | `issuance_id` remains UNKNOWN-PRESERVED; A-2-β is unavailable; B-VAL-013's issuance limb stays unbound |

**Refused in both directions, and not a candidate:** authoring an issuance
record at this layer. It would either attest to an event that did not happen or
exercise issuing authority this package does not hold. Equally, absence of a
reachable issuance record is **not** recorded as proof that no issuance
occurred (U-6).

---

## 7. CONSEQUENCE MATRIX — A × B

Consequences only. No cell is recommended.

| | **B settled — authority supplied (B-1-α/γ + B-2-α + B-3-α)** | **B settled — authority withheld (B-1-β, or B-3-β)** |
|---|---|---|
| **A settled toward transfer (A-1-β + A-2-β + A-3 either)** | All identified blockers dispositioned; the remaining items are engineering under separate authorization: v2 receiver binding, delivery construction, then a §15 execution mandate | A-2-β is unavailable without an issuer; A would need re-answering at A-2-α, and the §15.3 disposition returns |
| **A settled toward refusal (A-1-α)** | P-01 is not the vehicle; a Registry-issued fixture carrying `raw_input` octet-exactly is required before any handoff | The BC-02 chain terminates at construction; no boundary validation is entered |
| **A unsettled** | Receiver binding cannot be completed correctly: `raw_input_encoding` and the artifact/segment relation are inputs to it | No path; both kinds of incoherence stand |

The single invariant across the matrix: **no cell permits execution without both
A and B settled**, and no cell is reachable by construction at this layer.

---

## 8. DEPENDENCY GRAPH

```text
        DECISION A                                DECISION B
   (rulings over existing text)          (authority artifacts / acts)

   A-1 artifact ≡ segment ?               B-1 Registry contract
        │                                      │
        ├──────────────┐                       ├── VE-01, VE-02
        ▼              ▼                       ▼
   raw_input_encoding  admissibility of    B-2 fixture_hash rule
   value for P-01      any P-01 handoff         │
        │                                      └── GAP-07 UNKNOWN representation
        ▼                                           (subordinate)
   A-2 which value input_segment_sha256 carries
        │                    ▲
        │                    └──────────────  B-3 issuer identity + issuance act
        ▼                                          │
   BNC-1 acceptance criterion coherence            ├── issuance_id  → B-VAL-013 limb
        │                                          └── enables A-2-β
        ▼
   A-5 evidence representation (BoundaryReceipt vs BoundaryHandoffRecord)
        │
        ▼
   GAP-08  v2 receiver binding        ← requires A-1 and A-2 answered first
        │                               (N-13 §L.3: cannot be completed correctly otherwise)
        ▼
   A-3 sealed store + two delivery paths
        │
        ├── VE-05 · B-VAL-019 falsifiability
        ▼
   §15 execution mandate  →  B-VAL-012 · B-VAL-014 · BNC-1  →  §15.4 report

   A-4 fixture_artifact_identity type  →  B-VAL-013 semantics; disposition of the
                                          two executed v1 receipts
```

Two orderings are forced by the sources and are stated as observations, not as a
plan: A-1 and A-2 precede any receiver binding (N-13 §L.3); A-3 precedes any
delivery construction (N-14 §M.5).

---

## 9. EVIDENCE REQUIREMENTS

What would close each item. Listing these is not a request to produce them.

| Item | Closing evidence |
|---|---|
| A-1 | A Custodian ruling naming reading (a) or (b), and stating the `raw_input_encoding` value for artifact-only fixtures under the answer |
| A-2 | A Custodian ruling naming the operand's source, **and** a statement of how §15.3's *"caught by B-VAL-014"* is satisfied under it |
| A-3 | A Custodian ruling on §6.4 for a git-resident artifact, and on what constitutes two independent delivery paths under §15.2 step 5 |
| A-4 | A Custodian ruling naming the governing definition, and the disposition of the two executed v1 receipts under it |
| A-5 | A Custodian statement that BC-02.1 supersedes `BoundaryHandoffRecord` for B-VAL-014, or that it does not |
| B-1 | The Registry contract artifact: identity, version, entry schema, §4.2 field set — or a declaration of unenterability |
| B-2 | A declaration of the covered octets and encoding — or a declaration of permanent UNKNOWN together with the representation that carries it |
| B-3 | A named issuing authority and an issuance record over blob `b45ffa98…`, carrying `issuance_id` and issuer-computed values — or a declination |
| GAP-08 | A separate construction authorization naming the seven files enumerated at N-13 §L.4 |
| §15 execution | A separate execution mandate, not derivable from any of the above |

---

## 10. CUSTODIAN REFERRALS — NEITHER A NOR B

Two items are neither transfer semantics nor upstream supply. They are routed
separately so they are not absorbed into a decision they do not belong to.

| ID | Referral | Locus | State |
|---|---|---|---|
| **R-1** | CONF-003 §4.5 prohibits accepting *"any form listed in APS-200 §8.4"*; APS-200 has a §8 and **no §8.4** in the reachable text. §4.5's prohibited-input set is therefore unresolvable as written — independently of BC-02, and at the normative layer, which this package does not touch | `conformance/CONF-003_CANONICAL_SERIALIZATION.md` §4.5 vs `aps/APS-200_CANONICAL_DATA_MODEL.md` §8, both on `main` @ `528de0d` | **RAISED** — previously noted as `BC-02-OBS-006` and deferred to a separate reference-repair authorization |
| **R-2** | Every load-bearing artifact of the BC-02 chain is branch-local: the BC-02 contract, the boundary validation record, the pre-execution binding record, BC-02.1 v2 and the PRE-01/02/03 records are not on `main`. An auditor working from `main` cannot read the definitions of B-VAL-014, BNC-1, VE-01…05 or DEP-001…005 | §2.1 refs; N-14 §O | **RAISED** — integration/auditability, no semantic content |

**This package is itself subject to R-2.** It is written on a feature branch and
adds one more branch-local record to the chain it describes.

---

## 11. OPEN QUESTIONS — ROUTING COMPLETENESS

Every question carried by the record set is routed. Nothing is left unassigned,
and nothing is closed by assignment.

| Origin | Question | Routed to |
|---|---|---|
| PRE-01-G1 | two operands collapsed into one field | **closed at schema layer** by N-11/N-12; execution binding → GAP-08 |
| PRE-01-G2 | `receipt_digest_source` representation | **closed at schema layer** by N-11 §6.2 |
| PRE-01-G3 | `fixture_artifact_identity` type | **A-4** |
| PRE-01-G4 | `issuance_id` representation | **B-3** (representation exists in v2 §10; the *value* is the open item) |
| PRE-01-G5 | `fixture_hash` UNKNOWN representation | **B-2** (subordinate GAP-07) |
| PRE-01-G6 | `raw_input_encoding` for P-01 | **A-1** |
| PRE-01-G7 | artifact / input-segment boundary | **A-1** |
| DEP-001 | Registry contract | **B-1** |
| DEP-002 | `fixture_hash` rule | **B-2** |
| DEP-003 | octet-exact fixture input | **A-1** (admissibility) + **B-1** (supply) |
| DEP-004 | Boundary Spec v1, Core Interface Spec v1, BC-01 | **B-1** (same consumed-authority class; named explicitly so it is not lost) |
| DEP-005 | `input_characterization` vocabulary | **B-1**; affects B-VAL-015 only |
| VE-01…VE-05 | §15.1 preconditions | VE-01/02 → **B-1/B-2**; VE-03 → **A-1** + **B-1**; VE-04 → **B-1**; VE-05 → **A-3** |
| PRE-02 / BNC-1 | negative control | **A-2** for criterion coherence; execution → §15 mandate. Not closable before execution |
| PRE-03 | Registry / issuance binding | **B-1** + **B-3** |
| CONFLICT-01 | §5.3 vs §7.1 joint-satisfiability | **A-2** |
| CONFLICT-02 | identity type | **A-4** |
| CONFLICT-03 | VE-05 / delivery arrangement | **A-3** |
| CONFLICT-04 | declaration vs corpus | **§2.3 DIV-02/03/04**, context — not a decision |
| CONFLICT-05 | evidence representation | **A-5** |
| CONFLICT-06 | §4.5 → APS-200 §8.4 | **R-1** |
| GAP-07 | UNKNOWN representation | **B-2** |
| GAP-08 | v2 receiver binding | separate construction authorization; gated on **A-1**, **A-2** |
| GAP-09 | branch-local reachability | **R-2** |

**Unrouted residue: NONE.**

---

## 12. DECISION BRIEF

One page for the Custodian.

**The situation.** A real handoff of a real artifact was executed and recorded,
and its evidence is sound as far as it goes: two independent receivers, two
independent digest computations, agreeing on 15 octets. What is unresolved is
not the evidence but the **frame** in which it would count as transfer evidence.

**Why it cannot be resolved below.** Two irreducible reasons, and they are of
different kinds:

- **Decision A** — four contract sentences (BC-02 §5.3, §7.1, §14, §15.3) cannot
  all hold at once. No artifact supplies what is missing; a reading must be
  chosen. Choosing it below the Custodian would resolve a contract question by
  implementation convenience — the specific error the reconciliation record
  N-09 §16.1 was written to prevent.
- **Decision B** — the Fixture Registry is a *consumed authority*: BC-02 depends
  on it from outside itself and states it *"does not invent Registry fields"*.
  A downstream package that authored it would supply its own inputs and then
  validate against them. Issuance is the same class: it requires an issuer.

**What is being asked.** Eight rulings, sorted into two decisions, plus two
referrals that belong to neither. Five of the eight (A-1…A-5) require no new
artifact — they are rulings over text that already exists. Three (B-1…B-3)
require an artifact or an act.

**What is not being asked.** No execution, no authorization, no construction,
and no ratification of this package's own partition, which the Custodian may
discard.

**What happens if nothing is decided.** The state is stable and safe: BLOCKED,
not FAIL. No conformance claim exists, none is implied, and no evidence decays.
The cost of deferral is that the v2 receiver binding cannot be completed
correctly in the meantime (N-13 §L.3), so no further boundary evidence can be
produced.

---

## 13. CUSTODIAN GATE

### 13.1 Routing

This package is routed **exclusively to the Protocol Custodian**. No part of it
is routed to an implementation task, a construction task, or an execution
mandate, and no part of it may be actioned by inference from its own contents.

### 13.2 Keys

Mirroring the house protocol (`08_TWO_KEY_DECISION_PROTOCOL.md` §2):

| Key | Holder | Status for A / B |
|---|---|---|
| **KEY 1** | Protocol Custodian / Human Architectural Authority | **NOT ENTERED** |
| **KEY 2** | Independent architectural review | **NOT ENTERED** |
| **Gate** | — | **NOT PASSED** |

Claude prepared this package and **entered no key**. Until both keys accept a
resolution, nothing may be formalized for A or B — not a specification, not an
ADR, not a fixture, not a conformance test, not an implementation change.

### 13.3 Gate state

```text
Terrain Survey                  CLOSED — DIAGNOSTICALLY COMPLETE
Controlled Environment          OPEN / READ-CONSTRUCT ONLY

DECISION A                      PREPARED — NOT RESOLVED
DECISION B                      PREPARED — NOT RESOLVED
Referrals R-1, R-2              RAISED — NOT RESOLVED

S-3 / S-4 / S-5                 OPEN
Registry                        UNRESOLVED
Issuance                        UNRESOLVED

B-VAL-012                       NOT EXECUTED
B-VAL-014                       NOT EXECUTED
BNC-1                           NOT EXECUTED
CONF-003 §4.5                   NO RESULT
CONFORMANCE                     BLOCKED

NEXT AUTHORIZED ACTION:
NONE. Custodian consideration of Decision A and Decision B.
No execution of any kind is authorized by this package.
```

---

## 14. FIREWALL CONFIRMATION

| Item | Confirmation |
|---|---|
| Decision A resolved | **NO** — candidates recorded, none selected |
| Decision B resolved | **NO** — candidates recorded, none selected |
| Any candidate recommended, preferred or scored | **NO** |
| BC-02 modified | **NO** |
| BC-02.1 schema modified (v1 or v2) | **NO** |
| APS-200 modified | **NO** |
| CONF-003 modified | **NO** |
| P-01 artifact modified | **NO** |
| Receiver implementations modified | **NO** — RI-PY and RI-RS untouched, both remain `SCHEMA_VERSION = 1` |
| Existing receipts modified or rewritten | **NO** |
| Registry created | **NO** |
| Issuance record created | **NO** |
| Fixture created | **NO** |
| B-VAL-012 executed | **NO** |
| B-VAL-014 executed | **NO** |
| BNC-1…BNC-7 executed, or any corrupted copy created | **NO** |
| CONF-003 §4.5 executed | **NO** |
| N-01…N-08, C1–C8, P-01 as a conformance case, re-handoff | **NO** |
| Historical record rewritten or status retro-corrected | **NO** — §2.2 maps vocabulary, §2.3 records divergences, neither repairs |
| UNKNOWN upgraded without evidence | **NO** — DIV-02, DIV-03, U-1…U-6 preserved |
| Unreachable source recorded as non-existent | **NO** — U-6 |
| Normative decision manufactured | **NO** |
| Authority created | **NONE** |
| Existing file modified or deleted | **NO** — one new file |
| `main` modified, branch merged, PR opened | **NO** |
| Recovery / reconciliation gate opened | **NO** |

---

## Record provenance

| Field | Value |
|---|---|
| Repository | `Aura-IDToken/aura-specification` |
| Branch | `claude/bc-02-1-consistency-analysis-8ewd0q` |
| Path | `conformance/boundary/BC-02-CUSTODIAN-DECISION-PACKAGE-A-B-v1.md` |
| Files added | 1 (this file) |
| Files modified | 0 |
| Files deleted | 0 |
| Execution performed | **NO** |
| Keys entered | **NONE** |
| Authority created | **NONE** |
| Reachability | feature branch only — subject to R-2 |

# B-VAL-014 — DEFINITION RECONCILIATION RECORD

## 1. Status

**Definition reconciliation: COMPLETE.**
**B-VAL-014: NOT EXECUTED.**
**B-VAL-014 execution: NOT AUTHORIZED BY THIS RECORD.**

Governance record. Non-normative. Creates no execution authority, alters no
recorded verdict, and determines no conformance.

| Item | State |
|---|---|
| B-VAL-014 | NOT EXECUTED |
| CONF-003 §4.5 | NO RESULT |
| Protocol conformance | NOT DETERMINED |
| BC-02 | CLOSED |
| Controlled P-01 Handoff | COMPLETE |
| Custodian closure | COMPLETE |

## 2. Purpose

Resolve the conflict between two historically recorded definitions of B-VAL-014
before any authorization of its execution, and fix the current custodian
interpretation without rewriting either historical definition.

## 3. Evidence reviewed

Every finding below is bound to a named artifact, section, or commit. No source
was replaced by general interpretation.

| Artifact | Location | Sections read |
|---|---|---|
| BC-02 contract — Immutable Fixture Handoff | `conformance/boundary/BC-02_IMMUTABLE_FIXTURE_HANDOFF.md` @ `e2066bd` (branch `claude/bc-02-immutable-fixture-handoff-3s3fkp`) | §13.2, §14, §14.1, §14.2, §15.3, §15.4 |
| BC-02 Boundary Validation Record | `conformance/boundary/BC-02_BOUNDARY_VALIDATION_RECORD.md` @ `b90112b` (branch `claude/bc-02-boundary-validation-q0h7yg`) | §5.1, §5.3, §5.4 |
| BC-02.1 Common Receipt Schema v1 | `conformance/boundary/BC-02.1-COMMON-RECEIPT-SCHEMA-v1.md` @ `7d1977f` | §3, §6, §12, §15 |
| Cross-receiver pre-execution audit | `conformance/boundary/BC-02-CROSS-RECEIVER-PREEXEC-AUDIT.md` @ `5f226e6` | whole |
| Controlled P-01 Handoff record | `conformance/boundary/CONTROLLED-P01-HANDOFF-RECORD.md` @ `927e524` | whole |
| Custodian closure record | `conformance/boundary/BC-02-CUSTODIAN-CLOSURE-RECORD.md` @ `68495e0` | whole |
| Executed P-01 receipts | `evidence/controlled-p01-handoff/RI-{PY,RS}-P01-RECEIPT.json` @ `927e524` | full field set |

### 3.1 Sources sought and not found

| Source | Result |
|---|---|
| `CUSTODIAN-NORMATIVE-DECISION-REGISTER` | **Does not exist.** Searched every ref of all five in-scope repositories for `decision-register`, `NORMATIVE-DECISION`, `DECISION_REGISTER`. Zero hits. No custodian decision on B-VAL-014 pre-exists this record. |
| Specification completion / validation matrices containing B-VAL-014 | **None exist.** Searched every ref for files matching `matri`/`completion`/`register` that mention `B-VAL-01`. Zero hits. |
| Any other artifact defining B-VAL-014 | **None.** Only two artifacts define it; every other mention is a citation, a status line, or a non-execution statement. |

## 4. Historical definitions

### 4.1 Definition A — accepted BC-02 contract, §14

Verbatim row from `BC-02_IMMUTABLE_FIXTURE_HANDOFF.md` §14:

| ID | Assertion | Formal condition | Evidence class |
|---|---|---|---|
| **B-VAL-014** | Raw input preserved | `receipt.receipt_digest == input_segment_sha256` on **both** sides, with `receipt_digest_source == RECEIVER_RECOMPUTED`; and `raw_input_encoding ∈ {identity, base64, base16}` | **Transfer evidence** |

Provenance: BC-02 contract, version 1.0-CONSTRUCTION, dated 2026-08-23, commit
`e2066bd`. §14 heading is *"Validation assertions B-VAL-011 … B-VAL-020"* and
opens: *"Engineering validation assertions. **Not** P-01, **not** N-01 … N-08,
**not** CONF-003 §4.5, **not** conformance results, **not** certification
evidence."*

### 4.2 Definition B — earlier receiver-side twelve-limb formulation

Provenance: a task instruction, recorded — not authored — in
`BC-02_BOUNDARY_VALIDATION_RECORD.md` §5.4, commit `b90112b`. The twelve limbs
as recorded:

| # | Limb |
|---|---|
| 1 | RI-PY actually received the issued artifact |
| 2 | RI-RS actually received the issued artifact |
| 3 | fixture identity preserved |
| 4 | received byte length is 15 on both sides |
| 5 | raw bytes demonstrably identical to the issued artifact |
| 6 | SHA256(PY buffer) equals expected artifact hash |
| 7 | SHA256(RS buffer) equals expected artifact hash |
| 8 | SHA256(PY buffer) == SHA256(RS buffer) |
| 9 | receiver identities recorded |
| 10 | source identities recorded |
| 11 | handoff provenance recorded |
| 12 | no reconstruction occurred |

That record's §5.1 already characterised the relationship, at the time:

> *"The instruction restates B-VAL-014 as a twelve-limb "receiver-side octet
> verification" that also absorbs B-VAL-011, B-VAL-012, B-VAL-013 and
> B-VAL-019. The contract definition governs."*

So the conflict was identified and reported at `b90112b`, and left for custodian
resolution. This record supplies that resolution.

## 5. BC-02 §14 baseline

The contract's own commentary settles the substantive question. §14.1, verbatim:

> *"The evidence that the same octets arrived is B-VAL-012 together with
> B-VAL-014: two digests, each recomputed by a different receiver over the
> buffer that receiver actually holds, found equal."*

and:

> *"This distinction is deliberate and MUST NOT be flattened in any downstream
> summary. Recording B-VAL-013 as proof of transfer would reproduce, at the
> engineering layer, exactly the error CONF-003 §5 warns against: 'Two
> implementations agreeing on a digest they both read from the same file
> demonstrates nothing.'"*

Two consequences follow directly from the contract text, without interpretation:

1. B-VAL-012 and B-VAL-014 are **two assertions acting together**, not one
   assertion absorbing the other.
2. Flattening B-VAL-013 into transfer evidence is **expressly prohibited** by
   the contract itself.

§14 assigns each assertion its own evidence class — Label equality, Transfer
evidence, Traceability, Structural evidence, Metadata integrity, Firewall
evidence, Immutability, Layer separation, Determinism. A merged twelve-limb
assertion would destroy that classification.

## 6. Conflict analysis

| Dimension | Definition A (BC-02 §14) | Definition B (twelve-limb) |
|---|---|---|
| Authority level, per `CLAUDE.md` | Level 5 — approved Conformance Requirements | Level 8 — prompt/task instructions |
| Artifact type | Accepted engineering contract | Task instruction, quoted inside a record |
| Scope | One assertion: raw input preserved | Five assertions merged |
| Evidence classification | Preserved per assertion | Collapsed into one verdict |
| Treatment of B-VAL-013 | Traceability, explicitly *not* transfer evidence (§14.1) | Absorbed as limb 3 |
| Treatment of B-VAL-019 | Structural evidence, demonstrated by BNC-2 (§15.3) | Absorbed as limb 12 |

`CLAUDE.md` authority precedence places approved Conformance Requirements
(level 5) above prompt/task instructions (level 8). Definition A therefore
outranks Definition B on precedence alone, and additionally on substance,
because §14.1 forbids exactly the flattening Definition B performs.

**The conflict is resolvable and is resolved.** It is not a standing normative
contradiction: one source is a contract, the other is an instruction, and the
precedence rule between them is already written down.

## 7. B-VAL-011 disposition

| Attribute | Value |
|---|---|
| Current scope | `R_PY.fixture_id == R_RS.fixture_id == Registry.fixture_id` |
| Evidence class | Label equality |
| Historical scope | Absorbed as twelve-limb limb 3 (partially) |
| Evidence already produced | Partial. Both P-01 receipts carry `fixture_id = FIX-DIGEST-P01` (`927e524`). The `Registry.fixture_id` term is **unbound** — Registry unresolvable, `BC-02-DEP-001` |
| Prerequisite to B-VAL-014? | **No** |
| Separate assertion? | **Yes** |
| Part of B-VAL-014 execution scope? | **No** |

## 8. B-VAL-012 disposition

| Attribute | Value |
|---|---|
| Current scope | `fixture_hash` equality across both records and the Registry, **and** `R_PY.input_segment_sha256 == R_RS.input_segment_sha256`, each independently recomputed by its own receiver |
| Evidence class | **Transfer evidence** |
| Historical scope | Absorbed as limbs 6, 7, 8 |
| Evidence already produced | Second conjunct materially observed at `927e524`: both receivers independently derived `ecf9e98e…d4e65667`. First conjunct **UNKNOWN** — Registry hash rule unbound, `BC-02-DEP-002`, per §14.2 |
| Prerequisite to B-VAL-014? | **No — companion.** §14.1 pairs the two: *"B-VAL-012 together with B-VAL-014"* |
| Separate assertion? | **Yes** |
| Part of B-VAL-014 execution scope? | **No** — evaluated alongside it, not inside it |

B-VAL-012 is the closest neighbour to B-VAL-014 and the one most likely to be
wrongly merged. They are distinct: B-VAL-012 compares the two receivers'
independently recomputed digests *to each other*; B-VAL-014 checks, on each side
separately, that the receipt's digest is the receiver's own recomputation over
the segment it actually received, under an admitted encoding.

## 9. B-VAL-013 disposition

| Attribute | Value |
|---|---|
| Current scope | `R_PY.fixture_artifact_identity == R_RS.fixture_artifact_identity` **and** `R_PY.issuance_id == R_RS.issuance_id` |
| Evidence class | **Traceability — explicitly NOT independent transfer evidence** (§14, §14.1) |
| Historical scope | Absorbed as limb 3 |
| Evidence already produced | Partial. Both receipts carry `fixture_artifact_identity = FIX-DIGEST-P01.canonical.json` (`927e524`). No `issuance_id` exists in BC-02.1 or in either receipt |
| Prerequisite to B-VAL-014? | **No** |
| Separate assertion? | **Yes** |
| Part of B-VAL-014 execution scope? | **No — re-absorption expressly prohibited** |

Per the critical separation required of this reconciliation, and independently
required by contract §14.1: **B-VAL-013 remains distinct traceability /
artifact-identity evidence.** It holds by construction whenever both records
descend from one issuance and therefore proves no octet arrived anywhere. It
MUST NOT be counted toward B-VAL-014, now or in any downstream summary.

## 10. B-VAL-014 current definition

**Controlling definition: BC-02 contract §14 — "Raw input preserved."**

Formal condition, as written in the contract:

```text
receipt.receipt_digest == input_segment_sha256      on BOTH sides
receipt_digest_source  == RECEIVER_RECOMPUTED       on BOTH sides
raw_input_encoding     ∈ {identity, base64, base16}
```

Evidence class: **Transfer evidence**.

Semantic boundary, preserved:

> B-VAL-014 verifies that the raw octets actually received by the independent
> receivers correspond to the issued P-01 artifact at the byte/octet level,
> using independently receiver-derived observations.

The essential evidence relationship:

```text
H_PY(received_octets) == H_RS(received_octets) == H_ISSUED
```

with corresponding received-length and octet-identity evidence.

```text
issued artifact
      ↓
actual transfer
      ↓
receiver raw octets
      ↓
independent receiver hashing
      ↓
comparison
```

This is an **execution definition, not a conformance result**.

Negative control bound to it by §15.3: **BNC-1** — flip one octet of the buffer
delivered to one side only; MUST be caught by B-VAL-012 and B-VAL-014. A
happy-path-only demonstration does not satisfy §15.3.

## 11. B-VAL-019 disposition

| Attribute | Value |
|---|---|
| Current scope | Adapter has no Registry reference, no resident fixture copy, and no code path from `input_characterization` or `fixture_id` to `input_segment_bytes`; demonstrated by **BNC-2** (§15.3) |
| Evidence class | **Structural evidence** |
| Historical scope | Absorbed as limb 12, *"no reconstruction occurred"* |
| Evidence already produced | Partial and structural only. Both receivers reject reconstruction paths by construction; BNC-2 has **never been executed** |
| Prerequisite to B-VAL-014? | **No** |
| Separate assertion? | **Yes** |
| Part of B-VAL-014 execution scope? | **No** |

The historical record itself flagged the defect in treating this as a limb: at
`b90112b` §5.4, limb 12 was marked **VACUOUS** — *"nothing was transferred, so
nothing was reconstructed; this is not evidence of the invariant."* An assertion
that can be satisfied vacuously by the absence of a handoff cannot be a limb of
a transfer assertion. This corroborates keeping B-VAL-019 separate.

## 12. Precedence decision

**BC-02 §14 precedence: ESTABLISHED.**

| Definition | Standing |
|---|---|
| A — BC-02 §14 *"Raw input preserved"* | **CONTROLLING CURRENT CONTRACT** |
| B — twelve-limb receiver-side formulation | **HISTORICAL PROVENANCE. Not the current execution contract.** |

Basis: `CLAUDE.md` authority precedence, level 5 over level 8; and BC-02 §14.1,
which prohibits the flattening Definition B performs.

Historical grouping does not determine current execution scope. B-VAL-011,
B-VAL-012, B-VAL-013 and B-VAL-019 are **separate assertions and separate
gates**; none is inside B-VAL-014's execution scope.

## 13. Historical preservation statement

No history was rewritten.

- `BC-02_IMMUTABLE_FIXTURE_HANDOFF.md` — unmodified.
- `BC-02_BOUNDARY_VALIDATION_RECORD.md` — unmodified. Its §5.4 twelve-limb table
  remains as recorded, and its `NOT EXECUTED / BLOCKED` determination remains
  the correct historical disposition as of `b90112b`.
- The twelve-limb formulation is **retained as historical provenance**. This
  record does not assert that it never existed, was never issued, or was never
  evaluated. It asserts only that it is not the current execution contract.
- No prior audit, closure, evidence, or construction record was altered.

This record establishes the **current custodian interpretation**. Earlier
documents remain the historical record of what was stated when.

## 14. Execution boundary

**B-VAL-014 execution MAY only begin after this reconciliation is complete and
separately authorized. This reconciliation record grants NO execution
authority.**

During this reconciliation:

- No receiver was invoked.
- No fixture was consumed.
- No receipt was regenerated.
- No implementation was changed.
- The Controlled P-01 Handoff was not re-run.

Layer separation, restated and not to be collapsed:

```text
receipt/schema validation  ≠  B-VAL-014  ≠  CONF-003 §4.5  ≠  protocol conformance result
```

P-01 issuance alone is not validation. Receipt generation alone is not
validation. R-VAL-001…012 alone is not B-VAL-014.

## 15. Explicit non-execution

Prohibited inferences, none of which this record makes or permits:

```text
digest equality   →  protocol conformance      PROHIBITED
receipt equality  →  protocol conformance      PROHIBITED
receiver agreement→  §4.5 PASS                 PROHIBITED
B-VAL-014 PASS    →  overall protocol PASS     PROHIBITED
```

B-VAL-014 remains **one validation gate** among B-VAL-011 … B-VAL-020.

Unexecuted and undetermined: B-VAL-014; CONF-003 §4.5; conformance suite;
acceptance suite; protocol PASS/FAIL; CONFORMANT/NON_CONFORMANT. Canonicalization
rules and digest-input rules unchanged. No implementation modified.

## 16. Remaining ambiguity

The **definitional** conflict is resolved (§12). No residual ambiguity remains
about *what B-VAL-014 means*.

Three **execution preconditions** are nevertheless unmet. These are not
definitional conflicts; they are missing bindings between the contract's
vocabulary and the artifacts that exist. They are recorded here rather than
resolved, because resolving them by implementation choice is prohibited.

### 16.1 PRE-01 — schema binding gap between BC-02 §14 and BC-02.1 *(material)*

BC-02 §14 states B-VAL-014 over the `BoundaryHandoffRecord` schema. The
Controlled P-01 Handoff produced **BC-02.1 `BoundaryReceipt`s**. The two
vocabularies do not overlap at all:

| BC-02 §14 term | Occurrences in BC-02.1 schema | Occurrences in either executed receipt |
|---|---|---|
| `receipt_digest` | 0 | 0 |
| `receipt_digest_source` | 0 | 0 |
| `input_segment_sha256` | 0 | 0 |
| `raw_input_encoding` | 0 | 0 |
| `issuance_id` | 0 | 0 |
| `fixture_hash` | 0 | 0 |
| `BoundaryHandoffRecord` | 0 | 0 |

What the receipts actually carry:

```text
"received":{"octet_length":15,"raw_octets":"…","recomputed_sha256":"…"}
```

The plain reading is that `received.recomputed_sha256` corresponds to both
`receipt_digest` and `input_segment_sha256`; that `RECEIVER_RECOMPUTED` is
structurally guaranteed rather than recorded as a field; and that the Base64
transport of `raw_octets` corresponds to `raw_input_encoding = base64`. **That
mapping is not declared anywhere, and this record does not declare it.**
Adopting it silently would be resolving a contract question by implementation
choice.

A custodian-declared field binding — or an explicit statement that BC-02.1
supersedes `BoundaryHandoffRecord` for this purpose — is required before
B-VAL-014 can be evaluated against the existing evidence.

### 16.2 PRE-02 — BNC-1 negative control not executed

§15.3 requires each negative control to be shown caught by its named assertion;
BNC-1 is bound to B-VAL-012 and B-VAL-014. BNC-1 has never been run. §15.3 also
requires controls to be applied to temporary copies only and never left in a
committed artifact.

### 16.3 PRE-03 — Registry unbound (affects neighbours, not B-VAL-014 itself)

`BC-02-DEP-001` and `BC-02-DEP-002` remain open: the Fixture Registry is
unresolvable, so B-VAL-011's `Registry.fixture_id` term and B-VAL-012's
`fixture_hash` conjunct are unbound. §14.2 already records that limb as
**UNKNOWN**, and §11.2 requires that UNKNOWN be preserved, not converted.
B-VAL-014's own formal condition does not reference the Registry, so this does
not block B-VAL-014 — but it does block reading B-VAL-012 as complete, and
§14.1 pairs the two.

## 17. Custodian decision

BC-02 §14 is the controlling current definition of B-VAL-014. The earlier
twelve-limb receiver-side formulation is retained as historical provenance and
is not silently flattened into the current execution contract.

B-VAL-013 remains distinct traceability/artifact-identity evidence.

B-VAL-014 remains the raw-transfer / received-octet verification gate.

No B-VAL-014 execution is authorized by this record.

### 17.1 Definition of Done

| # | Criterion | State |
|---|---|---|
| 1 | Both historical definitions identified | met — §4.1, §4.2 |
| 2 | Provenance recorded | met — §3, §4 |
| 3 | BC-02 §14 precedence established or rejected | met — **established**, §12 |
| 4 | B-VAL-011 disposition explicit | met — §7 |
| 5 | B-VAL-012 disposition explicit | met — §8 |
| 6 | B-VAL-013 disposition explicit | met — §9 |
| 7 | B-VAL-019 disposition explicit | met — §11 |
| 8 | Current B-VAL-014 scope unambiguous | met — §10 |
| 9 | Historical records unchanged | met — §13 |
| 10 | No execution occurred | met — §14, §15 |
| 11 | No normative implementation changed | met — §15 |
| 12 | Next gate explicitly identified | met — §18 |

### 17.2 Answers to the governance questions

| Q | Answer |
|---|---|
| **Q1** Which definition is the current contract? | BC-02 §14, *"Raw input preserved"*. §12 |
| **Q2** Relation of the twelve-limb formulation to BC-02 §14? | A task-instruction restatement, subordinate by `CLAUDE.md` precedence (level 8 vs level 5) and contrary to §14.1. Retained as historical provenance; not the execution contract. §4.2, §12, §13 |
| **Q3** Are B-VAL-011/012/013/019 inside B-VAL-014's execution scope? | **No.** All four are separate assertions and separate gates. B-VAL-012 is a companion evaluated alongside B-VAL-014 (§14.1), not inside it. §7–§9, §11 |
| **Q4** What exactly must B-VAL-014 verify? | On both sides: the receipt digest equals the received-segment digest, that digest is receiver-recomputed, and the raw-input encoding is admitted — establishing `H_PY == H_RS == H_ISSUED` with length and octet-identity evidence, plus negative control BNC-1. §10 |
| **Q5** What may NOT be counted as B-VAL-014? | P-01 issuance; receipt generation; R-VAL-001…012; B-VAL-013 traceability; cross-receiver agreement read as conformance; Controlled P-01 Handoff completion; §4.5; any protocol PASS/FAIL. §14, §15 |
| **Q6** Any unresolved ambiguity after reconciliation? | **No definitional ambiguity.** Three unmet execution preconditions: PRE-01 schema binding gap (material), PRE-02 BNC-1 not run, PRE-03 Registry unbound. §16 |

## 18. Next gate

**Next gate: a separate B-VAL-014 execution authorization.**

Not granted by this record, not implied by it, and not to be cited as granting
it. Before such a mandate is issued, PRE-01 in particular should be settled by
custodian decision — a declared field binding between BC-02 §14's
`BoundaryHandoffRecord` vocabulary and BC-02.1's `BoundaryReceipt`, or an
explicit statement that BC-02.1 supersedes it for this purpose. PRE-02 should be
scheduled as part of the execution mandate, since §15.3 makes BNC-1 part of a
complete B-VAL-014 validation. PRE-03 constrains B-VAL-012, not B-VAL-014, and
its UNKNOWN must be preserved rather than converted.

```text
B-VAL-014                    NOT EXECUTED
B-VAL-014 execution          NOT AUTHORIZED BY THIS RECORD
CONF-003 §4.5                NO RESULT
Protocol conformance         NOT DETERMINED
BC-02                        CLOSED
Controlled P-01 Handoff      COMPLETE
Custodian closure            COMPLETE
```

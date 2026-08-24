# BC-02 — CUSTODIAN DECISION REVIEW SURFACE v1

**Record type:** Governance-only review surface. Read-only.
**Subject:** the Custodian Decision Package A / B
**Purpose:** make the package decision-ready. **Not** to make the decision.

Non-normative. Creates no authority, amends no record, resolves nothing, and
determines no conformance. **Neither Decision A nor Decision B is resolved
here.** Both candidate interpretations under each decision are preserved
symmetrically, with equal weight and no preference.

---

## 1. Package integrity and commit identity

### 1.1 Naming discrepancy — reported, not corrected

The review was requested against `BC-02-CUSTODIAN-DECISION-PACKAGE-A-B-v1.md`.
**No file of that name exists in any reachable commit of any in-scope
repository.** Exactly one decision package exists:

```text
requested   conformance/boundary/BC-02-CUSTODIAN-DECISION-PACKAGE-A-B-v1.md    ABSENT
actual      conformance/boundary/BC-02.1-CUSTODIAN-DECISION-PACKAGE-A-B.md     PRESENT
```

The differences are the `BC-02` / `BC-02.1` prefix and the absent `-v1` suffix.
The reviewed artifact is the one that exists. **The package was not renamed**;
renaming it would edit the committed record this review exists to verify.
Whether the package should be renamed is a recording question for the Custodian,
listed at §6.3.

### 1.2 Integrity of the reviewed artifact

| Property | Value | Method |
|---|---|---|
| Path | `conformance/boundary/BC-02.1-CUSTODIAN-DECISION-PACKAGE-A-B.md` | — |
| SHA-256 | `c05c20e9764e6f95354a6a24f964be291cb203b39e552ca069ffa49d2c2c3d21` | `sha256sum`, read-only |
| Git blob | `deaf6635787a970474ac8852e7f6f8e814f11f92` | `git hash-object` (worktree) |
| Committed blob | `deaf6635787a970474ac8852e7f6f8e814f11f92` | `git rev-parse HEAD:<path>` |
| Worktree == committed | **YES** | the two hashes above are equal |
| Size | 458 lines, 28 674 octets | `wc -lc` |

### 1.3 Commit identity

| Property | Value |
|---|---|
| Commit | `66bfdb1e7c03d86e75f64b9841d024fba08ed693` |
| Tree | `bc8273c48cad382f6a15c1f6128524e383f09d47` |
| Author | `Claude <kamilkrasinski4@gmail.com>` |
| Date | `2026-08-24 20:12:29 +0000` |
| Subject | *BC-02 / BC-02.1: Custodian Decision Package A/B; Terrain Survey closed* |
| Branch | `claude/bc-02-1-pre-01-schema-kvvm8z` |
| Files in that commit | one — the package |
| `origin/main` at review time | `528de0de6d34a4a7ff541db9cd93238587dac9ef` |
| Working tree at review start | clean |

### 1.4 Quotation integrity

Every verbatim quotation the package attributes to a source was re-checked
against that source's git object. **All located; zero misquotations.** Two
initially failed a naïve single-line grep and were confirmed present under
whitespace normalisation — the quoted sentences span a line break in the
source. That is a line-wrapping artifact of the source, not a quotation defect.

| Quotation | Attributed to | Result |
|---|---|---|
| *"does not invent Registry fields…"* | BC-02 §4.1 | located |
| *"…has verified nothing"* | BC-02 §5.4 | located |
| *"`input_segment_bytes` — an octet buffer"* | BC-02 §8.1 | located |
| *"RECOMPUTED BY THIS RECEIVER"* | BC-02 §7.1 | located |
| *"recomputed over the buffer actually received"* | BC-02 §7.1 | located |
| *"computed once by the issuer at seal time"* | BC-02 §5.3 | located |
| *"one careless `==` away…"* | BC-02 §13.1 refinement note | located |
| *"Flip one octet of the buffer delivered to one side only"* | BC-02 §15.3 | located |
| *"content-addressed store"* | BC-02 §6.4 | located |
| `matches_issued_digest` | BC-02 §7.1 | located |
| *"No evidence of either closure or issuance is reachable in any repository in scope."* | BC-02 Boundary Validation Record §8 | located (line-wrapped) |
| *"No P-01 issuance record exists in the repository to cross-check against."* | RI-RS P-01 Evidence Package §11 | located (line-wrapped) |
| *"PRE-01: OPEN — BINDING GAP (Outcome B)"* | Pre-execution Contract Binding Record §1 | located |
| *"PRE-01 — PASS"* | PRE-01 Schema Correction Record §I | located |
| *"BC-02.2 RI-PY  NOT STARTED"* | BC-02.1 v1 §18 | located |
| *"BC-02.2 RI-PY Receiver  CONSTRUCTED"* | BC-02.3 §7 | located |
| `"status":"TRANSFERRED"` in both receipts | executed P-01 receipts | located, both |
| `"fixture_artifact_identity":"FIX-DIGEST-P01.canonical.json"` in both receipts | executed P-01 receipts | located, both |
| `EXTERNALLY_SUPPLIED` in the v2 `DigestSource` domain | BC-02.1 v2 §6.2 | located |

The working copy of the BC-02 contract used for quotation checking was verified
byte-identical to its git object: both hash to
`1a7bb3b6d9dca00906163f9cc022a4a5880e01b7bdb752d1b0455fb5cc970945`.

---

## 2. Source artifacts relied upon

### 2.1 Complete enumeration, with reachability

`ON-MAIN` is measured against `origin/main` = `528de0d`. Blob identifiers are
from the commit named in the `REF` column.

| # | Artifact | REF | Blob | ON-MAIN | Relied on by |
|---|---|---|---|---|---|
| S1 | `BC-02_IMMUTABLE_FIXTURE_HANDOFF.md` | `e2066bd` | `9cfbc0fe66578dbb52cb6012f3ea03adcb48c40c` | **NO** | **A and B** |
| S2 | `BC-02_BOUNDARY_VALIDATION_RECORD.md` | `b90112b` | `e57ed4d230e90b4a1de5c22adee43c511b5dde8c` | **NO** | A |
| S3 | `B-VAL-014-PREEXEC-CONTRACT-BINDING-RECORD.md` | `31c238b` | `52f1264d27a946ea2c64630c897156af07018890` | **NO** | A and B |
| S4 | `B-VAL-014-DEFINITION-RECONCILIATION-RECORD.md` | `HEAD` | `281b29ca77dded2bbeb16ecc2fe916774ac57bb6` | YES | B |
| S5 | `BC-02.1-COMMON-RECEIPT-SCHEMA-v1.md` | `HEAD` | `f40f7a2ea246f382d12490a6489159f9e226fd17` | YES | A and B |
| S6 | `BC-02.1-COMMON-RECEIPT-SCHEMA-v2.md` | `HEAD` | `963623a58da42ca69c9c9980a661fc59b6e8be42` | **NO** | A and B |
| S7 | `BC-02.1-PRE-01-SCHEMA-CORRECTION-RECORD.md` | `HEAD` | `49807855eec1accb09c13a4c8a7ac28cb4bec047` | **NO** | A and B |
| S8 | `BC-02.1-PRE-02-PRE-03-CLOSURE-RECORD.md` | `HEAD` | `603383c1baf150b1ec7665955b26a5ffcf1904ec` | **NO** | A and B |
| S9 | `BC-02.1-PRE-02-PRE-03-DEPENDENCY-CLOSURE-REPORT-v1.md` | `HEAD` | `72f132b3efbfddd89438f612034f9d4220651f30` | **NO** | A and B |
| S10 | `BC-02.3-RI-RS-RECEIVER-v1.md` | `HEAD` | `e9bb28edbd87bafc05bd2f3fe1410d6abac6a77a` | YES | normalization only |
| S11 | `CONTROLLED-P01-HANDOFF-RECORD.md` | `HEAD` | `fe3de6b4af0a872892cdb07b94bf0c2620c74c8f` | YES | A |
| S12 | `BC-02-CUSTODIAN-CLOSURE-RECORD.md` | `HEAD` | `044f16a83ef42b9c9356372bf3def805b2a43404` | YES | normalization only |
| S13 | `BC-02-CROSS-RECEIVER-PREEXEC-AUDIT.md` | `HEAD` | `a9c7272ea6f64eb4ad52864cd418ec189999170e` | YES | normalization only |
| S14 | `evidence/RI-PY-P01-EVIDENCE-GAP-RECORD.md` | `HEAD` | `feffc15d5587c3bebf446b6f0df419c0c5bbeaa7` | YES | normalization only |
| S15 | `evidence/RI-RS-P01-EVIDENCE-PACKAGE.md` | `HEAD` | `229d481600d55907a48b0e3e55ad06a91601b417` | YES | **A** |
| S16 | `evidence/controlled-p01-handoff/RI-PY-P01-RECEIPT.json` | `HEAD` | `7bd81f082011b8578eef5f28c1d6357c1bfa1ac1` | YES | A and B |
| S17 | `evidence/controlled-p01-handoff/RI-RS-P01-RECEIPT.json` | `HEAD` | `836cbf2170b07d5b075374b9d6a3ab6850952d53` | YES | A and B |
| S18 | `p01/FIX-DIGEST-P01.canonical.json` | `HEAD` | `b45ffa980a1a776b6143d7fcb255fbfa8a436582` | YES | **A and B** |

### 2.2 Reachable-from-main versus branch-local

| Class | Count | Artifacts |
|---|---|---|
| Reachable from `main` | 11 | S4, S5, S10, S11, S12, S13, S14, S15, S16, S17, S18 |
| **Branch-local only** | 7 | **S1**, S2, S3, S6, S7, S8, S9 |

**The single most load-bearing artifact is branch-local.** S1 — the BC-02
contract — is the sole authoritative source of B-VAL-011…020, BNC-1…BNC-7,
VE-01…VE-05 and DEP-001…005, and every clause quoted under both decisions below
comes from it. It is reachable only from
`origin/claude/bc-02-immutable-fixture-handoff-3s3fkp` and is **not** an
ancestor of `origin/main`.

Consequence for the ruling, stated as a fact and not as a recommendation: a
Custodian reading only `main` cannot reach the text either decision turns on.
Whether to integrate S1, S2 and S3 is itself a Custodian question (§6.3). **No
merge, no PR and no branch change was made by this review.**

### 2.3 Per-decision source dependency

| Decision | Sources it depends on |
|---|---|
| **A** | S1 §4.1, §4.2, §5.2, §5.3, §5.4, §5.5, §6.4, §7.1, §15.2, §19 · S2 §8 · S3 §15 · S5 §4 · S6 §4, §10.2 · S7 · S8 · S9 · S11 §1 · S15 §2, §11 · S16 · S17 · S18 |
| **B** | S1 §5.3, §6.3, §7.1, §8, §13.1, §13.2, §14, §15.3 · S3 §9, §10 · S4 §10 · S5 §5, §6 · S6 §5, §6 · S7 · S9 §L, §N · S16 · S17 · S18 |

---

## 3. DECISION A — exposed surface

Exposed here, per the review scope: **Registry authority · `fixture_hash` rule ·
issuance authority · issuer identity · sealed-store authority / provenance.**
Scope note at §3.3.

**NOT RESOLVED. No option below is preferred, recommended or assumed.**

### 3.1 The five exposed questions, reproduced without change of semantics

| Exposure | Question as the package states it | Package ID | Source |
|---|---|---|---|
| **Registry authority** | *"Supply `CONFORMANCE_FIXTURE_REGISTRY_v1`, or declare BC-02 unenterable without it?"* | A-1 | S1 §4.1, VE-01, DEP-001 |
| **`fixture_hash` rule** | *"Declare the `fixture_hash` rule — covered octets and encoding — or hold `fixture_hash_verification` at UNKNOWN indefinitely?"* | A-2 | S1 §5.4, VE-02, DEP-002 |
| **Issuance authority** | *"Authorize an issuance event over the existing octets…?"* | A-3, first limb | S1 §15.2 step 2 |
| **Issuer identity** | *"…naming the issuer? BC-02 §5.3 and §7.1 require issuer-computed values at seal time; no issuer identity exists in any reachable artifact"* | A-3, second limb | S1 §5.3, §7.1 |
| **Sealed-store authority / provenance** | *"Does a committed content-addressed git blob satisfy §6.4's `storage the boundary cannot write to`? §6.4 admits a `content-addressed store`; a worktree path at that blob is writable"* | A-4 | S1 §6.4 |

Wording is reproduced from the package. The two limbs of A-3 are shown
separately because the review scope names issuance authority and issuer identity
as distinct exposures; **this is a presentation split, not a change of
semantics** — A-3 remains one question in the package.

### 3.2 Candidate dispositions, preserved symmetrically

| | **A-I** | **A-II** |
|---|---|---|
| **Disposition** | Supply the Registry and authorize an issuance over the existing octets | Declare BC-02 unenterable for P-01 in the Registry's absence, and record the boundary's terminal state |
| **Effect on PRE-03** | becomes closable | closes as permanently BLOCKED rather than pending |
| **Effect on VE** | VE-01…VE-04 become dischargeable | VE-01…VE-04 remain unmet by declaration |
| **Effect on the §5.5 chain** | gains its top two arrows, `Registry entry → issuance_id` | keeps them empty, as a recorded terminal state |
| **Residual questions either way** | sealed-store and UNKNOWN-recording questions still need answers | B-VAL-011's `Registry.fixture_id` term and B-VAL-012's `fixture_hash` conjunct stay UNKNOWN, preserved per S1 §11.2 |
| **Effect on the re-handoff** | a re-handoff becomes reachable, under separate authorization | no re-handoff is entered |

**A-III** — a different disposition the Custodian specifies — remains available
and is not narrowed by the two columns above.

### 3.3 Exposure-scope note

The package carries four further Decision A questions that this review's scope
does not expose: **A-5** (where `fixture_hash_verification`'s UNKNOWN is
recorded), **A-6** (which `fixture_artifact_identity` definition governs, and
the two receipts carrying a filename), **A-7** (Boundary Specification v1, Core
Interface Spec v1, BC-01), **A-8** (`input_characterization` value domain).

**They remain OPEN in the package.** Their absence from §3.1 is a scope limit of
this review surface and must not be read as closure, resolution, or withdrawal.

---

## 4. DECISION B — exposed surface

Exposed here, per the review scope: **issuer-sealed interpretation ·
receiver-recomputed interpretation · consequences for B-VAL-014 · consequences
for BNC-1 detectability.** Scope note at §4.4.

**NOT RESOLVED. Neither interpretation is preferred, recommended or assumed.**

### 4.1 The question, reproduced without change of semantics

> *"Does `raw_input_reference.input_segment_sha256` carry the issuer-sealed
> value or the receiver's recomputation?"* — package B-1, from S1 §5.3 vs §7.1.

The contract text both interpretations rest on, verbatim from S1:

```text
§7.1  raw_input_reference.input_segment_sha256
      "<hex SHA-256 of decoded octets — RECOMPUTED BY THIS RECEIVER>"

§7.1  receipt.receipt_digest
      "<hex SHA-256 recomputed over the buffer actually received>"

§7.1  receipt.matches_issued_digest : true

§5.3  "computed once by the issuer at seal time; recomputed independently by
       each adapter over the octets it actually received, before any use;
       recorded in both BoundaryHandoffRecords"

§8.1  the adapter receives "input_segment_bytes — an octet buffer"

§14   B-VAL-014: "receipt.receipt_digest == input_segment_sha256 on both sides,
       with receipt_digest_source == RECEIVER_RECOMPUTED; and
       raw_input_encoding ∈ {identity, base64, base16}"

§15.3 BNC-1: "Flip one octet of the buffer delivered to one side only"
       MUST be caught by: B-VAL-012, B-VAL-014
```

### 4.2 The two interpretations, preserved symmetrically

| | **B-I — issuer-sealed** | **B-II — receiver-recomputed** |
|---|---|---|
| **Reading** | the record's `input_segment_sha256` is the issuer's seal-time value, echoed in | the record's `input_segment_sha256` is this receiver's own recomputation |
| **Textual support** | §5.3 *"computed once by the issuer at seal time"*; §7.1's `matches_issued_digest` field; §15.3's requirement that B-VAL-014 catch BNC-1 | §7.1's inline definition, *"RECOMPUTED BY THIS RECEIVER"*; §5.3's *"recomputed independently by each adapter"* |
| **Textual cost** | §7.1's inline comment would need correcting | §15.3's control mapping would need amending, or BNC-1 rebinding to B-VAL-012 alone |
| **What B-VAL-014 then asserts** | receiver recomputation equals issuer seal — a cross-party comparison | the receipt digest equals the digest of the segment the receiver holds — a within-side binding |
| **Effect on BNC-1 detectability** | **caught by B-VAL-014**: the flipped side's recomputation diverges from the issuer's sealed value | **not caught by B-VAL-014**: the flipped side records `H(corrupted)` in both operands, so the equality still holds there; divergence appears only in B-VAL-012's cross-receiver conjunct |
| **Effect on §15.3 as written** | satisfiable as written | not satisfiable as written |
| **Effect on a v2 receipt** | that operand's `source` would be the issuer-supplied value | that operand's `source` is `RECEIVER_RECOMPUTED`, as v2 currently states |

**B-III** — a different reconciliation the Custodian specifies — remains
available and is not narrowed by the two columns above.

### 4.3 Consequence recorded by the package, reproduced

> BC-02 §5.3, §7.1, §14 and §15.3 are **not jointly satisfiable** without a
> determination of which value that field carries.

This review confirms the package states this as an unresolved tension and does
not resolve it. **This review does not resolve it either.** Which text yields —
§15.3's control mapping, §14's formal condition, or §7.1's inline definition —
is the Custodian's to say.

### 4.4 Exposure-scope note

The package carries three further Decision B questions this review's scope does
not expose: **B-2** (artifact / input-segment relation for an artifact-only
fixture), **B-3** (whether §15.3's BNC-1 mapping is satisfiable, and which text
yields), **B-4** (which `handoff_status` vocabulary governs a v2 receipt),
**B-5** (receiver-side versus issuer-side decode).

**They remain OPEN in the package.** B-2 and B-5 materially condition the
consequences tabulated in §4.2. Their absence from this surface is a scope
limit, not closure.

---

## 5. Verification of gate conditions

### 5.1 No implementation change is required or authorized at this gate

| Check | Result | Method |
|---|---|---|
| `ri_py_receiver.py` | identical to `origin/main` | blob comparison, core repository |
| `ri_py_adapter.py` | identical to `origin/main` | blob comparison, core repository |
| `ri_rs_receiver.rs` | identical to `origin/main` | blob comparison |
| `ri-rs/src/bin/p01_handoff.rs` | identical to `origin/main` | blob comparison |
| Both executed P-01 receipts | identical to `origin/main` | blob comparison |
| `FIX-DIGEST-P01.canonical.json` | identical to `origin/main`, blob `b45ffa98…` | blob comparison |
| `BC-02.1-COMMON-RECEIPT-SCHEMA-v1.md` | identical to `origin/main` | blob comparison |
| `APS-200_CANONICAL_DATA_MODEL.md` | identical to `origin/main` | blob comparison |
| `CONF-003_CANONICAL_SERIALIZATION.md` | identical to `origin/main` | blob comparison |
| An authorization for receiver binding to `schema_version = 2` | **none exists** in any reachable commit | corpus search |
| Any implementation change required *by this review* | **none** | this review is read-only |

The package's own position is that receiver binding to v2 is *required,
specified, and not authorized*, and that it is additionally gated on B-1 and
B-2 — neither of which is resolved. **Implementation is therefore NO-GO at this
gate**, and this review neither performs nor authorizes any implementation
change.

### 5.2 No UNKNOWN has been promoted

| UNKNOWN carried by the corpus | State in the package | State in this review |
|---|---|---|
| `DEP-001…005 SATISFIED FOR P-01` — claimed in headers, unevidenced | held **UNKNOWN**, explicitly *"not converted"* | held UNKNOWN |
| `fixture_hash_verification` | UNKNOWN, per S1 §5.4 | UNKNOWN |
| `issuance_id` for P-01 | UNKNOWN | UNKNOWN |
| BC-01 acceptance | UNKNOWN — recorded ACCEPTED, artifact unreachable | UNKNOWN |
| VE-03 — octet-exact fixture input | OPEN / unmet | OPEN / unmet |
| Whether the declared digest is an *issuer's* identity for an *issued* artifact | UNKNOWN | UNKNOWN |

**No UNKNOWN was promoted to PASS, CLOSED, SATISFIED, or VERIFIED by the package
or by this review.** The package's own firewall row *"UNKNOWN upgraded — NO"* is
confirmed by inspection of every UNKNOWN occurrence in it.

### 5.3 No new normative semantics are introduced by this review artifact

| Check | Result |
|---|---|
| New protocol requirement, field, or state | **none** |
| New identifier or namespace | **none** — every ID cited (A-1…A-4, B-1, B-I, B-II, D-*, VE-*, DEP-*, S1…S18) is either pre-existing or, for S1…S18, a local row label of §2.1 with no meaning outside this table |
| New status token | **none** — only tokens already in the corpus or in the package's §3.2 reading set |
| Any record amended, renumbered, re-scored or superseded | **none** |
| Any decision resolved, narrowed, or ranked | **none** — A-I/A-II and B-I/B-II are presented in parallel columns of equal structure; A-III and B-III preserved |
| Any interpretation adopted | **none** |
| Any file other than this one written | **none** |

The §3.1 presentation split of package question A-3 into *issuance authority*
and *issuer identity* follows the review scope's own naming and changes no
semantics; A-3 remains a single question in the package.

### 5.4 Read-only compliance

| Prohibition | Observed |
|---|---|
| Decision A or B resolved | **NO** |
| BC-02, BC-02.1 v1/v2, APS-200, CONF-003 modified | **NO** — all verified identical to `origin/main` |
| P-01 modified | **NO** — blob `b45ffa98…` unchanged |
| Receiver code modified | **NO** — all four files identical to `origin/main` |
| Receipts modified | **NO** — both identical to `origin/main` |
| Registry or issuance artifact created or modified | **NO** — none exists to modify |
| Fixture created | **NO** |
| B-VAL-014, B-VAL-012, BNC-1, §4.5, N-01…N-08, C1–C8 executed | **NO** |
| Receiver invoked | **NO** |
| Any file changed other than this artifact | **NO** |
| Merge, PR, or change to `main` | **NO** |

---

## 6. Question classification

### 6.1 Requires an authoritative Custodian ruling

Exposed by this surface:

| ID | Question | Decision |
|---|---|---|
| A-1 | Registry authority — supply, or declare BC-02 unenterable | **A** |
| A-2 | `fixture_hash` rule — covered octets and encoding | **A** |
| A-3a | Issuance authority — authorize an issuance over the existing octets | **A** |
| A-3b | Issuer identity — who the issuer is | **A** |
| A-4 | Sealed-store authority / provenance under §6.4 | **A** |
| B-1 | Which value `input_segment_sha256` carries | **B** |

Open in the package, outside this surface's exposure scope (§3.3, §4.4):
A-5, A-6, A-7, A-8, B-2, B-3, B-4, B-5. **All require a Custodian ruling.**

### 6.2 Execution-gated — not decisions

These cannot be ruled on. They have no answer until a controlled execution
occurs under a separate mandate, and no ruling can substitute for one.

| Item | Why it is not a decision |
|---|---|
| **BNC-1 result** | §15.3 requires the injected condition be *shown to be caught*. There is no buffer and no delivery outside a handoff. Its construction prerequisites can be closed; its result cannot |
| **B-VAL-012 result** | evaluated over `BoundaryHandoffRecord`s that exist only after §15.2 step 6 |
| **B-VAL-014 result** | as above. Note the ordering: B-1 is a ruling that must precede the execution; the *result* is not a ruling at all |
| **B-VAL-011, 013, 015…020 results** | as above |
| **CONF-003 §4.5** | conformance layer; blocked, and outside every gate here |

A ruling on B-1 makes B-VAL-014 *evaluable*. It does not make it *evaluated*.
The two must not be collapsed.

### 6.3 Recording questions — no execution effect

| Item | Nature |
|---|---|
| Package filename discrepancy (§1.1) | naming |
| Whether S1, S2, S3 should be integrated so `main` carries the authority every decision cites (§2.2) | reachability |
| The package's D-1, D-2, D-5, D-6, D-8 recording defects | recording |

---

## 7. Review conclusion

The package is **internally consistent, accurately sourced, and decision-ready**
on the surface exposed here. Integrity verifies; commit identity is fixed;
every quotation checks out against its source object; both candidate
interpretations under each decision are stated with equal structure and neither
is favoured; no UNKNOWN is promoted; no implementation change is required or
authorized; and this review introduces no new normative semantics.

Two conditions qualify readiness, both recorded as facts rather than as
obstacles this review may clear:

1. **The authority every decision turns on is branch-local** (§2.2). S1, the
   BC-02 contract, is not reachable from `main`.
2. **This surface exposes six of the fourteen open questions** the package
   carries (§3.3, §4.4). The remaining eight are open, and their absence here is
   a scope limit of this review.

---

DECISION A — OPEN / CUSTODIAN REQUIRED
DECISION B — OPEN / CUSTODIAN REQUIRED
B-VAL-014 — NOT EXECUTED
§4.5 — NO RESULT
IMPLEMENTATION — NO-GO AT THIS GATE
NORMATIVE AMENDMENT — NONE

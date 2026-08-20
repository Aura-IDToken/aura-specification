# DQ-002 FINAL CLOSURE AUDIT

**Classification:** EVIDENCE / AUDIT — non-normative. Decides nothing, approves
nothing, closes nothing.
**Audit date:** 2026-08-20 (revision 2 — adds executed oracle evidence)
**Method:** specification read first; then implementation source; then execution.
Every digest below was recomputed locally. Every command shown was run, and its
real exit status recorded. No output is reproduced from a prior report.

| Repository | Branch | HEAD | Working tree |
|---|---|---|---|
| `aura-specification` | `claude/ck003-canonical-serialization-hjlaba` | `f590863272c28214eb8458104c28934b18e6e459` | clean |
| RI-PY `aura-poc-a-core-v3.3` | = `origin/main` | `64bf959b1d23fbd5433723476c611ab66d423953` | clean, unmodified |
| RI-RS `aura-guard-v1.3` | = `origin/main` | `35082d7b4880dad780fb55a1a5f3ac0ef4322674` | clean, unmodified |

No production code, protocol semantics, hash domain, canonicalization or Merkle
implementation was modified. All mutation testing was performed on copies in a
scratch directory.

---

## Normative Contract

### Sources, in precedence order

| Element | Statement | Location | Status of source |
|---|---|---|---|
| Leaf hashing | `SHA-256(0x00 \|\| canonical_bytes)` | `aps/APS-300_EVIDENCE_MODEL.md:109`; `aps/APS-200_CANONICAL_DATA_MODEL.md:341` | `1.0-DRAFT` |
| Leaf hashing | `SHA-256(0x00 \|\| raw_data_bytes)` | `ADR-CK003-DQ002-HASH-DOMAIN.md:18,37` | **PROPOSED** |
| Interior node | `SHA-256(0x01 \|\| left[32] \|\| right[32])` | `APS-300:110`; `APS-200:359`; `APS-001` §7.1; both ADRs | `1.0-DRAFT` / PROPOSED |
| Domain separation | `0x00` leaf, `0x01` node, one raw octet each | `APS-001` §7.1–7.2 | `0.2-DRAFT` |
| SHA-256 input | raw bytes; "hexadecimal strings are presentation values and MUST NOT substitute for underlying digest bytes" | `APS-001` §7.1 | `0.2-DRAFT` |
| Byte ordering | children in left-then-right order, 32 raw digest bytes each | `APS-001` §7.2; ADR rule 2 | `0.2-DRAFT` / PROPOSED |
| Merkle construction | recursive split at largest power of two strictly < n; unpaired node promoted, never duplicated | `ADR-CK003-DQ002-HASH-DOMAIN.md` rules 4–5 | **PROPOSED ONLY** |
| Empty tree | `SHA-256("")` | ADR rule 6 (as a requirement to specify, not a value); `tools/rfc6962_oracle.sh` | **PROPOSED ONLY** |
| RFC 6962 compatibility | "Merkle semantics are RFC 6962-style" | `APS-001` §7.1 | `0.2-DRAFT` |

The contract is not rewritten here.

### N-1 — The normative chain terminates in a document that does not exist

`APS-001` §7.2, verbatim:

> "For Merkle use, leaf hashes use `0x00`, internal nodes use `0x01`, child values
> are the 32 raw digest bytes, and tree construction/odd-node behaviour MUST follow
> **the approved Aura Merkle profile**."

A repository-wide search returns that phrase **exactly once** — in that sentence
itself. No such profile exists in `aps/`, `specification/`, `adrs/`, `ck003/` or
anywhere else. The two rules that distinguish DQ-002 from an ordinary hash — tree
shape and odd-node behaviour — therefore have **no normative source**. They exist
only inside a PROPOSED ADR.

**UNRESOLVED.** Candidate content exists; promoting it is a Custodian act.

### N-2 — The two ADRs disagree on the leaf input domain

| Source | Leaf input |
|---|---|
| `02_hash_domain_adr.md:31,51` | `SHA-256(0x00 \|\| **canonical_bytes**)` |
| `ADR-CK003-DQ002-HASH-DOMAIN.md:18,37` | `SHA-256(0x00 \|\| **raw_data_bytes**)` |

The corpus splits cleanly along that line. `APS-200` §8.4, `APS-300` §5.1 and
`03_cross_language_fixture.json` say canonical bytes. `ADR-CK003-DQ002`,
`CROSS-LANGUAGE-002-EVIDENCE.md` §3, `cross-language-002-manifest.json` and
`FIX-CK003-DQ002-RFC6962-2LEAF` say raw bytes — and the 2-leaf fixture proves it,
hashing the octets `61`/`62`, the letters `a` and `b`, which are not JSON at all.

Both are coherent designs. They are not the same design. **UNRESOLVED — reported,
not reconciled.**

---

## Requirement Matrix

Every row carries explicit evidence or an explicit gap. "—" means the artifact does
not exist, not that it was not looked for.

| # | Requirement | Normative source | Implementation | Test | Fixture / vector | Oracle | Evidence | Status |
|---|---|---|---|---|---|---|---|---|
| R1 | Leaf = `SHA-256(0x00 ‖ bytes)` | `APS-001` §7.1; `APS-300` §5.1 | RI-RS `src/merkle.rs:29-34`; RI-PY **conformance only**, unmerged | RI-RS `ck003_dq002_ri_rs_conformance.rs`; RI-PY `test_leaf_domain_prefix_is_0x00`; **no CONF-0xx** | `FIX-…-2LEAF` (PROPOSED) | `rfc6962_oracle.sh selftest` → `ok leaf_a`, `ok leaf_b` | oracle exit 0; RI-PY 158/158; RI-RS 1/1 | **PASS (semantic) / BLOCKED (normative)** |
| R2 | Node = `SHA-256(0x01 ‖ L[32] ‖ R[32])` | `APS-001` §7.1; `APS-300` §5.1 | RI-RS `src/merkle.rs:38-44`; RI-PY production **contradicts** | as R1; **no CONF-0xx** | `FIX-…-2LEAF` root | oracle `ok root` | oracle exit 0; comparator exit 0 | **BLOCKED** |
| R3 | Raw bytes at every boundary; never hex text | `APS-001` §7.1; ADR rule 3 | RI-RS `[u8;32]` types; RI-PY production hashes **hex text** | NC-3 both sides | `negative_expectations` in 2LEAF | oracle uses `pack("H*")` → raw | NC-3 PASS both | **FAIL in RI-PY production** |
| R4 | Tree shape: recursive split at lpo2 < n | **— (N-1)** | RI-RS `largest_power_of_two_lt`; RI-PY production pairwise | edge matrix N=0…8 | `FIX-…-EDGE-MATRIX` (PROPOSED) | `rfc6962_oracle.sh emit` | **matrix reproduced byte-identical** | **BLOCKED — no normative source** |
| R5 | Odd node promoted, never duplicated | **— (N-1)** | RI-RS promotes; RI-PY production **duplicates** | NC-4, NC-4b | edge matrix | oracle `mth()` | NC-4 PASS both | **BLOCKED — no source; RI-PY divergent** |
| R6 | Empty tree = `SHA-256("")` | **— (ADR only)** | RI-RS `empty_root()`; RI-PY production **raises `ValueError`** | RI-RS `empty_tree_root_is_sha256_of_nothing` | `HD-007` ("no specification standing") | oracle `ok empty` | `e3b0c442…2b855` | **UNRESOLVED** |
| R7 | Cross-language byte-level equality | ADR rule 7; `APS-001` §9 | both emitters — **both unmerged** | `compare_vectors.py` | edge matrix + 2LEAF | third producer (coreutils) | `EQUAL + CONFORMANT`, exit 0 | **PASS (semantic) / BLOCKED (reachability)** |
| R8 | Leaf bytes are APS-200 §8 canonical bytes | `APS-200` §8.4; `APS-300` §5.1 | RI-RS domain-agnostic `&[u8]`; RI-PY `core/merkle.py` **not JCS** | CONF-003 covers canonicalization only; **nothing tests the join** | CANONICAL-001 (single leaf, no tree) | — | CROSS-LANGUAGE-001 PASS | **BLOCKED — see N-2** |
| R9 | `protocol_version` binding of the hash domain | `APS-001` §12 (general); `APS-200` §8.6 binds **canonicalization only** | none | CONF-008 does not cover it | 2LEAF says `1.0-DRAFT`; CANONICAL-001 says `1.0` | — | none | **UNRESOLVED** |
| R10 | `schema_version` binding | — | — | — | — | — | none | **UNRESOLVED — n/a as written** |
| R11 | `event_type` binding | `EVENT_TYPE_REGISTRY.md` §5: no token normative | n/a — DQ-002 leaves are raw bytes | — | 2LEAF leaves are `a`/`b` | — | none | **UNRESOLVED — out of scope** |
| R12 | No production-runtime divergence | `APS-001` §9 | RI-PY `audit/merkle.py` **and** `core/merkle.py` divergent | none in RI-PY production | — | — | measured, §RI-PY | **FAIL** |

---

## RI-PY Evidence

`Aura-IDToken/aura-poc-a-core-v3.3` @ `origin/main` = `64bf959b`. Unmodified; the
conformance tree was extracted read-only with `git archive`.

### Does RI-PY compute `SHA256(0x00 ‖ data)` and `SHA256(0x01 ‖ L ‖ R)`?

**In the conformance module: yes, and it is executable.**

```text
$ pytest -q conformance/merkle/
158 passed in 0.18s                                                    exit 0
```

`conformance/merkle/rfc6962.py` pins `LEAF_PREFIX == b"\x00"`, `NODE_PREFIX ==
b"\x01"`, returns raw 32-byte digests, and rejects `str` at the leaf boundary and
non-32-byte children at the node boundary.

**In production: no, on both counts, and there are two separate divergences.**

`audit/merkle.py`, executed directly against `main`:

```text
MerkleTree(['a','b']).root      62af5c3cb8da3e4f25061e829ebeea5c7513c54949115b1acc225930a90154da
DQ-002 fixture expected root    b137985ff484fb600db93107c77b0365c80d78f5b429ded0fd97361d077999eb
```

Leaf has no `0x00`; the node is `SHA-256(UTF-8(left_hex + right_hex))`; the odd node
is duplicated. All three DQ-002 byte rules violated.

`core/merkle.py` — `MerkleAttestor.generate_leaf`, which mints Event Trust
Certificates — is a **third** hash domain:

```text
bytes produced   {"event_type": "AUDIT_RECORD", "payload": {"value": 42}, …}   ← whitespace
APS-200 §8       {"event_type":"AUDIT_RECORD","payload":{"value":42},…}
digest           c3838d1e79350c4a2d44f30ea3adee222f4fa41eb7adb04998561d1bf0ec2a92
APS-200 §8 SHA   b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

`json.dumps(sort_keys=True)` uses default separators, so the output is not canonical
under APS-200 §8, and there is no `0x00` prefix.

> **Finding DQ002-A2.** Both DQ-002 ADRs analyse `audit/merkle.py` only.
> `core/merkle.py` appears in no DQ-002 artifact, no defect record and no conflict
> register entry. The DQ-002 divergence analysis is incomplete.

### Reachability

`conformance/merkle/` **does not exist on `origin/main`.** A ref-by-ref sweep of every
remote branch finds it in exactly one: `claude/aura-cross-language-002-6t2kdo`, which
is not an ancestor of `origin/main`. A reviewer cloning RI-PY at `main` finds no
DQ-002 evidence at all, and RI-PY has no DQ-002 CI workflow on any branch.

Meanwhile `.github/workflows/execution-checks.yml` runs
`scripts/generate_determinism_report.py`, which imports `audit.merkle.MerkleTree` —
so RI-PY CI publishes determinism artifacts built from the non-conformant Merkle on
every run.

---

## RI-RS Evidence

`Aura-IDToken/aura-guard-v1.3` @ `origin/main` = `35082d7b`. Unmodified.

**Source conforms.** `src/merkle.rs` implements `leaf_hash` (`0x00`), `node_hash`
(`0x01`, `&[u8; 32]` children), `empty_root`, the recursive split via
`largest_power_of_two_lt`, `audit_path_inner`, and `verify_audit_path` with
odd-node promotion. The `[u8; 32]` typing makes hexadecimal text *unrepresentable*
at a hash boundary — R3 is enforced by the type system rather than by a runtime check.

**Executed on `main`:**

```text
$ cargo test --test ck003_dq002_ri_rs_conformance
test ri_rs_matches_ck003_dq002_fixture ... ok
test result: ok. 1 passed; 0 failed; 0 ignored                          exit 0
```

**CI exists here and only here.** `.github/workflows/ck003-dq002.yml` runs that test
on PRs to `main` and on `ck003/**` pushes.

**But RI-RS `main` still declares DQ-002 unresolved.**
`tests/fixtures/hash_domains/HD-005…007` each carry, today:

> `"not_canonical": "DQ-002 and DQ-006 unresolved; these bytes carry no specification standing."`

RI-RS `main` says unresolved; `aura-specification` `main` says CLOSED.

> **Finding DQ002-A3 — fixture identifier collision.** Both repositories publish
> **`CK003-DQ002-001`**, and they are different fixtures:
>
> | | spec `03_cross_language_fixture.json` | RI-RS `audit/fixtures/ck003_dq002_001.json` |
> |---|---|---|
> | Leaf text | `agent_id=A001\|ari=95000\|…` | `agent_id=MACHINE_ACCOUNT_001\|ari=95000\|…` |
> | Leaf digest | `ba2749fe…fd123` | `f7acc9aa…58e4b` |
> | Node preimage | `0x01 ‖ 00×32 ‖ ff×32` | `0x01 ‖ leaf ‖ leaf` |
> | Self-declared status | `NORMATIVE_TEST_VECTOR` | — |
>
> RI-RS's values verify (`f7acc9aa…`, `1b3ff765…` — recomputed). The spec-side node
> digest does not (see Defect Register). One identifier, two meanings.

---

## RFC6962 Oracle

The repository's own oracle was executed with the documented commands.

### Selftest

```text
$ bash tools/rfc6962_oracle.sh selftest
ok   leaf_a = 022a6979e6dab7aa5ae4c3e5e45f7e977112a7e63593820dbec1ec738a24f93c
ok   leaf_b = 57eb35615d47f34ec714cacdf5fd74608a5e8e102724e80b24b287c0c27b6a31
ok   root = b137985ff484fb600db93107c77b0365c80d78f5b429ded0fd97361d077999eb
ok   empty = e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
EXIT=0
```

### Matrix emission versus the committed fixture

```text
$ bash tools/rfc6962_oracle.sh emit > /tmp/oracle_emit.json
EXIT=0        stderr: (empty)
$ diff <(canonicalise oracle_emit.json) <(canonicalise fixtures/FIX-CK003-DQ002-RFC6962-EDGE-MATRIX.json)
IDENTICAL to committed edge-matrix fixture
```

The committed edge-matrix fixture is **exactly regenerable** from the oracle. It was
not hand-written, and it has not drifted.

### Recorded artifact hashes all reproduce

Every SHA-256 recorded in `CROSS-LANGUAGE-002-EVIDENCE.md` §4 was recomputed:

| Artifact | Recorded | Actual | |
|---|---|---|---|
| `tools/rfc6962_oracle.sh` | `13b0b69d…5017b` | `13b0b69d…5017b` | ✅ |
| `FIX-…-2LEAF.json` | `bf21d2b8…e9aae` | `bf21d2b8…e9aae` | ✅ |
| `FIX-…-EDGE-MATRIX.json` | `dfa5320c…f3eb8` | `dfa5320c…f3eb8` | ✅ |
| `evidence/RI-PY-VECTORS.json` | `82e47587…8a67b` | `82e47587…8a67b` | ✅ |
| `evidence/RI-RS-VECTORS.json` | `82e47587…8a67b` | `82e47587…8a67b` | ✅ |

**Independence holds.** The oracle uses GNU coreutils `sha256sum` for hashing and
perl `pack`/`unpack` purely as a hex codec, sharing no code with CPython `hashlib`
(RI-PY) or the Rust `sha2` crate (RI-RS). Expected values are therefore externally
specified, not self-certified by either implementation.

---

## CROSS-LANGUAGE-002

**CROSS-LANGUAGE-001 is not a substitute and is not used as one here.**

| | CROSS-LANGUAGE-001 | CROSS-LANGUAGE-002 |
|---|---|---|
| Question | canonical serialization bridge (DQ-006) | Merkle hash domain (DQ-002) |
| Fixture | CANONICAL-001 | `FIX-…-2LEAF`, `FIX-…-EDGE-MATRIX` |
| Covers | JCS bytes, `SHA-256(bytes)`, one leaf | leaves, **nodes, roots, audit paths, proofs**, N = 0…8 |
| Verdict | CLOSED / PASS | **CONDITIONAL PASS** |

### Comparator executed

```text
$ python3 tools/compare_vectors.py \
    --a evidence/RI-PY-VECTORS.json --label-a RI-PY \
    --b evidence/RI-RS-VECTORS.json --label-b RI-RS \
    --fixture fixtures/FIX-CK003-DQ002-RFC6962-EDGE-MATRIX.json \
    --two-leaf fixtures/FIX-CK003-DQ002-RFC6962-2LEAF.json

CROSS-LANGUAGE-002 vector comparison
  RI-PY canonical sha256: 8e48aeea78e61a567c956abd0fb0be8a9e1b046364176948aa9e688542432932
  RI-RS canonical sha256: 8e48aeea78e61a567c956abd0fb0be8a9e1b046364176948aa9e688542432932
  structural diffs     : 0
  fixture/NC failures  : 0
  RESULT               : EQUAL + CONFORMANT
EXIT=0        stderr: (empty)
```

### Is the comparator a real discriminator? — tested, on copies

An auditor should not accept a green comparator without checking it can go red.
Three mutations were applied to **copies** in a scratch directory; the repository
files were never touched.

| Mutation | Result | Exit |
|---|---|---|
| One octet flipped in RI-PY `leaf_hashes_hex[0]` | `DIVERGENT` — caught structurally **and** against the fixture | 1 |
| Root for N=5 corrupted **identically in both files** | `DIVERGENT` — both flagged against the fixture | 1 |
| `tampered_leaf_accepted: true` injected in both | `DIVERGENT` — "tampered leaf accepted" | 1 |
| Unmodified copies (control) | `EQUAL + CONFORMANT` | 0 |

The second row is the important one: the comparator does **not** merely diff A
against B. When both agree with each other but disagree with the oracle-generated
fixture, it still fails. The green result is therefore meaningful.

### What CROSS-LANGUAGE-002 does not do

Its own §12 records **CONDITIONAL PASS** and ends:

> **DQ-002 remains OPEN. This document does not close it.**

Both emitters live on the same unmerged branch in both repositories, and conformance
is measured against a PROPOSED contract.

---

## Negative Controls

### Required by §8 — arithmetic verified

All four hold. Leaf data `a`; correct leaf `022a6979…4f93c`.

| Control | Value produced | Differs from correct? |
|---|---|---|
| `0x01` instead of `0x00` | `e3254ea61c09ead5a01d3bf07e946a561c6c2cd1c46b8ca1bfa8729d26a7d09f` | ✅ |
| ASCII `"0x00"` instead of raw `0x00` | `f369f7e2892f3b2d358ab358a8ace9611f8abd1923b400fa71393f54d05a7cb7` | ✅ |
| Missing domain prefix | `ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb` | ✅ |
| Concatenation order `node(R,L)` | `8af01af409f78be71c0de3efd008ef3f00d5415f36c3d7ab59abcc491dc1cf39` | ✅ (correct: `b137985f…7999eb`) |

### Coverage by existing tests — three GAPs

| Control | Asserted by an existing DQ-002 test? |
|---|---|
| Missing prefix (leaf) | ✅ NC-1 |
| Missing prefix (node) | ✅ NC-2 |
| Hex text at the node boundary | ✅ NC-3 |
| `str` rejected at the leaf boundary | ✅ type guard |
| Odd-node duplication | ✅ NC-4, NC-4b |
| Altered leaf / sibling / root / index / malformed proof | ✅ NC-5…NC-8, NC-10 |
| **`0x01` used as the leaf prefix** | **GAP** |
| **ASCII `"0x00"` used as the leaf prefix** | **GAP** |
| **`node(L,R)` vs `node(R,L)` swap** | **GAP** |

> **GAP-NC1 — domain-swap control absent.** `test_leaf_domain_prefix_is_0x00` pins
> the constant, and NC-1 covers *omitting* the prefix, but nothing asserts that a
> leaf computed with `0x01` differs from the correct leaf. The swap is the exact
> confusion RFC 6962's domain separation exists to prevent.
>
> **GAP-NC2 — ASCII-`"0x00"` control absent at the leaf.** NC-3 covers hex text at
> the *node* boundary; the `str` type guard blocks text from reaching the leaf in
> RI-PY. Neither is a value-level assertion that `SHA-256("0x00" ‖ data)` differs.
> This control *is* present for CANONICAL-001 (`scripts/validate_canonical_001.py`),
> but not for the DQ-002 vectors.
>
> **GAP-NC3 — concatenation-order control absent.** NC-6 alters siblings and NC-8
> rejects a reversed *path*, both of which catch order errors indirectly at the
> proof level. Nothing asserts `node(L,R) ≠ node(R,L)` directly.

All three are **test-coverage gaps, not defects**: the underlying arithmetic is
correct in both implementations, as the table above shows. **No production code was
modified to create these controls** — they were computed independently.

---

## Defect Register

| Defect | Determination | Basis |
|---|---|---|
| **DEFECT-DQ002-F1** | **OPEN** | Re-verified arithmetically this audit (below). The file is unchanged. |
| **DEFECT-DQ002-F2** | **OPEN** | DQ-002 is still silent on tree-size binding; no APS text added. Property confirmed present in `accepted_tree_sizes` in both vector sets. |
| **DEFECT-DQ002-F3** | **OPEN** | Re-executed: RI-PY collection still aborts. |

Status was determined by execution and by reading current file content — **not
inferred from file existence**.

### F1 — re-verified, and newly shown to be unasserted

| Field | Value |
|---|---|
| Declared preimage | `01` ‖ `00`×32 ‖ `ff`×32, 65 octets — length correct |
| SHA-256 of that preimage | `bc6b943b820c449acf880d293c216a24a8066b153f87f2361fae2beda3a72641` |
| Recorded `node.digest_hex` | `e2bd2dcef148b54e935fe552c7c83978103f85b2d970d55f482717bb3904b7ac` |
| Match | **NO** |

New this revision: **both implementations' vector files carry the correct value.**
`RI-PY-VECTORS.json` and `RI-RS-VECTORS.json` both record
`fixture_ck003_dq002_001.node_digest_hex = bc6b943b…a72641`.

And `compare_vectors.py` checks `--fixture` (edge matrix) and `--two-leaf` only. It
never opens `03_cross_language_fixture.json`. So the wrong digest in the file the
repository labels `NORMATIVE_TEST_VECTOR` is still asserted by nothing — F1's "blast
radius" claim is confirmed by execution, not just by reading.

### F3 — re-executed

```text
$ pytest -q --collect-only
E   NameError: name 'unittest' is not defined
!!! Interrupted: 1 error during collection !!!
120 tests collected, 1 error
```

`core/test_ari_observability.py` imports `from unittest import mock` (line 62) and
uses `unittest.TestCase` (lines 211, 280). No repository-wide green run of RI-PY
exists. Present on `main` today.

---

## Contradiction Search

Terms searched across the whole repository: `DQ-002` (48 files), `hash domain` (17),
`0x00` (39), `0x01` (31), `RFC 6962` (16), `leaf_hash` (12), `Merkle` (39),
`SHA-256` (53).

### C-1 — DQ-002 status: eight OPEN against one CLOSED

| Artifact | Recorded status |
|---|---|
| `closures/DQ-002_FINAL_CLOSURE.md:10,124` | **CLOSED / PASS** |
| `ck003/dq-002-hash-domain/CROSS-LANGUAGE-002-EVIDENCE.md:292` | "DQ-002 remains OPEN" |
| `ck003/dq-002-hash-domain/HASH_DOMAIN_EVIDENCE.md:61` | "DQ-002: OPEN" |
| `ck003/dq-002-hash-domain/02_hash_domain_adr.md:145` | "IMPLEMENTATION OPEN / CONFORMANCE NOT YET PROVEN" |
| `ADR-CK003-DQ002-HASH-DOMAIN.md:3` | PROPOSED |
| `ck003/APS001_INV_MATRIX/…:26` | "OPEN — DQ-002 + canonical bytes required" |
| `ck003/gates/GATE_A_…:18` | "DECIDED / IMPLEMENTATION PENDING" |
| `ck003/handover-assessment/03_DECISIONS.md:21` | "**OPEN.** Two ADRs exist for one decision" |
| `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md:54` | "DQ-002 final closure: BLOCKED" |

The one CLOSED artifact is the newest — commit `19ddeef`, 2026-08-20 — and was
committed **one day after** the evidence ledger (`3e848fa`, 2026-08-19) that says
DQ-002 is open. Its §6 states the whole basis:

```text
DQ-006 PASS → … → RFC-6962 leaf equality → DQ-002 FINAL CLOSURE
```

It does not mention the node domain, tree shape, odd-node promotion, the empty tree,
the PROPOSED ADR, any of the three defects, or the RI-PY divergence.

The repository had already written the rule that forbids this
(`ck003/handover-assessment/09_RECOMMENDED_SEQUENCE.md:145`):

> "Do not mark DQ-002, DQ-003 or DQ-004 closed on the strength of DQ-006."

### C-2 — leaf input domain: canonical bytes vs raw bytes

See N-2. A normative split, not a wording difference.

### C-3 — cross-corpus status

RI-RS `main` fixtures say "DQ-002 and DQ-006 unresolved; these bytes carry no
specification standing" while `aura-specification` `main` says CLOSED.

### C-4 — two ADRs, one decision, neither superseding the other

Both PROPOSED; `03_DECISIONS.md:21` already records this.

### C-5 — fixture identifier collision

`CK003-DQ002-001` (DQ002-A3, above).

### C-6 — `protocol_version` disagreement between fixtures

`FIX-…-2LEAF` declares `"1.0-DRAFT"`; CANONICAL-001 declares `"1.0"`.

**Per §10 of the audit order, an unresolved normative contradiction ⇒ BLOCKED.**
Six are recorded. None was silently repaired.

### Consistency confirmed (no contradiction)

The node formula `SHA-256(0x01 ‖ left ‖ right)` is stated **identically** in every
one of the eleven locations that state it. Domain constants `0x00`/`0x01` are
consistent everywhere. There is no disagreement about the node domain anywhere in
the corpus.

---

## DQ-006 Interaction

DQ-006 supplies bytes; DQ-002 decides what is done with them and with every node
above them.

| DQ-002 requirement | Strengthened by DQ-006 / CANONICAL-001? | Independently evidenced by? |
|---|---|---|
| R1 leaf domain | **Yes** — one leaf, both engines, byte-exact | oracle selftest; 2LEAF fixture |
| R2 node domain | **No** | oracle; edge matrix; comparator |
| R3 raw-byte boundaries | Partly — leaf only | NC-2, NC-3 |
| R4 tree shape | **No** | oracle `emit`, N = 0…8 |
| R5 odd-node promotion | **No** | NC-4, NC-4b |
| R6 empty tree | **No** | oracle `ok empty`; RI-RS test |
| R7 fixture equality | Only for the CANONICAL-001 vector | comparator, exit 0 |
| R8 canonical-byte binding | Supplies the bytes; **does not resolve N-2** | — |

**CANONICAL-001 is a single-leaf vector. It contains no node, no tree and no proof.**
It cannot evidence five of DQ-002's seven rules, and it is not used to here.

DQ-006's own documents agree: `ck003/dq-006-closure/DQ-006-CLOSURE.md` §9 and
`ck003/DQ-006_EVIDENCE_INDEX.md` — "`DQ-002 = NOT CLOSED BY THIS PACKAGE`".

---

## Traceability

Each link is marked. **✗** = broken.

| Stage | R1 leaf | R2 node | R4 shape | R5 odd | R6 empty | R8 canon. binding |
|---|---|---|---|---|---|---|
| Normative specification | ✅ `APS-001` §7.1 | ✅ `APS-001` §7.1 | **✗ N-1** | **✗ N-1** | **✗** | ⚠ split (N-2) |
| ADR | ⚠ two, disagreeing | ✅ both agree | ⚠ PROPOSED | ⚠ PROPOSED | ⚠ PROPOSED | **✗** |
| Fixture / vector | ✅ 2LEAF | ✅ 2LEAF | ✅ edge matrix | ✅ edge matrix | ✅ HD-007 | **✗** |
| Implementation | ⚠ RI-RS only in prod | ⚠ RI-RS only in prod | ⚠ RI-RS only | ⚠ RI-RS only | ⚠ RI-RS only | **✗** |
| Conformance test | **✗ no CONF-0xx** | **✗ no CONF-0xx** | **✗** | **✗** | **✗** | **✗** |
| Evidence | ✅ executed | ✅ executed | ✅ executed | ✅ executed | ✅ executed | ✅ CL-001 |
| Cross-language evidence | ✅ CL-002 | ✅ CL-002 | ✅ CL-002 | ✅ CL-002 | ✅ CL-002 | ✅ CL-001 |

**The most consequential broken link:** *no CONF identifier covers the Merkle hash
domain at all.* CONF-003 is canonicalization; CONF-010 is evidence hashes. DQ-002 has
no conformance test in the specification, so `APS-400`'s matrix cannot reference one
and `APS-500` cannot bind a fixture to one.

---

## Gaps

| ID | Gap |
|---|---|
| G-1 | "The approved Aura Merkle profile" (`APS-001` §7.2) does not exist. Tree shape and odd-node behaviour have no normative source |
| G-2 | Leaf input domain unresolved: canonical bytes vs raw bytes (N-2) |
| G-3 | No CONF identifier for the Merkle hash domain |
| G-4 | `APS-500` is `TODO`; `FIX-…-2LEAF` and `FIX-…-EDGE-MATRIX` remain `PROPOSED` — ADR gate item C4 unmet |
| G-5 | Both ADRs PROPOSED; ADR gate item C1 unmet |
| G-6 | Empty-tree admissibility undecided; three implementations behave three ways |
| G-7 | No version marker separates RFC-6962 evidence from legacy RI-PY evidence, though the ADR's migration rule requires the distinction |
| G-8 | `protocol_version` disagreement between fixtures (`1.0-DRAFT` vs `1.0`) |
| G-9 | `schema_version` participation in the leaf domain undecided |
| G-10 | `event_type` participation undecided; registry empty |
| G-11 | F2: inclusion proofs do not bind `tree_size`; DQ-002 is silent |
| G-12 | GAP-NC1 / NC2 / NC3 — three negative controls unasserted |
| G-13 | Evidence unreachable: both emitters and RI-PY's entire harness unmerged; RI-PY `main` has no DQ-002 evidence and no DQ-002 CI |
| G-14 | F1 uncorrected, and unasserted by any test |
| G-15 | F3 uncorrected; no repository-wide green RI-PY run |
| G-16 | `core/merkle.py` — second production divergence, unanalysed (DQ002-A2) |
| G-17 | `CK003-DQ002-001` identifier collision (DQ002-A3) |
| G-18 | `closures/DQ-002_FINAL_CLOSURE.md` closes on DQ-006 alone (C-1) |

---

## Required Remediation

Reported separately, as §14 requires. **None of this was applied.** All of it is
Custodian or Chief Architect work.

**Normative — must precede closure**

1. Rule on G-2 (leaf input domain). Everything downstream is shaped by it.
2. Approve one ADR; mark the other SUPERSEDED (G-5, C-4).
3. Write tree shape, odd-node promotion and empty-tree semantics into an APS
   document, or publish the "approved Aura Merkle profile" `APS-001` §7.2 already
   cites (G-1, G-6).
4. Allocate a CONF identifier for the Merkle hash domain; register it in `APS-400`
   (G-3).
5. Promote the two fixtures to normative under `APS-500` (G-4).
6. Decide G-7 (version marker) and G-11 (tree-size binding; F2 proposes the wording).

**Evidence corrections — non-semantic**

7. Correct `03_cross_language_fixture.json` `node.digest_hex` to
   `bc6b943b820c449acf880d293c216a24a8066b153f87f2361fae2beda3a72641`, and bind that
   file to an executable assertion so a published vector cannot again go unchecked
   (G-14). Both implementations already emit the correct value.
8. Reconcile the `CK003-DQ002-001` collision — rename one, or bind both (G-17).
9. Align the `protocol_version` values across fixtures (G-8).
10. Add the three missing negative controls (G-12). Test-only; touches no production
    code.
11. Fix `import unittest` in RI-PY `core/test_ari_observability.py` under a separate
    change, then record a repository-wide green run (G-15).

**Reachability**

12. Merge the conformance evidence in both implementation repositories, or record why
    it stays unmerged (G-13, CFL-004).
13. Add a DQ-002 CI workflow to RI-PY, mirroring RI-RS's (G-13).

**Analysis**

14. Extend the DQ-002 divergence analysis to `core/merkle.py` (G-16).
15. Re-examine `closures/DQ-002_FINAL_CLOSURE.md` (G-18). This audit does not alter it.

---

## FINAL VERDICT

```text
DQ-002: BLOCKED
```

**Why not PASS.** PASS requires every closure criterion to be evidenced. The
governing ADR's own six-item gate has two items unmet (C1: no approved contract;
C4: no normative fixture). Two of the seven rules — tree shape and odd-node
promotion — have no normative source at all, because `APS-001` §7.2 defers them to a
document that does not exist. The two ADRs disagree on what enters a leaf. No
conformance test in the specification covers the Merkle hash domain. Six unresolved
normative contradictions are recorded, and §10 of this audit's own terms makes any
one of them sufficient for BLOCKED. Two defects remain open, one of them a wrong
digest in a file labelled `NORMATIVE_TEST_VECTOR` that this audit confirmed is
asserted by nothing.

**Why not FAIL.** The contract itself is sound and the evidence behind it is real
and reproducible. The repository's own oracle runs clean (exit 0) and regenerates the
committed edge-matrix fixture byte-for-byte. All five recorded artifact hashes
reproduce. The comparator reports `EQUAL + CONFORMANT` (exit 0) and — tested here on
copies — genuinely goes red when values are mutated, including when both files agree
with each other but disagree with the oracle. RI-RS implements the contract correctly
on `main` with CI. RI-PY's conformance module implements it correctly and passes
158/158. Nothing measured contradicts the RFC 6962 decision.

DQ-002 is blocked on **governance and completeness**, not on cryptography. The
missing pieces are an approved ADR, a normative tree/odd-node rule, a conformance
test identifier, promoted fixtures, reachable evidence, and two uncorrected defects.

**No closure commit is prepared, and none should follow automatically from this
document.**

---

*This audit records findings. It resolves nothing, approves nothing, and confers no
normative status. No production code, protocol semantics, hash domain,
canonicalization or Merkle implementation was modified. All mutation testing was
performed on scratch copies.*

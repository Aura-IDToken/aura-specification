# DQ-002 FINAL CLOSURE AUDIT

**Classification:** EVIDENCE / AUDIT — non-normative. This document decides nothing,
approves nothing, and closes nothing.
**Audit date:** 2026-08-20
**Auditor scope:** `aura-specification`, `aura-poc-a-core-v3.3` (RI-PY),
`aura-guard-v1.3` (RI-RS)
**Method:** specification read first, then implementation source, then execution.
Every digest quoted below was recomputed locally; every test result was produced by
running the test, not by reading a prior report.

**Repository state at audit:**

| Repository | Branch | HEAD | Working tree |
|---|---|---|---|
| `aura-specification` | `claude/ck003-canonical-serialization-hjlaba` | `704832afa1ca76f48d98a3c0e84f845ddd3c98fa` | clean |
| RI-PY `aura-poc-a-core-v3.3` | `claude/ck003-canonical-serialization-hjlaba` (= `origin/main`) | `64bf959b1d23fbd5433723476c611ab66d423953` | clean, unmodified |
| RI-RS `aura-guard-v1.3` | `claude/ck003-canonical-serialization-hjlaba` (= `origin/main`) | `35082d7b4880dad780fb55a1a5f3ac0ef4322674` | clean, unmodified |

No production runtime, canonicalization implementation, or CANONICAL-001 value was
modified by this audit.

---

## 1. Normative definition

### 1.1 What DQ-002 is

DQ-002 is the **Merkle hash-domain decision**: which bytes are hashed to form a
leaf, which to form an interior node, how the tree is shaped, and what happens at
the odd-node and empty-tree edges. It is *not* the canonical serialization
decision — that is DQ-006 / APS-200 §8, and both DQ-002 ADRs say so explicitly.

### 1.2 Where the normative text lives

| Source | Status | Content |
|---|---|---|
| `specification/APS-001_PROTOCOL_SPECIFICATION.md` §7.1–7.2 | `0.2-DRAFT` — "ARCHITECTURE REVIEW REQUIRED" | leaf `0x00`, node `0x01`, 32 raw digest bytes, "RFC 6962-style"; **defers tree construction and odd-node behaviour to "the approved Aura Merkle profile"** |
| `aps/APS-300_EVIDENCE_MODEL.md` §5.1 | `1.0-DRAFT` | domain-separation table; explicitly assigns leaf/node ownership to "APS-001 §7 / DQ-002" |
| `aps/APS-200_CANONICAL_DATA_MODEL.md` §8.4 | `1.0-DRAFT` | states which bytes enter the leaf; explicitly **does not** define Merkle semantics |
| `ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` | **PROPOSED — awaiting Chief Architect approval** | the 7-rule decision, incl. tree shape, odd-node promotion, empty tree |
| `ck003/dq-002-hash-domain/02_hash_domain_adr.md` | **PROPOSED — pending review and merge** | a *second* ADR for the same decision |

### 1.3 UNRESOLVED — the "approved Aura Merkle profile" does not exist

`APS-001 §7.2` makes tree construction and odd-node behaviour conditional on a
document it names but never identifies:

> "tree construction/odd-node behaviour MUST follow the approved Aura Merkle profile."

A repository-wide search finds that phrase **exactly once** — in that sentence. No
such profile exists in `aps/`, `specification/`, `adrs/`, or anywhere else. The
normative chain therefore terminates in a dangling reference precisely at the two
rules that distinguish DQ-002 from an ordinary hash.

**Status: UNRESOLVED.** Not invented here. The candidate content exists in the
PROPOSED ADR; promoting it is a Custodian act.

### 1.4 UNRESOLVED — the two ADRs disagree on the leaf input domain

Both ADRs agree on `SHA-256(0x00 || …)` and `SHA-256(0x01 || L || R)`. They do not
agree on what goes into the leaf:

| ADR | Leaf input |
|---|---|
| `02_hash_domain_adr.md` §2 | `SHA-256(0x00 \|\| canonical_bytes)` — **canonical bytes** |
| `ADR-CK003-DQ002-HASH-DOMAIN.md` §Decision (1) | `SHA-256(0x00 \|\| leaf_data_bytes)` / `raw_data_bytes` — **arbitrary raw bytes** |

The fixtures inherit the disagreement. `FIX-CK003-DQ002-RFC6962-2LEAF` hashes the
raw octets `61`/`62` (the letters `a`, `b`) — not canonical JSON. And
`03_cross_language_fixture.json` hashes a pipe-delimited text string under a field
that reads `"status": "EXPLICITLY_OUT_OF_SCOPE_FOR_DQ002"` for canonical
serialization. Meanwhile `APS-300 §5.1` and `APS-200 §8.4` both write the leaf as
`SHA-256(0x00 || canonical_bytes)`.

So the specification says the leaf is over *canonical bytes*, while the DQ-002
evidence base tests the leaf over *arbitrary bytes*. Both are coherent designs.
They are not the same design, and DQ-002 cannot close without picking one.

**Status: UNRESOLVED.** Reported, not reconciled — per `CLAUDE.md` and §4 of the
governing execution order.

---

## 2. Closure criteria

DQ-002's closure conditions are not invented by this audit. They are the six-item
**Conformance gate** the governing ADR sets for itself, plus the six conditions the
CROSS-LANGUAGE-002 evidence ledger records as outstanding.

### 2.1 The ADR's own gate

| # | Condition (verbatim from `ADR-CK003-DQ002-HASH-DOMAIN.md`) | Status |
|---|---|---|
| C1 | Chief Architect approval recorded | **FAIL** — ADR still `PROPOSED`; a second ADR also `PROPOSED` |
| C2 | APS-200 §8 updated with the canonical byte-level rule | **PASS** — enacted 2026-08-20 (CK-003) |
| C3 | APS-300 evidence hash scope reconciled with the selected canonical serialization | **PASS** — APS-300 §5.1 |
| C4 | APS-500 fixture promoted from proposal to normative fixture | **FAIL** — APS-500 is `TODO`; `FIX-…-2LEAF` still `"status": "PROPOSED"` |
| C5 | RI-PY and RI-RS cross-language conformance tests both pass | **PASS on evidence, BLOCKED on reachability** — see §3, §6, §7 |
| C6 | Migration/version semantics documented | **PARTIAL** — the ADR states a migration rule; no version marker distinguishes RFC-6962 from legacy evidence (see §3 row R11) |

### 2.2 The evidence ledger's outstanding conditions

`ck003/dq-002-hash-domain/CROSS-LANGUAGE-002-EVIDENCE.md` §12 records
**CONDITIONAL PASS** and closes with the sentence:

> **DQ-002 remains OPEN. This document does not close it.**

Its six stated reasons, re-verified in this audit: (1) ADR is PROPOSED — confirmed;
(2) DEFECT-F1 uncorrected — confirmed arithmetically in §9.3; (3) DEFECT-F2 open —
confirmed; (4) DEFECT-F3 open — confirmed by running the collection in §6.4;
(5) no CI execution — partly overtaken, see §7.4; (6) RI-PY production path still
legacy — confirmed by execution in §6.2.

### 2.3 The contradiction this audit must report

`closures/DQ-002_FINAL_CLOSURE.md` records **`DQ-002 = CLOSED / PASS`**.

Its §6 gives the entire chain of reasoning:

> ```text
> DQ-006 PASS → … → RFC-6962 leaf equality → DQ-002 FINAL CLOSURE
> ```

That closure was committed in `19ddeef` on **2026-08-20**, one day *after* the
evidence ledger (`3e848fa`, 2026-08-19) that says DQ-002 is open and lists six
unmet conditions. The closure document does not mention the node domain, tree
shape, odd-node promotion, the empty tree, the PROPOSED ADR, any of the three
defects, or the RI-PY production divergence. It closes DQ-002 on the strength of
DQ-006 alone.

The repository's own handover assessment anticipated exactly this
(`ck003/handover-assessment/09_RECOMMENDED_SEQUENCE.md:145`):

> "Do not mark DQ-002, DQ-003 or DQ-004 closed on the strength of DQ-006."

**Eight artifacts record DQ-002 as OPEN / PROPOSED / BLOCKED; one records it as
CLOSED.** The one is the newest and is the only one that reasons solely from
DQ-006.

**Status: UNRESOLVED CONTRADICTION.** This audit does not alter either side.

---

## 3. Requirement → implementation → test → evidence matrix

Ten fields per row, as required. "spec loc." = specification location.

### R1 — Leaf domain: `SHA-256(0x00 || bytes)`

| Field | Finding |
|---|---|
| 1. Requirement | Leaf digest is SHA-256 over `0x00` (one raw octet) concatenated with the leaf bytes |
| 2. Spec loc. | `APS-001` §7.1–7.2; `APS-300` §5.1; `APS-200` §8.4; ADR rule 1 |
| 3. Impl. loc. | RI-RS `src/merkle.rs:29-34` `leaf_hash`. RI-PY: **none in production**; `conformance/merkle/rfc6962.py` on an unmerged branch |
| 4. Conformance test | RI-RS `tests/ck003_dq002_ri_rs_conformance.rs`; RI-PY `conformance/merkle/test_dq002_rfc6962.py` (unmerged). **No CONF-0xx in the specification covers it** |
| 5. Fixture | `FIX-CK003-DQ002-RFC6962-2LEAF` (PROPOSED); `HD-005` (RI-RS, "no specification standing") |
| 6. RI-PY evidence | 158/158 pass, re-executed by this audit — on unmerged branch only |
| 7. RI-RS evidence | 1/1 pass, re-executed by this audit, on `main` |
| 8. Cross-language | CROSS-LANGUAGE-002 §5; leaf equality PASS |
| 9. **Status** | **PASS (semantics) / BLOCKED (normative + reachability)** |
| 10. Ambiguity | §1.4 — leaf input domain is canonical bytes or raw bytes, unresolved |

### R2 — Node domain: `SHA-256(0x01 || left[32] || right[32])`

| Field | Finding |
|---|---|
| 1. Requirement | Interior digest over `0x01` and the two **raw 32-byte** child digests |
| 2. Spec loc. | `APS-001` §7.1–7.2; `APS-300` §5.1; ADR rule 2 |
| 3. Impl. loc. | RI-RS `src/merkle.rs:38-44` `node_hash`. RI-PY production: **contradicts it** (`audit/merkle.py` hashes hex text) |
| 4. Conformance test | Same as R1. No specification CONF test |
| 5. Fixture | `FIX-…-2LEAF` root; `HD-006`; `03_cross_language_fixture.json` — **the last one carries a wrong digest, see §9.3** |
| 6. RI-PY evidence | Conformance harness PASS (unmerged); production **FAIL by design** |
| 7. RI-RS evidence | PASS on `main` |
| 8. Cross-language | NC-2, NC-3 PASS both sides |
| 9. **Status** | **BLOCKED** |
| 10. Ambiguity | None on the formula |

### R3 — Raw bytes at every hash boundary; never hexadecimal text

| Field | Finding |
|---|---|
| 1. Requirement | ADR rule 3; `APS-001` §7.1 |
| 2. Spec loc. | `APS-001` §7.1; `APS-200` §8.4(4); ADR rule 3 |
| 3. Impl. loc. | RI-RS: `[u8; 32]` types make hex text unrepresentable. RI-PY production `audit/merkle.py:sha256(left + right)` over hex strings — **direct violation** |
| 4. Conformance test | NC-3 in both harnesses |
| 5. Fixture | `negative_expectations.hex_string_concatenation_node_domain` |
| 6. RI-PY evidence | Harness rejects `str` at the boundary (unmerged); production does the opposite |
| 7. RI-RS evidence | PASS |
| 8. Cross-language | NC-3 PASS both |
| 9. **Status** | **FAIL in RI-PY production** / PASS in conformance scope |
| 10. Ambiguity | None |

### R4 — Tree shape: RFC 6962 recursive split at largest power of two < n

| Field | Finding |
|---|---|
| 1. Requirement | ADR rule 4 |
| 2. Spec loc. | **UNRESOLVED** — `APS-001` §7.2 defers to a non-existent "approved Aura Merkle profile" (§1.3) |
| 3. Impl. loc. | RI-RS `src/merkle.rs` `largest_power_of_two_lt`, `audit_path_inner`. RI-PY production: pairwise, not recursive-split |
| 4. Conformance test | Edge matrix N=0…8 in both harnesses (unmerged for RI-PY) |
| 5. Fixture | `FIX-CK003-DQ002-RFC6962-EDGE-MATRIX.json` (not referenced by APS-500) |
| 6. RI-PY evidence | PASS in harness; production divergent |
| 7. RI-RS evidence | PASS |
| 8. Cross-language | Roots agree N=0…8 |
| 9. **Status** | **BLOCKED — no normative source** |
| 10. Ambiguity | The rule exists only in a PROPOSED ADR |

### R5 — Odd node promoted unchanged; last node never duplicated

| Field | Finding |
|---|---|
| 1. Requirement | ADR rule 5 |
| 2. Spec loc. | **UNRESOLVED** — same dangling reference as R4 |
| 3. Impl. loc. | RI-RS promotes. RI-PY production **duplicates**: `audit/merkle.py` `right = current_level[i+1] if i+1 < len else left` |
| 4. Conformance test | NC-4 (duplication must differ at N=3,5,6,7) |
| 5. Fixture | Edge matrix |
| 6. RI-PY evidence | Harness asserts non-duplication; production duplicates |
| 7. RI-RS evidence | PASS |
| 8. Cross-language | NC-4 PASS both |
| 9. **Status** | **BLOCKED — no normative source; RI-PY production divergent** |
| 10. Ambiguity | As R4 |

### R6 — Empty tree = `SHA-256("")`

| Field | Finding |
|---|---|
| 1. Requirement | ADR rule 6: "SHALL be explicitly specified wherever an empty tree is permitted" |
| 2. Spec loc. | **UNRESOLVED** — no APS document states an empty-tree value or says whether an empty tree is permitted |
| 3. Impl. loc. | RI-RS `empty_root()`. RI-PY production **raises `ValueError`** on empty leaves — a third behaviour |
| 4. Conformance test | RI-RS `empty_tree_root_is_sha256_of_nothing` |
| 5. Fixture | `HD-007` (RI-RS, "no specification standing") |
| 6. RI-PY evidence | Harness N=0 PASS; production rejects empty |
| 7. RI-RS evidence | PASS, verified locally: `e3b0c442…2b855` |
| 8. Cross-language | N=0 root agrees |
| 9. **Status** | **UNRESOLVED in specification** |
| 10. Ambiguity | Whether an empty tree is permitted at all is undecided |

### R7 — Cross-language byte-level fixture equality

| Field | Finding |
|---|---|
| 1. Requirement | ADR rule 7 |
| 2. Spec loc. | ADR rule 7; `APS-001` §9 |
| 3. Impl. loc. | Both emitters, both on unmerged branches |
| 4. Conformance test | `tools/compare_vectors.py` |
| 5. Fixture | Edge matrix + 2LEAF |
| 6. RI-PY evidence | `RI-PY-VECTORS.json`, SHA `82e47587…` |
| 7. RI-RS evidence | `RI-RS-VECTORS.json`, identical SHA |
| 8. Cross-language | `RESULT: EQUAL + CONFORMANT`, exit 0 |
| 9. **Status** | **PASS (semantics) / BLOCKED (both emitters unmerged)** |
| 10. Ambiguity | None |

### R8 — Canonical-serialization binding of the leaf

| Field | Finding |
|---|---|
| 1. Requirement | Leaf bytes are the APS-200 §8 canonical bytes |
| 2. Spec loc. | `APS-200` §8.4; `APS-300` §5.1 |
| 3. Impl. loc. | RI-RS `leaf_hash` takes `&[u8]` — domain-agnostic. RI-PY production `core/merkle.py` uses `json.dumps(sort_keys=True)` — **not JCS** |
| 4. Conformance test | CONF-003 covers canonicalization; **nothing tests the join between canonical bytes and the leaf** |
| 5. Fixture | CANONICAL-001 (leaf only, single leaf, no tree) |
| 6. RI-PY evidence | CANONICAL-001 PASS (unmerged); `core/merkle.py` divergent, §6.3 |
| 7. RI-RS evidence | CANONICAL-001 PASS on `main` |
| 8. Cross-language | CROSS-LANGUAGE-001 PASS |
| 9. **Status** | **BLOCKED** |
| 10. Ambiguity | §1.4 — the two ADRs disagree; DQ-002 fixtures hash non-canonical bytes |

### R9 — `protocol_version` binding

| Field | Finding |
|---|---|
| 1. Requirement | Changes to hash domains MUST be version-bound (`APS-001` §12) |
| 2. Spec loc. | `APS-001` §12; `APS-200` §8.6 binds **canonicalization** to `protocol_version` |
| 3. Impl. loc. | None — no implementation carries a hash-domain version marker |
| 4. Conformance test | CONF-008 (version compatibility) — does not cover the hash domain |
| 5. Fixture | `FIX-…-2LEAF` declares `"protocol_version": "1.0-DRAFT"`; CANONICAL-001 declares `"1.0"` — **two different values for one protocol** |
| 6. RI-PY evidence | None |
| 7. RI-RS evidence | None |
| 8. Cross-language | Not tested |
| 9. **Status** | **UNRESOLVED** |
| 10. Ambiguity | No APS text binds the *Merkle profile* to a version; §8.6 binds only canonicalization. The ADR's migration rule requires distinguishing RFC-6962 from legacy evidence, and no mechanism exists to do so |

### R10 — `schema_version` binding

| Field | Finding |
|---|---|
| 1. Requirement | Not stated for the hash domain |
| 2. Spec loc. | `APS-001` §12 / `APS-200` §8.6 say `schema_version` does **not** select a canonicalization profile; neither addresses the Merkle profile |
| 3.–8. | Not applicable / no evidence |
| 9. **Status** | **UNRESOLVED — not applicable as currently written** |
| 10. Ambiguity | Merkle leaves are byte sequences; whether an entity's `schema_version` participates in the leaf domain is undecided. Not invented here |

### R11 — `event_type` binding

| Field | Finding |
|---|---|
| 1. Requirement | Not stated for the hash domain |
| 2. Spec loc. | `aps/EVENT_TYPE_REGISTRY.md` §5: no token is normative yet |
| 3. Impl. loc. | Not applicable — DQ-002 leaves are raw bytes |
| 4.–8. | Not tested; `FIX-…-2LEAF` leaves are `a`/`b`, carrying no event type |
| 9. **Status** | **UNRESOLVED — out of DQ-002 scope as written** |
| 10. Ambiguity | CANONICAL-001 carries `AUDIT_RECORD` against an empty registry (CFL-005). That affects the DQ-006 vector, not the DQ-002 raw-byte domain. Unresolved either way |

### R12 — Absence of production-runtime divergence

| Field | Finding |
|---|---|
| 1. Requirement | Implied by `APS-001` §9 (implementations MUST agree on shared fixtures) |
| 2. Spec loc. | `APS-001` §9 |
| 3. Impl. loc. | RI-PY `audit/merkle.py`, `core/merkle.py`; RI-RS `src/merkle.rs` |
| 4. Conformance test | None in production scope for RI-PY |
| 5. Fixture | — |
| 6. RI-PY evidence | **Divergent — executed and measured, §6.2 and §6.3** |
| 7. RI-RS evidence | Conformant |
| 8. Cross-language | Divergence is between RI-PY production and everything else |
| 9. **Status** | **FAIL** |
| 10. Ambiguity | The ADR deliberately does not require remediation, so this is not a contract violation. It does mean no closure may claim "no production divergence" |

---

## 4. CANONICAL-001 evidence

**Not modified by this audit.** Values re-verified as internally consistent:

```text
canonical bytes  7b226576656e745f74797065223a2241554449545f5245434f5244…  (100 octets)
SHA-256          b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
leaf             ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

**What CANONICAL-001 proves for DQ-002:** the leaf domain `SHA-256(0x00 || bytes)`,
for one leaf, in both implementations.

**What it does not prove, and cannot:** the node domain, the tree shape, odd-node
promotion, the empty tree, audit paths, or proof verification. It is a single-leaf
vector. It contains no node, no tree and no proof. Five of DQ-002's seven rules are
untouched by it.

This is the precise reason the closure chain in `closures/DQ-002_FINAL_CLOSURE.md`
§6 does not carry: RFC-6962 leaf equality is one rule out of seven.

---

## 5. DQ-006 dependency

DQ-006 is **CLOSED / PASS** and that status is not disturbed here. Its relationship
to DQ-002 is one of *supply*, not *entailment*:

```text
DQ-006 supplies ─► the byte sequence that enters a leaf
DQ-002 decides  ─► what is done with that sequence, and with every node above it
```

| DQ-002 rule | Covered by DQ-006? |
|---|---|
| R1 leaf domain | **Yes** — single leaf |
| R2 node domain | No |
| R3 raw bytes at boundaries | Partly — leaf only |
| R4 tree shape | No |
| R5 odd-node promotion | No |
| R6 empty tree | No |
| R7 cross-language fixture equality | Only for the CANONICAL-001 vector |

DQ-006's own closure document says so twice: `ck003/dq-006-closure/DQ-006-CLOSURE.md`
§9 — "It does not establish that every existing Aura object or every existing
production hash domain is already conformant" — and `ck003/DQ-006_EVIDENCE_INDEX.md`
— "`DQ-002 = NOT CLOSED BY THIS PACKAGE`".

---

## 6. RI-PY evidence

Repository `Aura-IDToken/aura-poc-a-core-v3.3`, `origin/main` = `64bf959b`.
Nothing in this repository was modified; the conformance tree was extracted
read-only with `git archive`.

### 6.1 Conformance harness — PASS, but not on `main`

```text
$ pytest -q conformance/merkle/          158 passed in 0.18s
```

Re-executed by this audit against `origin/claude/aura-cross-language-002-6t2kdo`.
The result is genuine.

**`conformance/merkle/` does not exist on `origin/main`.** A ref-by-ref search of
every remote branch finds it in exactly one place — that unmerged branch, which is
**not an ancestor of `origin/main`**. A reviewer cloning RI-PY at `main` finds no
DQ-002 conformance evidence at all.

### 6.2 Production `audit/merkle.py` — measured divergence

Executed directly against `origin/main`:

```text
MerkleTree(['a','b']).root      62af5c3cb8da3e4f25061e829ebeea5c7513c54949115b1acc225930a90154da
DQ-002 fixture expected root    b137985ff484fb600db93107c77b0365c80d78f5b429ded0fd97361d077999eb
```

Divergent on all three rules: leaf without `0x00`; node over concatenated
**hexadecimal text**; odd node **duplicated**.

Two observations follow. First, `.github/workflows/execution-checks.yml` runs
`scripts/generate_determinism_report.py`, which imports `audit.merkle.MerkleTree` —
so RI-PY's CI actively exercises and publishes artifacts from the non-conformant
Merkle on every run. Second, and recorded as a new evidence discrepancy:

> **Finding DQ002-A1 (new).** `ck003/cross-language-002/CROSS-LANGUAGE-002-EVIDENCE.md`
> §4 records the RI-PY two-leaf "negative preflight" root as
> `fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603`. Executing
> `audit/merkle.py` at `origin/main` produces `62af5c3c…0154da` for leaves `a`/`b`,
> by both the plain and pre-hashed constructors. The recorded value is not
> reproducible from RI-PY `main` as documented. It may have been computed over
> different leaf payloads; the document does not say. **Reported, not corrected** —
> the discrepancy is in an evidence artifact, and it is a negative control, so
> nothing downstream depends on its value.

### 6.3 Production `core/merkle.py` — a second, unrecorded divergence

```python
hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
```

Executed on the CANONICAL-001 object:

```text
core/merkle.py bytes   {"event_type": "AUDIT_RECORD", "payload": {"value": 42}, …}   ← spaces
APS-200 §8 canonical   {"event_type":"AUDIT_RECORD","payload":{"value":42},…}
core/merkle.py digest  c3838d1e79350c4a2d44f30ea3adee222f4fa41eb7adb04998561d1bf0ec2a92
APS-200 §8 SHA-256     b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

`json.dumps` default separators insert whitespace, so these are not canonical bytes
under APS-200 §8, and there is no `0x00` prefix. This is a **third** hash domain in
the programme.

> **Finding DQ002-A2 (new).** Both DQ-002 ADRs analyse `audit/merkle.py` only.
> `core/merkle.py` — `MerkleAttestor.generate_leaf`, which mints Event Trust
> Certificates — appears in no DQ-002 artifact, no defect record, and no conflict
> register entry. The DQ-002 divergence analysis is incomplete.

### 6.4 DEFECT-F3 — still open, re-confirmed

```text
$ pytest -q --collect-only
E   NameError: name 'unittest' is not defined
!!! Interrupted: 1 error during collection !!!
120 tests collected, 1 error
```

`core/test_ari_observability.py` imports `from unittest import mock` (line 62) but
uses `unittest.TestCase` (lines 211, 280). Collection aborts, so **no repository-wide
green run of RI-PY exists.** Present at `main` today. Not fixed here — outside
DQ-002 scope, per the defect record's own reasoning.

---

## 7. RI-RS evidence

Repository `Aura-IDToken/aura-guard-v1.3`, `origin/main` = `35082d7b`. Unmodified.

### 7.1 Source conforms

`src/merkle.rs` implements `leaf_hash` (`0x00`), `node_hash` (`0x01`, `&[u8; 32]`
children), `empty_root`, the recursive split at `largest_power_of_two_lt`, audit-path
construction and `verify_audit_path` with odd-node promotion. The `[u8; 32]` typing
makes hexadecimal text unrepresentable at a hash boundary — R3 is enforced by the
type system rather than by a check.

### 7.2 Executed on `main`

```text
$ cargo test --test ck003_dq002_ri_rs_conformance
test ri_rs_matches_ck003_dq002_fixture ... ok
test result: ok. 1 passed; 0 failed
```

### 7.3 Fixture identifier collision

> **Finding DQ002-A3 (new).** Both repositories publish a fixture with the identifier
> **`CK003-DQ002-001`**, and they are different fixtures:
>
> | | `aura-specification/ck003/dq-002-hash-domain/03_cross_language_fixture.json` | `aura-guard-v1.3/audit/fixtures/ck003_dq002_001.json` |
> |---|---|---|
> | Leaf text | `agent_id=A001\|ari=95000\|…` | `agent_id=MACHINE_ACCOUNT_001\|ari=95000\|…` |
> | Leaf digest | `ba2749fe…fd123` | `f7acc9aa…58e4b` |
> | Node | `0x01 \|\| 00×32 \|\| ff×32` | `0x01 \|\| leaf \|\| leaf` |
> | Self-declared status | `NORMATIVE_TEST_VECTOR` | — |
>
> The RI-RS values are arithmetically correct (verified: leaf `f7acc9aa…`, node
> `1b3ff765…`). The spec-side node digest is not (§9.3). The RI-RS test asserts
> against the RI-RS file, so the identifier shared with a `NORMATIVE_TEST_VECTOR`
> in the specification is bound to nothing. One identifier, two meanings.

### 7.4 CI — present in RI-RS, absent in RI-PY

`.github/workflows/ck003-dq002.yml` runs the RI-RS conformance test on pull
requests to `main` and on `ck003/**` pushes. This partly overtakes the ledger's
"no CI execution" item — **for RI-RS only**. RI-PY has no DQ-002 workflow on any
branch.

### 7.5 RI-RS fixtures still declare DQ-002 unresolved

`tests/fixtures/hash_domains/HD-005…007` each carry, on `main` today:

> `"not_canonical": "DQ-002 and DQ-006 unresolved; these bytes carry no specification standing."`

RI-RS `main` therefore states DQ-002 is unresolved while `aura-specification` `main`
states it is CLOSED. **Reported, not reconciled.**

---

## 8. Cross-language evidence

CROSS-LANGUAGE-002 — **CONDITIONAL PASS**, and this audit does not upgrade it.

What it establishes, against an independent third producer (GNU coreutils
`sha256sum`) that neither implementation shares code with: identical leaf digests,
node digests and roots for N = 0…8; all 36 audit paths; proof verification; and ten
negative controls (NC-1…NC-10) on both sides. The comparator
(`tools/compare_vectors.py`) imports neither implementation and reported
`EQUAL + CONFORMANT`, exit 0.

That is a genuinely strong semantic result, and it is the reason this audit's
verdict is BLOCKED rather than FAIL.

Its limits, all recorded in the ledger itself: it measures conformance against a
**PROPOSED** contract; **both** emitters live on the same unmerged branch
(`claude/aura-cross-language-002-6t2kdo`) in both repositories; and it explicitly
declines to close DQ-002.

---

## 9. Hash-domain verification

Every value below was recomputed locally with CPython `hashlib` during this audit.

### 9.1 `FIX-CK003-DQ002-RFC6962-2LEAF` — fully correct

| Value | Computed | Matches fixture |
|---|---|---|
| `leaf_a` = SHA-256(`00`‖`61`) | `022a6979e6dab7aa5ae4c3e5e45f7e977112a7e63593820dbec1ec738a24f93c` | ✅ |
| `leaf_b` = SHA-256(`00`‖`62`) | `57eb35615d47f34ec714cacdf5fd74608a5e8e102724e80b24b287c0c27b6a31` | ✅ |
| `root` = SHA-256(`01`‖a‖b) | `b137985ff484fb600db93107c77b0365c80d78f5b429ded0fd97361d077999eb` | ✅ |
| empty root = SHA-256("") | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | ✅ |

### 9.2 Domain separation holds

CANONICAL-001's leaf under the interior domain `0x01`, and under an ASCII `"0x00"`
prefix, both differ from the recorded leaf — verified as negative controls in
`scripts/validate_canonical_001.py` (10/10 PASS).

### 9.3 `03_cross_language_fixture.json` — DEFECT-F1 independently confirmed

| Field | Value |
|---|---|
| Declared preimage | `01` ‖ `00`×32 ‖ `ff`×32, 65 octets — length correct |
| SHA-256 of that preimage | `bc6b943b820c449acf880d293c216a24a8066b153f87f2361fae2beda3a72641` |
| Recorded `node.digest_hex` | `e2bd2dcef148b54e935fe552c7c83978103f85b2d970d55f482717bb3904b7ac` |
| Match | **NO** |

The file's `leaf.digest_hex` (`ba2749fe…`) and `canonical_serialization.length_bytes`
(58) are correct; only the node digest is wrong. The file self-designates
`"status": "NORMATIVE_TEST_VECTOR"`.

**A file the repository labels a normative test vector carries a digest that is not
the hash of the bytes the same file declares, and it is still uncorrected.** Not
corrected here: editing a normative test vector is a Custodian act, and DEFECT-F1
already requests exactly that.

---

## 10. Remaining ambiguities

| ID | Ambiguity | Marked |
|---|---|---|
| A-1 | "The approved Aura Merkle profile" (`APS-001` §7.2) names a document that does not exist. Tree shape and odd-node behaviour have no normative source | **UNRESOLVED** |
| A-2 | The two DQ-002 ADRs disagree: leaf over `canonical_bytes` vs over arbitrary `raw_data_bytes`. APS-300 §5.1 says canonical bytes; the DQ-002 fixtures hash non-canonical bytes | **UNRESOLVED** |
| A-3 | Empty-tree semantics: is an empty tree permitted? RI-RS returns `SHA-256("")`; RI-PY production raises `ValueError`; no APS text decides | **UNRESOLVED** |
| A-4 | No version marker distinguishes RFC-6962 evidence from legacy RI-PY evidence, though the ADR's migration rule requires the distinction. `APS-200` §8.6 binds canonicalization, not the Merkle profile | **UNRESOLVED** |
| A-5 | `protocol_version` is `1.0-DRAFT` in the DQ-002 fixture and `1.0` in CANONICAL-001 | **UNRESOLVED** |
| A-6 | `schema_version` participation in the leaf domain is undecided | **UNRESOLVED** |
| A-7 | `event_type` participation is undecided; the registry is empty (CFL-005) | **UNRESOLVED** |
| A-8 | DEFECT-F2: DQ-002 is silent on whether an inclusion proof binds `tree_size`. It does not | **UNRESOLVED** |
| A-9 | Two ADRs govern one decision, both PROPOSED, neither superseding the other | **UNRESOLVED** |
| A-10 | `CK003-DQ002-001` identifies two different fixtures in two repositories (DQ002-A3) | **UNRESOLVED** |
| A-11 | `closures/DQ-002_FINAL_CLOSURE.md` records CLOSED against eight artifacts recording OPEN, reasoning solely from DQ-006 (§2.3) | **UNRESOLVED CONTRADICTION** |

None of these was reconciled by this audit.

---

## 11. Closure decision

### What is proven

The **semantic** contract is in good shape, and the evidence behind it is real. Two
independent implementations agree byte-for-byte on leaf digests, node digests, roots
for N = 0…8, all 36 audit paths, proof verification and ten negative controls, checked
against a third-party oracle. This audit re-executed both suites rather than trusting
the reports: RI-PY 158/158, RI-RS 1/1 on `main`, plus the CANONICAL-001 pair from the
prior task. Nothing here suggests the RFC 6962 decision is wrong.

### What is not proven

Closure is a governance act, and DQ-002's own gate is not met:

1. **C1 — no approved contract.** Both ADRs are `PROPOSED`. Conformance is being
   measured against a proposal, and two proposals disagree on the leaf input domain.
2. **A-1 — the normative chain is broken.** `APS-001` §7.2 defers the tree and
   odd-node rules to a document that does not exist. Two of the seven rules have no
   normative home at all.
3. **C4 — no normative fixture.** APS-500 is `TODO`; the 2-leaf fixture is still
   `PROPOSED`; the edge matrix is unreferenced by any APS.
4. **No conformance test in the specification.** CONF-003 covers canonicalization,
   CONF-010 covers evidence hashes. **Nothing covers the Merkle hash domain.** DQ-002
   has no CONF identifier.
5. **Evidence is unreachable.** Both cross-language emitters and RI-PY's entire
   conformance harness exist only on `claude/aura-cross-language-002-6t2kdo`,
   unmerged in both repositories. RI-PY `main` contains no DQ-002 evidence.
6. **DEFECT-F1 is uncorrected** — confirmed arithmetically — in a file the repository
   calls a `NORMATIVE_TEST_VECTOR`.
7. **DEFECT-F3 is uncorrected** — RI-PY cannot complete test collection, so no
   repository-wide green run exists.
8. **RI-PY production diverges** in `audit/merkle.py` and, unrecorded until now, in
   `core/merkle.py` (DQ002-A2). The ADR permits this; no closure may claim otherwise.
9. **The existing closure is unsupported.** `closures/DQ-002_FINAL_CLOSURE.md` closes
   DQ-002 on DQ-006 alone, post-dates the evidence that says DQ-002 is open, and
   addresses none of items 1–8.

### Three new findings raised by this audit

- **DQ002-A1** — the recorded RI-PY negative-preflight root is not reproducible from
  RI-PY `main`.
- **DQ002-A2** — `core/merkle.py` is a second, unanalysed production divergence and a
  third hash domain.
- **DQ002-A3** — `CK003-DQ002-001` identifies two different fixtures across the two
  repositories.

### FINAL VERDICT

```text
DQ-002 = BLOCKED
```

**BLOCKED, not FAIL.** The RFC 6962 contract is implemented correctly in RI-RS,
implemented correctly in RI-PY's conformance harness, and proven equal across both
against an independent oracle. Nothing measured contradicts the decision. What is
missing is the normative and governance scaffolding that would let a closure stand:
an approved ADR, a normative tree/odd-node rule, a normative fixture, a conformance
test identifier, reachable evidence, and two uncorrected defects.

**BLOCKED, not PASS.** DQ-006 supplies one of DQ-002's seven rules. The other six —
node domain, raw-byte boundaries above the leaf, tree shape, odd-node promotion,
empty tree, and fixture-level cross-language equality — are not established by
CANONICAL-001 and cannot be. A single-leaf vector contains no node and no tree.

**No closure patch is prepared.** The instruction conditions it on *every* normative
closure condition being proven. Six are not.

### Requested Custodian actions, in dependency order

1. Rule on A-2 (leaf input domain) — everything else is shaped by it.
2. Approve one ADR; supersede the other (A-9).
3. Write the tree-shape, odd-node and empty-tree rules into an APS document, or
   publish the "approved Aura Merkle profile" `APS-001` §7.2 already cites (A-1, A-3).
4. Correct DEFECT-F1 and bind every published fixture value to an executable test.
5. Assign a CONF identifier for the Merkle hash domain and promote the fixtures under
   APS-500 (C4).
6. Merge the conformance evidence in both implementation repositories, or record why
   it stays unmerged (CFL-004).
7. Decide A-4 (version marker for legacy vs RFC-6962 evidence) and A-8 (tree-size
   binding).
8. Re-examine `closures/DQ-002_FINAL_CLOSURE.md` (A-11). This audit does not alter it.

---

*This audit records findings. It resolves nothing, approves nothing, and confers no
normative status. No production runtime, canonicalization implementation, or
CANONICAL-001 value was modified.*

# DQ-002 — Final Closure

**Document ID:** DQ-002-CLOSURE-001
**Status:** **BLOCKED** — contract settled, closure evidence insufficient
**Classification:** DECISION / CLOSURE RECORD
**Authority:** APS-001 §7.1–§7.2 · APS-200 §8.5 · APS-300 §5.2 · ADR-CK003-DQ002-HASH-DOMAIN
**Original closure record:** 2026-08-19 (recorded CLOSED / PASS)
**Revalidated:** 2026-08-21 — DQ-002 FINAL CLOSURE REVALIDATION after DQ-006
**Ratification:** required — GOVERNANCE.md §2 reserves status transitions to the Chief Architect

> **This record supersedes its own 2026-08-19 content.** The earlier text is
> reproduced in §14 verbatim and retained for history. The 2026-08-19 record
> declared `DQ-002 = CLOSED / PASS` on the explicit stated basis that
> **DQ-006 is PASS**. On 2026-08-20 the authoritative DQ-006 record
> ([`DQ-006_CLOSURE_PACKAGE.md`](DQ-006_CLOSURE_PACKAGE.md) §15) was reconciled
> to **DQ-006 = OPEN**. The premise of the 2026-08-19 DQ-002 closure no longer
> holds, and DQ-006 §14 already routed that inconsistency to the Protocol
> Custodian. This revalidation resolves the resulting status conflict in the
> only direction an agent may resolve it: by reporting it and withdrawing the
> unsupported claim, not by re-asserting it.
>
> **This document does not approve any ADR, promote any fixture to normative,
> or transition any APS status.** Per GOVERNANCE.md §2 an AI assistant may
> propose, implement and test; it may not approve or freeze.

---

## 1. Objective

DQ-002 asks two questions:

1. **What is the hash domain?** Over which bytes, with which algorithm and
   which domain separators, are Aura's record digests and Merkle values
   computed?
2. **Is that domain unambiguous and cross-language reproducible?** Do
   independent implementations produce identical values at every hash
   boundary, and is every prohibited digest input demonstrably rejected?

This revalidation was commissioned to determine whether the canonical
serialization boundary closed under DQ-006 invalidates, contradicts, or
leaves unresolved the DQ-002 hash-domain contract. It is a **dependency
revalidation**, not a redesign. No element of the hash-domain contract was
changed, reinterpreted, or extended.

---

## 2. Normative hash-domain definition

Defined by **APS-001 §7.1–§7.2** (owner of the hash-domain model) over the
canonical byte boundary owned by **APS-200 §8.2**. Reproduced here as a
reference only — APS-001 §7.1 governs, and APS-200 §8.5 states that where its
own table and APS-001 §7.1 could be read differently, APS-001 §7.1 wins.

```text
validated protocol object
        ↓  RFC 8785 JCS                              (APS-200 §8.2 — DQ-006)
UTF-8 canonical_bytes  B
        ↓
digest(B)  = SHA-256(B)                              (APS-001 §7.2)
leaf(B)    = SHA-256(0x00 || B)                      (APS-001 §7.1)
node(l, r) = SHA-256(0x01 || l || r)                 (APS-001 §7.1)
```

| # | Element | Contract | Normative source |
|---|---|---|---|
| A | Hash input domain | `canonical_bytes` only | APS-001 §7 · APS-200 §8.2 |
| B | Canonical serialization boundary | RFC 8785 JCS over the validated semantic object | APS-200 §8.2 |
| C | Hash algorithm | SHA-256 for the current profile | APS-001 §7.2 |
| D | Leaf domain prefix | raw octet `0x00`, prepended to `B` | APS-001 §7.1–§7.2 · APS-200 §8.5 |
| E | Internal-node domain prefix | raw octet `0x01`, prepended to `l ‖ r` — **normative** | APS-001 §7.1–§7.2 · APS-200 §8.5 |
| F | Byte-vs-text boundary | hashing operates on bytes; no textual wrapper may intervene | APS-001 §7 · APS-200 §8.4 |
| G | Encoding | UTF-8, fixed by the canonicalization profile | APS-200 §8.2(3) |
| H | Hex-vs-raw handling | hexadecimal is presentation only; never a digest input, never a node child | APS-001 §7.1 · APS-200 §8.4 · APS-300 §5.1 |
| I | Hash input is bytes, not JSON text | `canonical_bytes`, never a JSON serialization of any other shape | APS-200 §8.2, §8.4 |
| J | Merkle children are raw digests | `l` and `r` are the raw 32 bytes, not hex strings | APS-001 §7.2 · APS-200 §8.5 |
| K | Version binding | hash algorithm changes require a later approved APS with explicit version binding; profile changes are protocol compatibility events | APS-001 §7.2 · APS-200 §8.8 |
| L | Event-type binding | none — canonicalization determines representation only, never event semantics | APS-200 §8.7 |

Tree construction beyond the two domains (recursive split shape, odd-node
policy, empty-tree value) is **not** settled at APS level: APS-001 §7.2 defers
it to "the approved Aura Merkle profile", which does not exist as an approved
artifact. See R-2.

---

## 3. Dependency on DQ-006

DQ-006 owns element **B**; DQ-002 owns **C**, **D**, **E** and consumes **B**.
The revalidation question is whether DQ-006 narrowed, widened, or destabilised
the DQ-002 input.

| Question | Finding |
|---|---|
| Does DQ-006 introduce a new hash dependency? | **NO.** JCS produces bytes; it performs no hashing. |
| Does DQ-006 change the hash algorithm? | **NO.** SHA-256 before and after. |
| Does DQ-006 change the leaf domain? | **NO.** `0x00` before and after. |
| Does DQ-006 change the node domain? | **NO.** `0x01` before and after. |
| Does DQ-006 change what is hashed? | It **fixes** it. Before DQ-006 the DQ-002 contract said "one explicitly defined sequence of canonical bytes" and deferred the profile (`02_hash_domain_adr.md` §3.1). DQ-006 supplies that profile. This resolves a DQ-002 dependency; it does not alter a DQ-002 rule. |
| Does DQ-006 create ambiguity in DQ-002? | **NO** at the byte boundary — verified by execution, §5. |
| Does DQ-002 inherit any DQ-006 defect? | **YES.** Deviation D-1, §8. |

The DQ-006 **decision** is settled and normatively bound (APS-200 §8.2,
APS-300 §5.1, ADR-CK003-DQ006). The DQ-006 **gate** is OPEN. DQ-002 therefore
consumes a settled contract whose conformance evidence is incomplete.

---

## 4. Canonical byte boundary

`canonical_bytes` is the sole hash input. Verified by execution on the real
CANONICAL-001 artifacts:

```text
canonical_bytes_len : 100
canonical_bytes_hex : 7b226576656e745f74797065223a2241554449545f5245434f5244222c2270
                      61796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c
                      5f76657273696f6e223a22312e30222c22736368656d615f76657273696f
                      6e223a22312e30227d
```

| Check | Result |
|---|---|
| RI-PY `canonical_bytes` == RI-RS `canonical_bytes` | PASS (`B-EQ`) |
| Length 100 bytes, as declared by both artifacts | PASS (`B-LEN`) |
| Decodes as UTF-8 | PASS (`B-UTF8`) |
| Both artifacts declare profile `RFC8785` | PASS (`B-PROFILE`) |
| Produced by two distinct engines in two distinct repositories | PASS (`T-DISTINCT`) |

**Canonical bytes boundary: PASS.**

---

## 5. SHA-256 boundary

The digest was recomputed by the revalidation harness from the artifact bytes
alone, not read from any recorded constant.

```text
SHA-256(canonical_bytes) = b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

| Check | Result |
|---|---|
| Recomputed digest == RI-PY `sha256` | PASS (`H-PY`) |
| Recomputed digest == RI-RS `sha256` | PASS (`H-RS`) |
| RI-PY `sha256` == RI-RS `sha256` | PASS (`H-EQ`) |
| Recomputed digest == frozen reference (secondary cross-check) | PASS (`X-SHA`) |

The SHA-256 input is the canonical bytes and nothing else. It is **not** JSON
text, pretty JSON, a hexadecimal representation, a Python `repr`, or a Rust
`Debug` form — each of those is separately falsified in §9.

**SHA input: PASS.**

---

## 6. RFC 6962 leaf boundary

```text
SHA-256(0x00 || canonical_bytes) = ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

| Check | Result |
|---|---|
| Recomputed leaf == RI-PY `leaf_sha256` | PASS (`L-PY`) |
| Recomputed leaf == RI-RS `leaf_sha256` | PASS (`L-RS`) |
| RI-PY leaf == RI-RS leaf | PASS (`L-EQ`) |
| Both artifacts declare `leaf_domain: "0x00"` | PASS (`L-DOMAIN`) |
| Leaf preimage is exactly one octet longer than `canonical_bytes` | PASS (`L-PREIMAGE`) |
| Recomputed leaf == frozen reference (secondary cross-check) | PASS (`X-LEAF`) |

`L-PREIMAGE` is the structural proof that the separator is a single raw octet
rather than a text token: any ASCII spelling of the domain would lengthen the
preimage by 2 or 4 bytes. §9 falsifies those spellings by value as well.

**Leaf input: PASS.** The DQ-002 leaf domain is `SHA-256(0x00 || canonical_bytes)`.
This matches the contract already recorded; nothing was changed.

The **interior-node** domain is exercised separately, on raw 32-byte children,
in §9 (`NC-N1…NC-N4`) and in the CROSS-LANGUAGE-002 vector set (§7).

---

## 7. Cross-language evidence

All evidence below was **re-executed during this revalidation**, not cited from
a previous run.

### 7.1 Canonicalization / digest / leaf — CANONICAL-001

| Item | Value |
|---|---|
| RI-PY | `Aura-IDToken/aura-poc-a-core-v3.3` @ `49d0e4f6` (exec) / `3e8e0e32` (evidence), `rfc8785` 0.1.4 |
| RI-RS | `Aura-IDToken/aura-guard-v1.3` @ `4e9e2284` (exec) / `420653e2` (evidence), `serde_json_canonicalizer` 0.3.2 |
| RI-PY artifact | `ri-py.json`, SHA-256 `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c` — re-verified |
| RI-RS artifact | `ri-rs.json`, SHA-256 `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` — re-verified |
| `test_jcs_behavior.py` | **13 passed** |
| `test_canonical_001.py` | **1 passed** |
| `test_cross_language_canonical_001.py` | **13 passed** |
| `negative_controls_canonical_001.py` | **PASS**, exit 0, committed corpus unmodified |

Both artifact digests and the input digest reproduce exactly the values
recorded in [`DQ-006_CLOSURE_PACKAGE.md`](DQ-006_CLOSURE_PACKAGE.md) §5–§6.
The evidence is therefore traceable to actual RI-PY and RI-RS executions and
not to a manually constructed expected-value file.

### 7.2 Merkle domain and tree — CROSS-LANGUAGE-002

| Item | Result |
|---|---|
| RI-PY `conformance/merkle/` @ `badd0b19` | **158 passed** |
| RI-RS `tests/hash_domains.rs` @ `35082d7b` | **17 passed** |
| RI-RS `tests/byte_representations.rs` @ `35082d7b` | **18 passed** |
| RI-RS `tests/ck003_dq002_ri_rs_conformance.rs` @ `35082d7b` | **1 passed** |
| RI-RS `tests/golden.rs` @ `35082d7b` | **10 passed** |
| RI-RS `conformance/canonical/canonical_001.rs` @ `35082d7b` | **5 passed** |
| `tools/rfc6962_oracle.sh selftest` (coreutils, third producer) | **PASS**, exit 0 |
| `tools/compare_vectors.py` RI-PY vs RI-RS vector sets | **EQUAL + CONFORMANT**, 0 structural diffs, 0 fixture/NC failures, exit 0 |

### 7.3 Verdict

| Boundary | Result |
|---|---|
| RI-PY execution | **PASS** |
| RI-RS execution | **PASS** |
| Canonical bytes equality | **PASS** |
| SHA-256 equality | **PASS** |
| Leaf equality | **PASS** |
| Node domain equality (CROSS-LANGUAGE-002 vector set) | **PASS** |
| Independent digest verification (coreutils oracle + in-harness recomputation) | **PASS** |

---

## 8. Negative-control evidence

Executed by `ck003/dq-002-hash-domain/tools/dq002_hash_domain_revalidation.py`
(Python standard library only — it imports no canonicalizer, so the harness
itself cannot become a second serializer). **41 checks, 0 failed, exit 0.**
Machine-readable output: `ck003/dq-002-hash-domain/evidence/DQ002-REVALIDATION-RESULT.json`.

The normative values are `digest = b6c3660c…a139a4e6` and `leaf = ce6b3673…6648c039`.

| ID | Control | Produced value | Result |
|---|---|---|---|
| `NC-B1` | SHA-256(pretty JSON text) | `90d53785…7f71b6a` | differs — PASS |
| `NC-B2` | SHA-256(default `json.dumps` text) | `dfcd927f…4632cb01` | differs — PASS |
| `NC-B3` | SHA-256(`input.json` file bytes) | `649bb748…3d039261` | differs — PASS |
| `NC-B4` | SHA-256(JSON string escaping the canonical bytes) | `f92d4c92…d6229d1b` | differs — PASS |
| `NC-B5` | SHA-256(hex **text** of the canonical bytes) | `07ddadb3…842b78aa` | differs — PASS |
| `NC-B6` | SHA-256(Python `repr`) | `bbc242f9…c0a99097` | differs — PASS |
| `NC-D1` | SHA-256(`0x01` ‖ bytes) — wrong domain octet | `491a8dcc…119a10b1` | differs — PASS |
| `NC-D2` | SHA-256(bytes) — no domain octet | `b6c3660c…a139a4e6` | differs — PASS |
| `NC-E1` | SHA-256(ASCII `"0x00"` ‖ bytes) | `c85ca186…a601aed1` | differs — PASS |
| `NC-E2` | SHA-256(ASCII `"00"` ‖ bytes) | `c838f1b8…d6ed7939` | differs — PASS |
| `NC-E3` | SHA-256(hex text of the whole leaf preimage) | `015cf0e2…e9a5c6d9` | differs — PASS |
| `NC-N1` | node as SHA-256(`0x01` ‖ hex(l) ‖ hex(r)) | `f70d1a73…b3f52551` | differs — PASS |
| `NC-N2` | node as SHA-256(hex(l) ‖ hex(r)) — the RI-PY legacy domain | `3c6f1dd2…04310720` | differs — PASS |
| `NC-N3` | node computed under the leaf domain `0x00` | `b9912389…84506e78` | differs — PASS |
| `NC-N4` | `node()` given a hexadecimal-text child | rejected — PASS |
| `NC-C1` | canonicalization variant: sorted + `indent=2` | differs — PASS |
| `NC-C2` | canonicalization variant: insertion order, compact | differs — PASS |
| `NC-C3` | canonicalization variant: `ensure_ascii=True` | **identical on this fixture** — recorded, see D-1 |

`NC-D1` independently reproduces `491a8dccdaf280c90d6ce9984ecd8b067c26c994aff7144b0a7606e3119a10b1`,
the wrong-domain control value recorded in
[`DQ-006_CLOSURE_PACKAGE.md`](DQ-006_CLOSURE_PACKAGE.md) §4, confirming that
the leaf domain is genuinely `0x00`.

The ten CROSS-LANGUAGE-002 controls NC-1…NC-10 (missing prefixes, hexadecimal
node children, last-node duplication at N ∈ {3,5,6,7}, altered leaf/sibling/root,
malformed proofs, wrong leaf index) re-executed clean inside the 158-test RI-PY
run and the RI-RS targets in §7.2.

**No production file was mutated.** The DQ-006 negative-control runner copies
the corpus to a temporary directory before mutating it and re-verified the
committed corpus as unmodified; the DQ-002 harness performs no mutation at all.

### D-1 — inherited deviation · **SUBSTANTIVE**

Check `D1-INHERITED` asserts, by execution, that

```python
json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
```

reproduces the CANONICAL-001 canonical bytes exactly. A conforming RFC 8785
engine and a non-conforming sorted-JSON serializer are therefore
indistinguishable on this vector, and so are the digest and the leaf derived
from it.

**Consequence for DQ-002:** the leaf-domain evidence in §6 proves that RI-PY
and RI-RS *agree* on a leaf over bytes both call canonical. It does not prove
those bytes are RFC 8785 output. DQ-002 element **B** is therefore evidenced
only as strongly as DQ-006 criterion 13, which is NOT MET. This is exactly the
inheritance flagged in [`DQ-006_CLOSURE_PACKAGE.md`](DQ-006_CLOSURE_PACKAGE.md) §14.
It is **not** a defect in the DQ-002 domains: `0x00`, `0x01`, SHA-256 and the
raw-byte rule are all independently exercised by §7.2 and §8 on non-degenerate
inputs.

---

## 9. Production integrity

| Repository | Check | Result |
|---|---|---|
| `aura-specification` | no production/normative specification file modified by this revalidation | **CLEAN** |
| RI-PY `aura-poc-a-core-v3.3` | `core/`, `audit/` — not modified; working tree clean at `64bf959b` | **CLEAN** |
| RI-RS `aura-guard-v1.3` | `src/`, `Cargo.toml`, `Cargo.lock` — not modified; working tree clean after `cargo test` at `35082d7b` | **CLEAN** |

This revalidation added only specification-side evidence: a harness, its
result file, transported artifacts, and this record. It changed no
implementation in any repository.

Production hash behaviour, unchanged and confirmed by inspection:

- **RI-RS `src/merkle.rs`** implements the DQ-002 contract natively —
  `leaf_hash` prepends `0x00`, `node_hash` prepends `0x01` over two 32-byte
  digests, `merkle_root` uses the RFC 6962 recursive split, unpaired nodes are
  promoted. It imports no canonicalizer.
- **RI-PY `audit/merkle.py`** does **not**. `sha256(data: str)` hashes UTF-8
  text and returns hex; interior nodes hash `left_hex + right_hex` as text; odd
  nodes are duplicated. This is the legacy contract, deliberately untouched:
  `ADR-CK003-DQ002-HASH-DOMAIN` §"Compatibility and migration rule" forbids
  recomputing historical evidence under the new domain. RI-PY's conformant
  RFC 6962 implementation lives in the conformance-only module
  `conformance/merkle/rfc6962.py`.

---

## 10. Dependency impact

| Question | Answer |
|---|---|
| Does DQ-006 change DQ-002 semantics? | **NO** |
| Does DQ-006 introduce a new hash dependency? | **NO** — JCS defines serialization; SHA-256 remains the hash; RFC 6962 remains the Merkle domain |
| Hash algorithm changed? | **NO** |
| Leaf domain changed? | **NO** |
| Node domain changed? | **NO** |
| Do the JCS engines become production hash dependencies? | **NO at the runtime boundary**, with one manifest-level deviation — see C-2 |

Neither JCS engine is referenced from any production source file. RI-PY
`core/` and `audit/` import no canonicalizer; RI-RS `src/` contains no match
for `canonicalizer`, `rfc8785` or `jcs`. Production hashing in both
implementations is unchanged by DQ-006 and by this revalidation.

---

## 11. Reported conflicts — not resolved by this record

Per `CLAUDE.md`, a detected conflict with higher authority is reported, not
silently reconciled.

### C-1 — DQ-002 status is recorded four different ways · **SUBSTANTIVE**

| Artifact | Recorded status |
|---|---|
| `closures/DQ-002_FINAL_CLOSURE.md` (2026-08-19, superseded by this record) | `CLOSED / PASS` |
| `ck003/dq-002-hash-domain/HASH_DOMAIN_EVIDENCE.md` | `OPEN` |
| `ck003/dq-002-hash-domain/CROSS-LANGUAGE-002-EVIDENCE.md` §12 | `CONDITIONAL PASS`; "DQ-002 remains OPEN" |
| `ck003/dq-002-hash-domain/02_hash_domain_adr.md` §9 | `DECISION RECORDED / IMPLEMENTATION OPEN / CONFORMANCE NOT YET PROVEN` |
| `ck003/gates/GATE_A_APS001_CLOSURE_MATRIX.md` | `DECIDED / IMPLEMENTATION PENDING` |
| `aura-guard-v1.3` `ck003/dq-002-hash-domain/07_DQ-002_verdict.md` | `CONDITIONALLY CLOSED / CI-BLOCKED` |

Only the 2026-08-19 record claimed closure, and only on the DQ-006 premise
that no longer holds. This record withdraws that claim and makes itself the
single authoritative DQ-002 status record. Every other artifact above is
subordinate and consistent with **BLOCKED**.

### C-2 — the RI-RS conformance boundary of record is not the one on `main` · **SUBSTANTIVE**

[`DQ-006_CLOSURE_PACKAGE.md`](DQ-006_CLOSURE_PACKAGE.md) §6 states that the
RI-RS engine "lives in a separate `aura-guard-conformance` package with its own
workspace root and lockfile, so the production `aura-guard` dependency graph
gains no canonicalizer", and §9 records `git diff -- src/ Cargo.toml Cargo.lock`
as empty. That is true of evidence commit `420653e2`.

It is **not** true of `aura-guard-v1.3` `main` at `35082d7b`, which merged
PR #58 — the competing implementation that D-3 / CFL-003 flagged for disposal.
On `main`:

- `Cargo.toml` carries `serde_json_canonicalizer = "=0.3.2"` under
  `[dev-dependencies]` of the **production crate** `aura-guard`;
- `Cargo.lock` lists `serde_json_canonicalizer` among the `aura-guard`
  package's dependencies;
- the conformance test target `canonical_001` is declared in the production
  manifest and reports 5 tests, where the evidence of record reports 4.

Assessment: this is a **dev-dependency**, so the engine is not linked into the
`aura-guard` library or binaries, is not shipped in a release artifact, and is
not propagated to downstream consumers. The Phase-7 requirement — "JCS MUST NOT
become a production **hash** dependency" — is therefore not violated at the
runtime boundary. But the isolation boundary described by the closure record of
record is not the boundary present on `main`, and a reviewer verifying §6 or §9
against `main` will find them false. This is DQ-006 residual **R3**, now
materialised in the default branch. Routed to the Protocol Custodian.

### C-3 — task premise vs. corpus · **PROCEDURAL, reported**

The execution order commissioning this revalidation states `DQ-006: PASS` and
`CROSS-LANGUAGE-001: PASS`. CROSS-LANGUAGE-001 is PASS and was re-executed
(§7.1). DQ-006 is **OPEN** per its authoritative record. Prompt-level
instructions rank below the specification and closure corpus in the CLAUDE.md
authority ladder, so the corpus governs and the conflict is reported here
rather than reconciled. This revalidation proceeded on the substance of the
order — the semantic revalidation was performed in full — while declining to
inherit the false premise into a verdict.

---

## 12. Residual risks

Only unresolved risks are listed. Each is executable; none requires
re-deciding the contract in §2.

| ID | Residual | Blocks | Owner |
|---|---|---|---|
| **R-1** | `ADR-CK003-DQ002-HASH-DOMAIN` is `PROPOSED — awaiting Chief Architect approval`, and the duplicate `02_hash_domain_adr.md` is `PROPOSED — pending review and merge`. Two ADRs exist for one decision. Conformance is measured against a proposal. Its own conformance gate (APS-200 §8 update, APS-300 reconciliation, APS-500 fixture promotion, cross-language tests, migration semantics) is partly satisfied by DQ-006 but not recorded as such. | closure criteria 1, 13 | Chief Architect |
| **R-2** | APS-001 §7.2 requires odd-node behaviour to "follow the approved Aura Merkle profile". No artifact of that name exists in an approved state. The leaf and node **domains** are unambiguous; the **tree construction** is not normatively anchored. RFC 6962 shape is asserted in the ADRs, the oracle and both implementations, but only as proposals. | criterion 2 | Protocol Custodian |
| **R-3** | `DEFECT-DQ002-F1` OPEN. `03_cross_language_fixture.json` self-designates `NORMATIVE_TEST_VECTOR` and records `node.digest_hex = e2bd2dce…3904b7ac`, which is not the SHA-256 of the preimage the same file declares (`bc6b943b…a3a72641`). Re-asserted by this revalidation (`F1-NODE-DEFECT`). Correction is a Custodian action. That fixture also does not exercise the DQ-006 boundary at all: its "canonical serialization" is a pipe-delimited string (`F1-CANON-DISJOINT`). | criterion 6 | Protocol Custodian |
| **R-4** | `DEFECT-DQ002-F2` OPEN. DQ-002 does not state that an inclusion proof authenticates `(leaf, root)` and **not** `tree_size`. Measured acceptance sets are pinned in both implementations, so this is a specification-completeness gap, not a divergence. | criterion 6 | Protocol Custodian |
| **R-5** | `DEFECT-DQ002-F3` OPEN. The RI-PY suite cannot be collected without `--ignore=core/test_ari_observability.py` (`NameError: name 'unittest' is not defined`), so no repository-wide green run exists for RI-PY. | criterion 5 | RI-PY |
| **R-6** | **No CI execution of any DQ-002 gate has ever succeeded.** The RI-RS workflow `.github/workflows/ck003-dq002.yml` has four recorded runs (`32067890217`, `32067907383`, `32069885289`, `32069892166`), all `conclusion: failure`, each completing in under five seconds — consistent with the billing block recorded in the RI-RS verdict document. `aura-specification` has no workflows at all, and the RI-PY DQ-002 conformance suite has no gate. The RI-RS verdict's own closure criterion — one successful Actions run — is unmet. All DQ-002 evidence, including this revalidation, is local. | criterion 7 | Protocol Custodian |
| **R-7** | Evidence reachability. RI-PY's entire `conformance/` tree — both the DQ-006 canonical gate and the 158-test DQ-002 merkle suite — exists only on unmerged branches (`claude/cross-language-canonical-001-n4v2c5`, `claude/aura-cross-language-002-6t2kdo`); `main` has no `conformance/` directory. RI-RS `main` carries the DQ-002 hash-domain tests but not the CROSS-LANGUAGE-002 vector target. Transporting the CANONICAL-001 artifacts into this repository (§13) makes the DQ-002 chain resolvable from the specification corpus; it does not repair reachability in the reference repositories. This is DQ-006 residual **R2**. | criterion 5 | RI-PY + RI-RS |
| **R-8** | D-1 inheritance (§8). DQ-002's canonical-byte input is evidenced only as strongly as DQ-006 criterion 13, which is NOT MET. Closes when DQ-006 **R1** lands a JCS-discriminating cross-language vector. | criterion 3 | RI-PY + RI-RS |
| **R-9** | C-2 (§11). The RI-RS conformance boundary on `main` contradicts the isolation claim in the DQ-006 closure record. | criterion 9 | Protocol Custodian |
| **R-10** | Ratification. GOVERNANCE.md §2 reserves status transitions to the Chief Architect. No DQ-002 verdict — including this one — is ratified. | criterion 10 | Chief Architect |

Explicitly **not** DQ-002 residuals: CFL-001 (cross-corpus governance
precedence) and CFL-005 (empty Event-Type Registry). Both are reported in
[`DQ-006_CLOSURE_PACKAGE.md`](DQ-006_CLOSURE_PACKAGE.md) §14; neither is
DQ-002's to resolve, and APS-200 §8.7 keeps event semantics out of this gate.

---

## 13. Evidence

Produced or re-verified by this revalidation, in `aura-specification`:

| Path | SHA-256 | Role |
|---|---|---|
| `ck003/dq-002-hash-domain/tools/dq002_hash_domain_revalidation.py` | `dee6af8b19ec95986f82e5d55a5247beccb1b7b2827cfd5b10f6cd3e8c5ef9b0` | revalidation harness, stdlib only |
| `ck003/dq-002-hash-domain/evidence/DQ002-REVALIDATION-RESULT.json` | `ee6ee69278abb308edc7bc5b611559fcc260d09f037569cd024c31b5def76eaa` | 41 checks, 0 failed |
| `ck003/dq-002-hash-domain/evidence/canonical-001/input.json` | `649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261` | transported |
| `ck003/dq-002-hash-domain/evidence/canonical-001/manifest.json` | `28890ee7bcc14d37cfd433d496d48f1296fabffa3ad4f2e42c4c0a772ae5aa10` | transported |
| `ck003/dq-002-hash-domain/evidence/canonical-001/ri-py.json` | `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c` | transported RI-PY execution artifact |
| `ck003/dq-002-hash-domain/evidence/canonical-001/ri-rs.json` | `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` | transported RI-RS execution artifact |
| `ck003/dq-002-hash-domain/evidence/canonical-001/PROVENANCE.md` | — | transport record |
| `ck003/dq-002-hash-domain/tools/rfc6962_oracle.sh` | `13b0b69d68aa0ca8df1d1555f863a720392bb8e352b3957fe5bd29a4d035017b` | third-producer oracle, selftest re-run PASS |
| `ck003/dq-002-hash-domain/tools/compare_vectors.py` | — | vector comparator, re-run EQUAL + CONFORMANT |
| `ck003/dq-002-hash-domain/evidence/RI-PY-VECTORS.json` | `82e47587b046bfdb121a5170b967a44403dd98ccd6cbbfedd2321db010e8a67b` | re-compared |
| `ck003/dq-002-hash-domain/evidence/RI-RS-VECTORS.json` | `82e47587b046bfdb121a5170b967a44403dd98ccd6cbbfedd2321db010e8a67b` | re-compared |

Referenced commits, all fetched and verified during this revalidation:

| Repository | Commit | Role |
|---|---|---|
| `Aura-IDToken/aura-specification` | `ff30e166be2511b6d5684a33efb8c7da9d63a574` | revalidation baseline (`main` == branch point) |
| `Aura-IDToken/aura-poc-a-core-v3.3` | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` | RI-PY CANONICAL-001 execution |
| `Aura-IDToken/aura-poc-a-core-v3.3` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` | RI-PY CANONICAL-001 evidence |
| `Aura-IDToken/aura-poc-a-core-v3.3` | `badd0b19e424ec57e484531e039f653e0cf6f596` | RI-PY CROSS-LANGUAGE-002 / DQ-002 merkle suite |
| `Aura-IDToken/aura-poc-a-core-v3.3` | `64bf959b1d23fbd5433723476c611ab66d423953` | RI-PY working head, production integrity check |
| `Aura-IDToken/aura-guard-v1.3` | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` | RI-RS CANONICAL-001 execution |
| `Aura-IDToken/aura-guard-v1.3` | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` | RI-RS CANONICAL-001 evidence |
| `Aura-IDToken/aura-guard-v1.3` | `35082d7b4880dad780fb55a1a5f3ac0ef4322674` | RI-RS working head, DQ-002 test execution, C-2 |

Execution environment: Ubuntu 24.04.4 LTS · Linux 6.18.5-fc-v20 x86_64 ·
CPython 3.11.15 · pytest 9.1.1 · rustc 1.94.1 · cargo 1.94.1 · GNU coreutils
`sha256sum` 9.4 · 2026-08-21T04:25:45Z. Toolchain versions match those recorded
for the original executions. **CI: NOT EXECUTED** — see R-6.

---

## 14. Superseded record — 2026-08-19, verbatim

Retained for history. Its verdict does not govern; §15 does.

> **Status:** CLOSED — PASS · **Closure date:** 2026-08-19 ·
> **Dependent gate:** DQ-006 · **Decision branch:** `ck003/dq-006-closure-package`
>
> **1. Decision.** DQ-002 is formally closed as **PASS**. The closure follows
> successful DQ-006 cross-language conformance. The canonical digest boundary is
> now backed by independently executed RI-PY and RI-RS evidence and is no longer
> supported solely by a shared expected digest.
>
> **2. Frozen Hash-Domain Contract.** For CANONICAL-001 and the corresponding
> protocol boundary: (1) canonical input is serialized using the frozen RFC 8785
> JCS profile; (2) the record digest domain is `SHA-256(canonical_bytes)`;
> (3) the RFC 6962 leaf domain is `SHA-256(0x00 || canonical_bytes)`; (4) `0x00`
> is a raw binary octet, not the ASCII string `"0x00"`; (5) no JSON
> reserialization, hexadecimal representation, whitespace transformation, or
> textual wrapper is introduced between canonicalization and hashing; (6) RFC 6962
> interior-node domain separation remains `0x01` and is not substituted for the
> leaf domain.
>
> **3. CANONICAL-001 Evidence.** canonical bytes `7b226576…22312e30227d`;
> `SHA-256(canonical_bytes)` = `b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6`;
> `SHA-256(0x00 || canonical_bytes)` = `ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039`.
> Both RI-PY and RI-RS independently generated these values and the equality
> runner verified byte, SHA-256 and leaf equality.
>
> **4. Conformance Evidence.** RI-PY: `rfc8785==0.1.4`; CANONICAL-001 PASS;
> JCS-B01…B06 PASS; cross-language artifact PASS. RI-RS:
> `serde_json_canonicalizer==0.3.2`; CANONICAL-001 PASS; cross-language artifact
> PASS. Cross-language: canonical bytes equality, SHA equality, leaf equality,
> independent recomputation, negative controls — all PASS.
>
> **5. Production Boundary.** The conformance work did not modify production
> hash/Merkle core behavior. JCS engines are conformance-only dependencies.
> Therefore DQ-002 closes the **protocol contract**, not a mandate to introduce
> JCS into production runtime.
>
> **6. Relationship to DQ-006.** DQ-006 established that RI-PY and RI-RS
> independently execute the same canonicalization/hash/leaf contract. DQ-002 now
> records the resulting hash-domain semantics as frozen protocol semantics.
> Dependency chain: DQ-006 PASS → independent cross-language evidence → canonical
> bytes equality → SHA-256 equality → RFC-6962 leaf equality → DQ-002 FINAL
> CLOSURE.
>
> **7. Remaining Scope.** DQ-002 closure does not by itself close APS-001, DQ-003,
> DQ-004, INV-001…INV-015, the full canonical fixture corpus, the
> specification/core/guard CI gates, or the release gate.
>
> **8. Final Verdict.** **DQ-002 = CLOSED / PASS.** The hash-domain contract is
> frozen and backed by executable cross-language evidence.

What this revalidation changes in that text: §1's dependency premise
("successful DQ-006 cross-language conformance") is narrowed — CROSS-LANGUAGE-001
is PASS, DQ-006 as a gate is OPEN. §4's "JCS-B01…B06" is label drift for
`test_jcs_behavior.py` (13 passed), already reported in the DQ-006 consistency
scan row 33. §5's "JCS engines are conformance-only dependencies" needs the
C-2 qualification. §2, §3 and §6's hash-domain content are **confirmed
unchanged** by §2–§8 of this record.

---

## 15. Closure criteria and final verdict

| # | Criterion | State |
|---|---|---|
| 1 | Normative hash-domain model exists and is unambiguous at the digest, leaf and node boundaries | **MET** — APS-001 §7.1–§7.2, APS-200 §8.5, APS-300 §5.2; §2 above |
| 2 | Merkle tree construction (shape, odd-node policy, empty tree) normatively anchored | **NOT MET** — R-2 |
| 3 | Canonical serialization boundary established and feeding the hash | **MET as a contract** (APS-200 §8.2), **evidence PARTIAL** — R-8 |
| 4 | Canonical bytes are the SHA-256 input; prohibited inputs falsified | **MET** — §5, §8 |
| 5 | RI-PY evidence exists and re-executes | **MET as execution** (158 + 13 + 1 + 13 passed), **reachability NOT MET** — R-5, R-7 |
| 6 | RI-RS evidence exists and re-executes | **MET as execution** (17 + 18 + 1 + 10 + 5 passed), **defects open** — R-3, R-4 |
| 7 | Cross-language byte / digest / leaf / node equality, independently recomputed | **MET locally** — §7; **no CI evidence** — R-6 |
| 8 | Negative controls, including wrong domain, ASCII `"0x00"`, JSON text and hexadecimal children | **MET** — §8, 41/41 |
| 9 | Production runtime unchanged; JCS conformance-only | **MET at the runtime boundary**, **manifest deviation** — C-2, R-9 |
| 10 | No unresolved DQ-002 defect remains | **NOT MET** — F1, F2, F3 all OPEN (R-3, R-4, R-5) |
| 11 | All normative references traceable to an existing artifact | **NOT MET** — R-2; ADR still PROPOSED — R-1 |
| 12 | Single authoritative DQ-002 status record, no competing claim | **MET by this record** — C-1 resolved by supersession |
| 13 | Chief Architect ratification | **NOT MET** — R-10 |

Criteria 4, 8 and 12 are fully met. Criteria 1 and 3 are met as contract.
Criteria 5, 6, 7 and 9 are met as local execution with named deficiencies.
Criteria 2, 10, 11 and 13 are not met.

```text
Hash-domain contract              : SETTLED   (criteria 1, 4, 8)
Cross-language conformance        : EXECUTED  (criteria 5-7, local only)
Specification completeness        : PARTIAL   (criteria 2, 11 not met)
Defect closure                    : OPEN      (criterion 10 not met)
Procedural closure                : OPEN      (criteria 7, 13 not met)

DQ-002 = BLOCKED
```

**BLOCKED, not FAIL.** No contradiction was found in the hash-domain contract
itself. Every normative source that states the domain — APS-001 §7.1–§7.2,
APS-200 §8.5, APS-300 §5.2, both DQ-002 ADRs, the RI-RS verdict, and both
implementations' conformant code paths — states the same thing: SHA-256 over
`canonical_bytes`, leaf `0x00`, node `0x01`, raw digest children. Forty-one
executed checks and five re-executed test suites agree. DQ-006 neither
invalidates nor contradicts that contract, and introduces no new hash
dependency.

**BLOCKED, not PASS.** The evidence is insufficient for closure on five
independent grounds, any one of which is disqualifying: the governing ADR is
unapproved (R-1); the tree-construction rule has no approved referent (R-2);
three DQ-002 defects are open, one of them a wrong digest inside a file
self-designated `NORMATIVE_TEST_VECTOR` (R-3, R-4, R-5); no CI gate has ever
executed successfully (R-6); and the depended-upon DQ-006 gate is itself OPEN,
so the canonical-byte input is evidenced only up to D-1 (R-8).

DQ-002 is **not** closed by the fact that CROSS-LANGUAGE-001 passed. It is not
closed by the fact that DQ-006's decision is settled. It closes when R-1
through R-10 are discharged.

**No production runtime change is implied or authorized by this record.**

**This record does not close** DQ-003, DQ-004, APS-001, INV-001…INV-015, the
canonical fixture corpus, the CI gates, or the release gate. It makes no claim
about any of them.

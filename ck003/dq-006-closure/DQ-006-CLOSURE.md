# DQ-006 Closure Record

Document ID: DQ-006-CLOSURE  
Version: 1.0  
Status: CLOSED — PASS  
Classification: Decision Closure Record (CK-003 evidence scope, non-normative for APS text)  
Authority: APS-001 → APS-200 → APS-300 → APS-400 → CK-003 GATE B  
Last Review: 2026-08-20

> This record closes the **DQ-006 evidence and decision gate**. It does not amend any APS
> document, does not change production runtime behaviour, and does not close any other gate.
> This file is the **single canonical DQ-006 closure record**. Earlier copies elsewhere in the
> repository are superseded pointers — see §15.

---

## 1. Decision identity

| Field | Value |
|---|---|
| Decision | DQ-006 — canonical serialization / cross-language conformance |
| Workstream | CK-003 Remediation, GATE B (Conformance) |
| Fixture | `CANONICAL-001` |
| Gate | `CROSS-LANGUAGE-001` artifact bridge |
| Decision status | **CLOSED — PASS** |
| Canonical package | `ck003/dq-006-closure/` |
| Production runtime change authorized by this record | **NONE** |

---

## 2. Closure statement

DQ-006 asked whether the two Aura reference implementations — **RI-PY**
(`Aura-IDToken/aura-poc-a-core-v3.3`) and **RI-RS** (`Aura-IDToken/aura-guard-v1.3`) — execute
the *same* canonical serialization, digest and Merkle-leaf contract for the frozen
`CANONICAL-001` vector.

DQ-006 is closed **PASS** because both implementations independently produced byte-identical
canonical bytes, an identical `SHA-256(canonical_bytes)` digest, and an identical
`SHA-256(0x00 || canonical_bytes)` RFC 6962 leaf; because the equality gate recomputed both
artifacts rather than comparing metadata; and because controlled mutations were rejected by that
gate.

The closure is bounded by §11 (scope of proof) and §13 (residual dependencies).

---

## 3. Evidence classes

DQ-006 closure is asserted across five distinct classes. They are kept separate because they
carry different strengths of claim.

### A. Specification contract

| Element | Value | Specification state |
|---|---|---|
| Canonical serialization profile | RFC 8785 JSON Canonicalization Scheme (JCS) | **Proposed**, not yet bound in APS text — `ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` is `PROPOSED`; `APS-200 §8` still carries a TODO for the RI-PY/RI-RS interoperability format |
| Record digest | `SHA-256(canonical_bytes)` | Frozen for the conformance boundary |
| Merkle leaf | `SHA-256(0x00 \|\| canonical_bytes)` | Frozen for the conformance boundary |

DQ-006 closes the **conformance question**. The APS-200 §8 normative amendment is a separate
architectural action (§13.1). This record MUST NOT be read as that amendment.

### B. Implementation evidence

Both implementations executed the fixture from their own adapter, against a clean worktree, with
a pinned engine, and emitted a self-describing artifact. Neither adapter read the other
implementation's artifact, and neither read the frozen expected values in order to produce its
own output. See `DQ-006_EVIDENCE_INDEX.md` (`DQ006-E01` … `DQ006-E04`).

### C. Cross-language equality

The equality runner compares two independently produced artifacts and independently recomputes
each artifact's digest and leaf before accepting any equality claim. The frozen expected values
are applied only as a **secondary** cross-check, never as a source for producing or backfilling
an artifact. See `DQ-006_CROSS_LANGUAGE_MATRIX.md` and `DQ006-E05`.

### D. Negative-control evidence

The gate was shown to be discriminating against three controlled mutations, including the
leaf-domain mutation whose significance is preserved in §8. See `DQ006-E06`.

### E. Production-integrity evidence

Neither implementation's production tree was modified by the conformance work. See §9 and
`DQ006-E07`.

---

## 4. Canonical serialization profile

The canonical serialization profile under test is **RFC 8785 JSON Canonicalization Scheme
(JCS)**, producing UTF-8 canonical bytes.

| Implementation | Conformance engine | Pinned in |
|---|---|---|
| RI-PY | `rfc8785==0.1.4` | `conformance/requirements-conformance.txt` |
| RI-RS | `serde_json_canonicalizer==0.3.2` | `conformance/Cargo.toml` + `conformance/Cargo.lock` (separate workspace) |

Both engines are **CONFORMANCE-ONLY**.

They are **NOT** normative production runtime dependencies, and this record does not authorize
introducing either engine into a production dependency graph. The RI-RS conformance package is a
separate crate with its own workspace root and its own lockfile precisely so the production
`aura-guard` dependency graph does not gain a JCS engine.

---

## 5. Hash-domain closure

For a canonical byte sequence `B`:

```text
digest(B) = SHA-256(B)
leaf(B)   = SHA-256(0x00 || B)
```

`0x00` is **one raw octet** prepended to the canonical bytes.

It is **NOT**:

- the ASCII text `0x00`;
- a hexadecimal text representation;
- a JSON value;
- a serialized string;
- any textual wrapper.

The verified leaf preimage is exactly `[0x00] || canonical_bytes` — a 101-octet preimage for the
100-octet `CANONICAL-001` canonical byte sequence.

RFC 6962 interior-node domain separation (`0x01`) is out of scope for this record and is not
substituted for the leaf domain.

**No production Merkle or hashing implementation is modified or reinterpreted by this record.**

---

## 6. CANONICAL-001 — NORMATIVE FIXTURE VALUES

Fixture input (`conformance/corpus/canonical-001/input.json`,
SHA-256 `649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261`):

```json
{
  "event_type": "AUDIT_RECORD",
  "protocol_version": "1.0",
  "schema_version": "1.0",
  "payload": {
    "value": 42
  }
}
```

The following are **NORMATIVE FIXTURE VALUES** for `CANONICAL-001`, not illustrative examples.

| Property | Value |
|---|---|
| `canonical_bytes_len` | `100` |
| `canonical_bytes_hex` | `7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d` |
| `sha256` | `b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6` |
| `leaf_sha256` (RFC 6962, domain `0x00`) | `ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039` |

Canonical bytes decoded as UTF-8:

```text
{"event_type":"AUDIT_RECORD","payload":{"value":42},"protocol_version":"1.0","schema_version":"1.0"}
```

JCS member ordering is determined by the canonicalization profile, not by the input document's
member order. The input above and the canonical output above are therefore consistent, not
contradictory.

---

## 7. Cross-language equality

| Property | RI-PY | RI-RS | Equality |
|---|---|---|---|
| canonical bytes | `7b2265…30227d` (100 octets) | `7b2265…30227d` (100 octets) | **PASS** |
| SHA-256 | `b6c3660c…a139a4e6` | `b6c3660c…a139a4e6` | **PASS** |
| RFC 6962 leaf | `ce6b3673…6648c039` | `ce6b3673…6648c039` | **PASS** |

Full-length values, artifact digests, adapter digests and execution environments are recorded in
`DQ-006_CROSS_LANGUAGE_MATRIX.md`.

### Implementation provenance

| Field | RI-PY | RI-RS |
|---|---|---|
| Repository | `Aura-IDToken/aura-poc-a-core-v3.3` | `Aura-IDToken/aura-guard-v1.3` |
| Execution commit | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` |
| Artifact publication commit | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |
| Engine / version | `rfc8785` `0.1.4` | `serde_json_canonicalizer` `0.3.2` |
| Toolchain | CPython 3.11.15, Linux x86_64 | rustc 1.94.1 (e408947bf 2026-03-25), Linux x86_64 |
| Worktree clean at execution | `true` | `true` |

Artifacts record the **execution** commit, not their own publication commit, so no artifact is
self-referential.

---

## 8. Negative controls

| # | Mutation | Expected | Observed |
|---|---|---|---|
| 1 | canonical bytes mutated | gate FAILS | gate FAILED as required |
| 2 | recorded SHA-256 mutated | gate FAILS | gate FAILED as required |
| 3 | leaf domain `0x00` → `0x01` | gate FAILS | gate FAILED as required, via independent leaf recomputation |

All mutations were applied to temporary copies. The committed corpus was verified unchanged
afterwards.

### 8.1 Preserved architectural finding — symmetric mutation

Negative control 3 is **not** reducible to leaf-to-leaf equality between the two artifacts.

A mutation applied symmetrically — the same wrong leaf domain on both sides — preserves
`RI-PY leaf == RI-RS leaf`. Cross-language equality alone would therefore accept a consistently
wrong leaf domain.

**Therefore independent recomputation of the leaf from each artifact's own canonical bytes is a
required property of the evidence gate, not an optimisation.** Equality between implementations
is necessary but not sufficient; the gate MUST recompute. This property MUST be preserved in any
future refactor of the equality runner and MUST NOT be simplified away.

---

## 9. Production isolation

| Implementation | Path | State |
|---|---|---|
| RI-PY | `core/` | unchanged |
| RI-PY | `audit/` | unchanged |
| RI-RS | `src/` | unchanged |
| RI-RS | production `Cargo.toml` | unchanged |
| RI-RS | production `Cargo.lock` | unchanged |

Both execution commits record that the corresponding `git diff` over those paths is empty, and
the JCS engines are confined to conformance-scoped dependency files.

**DQ-006 evidence therefore does not constitute a production-runtime change.** No production
hashing, Merkle implementation, event-type semantics or protocol semantics were altered.

---

## 10. Closure criteria

| # | Criterion | Evidence | Result |
|---|---|---|---|
| 1 | JCS profile identified | §4, `DQ006-E01`, `DQ006-E02` | **PASS** |
| 2 | RI-PY JCS engine identified | `rfc8785==0.1.4`, `DQ006-E01` | **PASS** |
| 3 | RI-RS JCS engine identified | `serde_json_canonicalizer==0.3.2`, `DQ006-E02` | **PASS** |
| 4 | CANONICAL-001 executed independently in RI-PY | `DQ006-E03` | **PASS** |
| 5 | CANONICAL-001 executed independently in RI-RS | `DQ006-E04` | **PASS** |
| 6 | canonical bytes equality | `DQ006-E05` | **PASS** |
| 7 | independent RI-PY SHA verification | `DQ006-E05` | **PASS** |
| 8 | independent RI-RS SHA verification | `DQ006-E05` | **PASS** |
| 9 | SHA equality | `DQ006-E05` | **PASS** |
| 10 | independent RI-PY leaf verification | `DQ006-E05` | **PASS** |
| 11 | independent RI-RS leaf verification | `DQ006-E05` | **PASS** |
| 12 | leaf equality | `DQ006-E05` | **PASS** |
| 13 | frozen expected cross-check (secondary) | `DQ006-E05` | **PASS** |
| 14 | negative controls | `DQ006-E06`, §8 | **PASS** |
| 15 | production integrity | `DQ006-E07`, §9 | **PASS** |
| 16 | evidence provenance | §7, `DQ006-E01` … `DQ006-E07` | **PASS** |
| 17 | cross-language equality | §7, `DQ-006_CROSS_LANGUAGE_MATRIX.md` | **PASS** |

All seventeen required criteria are represented by actual executed evidence recorded against
immutable commit identifiers.

---

## 11. Scope of proof

### 11.1 What this closure proves

- `CANONICAL-001` — the frozen normative vector — canonicalizes, digests and leaf-hashes
  identically in RI-PY and RI-RS.
- The equality boundary is **canonical bytes**, not semantic JSON equivalence.
- The digest domain consumes canonical bytes directly.
- The RFC 6962 leaf domain is the raw octet `0x00` prefixed to canonical bytes.
- Cross-language equality was established from independently produced artifacts.
- The evidence gate rejects byte, digest and leaf-domain mutations.
- The conformance work is isolated from production runtime.

### 11.2 What this closure does NOT prove

- It does **not** prove that all possible JSON inputs are cross-language equivalent.
  `CANONICAL-001` proves the frozen normative vector only.
- It does **not** prove any future `schema_version` or `protocol_version` behaviour.
- It does **not** state or imply that production runtime uses JCS.
- It does **not** establish that the fixture corpus is complete. It is one vector.
- It does **not** close INV-001 … INV-015, and `compliance/TRACEABILITY_MATRIX.md` correctly
  still records INV-003 as `NOT VERIFIED` for both RI-PY and RI-RS, because CONF-003 is scoped
  to *all* protocol objects.
- It does **not** close DQ-002, DQ-001, DQ-003, DQ-004 or APS-001.

### 11.3 Discriminating engine evidence

`CANONICAL-001` alone characterises one vector. The RI-PY JCS behaviour suite
(`conformance/canonical/test_jcs_behavior.py`, recorded in CK-003 registers as `JCS-B01…B06`)
characterises the **engine**: key ordering by UTF-16 code unit, absence of insignificant
whitespace, array order preservation, ES6 number serialization, rejection of non-finite numbers,
minimal string escaping, raw UTF-8 for non-ASCII, and input-order independence. Its purpose is
that a silent engine substitution or upgrade cannot pass unnoticed underneath the CANONICAL-001
execution evidence.

Traceability note: the executable suite is not individually tagged `JCS-B01` … `JCS-B06` in
RI-PY; those identifiers are CK-003 register labels applied to the suite as a whole. Tagging
individual behaviours is a traceability improvement, not a DQ-006 closure dependency — DQ-006
rests on `CANONICAL-001` / `CROSS-LANGUAGE-001`. There is no equivalent behaviour suite recorded
for RI-RS.

---

## 12. Traceability

```text
APS-001 §1 (8) "serializing normative objects into canonical bytes"
        ↓
canonical serialization contract  (APS-200 §8 — amendment pending, see §13.1)
        ↓
INV-003 Canonical Serialization  →  CONF-003
        ↓
DQ-006  (this record)
        ↓
CANONICAL-001  (frozen normative fixture, §6)
        ↓
RI-PY execution ─────┐
                     ├── CROSS-LANGUAGE-001  (independent artifact bridge)
RI-RS execution ─────┘
        ↓
byte / digest / leaf equality + independent recomputation + negative controls
        ↓
DQ-006 = CLOSED
```

`APS-001` is referenced for traceability only. **APS-001 is not modified, not amended and not
closed by this record.**

---

## 13. Residual dependencies

These are recorded so the closure is not read more widely than the evidence supports. None of
them is a DQ-006 closure criterion under §10; each is a separate gate.

### 13.1 APS-200 §8 amendment (specification-side)

`APS-200 §8` still reads *"TODO: Define the canonical serialization format for interoperability
between RI-PY and RI-RS"*, and `ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` remains `PROPOSED`.
`ck003/dq-006-canonical-serialization/CANONICAL_SERIALIZATION_CLOSURE_STATE.md` accordingly
records the *specification* gate as OPEN.

DQ-006 closes the **conformance/evidence** gate; binding RFC 8785 JCS into normative APS text
requires Chief Architect approval and an APS-200 amendment, which this record does not perform
and does not pre-authorize.

### 13.2 Evidence durability

The `CANONICAL-001` conformance tree is not present on the default branch of either reference
implementation repository. The evidence is referenced here by immutable commit SHA, which
remains valid, but merging the conformance tree to the default branches — and running it under
CI — is a separate GATE C action.

### 13.3 RI-RS behaviour suite

No JCS engine-behaviour suite equivalent to RI-PY's `test_jcs_behavior.py` is recorded for RI-RS
(§11.3).

---

## 14. Explicit non-closures

| Item | Status after this record |
|---|---|
| DQ-002 | **DQ-002 remains subject to its own closure gate.** Not closed, not inferred, and not evaluated by this record. See §14.1. |
| DQ-001 / DQ-003 / DQ-004 | NOT closed by this record |
| APS-001 | NOT closed, NOT amended, NOT rewritten by this record |
| APS-200 §8 | NOT amended by this record (§13.1) |
| INV-001 … INV-015 | NOT closed by this record |
| Fixture corpus (APS-500) | NOT complete |
| CI / release gates (GATE C, GATE D) | NOT established by this record |
| Production runtime | NOT modified |
| Production JCS dependency | NOT authorized |

### 14.1 DQ-002 boundary

DQ-002 closure MUST NOT be inferred from DQ-006. A pre-existing document
`closures/DQ-002_FINAL_CLOSURE.md` asserts a DQ-002 closure and cites DQ-006 as its dependent
gate. That document predates this record and is **outside DQ-006 authority**: this record
neither ratifies, extends nor withdraws it. Reconciling DQ-002's status is a Protocol Custodian /
DQ-002 gate action.

---

## 15. Canonical location and superseded copies

This file is the canonical DQ-006 closure record. The following files previously carried
overlapping DQ-006 closure text and are now `SUPERSEDED` pointers to this package. No evidence
value was removed; all values they carried are reproduced here or in the package's index and
matrix.

- `ck003/DQ-006_CLOSURE.md`
- `ck003/DQ-006_EVIDENCE_INDEX.md`
- `closures/DQ-006_CLOSURE_PACKAGE.md`
- `evidence/DQ-006_CLOSURE_PACKAGE.md`

---

## 16. Accepted deviations

1. **Branch naming.** The RI execution branches were session-designated `claude/*` branches
   rather than `ck003/*`. This is an execution-environment deviation with no protocol-semantic
   impact. The same applies to the branch carrying this package (see `README.md`).
2. **Artifact commit identity.** Artifacts record the clean source/execution commit that
   produced them rather than their own publication commit, avoiding self-reference.
3. **Corpus transport.** The RI-RS artifact was generated in `aura-guard-v1.3` and transported
   byte-identically into the RI-PY corpus used by the equality runner
   (file SHA-256 `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` in both
   repositories). It was not reconstructed or re-keyed.

---

## 17. Verdict

```text
CROSS-LANGUAGE-001 = PASS
DQ-006             = CLOSED / PASS
```

**No production implementation change is implied or authorized by this closure.**

Next gates, each subject to its own evidence: APS-200 §8 amendment (§13.1), DQ-002 (§14.1),
INV-001 … INV-015 conformance mapping, fixture corpus completion, CI and release gates.

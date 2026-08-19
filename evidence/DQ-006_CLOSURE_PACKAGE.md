# DQ-006 Closure Package

Document ID: DQ-006-CLOSURE-001  
Status: **CLOSED — PASS**  
Authority: DQ-006 / APS-200 / APS-300 / APS-400  
Closure date: 2026-08-19

---

## 1. Decision

**DQ-006: CLOSED.**

Classification: `DECISION` / `EVIDENCE` (CK-003 status vocabulary).

DQ-006 — canonical serialization / canonical digest cross-language conformance — is closed as **PASS** on the basis of the independently executed CROSS-LANGUAGE-001 ARTIFACT BRIDGE.

The evidence-backed claim recorded by this closure is exactly:

> CANONICAL-001 has been independently executed by RI-PY and RI-RS and the resulting canonical bytes, SHA-256 digest and RFC-6962 leaf are byte/digest identical.

No broader claim is made. See §10.

This closure does **not** modify production hashing, Merkle behaviour, event-type semantics, or runtime canonicalization.

---

## 2. Scope

DQ-006 concerns the canonical serialization / canonical digest cross-language conformance boundary.

The verified chain is:

```text
RFC 8785 JCS
        ↓
canonical bytes
        ↓
SHA-256(canonical_bytes)
        ↓
RFC-6962 leaf:
SHA-256(0x00 || canonical_bytes)
        ↓
RI-PY == RI-RS
```

### DQ-006 closes

- the definition of the canonicalization → digest → leaf chain used by CANONICAL-001;
- independent executability of that chain in RI-PY and RI-RS;
- byte equality of the canonical bytes produced by the two implementations for CANONICAL-001;
- digest equality of `SHA-256(canonical_bytes)` for CANONICAL-001;
- leaf equality of `SHA-256(0x00 || canonical_bytes)` for CANONICAL-001;
- demonstrated sensitivity of the equality gate to tampering (negative controls);
- production-runtime non-modification by the conformance work;
- traceability of the above to concrete repository commits and artifacts.

### DQ-006 does not close

The evidence demonstrates equality **for CANONICAL-001**. It does **not** by itself prove that all possible JSON values are cross-language equivalent. The broader fixture corpus remains a subsequent conformance activity. See §10.

---

## 3. Normative Contract

| Property | Value |
|---|---|
| Canonical serialization | RFC 8785 JCS |
| RI-PY conformance engine | `rfc8785==0.1.4` |
| RI-RS conformance engine | `serde_json_canonicalizer==0.3.2` |
| Digest | `SHA-256(canonical_bytes)` |
| RFC-6962 leaf domain octet | `0x00` (one raw octet, not an ASCII representation) |
| Leaf | `SHA-256(0x00 \|\| canonical_bytes)` |
| Production runtime changes | None |

### Conformance-only engine scope

Both JCS engines are **CONFORMANCE-ONLY**. Neither `rfc8785` nor `serde_json_canonicalizer` is asserted here as a production runtime dependency, and this closure does not authorize introducing one. The existing specification does not state otherwise.

The production Core (`aura-poc-a-core-v3.3`) was **not** changed by this work. See §5 and DQ6-C12.

### Normative dependency notice

This closure records an **evidence/decision** gate. It is not an amendment of the normative APS documents. At the closure date:

- `ADR-CK003-DQ006 — Canonical Serialization Profile` has status **PROPOSED**;
- `aps/APS-200_CANONICAL_DATA_MODEL.md` §8 still carries its TODO for the RI-PY / RI-RS interoperability serialization format;
- `ck003/dq-006-canonical-serialization/APS-300-RECONCILIATION.md` remains **OPEN — proposed binding prepared**.

DQ-006 closure supplies the executable evidence those items were waiting on for the CANONICAL-001 boundary. It does **not** itself perform the APS-200 §8 amendment, the APS-300 reconciliation, or the ADR approval. Those remain separate normative acts requiring Chief Architect / Protocol Custodian authority, and are recorded here so the gap is not lost.

---

## 4. CANONICAL-001

### Fixture input

Stored byte-identically in both reference implementations as
`conformance/corpus/canonical-001/input.json`,
SHA-256 `649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261`:

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

### Canonical bytes

Length: **100 bytes**.

```text
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
```

### SHA-256

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

### RFC-6962 leaf

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

These are the exact values recorded by the RI-PY and RI-RS execution artifacts. They are unchanged by this closure package.

---

## 5. CROSS-LANGUAGE-001

### RI-PY execution

| Field | Value |
|---|---|
| Repository | `Aura-IDToken/aura-poc-a-core-v3.3` |
| Execution/source commit | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` (clean worktree) |
| Evidence/artifact commit | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| Engine | `rfc8785` 0.1.4 |
| Environment | CPython 3.11.15, Linux x86_64 |
| Adapter | `conformance/canonical/jcs.py` |
| Artifact | `conformance/corpus/canonical-001/ri-py.json` |
| Result | **PASS** |

### RI-RS execution

| Field | Value |
|---|---|
| Repository | `Aura-IDToken/aura-guard-v1.3` |
| Execution/source commit | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` (clean worktree) |
| Evidence/artifact commit | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |
| Engine | `serde_json_canonicalizer` 0.3.2 |
| Environment | rustc 1.94.1, Linux x86_64 |
| Adapter | `conformance/canonical/jcs.rs` |
| Artifact | `conformance/corpus/canonical-001/ri-rs.json` |
| Result | **PASS** |

The RI-RS artifact was transported byte-identically into the RI-PY corpus for the bridge comparison. It was not reconstructed or re-keyed. Both copies hash to
`a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c`.

### Equality results

| Property | Result |
|---|---|
| Canonical byte equality (RI-PY vs RI-RS) | PASS |
| RI-PY SHA-256 independent recomputation | PASS |
| RI-RS SHA-256 independent recomputation | PASS |
| SHA-256 equality (RI-PY vs RI-RS) | PASS |
| RI-PY RFC-6962 leaf independent recomputation | PASS |
| RI-RS RFC-6962 leaf independent recomputation | PASS |
| RFC-6962 leaf equality (RI-PY vs RI-RS) | PASS |
| Frozen expected-value cross-check (secondary) | PASS |

The equality runner loads only the two artifacts. It imports no canonicalizer, does not re-serialize the fixture input, and recomputes each digest and leaf from the decoded bytes before accepting metadata equality.

**CROSS-LANGUAGE-001: PASS.**

### Negative controls

| Control | Mutation | Gate result | Checks that fired |
|---|---|---|---|
| baseline | none | pass | — |
| A | RI-RS `canonical_bytes_hex` final byte flipped | detected | byte equality, RI-RS SHA recomputation, RI-RS leaf recomputation |
| B | RI-PY `sha256` first byte corrupted | detected | RI-PY SHA recomputation, SHA equality |
| C | both leaves recomputed under domain `0x01` | detected | RI-PY and RI-RS leaf recomputation |

Control C is the significant one: because both leaves were mutated consistently, leaf-to-leaf equality still passed. Only the independent leaf recomputations detected it. This is why leaf equality alone is not accepted as the leaf-domain check.

Each control operated on a temporary copy of the corpus. The committed corpus was verified unchanged afterwards.

**Negative controls: PASS.**

### Production integrity

| Repository | Check | Result |
|---|---|---|
| RI-PY | `git diff -- core/ audit/` | empty |
| RI-RS | `git diff -- src/ Cargo.toml Cargo.lock` | empty |

The RI-RS JCS engine is confined to a separate `conformance/` package with its own workspace root and lockfile, so the production `aura-guard` dependency graph does not gain a canonicalizer.

**Production integrity: PASS.**

---

## 6. Closure Matrix

Allowed statuses: `PASS` · `FAIL` · `BLOCKED` · `NOT APPLICABLE`.

| ID | Requirement | Evidence | Status | Notes |
|---|---|---|---|---|
| DQ6-C01 | JCS canonicalization profile is defined | `ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md`; frozen CANONICAL-001 contract in `conformance/corpus/canonical-001/EXECUTION-EVIDENCE.md` (RI-PY `3e8e0e3`) | PASS | Defined and frozen **for the conformance boundary under test**: RFC 8785 JCS, pinned engines, fixed digest and leaf domains. The ADR remains `PROPOSED` and APS-200 §8 retains its TODO; the normative amendment is outside DQ-006 scope. See §3 *Normative dependency notice*. |
| DQ6-C02 | RI-PY has an approved conformance JCS engine | `conformance/requirements-conformance.txt` pinning `rfc8785==0.1.4` (RI-PY `49d0e4f` / `3e8e0e3`) | PASS | Pin is marked conformance-only and explicitly excluded from the production runtime environment. |
| DQ6-C03 | RI-RS has an approved conformance JCS engine | `conformance/Cargo.toml` / `conformance/Cargo.lock` pinning `serde_json_canonicalizer==0.3.2`, lockfile checksum `fe52319a927259afbfa5180c5157cd8167edfd3e8c254f9558c7fef44c5649f2` (RI-RS `4e9e228` / `420653e`) | PASS | Resolved under `cargo test --locked` in a separate conformance workspace. |
| DQ6-C04 | CANONICAL-001 is executable independently in RI-PY | `python -m pytest -q conformance/canonical/test_canonical_001.py` → 1 passed; `python -m conformance.canonical.emit_ri_py_artifact` → `ri-py.json` | PASS | Emitter imports only the RI-PY adapter; reads no RI-RS file and no frozen reference constant. |
| DQ6-C05 | CANONICAL-001 is executable independently in RI-RS | `cargo test --locked --test canonical_001` → 4 passed; 0 failed → `ri-rs.json` | PASS | Rust test and adapter reference no RI-PY value, path or artifact. |
| DQ6-C06 | RI-PY canonical bytes independently equal RI-RS canonical bytes | Equality runner CHECK 1 over `ri-py.json` and `ri-rs.json` | PASS | Identical 100-byte sequence. |
| DQ6-C07 | SHA-256 is independently verified over the produced bytes | Equality runner CHECK 2 (RI-PY) and CHECK 3 (RI-RS) | PASS | Digest recomputed from the decoded canonical bytes of each artifact, not read from metadata. |
| DQ6-C08 | RI-PY SHA-256 equals RI-RS SHA-256 | Equality runner CHECK 4 | PASS | `b6c3660c…139a4e6`. |
| DQ6-C09 | RFC-6962 leaf construction is independently verified | Equality runner CHECK 5 (RI-PY) and CHECK 6 (RI-RS) | PASS | Leaf recomputed as `SHA-256(0x00 \|\| bytes)` from each artifact's decoded bytes. |
| DQ6-C10 | RI-PY leaf equals RI-RS leaf | Equality runner CHECK 7 | PASS | `ce6b3673…648c039`. |
| DQ6-C11 | Negative controls demonstrate that the equality gate detects tampering/mismatch | `conformance/canonical/negative_controls_canonical_001.py` → exit 0; controls A, B, C all detected | PASS | Control C (consistent wrong leaf domain `0x01`) was caught only by independent leaf recomputation. Corpus verified unchanged after the controls. |
| DQ6-C12 | No production runtime was modified by the conformance implementation | RI-PY `git diff -- core/ audit/` empty; RI-RS `git diff -- src/ Cargo.toml Cargo.lock` empty | PASS | JCS engines confined to conformance boundaries in both repositories. |
| DQ6-C13 | Evidence is traceable to concrete repository commits/artifacts | §7 Evidence References; §8 Provenance | PASS | Every artifact is addressed by repository, commit and path. Source execution commits and artifact publication commits are recorded separately. |

**All mandatory criteria DQ6-C01…DQ6-C13: PASS.**

---

## 7. Evidence References

The evidence artifacts are **not** files of `aura-specification`. They reside in the reference-implementation repositories and are referenced here by repository, commit and path.

### RI-PY — `Aura-IDToken/aura-poc-a-core-v3.3` @ `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e`

| Path | Role |
|---|---|
| `conformance/corpus/canonical-001/input.json` | fixture input (SHA-256 `649bb748…3039261`) |
| `conformance/corpus/canonical-001/ri-py.json` | RI-PY execution artifact (file SHA-256 `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c`) |
| `conformance/corpus/canonical-001/ri-rs.json` | RI-RS execution artifact, transported byte-identically (file SHA-256 `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c`) |
| `conformance/corpus/canonical-001/manifest.json` | machine-readable evidence index |
| `conformance/corpus/canonical-001/EXECUTION-EVIDENCE.md` | commands, outputs, digests, independence argument, negative-control results, production-integrity checks |
| `conformance/canonical/test_cross_language_canonical_001.py` | equality runner |
| `conformance/canonical/negative_controls_canonical_001.py` | negative controls |
| `conformance/canonical/jcs.py` | RI-PY JCS adapter |
| `conformance/canonical/emit_ri_py_artifact.py` | RI-PY artifact emitter |
| `conformance/requirements-conformance.txt` | conformance-only engine pin |
| `conformance/CANONICAL-001.md` | fixture definition |

### RI-RS — `Aura-IDToken/aura-guard-v1.3` @ `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0`

| Path | Role |
|---|---|
| `conformance/corpus/canonical-001/input.json` | fixture input, byte-identical to RI-PY |
| `conformance/corpus/canonical-001/ri-rs.json` | RI-RS execution artifact (origin copy) |
| `conformance/canonical/jcs.rs` | RI-RS JCS adapter |
| `conformance/canonical/test/canonical_001.rs` | RI-RS execution test |
| `conformance/Cargo.toml`, `conformance/Cargo.lock` | separate conformance workspace and engine pin |

### `aura-specification` (this repository)

| Path | Role |
|---|---|
| `evidence/DQ-006_CLOSURE_PACKAGE.md` | this closure package (decision of record) |
| `ck003/dq-006-closure/DQ-006-CLOSURE.md` | CK-003 workstream closure record |
| `ck003/dq-006-closure/CROSS-LANGUAGE-001-EVIDENCE.md` | CK-003 evidence ledger |
| `ck003/dq-006-closure/canonical-001-evidence-manifest.json` | CK-003 machine-readable evidence index |
| `ck003/dq-006-canonical-serialization/` | canonical serialization decision inputs (ADR, APS-200 §8 proposal, APS-300 reconciliation, independent oracle) |

---

## 8. Provenance

Source execution commits and artifact publication commits are recorded separately and are **not** collapsed.

| Implementation | Repository | Source execution commit | Artifact publication commit |
|---|---|---|---|
| RI-PY | `Aura-IDToken/aura-poc-a-core-v3.3` | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| RI-RS | `Aura-IDToken/aura-guard-v1.3` | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |

Each artifact's `commit` field identifies the clean source commit that produced it. The publication commit is its parent-child successor, which avoids self-referential commit identity. This mapping is the one carried by the evidence package itself and is preserved verbatim.

Both execution commits were recorded against clean worktrees (`worktree_clean: true` in both artifacts).

---

## 9. Deviations

The following deviations were declared by the executor. None of them is a protocol failure; the evidence does not demonstrate a protocol violation in any of these cases.

| # | Deviation | Classification | Impact |
|---|---|---|---|
| D1 | The execution and closure branches were session-designated branches rather than the requested `ck003/...` naming (RI execution ran on `claude/cross-language-canonical-001-n4v2c5`; this closure is authored on `claude/dq-006-closure-i8u8u6`). | Execution-environment deviation | None on protocol semantics or evidence. Session branch policy overrode the preferred name. |
| D2 | The RI-PY adapter was rebound from the pre-existing `jcs` package to `rfc8785==0.1.4` at source commit `49d0e4f`. | Conformance engine binding | Intentional. Fixes the RI-PY engine identity to the pinned, versioned contract recorded in §3. |
| D3 | The RI-RS conformance implementation was introduced in a separate `conformance/` package with its own workspace root and lockfile. | Isolation measure | Keeps the canonicalizer out of the production `aura-guard` dependency graph. Supports DQ6-C12. |
| D4 | The RI-RS corpus artifact was transported byte-identically from `aura-guard-v1.3` into the RI-PY corpus used by the equality runner. | Evidence transport | Not reconstructed and not re-keyed. Both copies hash to `a6ebad01…9af329c`, so transport integrity is itself evidenced. |
| D5 | RI-RS artifact metadata is tied to the source execution commit `4e9e228`, not to its publication commit. | Provenance convention | Intentional; avoids self-referential commit identity. Recorded in §8. |
| D6 | Environment dependencies were installed to perform execution. | Execution prerequisite | Conformance-scoped only. Production runtime dependency graphs unchanged (DQ6-C12). |

---

## 10. Non-Closure Statements

This closure is deliberately narrow. Explicitly:

- This closure does **not** close **DQ-002**.
- This closure does **not** close **APS-001**.
- This closure does **not** close **INV-001…INV-015**.
- This closure does **not** establish exhaustive cross-language equality for all future fixtures. The evidence covers CANONICAL-001 only; it does not by itself prove that all possible JSON values are cross-language equivalent.

Additionally, and consistent with §3:

- This closure does **not** amend `APS-200 §8`, which retains its TODO for the interoperability serialization format.
- This closure does **not** approve `ADR-CK003-DQ006`, which remains `PROPOSED`.
- This closure does **not** complete the APS-300 evidence-hash reconciliation, which remains `OPEN`.
- This closure does **not** authorize a production JCS dependency in Core or Guard.
- This closure does **not** establish the APS-500 canonical fixture corpus, CI/release gates, or `aura-specification v1.0` release approval.

Each of these remains a subsequent gate with its own evidence and decision record.

---

## 11. Consequence

After DQ-006 closure, the protocol may proceed to the next conformance and specification closure gates.

The following are now evidence-backed inputs for that subsequent work:

- RFC 8785 JCS is the canonicalization profile under test;
- canonical bytes, not semantic JSON equivalence, are the equality boundary;
- SHA-256 is applied directly to the canonical byte sequence;
- the RFC-6962 leaf domain octet `0x00` is applied to raw canonical bytes, never to hexadecimal digest text;
- cross-language equality must be evaluated on independently produced artifacts, with independent recomputation rather than metadata comparison;
- conformance evidence is separable from production runtime change.

### Traceability

```text
APS-200 canonical data model (§8 amendment OPEN)
        ↓
ADR-CK003-DQ006 (PROPOSED)
        ↓
INV-003 Canonical Serialization → CONF-003
        ↓
CANONICAL-001
        ↓
RI-PY actual execution ─────┐
                            ├── CROSS-LANGUAGE-001 = PASS
RI-RS actual execution ─────┘
        ↓
canonical byte / SHA-256 / RFC-6962 leaf equality
        ↓
DQ-006 = CLOSED
```

APS-300 requires evidence to be immutable, deterministic, traceable and independently verifiable, and its traceability model connects APS requirement → invariant → evaluation → evidence → conformance test → release. This closure package preserves that chain.

Version semantics remain governed by CONF-008 / INV-009. DQ-006 does not reopen DQ-003.

### Next gate

**DQ-002 final closure**, subject to its own evidence and decision record. It is not executed or affected by this package.

---

## 12. Final Verdict

**DQ-006: CLOSED — PASS**

**CROSS-LANGUAGE-001: PASS**

No production runtime change was required for, or made by, this closure.

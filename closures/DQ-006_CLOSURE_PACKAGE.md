# DQ-006 — Closure Package

**Document ID:** DQ-006-CLOSURE-001
**Status:** **CLOSED**
**Classification:** DECISION / CLOSURE RECORD
**Authority:** APS-200 §8 · APS-300 §5 · ADR-CK003-DQ006 · CONF-003
**Original closure record:** 2026-08-19 (recorded CLOSED / PASS)
**Reconciled:** 2026-08-20 — DQ-006 CLOSURE RECONCILIATION
**Closed:** 2026-08-20 — DQ-006 CLOSURE INTEGRATION, on Chief Architect Execution Order
**Ratification:** recorded — the closure integration order is the Chief Architect act required by GOVERNANCE.md §2

> **This is the single authoritative DQ-006 closure record.** Four earlier records
> ([`evidence/DQ-006_CLOSURE_PACKAGE.md`](../evidence/DQ-006_CLOSURE_PACKAGE.md),
> [`ck003/DQ-006_CLOSURE.md`](../ck003/DQ-006_CLOSURE.md),
> [`ck003/dq-006-closure/DQ-006-CLOSURE.md`](../ck003/dq-006-closure/DQ-006-CLOSURE.md),
> [`ck003/dq-006-closure/README.md`](../ck003/dq-006-closure/README.md))
> are SUPERSEDED by this one and retained for history. Where any of them differs from this
> record, this record governs.

---

## 1. Decision

DQ-006 asked which canonical serialization profile the Aura Protocol uses, and whether independent implementations execute it identically.

The **decision** is settled: the profile is **RFC 8785 JSON Canonicalization Scheme (JCS)** over UTF-8 bytes, with `SHA-256(canonical_bytes)` as the record digest and the RFC 6962 leaf domain `SHA-256(0x00 || canonical_bytes)`. As of this reconciliation the decision is normatively bound in **APS-200 §8** and **APS-300 §5**, and recorded in **ADR-CK003-DQ006**.

The **gate** is closed. Two independent conformance implementations execute the profile and produce identical canonical bytes, identical SHA-256 and identical RFC 6962 leaf for two fixtures — CANONICAL-001 and the JCS-discriminating CANONICAL-002. Because CANONICAL-002 separates RFC 8785 from an ordinary sorted-JSON serializer, the result establishes *profile conformance*, not merely implementation *agreement*. See §7, §8 and §12.

Both JCS engines are **conformance-only**. Nothing in this package states or implies that production Core or Guard uses JCS.

---

## 2. Scope

**In scope.** The canonical byte boundary for JSON-represented protocol objects; the digest domain over those bytes; the RFC 6962 leaf domain over those bytes; cross-implementation byte identity; the evidence required to demonstrate all of it.

**Out of scope.** Production runtime behaviour in either reference implementation; the Merkle tree construction semantics beyond the leaf/node domains (DQ-002); event-type vocabulary (DQ-004); version compatibility policy (DQ-003); INV-001…INV-015 closure; CI and release gates.

No production implementation change is authorized or implied by this package.

---

## 3. Normative contract

Defined once, in APS-200 §8. Reproduced here as a reference only — APS-200 §8 governs.

```text
validated protocol object
        ↓  RFC 8785 JCS
UTF-8 canonical_bytes
        ↓
digest(B)  = SHA-256(B)
leaf(B)    = SHA-256(0x00 || B)
node(l, r) = SHA-256(0x01 || l || r)
```

`0x00` and `0x01` are raw octets. `l` and `r` are raw digest bytes. Prohibited digest inputs — pretty-printed JSON, implementation-specific serializations, escaped or hex/Base64 encodings of the canonical bytes, hex digest strings in place of digest bytes — are enumerated in APS-200 §8.4.

The evidence-hash domain is bound to the same canonical bytes by APS-300 §5.1.

| Layer | Content |
|---|---|
| **Normative protocol contract** | RFC 8785 JCS · UTF-8 canonical bytes · SHA-256 digest · RFC 6962 `0x00` leaf / `0x01` node |
| **Conformance implementation detail** | `rfc8785` 0.1.4 (RI-PY) · `serde_json_canonicalizer` 0.3.2 (RI-RS) · adapters · runners · corpus layout |

The engines are not the protocol. See ADR-CK003-DQ006 §2.

---

## 4. Evidence

Fixture **CANONICAL-001**.

Input (`input.json`, SHA-256 `649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261`), stored byte-identically in both reference repositories:

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

Observed values, identical on both sides:

```text
canonical_bytes_len : 100
canonical_bytes_hex : 7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
sha256              : b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
leaf_sha256 (0x00)  : ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

Independently recomputed from the frozen hex alone, without reference to any recorded constant, at reconciliation and again at closure integration on 2026-08-20: all three values reproduce. The wrong-domain control `SHA-256(0x01 || canonical_bytes)` yields `491a8dccdaf280c90d6ce9984ecd8b067c26c994aff7144b0a7606e3119a10b1`, confirming the leaf domain is genuinely `0x00`.

### 4.1 CANONICAL-002 — the discriminating fixture

Input digest `aee31642d0186c17daabdc910da64183567a3aa655348cc41195e4f2f7956588`
(992 bytes), stored byte-identically in both reference repositories, with
deliberately non-canonical member order so an engine that echoes its input
cannot pass.

**VERIFIED EXECUTION EVIDENCE:**

```text
canonical_bytes_len : 655
sha256              : cdceb08100d88c81adc5a7e4f0462328071711808bc990458c0fa6b2c87d0952
leaf_sha256 (0x00)  : 20fd6065aa4a21233119ad361835e43e64932e7805568947b4715a07c95b9368
```

Sorted-JSON serialization of the same input is 716 bytes — the two provably
differ. Properties exercised: UTF-16 code-unit member ordering (including at
depth), raw UTF-8 output, ECMAScript number form (`1.0`→`1`, `-0.0`→`0`,
`1e-6`→`0.000001`, `1e-7`→`1e-7`), recursive canonicalization, array-order
preservation, and minimal escaping with unescaped solidus.

Both values were independently recomputed from the committed corpus on
2026-08-20 and match both artifacts. Full detail:
[`ck003/dq-006-closure/DQ-006_EVIDENCE.md`](../ck003/dq-006-closure/DQ-006_EVIDENCE.md).

| Implementation | Execution commit | Evidence commit |
|---|---|---|
| RI-PY | `7bcc600f649a35f76cee5752ce597ac2b71b6d62` | `ea39a53a60336b1715abd41166348eea2ad6f52e` |
| RI-RS | `bd4a2fa6b4d11dcfb270b4a4f98b2f359ab32609` | `5685b2a74ca2fabcdbcf36c89733c42ba0141f7e` |

---

## 5. RI-PY evidence

| Field | Value |
|---|---|
| Repository | `Aura-IDToken/aura-poc-a-core-v3.3` |
| Execution commit | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` (clean worktree) |
| Evidence commit | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| Branch | `claude/cross-language-canonical-001-n4v2c5` — **not merged to `main`** |
| Engine | `rfc8785` 0.1.4 |
| Adapter | `conformance/canonical/jcs.py`, SHA-256 `8f6c3b440221113721a82c6ff3ff61dcfbaccbcbe972ce7ae635d00444b8b5a4` (pure delegation to `rfc8785.dumps`) |
| Toolchain | CPython 3.11.15, Linux x86_64 |
| Artifact | `conformance/corpus/canonical-001/ri-py.json`, SHA-256 `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c` |
| Result | **PASS** |

Executed: `test_jcs_behavior.py` → 13 passed; `test_canonical_001.py` → 1 passed; `emit_ri_py_artifact` → artifact.

Artifact digest and adapter digest were re-verified against the source tree during this reconciliation; both match.

---

## 6. RI-RS evidence

| Field | Value |
|---|---|
| Repository | `Aura-IDToken/aura-guard-v1.3` |
| Execution commit | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` (clean worktree) |
| Evidence commit | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |
| Branch | `claude/cross-language-canonical-001-n4v2c5` — **not merged to `main`** |
| Engine | `serde_json_canonicalizer` 0.3.2, resolved from `conformance/Cargo.lock` |
| Adapter | `conformance/canonical/jcs.rs`, SHA-256 `0dae4ef696f06a4d3248ca85284fd7db280ef3c897a96cf898ef076cd4e846f2` (pure delegation to `serde_json_canonicalizer::to_vec`) |
| Toolchain | rustc 1.94.1, Linux x86_64 |
| Artifact | `conformance/corpus/canonical-001/ri-rs.json`, SHA-256 `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` |
| Result | **PASS** |

Executed: `cargo test --locked --test canonical_001` → 4 passed, 0 failed. The engine lives in a separate `aura-guard-conformance` package with its own workspace root and lockfile, so the production `aura-guard` dependency graph gains no canonicalizer.

Artifact digest re-verified during this reconciliation; matches.

---

## 7. Cross-language equality — CROSS-LANGUAGE-001

Runner: `conformance/canonical/test_cross_language_canonical_001.py` (RI-PY repository). It loads only the two artifacts; it imports no canonicalizer and never re-serializes the input.

| Check | Assertion | Result |
|---|---|---|
| C1 | RI-PY bytes == RI-RS bytes | PASS |
| C2 | Gate recomputes `SHA-256(RI-PY bytes)` == RI-PY `sha256` | PASS |
| C3 | Gate recomputes `SHA-256(RI-RS bytes)` == RI-RS `sha256` | PASS |
| C4 | RI-PY `sha256` == RI-RS `sha256` | PASS |
| C5 | Gate recomputes `SHA-256(0x00 \|\| RI-PY bytes)` == RI-PY leaf | PASS |
| C6 | Gate recomputes `SHA-256(0x00 \|\| RI-RS bytes)` == RI-RS leaf | PASS |
| C7 | RI-PY leaf == RI-RS leaf | PASS |
| C8 | Distinct implementations, repositories, engines declared | PASS |

Suite result: 13 passed. Secondary cross-check against the frozen reference values: PASS on both sides.

**CROSS-LANGUAGE-001 = PASS** for byte, digest and leaf equality on CANONICAL-001.

### 7.1 CANONICAL-002 — CROSS-LANGUAGE-CANONICAL-002

Runner: `conformance/canonical/test_cross_language_canonical_002.py`. Same
architecture and the same checks C1–C8, all **PASS**, 17 tests. It adds three
guards the CANONICAL-001 gate does not have:

- both artifacts must declare the same `provenance.input_sha256`, so byte
  equality is only accepted when both engines read the same input;
- the fixture is asserted to be JCS-discriminating against the manifest's
  recorded sorted-JSON serialization;
- the UTF-16 member ordering and the ECMAScript number forms are re-verified
  directly from the produced bytes.

| Property | RI-PY | RI-RS | Equality |
|---|---|---|---|
| Engine | `rfc8785` 0.1.4 | `serde_json_canonicalizer` 0.3.2 | N/A |
| Canonical bytes | 655 B | identical | **PASS** |
| SHA-256 | `cdceb081…c87d0952` | identical | **PASS** |
| RFC-6962 leaf | `20fd6065…c95b9368` | identical | **PASS** |

**CROSS-LANGUAGE-CANONICAL-002 = PASS.**

> The RI repositories name this gate `CROSS-LANGUAGE-002`, an identifier already
> assigned in this specification to the DQ-002 Merkle gate (status OPEN /
> CONDITIONAL PASS). This specification uses `CROSS-LANGUAGE-CANONICAL-002` to
> avoid a false reading that the Merkle gate has passed. Carried as C-3.

---

## 8. Negative controls

Each control copies the committed corpus to a temporary directory, mutates the copy, and runs the real gate against it.

| Control | Mutation | Gate exit | Checks that fired | Result |
|---|---|---|---|---|
| baseline | none | 0 | — | 13 passed |
| N1 | RI-RS `canonical_bytes_hex` final byte flipped | 1 | C1, C3, C6 | rejected |
| N2 | RI-PY `sha256` first byte corrupted | 1 | C2, C4 | rejected |
| N3 | Both leaves recomputed under domain `0x01` | 1 | C5, C6 | rejected |

N3 is the discriminating control: because both leaves were mutated consistently, C7 still passed. Only the independent recomputations in C5 and C6 caught it.

Corpus digests after the controls: unchanged. No mutation remains in either repository.

### 8.1 CANONICAL-002 controls

The same three controls were run against the CANONICAL-002 gate and all three
were rejected. A fourth control was added, and it is the decisive one:

| Control | Mutation | Gate exit | Result |
|---|---|---|---|
| baseline | none | 0 | 17 passed |
| N1 | canonical bytes modified | 1 | rejected |
| N2 | SHA-256 modified | 1 | rejected |
| N3 | wrong leaf domain `0x01`, both sides | 1 | rejected |
| **N4** | one side's bytes replaced by sorted-JSON output of the same input, with digest and leaf recomputed to match | 1 | **rejected** |

N4 substitutes a plausible non-conforming serializer for one implementation. The
substituted artifact is internally consistent, so C2, C3, C5 and C6 still pass;
C1, C4 and C7 catch it.

Run against **CANONICAL-001**, the identical substitution is **not detected** —
that gate reports 13 passed, because sorted JSON reproduces those canonical bytes
exactly. Run against **CANONICAL-002** it fails. That contrast is the executable
demonstration that the corpus now discriminates RFC 8785, and it is what closes
criterion 13.

The incorrect serializer is confined to the control script and to temporary
copies. It is never installed as an adapter and never written to the committed
corpus, which was hashed before and after and is unchanged.

---

## 9. Production integrity

| Repository | Check | Result |
|---|---|---|
| RI-PY | `git diff -- core/ audit/` | empty |
| RI-RS | `git diff -- src/ Cargo.toml Cargo.lock` | empty |

The JCS engines are confined to conformance-only package boundaries in both
repositories. No production hash, Merkle, event-type or protocol-semantics code
was changed by CROSS-LANGUAGE-001 or by the CANONICAL-002 work.

The CANONICAL-002 work added one `[[test]]` target registration to the RI-RS
`Cargo.toml`. It adds no dependency, changes no lockfile, and affects neither the
library nor any binary; `serde_json_canonicalizer` remains under
`[dev-dependencies]`. Recorded here rather than omitted.

---

## 10. Known deviations

### D-1 — CANONICAL-001 is JCS-degenerate · **RESOLVED by CANONICAL-002**

For this object, `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` produces bytes identical to the frozen canonical bytes, and therefore the identical SHA-256 and the identical leaf. Verified by execution during this reconciliation.

A fully conforming RFC 8785 engine and a non-conforming sorted-JSON serializer are indistinguishable on this vector. CROSS-LANGUAGE-001 therefore establishes that RI-PY and RI-RS agree; it does not establish that either implements RFC 8785, which is the decision it is cited for.

Partial mitigation, RI-PY only: `test_jcs_behavior.py` (13 passed) exercises discriminating behaviour — ES6 number form, non-finite rejection, minimal escaping, raw UTF-8 for non-ASCII. RI-RS has no equivalent executed behavioural suite.

Recorded independently at [`ck003/handover-assessment/10_INDEPENDENT_VERIFICATION.md`](../ck003/handover-assessment/10_INDEPENDENT_VERIFICATION.md) §3.2 and [`05_EVIDENCE_GAPS.md`](../ck003/handover-assessment/05_EVIDENCE_GAPS.md) EG-01.

**Resolution — 2026-08-20 (DQ-006-R1).** CANONICAL-002 was added, executed on
both frozen engines, and verified. It is 655 canonical bytes against 716 bytes
of sorted JSON for the same input, so the two provably differ. Its equality gate
adds a fourth negative control that replaces one side's bytes with sorted-JSON
output of the same input: run against CANONICAL-001 that substitution passes
undetected, run against CANONICAL-002 it fails the gate. The corpus now
distinguishes RFC 8785 from a plausible non-conforming serializer, and the
cross-language result evidences conformance rather than only agreement.
Details: [`ck003/dq-006-closure/DQ-006_EVIDENCE.md`](../ck003/dq-006-closure/DQ-006_EVIDENCE.md) §1.2, §2.2, §4.

CANONICAL-001 remains in the corpus unchanged. Its degeneracy is a property of
that vector, not a defect, and is recorded so no future reader over-reads it.

### D-2 — Evidence is not merged to a default branch · **CARRIED as C-1**

All eight cited commits (four per fixture) live on published branches that are
unmerged in their repositories. They were confirmed present on `origin` and
independently re-verified on 2026-08-20, so the evidence is reachable by SHA and
reproducible; what is missing is a merge to `main`. A reviewer cloning either
repository at `main` must fetch the named branch to reach it.

This is repository hygiene, not an evidence defect. It is carried to the release
gate as **C-1** and does not qualify the canonical serialization decision.

### D-3 — RI-RS conformance boundary: decided in practice, branches undisposed · **CARRIED as C-2**

At reconciliation time three incompatible RI-RS implementations of this gate
existed with none merged (CFL-003, [`ck003/handover-assessment/04_CONFLICT_REGISTER.md`](../ck003/handover-assessment/04_CONFLICT_REGISTER.md)).

**Update — 2026-08-20.** `aura-guard-v1.3` `main` now carries a JCS conformance
boundary at `conformance/canonical/` with the engine confined to
`[dev-dependencies]` and `Cargo.lock` untouched. CANONICAL-002 was executed
directly on top of that boundary, so the discriminating evidence rests on the
implementation that is actually on the default branch — a stronger position than
CANONICAL-001, whose RI-RS evidence was produced under a separate-package
layout that is still unmerged.

Two superseded branches remain on `origin` and are not yet disposed of. That
disposal is carried as **C-2**. No conformance-only engine has entered the
production dependency graph.

### D-4 — Branch naming · **PROCEDURAL**

Execution used session-designated branches rather than `ck003/cross-language-canonical-001`. No protocol-semantic impact.

### D-5 — Artifact commit identity · **PROCEDURAL**

Artifacts record the clean source commit that produced them; the publication commit is separate, avoiding self-referential commit identity. Re-running RI-RS evidence generation would update execution metadata; the canonical bytes, digest and leaf are deterministic and would not change.

### D-6 — Corpus transport · **PROCEDURAL**

The RI-RS artifact was generated in `aura-guard-v1.3` and transported byte-identically into the RI-PY corpus used by the gate. Both copies hash to `a6ebad01…59af329c`. It was not reconstructed or re-keyed.

### D-7 — Event-type interaction · **REPORTED, NOT RESOLVED**

CANONICAL-001 carries `"event_type": "AUDIT_RECORD"`. The Event-Type Registry currently registers no tokens and requires strict-mode rejection of unregistered tokens. See §14 and CFL-005. Not repaired here; DQ-004 governs.

---

## 11. Traceability

```text
DQ-006  ── closures/DQ-006_CLOSURE_PACKAGE.md  (this record)
  │
  ├─ APS-200 §8            aps/APS-200_CANONICAL_DATA_MODEL.md §8.1–8.9   NORMATIVE AUTHORITY
  │     └─ INV-003         invariants/INVARIANT_REGISTRY.md
  │
  ├─ APS-300 §5            aps/APS-300_EVIDENCE_MODEL.md §5.1–5.3         evidence-hash byte domain
  │
  ├─ ADR-CK003-DQ006       ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md
  │
  ├─ CONF-003              conformance/CONF-003_CANONICAL_SERIALIZATION.md   verdict PARTIAL
  │     └─ APS-400 §4      aps/APS-400_CONFORMANCE_TEST_MATRIX.md
  │
  └─ CANONICAL-001         fixtures/corpus/CANONICAL-001_jcs_evidence.json
        │
        ├─ RI-PY   aura-poc-a-core-v3.3 @ 49d0e4f6 (exec) / 3e8e0e32 (evidence)
        │            conformance/canonical/jcs.py
        │            conformance/canonical/test_jcs_behavior.py            13 passed
        │            conformance/canonical/test_canonical_001.py            1 passed
        │            conformance/corpus/canonical-001/ri-py.json            6b5b5ccd…5f2b856c
        │
        ├─ RI-RS   aura-guard-v1.3 @ 4e9e2284 (exec) / 420653e2 (evidence)
        │            conformance/canonical/jcs.rs
        │            conformance/canonical/test/canonical_001.rs            4 passed
        │            conformance/corpus/canonical-001/ri-rs.json            a6ebad01…59af329c
        │
        └─ CROSS-LANGUAGE-001
             conformance/canonical/test_cross_language_canonical_001.py     13 passed
             conformance/canonical/negative_controls_canonical_001.py       exit 0
             conformance/corpus/canonical-001/EXECUTION-EVIDENCE.md
                │
                ├─ canonical_bytes   100 B, 7b226576…22312e30227d
                ├─ SHA-256           b6c3660c…a139a4e6
                └─ RFC 6962 leaf     ce6b3673…6648c039
```

The same chain for CANONICAL-002 runs through
`fixtures/corpus/CANONICAL-002_jcs_evidence.json` to RI-PY `@ 7bcc600f` and
RI-RS `@ bd4a2fa6`, and terminates in
`CROSS-LANGUAGE-CANONICAL-002` (655 B · `cdceb081…` · `20fd6065…`).

The full traceability graph, link table and adjacent-decision status table are
maintained in
[`ck003/dq-006-closure/DQ-006_TRACEABILITY.md`](../ck003/dq-006-closure/DQ-006_TRACEABILITY.md);
the consolidated evidence record is
[`ck003/dq-006-closure/DQ-006_EVIDENCE.md`](../ck003/dq-006-closure/DQ-006_EVIDENCE.md).

Every link above is identified by repository path plus section, test or document identifier. Evidence-side paths resolve on the branches named in §5, §6 and §4.1, not on `main` (carried item C-1).

---

## 12. Closure criteria

| # | Criterion | State |
|---|---|---|
| 1 | Normative canonical serialization rule exists in the specification | **MET** — APS-200 §8 |
| 2 | Evidence-hash byte domain bound to canonical bytes | **MET** — APS-300 §5.1 |
| 3 | Decision recorded in an ADR distinguishing contract from implementation detail | **MET** — ADR-CK003-DQ006 §2 |
| 4 | Conformance requirement expresses byte-level cross-implementation equality | **MET** — CONF-003 §4.2, §5 |
| 5 | A frozen normative cross-language fixture exists | **MET** — CANONICAL-001 |
| 6 | RI-PY independent execution | **MET** |
| 7 | RI-RS independent execution | **MET** |
| 8 | Canonical byte / SHA-256 / RFC 6962 leaf equality, independently recomputed | **MET** |
| 9 | Discriminating negative controls | **MET** |
| 10 | Production runtime unchanged | **MET** |
| 11 | Version and migration semantics recorded | **MET** — APS-200 §8.8, APS-300 §5.3 |
| 12 | Single normative authority; no competing definition | **MET** — APS-200 §8.2; superseded records marked |
| 13 | Evidence discriminates RFC 8785 from sorted JSON, cross-language | **MET** — CANONICAL-002; see §10 D-1 |
| 14 | Evidence reachable from each reference repository's default branch | **PARTIAL** — reachable by SHA on `origin`, not merged to `main`; carried as C-1 |
| 15 | RI-RS conformance boundary of record decided, alternatives disposed | **PARTIAL** — `aura-guard` `main` now carries a JCS conformance boundary and CANONICAL-002 was executed on it; two superseded branches remain undisposed. Carried as C-2 |
| 16 | Chief Architect ratification of the verdict | **MET** — DQ-006 CLOSURE INTEGRATION order, 2026-08-20 |

Criteria 1–13 and 16 are met. Criteria 14 and 15 are partially met and are
carried forward as release-gate items, not as evidence-validity defects: the
evidence exists, is published, and was independently re-verified. What is
outstanding is repository hygiene — merging and branch disposal — which belongs
to the release gate, not to the canonical serialization decision.

---

## 13. Carried items

DQ-006 is closed. The following are carried forward. None of them qualifies the
canonical serialization decision or the evidence behind it; each is repository
hygiene or an adjacent decision with its own owner.

| ID | Item | Owner | Gate |
|---|---|---|---|
| **C-1** | Merge the CANONICAL-001 and CANONICAL-002 evidence to the default branch of both reference repositories. Evidence is published and reachable by SHA today; it is not on `main`. | RI-PY + RI-RS | Release |
| **C-2** | Dispose of the two superseded RI-RS conformance branches on `origin`. `main` already carries the boundary of record. | Protocol Custodian | Release |
| **C-3** | Rename the RI-side `CROSS-LANGUAGE-002` identifier for the CANONICAL-002 equality gate. That identifier is already assigned in this specification to the DQ-002 Merkle gate. This specification uses `CROSS-LANGUAGE-CANONICAL-002` to disambiguate. Traceability defect only: no digest, byte or verdict is affected. | RI-PY + RI-RS | Release |

Closed by this integration: **R1** (discriminating cross-language vector) and
**R4** (ratification). **R2** and **R3** are carried as C-1 and C-2 above.

Explicitly **not** items of DQ-006: CFL-001 (cross-corpus governance precedence)
and CFL-005 (empty event-type registry). Both are reported in §14; neither is
DQ-006's to resolve.

---

## 14. Reported conflicts — not resolved by this package

- **CFL-001** — the specification corpus and the implementation corpus make incompatible statements about canonical encoding, and no cross-corpus precedence rule exists in either. Binding APS-200 §8 settles the question *within the specification corpus*; it does not adjudicate which governance ladder wins cross-corpus. Routed to the Protocol Custodian.
- **CFL-005** — CANONICAL-001 carries `event_type: "AUDIT_RECORD"`, which the Event-Type Registry does not register, while requiring strict-mode rejection of unregistered tokens. Under the registry's own rule, strict conformance would reject the object this gate rests on. Canonicalization determines representation, never event semantics (APS-200 §8.7), so DQ-006 does not repair this. DQ-004 governs.
- **DQ-002 dependency** — [`closures/DQ-002_FINAL_CLOSURE.md`](DQ-002_FINAL_CLOSURE.md) records DQ-002 as CLOSED / PASS on the stated basis that DQ-006 is PASS. That dependency is now **satisfied**, and the evidentiary weakness it previously inherited (deviation D-1) is repaired by CANONICAL-002. **DQ-002's status is unchanged by this integration** — it was already CLOSED, no status transition was performed, and no new architectural decision about DQ-002 was made here.

---

## 15. Final verdict

```text
Normative specification closure  : CLOSED   (criteria 1-4, 11, 12)
Conformance evidence closure     : CLOSED   (criteria 5-10, 13)
Ratification                     : RECORDED (criterion 16)
Repository hygiene               : CARRIED  (criteria 14, 15 -> C-1, C-2)

DQ-006 = CLOSED
```

The canonical serialization boundary for the Aura Protocol is **RFC 8785 JCS**,
normatively bound in APS-200 §8, with `SHA-256(canonical_bytes)` as the content
digest and `SHA-256(0x00 || canonical_bytes)` as the RFC 6962 leaf.

Two independent conformance implementations — `rfc8785` 0.1.4 in RI-PY and
`serde_json_canonicalizer` 0.3.2 in RI-RS — independently produce identical
canonical bytes, identical SHA-256 and identical RFC 6962 leaf for both
CANONICAL-001 and CANONICAL-002. CANONICAL-002 is JCS-discriminating: a
sorted-JSON serializer passes the CANONICAL-001 gate and fails this one. The
result therefore evidences conformance to RFC 8785, not merely agreement.

Both JCS engines remain **conformance-scoped**. This closure does not state, and
must not be read as stating, that production Core or Guard uses JCS. No
production hash, Merkle, event-type or protocol-semantics code was changed by any
of the work behind this closure.

**No production runtime change is implied or authorized by this package.**

This closure does not by itself close DQ-002, DQ-003, DQ-004, APS-001,
INV-001…INV-015, the fixture corpus, the CI gate or the release gate.

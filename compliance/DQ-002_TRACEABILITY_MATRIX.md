# DQ-002 — Traceability Matrix

**Document ID:** COMP-TR-DQ002-001
**Classification:** EVIDENCE — NON-NORMATIVE
**Audit date:** 2026-08-20
**Audit target:** `main` @ `19ddeef5672cd3d19a1049a31d85565396783a72` + current CK-003 closure material
**Primary closure under audit:** `closures/DQ-002_FINAL_CLOSURE.md` (Status: CLOSED — PASS)
**Companion review:** [DQ-002_TRACEABILITY_REVIEW.md](DQ-002_TRACEABILITY_REVIEW.md)

> This document records traceability. It does not reopen DQ-002, does not change DQ-002
> semantics, does not approve any ADR, and confers no normative status. It is a supplement to
> `compliance/TRACEABILITY_MATRIX.md` under the chain defined in `compliance/README.md`.

---

## 1. Status legend

| Token | Meaning |
|---|---|
| `PASS` | Claim is supported by a normative source **and** by executable evidence located in this audit. |
| `PARTIAL` | Executable evidence supports the claim, but the normative source is DRAFT/PROPOSED/TODO. |
| `GAP` | A mandatory link in the chain is absent. No support was invented to fill it. |
| `CONTRADICTION` | Two repository artifacts assert incompatible states for the same claim. |

Chain columns follow `compliance/README.md`: requirement → normative source → conformance
requirement → fixture → executable evidence → RI-PY → RI-RS → cross-language → status.

---

## 2. Requirement traceability

### R-01 — Canonicalization boundary

| Link | Value |
|---|---|
| DQ-002 statement | `closures/DQ-002_FINAL_CLOSURE.md` §2.1 — "Canonical input is serialized using the frozen RFC 8785 JCS profile." |
| Normative source | **GAP.** `aps/APS-200_CANONICAL_DATA_MODEL.md` §8:218 still reads `**TODO**: Define the canonical serialization format for interoperability between RI-PY and RI-RS`; document is `1.0-DRAFT / DRAFT`. `specification/APS-001_PROTOCOL_SPECIFICATION.md` §7.1 explicitly defers: "The serialization profile producing `canonical bytes` is owned by APS-200." The amendment `ck003/dq-006-canonical-serialization/APS-200-SECTION-8-PROPOSED.md` is `PROPOSED — not yet frozen`. |
| Conformance requirement | `conformance/CONF-003_CANONICAL_SERIALIZATION.md` — `1.0-DRAFT / DRAFT`, §3 carries `TODO`, and cites fixture `FIX-001`, not CANONICAL-001. |
| Fixture | `fixtures/corpus/CANONICAL-001_jcs_evidence.json`. **Not registered in APS-500** (0 occurrences of `CANONICAL-001` in `aps/APS-500_REFERENCE_FIXTURES.md`; §5 is `TODO`). |
| Executable evidence | `conformance/canonical/test_cross_language_canonical_001.py` — RI-PY repo, branch `claude/cross-language-canonical-001-n4v2c5` only. Not on any `main`. |
| RI-PY | `rfc8785==0.1.4`; artifact `conformance/corpus/canonical-001/ri-py.json`, SHA-256 `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c` — **verified in this audit**, matches `ck003/DQ-006_EVIDENCE_INDEX.md`. |
| RI-RS | `serde_json_canonicalizer==0.3.2`; artifact `ri-rs.json`, SHA-256 `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` — **verified in this audit**, matches the evidence index. |
| Cross-language | CROSS-LANGUAGE-001 = PASS. Both artifacts declare the same `input_sha256` `649bb748…39261` and identical canonical bytes under two independent engines. |
| **Status** | **PARTIAL** — executable evidence is sound; no frozen normative source exists. |

---

### R-02 — SHA-256 digest domain

| Link | Value |
|---|---|
| DQ-002 statement | §2.2 — `SHA-256(canonical_bytes)`. |
| Normative source | `aps/APS-200…md:58` (`integrity_hash` = SHA-256 of canonical serialization) and `specification/APS-001…md` §7.2 (SHA-256 is the canonical primitive). Both DRAFT. `aps/APS-300_EVIDENCE_MODEL.md:73` still reads `**TODO**: Define the canonical algorithm for computing evidence_hash`. |
| Conformance requirement | `conformance/CONF-010_CRYPTOGRAPHIC_VERIFICATION.md` — `1.0-DRAFT / DRAFT`, §3 `TODO`, cites `FIX-001`. |
| Fixture | CANONICAL-001, field `canonical_sha256_hex`. |
| Executable evidence | Cross-language runner (unmerged branch, as R-01). |
| RI-PY | `sha256` = `b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6`. |
| RI-RS | Identical value, independently produced. |
| Cross-language | SHA equality PASS. **Independently recomputed in this audit** from the published canonical bytes: match. |
| **Status** | **PARTIAL** — digest arithmetic verified; normative source DRAFT with an open TODO in APS-300. |

---

### R-03 — RFC-6962 leaf domain

| Link | Value |
|---|---|
| DQ-002 statement | §2.3 — `SHA-256(0x00 \|\| canonical_bytes)`. |
| Normative source | `specification/APS-001…md` §7.1/§7.2 states the leaf domain, but labels it "the **proposed** canonical model", and the document is `0.2-DRAFT / DRAFT — ARCHITECTURE REVIEW REQUIRED`. `ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` is `PROPOSED — awaiting Chief Architect approval`. **`aps/APS-300_EVIDENCE_MODEL.md` contains no Merkle, RFC-6962 or `0x00` language at all.** |
| Conformance requirement | **GAP** — no CONF-nnn covers the Merkle leaf domain. CONF-010 addresses `evidence_hash`/`input_hash`/`output_hash` only; `aps/APS-400…md` assigns no Merkle test. |
| Fixture | CANONICAL-001 `merkle_leaf_hash_hex`; `ck003/dq-002-hash-domain/fixtures/FIX-CK003-DQ002-RFC6962-2LEAF.json`. |
| Executable evidence | CROSS-LANGUAGE-001 runner (leaf only); `conformance/merkle/` in RI-PY — **branch `claude/aura-cross-language-002-6t2kdo` only, absent from RI-PY `main`**. |
| RI-PY | `leaf_sha256` = `ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039`. |
| RI-RS | Identical. RI-RS `main` additionally carries `tests/ck003_dq002_ri_rs_conformance.rs` and `.github/workflows/ck003-dq002.yml`. |
| Cross-language | Leaf equality PASS (CROSS-LANGUAGE-001); leaf A/B PASS (CROSS-LANGUAGE-002). **Independently recomputed in this audit**: match. |
| **Status** | **PARTIAL** — evidence strong; no conformance requirement assigned, normative source DRAFT/proposed. |

---

### R-04 — Raw `0x00` prefix (one octet, not ASCII)

| Link | Value |
|---|---|
| DQ-002 statement | §2.4 — "`0x00` is a raw binary octet, not the ASCII string `\"0x00\"`." |
| Normative source | APS-001 §7.2 (DRAFT); ADR-CK003-DQ002 §3.2 (PROPOSED). |
| Conformance requirement | **GAP** — none assigned. |
| Fixture | CANONICAL-001 `leaf_algorithm`; FIX-CK003-DQ002-RFC6962-2LEAF. |
| Executable evidence | Negative control NC-1 ("leaf without `0x00` prefix must differ") in `ck003/dq-002-hash-domain/CROSS-LANGUAGE-002-EVIDENCE.md` §9; wrong-leaf-domain control in CROSS-LANGUAGE-001. |
| RI-PY | NC-1 PASS. |
| RI-RS | NC-1 PASS. |
| Cross-language | CROSS-LANGUAGE-002 = **CONDITIONAL PASS**. |
| **Status** | **PARTIAL** |

---

### R-05 — No textual / hexadecimal wrapper between canonicalization and hashing

| Link | Value |
|---|---|
| DQ-002 statement | §2.5 — no JSON reserialization, hex representation, whitespace transformation or textual wrapper. |
| Normative source | APS-001 §7.1 ("hexadecimal strings are presentation values and MUST NOT substitute for underlying digest bytes") — DRAFT; ADR-CK003-DQ002 §3 clause 3 — PROPOSED. |
| Conformance requirement | **GAP** — none assigned. |
| Fixture | FIX-CK003-DQ002-RFC6962-EDGE-MATRIX.json. |
| Executable evidence | NC-3 (`hex(left) ‖ hex(right)` as node input must differ) — PASS both implementations. Recorded: "RI-PY's Merkle primitives additionally reject `str` and non-32-byte digests at the hash boundary." |
| RI-PY | NC-3 PASS (in `conformance/merkle/`, unmerged branch). |
| RI-RS | NC-3 PASS. |
| Cross-language | CROSS-LANGUAGE-002 CONDITIONAL PASS. |
| **Status** | **PARTIAL** |

---

### R-06 — RFC-6962 interior-node domain (`0x01`)

| Link | Value |
|---|---|
| DQ-002 statement | §2.6 — "RFC 6962 interior-node domain separation remains `0x01` and is not substituted for the leaf domain." |
| Normative source | APS-001 §7.1/§7.2 (DRAFT, "proposed"); ADR-CK003-DQ002 §3.3 (PROPOSED). |
| Conformance requirement | **GAP** — none assigned. |
| Fixture | `fixtures/ck003/expected_digests.json` (`node` domain declared, all `expected_digest` = `null`, status `EXPECTED_VALUES_PENDING_CANONICAL_SERIALIZATION`); FIX-CK003-DQ002-RFC6962-EDGE-MATRIX.json. |
| Executable evidence | **Not covered by CROSS-LANGUAGE-001.** Both cited artifacts (`ri-py.json`, `ri-rs.json`) contain only `canonical_bytes_hex`, `sha256` and `leaf_sha256` — **no node digest and no root**, confirmed by direct inspection in this audit. Node/root/proof coverage exists only in CROSS-LANGUAGE-002. |
| RI-PY | NC-2 PASS and N = 0…8 roots match — but only in `conformance/merkle/`, which is **absent from RI-PY `main`**. RI-PY `main` carries `audit/merkle.py`, documented in the ADR as hex-string concatenation with last-node duplication — i.e. **not** the DQ-002 contract. |
| RI-RS | `src/merkle.rs` implements the contract; `tests/dq002_cross_language.rs` on the unmerged branch, 9 tests. |
| Cross-language | **CONTRADICTION** — `ck003/dq-002-hash-domain/CROSS-LANGUAGE-002-EVIDENCE.md` = `CONDITIONAL PASS`; `ck003/cross-language-002/CROSS-LANGUAGE-002-EVIDENCE.md` = `OPEN — execution gate not yet PASS`, with `Root equality: NOT ESTABLISHED`, `RI-PY actual execution: NOT PASS`, `RI-RS actual execution: NOT RUN`. Both are present at HEAD; neither references the other; neither is marked `SUPERSEDED`. |
| **Status** | **CONTRADICTION + GAP** — the closure's only interior-node claim rests on evidence that a sibling artifact records as not established, and `DEFECT-DQ002-F1` (OPEN) records a wrong `node.digest_hex` in a file self-designated `NORMATIVE_TEST_VECTOR`. |

---

### R-07 — Canonical bytes equality

| Link | Value |
|---|---|
| DQ-002 statement | §4 — canonical bytes equality PASS. |
| Normative source | APS-001 §10:139 — "they MUST produce byte-identical canonical bytes … for shared fixtures" (DRAFT). |
| Conformance requirement | CONF-003 (DRAFT). |
| Fixture | CANONICAL-001. |
| Executable evidence | `test_cross_language_canonical_001.py` (unmerged branch). |
| RI-PY | `canonical_bytes_hex`, 100 bytes. |
| RI-RS | Identical hex, 100 bytes. |
| Cross-language | PASS. **Re-verified in this audit**: hex decodes to exactly 100 bytes. |
| **Status** | **PASS** (evidence layer). See REVIEW §4 on discrimination. |

---

### R-08 — Digest equality

| Link | Value |
|---|---|
| Normative source | APS-001 §10:139 (DRAFT). |
| Conformance requirement | CONF-010 (DRAFT). |
| Fixture | CANONICAL-001. |
| Executable evidence | Cross-language runner + independent SHA recomputation on both sides. |
| RI-PY / RI-RS | Both `b6c3660c…39a4e6`. |
| Cross-language | PASS — **recomputed independently in this audit**: `sha256(canonical_bytes)` = `b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6`. |
| **Status** | **PASS** (evidence layer). |

---

### R-09 — Leaf equality

| Link | Value |
|---|---|
| Normative source | APS-001 §7.2 (DRAFT). |
| Conformance requirement | **GAP**. |
| Fixture | CANONICAL-001. |
| Executable evidence | Cross-language runner + independent leaf recomputation on both sides; wrong-leaf-domain (`0x01`) negative control. |
| RI-PY / RI-RS | Both `ce6b3673…48c039`. |
| Cross-language | PASS — **recomputed independently in this audit**: `sha256(0x00 ‖ B)` = `ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039`; `sha256(0x01 ‖ B)` = `491a8dcc…9a10b1`, confirming the domain separator is discriminating. |
| **Status** | **PASS** (evidence layer). |

---

### R-10 — Production boundary

| Link | Value |
|---|---|
| DQ-002 statement | §5 — "did not modify production hash/Merkle core behavior. JCS engines are conformance-only … not a mandate to introduce JCS into production runtime." |
| Normative source | ADR-CK003-DQ002 "Compatibility and migration rule" (PROPOSED); `ck003/README.md` operating rule. |
| Conformance requirement | Not applicable — a scope constraint, not a protocol behaviour. |
| Fixture | Not applicable. |
| Executable evidence | Production-integrity checks recorded in `closures/DQ-006_CLOSURE_PACKAGE.md` §7 (RI-PY `core/`, `audit/` unchanged; RI-RS `src/`, root `Cargo.toml`, root `Cargo.lock` unchanged). RI-RS conformance workspace uses its own `conformance/Cargo.lock` (`3ff49a0f…`), confirmed in `ri-rs.json` provenance. |
| RI-PY | `audit/merkle.py` remains the legacy contract — **consistent** with the ADR's migration rule forbidding recomputation of historical evidence. |
| RI-RS | Production `src/` unchanged. |
| Cross-language | Not applicable. |
| **Status** | **PASS**, with the caveat in REVIEW §5 (an open conflict, CFL-003, records a competing RI-RS branch that would place the JCS engine in the production dependency graph). |

---

## 3. Summary

| Requirement | Status |
|---|---|
| R-01 canonicalization boundary | PARTIAL |
| R-02 SHA-256 digest domain | PARTIAL |
| R-03 RFC-6962 leaf domain | PARTIAL |
| R-04 raw `0x00` prefix | PARTIAL |
| R-05 no textual/hex wrapper | PARTIAL |
| R-06 RFC-6962 interior-node `0x01` | **CONTRADICTION + GAP** |
| R-07 canonical bytes equality | PASS |
| R-08 digest equality | PASS |
| R-09 leaf equality | PASS |
| R-10 production boundary | PASS |

**4 PASS · 5 PARTIAL · 1 CONTRADICTION + GAP.**

---

## 4. INV / CONF mapping

Only relationships supported by repository material are recorded. Invariants with no
DQ-002 relationship are not forced into the table.

| Invariant | Relation | Conformance test | Basis | Registry status |
|---|---|---|---|---|
| INV-003 Canonical Serialization | **DIRECT** | CONF-003 (DRAFT) | `invariants/INVARIANT_REGISTRY.md:47` maps INV-003 → APS-200 §8, the section DQ-002 R-01 depends on | `ck003/APS001_INV_MATRIX/…:18` — **BLOCKED — APS-200 serialization still open** |
| INV-011 Cryptographic Integrity | **DIRECT** | CONF-010 (DRAFT) | Registry maps INV-011 → APS-300 §7; DQ-002 R-02/R-03 define the digest domain it verifies | `…:26` — **OPEN — DQ-002 + canonical bytes required** |
| INV-006 Platform Independence | **INDIRECT** | CONF-006 | `HASH_DOMAIN_EVIDENCE.md`: "Cross-language byte equality is required for the evidence domain"; supported by R-07/R-08/R-09 | OPEN |
| INV-014 Reference Compatibility | **INDIRECT** | CONF-014 | `HASH_DOMAIN_EVIDENCE.md`: "Fixture is the conformance mechanism"; ADR §Related cites INV-014 | OPEN — APS-500 corpus/version binding not frozen |
| INV-004 Immutable Evidence | **INDIRECT** | CONF-004 | ADR migration rule: "No historical digest may be recomputed and presented as unchanged evidence" | OPEN |
| INV-012 Auditability | **GAP** | CONF-012 | Registry closure note: "final PASS depends on the normative ENT-007/event-type and hash-domain contracts". CFL-005 records that the empty event-type registry would reject CANONICAL-001's `AUDIT_RECORD` token in strict mode | OPEN |
| INV-001, 002, 005, 007, 008, 009, 010, 013, 015 | **NOT APPLICABLE** | — | No repository material links them to the DQ-002 hash-domain contract | — |

**Merkle-specific coverage:** no CONF-nnn in `conformance/` or `aps/APS-400…md` covers the
RFC-6962 leaf domain, interior-node domain, tree shape, or inclusion proofs. This is the
single largest structural gap — recorded as **GAP-06** in the review.

---

*This matrix records traceability and fills no gap. It confers no normative semantics.*

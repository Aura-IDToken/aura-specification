# DQ-006 Cross-Language Equality Matrix

Document ID: DQ-006-XLANG-MATRIX  
Version: 1.0  
Status: EVIDENCE  
Classification: Evidence Matrix (CK-003)  
Authority: `DQ-006-CLOSURE.md`  
Last Review: 2026-08-20

Gate: `CROSS-LANGUAGE-001`  
Fixture: `CANONICAL-001`  
Verdict: **PASS**

---

## 1. Equality matrix

| Property | RI-PY | RI-RS | Equality |
|---|---|---|---|
| canonical bytes (hex) | `7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d` | `7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d` | **PASS** |
| canonical bytes length | `100` | `100` | **PASS** |
| SHA-256 | `b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6` | `b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6` | **PASS** |
| RFC-6962 leaf | `ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039` | `ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039` | **PASS** |
| leaf domain | `0x00` (raw octet) | `0x00` (raw octet) | **PASS** |
| canonicalization profile | `RFC8785` | `RFC8785` | **PASS** |

---

## 2. Implementation provenance

| Field | RI-PY | RI-RS |
|---|---|---|
| Repository | `Aura-IDToken/aura-poc-a-core-v3.3` | `Aura-IDToken/aura-guard-v1.3` |
| Execution commit | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` |
| Artifact publication commit | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |
| Engine | `rfc8785` | `serde_json_canonicalizer` |
| Engine version | `0.1.4` | `0.3.2` |
| Engine pin | `conformance/requirements-conformance.txt` | `conformance/Cargo.toml` + `conformance/Cargo.lock` |
| Adapter | `conformance/canonical/jcs.py` | `conformance/canonical/jcs.rs` |
| Execution command | `python -m conformance.canonical.emit_ri_py_artifact` | `cargo test --locked --test canonical_001` |
| Toolchain | CPython 3.11.15 | rustc 1.94.1 (e408947bf 2026-03-25) |
| Platform | Linux x86_64 | Linux x86_64 |
| Worktree clean | `true` | `true` |
| Artifact | `conformance/corpus/canonical-001/ri-py.json` | `conformance/corpus/canonical-001/ri-rs.json` |
| Artifact SHA-256 | `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c` | `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` |

Both artifacts were produced from the same frozen input
(`conformance/corpus/canonical-001/input.json`,
SHA-256 `649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261`), held byte-identically
in both repositories.

---

## 3. Independence

| Property | Evidence |
|---|---|
| RI-RS reads no RI-PY value, path or artifact | RI-RS conformance crate is self-contained; recorded in `4e9e228` / `420653e` |
| RI-PY artifact emitter reads no frozen expected constant | `conformance/canonical/emit_ri_py_artifact.py` produces output from an actual adapter run |
| Equality runner never canonicalizes | `conformance/canonical/test_cross_language_canonical_001.py` compares two independently produced artifacts and does not invoke a canonicalizer, re-serialize the input, or construct canonical bytes |
| Frozen expected values are secondary only | `manifest.json`: *"Frozen reference values. SECONDARY cross-check only. Never used to produce, patch or backfill an execution artifact."* |
| Engine versions are resolved, not asserted | RI-RS `build.rs` resolves the engine version from `conformance/Cargo.lock` |

---

## 4. Gate checks

| Check | Result |
|---|---|
| RI-PY canonical bytes independently produced | PASS |
| RI-RS canonical bytes independently produced | PASS |
| canonical bytes equality | PASS |
| RI-PY SHA-256 independent recomputation | PASS |
| RI-RS SHA-256 independent recomputation | PASS |
| SHA-256 equality | PASS |
| RI-PY leaf independent recomputation | PASS |
| RI-RS leaf independent recomputation | PASS |
| leaf equality | PASS |
| RI-PY vs frozen expected (secondary) | PASS |
| RI-RS vs frozen expected (secondary) | PASS |
| RI-PY production integrity | PASS |
| RI-RS production integrity | PASS |

---

## 5. Negative controls

| Control | Mutation | Expected | Observed |
|---|---|---|---|
| A | canonical bytes modified | gate FAILS | gate FAILED as required |
| B | recorded SHA-256 modified | gate FAILS | gate FAILED as required |
| C | leaf domain `0x00` → `0x01` | gate FAILS | gate FAILED as required, via independent leaf recomputation |

Mutations were applied to temporary copies only; the committed corpus was verified unchanged
afterwards.

**Control C is load-bearing.** A symmetric mutation — the same wrong leaf domain applied to both
implementations — preserves `RI-PY leaf == RI-RS leaf`. Equality between implementations would
accept it. Only independent recomputation of the leaf from each artifact's own canonical bytes
detects it. See `DQ-006-CLOSURE.md` §8.1.

---

## 6. Boundary

This matrix evidences equality for the executed `CANONICAL-001` vector and the associated
conformance boundary. It does not generalise to arbitrary JSON inputs, to future schema
versions, or to production runtime behaviour. See `DQ-006-CLOSURE.md` §11.

# DQ-006 Evidence Index

Document ID: DQ-006-EVIDENCE-INDEX  
Version: 1.0  
Status: EVIDENCE  
Classification: Evidence Index (CK-003)  
Authority: `DQ-006-CLOSURE.md`  
Last Review: 2026-08-20

This index binds the DQ-006 closure record to the executed evidence. The specification
repository holds the closure, the index and the traceability; the **reference implementation
repositories remain the source of the execution artifacts**. Nothing here duplicates an
execution artifact.

Evidence identifiers use the `DQ006-Enn` scheme, consistent with the existing CK-003 practice of
namespacing artifact identifiers to their decision (`DEFECT-DQ002-Fn`,
`FIX-CK003-DQ002-*`).

---

## 1. Evidence table

| Evidence ID | Description | Repository | Path | Commit | Status |
|---|---|---|---|---|---|
| `DQ006-E01` | RI-PY JCS conformance boundary — adapter, pinned engine `rfc8785==0.1.4`, engine-behaviour suite (`JCS-B01…B06` register label) | `Aura-IDToken/aura-poc-a-core-v3.3` | `conformance/canonical/jcs.py`, `conformance/requirements-conformance.txt`, `conformance/canonical/test_jcs_behavior.py`, `conformance/canonical/test_canonical_001.py` | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` | PASS |
| `DQ006-E02` | RI-RS JCS conformance boundary — adapter, pinned engine `serde_json_canonicalizer==0.3.2`, isolated conformance crate and lockfile | `Aura-IDToken/aura-guard-v1.3` | `conformance/canonical/jcs.rs`, `conformance/canonical/test/canonical_001.rs`, `conformance/Cargo.toml`, `conformance/Cargo.lock`, `conformance/build.rs` | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` | PASS |
| `DQ006-E03` | CANONICAL-001 RI-PY execution artifact (`artifact SHA-256 6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c`) | `Aura-IDToken/aura-poc-a-core-v3.3` | `conformance/corpus/canonical-001/ri-py.json` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` | PASS |
| `DQ006-E04` | CANONICAL-001 RI-RS execution artifact (`artifact SHA-256 a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c`) | `Aura-IDToken/aura-guard-v1.3` | `conformance/corpus/canonical-001/ri-rs.json` | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` | PASS |
| `DQ006-E05` | CROSS-LANGUAGE-001 equality gate — independent recomputation, byte/digest/leaf equality, frozen-expected secondary cross-check; corpus manifest and execution evidence | `Aura-IDToken/aura-poc-a-core-v3.3` | `conformance/canonical/test_cross_language_canonical_001.py`, `conformance/corpus/canonical-001/manifest.json`, `conformance/corpus/canonical-001/EXECUTION-EVIDENCE.md` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` | PASS |
| `DQ006-E06` | Negative controls — mutated canonical bytes, mutated SHA-256, wrong leaf domain (`0x00` → `0x01`) | `Aura-IDToken/aura-poc-a-core-v3.3` | `conformance/canonical/negative_controls_canonical_001.py` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` | PASS |
| `DQ006-E07` | Production integrity — `core/`, `audit/`, `src/`, production `Cargo.toml`, production `Cargo.lock` unchanged; JCS engines confined to conformance scope | `Aura-IDToken/aura-poc-a-core-v3.3` + `Aura-IDToken/aura-guard-v1.3` | recorded in the execution/publication commit records | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e`, `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` | PASS |

The RI-RS artifact `DQ006-E04` is also present, byte-identically, in the shared corpus of
`Aura-IDToken/aura-poc-a-core-v3.3` at commit `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e`, which
is where the equality runner reads it.

---

## 2. Immutable references

| Reference | Value |
|---|---|
| RI-PY execution commit | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` |
| RI-PY artifact publication commit | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| RI-RS execution commit | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` |
| RI-RS artifact publication commit | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |

Evidence is referenced by commit SHA. The `CANONICAL-001` conformance tree is **not** present on
the default branch of either reference implementation repository; commit-addressed references
remain valid, and merging plus CI execution is a separate GATE C action
(`DQ-006-CLOSURE.md` §13.2).

---

## 3. Frozen fixture values

```text
canonical_bytes_len: 100

canonical_bytes_hex:
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d

sha256:
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6

leaf_sha256 (SHA-256(0x00 || canonical_bytes)):
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039

input.json sha256:
649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261
```

These values are `NORMATIVE FIXTURE VALUES` for `CANONICAL-001`, as recorded in
`DQ-006-CLOSURE.md` §6.

---

## 4. Artifact digests

| Artifact | SHA-256 |
|---|---|
| `ri-py.json` | `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c` |
| `ri-rs.json` | `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` |
| RI-PY adapter `conformance/canonical/jcs.py` | `8f6c3b440221113721a82c6ff3ff61dcfbaccbcbe972ce7ae635d00444b8b5a4` |
| RI-RS adapter `conformance/canonical/jcs.rs` | `0dae4ef696f06a4d3248ca85284fd7db280ef3c897a96cf898ef076cd4e846f2` |
| RI-RS `conformance/Cargo.lock` | `3ff49a0f01aafa9925dc2904927f0810a2628d24ff944b200c7858c06a534638` |

---

## 5. Governance boundary

This index records conformance evidence. It does not authorize production runtime changes, does
not amend APS text, and does not collapse any other decision into DQ-006.

```text
CROSS-LANGUAGE-001 = PASS
DQ-006             = CLOSED / PASS
DQ-002             = NOT CLOSED BY THIS PACKAGE
DQ-001             = NOT CLOSED BY THIS PACKAGE
APS-001            = NOT CLOSED, NOT AMENDED BY THIS PACKAGE
INV-001…INV-015    = NOT CLOSED BY THIS PACKAGE
```

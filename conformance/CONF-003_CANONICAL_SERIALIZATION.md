# CONF-003 CANONICAL SERIALIZATION

Document ID: CONF-003
Version: 1.1-DRAFT
Status: DRAFT
Classification: **Normative Conformance Requirement**
Authority: APS-400 §4
Normative source: APS-200 §8 (canonical serialization) · APS-300 §5 (evidence-hash domain)
Related Invariant: INV-003 (also exercises INV-006, INV-011)
Related Decision: ADR-CK003-DQ006 · DQ-006
Last Review: 2026-08-20

---

## 1. Purpose

Verify that a protocol object has exactly one canonical byte representation under APS-200 §8, that independent implementations produce that same byte sequence, and that the digest and Merkle-leaf domains are computed over those bytes and nothing else.

**This document is a normative conformance requirement.** An implementation that does not satisfy §5 does not conform to INV-003, regardless of any documentation it publishes.

CONF-003 does not define canonical serialization. APS-200 §8 does. This test verifies it.

---

## 2. Related APS

- APS-100: INV-003, INV-006, INV-011
- APS-200 §8: canonical serialization profile (normative authority)
- APS-300 §5: evidence-hash byte domain
- APS-400 §4: CONF-003
- APS-500: Reference Fixtures

---

## 3. Preconditions

1. Two independent conformant implementations are available (currently RI-PY and RI-RS).
2. Each implementation exposes a canonicalization boundary that returns raw `canonical_bytes` — not a digest, not a hexadecimal string, not a re-parsed object.
3. A canonical fixture is loaded, byte-identically, by both implementations from the same frozen input file, identified by the SHA-256 of that file.
4. Neither implementation reads the other's artifact, and neither reads a frozen expected value in order to produce its own output.
5. No state from a prior test run is present.

Bound fixture: **CANONICAL-001** — [`fixtures/corpus/CANONICAL-001_jcs_evidence.json`](../fixtures/corpus/CANONICAL-001_jcs_evidence.json).

---

## 4. Test Procedure

### 4.1 Per-implementation execution (run independently on each side)

1. Read the frozen fixture input; record its SHA-256.
2. Produce `canonical_bytes` through the implementation's RFC 8785 boundary.
3. Record `canonical_bytes` verbatim as hex, together with its length.
4. Record `SHA-256(canonical_bytes)`.
5. Record `SHA-256(0x00 || canonical_bytes)`, where `0x00` is a raw octet.
6. Emit an execution artifact carrying all of the above plus engine identity, engine version, repository, source commit and worktree-clean state.
7. Write the artifact **before** asserting anything, so a divergence is recorded as evidence rather than suppressed.

### 4.2 Cross-language equality gate

Given artifacts `A` (RI-PY) and `B` (RI-RS), the gate MUST evaluate all of:

| Check | Assertion |
|---|---|
| C1 | `A.canonical_bytes == B.canonical_bytes` (byte-for-byte) |
| C2 | `SHA-256(decode(A.canonical_bytes)) == A.sha256` — recomputed by the gate |
| C3 | `SHA-256(decode(B.canonical_bytes)) == B.sha256` — recomputed by the gate |
| C4 | `A.sha256 == B.sha256` |
| C5 | `SHA-256(0x00 \|\| decode(A.canonical_bytes)) == A.leaf_sha256` — recomputed by the gate |
| C6 | `SHA-256(0x00 \|\| decode(B.canonical_bytes)) == B.leaf_sha256` — recomputed by the gate |
| C7 | `A.leaf_sha256 == B.leaf_sha256` |
| C8 | `A` and `B` declare distinct implementations, repositories and engines |

C2, C3, C5 and C6 are independent recomputations by the gate. They are not optional: without them, a mutation applied consistently to both sides would pass C1, C4 and C7 undetected.

### 4.3 Profile discrimination

At least one fixture in the CONF-003 corpus MUST be **JCS-discriminating**: its RFC 8785 output MUST differ from the output of an ordinary sorted-JSON serializer
(`sort_keys`, no whitespace, no ASCII escaping) for the same object.

A corpus in which every fixture is JCS-degenerate verifies cross-implementation *agreement* only. It does not verify conformance to RFC 8785, because a non-conforming sorted-JSON serializer would pass every check in §4.2.

Discriminating properties include, at minimum: member ordering that depends on UTF-16 code units; ES6 number serialization (`1.0` → `1`, `-0` → `0`, exponent form); and non-ASCII strings emitted as raw UTF-8 rather than `\uXXXX` escapes.

### 4.4 Negative controls

The gate MUST be demonstrated to reject each of:

| Control | Mutation | MUST be caught by |
|---|---|---|
| N1 | One byte of one side's `canonical_bytes` altered | C1, C3, C6 |
| N2 | One side's recorded `sha256` corrupted | C2, C4 |
| N3 | Both leaves recomputed under domain `0x01` instead of `0x00` | C5, C6 (C7 still passes — this is the point) |

Mutations MUST be applied to temporary copies and MUST NOT remain in the committed corpus. Corpus digests MUST be re-verified after the controls run.

### 4.5 Prohibited-input controls

The implementation MUST NOT accept, as a digest input, any form listed in APS-200 §8.4. Where the boundary can be driven with such an input, the attempt MUST fail rather than produce a digest.

---

## 5. Expected Result

CONF-003 PASSES only when **all** of the following hold:

1. Each implementation independently produced its own `canonical_bytes`; neither derived them from the other or from a frozen constant.
2. C1–C8 all pass.
3. N1–N3 are all rejected by the gate.
4. At least one JCS-discriminating fixture (§4.3) passed C1–C7.
5. Both artifacts carry engine identity, engine version, source commit and clean-worktree state.
6. The frozen expected values, where present, are used only as a **secondary** cross-check. The primary gate is `RI-PY actual == RI-RS actual`.

Comparing two computed digests against a shared expected constant is **not** sufficient. Two implementations agreeing on a digest they both read from the same file demonstrates nothing.

---

## 6. Evidence Required

`EVID-CORE` containing, for each implementation: the fixture input digest, `canonical_bytes` (hex) and length, `SHA-256(canonical_bytes)`, `SHA-256(0x00 || canonical_bytes)`, engine identity and version, adapter digest, source repository and commit, toolchain and platform.

Plus: the gate's own output, the negative-control results, and a production-integrity statement declaring whether the canonicalization engine entered any production dependency graph.

---

## 7. PASS / FAIL Criteria

| Outcome | Condition |
|---------|-----------|
| PASS | All of §5 satisfied |
| PARTIAL | C1–C8 and N1–N3 pass, but the corpus contains no JCS-discriminating fixture (§4.3). Records cross-implementation agreement; does **not** record RFC 8785 conformance. Not a PASS. |
| FAIL | Any byte, digest or leaf mismatch; any negative control not rejected; any artifact lacking required provenance; any digest computed over a prohibited input |
| NOT APPLICABLE | Implementation exposes no JSON-representable protocol object (requires written justification) |
| ERROR | Test infrastructure failure — result not recorded |

---

## 8. Current execution status

| Item | Status | Source |
|---|---|---|
| CANONICAL-001, RI-PY actual execution | PASS | `rfc8785` 0.1.4 @ `49d0e4f6` |
| CANONICAL-001, RI-RS actual execution | PASS | `serde_json_canonicalizer` 0.3.2 @ `4e9e2284` |
| C1–C8 | PASS | CROSS-LANGUAGE-001 |
| N1–N3 | PASS (all rejected) | CROSS-LANGUAGE-001 |
| §4.3 profile discrimination, RI-PY only | PASS | `test_jcs_behavior.py`, 13 passed |
| §4.3 profile discrimination, cross-language | **NOT ESTABLISHED** | CANONICAL-001 is JCS-degenerate |
| §4.5 prohibited-input controls | NOT EXECUTED | — |

**CONF-003 verdict: PARTIAL.** See [`closures/DQ-006_CLOSURE_PACKAGE.md`](../closures/DQ-006_CLOSURE_PACKAGE.md).

---

## 9. Traceability

| Field | Value |
|-------|-------|
| Test ID | CONF-003 |
| Invariant | INV-003 (exercises INV-006, INV-011) |
| Normative source | APS-200 §8 · APS-300 §5 |
| Decision | ADR-CK003-DQ006 · DQ-006 |
| Fixture | CANONICAL-001 |
| Evidence Type | EVID-CORE |
| Closure record | `closures/DQ-006_CLOSURE_PACKAGE.md` |

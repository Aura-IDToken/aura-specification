# CONF-003 CANONICAL SERIALIZATION

Document ID: CONF-003
Version: 1.1-DRAFT
Status: DRAFT
Classification: Normative Conformance Test
Authority: APS-400 · APS-200 §8
Related Invariant: INV-003
Related Fixture: CANONICAL-001
Last Review: 2026-08-20

---

## 1. Purpose

Verify that an implementation reproduces the canonical bytes and digests defined
by the canonical serialization profile of APS-200 §8 (RFC 8785 / JCS), and that
the same value always canonicalizes to the same bytes.

---

## 2. Related APS

- APS-200 §8: the normative canonical serialization contract (authority)
- APS-100: INV-003
- APS-400 §4: CONF-003
- APS-300 §5.1: evidence digest byte domain
- APS-500: Reference Fixtures

---

## 3. Preconditions

- The implementation under test exposes an RFC 8785 canonicalization boundary and
  a SHA-256 primitive.
- The frozen fixture `fixtures/corpus/CANONICAL-001_jcs_evidence.json` is loaded.
- No prior state from a different test run exists.
- The implementation's canonicalization engine is recorded (name and version) as
  provenance. The engine identity is **not** a pass condition — see §9.

> **TODO (unchanged by CK-003):** per-entity preconditions for ENT-001…ENT-008
> remain pending the APS-200 §9 JSON Schema publication.

---

## 4. Test Procedure

**Part A — CANONICAL-001 (frozen vector, mandatory).**

1. Read `protocol_object` from the fixture. Do not reorder its members: RFC 8785
   ordering is the engine's responsibility, and a pre-sorted input would not
   exercise the ordering rule.
2. Canonicalize it with the implementation's RFC 8785 boundary and capture the
   raw output octets.
3. Compare those octets byte-for-byte against `canonical_bytes_hex`.
4. Compute `SHA-256(canonical_bytes)` over the octets produced in step 2 — not
   over the fixture's recorded hex — and compare against `canonical_sha256_hex`.
5. Compute `SHA-256(0x00 || canonical_bytes)` with `0x00` as a single raw octet,
   and compare against `merkle_leaf_hash_hex`.

**Part B — determinism.**

Canonicalize the same value twice in two fresh processes and compare the two
byte sequences.

**Part C — entity coverage.**

Serialize ENT-001 through ENT-008 objects twice independently (fresh process each
time). This part becomes fully executable when APS-200 §9 schemas and the APS-500
corpus are published; until then Part A and Part B are the executable core of
CONF-003.

**Negative controls (all MUST fail the gate).**

- Canonical bytes mutated in one octet.
- Expected SHA-256 mutated.
- Leaf computed with the interior domain `0x01` instead of `0x00`.
- Leaf computed with the ASCII text `"0x00"` instead of the raw octet.

---

## 5. Expected Result

Part A: all three comparisons MUST match exactly.

Part B: both serializations MUST be byte-identical.

Part C: both serializations MUST be byte-identical, and JSON Schema validation
against APS-200 schemas MUST pass for all objects.

A matching digest without matching canonical bytes MUST NOT be recorded as a
pass (APS-200 §8.7).

---

## 6. Evidence Required

EVID-CORE

---

## 7. PASS / FAIL Criteria

| Outcome | Condition |
|---------|-----------|
| PASS | Expected result achieved with no deviations |
| FAIL | Any required field missing, any hash mismatch, or any deviation from expected result |
| NOT APPLICABLE | Implementation does not support this feature (requires justification) |
| ERROR | Test infrastructure failure — result not recorded |

---

## 8. Traceability

| Field | Value |
|-------|-------|
| Test ID | CONF-003 |
| Invariant | INV-003 |
| Normative authority | APS-200 §8 |
| Related Fixture | CANONICAL-001 — `fixtures/corpus/CANONICAL-001_jcs_evidence.json` |
| Fixture self-check | `scripts/validate_canonical_001.py` |
| Implementation evidence | CROSS-LANGUAGE-001 (RI-PY, RI-RS) |
| Evidence Type | EVID-CORE |

---

## 9. Implementation independence

CONF-003 tests **behaviour and bytes**, not tooling. The requirement is the
behaviour APS-200 §8 defines. An implementation MUST NOT be failed for using any
particular RFC 8785 library, language, or package version, and MUST NOT be passed
merely for using the same engine as a reference implementation.

The reference engines — `rfc8785==0.1.4` (RI-PY) and
`serde_json_canonicalizer==0.3.2` (RI-RS) — are recorded as conformance
provenance. They are informative and are not part of the protocol contract
(APS-200 §8.7).

## 10. Scope note

CANONICAL-001 is a serialization-profile vector over the JSON data model
(APS-200 §8.2). Passing CONF-003 establishes canonicalization and digest-domain
conformance only. It does not establish that the fixture's `event_type` is a
registered token, that the object satisfies the APS-200 §4 common object
contract, or that any entity-level invariant holds; those are CONF-012, CONF-008
and the APS-200 entity model respectively.

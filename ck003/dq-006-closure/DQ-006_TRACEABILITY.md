# DQ-006 — Traceability

**Classification:** TRACEABILITY
**Status of record:** DQ-006 = **CLOSED** — authority: [`closures/DQ-006_CLOSURE_PACKAGE.md`](../../closures/DQ-006_CLOSURE_PACKAGE.md)
**Integrated:** 2026-08-20

Every link below is identified by repository path plus section, test or document
identifier. Only references that actually exist are listed; no section number is
invented.

---

## 1. Decision chain

```text
DQ-006  — canonical serialization decision
  │
  ├─ NORMATIVE CONTRACT
  │    APS-200 §8      aps/APS-200_CANONICAL_DATA_MODEL.md
  │      §8.2  RFC 8785 JCS -> UTF-8 canonical_bytes   (sole authority)
  │      §8.3  properties fixed by the profile
  │      §8.4  prohibited digest inputs
  │      §8.5  SHA-256(B) / SHA-256(0x00||B) / SHA-256(0x01||l||r)
  │      §8.6  cross-implementation byte identity
  │      §8.7  scope boundary — not event, version or identity semantics
  │      §8.8  compatibility and migration
  │    APS-300 §5      aps/APS-300_EVIDENCE_MODEL.md
  │      §5.1  evidence_hash bound to APS-200 §8 canonical bytes
  │      §5.2  domain separation
  │      §5.3  migration
  │    APS-001 §7.1    specification/APS-001_PROTOCOL_SPECIFICATION.md
  │      hash-domain model owner; states the serialization profile is owned by APS-200
  │
  ├─ INVARIANT
  │    INV-003         invariants/INVARIANT_REGISTRY.md · aps/APS-100_PROTOCOL_INVARIANTS.md
  │
  ├─ DECISION RECORD
  │    ADR-CK003-DQ006 ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md
  │      §2  normative contract vs conformance implementation detail
  │
  ├─ CONFORMANCE REQUIREMENT
  │    CONF-003        conformance/CONF-003_CANONICAL_SERIALIZATION.md
  │      §4.2  cross-language equality gate, checks C1-C8
  │      §4.3  profile discrimination requirement
  │      §4.4  negative controls N1-N3
  │    APS-400 §4      aps/APS-400_CONFORMANCE_TEST_MATRIX.md
  │
  └─ EVIDENCE
       ck003/dq-006-closure/DQ-006_EVIDENCE.md
       closures/DQ-006_CLOSURE_PACKAGE.md          (closure authority)
```

---

## 2. Evidence chain

```text
CANONICAL-001                                    CANONICAL-002
fixtures/corpus/CANONICAL-001_jcs_evidence.json  fixtures/corpus/CANONICAL-002_jcs_evidence.json
  │  100 bytes · JCS-degenerate                    │  655 bytes · JCS-discriminating
  │                                                │
  ├─ RI-PY  rfc8785 0.1.4                          ├─ RI-PY  rfc8785 0.1.4
  │    aura-poc-a-core-v3.3 @ 49d0e4f6             │    aura-poc-a-core-v3.3 @ 7bcc600f
  │    conformance/canonical/jcs.py                │    conformance/canonical/jcs.py
  │    corpus/canonical-001/ri-py.json             │    corpus/canonical-002/ri-py.json
  │                                                │
  ├─ RI-RS  serde_json_canonicalizer 0.3.2         ├─ RI-RS  serde_json_canonicalizer 0.3.2
  │    aura-guard-v1.3 @ 4e9e2284                  │    aura-guard-v1.3 @ bd4a2fa6
  │    conformance/canonical/jcs.rs                │    conformance/canonical/jcs.rs
  │    corpus/canonical-001/ri-rs.json             │    corpus/canonical-002/ri-rs.json
  │                                                │
  ▼                                                ▼
CROSS-LANGUAGE-001                               CROSS-LANGUAGE-CANONICAL-002
test_cross_language_canonical_001.py             test_cross_language_canonical_002.py
negative_controls_canonical_001.py               negative_controls_canonical_002.py
  │                                                │
  ├─ canonical bytes equality      PASS            ├─ canonical bytes equality      PASS
  ├─ SHA-256 equality              PASS            ├─ SHA-256 equality              PASS
  ├─ RFC-6962 leaf equality        PASS            ├─ RFC-6962 leaf equality        PASS
  ├─ independent recomputation     PASS            ├─ independent recomputation     PASS
  ├─ negative controls A/B/C       PASS            ├─ negative controls A/B/C/D     PASS
  └─ profile discrimination        NOT PROVIDED    └─ profile discrimination        PASS
  │                                                │
  └────────────────────┬───────────────────────────┘
                       ▼
                canonical_bytes
                       ▼
              SHA-256(canonical_bytes)
                       ▼
           SHA-256(0x00 || canonical_bytes)
                       ▼
                 DQ-006 = CLOSED
       closures/DQ-006_CLOSURE_PACKAGE.md
```

---

## 3. Link table

| From | To | Path / identifier | State |
|---|---|---|---|
| DQ-006 | canonical serialization contract | `aps/APS-200_CANONICAL_DATA_MODEL.md` §8 | PASS |
| DQ-006 | RFC 8785 | APS-200 §8.2 | PASS |
| DQ-006 | evidence-hash byte domain | `aps/APS-300_EVIDENCE_MODEL.md` §5.1 | PASS |
| DQ-006 | hash-domain model | `specification/APS-001_PROTOCOL_SPECIFICATION.md` §7.1 | PASS |
| DQ-006 | INV-003 | `invariants/INVARIANT_REGISTRY.md` | PASS |
| DQ-006 | decision record | `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | PASS |
| DQ-006 | conformance requirement | `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | PASS |
| DQ-006 | CANONICAL-001 | `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | PASS |
| DQ-006 | CANONICAL-002 | `fixtures/corpus/CANONICAL-002_jcs_evidence.json` | PASS |
| DQ-006 | RI-PY | `Aura-IDToken/aura-poc-a-core-v3.3` @ `49d0e4f6`, `7bcc600f` | PASS |
| DQ-006 | RI-RS | `Aura-IDToken/aura-guard-v1.3` @ `4e9e2284`, `bd4a2fa6` | PASS |
| DQ-006 | CROSS-LANGUAGE-001 | `ck003/dq-006-closure/CROSS-LANGUAGE-001-EVIDENCE.md` | PASS |
| DQ-006 | CROSS-LANGUAGE-CANONICAL-002 | `ck003/dq-006-closure/DQ-006_EVIDENCE.md` §2.2 | PASS |
| DQ-006 | closure record | `closures/DQ-006_CLOSURE_PACKAGE.md` | PASS |
| DQ-006 | reference implementations | `reference/RI-PY_AURA_POC_A_CORE.md`, `reference/RI-RS_AURA_GUARD.md` | PASS |

---

## 4. Adjacent decisions — status preserved, not changed

| Decision | Relationship to DQ-006 | Action taken here |
|---|---|---|
| **DQ-002** — hash domain | `closures/DQ-002_FINAL_CLOSURE.md` records CLOSED / PASS on the stated basis that DQ-006 is PASS. That dependency is now satisfied, and the evidentiary weakness it inherited (CANONICAL-001 degeneracy) is repaired by CANONICAL-002. | **Status unchanged.** DQ-002 was already CLOSED; no status transition was performed, and no new architectural decision about DQ-002 was made. Recorded as *dependency satisfied*. |
| **DQ-003** — version semantics | APS-200 §8.7 excludes version semantics from the canonicalization profile. `protocol_version` and `schema_version` remain distinct, unrenamed, unmerged. | **No change.** No reopening, no semantic change. |
| **DQ-004** — event-type semantics | APS-200 §8.7 excludes event semantics. The Event-Type Registry §7 defers to APS-200 for canonical representation. Both fixtures carry `event_type: "AUDIT_RECORD"`, which the registry does not register — CFL-005, unresolved and owned by DQ-004. | **No change.** Reported, not repaired. |
| **CROSS-LANGUAGE-002** (Merkle) | Distinct gate over the DQ-002 Merkle contract; status OPEN / CONDITIONAL PASS. Shares an identifier with the RI-side name for the CANONICAL-002 gate. | **No change to its status.** The specification disambiguates by using `CROSS-LANGUAGE-CANONICAL-002` for the canonicalization gate. |

---

## 5. Cross-language conformance invariant

The invariant DQ-006 closure preserves, for any protocol object subject to
canonical serialization:

```text
RI-PY canonical_bytes == RI-RS canonical_bytes
        ⇒  SHA-256(RI-PY canonical_bytes) == SHA-256(RI-RS canonical_bytes)
        ⇒  SHA-256(0x00 || RI-PY canonical_bytes) == SHA-256(0x00 || RI-RS canonical_bytes)
```

Verified by execution on CANONICAL-001 and CANONICAL-002. Normatively required
by APS-200 §8.6; verified by CONF-003.

No alternate canonical representation is introduced by this closure. `0x00` is a
raw octet, never the ASCII text `"0x00"`.

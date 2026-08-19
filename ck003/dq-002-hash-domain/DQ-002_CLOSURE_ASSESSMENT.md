# DQ-002 Closure Assessment

Document ID: DQ-002-ASSESSMENT-001
Classification: `DECISION` / `WORKING`
Assessment date: 2026-08-19
Authority: DQ-002 / APS-200 / APS-300 / APS-500 / ADR-CK003-DQ002

> **This is an assessment, not a closure record.** DQ-002 is **not** closed by this
> document. A DQ-002 closure record must not be created until every mandatory
> acceptance criterion below is `PASS`.

---

## 1. Verdict

**DQ-002 = BLOCKED.**

The blocker is primarily an **unresolved architectural decision**, which in turn gates
the missing execution evidence:

1. `ADR-CK003-DQ002 — Normative Hash Domain for Merkle Evidence` has status
   **PROPOSED — awaiting Chief Architect approval**. No approval record exists in this
   repository.
2. RI-PY does **not** implement the proposed contract, so the cross-language gate
   cannot be executed until remediation follows an approved decision.

DQ-002 therefore cannot be closed on the currently available evidence, and no
closure record has been written.

---

## 2. Scope of DQ-002

DQ-002 is the **cross-language Merkle hash-domain decision**: the leaf domain, the
interior-node domain, the byte-vs-hex input rule, the tree shape for odd node counts,
empty-tree semantics, and the requirement that every conformant implementation pass
the same byte-level fixtures.

DQ-002 is **not** the canonical serialization decision. Canonicalization is DQ-006.

---

## 3. Relationship to DQ-006

DQ-006 is a genuine, verified evidence input to DQ-002, but a **partial** one.

CROSS-LANGUAGE-001 independently demonstrated, for `CANONICAL-001`, that RI-PY and
RI-RS produce identical `SHA-256(0x00 || canonical_bytes)`. That is the **RFC-6962
leaf domain**, cross-language verified. Its formal closure package exists at
`evidence/DQ-006_CLOSURE_PACKAGE.md` and its contents and traceability were verified
during this assessment.

What CROSS-LANGUAGE-001 does **not** establish, and what DQ-002 additionally requires:

- the interior-node domain `SHA-256(0x01 || L || R)`;
- Merkle root equality;
- the RFC 6962 recursive tree shape and odd-node promotion rule;
- inclusion-proof generation and verification;
- Merkle-specific negative controls.

DQ-006 closure is therefore **necessary but not sufficient** for DQ-002. The gate that
would supply the remainder is `CROSS-LANGUAGE-002`, which is **OPEN**.

---

## 4. Acceptance Matrix

Statuses: `PASS` · `FAIL` · `BLOCKED` · `UNRESOLVED` · `N/A`.

Criteria are derived from the ADR's own conformance gate and from the
`CROSS-LANGUAGE-002` closure criteria.

| ID | Requirement | Evidence | Evidence location | Implementation | Test | Result | Status |
|---|---|---|---|---|---|---|---|
| DQ2-A01 | Leaf domain `SHA-256(0x00 \|\| leaf_bytes)` is normatively defined | Drafted in a PROPOSED ADR | `ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` | — | — | Defined, no normative standing | UNRESOLVED |
| DQ2-A02 | Interior-node domain `SHA-256(0x01 \|\| L \|\| R)` is normatively defined | Drafted in a PROPOSED ADR | same | — | — | Defined, no normative standing | UNRESOLVED |
| DQ2-A03 | Hash inputs are raw bytes, never hexadecimal digest text | Drafted in a PROPOSED ADR | same | — | — | Defined, no normative standing | UNRESOLVED |
| DQ2-A04 | RFC 6962 tree shape; lone node promoted, last node not duplicated | Drafted in a PROPOSED ADR | same | — | — | Defined, no normative standing | UNRESOLVED |
| DQ2-A05 | Empty-tree semantics explicitly specified | ADR requires it; no APS text specifies it | APS-200 / APS-300 | RI-RS has `empty_root` | — | Not specified normatively | UNRESOLVED |
| DQ2-A06 | Chief Architect approval of the hash-domain ADR is recorded | None found | — | — | — | No approval record | UNRESOLVED |
| DQ2-A07 | APS-200 §8 updated with the canonical byte-level rule | APS-200 §8 still reads TODO | `aps/APS-200_CANONICAL_DATA_MODEL.md` §8 | — | — | Normative gap open | UNRESOLVED |
| DQ2-A08 | APS-300 `evidence_hash` scope reconciled with canonical bytes | APS-300 §5 still reads TODO | `aps/APS-300_EVIDENCE_MODEL.md` §5 | — | — | Normative gap open | UNRESOLVED |
| DQ2-A09 | Fixture promoted from proposal to normative fixture | Fixture `status: PROPOSED`; APS-500 fixtures TODO | `ck003/dq-002-hash-domain/fixtures/FIX-CK003-DQ002-RFC6962-2LEAF.json`; `aps/APS-500_REFERENCE_FIXTURES.md` | — | — | Still proposed | UNRESOLVED |
| DQ2-A10 | RI-PY implements the approved contract | Source verified non-conformant | `aura-poc-a-core-v3.3` `audit/merkle.py`, blob `c0db98fbfb01eaf558c25d05e3696e78c3e5ffd5` | RI-PY | source review + execution | No `0x00` leaf prefix; node = `SHA-256(UTF-8(left_hex + right_hex))`; last node duplicated | FAIL |
| DQ2-A11 | RI-RS implements the approved contract | Source verified conformant | `aura-guard-v1.3` `src/merkle.rs`, blob `658d5b51e14830b03be8a4248ac06ca9731578ae` | RI-RS | source review | `0x00` leaf prefix, `0x01` node prefix, raw digest bytes, recursive split | PASS (source inspection only) |
| DQ2-A12 | RI-PY independent execution of the fixture | Divergent root recorded as negative preflight | `ck003/cross-language-002/CROSS-LANGUAGE-002-EVIDENCE.md` §4 | RI-PY | two-leaf execution | root `fb8e20fc…620603` ≠ `b137985f…7999eb` | FAIL |
| DQ2-A13 | RI-RS independent execution of the fixture | Never run | `ck003/cross-language-002/cross-language-002-manifest.json` (`ri_rs_execution: NOT_RUN`) | RI-RS | — | No execution artifact | BLOCKED |
| DQ2-A14 | Cross-language leaf / node / root equality | Not established | `CROSS-LANGUAGE-002-EVIDENCE.md` §5 | both | CROSS-LANGUAGE-002 | Gate OPEN | BLOCKED |
| DQ2-A15 | Inclusion proofs verify cross-language | Not established | same | both | CROSS-LANGUAGE-002 | Gate OPEN | BLOCKED |
| DQ2-A16 | Merkle negative controls (wrong leaf, wrong node domain, mutated root) reject | Not established cross-language | same | both | CROSS-LANGUAGE-002 | Gate OPEN | BLOCKED |
| DQ2-A17 | Execution/source commit provenance recorded for both implementations | Ledger incomplete | same | both | — | No execution provenance | BLOCKED |
| DQ2-A18 | Migration / version semantics for legacy Merkle evidence documented | ADR states the requirement; no versioned rule exists | ADR "Compatibility and migration rule"; DQ-003 `OPEN` | — | — | Not documented | UNRESOLVED |

**Mandatory criteria at `PASS`: 0 of 18** (DQ2-A11 is a source-inspection result only and
does not constitute execution evidence).

---

## 5. Independent verification performed for this assessment

The following were recomputed or re-read from primary sources rather than taken from
the existing evidence documents.

| Check | Result |
|---|---|
| RFC 6962 fixture leaf A, leaf B and root recomputed from the byte-domain formulas | Reproduces `022a6979…24f93c`, `57eb3561…7b6a31`, `b137985f…7999eb` — fixture values confirmed |
| RI-PY negative preflight root `fb8e20fc…620603` | Reproduces as `SHA-256(UTF-8("a" + "b"))`, i.e. the RI-PY node domain over two pre-hashed leaves — recorded value confirmed |
| RI-PY `audit/merkle.py` blob SHA at `origin/main` | `c0db98fbfb01eaf558c25d05e3696e78c3e5ffd5` — matches `HASH_DOMAIN_EVIDENCE.md`; implementation unchanged and still non-conformant |
| RI-RS `src/merkle.rs` blob SHA at `origin/main` | `658d5b51e14830b03be8a4248ac06ca9731578ae` — matches `HASH_DOMAIN_EVIDENCE.md`; `leaf_hash`/`node_hash` confirmed RFC 6962 |
| RI-RS hash-domain fixtures HD-005 / HD-006 / HD-007 | Self-declared `AS-IS IMPLEMENTATION BYTES` with the note "DQ-002 and DQ-006 unresolved; these bytes carry no specification standing" — corroborates the open state and is not cross-language evidence |
| DQ-006 closure package existence and traceability | Present at `evidence/DQ-006_CLOSURE_PACKAGE.md`; contents verified |

---

## 6. Traceability chain — as far as it currently reaches

```text
DQ-002
  ↓
APS-200 §4 integrity_hash / §8 canonical serialization  ......... TODO (open)
APS-300 §5 evidence_hash algorithm ............................. TODO (open)
  ↓
ADR-CK003-DQ002 normative Merkle hash domain ................... PROPOSED (not approved)
  ↓
INV-003 / INV-006 / INV-011 / INV-014 → CONF-010 ............... OPEN
  ↓
FIX-CK003-DQ002-RFC6962-2LEAF .................................. PROPOSED (values independently verified)
  ↓
RI-PY evidence ................................................. FAIL (legacy domain)
RI-RS evidence ................................................. NOT RUN
  ↓
CROSS-LANGUAGE-002 ............................................. OPEN
  ↓
DQ-002 ......................................................... BLOCKED
```

The canonical-serialization branch of the chain, which DQ-002 depends on but does not
own, reaches PASS only for the leaf boundary:

```text
DQ-006 → JCS/RFC 8785 → CANONICAL-001 → RI-PY → RI-RS → CROSS-LANGUAGE-001 → PASS
```

---

## 7. Open issues

1. **ADR-CK003-DQ002 is not approved.** No Chief Architect approval record exists.
2. **APS-200 §8 canonical byte-level rule is TODO.**
3. **APS-300 §5 `evidence_hash` algorithm is TODO.**
4. **APS-500 canonical fixtures are TODO;** `FIX-CK003-DQ002-RFC6962-2LEAF` is `PROPOSED`.
5. **RI-PY Merkle implementation is non-conformant** to the proposed contract on three
   independent points: leaf domain, node domain, and odd-node handling.
6. **RI-RS has never executed the fixture;** only source inspection exists.
7. **CROSS-LANGUAGE-002 is OPEN:** no root equality, no proof verification, no Merkle
   negative controls, incomplete provenance ledger.
8. **Empty-tree semantics are not normatively specified.**
9. **Migration/version semantics for legacy Merkle evidence are not documented;**
   DQ-003 is `OPEN`.
10. **DQ-004 event-type semantics are `OPEN`** (`BLOCKED FOR FINAL CLOSURE`). Tracked
    separately from DQ-002, and recorded here because it is a mandatory checkbox of the
    DQ-002 final-closure order.

---

## 8. Minimum action required to unblock

In order:

1. Chief Architect approves `ADR-CK003-DQ002` (or directs an alternative hash domain).
2. Amend APS-200 §8 and reconcile APS-300 §5 to the approved byte domain.
3. Promote `FIX-CK003-DQ002-RFC6962-2LEAF` to a normative APS-500 fixture and specify
   empty-tree semantics.
4. Remediate RI-PY `audit/merkle.py` to the approved contract, under an explicit
   migration/version boundary so existing evidence keeps its original algorithm identity.
5. Execute the fixture independently in RI-PY and RI-RS; record execution and source
   commit provenance for both.
6. Run `CROSS-LANGUAGE-002`: leaf, node and root equality with independent
   recomputation, both inclusion proofs, and the wrong-leaf / wrong-node-domain /
   mutated-root negative controls.
7. Only then create the DQ-002 closure record.

Steps 4–6 are production-affecting for RI-PY and are **not** authorized by this
assessment.

---

## 9. Production integrity

No production runtime was inspected destructively and none was modified by this
assessment. `aura-poc-a-core-v3.3` and `aura-guard-v1.3` were read only.

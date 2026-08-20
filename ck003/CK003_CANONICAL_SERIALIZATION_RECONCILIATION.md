# CK-003 — Canonical Serialization Normative Reconciliation

**Classification:** TRACEABILITY / DECISION RECORD — this document reconciles and
indexes. It defines nothing.
**Normative authority:** `aps/APS-200_CANONICAL_DATA_MODEL.md` §8.
**Date:** 2026-08-20
**Scope:** specification corpus (`Aura-IDToken/aura-specification`) only.

---

## 1. What changed

Before CK-003, the canonical serialization profile existed in the repository
**four times and nowhere**:

- `APS-200 §8` — the document INV-003 designates as the authority — said
  *"TODO: Define the canonical serialization format"*.
- `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-…` proposed RFC 8785,
  status PROPOSED.
- `ck003/dq-006-canonical-serialization/APS-200-SECTION-8-PROPOSED.md` drafted the
  amendment, status "PROPOSED — not yet frozen".
- `closures/DQ-002_FINAL_CLOSURE.md` and `ck003/DQ-006_CLOSURE.md` asserted the
  profile was **frozen** and closed the gates on that basis.

A closed gate rested on an amendment that had never been made. CK-003 makes the
amendment: APS-200 §8 now carries the contract, and every other statement is
subordinated to it or marked superseded.

---

## 2. The fourteen questions

APS-200 §8 answers each of these exactly once.

| # | Question | Answer | Where |
|---|---|---|---|
| 1 | Canonical serialization format | JSON, canonicalized | §8.1 |
| 2 | Governing RFC / profile | RFC 8785 (JCS) | §8.1 |
| 3 | Exact byte representation | UTF-8 octets of the RFC 8785 output, unmodified | §8.1 |
| 4 | Character encoding | UTF-8; no BOM; no other encoding | §8.1 |
| 5 | Object member ordering | Delegated to RFC 8785 §3.2.3 | §8.3 |
| 6 | String escaping | Delegated to RFC 8785 §3.2.2.2 | §8.3 |
| 7 | Number representation | Delegated to RFC 8785 §3.2.2.3 | §8.3 |
| 8 | Unicode normalization | **None.** Never applied, before or after | §8.3 |
| 9 | Input domain | The JSON data model (RFC 8259 as constrained by RFC 8785 §3) | §8.2 |
| 10 | Bytes entering SHA-256 | `canonical_bytes`, and nothing else | §8.4 |
| 11 | Bytes entering the RFC-6962 leaf | `0x00 \|\| canonical_bytes`, `0x00` a raw octet | §8.4 |
| 12 | Version binding | `protocol_version`; not independently versioned | §8.6 |
| 13 | Implementation details that are evidence only | Engine identity and version (`rfc8785==0.1.4`, `serde_json_canonicalizer==0.3.2`) | §8.7 |
| 14 | Normative vs informative | §8 normative; engines, fixtures' provenance blocks and all `ck003/` material informative | §8, and §6 below |

---

## 3. Reconciliation matrix

| Item | Current specification (before CK-003) | Existing CK-003 evidence | Current implementation evidence | Normative decision | Status | Required action |
|---|---|---|---|---|---|---|
| Serialization format | APS-200 §8: "MAY use JSON, CBOR, Protocol Buffers"; format TODO | ADR proposed JCS (PROPOSED) | RI-PY and RI-RS both emit JCS JSON | JSON canonicalized per RFC 8785; alternates are transport only (§8.5) | **RECONCILED** | Done — APS-200 §8.1, §8.5 |
| RFC / profile | Not stated | RFC 8785 proposed | `rfc8785` 0.1.4 / `serde_json_canonicalizer` 0.3.2 | RFC 8785 (JCS) | **RECONCILED** | Done — §8.1 |
| Encoding | Not stated | UTF-8 proposed | UTF-8 in both engines | UTF-8, no BOM, no trailing newline | **RECONCILED** | Done — §8.1 |
| Object ordering | "Deterministic where required" | Delegation proposed | Engine-enforced | Delegated to RFC 8785 §3.2.3; ad-hoc sorting prohibited | **RECONCILED** | Done — §8.3 |
| Number formatting | Not stated | "obey RFC 8785"; no NaN/Infinity | Engine-enforced | Delegated to RFC 8785 §3.2.2.3; non-JSON numerics fail closed | **RECONCILED** | Done — §8.3 |
| String escaping | Not stated | "JCS/JSON UTF-8 representation" | Engine-enforced | Delegated to RFC 8785 §3.2.2.2 | **RECONCILED** | Done — §8.3 |
| Unicode handling | Not stated anywhere | Not addressed | Not addressed | **No normalization.** Explicitly prohibited | **RECONCILED (gap closed)** | Done — §8.3 |
| Input domain | Not stated; ADR said "validated protocol object" | Ambiguous — see §4 below | Both engines take a parsed JSON value | JSON data model; canonicalization total over it; validation ordering stated separately | **RECONCILED (gap closed)** | Done — §8.2 |
| Canonical bytes | Concept referenced by APS-001 §7, undefined | CANONICAL-001 hex recorded | Reproduced by both engines 2026-08-20 | `UTF-8(RFC8785(value))` | **RECONCILED** | Done — §8.1 |
| SHA domain | APS-001 §7 required "canonical bytes" | DQ-002 ADR | Both engines | `SHA-256(canonical_bytes)` | **RECONCILED** | Done — §8.4 |
| Leaf domain | APS-001 §7.1 `SHA-256(0x00 \|\| bytes)` | DQ-002 closure | Both engines; RI-RS asserts the raw octet | Unchanged; §8.4 states which bytes enter it | **CONSISTENT — no change** | None |
| Interior node domain | APS-001 §7.1 `SHA-256(0x01 \|\| l \|\| r)` | DQ-002 closure | RI-RS `src/merkle.rs` | Unchanged; owned by APS-001 §7 / DQ-002 | **OUT OF SCOPE — untouched** | None |
| `protocol_version` | APS-001 §12 semantics | DQ-003 snapshot (OPEN) | Carried in fixture | Binds the canonicalization profile | **RECONCILED** | Done — §8.6 |
| `schema_version` | APS-001 §12 semantics | DQ-003 snapshot (OPEN) | Carried in fixture | Does **not** select a profile | **RECONCILED** | Done — §8.6 |
| `evidence_hash` byte domain | APS-300 §5: TODO | APS-300-RECONCILIATION (PROPOSED) | — | Canonical bytes per APS-200 §8 | **RECONCILED** | Done — APS-300 §5.1 |
| `integrity_hash` byte domain | APS-200 §4: "canonical serialization", undefined | Not addressed | — | Canonical bytes per §8 | **RECONCILED (byte domain only)** | Done — APS-200 §4 note |
| Self-hash member exclusion | Not stated | Not addressed | — | **Not decided by CK-003** | **OPEN** | APS-200/APS-300 entity-model decision |
| CANONICAL-001 | Fixture existed, marked `PENDING_EXECUTION` | Values recorded in five places | PASS in both engines | Frozen normative fixture | **FROZEN** | Done — see §5 |
| RI-PY evidence | Cited by closures | Commits cited | Re-executed 2026-08-20: 27 tests PASS | Informative provenance | **VERIFIED (with provenance gap)** | See §7 |
| RI-RS evidence | Cited by closures | Commits cited | Re-executed 2026-08-20: 5 tests PASS on default branch | Informative provenance | **VERIFIED (with provenance gap)** | See §7 |
| CROSS-LANGUAGE-001 | Recorded PASS | Equality runner + negative controls | Equality gate re-run in RI-PY suite | Byte, SHA and leaf equality | **VERIFIED** | None |
| Legacy CK003-001…010 | Manifest placeholders, `expected_digest: null` | No artifact in any commit | None | Not normative fixtures | **UNRESOLVED** | See §4 and the legacy register |
| Stale "BLOCKED"/"PROPOSED" artifacts | Contradicted the closures | Five documents | — | Superseded by APS-200 §8 | **SUPERSEDED** | Done — §6 |

---

## 4. CK003-001…010

A full-history search (`git rev-list --all` × `git grep`) finds these identifiers
in exactly two kinds of file: the two `fixtures/ck003/` manifests that list them
as placeholders, and the reconciliation documents that record them as missing. No
commit in this repository has ever contained a CK003-001…010 fixture, input,
expected digest, or execution record.

| ID | Status | Evidence | Decision | Action |
|---|---|---|---|---|
| CK003-001 | **UNRESOLVED** | Identifier only; `expected_digest: null` | Not a normative fixture | Retain placeholder; recover or retire |
| CK003-002 | **UNRESOLVED** | Identifier only | Not a normative fixture | As above |
| CK003-003 | **UNRESOLVED** | Identifier only | Not a normative fixture | As above |
| CK003-004 | **UNRESOLVED** | Identifier only | Not a normative fixture | As above |
| CK003-005 | **UNRESOLVED** | Identifier only | Not a normative fixture | As above |
| CK003-006 | **UNRESOLVED** | Identifier only | Not a normative fixture | As above |
| CK003-007 | **UNRESOLVED** | Identifier only | Not a normative fixture | As above |
| CK003-008 | **UNRESOLVED** | Identifier only | Not a normative fixture | As above |
| CK003-009 | **UNRESOLVED** | Identifier only | Not a normative fixture | As above |
| CK003-010 | **UNRESOLVED** | Identifier only | Not a normative fixture | As above |

None is marked SUPERSEDED: supersession requires content that conflicts with the
frozen profile, and there is no content. None is marked VERIFIED: there is no
execution evidence to verify. None is deleted — the identifiers are retained so
that a later recovery has somewhere to land.

Recovery conditions are unchanged and are recorded in
`ck003/legacy/CK003_EVIDENCE_RECONCILIATION.md`. `UNRESOLVED` entries MUST NOT
participate in any PASS calculation.

---

## 5. CANONICAL-001 — frozen

**Normative fixture:** `fixtures/corpus/CANONICAL-001_jcs_evidence.json`
**Status:** FROZEN
**Verified by:** CONF-003; self-checked by `scripts/validate_canonical_001.py`

Input:

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

Canonical bytes (100 octets):

```text
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
```

`SHA-256(canonical_bytes)`:

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

`SHA-256(0x00 || canonical_bytes)`:

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

These are execution evidence, reproduced from both engines on 2026-08-20
(`ck003/dq-006-canonical-serialization/CK003_EXECUTION_EVIDENCE.md`). They are not
illustrative examples. Changing any of them is a `protocol_version` event under
APS-200 §8.6, not a fixture correction.

**Scope of the fixture.** CANONICAL-001 is a serialization-profile vector over the
JSON data model (APS-200 §8.2). Its object does not carry the APS-200 §4 common
object fields and is not an ENT-001…ENT-008 instance. It proves canonicalization
and digest-domain behaviour, and nothing about entity admissibility.

---

## 6. Normative / informative boundary

**NORMATIVE — defines the protocol:**

| Artifact | Role |
|---|---|
| `aps/APS-200_CANONICAL_DATA_MODEL.md` §8 | The canonicalization contract. Sole authority. |
| `aps/APS-200_CANONICAL_DATA_MODEL.md` §4 (byte-domain note) | Binds `integrity_hash` to canonical bytes |
| `aps/APS-300_EVIDENCE_MODEL.md` §5.1 | Binds Evidence digests to canonical bytes; domain separation |
| `aps/APS-100_PROTOCOL_INVARIANTS.md` INV-003 | Invariant, pointing at APS-200 §8 |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | Normative conformance test |
| `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | Frozen conformance vector |
| `specification/APS-001_PROTOCOL_SPECIFICATION.md` §7 | Hash/Merkle domain (pre-existing, unchanged) |

**INFORMATIVE — explains, evidences, or records:**

| Artifact | Role |
|---|---|
| `rfc8785==0.1.4`, `serde_json_canonicalizer==0.3.2` | Conformance provenance. **Not** part of the wire contract. |
| `ck003/**` (this file included) | Decision, evidence and traceability material |
| `closures/**`, `evidence/**` | Gate closure records |
| The `implementation_evidence` block of CANONICAL-001 | Provenance |
| `scripts/*.py` | Test tooling |

The package versions are the sharpest edge here. An implementation using a
different RFC 8785 library that produces the same bytes is conformant; an
implementation using `rfc8785==0.1.4` that produces different bytes is not.
APS-200 §8.7 states this directly.

---

## 7. Traceability

```text
INV-003  (APS-100)
   │
   ▼
APS-200 §8            ← the normative rule
   │
   ├── APS-300 §5.1   ← evidence digest byte domain
   ├── APS-001 §7     ← hash / Merkle domain (unchanged)
   │
   ▼
CONF-003              ← the conformance test
   │
   ▼
CANONICAL-001         ← the frozen fixture
   │
   ├── RI-PY   rfc8785 0.1.4                  → PASS
   ├── RI-RS   serde_json_canonicalizer 0.3.2 → PASS
   │
   ▼
CROSS-LANGUAGE-001    ← byte / SHA / leaf equality → PASS
```

| Gate | State after CK-003 |
|---|---|
| DQ-002 (hash domain) | Already CLOSED — `closures/DQ-002_FINAL_CLOSURE.md`. **Not reopened, not re-closed by CK-003.** Its byte domain now has the normative definition it referenced. |
| DQ-006 (canonical serialization) | Already CLOSED — `ck003/DQ-006_CLOSURE.md`. CK-003 supplies the normative amendment the closure presupposed. |
| DQ-003 (version semantics) | OPEN. §8.6 binds the profile using the existing APS-001 §12 semantics; it introduces no new versioning scheme and does not close DQ-003. |
| DQ-004 (event-type semantics) | OPEN. Untouched. |

**CK-003 READY FOR DQ-006 / DQ-002 FORMAL CLOSURE CONFIRMATION.** Both gates were
already recorded CLOSED before this task; CK-003 does not alter either status.

---

## 8. Conflicts — reported, not reconciled

`ck003/handover-assessment/04_CONFLICT_REGISTER.md` records five conflicts routed
to the Protocol Custodian. CK-003 resolves none of them. Their disposition:

### CFL-001 — cross-corpus authority on canonical encoding — **OPEN, narrowed**

The register frames this as two corpora making "incompatible" statements about
canonical encoding. Reading the implementation-corpus artifact
(`aura-poc-a-core-v3.3/review/2026-08-14_P0_6_D3_D4_DECISION_RECORD/`) closely,
it does not assert a competing encoding. It asserts that *it* establishes none,
and — §5 — that no value may be **derived** from implementation behaviour, RI-PY,
ADR-0001, code comments, or agent judgement.

APS-200 §8 derives nothing from any of those. It is a specification decision in
the specification corpus, made under GOVERNANCE.md §5.2, and it cites the D-3
record as authority for nothing. The two texts are therefore not in logical
contradiction.

That narrows CFL-001; it does not close it. The live question — *whether an
approved `aura-specification` APS binds the implementation corpus, and which
governance ladder rules a cross-corpus protocol-semantics decision* — is
untouched and remains with the Protocol Custodian. **CK-003 binds the
specification corpus only.**

### CFL-002 — DQ-006 carried three contradictory statuses — **RESOLVED by classification**

This is the one conflict inside CK-003's mandate, and §13 of the execution order
directs exactly this treatment. The two stale artifacts asserting BLOCKED /
PENDING_EXECUTION and the two PROPOSED amendment drafts are marked SUPERSEDED
with reasons (§9 below), and the fixture's stale `PENDING_EXECUTION` flags are
replaced with the executed result. The governing ADR is updated to point at the
enacted APS-200 §8. One status now stands.

### CFL-003 — three incompatible RI-RS implementations — **OPEN, partially overtaken**

PR #58 has since merged into `aura-guard-v1.3` `main` at `35082d7`, with the JCS
engine in `[dev-dependencies]` — the production-isolation constraint holds. The
closure-cited artifact (`4e9e228`) remains unmerged and is a different harness.
Which is the RI-RS boundary of record, and the disposal of PR #59, are
implementation-corpus decisions. CK-003 modifies nothing in either repository.

### CFL-004 — closed gate whose evidence is not merged — **OPEN, confirmed**

Verified during this task: `49d0e4f`, `3e8e0e3`, `4e9e228` and `420653e` are all
reachable from `claude/cross-language-canonical-001-n4v2c5` in their respective
repositories and **none** is reachable from `origin/main`. `aura-poc-a-core-v3.3`
`main` contains no RFC 8785 reference whatsoever. Detail in
`ck003/dq-006-canonical-serialization/CK003_EXECUTION_EVIDENCE.md` §2.

### CFL-005 — the event-type registry rejects CANONICAL-001's object — **OPEN, out of scope**

`aps/EVENT_TYPE_REGISTRY.md` §3 requires strict-mode rejection of unregistered
tokens; §5 records that no token is yet promoted; CANONICAL-001 carries
`"event_type": "AUDIT_RECORD"`.

CK-003 does **not** resolve this and does **not** register the token. It removes
the collision from the *serialization* question by stating the input domain
explicitly: canonicalization is total over the JSON data model and asserts nothing
about semantic admissibility (APS-200 §8.2), and CANONICAL-001 is scoped as a
serialization vector rather than an entity instance (§5 above, CONF-003 §10). The
registry question is DQ-004's and is untouched.

*This is a deliberate, recorded scoping decision, not a silent reconciliation. If
the Protocol Custodian rules that the canonicalization input domain must instead
be the validated-entity space, CANONICAL-001 must be re-scoped and this decision
reversed.*

### Observation — not a registered conflict, raised here for the record

`ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` is still
`PROPOSED — awaiting Chief Architect approval`, while
`closures/DQ-002_FINAL_CLOSURE.md` records DQ-002 as `CLOSED — PASS`. This is the
same shape of inconsistency as CFL-002, one gate over. **CK-003 does not touch
it**: §18 of the execution order forbids altering DQ-002's closure state, and the
hash-domain decision is not CK-003's to enact. Raised for the Protocol Custodian
alongside the register.

---

## 9. Superseded artifacts

Retained, never deleted, each marked in place with its reason.

| Artifact | Was | Now | Reason |
|---|---|---|---|
| `ck003/dq-006-canonical-serialization/APS-200-SECTION-8-PROPOSED.md` | PROPOSED — not yet frozen | SUPERSEDED | The amendment it drafted is enacted in APS-200 §8 |
| `ck003/dq-006-canonical-serialization/APS-300-RECONCILIATION.md` | PROPOSED | SUPERSEDED | Enacted as APS-300 §5.1 |
| `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md` | BLOCKED_PENDING_IMPLEMENTATION_CONFORMANCE | SUPERSEDED | Its BLOCKED verdicts were overtaken by executed evidence |
| `ck003/dq-006-canonical-serialization/CANONICAL_SERIALIZATION_CLOSURE_STATE.md` | OPEN / PROPOSED PROFILE READY | SUPERSEDED | Every blocker it lists is now met or explicitly routed |
| `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-…` | PROPOSED — approval/freeze required | ENACTED (pending merge approval) | Its decision is now APS-200 §8 |

---

## 10. Production impact

**None.** No file in `aura-poc-a-core-v3.3`, `aura-guard-v1.3` or `cargo` is
modified by CK-003. No runtime dependency is added anywhere. JCS remains a
conformance boundary in both reference implementations and is not moved into
production hashing or Merkle code.

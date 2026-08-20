# Conflict Register

**Classification:** EVIDENCE — NON-NORMATIVE
**Reconciled:** 1 of 5 (CFL-002, by classification under CK-003). The remaining four are
routed to the Protocol Custodian / Human Architectural Authority and are not resolved by
any agent.

> **CK-003 disposition, 2026-08-20.** CFL-002 is addressed: the contradictory DQ-006
> statuses are reconciled by enacting APS-200 §8 and marking the stale artifacts
> SUPERSEDED, which is the treatment §13 of the CK-003 execution order directs. That
> marking is proposed on a branch and takes effect on merge — the approval remains the
> Chief Architect's act under `GOVERNANCE.md` §2.
>
> CFL-001 is **narrowed but open**: the implementation-corpus D-3 record asserts no
> competing encoding, only that none may be *derived* from implementation behaviour;
> APS-200 §8 derives nothing from it. The cross-corpus precedence question itself is
> untouched. CFL-003 is partially overtaken (PR #58 merged to `aura-guard-v1.3` `main`
> with the engine in `[dev-dependencies]`). CFL-004 is **confirmed** by direct
> reachability checks. CFL-005 is **open and out of CK-003 scope**; the serialization
> question is separated from it by the input-domain rule in APS-200 §8.2.
>
> Full disposition: `ck003/CK003_CANONICAL_SERIALIZATION_RECONCILIATION.md` §8.

---

## CFL-001 — Cross-corpus authority conflict on canonical encoding

**Verdict: CONFLICT / DECISION REQUIRED**

| Side | Artifact | Says |
|---|---|---|
| Specification corpus | `aura-specification/evidence/DQ-006_CLOSURE_PACKAGE.md` | RFC 8785 JCS + SHA-256 + RFC-6962 `0x00` leaf: **CLOSED — PASS** |
| Implementation corpus | `aura-poc-a-core-v3.3/review/2026-08-14_P0_6_D3_D4_DECISION_RECORD/D3_D4_DECISION_RECORD.md` §4–§5 | D-3 concrete semantic value **NOT ESTABLISHED**; canonical byte encoding, serialization format and hash-domain representation explicitly **not** established, and not derivable from implementation behaviour or RI-PY |

These are statements about the same question with incompatible content.

**Why it cannot be reconciled here.** The core repository's own OQ-A package already
established that the two corpora are governance-disjoint, that no cross-corpus precedence rule
exists in either, and that the only text ordering them is one whose authority to do so is
established by nothing. Choosing a winner *is* the missing governance act.

**Required:** a ruling from the Protocol Custodian / Chief Architect on which ladder governs a
cross-corpus protocol-semantics decision, recorded in an artifact both corpora acknowledge.
Everything downstream of canonical encoding — DQ-002, DQ-006, INV-003, INV-011, CONF-003,
CONF-010, the fixture corpus — waits on this.

---

## CFL-002 — DQ-006 carries three contradictory statuses inside one repository

**Verdict: CONFLICT**

| Artifact | Status |
|---|---|
| `evidence/DQ-006_CLOSURE_PACKAGE.md:4` | `Status: **CLOSED — PASS**` |
| `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md:3` | `**Status:** BLOCKED_PENDING_IMPLEMENTATION_CONFORMANCE`, and at `:44` `DQ-006: BLOCKED` |
| `fixtures/corpus/CANONICAL-001_jcs_evidence.json:27-29` | `"RI-PY": "PENDING_EXECUTION"`, `"RI-RS": "PENDING_EXECUTION"`, `"cross_language_equality": "PENDING_EXECUTION"` |

None of the three references the others. `ck003/README.md` defines a `SUPERSEDED` status; it is
not applied to any of them.

Compounding: the governing ADR
(`ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md:3`) is
`**Status:** PROPOSED — approval/freeze required`, and the amendment that would make JCS
normative (`APS-200-SECTION-8-PROPOSED.md`) is `PROPOSED — not yet frozen`. A gate recorded
CLOSED sits above an ADR that is not approved.

**Required:** a single status for DQ-006, with the superseded artifacts marked. Status changes
are a human act under `GOVERNANCE.md` §2.

---

## CFL-003 — Three incompatible RI-RS implementations of the same gate

**Verdict: CONFLICT**

| Branch / PR | Dependency placement | Executes JCS? | Status |
|---|---|---|---|
| `claude/cross-language-canonical-001-n4v2c5` @ `4e9e228` — *the one the closure cites* | separate `conformance/` package, own workspace + lockfile | yes | unmerged, **no PR** |
| PR #58 `claude/canonical-001-conformance-vm2k69` | `[dev-dependencies]` | yes | open; own commit message: *"does not close DQ-006 or DQ-002"* |
| PR #59 `ck003/canonical-001-conformance` | **root `Cargo.toml` `[dependencies]`** | **no** | open; `BLOCKED_PENDING_JCS_BOUNDARY`; 0 checks run |

PR #59 would put a conformance-only engine into the production dependency graph, contradicting
the scope rule written in the same pull request
(`conformance/canonical/JCS_DEPENDENCY_DECISION.md`: *"It MUST NOT be introduced into
production hash/Merkle code as part of this change"*), and would record the gate as BLOCKED
while the specification records it as CLOSED.

**Required:** a decision on which of the three is the RI-RS conformance boundary of record, and
disposal of the other two. Merging #59 as-is would breach the production-isolation constraint
the handover lists as frozen.

---

## CFL-004 — A closed gate whose evidence is not merged anywhere

**Verdict: CONFLICT / EVIDENCE GAP** — detail in `05_EVIDENCE_GAPS.md` / EG-01.

The DQ-006 closure is merged into `aura-specification` `main`. All four commits it cites are
unreachable from the default branch of the repository each lives in, and none has an open pull
request. A reviewer who clones the three repositories at `main` cannot reproduce, inspect, or
even locate the evidence for the program's only closed gate.

---

## CFL-005 — The event-type registry rejects the object in the closed fixture

**Verdict: CONFLICT**

- `aps/EVENT_TYPE_REGISTRY.md` §3: an unregistered token **MUST** be REJECTED in strict mode;
  *"An implementation MUST NOT silently normalize an unknown token into a known token."*
- `aps/EVENT_TYPE_REGISTRY.md` §5: *"No individual event token is promoted to final normative
  status by this document yet."* — the registry is empty.
- CANONICAL-001, the fixture underlying the DQ-006 closure, has
  `"event_type": "AUDIT_RECORD"`.

Under the registry's own rule, strict conformance would reject the object on which the closed
gate rests. CONF-012 cannot pass against an empty vocabulary, and DQ-004 correctly records
itself as BLOCKED for final closure.

**Required:** normative entries in the event-type registry, via whatever approval path CFL-001
establishes.

---

*This register records conflicts. It resolves none of them, and confers no normative
semantics.*

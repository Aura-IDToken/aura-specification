# B — Normative Graph

**Classification:** EVIDENCE — NON-NORMATIVE

---

## B.1 What is actually normative

Very little. The graph below distinguishes four tiers that the program's own documents keep
conflating.

| Tier | Meaning | What is in it |
|---|---|---|
| **FROZEN** | Approved and immutable | `AURA Constitution` v1.0 only |
| **DRAFT** | Written, not approved | All APS documents (`1.0-DRAFT`); `APS-001` (`0.2-DRAFT`); `SPEC-002` (`0.3-DRAFT`, banner: *"Normative effect: NONE until APPROVED"*); CONF-001…015 (all DRAFT) |
| **PROPOSED** | Offered for approval, not approved | `ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md`; `ADR-CK003-DQ002-HASH-DOMAIN.md`; `APS-200-SECTION-8-PROPOSED.md` |
| **ASSERTED** | Recorded as settled without an approved artifact beneath it | `evidence/DQ-006_CLOSURE_PACKAGE.md` (**CLOSED — PASS**) |

The fourth tier should not exist. A gate recorded CLOSED above a PROPOSED ADR has no approved
artifact carrying its semantics. See `04_CONFLICT_REGISTER.md` / CFL-002.

## B.2 The chain the handover assumes

```
NORMATIVE SPECIFICATION → DECISION → INVARIANT → CONFORMANCE REQUIREMENT
    → CANONICAL FIXTURE → IMPLEMENTATION EXECUTION → EVIDENCE → CI GATE → RELEASE GATE
```

## B.3 The chain as it actually stands, for the one gate claimed closed

```
APS-200 §8  ................................  PROPOSED — not frozen
    ↓
ADR-CK003-DQ006  ...........................  PROPOSED — approval/freeze required
    ↓
INV-003  ...................................  OPEN / BLOCKED (APS-200 serialization open)
    ↓
CONF-003  ..................................  DRAFT
    ↓
CANONICAL-001 fixture  .....................  implementation_status: PENDING_EXECUTION
    ↓                                          (fixtures/corpus/CANONICAL-001_jcs_evidence.json)
RI-PY execution  ...........................  exists — on an unmerged branch, no PR
RI-RS execution  ...........................  exists — on an unmerged branch, no PR
    ↓
CROSS-LANGUAGE-001  ........................  recorded 18/18 checks
    ↓
CI gate  ...................................  DOES NOT EXIST (no workflows in this repo)
    ↓
DQ-006  ....................................  recorded CLOSED — PASS
```

Every link above the closure is PROPOSED, OPEN, PENDING or absent. The chain does not carry
weight at any point, yet the terminal node is recorded as closed.

## B.4 Four parallel decision namespaces

The program is running four independent identifier systems over overlapping subject matter,
with no mapping between them:

| Namespace | Home | Subject | Example |
|---|---|---|---|
| `DQ-nnn` | `aura-specification` (`ck003/`) | canonical serialization, hash domain, version, event type | DQ-002, DQ-003, DQ-004, DQ-006 |
| `D-n` | `aura-poc-a-core-v3.3` (`review/`, P0-6) | canonical representation, collection semantics, version discriminator | D-3, D-4, D-5, D-7, EG-1 |
| `ARI-D-nnn` | `aura-poc-a-core-v3.3` (`review/`, RD-1) | the ARI measurement algorithm | ARI-D-001…ARI-D-027 (**27 decisions, 0 answered**) |
| `AD-CA-nnn` / `REQ-002-nnn` | `SPEC-002` | Constitution Artifact contract | cited by the others as "related identifiers only" |

**DQ-002 and D-3 are about the same question** — what bytes are hashed — and record different
states. `DQ-001`, `DQ-005` and `DQ-007+` are referenced nowhere in the specification repository;
the DQ numbering is not contiguous, which makes "all DQs closed" unverifiable by construction.

## B.5 The governance-disjointness finding already on record

The core repository's OQ-A package
(`review/2026-08-12_OQ-A_GOVERNANCE_JURISDICTION/13_EXECUTIVE_DECISION_BRIEF.md`) already
established, with provenance, that:

1. **The two corpora are governance-disjoint.** Neither cites the other, in either direction.
   Each has its own hierarchy, named authority, change process and conflict rule, and no
   artifact spans them.
2. The only text that orders them is `AGENTS.md`/`CLAUDE.md` tiers 1–2 — asserted by a document
   that the same list places at tier 6, carrying no document ID, version or status, and which
   the specification corpus does not acknowledge.
3. **Every approval gate that exists in text has either no identified actor or no instance.**
   Chief Architect — never identified. ARB — no roster, no charter. RFC route — never
   exercised. Custodian signature — required, never produced. SPEC class — no approver at all.

Recorded there: **13 conflicts, 0 reconciled; 15 evidence gaps, 0 fillable from repository
material alone.** That package pre-dates this one and its conclusions are unchanged by it.

**Implication for this assessment.** A cross-corpus decision — which is what every remaining
DQ closure is — has no established route to approval today. That is the top of the graph, and
it is empty.

---

*This document records state and confers no normative semantics.*

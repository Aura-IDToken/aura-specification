# A — Current State Assessment

**Classification:** EVIDENCE — NON-NORMATIVE

---

## A.1 The one-sentence summary

The specification repository has recorded a canonical-serialization gate as **CLOSED — PASS**,
while the evidence that closure cites is not merged into either implementation, the ADR that
would make it normative is still PROPOSED, two sibling artifacts in the same repository still
say BLOCKED and PENDING_EXECUTION, and the implementation repository holds a governance record
stating that no canonical byte encoding has been established at all.

## A.2 Branch reality

All three Aura repositories are checked out at their `main` tip. The designated development
branch is a zero-commit pointer at `main` in each:

| Repository | `main` | `claude/aura-protocol-handover-80wawo` | `git diff main...HEAD` |
|---|---|---|---|
| `aura-specification` | `2f5d226` | `2f5d226` | empty |
| `aura-poc-a-core-v3.3` | `64bf959` | `64bf959` | empty |
| `aura-guard-v1.3` | `cd3494b` | `cd3494b` | empty |

**Consequence.** Anyone reading a working tree of this program reads `main`, and `main`
contains none of the conformance work the handover describes. The work exists, but it exists
on unmerged branches (§A.4).

## A.3 `aura-specification` @ `2f5d226` — AS-IS

| Area | State |
|---|---|
| APS corpus | APS-000/100/200/300/400/500/900/950 exist as `1.0-DRAFT`. `APS-001` exists at `specification/APS-001_PROTOCOL_SPECIFICATION.md` as **`0.2-DRAFT — ARCHITECTURE REVIEW REQUIRED`**, with Appendix A listing 8 open closure dependencies. |
| Open TODOs in normative text | APS-200 carries 6 (including §canonical serialization for RI-PY↔RI-RS); APS-300 carries 3 (including the `evidence_hash` algorithm); APS-500 §5 canonical fixtures is TODO. |
| Invariants | INV-001…INV-015 all defined. **0 are PASS.** All OPEN; INV-003 BLOCKED pending APS-200 serialization. |
| INV→CONF mapping | Defined in **three** places that disagree — `invariants/INVARIANT_REGISTRY.md` (all 15 mapped), `aps/APS-100_PROTOCOL_INVARIANTS.md` (5 unmapped), `invariants/README.md` (5 TODO). |
| Conformance tests | CONF-001…CONF-015 exist, all `Status: DRAFT`. `conformance/README.md` indexes only CONF-001…010. |
| Fixtures | `FIX-001` is a placeholder whose every value is the literal string `"TODO"`. `FIX-INV-007/012/013/014/015` exist but four are self-declared blocked or parametric. **`CK003-001…010` do not exist** (see `05_`). |
| Event-type registry | `aps/EVENT_TYPE_REGISTRY.md` exists and §5 states: *"No individual event token is promoted to final normative status by this document yet."* The vocabulary is empty. |
| Traceability | `compliance/TRACEABILITY_MATRIX.md` shows **`NOT VERIFIED` for RI-PY and RI-RS on all 15 rows**, last reviewed 2026-07-23. |
| CI | **`.github/workflows/` does not exist.** Zero workflows, zero gates. All five planned validation scripts in `scripts/README.md` are TODO and absent. Nothing in this repository is machine-verified. |
| RFCs / ARRs | `rfcs/` contains only `README.md`; no `ARR-NNN` exists. `GOVERNANCE.md` §5.2 requires an RFC plus a 14-day comment period for changes affecting protocol behaviour, so CONF-011…015 entered outside the required path. |

## A.4 Where the conformance work actually is

The DQ-006 closure package cites four execution/evidence commits. None is reachable from the
default branch of the repository it lives in, and none has an open pull request:

| Cited artifact | Repository | Commit | Location | PR |
|---|---|---|---|---|
| RI-PY execution | `aura-poc-a-core-v3.3` | `49d0e4f` | branch `claude/cross-language-canonical-001-n4v2c5` | none |
| RI-PY evidence | `aura-poc-a-core-v3.3` | `3e8e0e3` | same branch | none |
| RI-RS execution | `aura-guard-v1.3` | `4e9e228` | branch `claude/cross-language-canonical-001-n4v2c5` | none |
| RI-RS evidence | `aura-guard-v1.3` | `420653e` | same branch | none |

A related RI-PY branch, `claude/ri-py-jcs-conformance-5anw9q` (`2beac9e`), carries the
`JCS-B01…B06` behaviour suite. It is likewise unmerged with no open PR.

**Three mutually contradictory RI-RS implementations of the same gate exist simultaneously:**

| Branch / PR | Isolation of `serde_json_canonicalizer` | Does the test execute JCS? | Self-declared status |
|---|---|---|---|
| `claude/cross-language-canonical-001-n4v2c5` @ `4e9e228` (no PR) | Separate `conformance/` package with its own workspace root and lockfile | Yes | executed |
| PR #58 `claude/canonical-001-conformance-vm2k69` | `[dev-dependencies]` | Yes | *"does not close DQ-006 or DQ-002"* (its own commit message) |
| PR #59 `ck003/canonical-001-conformance` | **Root `Cargo.toml` `[dependencies]` — production graph** | **No** — the test re-hashes the frozen oracle hex; `jcs.rs` is never called | `BLOCKED_PENDING_JCS_BOUNDARY` |

PR #59 contradicts the isolation rule stated in the file it adds
(`conformance/canonical/JCS_DEPENDENCY_DECISION.md`: *"It MUST NOT be introduced into
production hash/Merkle code as part of this change"*). Its combined status check returns
`pending` with `total_count: 0` — no check has run. See `04_CONFLICT_REGISTER.md` / CFL-003.

## A.5 `aura-poc-a-core-v3.3` @ `64bf959` — AS-IS

- **No `conformance/` package. No `rfc8785`. No JCS adapter. No RFC-6962 leaf.** Confirmed by
  search across the tree.
- **Three mutually incompatible canonicalizations coexist**, all `json.dumps`:

  | Site | Form |
  |---|---|
  | `audit/merkle.py:85` | `sort_keys=True, separators=(",", ":")` |
  | `compliance/certificate.py:69` | `sort_keys=True` (default separators `", "` / `": "`) |
  | `core/merkle.py:8` | `sort_keys=True` (default separators, default encoding) |

  This is a recorded, unresolved finding in the repository's own baseline audit
  (`review/2026-08-11_ENGINEERING_BASELINE/04_DETERMINISM_AUDIT.md`, D-7; `08_BLOCKERS.md`,
  P1-4 / NB-010).
- **Merkle is not RFC-6962**: `audit/merkle.py:163` computes `sha256(left + right)` over
  concatenated *hex digest strings* with no domain-separation byte, and duplicates the odd
  node (`audit/merkle.py:162`).
- `protocol_version` **does not appear in any Python source file**. `event_type` likewise does
  not appear anywhere in code — there is no event-type handling at all.
- The binding governance corpus is heavy and explicit: `CONSTITUTIONAL_DECREE.md` declares the
  repository a *"FROZEN REGULATORY MEASUREMENT INSTRUMENT"*; `AGENTS.md` rule 9 requires
  executable evidence for every conformance claim; rule 13 requires human approval before
  merging protocol-affecting changes.
- CI: one workflow, `execution-checks.yml` — determinism checks across x86_64/arm64 plus a
  cross-architecture bit-identity comparison. **No conformance gate, no canonicalization gate,
  no evidence gate.**

## A.6 `aura-guard-v1.3` @ `cd3494b` — AS-IS

- **No `serde_json_canonicalizer`, no JCS boundary, no `CANONICAL-001`** anywhere in the tree
  or the lockfile.
- `src/merkle.rs` **is** RFC-6962 — verified directly: `h.update([0x00u8])` for leaves
  (`src/merkle.rs:31`), `h.update([0x01u8])` for interior nodes (`:40`), no last-leaf
  duplication.
- The audit chain preimage is **not JSON**: nine fields joined by `"|"` (`src/chain.rs`).
- Every recorded fixture is explicitly stamped
  `"DQ-002 and DQ-006 unresolved; these bytes carry no specification standing."`
  This repository claims canonical standing for nothing — which is correct, and is the most
  disciplined status handling in the program.
- Three test harnesses exist and are substantial: hash-domain replay (`tests/hash_domains.rs`),
  byte-representation fixtures (`tests/byte_representations.rs`), regression/mutation
  (`tests/regression.rs`), including mutation controls for field value, field order,
  separator, encoding and timestamp representation.
- **Documentation/implementation divergence:** `src/models.rs:95` documents a **7-field**
  chain preimage (`prev_hash || decision || policy_set || input_hash || shadow_hash || seq ||
  timestamp`) while `src/chain.rs` implements **9** (adding `policy_hash` and `context`).
  Verified; unresolved; tracked as D-3.4.
- `.github/workflows/docker-image.yml:21` runs `docker build . --file Dockerfile`; there is no
  root `Dockerfile` (only `deploy/Dockerfile`). That workflow cannot succeed.
- `D3_REAL_CHAIN_EXECUTION_BLOCKER.md` states at lines 15–17 that two artifacts are
  "deliberately absent"; both are present at repo root today, produced by later commits. The
  blocker report was never amended or retracted.

## A.7 Maturity, restated

The handover positions the program at "specification → conformance transition". The evidence
supports a different position: the program has produced high-quality *decision-preparation*
material and high-quality *implementation-side harnesses*, and has not yet produced a single
machine-verified, merged, cross-repository conformance result. The blocking constraint is not
technical. It is that no established authority can currently accept one — see
`04_CONFLICT_REGISTER.md` / CFL-001.

---

*This document records state and confers no normative semantics.*

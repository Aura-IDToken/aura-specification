# G-1b — Historical Normative Recovery Audit: APS-200 §8.1–§8.9

**Artifact class:** GOVERNANCE / HISTORICAL FORENSIC AUDIT — non-normative
**Authority rank:** below every approved APS document (APS-001 §10 ladder). This
document defines no protocol semantics, authors no normative text and authorizes
no implementation.
**Branch:** `claude/aps-200-spec-recovery-b7wc2h`
**Repository state:** read-only audit. APS-200 byte-identical before and after.
**Gate:** P0 RECOVERY GATE — GO specification reconciliation · NO-GO implementation ·
NO-GO C4 · NO-GO DQ-003 closure
**Central question:** did APS-200 historically contain a normative §8.1–§8.9 structure,
what exactly was it, how did it disappear, and what depends on it?

---

## 1. Executive Summary

**Answer: YES — and the disappearance was a merge-resolution overwrite, not a decision.**

APS-200 carried a fully authored normative `§8.1`–`§8.9` structure on `main` at
commit `ff30e16` (2026-08-20, PR #26). That commit was an **atomic 24-file
reconciliation**: it authored §8.1–§8.9 *and*, in the same commit, authored every
downstream `§8.x` citation now found dangling — in APS-300, the DQ-006 ADR, CONF-003,
the DQ-006 closure package, the specification consistency scan, the independent oracle,
the CHANGELOG and the CANONICAL-001 fixture.

Twenty-two hours later, merge commit `7826db9`
(*"Merge branch 'main' into ck003/specification-integration-dq006"*) resolved the
APS-200 conflict by **taking the branch side wholesale**. The evidence is arithmetic:

| Comparison | Result |
|---|---|
| `7826db9` vs its **branch-side** parent `e71ca3e` | **3 insertions, 1 deletion** — a §4 `integrity_hash` edit only. §8 untouched. |
| `7826db9` vs its **main-side** parent `57a0a60` | **39 insertions, 84 deletions** — the entire §8.1–§8.9 structure discarded. |

The merge performed **no reconciliation of §8 at all**. It kept the branch's older §8
draft (`b9311d0`, authored 2026-08-20 19:57 +0200) and discarded main's newer, more
developed §8.1–§8.9 (`a0df11a`/`ff30e16`, authored 22:12 / 22:42 +0200).
`9682cf5` (PR #25) is the squash-merge that landed that resolution on `main`; it touched
4 files, **none of them a citing artifact**.

**G-1b is therefore a half-reverted atomic reconciliation.** Twenty-three of the
twenty-four files that `ff30e16` wrote still stand. APS-200 alone was rolled back — to a
draft that predates the text its own dependents were written against.

**The current §8 is the older draft, not a refinement of §8.1–§8.9.**

Damage triage across the nine historical subsections:

| Damage type | Subsections |
|---|---|
| **NORMATIVE REPLACEMENT** (rule survives with proven authority) | §8.5, §8.9 |
| **AMBIGUOUS** (plausible replacement, equivalence not provable) | §8.2, §8.3, §8.6, §8.8 |
| **NORMATIVE CONTENT LOSS** (no authoritative home anywhere) | **§8.1, §8.4, §8.7** |

49 explicit `§8.x` references across 6 files are **REFERENCE LOSS** in every case; three
of those subsections are also **NORMATIVE CONTENT LOSS**, which is the finding that
actually blocks reconciliation.

Two corrections to the previously delivered G-1 report are recorded in **§12**; neither
changes the G-1 verdict, both change the mechanism narrative.

**One counter-intuitive finding:** the same merge that destroyed §8.1–§8.9 **added** the
§9 Event-Type Registry incorporation rule that G-3 now depends on. The merge was not
purely destructive, which is why a blanket revert is not the safe repair (§10).

**Verdict: SPECIFICATION RECOVERY STATUS = READY FOR RECONCILIATION.** The historical
truth is fully established from primary git evidence; what remains are seven Custodian
decisions (§13), not further forensic work.

---

## 2. Repository / Commit Baselines

### 2.1 Working state at audit time

| Repository | Branch | Working tree |
|---|---|---|
| `aura-specification` | `claude/aps-200-spec-recovery-b7wc2h` | CLEAN |
| `aura-poc-a-core-v3.3` (RI-PY) | same | CLEAN |
| `aura-guard-v1.3` (RI-RS) | same | CLEAN |
| `cargo` | same | CLEAN |
| `.github` | same | CLEAN |

`aps/APS-200_CANONICAL_DATA_MODEL.md` — SHA-256
`46d2d53d4b6c2095f5d33e08fe0eab477e611a114e02b0dc9d79649a1e1b9a66`, unchanged
throughout this audit.

### 2.2 Commit identifiers — verified, not assumed

Every identifier supplied in the task brief was independently resolved against git.
**No discrepancy found.** Two identifiers required refinement rather than correction.

| Given | Verified | Date | Subject | Verdict |
|---|---|---|---|---|
| `ff30e16` | `ff30e166be2511b6d5684a33efb8c7da9d63a574` | 2026-08-20 22:42:07 +0200 | spec(dq-006): reconcile canonical serialization closure across APS-200/300, ADR, CONF-003 (#26) | **CONFIRMED** — holds §8.1–§8.9; ancestor of `main` |
| `9682cf5` | `9682cf53956f27c18821ac29531a356c5ed4afa5` | 2026-08-21 18:48:56 +0200 | CK-003: reconcile APS-200 with DQ-006 and refresh closure controls (#25) | **CONFIRMED but incomplete** — it is the *landing* commit, not the deciding one; see `7826db9` |
| `bf33eb4` | `bf33eb40411d02ba30c68708f980b31747e6ac99` | 2026-08-22 21:44:56 +0200 | spec(dq-003): define EP-001 event payload contract | **CONFIRMED** — DQ-003 lineage regression, separate event |
| — | **`7826db9`** `7826db9e3e28d356693ba24618f320c44e3120b1` | 2026-08-21 18:48:18 +0200 | Merge branch 'main' into ck003/specification-integration-dq006 | **NEWLY IDENTIFIED** — the actual deciding commit |

Supporting revisions, all verified:

| Commit | Date | Blob | §8.x headings | Lines | Branch | Ancestor of `main`? |
|---|---|---|---:|---:|---|---|
| `b68181e` | 2026-07-23 21:03 +0000 | `c974f59` | 0 | 243 | initial structure | yes |
| `704832a` | 2026-08-20 15:56 +0000 | `7ab340a` | **7** | 447 | `claude/ck003-canonical-serialization-hjlaba` | **no** |
| `b9311d0` | 2026-08-20 19:57 +0200 | `091e331` | 0 | 289 | `ck003/specification-integration-dq006` | **no** |
| `a0df11a` | 2026-08-20 20:12 +0000 | `5f3ea8b` | **9** | 336 | `claude/dq-006-closure-reconciliation-j3httg` | **no** |
| **`ff30e16`** | 2026-08-20 22:42 +0200 | `5f3ea8b` | **9** | 336 | merged to `main` (PR #26) | **yes** |
| **`7826db9`** | 2026-08-21 18:48:18 +0200 | `0488eec` | **0** | 291 | `ck003/specification-integration-dq006` | **no** |
| **`9682cf5`** | 2026-08-21 18:48:56 +0200 | `0488eec` | **0** | 291 | `main` (PR #25) | yes — **is** main |
| `8d3f1fe` | 2026-08-22 21:34 +0200 | `191adb7` | 0 | 389 | DQ-003 lineage | no |
| `bf33eb4` | 2026-08-22 21:44 +0200 | `fc1b58e` | 0 | 353 | DQ-003 lineage | no |
| `e109cff` | 2026-08-22 21:53 +0200 | `4d10ff5` | 0 | 398 | DQ-003 lineage | no |

Whole-file digests:

```text
704832a      035342d6999f59ad6a65a1ec6bb21284a5d9e5bef67aeee32e788be0b9a0d395  18408 B
b9311d0      666a9d5e350332435db8e11fdeaaa49c0ed76bf0dabc6b8098140f514b5345b2  11087 B
ff30e16      d008dde9bbd0e9d2a97419119a18bfd0c797ecadab4e4841afa6caf5faffc7c0  13863 B
origin/main  46d2d53d4b6c2095f5d33e08fe0eab477e611a114e02b0dc9d79649a1e1b9a66  11445 B
```

§8 block digests (heading to the rule before §9):

```text
ff30e16     §8 block  5459 B  sha256 e3f4f19f68b8e7890298672b7dbf345949c6f169bdd7e26a350c592e76e3a43b
origin/main §8 block  2763 B  sha256 12c1a825c6fa3dbb2fbb8439f20e66678052ac31d110e283eea7e5b6e9429c39
```

### 2.3 Authority ladder used for rank

From `specification/APS-001_PROTOCOL_SPECIFICATION.md` §10 (verbatim order):

```text
AURA Constitution v1.0 (FROZEN) → APS-001 → APS-100 → APS-200 → APS-300
→ APS-400 → APS-500 → APS-900 → APS-950
```

> "Supporting ADRs, RFCs, fixtures and implementation documents MUST NOT contradict an
> approved APS requirement. Higher-authority approved documents prevail in conflicts."

This ladder is used throughout: **APS-300 sits *below* APS-200.** A rule that migrates
from APS-200 to APS-300 has been *demoted*, not merely relocated.

---

## 3. Historical APS-200 §8 Timeline

| # | Commit | Date | APS-200 state | Change | Normative effect | Evidence |
|---:|---|---|---|---|---|---|
| 1 | `b68181e` | 2026-07-23 | flat §8, 243 L | Repository bootstrap. §8 permits "JSON, CBOR, Protocol Buffers" with deterministic serialization; interoperability format `TODO`. | INV-003 has no executable byte domain. | blob `c974f59` |
| 2 | `704832a` | 2026-08-20 15:56 | **§8.1–§8.7**, 447 L | First subsectioned §8. Numbering scheme **A**: 8.1 Canonical serialization profile · 8.2 Canonicalization input domain · 8.3 Delegated rules · 8.4 Hash domain · 8.5 Alternate wire encodings · 8.6 Version binding · 8.7 Conformance. | Never reached `main`. **Not the scheme the surviving citations use.** | blob `7ab340a`; branch `claude/ck003-canonical-serialization-hjlaba`; `git merge-base --is-ancestor 704832a origin/main` → false |
| 3 | `b9311d0` | 2026-08-20 19:57 | **flat §8**, 289 L | Parallel authoring from the same base `19ddeef`. Flat prose §8 + the CANONICAL-001 reference vector. **Adds the §9 Event-Type Registry incorporation rule.** | This is the text that is normative today. | blob `091e331` |
| 4 | `a0df11a` | 2026-08-20 20:12 | **§8.1–§8.9**, 336 L | Numbering scheme **B** authored. | The scheme every surviving citation matches. | blob `5f3ea8b` |
| 5 | **`ff30e16`** | 2026-08-20 22:42 | **§8.1–§8.9** on `main` | PR #26 merges scheme B **atomically with 23 other files** — APS-300, ADR-CK003-DQ006, CONF-003, DQ-006 closure package, consistency scan, independent oracle, CHANGELOG, CANONICAL-001 fixture, TRACEABILITY_MATRIX, APS-001. | **Peak normative coherence.** Structure and every citation to it exist simultaneously. | `git show --stat ff30e16` → 24 files, +849/−166 |
| 6 | `0693b0f`→`57a0a60` | 2026-08-21 | §8.1–§8.9 retained | DQ-002 / CROSS-LANGUAGE-002 work on `main`. APS-200 untouched. | none | blob still `5f3ea8b` at `57a0a60` |
| 7 | **`7826db9`** | 2026-08-21 18:48:18 | **flat §8**, 291 L | **Merge of `main` into the stale branch. §8 resolved to the branch side.** | **§8.1–§8.9 discarded. No reconciliation of §8 performed.** | parents `e71ca3e` (branch, `091e331`) + `57a0a60` (main, `5f3ea8b`); result `0488eec`. Diff vs branch parent: **+3/−1, §4 only**. Diff vs main parent: **+39/−84**. |
| 8 | **`9682cf5`** | 2026-08-21 18:48:56 | **flat §8** on `main` | Squash-merge of PR #25 (single parent `57a0a60`). Touches 4 files: APS-200, INV-001_015 matrix, architecture execution audit, GATE_A. | **The loss lands on `main`. No citing artifact is updated.** | `git show --name-only 9682cf5` |
| 9 | `c069a1b`, `8a27069` | 2026-08-23 | unchanged | Control records only. | none | APS-200 not in diff |
| 10 | `8d3f1fe`…`e109cff` | 2026-08-22 | DQ-003 lineage | `bf33eb4` deletes §6–§10 entirely and truncates the ENT-008 table. | Separate regression, **confined to two unmerged branches**. Addressed in the G-1 audit. | blob `fc1b58e` |

### 3.1 The 38-second window

`7826db9` at 18:48:18 and `9682cf5` at 18:48:56 are 38 seconds apart. This is the
signature of a merge-then-squash PR landing, not of two deliberations. **No commit
message, PR title or repository artifact anywhere states that §8.1–§8.9 was removed,
deprecated, superseded, renumbered or migrated.**

Search executed:
`git grep -iE 'remov|delet|deprecat|supersed' -- '*.md'` filtered for §6–§10 context,
across `main` and the DQ-003 branches → **only** the `APS-200-SECTION-8-PROPOSED.md`
supersession banner, which concerns a *different* artifact and points **to** §8.

---

## 4. Historical §8.1–§8.9 Matrix

Historical text is quoted **verbatim** from `git show ff30e16:aps/APS-200_CANONICAL_DATA_MODEL.md`
(blob `5f3ea8b`; §8 spans lines 213–313). Nothing in this section is paraphrased into normative form.

Equivalence is asserted **only** where the same requirement, scope, normative strength,
subject, object, constraints and authority rank can all be shown. Where any of the seven
fails, the classification is AMBIGUOUS or BROKEN — never CURRENT.

| § | Historical title | Historical rule (source: `ff30e16`) | Current equivalent | Authority of equivalent | Status |
|---|---|---|---|---|---|
| **8.1** | Transport representations | L215–222. "Implementations MAY use different transport formats (JSON, CBOR, Protocol Buffers), provided: Full model semantics are preserved / The transport representation round-trips to the same semantic object / INV-003 … is not violated." + "A transport representation is never itself the canonical representation." | **NONE.** Current §8 contains no transport-format permission, no round-trip obligation, no transport-vs-canonical distinction. Corpus-wide search for `CBOR` / `Protocol Buffers` / `transport format` in `aps/`, `specification/`, `conformance/`, `invariants/` returns **zero** normative hits — only the ADR's past-tense description at line 62 and an unrelated hex-presentation sentence in the DQ-002 ADR. | none | **BROKEN — NORMATIVE CONTENT LOSS** |
| **8.2** | Canonical serialization profile | L224–235. "**This section is the single normative authority for canonical serialization in the Aura Protocol.** No other document may define a conflicting canonical serialization profile…" + the numbered procedure: "1. The object MUST first satisfy the applicable APS schema and semantic constraints (§7). 2. … RFC 8785 … 3. … UTF-8. 4. The exact byte sequence … is the object's `canonical_bytes`." + "`canonical_bytes` is the sole input to every cryptographic operation…" | **PARTIAL.** Current §8 ¶1–2 carry the RFC 8785 + UTF-8 + byte-boundary requirement. **Absent:** (a) APS-200's own exclusivity declaration — the claim survives only as an assertion *from below* in APS-300 §5.1 ("APS-200 §8 is the sole normative authority"); (b) **step (1), schema validation before canonicalization** — current §7 lists five validation duties but imposes no ordering relative to canonicalization; the only surviving statement is ADR line 54, rank 6. | APS-300 (rank **below** APS-200); ADR (rank far below) | **AMBIGUOUS** — authority rank of the replacement is lower; ordering constraint unhomed |
| **8.3** | Properties fixed by the profile | L237–249. Seven-row table: member ordering by JCS UTF-16 code units never insertion order · insignificant whitespace absent · JCS/JSON string form minimal escaping · non-ASCII as raw UTF-8 not `\uXXXX` · RFC 8785 number rules · "`NaN` and `Infinity` … MUST be rejected, never coerced" · array order preserved. Framed by: "the following are fixed by it and **MUST NOT be redefined by an implementation or by a subordinate document**". | **MOSTLY REPLACED BY INCORPORATION.** Current §8 ¶1 makes RFC 8785 mandatory, and RFC 8785 itself fixes member ordering, whitespace, number form and non-finite rejection — so those properties are normatively reachable by reference. **Absent:** the explicit anti-redefinition precedence clause, which is not derivable from RFC 8785 and appears nowhere else. Non-finite rejection is otherwise stated only in the ADR (L53) and the DQ-006 execution order (L40), both rank 6; CONF-003 L83 lists the properties as *test* discriminators, rank 5. | RFC 8785 by incorporation (adequate for the properties); nothing for the precedence clause | **AMBIGUOUS** |
| **8.4** | Prohibited digest inputs | L251–260. Six-item enumeration: "An implementation MUST NOT compute a protocol digest over any of the following: pretty-printed or indented JSON; an implementation-specific or parser-preserving JSON serialization; a JSON string containing an escaped copy of `canonical_bytes`; a hexadecimal, Base64 or other textual encoding of `canonical_bytes`; a hexadecimal digest string used in place of raw digest bytes; a language-specific debug or `repr` form of the object." | **NO EQUIVALENT ENUMERATION.** Current §8 ¶2 forbids substituting textual/hex representations **for canonical-byte equality** — a different subject (equality comparison) and object (byte equality) from §8.4 (digest input). APS-300 §5.1 covers **one** of six items (hex is never a digest input). APS-001 §7.1 covers hex substitution. The remaining four items exist only in rank-6 decision records: `APS-300-RECONCILIATION.md:12`, `ADR-CK003-DQ006:29`, `02_hash_domain_adr.md:42`. **`CONF-003:99` requires an implementation to reject "any form listed in APS-200 §8.4" — there is no list.** | none at APS-200 rank | **BROKEN — NORMATIVE CONTENT LOSS** |
| **8.5** | Hash and Merkle domains | L262–278. `digest(B)=SHA-256(B)` / `leaf(B)=SHA-256(0x00‖B)` / `node(l,r)=SHA-256(0x01‖l‖r)`; raw octets not ASCII; **"The hash-domain model itself is owned by APS-001 §7.1 … Where this table and APS-001 §7.1 could be read differently, APS-001 §7.1 governs."**; "APS-001 §7.1 states that the serialization profile producing `canonical bytes` is owned by APS-200 — that profile is §8.2 above."; "The evidence-hash domain is defined by APS-300 §5 and is bound to `canonical_bytes` there." | **REPLACED, PROVABLY.** Current §8 restates all three formulas and the raw-octet rule. `APS-001 §7.1` — **higher** in the ladder — independently owns the domain model verbatim: leaf `SHA-256(0x00 ‖ bytes)`, node `SHA-256(0x01 ‖ left[32] ‖ right[32])`, "Hash inputs are raw bytes; hexadecimal strings are presentation values and MUST NOT substitute", "The serialization profile producing `canonical bytes` is owned by APS-200". APS-300 §5.1 binds the evidence-hash domain. Every rule survives at equal or higher authority. **Lost: only the two cross-attribution sentences and the tie-break clause**, which are navigational, not constraining. | APS-001 §7.1 (**above** APS-200) + current APS-200 §8 + APS-300 §5.1 | **NORMATIVE REPLACEMENT** (reference loss only) |
| **8.6** | Cross-implementation requirement | L280–282. "For the same semantic protocol object, **every conformant implementation MUST produce identical `canonical_bytes`**. In particular, RI-PY and RI-RS MUST be byte-identical. Verification is defined by CONF-003." | **PARTIAL, SCOPE NARROWED.** Current §8 states only that RI-PY and RI-RS *have* produced byte-identical output — **executed evidence, not a requirement**. `APS-001:139` supplies a rank-above-APS-200 MUST: "Where multiple implementations support the same canonical object, they MUST produce byte-identical canonical bytes and digest-identical cryptographic outputs **for shared fixtures**." The historical scope was *every semantic protocol object*; the surviving scope is *shared fixtures*. CONF-003 §4.2/§5 verifies at rank 5. | APS-001 (above) — but narrower scope | **AMBIGUOUS** — normative strength restored, scope demonstrably reduced |
| **8.7** | Scope boundary | L284–292. "Canonical serialization determines **representation only**. It does not define, and MUST NOT be read as defining: event semantics or the `event_type` vocabulary — see the Event-Type Registry and DQ-004; version semantics, or the distinction between `protocol_version` and `schema_version` — see §4 and DQ-003; object identity semantics — see §4 and INV-015; entity schemas — see §5 and §9; Merkle tree construction semantics beyond the domains stated in §8.5." | **NONE.** Current §8 contains no scope-boundary clause. `EVENT_TYPE_REGISTRY.md` §7 defers **to** APS-200 ("`event_type` participates in canonical object serialization exactly as defined by APS-200's approved serialization profile") — a one-directional deferral that does **not** assert the converse exclusion. Corpus search for "representation only" / "scope boundary" / "excludes event semantics" returns only *citations of* §8.7, never a restatement. | none | **BROKEN — NORMATIVE CONTENT LOSS** |
| **8.8** | Compatibility and migration | L294–298. "Binding or changing the canonical serialization profile is a protocol compatibility event and MUST be version-bound with explicit impact analysis." + "Evidence generated before this profile was bound MUST retain its original serialization and hash-profile identity. Such evidence MUST NOT be silently reinterpreted as RFC 8785 / RFC 6962 evidence." | **PARTIAL.** Current §8 keeps the version-binding sentence in equivalent form. The historical-evidence clause survives in **APS-300 §5.3** — verbatim and strengthened ("MUST NOT be compared for equality … without an explicit, version-bound migration record") — but APS-300 is **below** APS-200 and §5.3 is scoped to **Evidence objects**, whereas §8.8 governed *all* evidence under the profile. | APS-300 §5.3 (below APS-200), narrower subject | **AMBIGUOUS** — rank demoted, scope narrowed |
| **8.9** | Reference engines (informative) | L300–313. RI-PY `rfc8785` 0.1.4 / RI-RS `serde_json_canonicalizer` 0.3.2 table + "These engines are **conformance implementation detail, not protocol contract** … Naming an engine here does not authorize introducing it into any production runtime dependency graph, and an implementation using a different RFC 8785-conformant engine is not thereby non-conformant." + traceability footer. | **REPLACED.** Current §8 names both engines with versions, marks them "conformance-only", states "These implementation dependencies do not mandate insertion of either library into production runtime code. Production implementations MUST satisfy the RFC 8785 semantics; the named engines are reference conformance tools." Same subject, same object, same (informative) strength, same authority. **Lost: only the traceability footer**, which is navigational. | current APS-200 §8, same rank | **NORMATIVE REPLACEMENT** (reference loss only) |

### 4.1 Two competing numbering schemes existed — citations match only one

`704832a` used a **different** seven-part scheme. Any recovery that assumes a single
historical numbering is wrong.

| № | Scheme A (`704832a`, never on `main`) | Scheme B (`ff30e16`, on `main`) |
|---|---|---|
| 8.1 | Canonical serialization profile | Transport representations |
| 8.2 | Canonicalization input domain | Canonical serialization profile |
| 8.3 | Delegated rules | Properties fixed by the profile |
| 8.4 | Hash domain | Prohibited digest inputs |
| 8.5 | Alternate wire encodings | Hash and Merkle domains |
| 8.6 | Version binding | Cross-implementation requirement |
| 8.7 | Conformance | Scope boundary |
| 8.8 | — | Compatibility and migration |
| 8.9 | — | Reference engines (informative) |

**Every surviving citation matches Scheme B**, verified by content not by number:

- `CONF-003:99` "any form **listed** in §8.4" ↔ B/8.4 *Prohibited digest inputs* (a list).
  A/8.4 is *Hash domain* — not a list. ✔ B
- `ADR:42` "hash/Merkle domain defined in §8.5" ↔ B/8.5 *Hash and Merkle domains*.
  A/8.5 is *Alternate wire encodings*. ✔ B
- `ADR:54` "§8.2**(1)** schema-validated before canonicalization" ↔ item 1 of B/8.2's
  numbered procedure. ✔ B
- `ADR:57` "alternate wire encodings are transport only — §8.1" ↔ B/8.1
  *Transport representations*. Note the ADR borrows Scheme A's *vocabulary* while using
  Scheme B's *number* — consistent with one author revising A into B. ✔ B
- `SCAN:108,109` "§8.7 explicitly excludes version/event semantics" ↔ B/8.7
  *Scope boundary*. A/8.7 is *Conformance*. ✔ B

**Conclusion: `ff30e16` (Scheme B) is the unique historical referent of all 49 citations.**

---

## 5. Deletion / Collapse Analysis

### 5.1 Mechanism — proven

```text
     19ddeef ──┬── 704832a  §8.1–§8.7 (Scheme A)   ✗ never merged
               │
               └── b9311d0  flat §8  (19:57)  ── … ── e71ca3e ──┐
                                                                │
     e0f044d ── a0df11a  §8.1–§8.9 (20:12) ── ff30e16 (#26) ──► main ── 57a0a60 ──┤
                                                                                  │
                                                        7826db9  MERGE (18:48:18) ◄┘
                                                            │  §8 ← BRANCH SIDE
                                                            │  §8.1–§8.9 DISCARDED
                                                            ▼
                                                        9682cf5  squash (#25, 18:48:56)
                                                            │
                                                            ▼
                                                          main   flat §8, no subsections
```

### 5.2 Was the removal explicit or accidental?

**Accidental in effect; no explicit act exists.** Six independent lines of evidence:

1. **The merge did not edit §8.** `git diff e71ca3e 7826db9 -- aps/APS-200_…md` yields
   **+3/−1**, entirely inside §4 (`integrity_hash` self-exclusion note). §8 arrives at
   the merge result unchanged from the branch. A deliberate collapse would show edits.
2. **The surviving §8 predates the deleted one.** `b9311d0` 19:57 +0200 vs `a0df11a`
   20:12 +0000 (=22:12 +0200). The repository kept the **older** draft.
3. **PR ordering.** PR #26 (`ff30e16`) merged before PR #25 (`9682cf5`). The #25 branch
   was cut before #26 existed and was never rebased onto it.
4. **No deprecation record anywhere.** Corpus-wide search finds no statement that
   §8.1–§8.9 was removed, renumbered, superseded or migrated.
5. **Citations were left live.** `9682cf5` touched 4 files; **none** is a citing
   artifact. APS-300, the ADR, CONF-003, the closure package, the consistency scan and
   the oracle all still cite Scheme B.
6. **The CHANGELOG still describes the deleted text.** `CHANGELOG.md:26` — authored by
   `ff30e16`, verified via `git log -L 26,26:CHANGELOG.md` — states that §8 binds
   "the cross-implementation byte-identity requirement, the scope boundary against event
   and version semantics". Neither is in current §8. A deliberate collapse would have
   updated the changelog it had just written.

### 5.3 The atomicity that was broken

`ff30e16` changed 24 files, +849/−166:

```
CHANGELOG.md · aps/APS-200_CANONICAL_DATA_MODEL.md · aps/APS-300_EVIDENCE_MODEL.md
ck003/APS001_INV_MATRIX/INV-001_015_CONFORMANCE_MATRIX.md · ck003/DQ-006_CLOSURE.md
ck003/DQ-006_EVIDENCE_INDEX.md · ck003/README.md
ck003/dq-002-hash-domain/CROSS-LANGUAGE-002-EVIDENCE.md
ck003/dq-006-canonical-serialization/{ADR-CK003-DQ006-…, APS-200-SECTION-8-PROPOSED,
  APS-300-RECONCILIATION, CANONICAL-001_INDEPENDENT_ORACLE, CANONICAL_SERIALIZATION_CLOSURE_STATE}
ck003/dq-006-closure/{CROSS-LANGUAGE-001-EVIDENCE, DQ-006-CLOSURE,
  DQ-006_SPECIFICATION_CONSISTENCY_SCAN, README}
ck003/gates/GATE_A_APS001_CLOSURE_MATRIX.md · closures/DQ-006_CLOSURE_PACKAGE.md
compliance/TRACEABILITY_MATRIX.md · conformance/CONF-003_CANONICAL_SERIALIZATION.md
evidence/DQ-006_CLOSURE_PACKAGE.md · fixtures/corpus/CANONICAL-001_jcs_evidence.json
specification/APS-001_PROTOCOL_SPECIFICATION.md
```

`9682cf5` changed 4:

```
aps/APS-200_CANONICAL_DATA_MODEL.md
ck003/APS001_INV_MATRIX/INV-001_015_CONFORMANCE_MATRIX.md
ck003/audit/2026-08-20_ARCHITECTURE_EXECUTION_AUDIT.md
ck003/gates/GATE_A_APS001_CLOSURE_MATRIX.md
```

**Intersection with the citing set: `aps/APS-200_…md` only.** The specification was
rolled back; its 23 dependents were not.

### 5.4 What the collapse also *added*

The branch-side §9 text that survived is **not** a loss — it is content that never
existed on `main` before:

| §9 at `ff30e16` | §9 at `9682cf5` / today |
|---|---|
| "> **TODO**: Publish JSON Schema definitions for each entity at a stable URL." | "Machine-readable schema definitions … are maintained under `fixtures/schemas/`. Entity-specific schemas remain subject to APS-200 completion and MUST be added before APS-001 v1.0 approval…" **and** "The event-type vocabulary and validation contract are governed by `aps/EVENT_TYPE_REGISTRY.md`. That registry MUST be incorporated into the approved APS-200 profile before DQ-004 can be closed." |

Provenance: `git show b9311d0:aps/APS-200_…md` — the registry-incorporation sentence is
present at `b9311d0`, byte-identical to today. **G-3's §9 anchor was created by the same
merge that destroyed §8.1–§8.9.** A blanket revert to `ff30e16` would destroy it.

`9682cf5` also strengthened §10 traceability (ENT-007: `INV-012` → `INV-003, INV-012`;
CONF column `—` → `CONF-003, CONF-012`) and removed the
`*Source: Original text preserved in …txt*` footer.

---

## 6. Complete Reference Inventory

### 6.1 Scope

- Repositories: `aura-specification`, `aura-poc-a-core-v3.3` (RI-PY),
  `aura-guard-v1.3` (RI-RS), `cargo`, `.github` — git-tracked files only, 3 517 files.
- Excluded: binary/vendor extensions; NUL-bearing files; **`conformance/canonical/`**
  (this audit family — excluded so the inventory does not count itself).
- Explicit-reference rule: literal `APS-200` followed on the same line by a section
  token 6–10 (optionally `.1`–`.9`) as `§N`, `§N.M`, `Section N`, or a `/ , and ·`
  chain, rejected when another document identifier intervenes; plus filename-anchored
  `…_CANONICAL_DATA_MODEL.md §8.x–§8.y` ranges expanded to members.

### 6.2 Explicit references

| Target | Occurrences | Exists in current APS-200 |
|---|---:|---|
| §6 | **0** | yes |
| §7 | **0** | yes |
| §8 | **75** | yes |
| §8.1 | 3 | **no** |
| §8.2 | 5 | **no** |
| §8.3 | 6 | **no** |
| §8.4 | 6 | **no** |
| §8.5 | 10 | **no** |
| §8.6 | 2 | **no** |
| §8.7 | 9 | **no** |
| §8.8 | 6 | **no** |
| §8.9 | 2 | **no** |
| §9 | **5** | yes |
| §10 | **0** | yes |
| **Total** | **129** across **108** sites in **31** files | — |
| **§8.x subtotal** | **49** across **33** lines in **6** files | — |

Identical to the G-1 inventory — independently recomputed with the audit family excluded.

### 6.3 The 49 §8.x citation sites

| File | Lines | Targets |
|---|---|---|
| `aps/APS-300_EVIDENCE_MODEL.md` | 84, 94, 96, 97, 103 | §8.4, §8.2, §8.5 ×2, §8.8 |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | 99 | §8.4 |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 55, 230 (range ×9), 281, 282, 310 | §8.4, §8.1–§8.9, §8.8, §8.2, §8.7 |
| `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 42, 50, 51, 52, 53, 54, 56, 57, 58, 66, 110 | §8.5, §8.3 ×4, §8.2(1), §8.4, §8.1, §8.7, §8.8 ×2 |
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 28 (range ×9), 32, 55, 56, 57, 94, 95, 108, 109, 110 | §8.1–§8.9, §8.5 ×4, §8.7 ×4 |
| `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md` | 6 | §8.5 |

**Neither RI repository cites any APS-200 section.** `aura-guard-v1.3` mentions APS-200
only in a disclaimer at `tests/hash_domains.rs:697` and
`tests/fixtures/hash_domains/INVENTORY.json:191` ("No relationship is claimed between
these constructions and APS-200 `integrity_hash`, `event_payload_hash` or
`previous_record_hash`"). `aura-poc-a-core-v3.3` has **zero** `§8.x` matches.

### 6.4 Semantic dependencies — kept strictly separate from explicit references

These are **not** counted as references. They are locations whose *content* depends on a
historical §8.x rule without naming it.

| Historical rule | Semantic dependency | Rank | Effect of the loss |
|---|---|---|---|
| §8.1 transport | `ADR-CK003-DQ006:62` describes the pre-decision multi-format state (past tense) | 6 | Descriptive only — the ADR is correct about history |
| §8.3 non-finite | `DQ-006_FINAL_CLOSURE_EXECUTION_ORDER:40` "rejection of non-finite numbers" | 6 | Requirement now reachable only via RFC 8785 incorporation |
| §8.3 properties | `CONF-003:83` UTF-16 ordering, ES6 numbers, raw-UTF-8 escapes as *discriminating test properties* | 5 | Test-side survives; spec-side precedence clause does not |
| §8.4 prohibited inputs | `APS-300-RECONCILIATION:12`; `ADR-CK003-DQ006:29`; `02_hash_domain_adr:42` | 6 | Three rank-6 partial restatements cannot carry a rank-APS-200 MUST NOT |
| §8.5 domains | `APS-001 §7.1` (leaf/node/raw-bytes/hex-not-substitute) | **above APS-200** | Fully carried |
| §8.6 cross-impl | `APS-001:139` MUST, scoped to shared fixtures; `CONF-003 §4.2/§5` | above / 5 | Carried at narrower scope |
| §8.7 scope boundary | `EVENT_TYPE_REGISTRY §7` defers **to** APS-200; `DQ-004_EVENT_TYPE_SEMANTICS:38` | 3 / 6 | **One-directional only — the exclusion itself is unstated anywhere** |
| §8.8 migration | `APS-300 §5.3` verbatim + strengthened | below APS-200 | Carried, demoted, narrowed to Evidence |
| §8.9 engines | current APS-200 §8 | same | Fully carried |

---

## 7. CURRENT / HISTORICAL / BROKEN / AMBIGUOUS Classification

Definitions applied exactly as specified in the mandate. **No item is classified CURRENT
because a similar sentence exists** — the seven-way equivalence test governs.

### 7.1 Explicit-reference classification (n = 129)

| Status | Occurrences |
|---|---:|
| CURRENT | **54** |
| HISTORICAL | **23** |
| BROKEN | **49** |
| AMBIGUOUS | **3** |

| Target group | CURRENT | HISTORICAL | BROKEN | AMBIGUOUS | Total |
|---|---:|---:|---:|---:|---:|
| §6 | 0 | 0 | 0 | 0 | 0 |
| §7 | 0 | 0 | 0 | 0 | 0 |
| §8 | 53 | 21 | **0** | 1 | 75 |
| §8.1–§8.9 | 0 | 0 | **49** | 0 | 49 |
| §9 | 1 | 2 | 0 | 2 | 5 |
| §10 | 0 | 0 | 0 | 0 | 0 |

All 49 §8.x occurrences are BROKEN **at reference level** regardless of whether the
underlying rule survives — the numbered target does not exist. Reference status and
content status are **different axes** and are kept separate in §12.

The 3 AMBIGUOUS: `CHANGELOG.md:26` (describes the deleted §8 — cause now proven in
§5.2/5.4); `invariants/INVARIANT_REGISTRY.md:140` and `compliance/TRACEABILITY_MATRIX.md:26`
(INV-009 Version Consistency cites §9 "JSON Schema" — the G-1c finding, see §11.4).

### 7.2 Rule-level classification (the nine subsections)

| § | Reference status | Content status | Combined verdict |
|---|---|---|---|
| 8.1 | BROKEN | **LOST** | **BROKEN — NORMATIVE CONTENT LOSS** |
| 8.2 | BROKEN | partially replaced, lower rank | **AMBIGUOUS** |
| 8.3 | BROKEN | replaced by RFC 8785 incorporation, except precedence clause | **AMBIGUOUS** |
| 8.4 | BROKEN | **LOST** (1 of 6 items survives) | **BROKEN — NORMATIVE CONTENT LOSS** |
| 8.5 | BROKEN | replaced at equal/higher rank | **NORMATIVE REPLACEMENT** |
| 8.6 | BROKEN | replaced at higher rank, narrower scope | **AMBIGUOUS** |
| 8.7 | BROKEN | **LOST** | **BROKEN — NORMATIVE CONTENT LOSS** |
| 8.8 | BROKEN | replaced at lower rank, narrower scope | **AMBIGUOUS** |
| 8.9 | BROKEN | replaced at equal rank | **NORMATIVE REPLACEMENT** |

---

## 8. Blast-Radius Matrix

Dependency types: **N** normative · **C** conformance · **I** implementation ·
**T** test · **F** fixture · **A** audit/closure · **D** documentation-only.

| Repo | File | Line | Artifact | Reference text (abridged) | Historical § | Current target | Class | Rank | Type | Blast radius | Downstream | Closure claim depends? |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| spec | `aps/APS-300_EVIDENCE_MODEL.md` | 84 | Evidence Model §5.1 | "never itself a digest input (APS-200 §8.4)" | B/8.4 | none | BROKEN | APS-300 | **N** | Evidence-hash digest-input rule loses its APS-200 anchor | `evidence_hash`, CONF-004, CONF-010, INV-011 | no |
| spec | `aps/APS-300_EVIDENCE_MODEL.md` | 94 | §5.2 domain table | "`canonical_bytes` … Authority: APS-200 §8.2" | B/8.2 | §8 (flat) | BROKEN | APS-300 | **N** | Authority column of the domain-separation table | all §5 hash fields | no |
| spec | `aps/APS-300_EVIDENCE_MODEL.md` | 96–97 | §5.2 domain table | "Merkle leaf / interior-node … APS-200 §8.5 / DQ-002" | B/8.5 | §8 + APS-001 §7.1 | BROKEN (ref) / **replaced** (content) | APS-300 | **N** | Merkle domain authority | CANONICAL-001, CONF-003 | no |
| spec | `aps/APS-300_EVIDENCE_MODEL.md` | 103 | §5.3 Migration | "retains its original serialization and hash-profile identity (APS-200 §8.8)" | B/8.8 | §8 partial | BROKEN (ref) / **AMBIGUOUS** (content) | APS-300 | **N** | Migration rule now *only* homed in APS-300, below APS-200 | all pre-profile evidence | no |
| spec | `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | 99 | CONF-003 §4.4 | "MUST NOT accept, as a digest input, **any form listed in APS-200 §8.4**" | B/8.4 | none | **BROKEN — unenforceable** | CONF-003 | **C** | **A normative conformance obligation with an empty referent** | CONF-003 verdicts, INV-003, RI-PY/RI-RS gates | **yes — CONF-003 PASS** |
| spec | `closures/DQ-006_CLOSURE_PACKAGE.md` | 55 | §3 hash domain | "Prohibited digest inputs … enumerated in APS-200 §8.4" | B/8.4 | none | BROKEN | closure | **A** | Closure package restates a list it says lives in §8.4 | DQ-006 | no |
| spec | `closures/DQ-006_CLOSURE_PACKAGE.md` | 230 | authority tree | "APS-200 §8 … §8.1–8.9 **NORMATIVE AUTHORITY**" | B/8.1–8.9 | §8 (flat) | BROKEN ×9 | closure | **A** | The closure record's authority node names a structure that no longer exists | DQ-006, GATE A | **yes — authority basis** |
| spec | `closures/DQ-006_CLOSURE_PACKAGE.md` | 281 | criterion 11 | "Version and migration semantics recorded — **MET** — APS-200 §8.8, APS-300 §5.3" | B/8.8 | APS-300 §5.3 only | BROKEN (ref) | closure | **A** | Criterion half-anchored | DQ-006 closure | **yes** |
| spec | `closures/DQ-006_CLOSURE_PACKAGE.md` | 282 | criterion 12 | "Single normative authority; no competing definition — **MET** — APS-200 §8.2" | B/8.2 | assertion in APS-300 §5.1 | BROKEN (ref) | closure | **A** | The declaration that made §8 exclusive is gone from §8 | DQ-006 closure | **yes** |
| spec | `closures/DQ-006_CLOSURE_PACKAGE.md` | 310 | CFL-005 | "Canonicalization determines representation, never event semantics (APS-200 §8.7)" | B/8.7 | none | **BROKEN — content lost** | closure | **A + C** | **CFL-005's entire disposition rests on a deleted rule** | DQ-004, G-3, CANONICAL-001 | **yes** |
| spec | `…/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 42, 50–58, 66, 110 | ADR traceability | 11 constraint→section citations | B/8.1–8.8 | mixed | BROKEN ×11 | ADR | **A** | The ADR's entire "realised normatively in APS-200" mapping | DQ-006 | **yes — line 110 "DONE"** |
| spec | `…/CANONICAL-001_INDEPENDENT_ORACLE.md` | 6 | oracle header | "Hash domain: APS-200 §8.5 / DQ-002" | B/8.5 | §8 + APS-001 §7.1 | BROKEN (ref) / replaced | evidence | **A + F** | Oracle's domain anchor | CANONICAL-001, CROSS-LANGUAGE-001 | no — result is byte-level |
| spec | `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 28 | row 1 | "`APS-200_…md` §8.1–§8.9 … **Amended.** … Declared the single normative authority." | B/8.1–8.9 | §8 (flat) | BROKEN ×9 | scan | **A** | The scan's own subject row is now false | DQ-006 reconciliation | **yes** |
| spec | `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 32, 94 | rows 5, authority table | "APS-200 §8.5 **now attributes** the domain model back to APS-001 §7.1" | B/8.5 | absent | **BROKEN — assertion false** | scan | **A** | Attribution sentence deleted; the scan asserts it exists | APS-001 §7.1 authority chain | **yes** |
| spec | `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 95 | authority table | "APS-200 §8.5 **defers to** [APS-300 §5.1]" | B/8.5 | absent | **BROKEN — assertion false** | scan | **A** | Deferral sentence deleted | APS-300 §5.1 | **yes** |
| spec | `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 110 | non-regression | "DQ-002 — **PASS** — APS-200 §8.5 binds the input byte domain only" | B/8.5 | §8 + APS-001 §7.1 | BROKEN (ref) / replaced | scan | **A + C** | DQ-002 non-regression | DQ-002 | **yes** |
| spec | `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 55, 56, 57 | rows 28–30 | CFL-005 / DQ-004 / DQ-003 dispositions "consistent with §8.7" | B/8.7 | none | **BROKEN — content lost** | scan | **A + C** | Three dispositions unanchored | DQ-003, DQ-004 | **yes** |
| spec | `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 108 | non-regression | "**DQ-003** … **PASS** — APS-200 §8.7 excludes version semantics" | B/8.7 | none | **BROKEN — content lost** | scan | **A + C** | **DQ-003 non-regression PASS has no surviving basis** | DQ-003, C4 | **yes — critical** |
| spec | `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 109 | non-regression | "**DQ-004** … **PASS** — APS-200 §8.7 excludes event semantics" | B/8.7 | none | **BROKEN — content lost** | scan | **A + C** | **DQ-004 non-regression PASS has no surviving basis** | DQ-004, G-3, C4 | **yes — critical** |
| spec | `CHANGELOG.md` | 26 | changelog | describes §8 as binding cross-impl identity + scope boundary | B/8.6, 8.7 | absent | AMBIGUOUS | changelog | **D + A** | Public record of a state that was reverted | release notes | no |
| spec | `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | 31 | fixture | `"normative_authority": "APS-200 §8"` | §8 top | §8 | **CURRENT** | fixture | **F** | Fixture anchor intact | CANONICAL-001, CROSS-LANGUAGE-001 | no — **not modified** |
| spec | `invariants/INVARIANT_REGISTRY.md` | 54 | INV-003 | "Related APS: APS-200 §8" | §8 top | §8 | **CURRENT** | registry | **N + C** | INV-003 anchor intact | CONF-003 | no |
| spec | `specification/APS-001_PROTOCOL_SPECIFICATION.md` | 202–203 | Appendix A | "the canonical serialization profile itself is closed: APS-200 §8 binds…" | §8 top | §8 | **CURRENT** | spec (**above** APS-200) | **N** | APS-001 closure dependency intact | APS-001 v1.0 | yes — but resolves |
| RI-PY | `aura-poc-a-core-v3.3/**` | — | — | **no `§8.x` reference** | — | — | — | — | **I** | **none** | — | no |
| RI-RS | `aura-guard-v1.3/tests/hash_domains.rs` | 697 | disclaimer | "No relationship is claimed … APS-200 `integrity_hash`…" | — | — | **CURRENT** (disclaimer) | test | **I + T** | **none** | — | no |
| — | `cargo`, `.github` | — | — | no `APS-200` occurrence | — | — | — | — | — | **none** | — | no |

**Implementation blast radius = zero.** Neither reference implementation depends on the
lost material at source level. The damage is entirely in the specification and closure
corpus.

---

## 9. Closure / Verification Dependency Audit

Each claim is triaged on the mandated four-way axis:

- **(A)** cryptographic/technical result remains valid
- **(B)** normative anchor is missing
- **(C)** closure evidence requires reconciliation
- **(D)** closure is actually contradicted

| Artifact | Claim | §8.x dependency | Still provable? | Triage | Reason |
|---|---|---|---|---|---|
| `closures/DQ-006_CLOSURE_PACKAGE.md:271` | criterion 1 "Normative canonical serialization rule exists" — **MET** | §8 top level | **YES** | **A** | Current §8 binds RFC 8785 + UTF-8 + digest/leaf domains. Claim resolves. |
| `closures/DQ-006_CLOSURE_PACKAGE.md:274` | criterion 4 "byte-level cross-implementation equality" — **MET** — CONF-003 §4.2, §5 | none (cites CONF-003) | **YES** | **A** | Anchored in CONF-003, not §8.x. |
| `closures/DQ-006_CLOSURE_PACKAGE.md:281` | criterion 11 "Version and migration semantics recorded" — **MET** — §8.8, APS-300 §5.3 | **§8.8** | **PARTIALLY** | **B + C** | APS-300 §5.3 carries the rule but sits **below** APS-200 and is scoped to Evidence. The APS-200 half of the citation is empty. |
| `closures/DQ-006_CLOSURE_PACKAGE.md:282` | criterion 12 "Single normative authority; no competing definition" — **MET** — §8.2 | **§8.2** | **NO, as cited** | **B + C** | The exclusivity declaration lived in §8.2 and was deleted. It now exists only as APS-300 §5.1's assertion *about* APS-200 — a lower-authority document asserting a higher one's exclusivity. |
| `closures/DQ-006_CLOSURE_PACKAGE.md:230` | authority tree "§8.1–8.9 NORMATIVE AUTHORITY" | **§8.1–§8.9** | **NO** | **B** | Named structure does not exist. |
| `closures/DQ-006_CLOSURE_PACKAGE.md:310` | **CFL-005** disposition: "DQ-006 does not repair this … (APS-200 §8.7)" | **§8.7** | **NO** | **B + C** | The scope-boundary rule that justified deferring CFL-005 to DQ-004 is gone with no replacement. |
| `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md:108` | **DQ-003 non-regression — PASS** | **§8.7** | **NO** | **B + C** | Only basis given is §8.7. Independently, `protocol_version`/`schema_version` remain distinct in current §4 — so the *fact* holds; the *stated reason* does not. |
| `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md:109` | **DQ-004 non-regression — PASS** | **§8.7** | **NO** | **B + C** | Same. The registry deferral in §9 (current) can substitute, but that is a **different** anchor and a Custodian call. |
| `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md:110` | **DQ-002 non-regression — PASS** | §8.5 | **YES** | **A + B** | Domain model survives in APS-001 §7.1 (higher rank) and current §8. Reference broken, substance intact. |
| `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md:32, 94, 95` | "§8.5 now attributes … back to APS-001 §7.1" / "defers to APS-300 §5.1" | §8.5 | **NO** | **D** | **These are the only findings where the record is *contradicted*, not merely unanchored:** the current §8 makes neither attribution. The scan asserts a textual fact that is false. |
| `…/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md:28` | row 1 "**Amended** … Declared the single normative authority" over `§8.1–§8.9` | §8.1–§8.9 | **NO** | **D** | The scan's subject row describes a document state that was reverted 22 h later. |
| `…/ADR-CK003-DQ006:106` | "APS-200 §8 updated to bind the profile — **DONE**" | §8 top | **YES** | **A** | Resolves. |
| `…/ADR-CK003-DQ006:110` | "Version/migration semantics documented — **DONE** — §8.8, APS-300 §5.3" | **§8.8** | **PARTIALLY** | **B + C** | As criterion 11. |
| `…/ADR-CK003-DQ006:48–58` | "Each is realised normatively in APS-200 §8" (9 numbered constraints) | §8.1–§8.8 | **PARTIALLY** | **B + C** | 5 of 9 realisable via current §8 / RFC 8785 / APS-001 §7.1; constraints 5 (§8.2(1)), 8 (§8.1) and 9 (§8.7) have **no** normative realisation. |
| `conformance/CONF-003:99` | "MUST NOT accept … any form listed in APS-200 §8.4" | **§8.4** | **NO** | **B + C** | **The most severe finding.** A conformance MUST NOT with an empty enumeration cannot be executed, passed or failed as written. |
| `conformance/CONF-003:8, 17, 21, 28, 160` | "Normative source: APS-200 §8" | §8 top | **YES** | **A** | Resolve. |
| `aps/APS-300:75` | "APS-200 §8 is the **sole normative authority**" | §8 top | **YES (as an assertion)** | **A + B** | Statement resolves to an existing section; but it is APS-300 asserting APS-200's exclusivity, which §8 no longer declares itself. |
| `specification/APS-001:202–203` | "the canonical serialization profile itself is **closed**" | §8 top | **YES** | **A** | Resolves against current §8. |
| `ck003/gates/GATE_A_APS001_CLOSURE_MATRIX.md:22` | "APS-200 §8 reconciliation on this branch … INCORPORATION IN REVIEW" | §8 top | n/a | **A** | Dated; the incorporation did land (as the flat draft). HISTORICAL. |
| `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | CANONICAL-001 bytes / SHA-256 / leaf | none | **YES** | **A** | Byte-level results are independent of §8 prose. **CROSS-LANGUAGE-001 PASS is unaffected.** |

**Summary.** No cryptographic or executed result is invalidated. Eleven closure or
non-regression claims lose or weaken their normative anchor (**B/C**); four assertions
in the consistency scan are **contradicted (D)** by the current text. The two claims that
matter most for the gate are `SCAN:108` (DQ-003) and `SCAN:109` (DQ-004).

---

## 10. G-3 Interaction

Mapping only. **G-3 is not resolved, and no event token is registered by this audit.**

| Question | Finding | Evidence |
|---|---|---|
| **1. Does G-3 depend on lost §8.x content?** | **YES — on §8.7.** The disposition that canonicalization never governs event vocabulary (hence CFL-005 belongs to DQ-004, not DQ-006) is anchored **only** to §8.7 in `CLOSURE_PACKAGE:310`, `SCAN:55`, `SCAN:56` and `SCAN:109`. §8.7 is NORMATIVE CONTENT LOSS. | §4 matrix; §9 audit |
| **2. Does G-3 depend on §9 content?** | **YES — and that anchor is intact and NEW.** Current §9 ¶2: "The event-type vocabulary and validation contract are governed by `aps/EVENT_TYPE_REGISTRY.md`. That registry MUST be incorporated into the approved APS-200 profile before DQ-004 can be closed." **This sentence did not exist at `ff30e16`** (§9 was a bare TODO). It arrived from the branch draft `b9311d0` via the same merge that destroyed §8.1–§8.9. | `git show ff30e16:…` §9 vs `git show b9311d0:…` §9 |
| **3. Is the current registry rule validly anchored?** | **YES.** APS-200 §9 ¶2 (rank APS-200) states the incorporation obligation; `EVENT_TYPE_REGISTRY.md` §7 defers back ("`event_type` participates in canonical object serialization exactly as defined by APS-200's approved serialization profile"). The registry's own status remains **DRAFT — DQ-004 closure artifact**, and §5 states "**No individual event token is promoted to final normative status by this document yet**", with §3 requiring `unknown token → REJECT in strict conformance mode`. The anchor is valid; the vocabulary is empty by design. | `aps/EVENT_TYPE_REGISTRY.md` §§3, 5, 7; `aps/APS-200…md:276` |
| **4. Does CANONICAL-001 depend on the missing material?** | **Split.** Its *bytes, SHA-256 and leaf digest* depend on nothing in §8.x — the fixture cites only `"normative_authority": "APS-200 §8"` (CURRENT). Its *closure disposition* does: the fixture carries `event_type: "AUDIT_RECORD"`, unregistered, and the reason it is not a DQ-006 defect is §8.7. | `fixtures/corpus/CANONICAL-001_jcs_evidence.json:31`; `CLOSURE_PACKAGE:310` |
| **5. Does RI-RS CANONICAL-001 depend on the same material?** | **NO.** `aura-guard-v1.3` contains no APS-200 section reference at all — only a disclaimer at `tests/hash_domains.rs:697`. The RI-RS result is byte-level and structurally independent. | `git grep 'APS-200' aura-guard-v1.3` |

**Net effect on G-3:** the §8.x loss removes G-3's *exclusion* anchor (§8.7) while the
same merge supplied its *incorporation* anchor (§9). G-3 remains **OPEN / CUSTODIAN
INPUT**, unchanged in status, with its dependency structure now precisely mapped.

---

## 11. G-5 / G-6 / G-9 Interaction

Status is **not altered** for any of these. Only dependency on the §8.x loss is assessed.

| Finding | Subject | Location of substance | Dependency on §8.x loss | Evidence |
|---|---|---|---|---|
| **G-5** | Session semantics — scope of `sequence_number` monotonicity | The **only** occurrence of "session" in the entire normative corpus (`aps/`, `specification/`, `conformance/`, `invariants/`) is `APS-200:159`, inside **§5** ENT-007. | **INDEPENDENT** | §5 was untouched by `7826db9`/`9682cf5`; the merge diff is confined to §4 and §8. G-5 was under-specified before the loss and is equally under-specified after it. |
| **G-6** | Chain link `record[n].audit_record_hash → record[n+1].previous_record_hash` | On `main`, only `previous_record_hash` at `APS-200:160`, inside **§5**. `audit_record_hash` and the §5.2 diagram exist **only** on the DQ-003 branches (`8d3f1fe` onward). | **INDEPENDENT** | The artifact G-6 concerns is not on `main` at all and is unrelated to §8. |
| **G-9** | Unicode normalization | **No Unicode-normalization rule existed in §8.1–§8.9 either.** Historical §8.3 covered *escaping* (raw UTF-8 vs `\uXXXX`), not NFC/NFKC. RFC 8785 does not mandate a normalization form. Token-level prohibitions live in `EVENT_TYPE_REGISTRY:71` and `DQ-004_EVENT_TYPE_SEMANTICS:38`. | **INDEPENDENT on substance; PARTIALLY DEPENDENT on reference** | The loss removes no normalization rule, so G-9's CLOSED status is **not** disturbed. One reference-level effect: `SPEC-002:406` REQ-002-011 ("Explicit normalization rules") points its Section column at APS-200 **§8**, and the nearest thing §8 ever offered — the §8.3 properties table — is now weaker. SPEC-002 is `v0.3-DRAFT`, "Normative effect: NONE until APPROVED", so no approved requirement is disturbed. |

**No previously closed finding is reopened by this audit.**

---

## 12. Normative Content Loss Findings

### 12.1 The mandated three-way damage split

| Damage type | Definition applied | Items |
|---|---|---|
| **1. REFERENCE LOSS** | The numbered target no longer exists; the rule may or may not survive. | **All 49 §8.x citations**, across 6 files |
| **2. NORMATIVE CONTENT LOSS** | The historical rule exists nowhere authoritative. | **§8.1**, **§8.4**, **§8.7** — plus the §8.2(1) ordering constraint and the §8.3 anti-redefinition precedence clause |
| **3. NORMATIVE REPLACEMENT** | The rule disappeared from §8.x but an authoritative equivalent is provable. | **§8.5** (APS-001 §7.1, higher rank) · **§8.9** (current §8, equal rank) · §8.8's evidence clause (APS-300 §5.3, **lower** rank) · §8.6's requirement (APS-001:139, higher rank, **narrower** scope) · §8.3's RFC-fixed properties (RFC 8785 by incorporation) |

### 12.2 The three unrecoverable rules — replacement search results

For each, the mandated question was asked: *can an authoritative replacement be proven?*

**§8.1 — Transport representations.** Searched `aps/`, `specification/`, `conformance/`,
`invariants/` for `CBOR`, `Protocol Buffers`, `transport format`, `transport representation`,
`wire encoding`. Result: **no normative hit**. The only matches are
`ADR-CK003-DQ006:62` (past-tense history) and `02_hash_domain_adr:68` (about hex
presentation of digests, unrelated). The rules that no implementation may now rely on:
transport-format permission, the round-trip obligation, and "a transport representation
is never itself the canonical representation".
→ **NORMATIVE CONTENT LOSS — CUSTODIAN DECISION REQUIRED.**

**§8.4 — Prohibited digest inputs.** One of six items (hex-as-digest-input) survives at
APS-300 §5.1 and APS-001 §7.1. Five do not: pretty-printed/indented JSON;
implementation-specific or parser-preserving serialization; a JSON string containing an
escaped copy of `canonical_bytes`; Base64 or other textual encoding of `canonical_bytes`;
a language-specific debug/`repr` form. Rank-6 partial restatements exist
(`APS-300-RECONCILIATION:12`, `ADR-CK003-DQ006:29`, `02_hash_domain_adr:42`) but cannot
carry an APS-200-rank MUST NOT. **`CONF-003:99` is inoperative as written.**
→ **NORMATIVE CONTENT LOSS — CUSTODIAN DECISION REQUIRED.**

**§8.7 — Scope boundary.** Searched for `representation only`, `determines representation`,
`scope boundary`, `excludes event semantics`, `excludes version semantics`. Every hit is a
*citation of* §8.7, never a restatement. `EVENT_TYPE_REGISTRY §7` defers **to** APS-200
but does not assert the converse exclusion. Lost: the explicit statement that
canonicalization does not define event semantics, version semantics, object identity,
entity schemas, or Merkle construction beyond the stated domains.
→ **NORMATIVE CONTENT LOSS — CUSTODIAN DECISION REQUIRED.**

**No replacement text is proposed. No subsection number is assigned. No semantics are
inferred from RI-PY, RI-RS or the Golden Fixture.** Implementation behaviour is recorded
in §8 above solely as implementation evidence and carries no normative weight.

### 12.3 Conflict with the previously delivered G-1 report

Per the mandate, this is reported rather than silently reconciled. **Neither conflict
changes the G-1 verdict (CLOSED); both change the mechanism narrative.**

| # | PREVIOUS FINDING (G-1 §11.3) | NEW EVIDENCE | CONFLICT | REQUIRED CUSTODIAN DECISION |
|---|---|---|---|---|
| **C-1** | "`9682cf5` is AMBIGUOUS — a **deliberate rewrite** of §8's prose whose structural consequence was evidently not analysed." | `9682cf5` is the squash-*landing* of merge `7826db9`, whose §8 is **byte-identical to its stale branch parent** (+3/−1, §4 only) and differs from its main parent by −84 lines. The surviving flat §8 (`b9311d0`, 19:57 +0200) **predates** §8.1–§8.9 (`a0df11a`, 22:12 +0200). | "Deliberate rewrite" vs **stale-branch merge overwrite**. The current §8 is not a refinement of §8.1–§8.9; it is an earlier draft that displaced it. | Whether the §8.1–§8.9 content was ever *rejected* on the merits, or only *lost*. Nothing in the repository records a rejection. |
| **C-2** | G-1 §10.2 content table: §8.6 "**ABSENT as a requirement**"; §8.3 "PARTIAL"; §8.5 "PARTIAL"; §8.9 "PRESENT in substance". | Applying the seven-way equivalence test: §8.6's MUST survives at `APS-001:139` — **higher** rank, narrower scope (shared fixtures) → AMBIGUOUS, not absent. §8.3's RFC-fixed properties survive by incorporation of RFC 8785 → AMBIGUOUS, with only the precedence clause lost. §8.5 and §8.9 meet the full test → **NORMATIVE REPLACEMENT**, not PARTIAL. | G-1 under-credited three replacements and over-credited none. The count of genuinely unrecoverable rules falls from an implied four (§8.1, §8.4, §8.6, §8.7) to **three (§8.1, §8.4, §8.7)**. | Confirm the narrower blast radius before scoping repair. |

Two G-1 statements are **reconfirmed unchanged**: §8.1–§8.9 did exist on `main` at
`ff30e16` (not "subsections that never existed"), and the `bf33eb4` §6–§10 deletion is a
separate, confined regression on the DQ-003 branches.

### 12.4 G-1c reconfirmed (not expanded)

`invariants/INVARIANT_REGISTRY.md:140` and `compliance/TRACEABILITY_MATRIX.md:26` cite
**APS-200 §9** as the authority for INV-009 *Version Consistency*. §9 is "JSON Schema" —
at `ff30e16`, at `9682cf5` and today. The authoritative source
`APS-200 — Canonical Data Model_260723_192852.txt:134` has §9 = **"Compatibility"**
(semantic versioning of the data model), which is what INV-009 needs. The markdown
substitution predates every event in this audit — it originates at `b68181e`
(2026-07-23) — and is therefore **not** caused by the §8.x loss.
**AMBIGUOUS / CUSTODIAN INPUT.** Unchanged, not expanded, not repaired.

---

## 13. Custodian Decision Matrix

| Finding | Status | Byte-bearing? | Normative? | Evidence | Blast radius | Custodian action | C4 impact |
|---|---|---|---|---|---|---|---|
| **G-1** | **CLOSED** | No | Yes | §6–§10 present, byte-identical to `origin/main`; 0 broken top-level refs (G-1 audit §5–§9) | none outstanding | none | none |
| **G-1b** | **OPEN / CUSTODIAN INPUT** | **No** | **Yes** | This audit §3–§9. 49 broken refs; 3 rules unrecoverable | APS-300, CONF-003, DQ-006 closure, consistency scan, ADR, oracle, CHANGELOG | **D-1 … D-5** below | **BLOCK** |
| **G-1c** | **OPEN / CUSTODIAN INPUT** | No | Yes | §12.4; source `.txt:134` vs markdown §9 | INV-009, TRACEABILITY_MATRIX | **D-6** | BLOCK (minor) |
| **G-3** | **OPEN / CUSTODIAN INPUT** | No | Yes | §10. Registry DRAFT; §5 registers no token; exclusion anchor §8.7 lost; incorporation anchor §9 intact | DQ-004, CFL-005, CANONICAL-001 disposition | **D-7** (unchanged scope) | **BLOCK** |
| **G-5** | **OPEN** (unchanged) | No | Yes | §11 — sole occurrence is `APS-200:159`, §5 | ENT-007 replay/verification boundary | unchanged | BLOCK |
| **G-6** | **OPEN** (unchanged) | No | Documentation | §11 — artifact lives only on DQ-003 branches | ENT-007 chain diagram | unchanged | no direct block |
| **G-9** | **CLOSED** (unchanged) | Potentially | Yes | §11 — no normalization rule existed in §8.x | `SPEC-002:406` pointer weakened (draft, normative effect NONE) | none | none |
| **G-1b-R** *(new, reported only)* | **OPEN / CUSTODIAN INPUT** | No | Yes | §5.4 — the merge that destroyed §8.1–§8.9 **created** the §9 registry rule G-3 depends on | any blanket revert to `ff30e16` would delete G-3's anchor and re-introduce the §9 TODO | **D-2** must be answered before any revert-shaped repair | **BLOCK** |

### 13.1 Decisions required

| # | Decision | Depends on | Why it cannot be inferred |
|---|---|---|---|
| **D-1** | **Was §8.1–§8.9 ever rejected on the merits, or only lost?** The repository contains no rejection record and the surviving text is the older draft. | §5.2, §12.3 C-1 | Intent is not recoverable from git. Only the Custodian can state it. |
| **D-2** | **§8 target structure**: (A) keep flat §8 and migrate all 49 citations to semantic anchors; (B) reinstate Scheme B §8.1–§8.9 from `ff30e16`; (C) a new structure with an explicit citation migration. **Any revert-shaped option must preserve the current §9 registry rule** (§5.4). | D-1, §4, §5.4 | Normative structuring decision. |
| **D-3** | **§8.1 transport representations** — still normative, repealed, or relocated? Nothing in the corpus states any of the three. | §12.2 | No authoritative text exists to read. |
| **D-4** | **§8.4 prohibited digest inputs** — the enumeration must exist somewhere at APS-200 rank or `CONF-003:99` must be re-scoped. **`CONF-003` cannot be executed as written until this is answered.** | §12.2, §9 | A conformance MUST NOT with an empty referent is not testable. |
| **D-5** | **§8.7 scope boundary** — restate, relocate, or repeal. Four closure dispositions (CFL-005, DQ-003, DQ-004 non-regression, SCAN rows 55–57) currently rest on it. | §12.2, §9, §10 | The rule exists nowhere; inferring it from citations would be reconstruction. |
| **D-5b** | **Re-affirm or re-open** DQ-006 criteria 11 & 12, the DQ-003/DQ-004 non-regression PASS verdicts, and the four contradicted scan assertions (`SCAN:28, 32, 94, 95`). | §9 | Re-recording a closure verdict is a Custodian act. |
| **D-6** | **APS-200 §9** — was the source's "Compatibility" deliberately replaced by "JSON Schema"? If deliberate, INV-009 needs a new target. | §12.4 | Requires intent, not text. |
| **D-7** | **G-3 / G-5 / G-6** unchanged: event vocabulary; session lifecycle; chain-link diagram. | §10, §11 | Out of scope for this audit by mandate. |

---

## 14. C4 Impact

```text
C4 AUTHORIZATION GATE
        │
        ├── G-1   CLOSED ......................... does not block
        ├── G-1b  OPEN — 3 unrecoverable rules ... BLOCKS
        │     └── CONF-003:99 inoperative ........ BLOCKS conformance execution
        │     └── DQ-003 / DQ-004 non-regression
        │         PASS verdicts unanchored ....... BLOCKS closure reliance
        ├── G-1b-R OPEN — revert would delete
        │         G-3's §9 anchor ................ BLOCKS naive repair
        ├── G-1c  OPEN ........................... BLOCKS (minor)
        ├── G-3   OPEN ........................... BLOCKS
        ├── G-5   OPEN ........................... BLOCKS
        ├── G-6   OPEN ........................... no direct block
        └── G-9   CLOSED ......................... does not block
                        │
                        ▼
             C4 = NOT AUTHORIZED
```

Specifically for C4: **CONF-003 cannot be executed to a defensible PASS** while
`CONF-003:99` requires rejection of "any form listed in APS-200 §8.4" and no such list
exists. That is a hard blocker independent of every other finding.

**No cryptographic result is invalidated.** CANONICAL-001 bytes, SHA-256 digests, RFC 6962
leaf digests and CROSS-LANGUAGE-001 equality remain valid — they never depended on §8
prose. The blockage is normative-anchor integrity, not arithmetic.

---

## 15. Recovery Verdict

```text
SPECIFICATION RECOVERY STATUS:  READY FOR RECONCILIATION

    Historical truth ......................... ESTABLISHED
      §8.1–§8.9 existed on main at ff30e16 (Scheme B), verbatim text recovered
      Competing Scheme A (704832a) identified and excluded as non-referent
      Loss mechanism proven: merge 7826db9 took the stale branch side;
      squash 9682cf5 landed it on main; no deprecation record exists
      Surviving §8 is the OLDER draft (b9311d0), not a refinement

    Reference integrity ...................... MAPPED
      129 explicit refs / 108 sites / 31 files; 49 §8.x refs BROKEN in 6 files
      Semantic dependencies enumerated separately (§6.4)

    Normative equivalence .................... TESTED
      NORMATIVE REPLACEMENT ....... §8.5, §8.9
      AMBIGUOUS ................... §8.2, §8.3, §8.6, §8.8
      NORMATIVE CONTENT LOSS ...... §8.1, §8.4, §8.7

    Blast radius ............................. ASSESSED
      Specification + closure corpus: 6 files, 11 weakened claims,
        4 contradicted assertions
      Implementation (RI-PY / RI-RS / cargo / .github): ZERO dependency
      Cryptographic evidence: UNAFFECTED

    Custodian decision ....................... PENDING — D-1 … D-7
```

**No additional historical evidence is required.** Every question in the mandate is
answered from primary git objects. What remains is a decision, not an investigation.

```text
C4 AUTHORIZATION:  NOT AUTHORIZED
DQ-003:            OPEN
IMPLEMENTATION:    NO-GO — no separate authorization exists or is sought
G-1:               CLOSED (unchanged)
G-1b:              OPEN / CUSTODIAN INPUT REQUIRED
G-1c:              OPEN / CUSTODIAN INPUT REQUIRED
G-3:               OPEN / CUSTODIAN INPUT REQUIRED (unchanged)
G-5:               OPEN (unchanged) — INDEPENDENT of the §8.x loss
G-6:               OPEN (unchanged) — INDEPENDENT of the §8.x loss
G-9:               CLOSED (unchanged) — INDEPENDENT on substance
```

---

## 16. Evidence Appendix

Every command below was executed in this session against
`aura-specification` on `claude/aps-200-spec-recovery-b7wc2h`.
`$F = aps/APS-200_CANONICAL_DATA_MODEL.md`.

### E-1 — Structural census across all refs

```console
$ git log --all --reverse --format='%H' -- $F | while read h; do
    echo "$(echo $h|cut -c1-7) blob=$(git rev-parse $h:$F|cut -c1-7)" \
         "8.x=$(git show $h:$F|grep -cE '^#{3} *8\.[0-9]')" \
         "L=$(git show $h:$F|wc -l)"; done
b68181e blob=c974f59 8.x=0 L=243
704832a blob=7ab340a 8.x=7 L=447
b9311d0 blob=091e331 8.x=0 L=289
a0df11a blob=5f3ea8b 8.x=9 L=336
ff30e16 blob=5f3ea8b 8.x=9 L=336
7826db9 blob=0488eec 8.x=0 L=291
9682cf5 blob=0488eec 8.x=0 L=291
8d3f1fe blob=191adb7 8.x=0 L=389
bf33eb4 blob=fc1b58e 8.x=0 L=353
e109cff blob=4d10ff5 8.x=0 L=398
```

### E-2 — The merge that decided it

```console
$ git log -1 --format='%H%nparents: %P%n%s' 7826db9
7826db9e3e28d356693ba24618f320c44e3120b1
parents: e71ca3edfb2a4b94c891e079962491521441501b 57a0a60f0df6d9d95bd661f68d87d05ae4c0dc1c
Merge branch 'main' into ck003/specification-integration-dq006

$ git diff --stat e71ca3e 7826db9 -- $F        # branch-side parent
 aps/APS-200_CANONICAL_DATA_MODEL.md | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)

$ git diff --stat 57a0a60 7826db9 -- $F        # main-side parent (had 8.1-8.9)
 aps/APS-200_CANONICAL_DATA_MODEL.md | 123 +++++++------------
 1 file changed, 39 insertions(+), 84 deletions(-)

$ git merge-base --is-ancestor ff30e16 57a0a60 && echo "ff30e16 reachable from main side"
ff30e16 reachable from main side
$ git merge-base --is-ancestor ff30e16 e71ca3e || echo "ff30e16 NOT reachable from branch side"
ff30e16 NOT reachable from branch side
```

The only content the merge added over its branch parent:

```diff
-| `integrity_hash` | string | MUST | SHA-256 hash of the canonical serialization of this object |
+| `integrity_hash` | string | MUST | `SHA-256(canonical_bytes)` of this object, excluding `integrity_hash` itself. Canonical bytes are defined by §8. |
+
+> **Note on self-reference.** A digest field cannot cover its own value. …
```

§8 does not appear in that diff.

### E-3 — Atomicity broken

```console
$ git show --stat --format='' ff30e16 | tail -1
 24 files changed, 849 insertions(+), 166 deletions(-)
$ git show --name-only --format='' 9682cf5
aps/APS-200_CANONICAL_DATA_MODEL.md
ck003/APS001_INV_MATRIX/INV-001_015_CONFORMANCE_MATRIX.md
ck003/audit/2026-08-20_ARCHITECTURE_EXECUTION_AUDIT.md
ck003/gates/GATE_A_APS001_CLOSURE_MATRIX.md
```

Citing artifacts touched by `9682cf5`: **none**.

### E-4 — Historical §8 structure and digests

```console
$ git show ff30e16:$F | grep -nE '^#{2,3} *(8|8\.[0-9]|9)\.'
213:## 8. Serialization Requirements
215:### 8.1 Transport representations
224:### 8.2 Canonical serialization profile
237:### 8.3 Properties fixed by the profile
251:### 8.4 Prohibited digest inputs
262:### 8.5 Hash and Merkle domains
280:### 8.6 Cross-implementation requirement
284:### 8.7 Scope boundary
294:### 8.8 Compatibility and migration
300:### 8.9 Reference engines (informative)
315:## 9. JSON Schema

ff30e16     §8 block  5459 B  sha256 e3f4f19f68b8e7890298672b7dbf345949c6f169bdd7e26a350c592e76e3a43b
origin/main §8 block  2763 B  sha256 12c1a825c6fa3dbb2fbb8439f20e66678052ac31d110e283eea7e5b6e9429c39
```

### E-5 — Scheme A was never a referent

```console
$ git merge-base --is-ancestor 704832a origin/main || echo "704832a NOT an ancestor of main"
704832a NOT an ancestor of main
$ git show 704832a:$F | grep -nE '^### 8\.[0-9]'
224:### 8.1 Canonical serialization profile
260:### 8.2 Canonicalization input domain
298:### 8.3 Delegated rules
331:### 8.4 Hash domain
364:### 8.5 Alternate wire encodings
378:### 8.6 Version binding
401:### 8.7 Conformance
```

### E-6 — Reference inventory (audit family excluded)

```console
EXPLICIT reference occurrences: 129  sites: 108  files: 31
  §6: 0   §7: 0   §8: 75   §9: 5   §10: 0
  §8.1: 3  §8.2: 5  §8.3: 6  §8.4: 6  §8.5: 10
  §8.6: 2  §8.7: 9  §8.8: 6  §8.9: 2      §8.x subtotal: 49

$ for d in aura-specification aura-poc-a-core-v3.3 aura-guard-v1.3 cargo .github; do
    git -C $d grep -n -I -E '§+ ?8\.[0-9]' -- . ; done | grep -v conformance/canonical | wc -l
33          # 33 citation lines -> 49 targets after range expansion
```

### E-7 — Replacement proofs

```console
$ grep -n 'byte-identical canonical bytes' specification/APS-001_PROTOCOL_SPECIFICATION.md
139:Where multiple implementations support the same canonical object, they MUST produce
    byte-identical canonical bytes and digest-identical cryptographic outputs for shared fixtures.

$ sed -n '/^### 7.1 Canonical hash-domain model/,/^### 7.2/p' specification/APS-001_PROTOCOL_SPECIFICATION.md
… leaf ──► SHA-256(0x00 || bytes) … node ──► SHA-256(0x01 || left[32] || right[32]) …
Hash inputs are raw bytes; hexadecimal strings are presentation values and MUST NOT
substitute for underlying digest bytes.
The serialization profile producing `canonical bytes` is owned by APS-200. …

$ sed -n '/^### 5.3 Migration/,+3p' aps/APS-300_EVIDENCE_MODEL.md
Evidence generated before APS-200 §8 bound the canonical serialization profile retains its
original serialization and hash-profile identity (APS-200 §8.8). Such evidence MUST NOT be
silently reinterpreted … and MUST NOT be compared for equality … without an explicit,
version-bound migration record.
```

Failed replacement searches (empty results are the evidence):

```console
$ grep -rn -iE 'CBOR|Protocol Buffers' --include='*.md' aps/ specification/ conformance/ invariants/
                                                     # (no output)  -> §8.1 unhomed
$ grep -rn -iE 'representation only|scope boundary|excludes (event|version) semantics' \
    --include='*.md' aps/ specification/ conformance/ invariants/
                                                     # only citations of §8.7, no restatement
```

### E-8 — G-3 §9 provenance

```console
$ git show ff30e16:$F | sed -n '315,318p'
## 9. JSON Schema

> **TODO**: Publish JSON Schema definitions for each entity at a stable URL. …

$ git show b9311d0:$F | sed -n '270,275p'
## 9. JSON Schema

Machine-readable schema definitions … MUST be added before APS-001 v1.0 approval …

The event-type vocabulary and validation contract are governed by `aps/EVENT_TYPE_REGISTRY.md`.
That registry MUST be incorporated into the approved APS-200 profile before DQ-004 can be closed.
```

### E-9 — Implementation independence

```console
$ git -C ../aura-guard-v1.3 grep -n -I -E 'APS-200|§ ?8' -- .
tests/fixtures/hash_domains/INVENTORY.json:191: "No relationship is claimed between these
  constructions and APS-200 integrity_hash, event_payload_hash or previous_record_hash.",
tests/hash_domains.rs:697: (same disclaimer)

$ git -C ../aura-poc-a-core-v3.3 grep -n -I -E '§ ?8\.[0-9]' -- .
                                                     # (no output)
```

### E-10 — Read-only discipline

```console
$ git status --porcelain
?? conformance/canonical/G-1B-HISTORICAL-NORMATIVE-RECOVERY-AUDIT.md
$ git diff --stat
$ sha256sum aps/APS-200_CANONICAL_DATA_MODEL.md
46d2d53d4b6c2095f5d33e08fe0eab477e611a114e02b0dc9d79649a1e1b9a66  aps/APS-200_CANONICAL_DATA_MODEL.md
$ for d in ../aura-poc-a-core-v3.3 ../aura-guard-v1.3 ../cargo ../.github; do
    git -C $d status --porcelain; done
                                                     # (no output — all clean)
```

### E-11 — Environment limitation, declared

`aura-specification` has no CI workflows, no test harness, no linter and no Makefile
(`.github/workflows/` absent; `scripts/` contains only `README.md`). Every result in this
audit was produced by git object inspection, SHA-256 digests over extracted byte ranges,
structural `grep` assertions and the tracked-file reference sweep of §6.1. **No
conformance suite, no RI-PY or RI-RS execution and no CI job was run, and none is
claimed.** No RI behaviour was used as normative evidence anywhere in this document.

---

## 17. Explicit statement of what was NOT done

- **APS-200 not modified** — SHA-256 identical before and after
  (`46d2d53d…9a66`). No section restored, renumbered, retitled or reworded.
- **§8.1–§8.9 not restored, not reconstructed, not proposed.** No replacement text was
  authored for §8.1, §8.4 or §8.7. No new subsection number was assigned.
- **No broken reference repaired.** All 49 remain exactly as found.
- **No specification document modified** — APS-000/001/100/300/400/500/900/950,
  EVENT_TYPE_REGISTRY, SPEC-002, CONF-001…CONF-015, invariant registry, traceability
  matrix, CHANGELOG, ADRs, closure packages: untouched.
- **RI-PY untouched · RI-RS untouched · Aura-Guard untouched · `cargo` untouched.**
- **Golden Fixture and DQ-003 fixture untouched.** No fixture value changed.
  `Cargo.toml`, tests, registry and schemas untouched.
- **No test behaviour changed. No conformance implementation changed.**
- **No history rewritten.** `ff30e16`, `7826db9`, `9682cf5`, `bf33eb4` were read only.
- **No previously closed finding reopened** — G-9 remains CLOSED; G-5 and G-6 remain as
  recorded.
- **G-3 not resolved.** No event token registered; no session semantics defined; no
  error codes authored.
- **No remediation commit.** Exactly one file added: this audit.
- **DQ-003 not closed. C4 not authorized. No implementation performed.**

---

*Produced under the P0 Recovery Gate as a historical forensic audit. Specification
reconciliation input only. This document establishes what the record shows so that the
Protocol Custodian can decide; it does not decide.*

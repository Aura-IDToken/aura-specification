# G-1 — APS-200 §6–§10 Specification Recovery & Reference-Integrity Audit

**Artifact class:** GOVERNANCE / SPECIFICATION RECONCILIATION — non-normative
**Authority rank:** below the Protocol Specification and Protocol Invariants; this document creates no protocol semantics
**Branch:** `claude/aps-200-spec-recovery-b7wc2h`
**Recovery baseline:** `origin/main` @ `8a2706969f65707817486a865af356f2398cf275`
**APS-200 path:** `aps/APS-200_CANONICAL_DATA_MODEL.md`
**Scope:** restoration and reference integrity of APS-200 §6–§10 only
**DQ-003:** OPEN — untouched by this audit
**C4:** NOT AUTHORIZED
**ENT-007 implementation:** NOT PERFORMED

---

## 1. Executive verdict

```text
G-1  = CLOSED  (restoration + top-level reference integrity)
G-1b = OPEN / CUSTODIAN INPUT REQUIRED  (§8.1–§8.9 reference integrity)
G-1c = OPEN / CUSTODIAN INPUT REQUIRED  (NEW — §9 semantic mismatch, see §10.3)
```

**G-1 is CLOSED, but not for the reason the task premise assumed.**

APS-200 §6–§10 are **present and byte-identical to `origin/main`** on the designated
recovery branch. The restore operation was executed mechanically (§4) and produced a
**zero-byte diff**: the branch already carried the authoritative content. No text was
reconstructed, paraphrased or invented.

Every reference to APS-200 **§6, §7, §8 (top level), §9 and §10** resolves against the
restored structure. There are **zero** dangling top-level references.

**G-1b remains OPEN and is NOT merged into G-1.** 50 subsection references to
`§8.1`–`§8.9` do not resolve, because current §8 has no numbered subsections.

**The task's framing of G-1b requires one factual correction, evidenced in §11.3:**
`§8.1`–`§8.9` **did exist** in APS-200 on `origin/main` at commit `ff30e16`, and were
collapsed into a flat §8 by commit `9682cf5` with no deprecation, renumbering or
migration record. They are **not** "references to subsections that never existed."
This distinction is material to the Custodian decision and is recorded here without
any repair being attempted.

---

## 2. Baseline identification

### 2.1 Pre-execution state (recorded before any change)

| Repository | Branch | HEAD | Working tree |
|---|---|---|---|
| `aura-specification` | `claude/aps-200-spec-recovery-b7wc2h` | `8a2706969f65707817486a865af356f2398cf275` | clean |
| `aura-poc-a-core-v3.3` | `claude/aps-200-spec-recovery-b7wc2h` | `64bf959b1d23fbd5433723476c611ab66d423953` | clean |
| `aura-guard-v1.3` | `claude/aps-200-spec-recovery-b7wc2h` | `35082d7b4880dad780fb55a1a5f3ac0ef4322674` | clean |
| `cargo` | `claude/aps-200-spec-recovery-b7wc2h` | `92e3ebecbdf96a52375542ad51b7601009a2574f` | clean |
| `.github` | `claude/aps-200-spec-recovery-b7wc2h` | `95f017a833950d77542ebcf579a8c172f9027173` | clean |

`origin/main` (`aura-specification`) after `git fetch origin main`:
`8a2706969f65707817486a865af356f2398cf275`
— *"chore(dq-003): keep reconciliation control record off main"*, 2026-08-23 01:39 +0200.

**The designated recovery branch HEAD is identical to `origin/main` HEAD.**

### 2.2 Which revision is authoritative — `9682cf5` or `8a27069`?

The task named `origin/main / 9682cf5` as the reported baseline and required repository
inspection to confirm or supersede it. Inspection resolves the question with no conflict:

```
$ git rev-parse 9682cf5:aps/APS-200_CANONICAL_DATA_MODEL.md
0488eec04e102e87b5724ca385a534d0c5f4e1cd
$ git rev-parse origin/main:aps/APS-200_CANONICAL_DATA_MODEL.md
0488eec04e102e87b5724ca385a534d0c5f4e1cd
$ git log --oneline origin/main -- aps/APS-200_CANONICAL_DATA_MODEL.md | head -1
9682cf5 CK-003: reconcile APS-200 with DQ-006 and refresh closure controls (#25)
```

`9682cf5` is the **most recent commit on `main` that touches APS-200**. The two later
commits on `main` (`c069a1b`, `8a27069`) do not modify the file. The APS-200 blob is
therefore identical at `9682cf5`, `c069a1b`, `8a27069`, `origin/main` and branch `HEAD`.

**Both names designate the same authoritative content.** The restore below uses
`origin/main`; using `9682cf5` would produce byte-identical output.

### 2.3 Authoritative APS-200 structure on the baseline

| Section | Title | Present on baseline |
|---|---|---|
| §1 | Purpose | yes |
| §2 | Design Principles | yes |
| §3 | Core Entities | yes |
| §4 | Common Object Contract | yes |
| §5 | Entity Definitions (ENT-001 … ENT-008) | yes |
| **§6** | **Relationships** | **yes** |
| **§7** | **Validation Rules** | **yes** |
| **§8** | **Serialization Requirements** | **yes** (flat; sub-heading `CANONICAL-001 reference vector` only) |
| **§9** | **JSON Schema** | **yes** |
| **§10** | **Traceability** | **yes** |
| §8.1 … §8.9 | — | **NOT PRESENT** |

---

## 3. Pre-restore state

Digests computed over the file as it stood on the branch **before** the restore
operation. The split point is the first byte of the line `## 6. Relationships`
(byte offset 6965); everything before it is "§1–§5", everything from it to EOF is
"§6–§10".

| Region | Bytes | SHA-256 |
|---|---:|---|
| whole file | 11445 | `46d2d53d4b6c2095f5d33e08fe0eab477e611a114e02b0dc9d79649a1e1b9a66` |
| §1–§5 | 6965 | `47ea97b67c06c5a1a8e67c43f84aa760df799ff0db0730370929c88e741f9adf` |
| §6–§10 | 4480 | `74de67d37ce8fcc84d85d03081e2c72e12fc05bf0f5d404b55f252bb3e027c37` |

Cross-revision comparison of the same split:

| Revision | whole SHA-256 | §1–§5 SHA-256 | §6–§10 |
|---|---|---|---|
| `9682cf5` | `46d2d53d…9a66` | `47ea97b6…9adf` | `74de67d3…c37` (4480 B) |
| `origin/main` (`8a27069`) | `46d2d53d…9a66` | `47ea97b6…9adf` | `74de67d3…c37` (4480 B) |
| branch `HEAD` (pre-restore) | `46d2d53d…9a66` | `47ea97b6…9adf` | `74de67d3…c37` (4480 B) |
| `bf33eb4` | `821139f8…a3a3` | (whole file) | **ABSENT (0 B)** |
| `origin/dq/dq-003-audit-record-hash-domain` | `bbcf0b98…4a0b` | (whole file) | **ABSENT (0 B)** |
| `origin/claude/dq-003-conformance-audit-4ok63x` | `bbcf0b98…4a0b` | (whole file) | **ABSENT (0 B)** |

**Finding.** The §6–§10 loss is confined to the DQ-003 lineage
(`bf33eb4` and its descendants on two unmerged branches). It is **not** present on
`main`, and it is **not** present on the designated recovery branch.

---

## 4. Exact restoration performed

The restore was executed as a byte-level splice, not an edit:

1. `§1–§5` was taken verbatim from the branch working tree (untouched region).
2. `§6–§10` was extracted verbatim from `git show origin/main:aps/APS-200_CANONICAL_DATA_MODEL.md`
   at the same split marker.
3. The two byte strings were concatenated and written back to
   `aps/APS-200_CANONICAL_DATA_MODEL.md`.

No reformatting, paraphrase, renumbering, reflow or reconstruction of absent
subsections occurred at any point.

Result:

```text
PRE  whole sha256        : 46d2d53d4b6c2095f5d33e08fe0eab477e611a114e02b0dc9d79649a1e1b9a66
POST whole sha256        : 46d2d53d4b6c2095f5d33e08fe0eab477e611a114e02b0dc9d79649a1e1b9a66
§1-§5  pre == post       : True   (47ea97b67c06c5a1a8e67c43f84aa760df799ff0db0730370929c88e741f9adf)
§6-§10 post == origin/main: True  (74de67d37ce8fcc84d85d03081e2c72e12fc05bf0f5d404b55f252bb3e027c37)
bytes written            : 11445

$ git diff --stat
(empty)
$ git status --porcelain
(empty)
```

**The restore is a verified idempotent no-op on this branch.** The authoritative
§6–§10 content was already in place. This is recorded as an executed, proven
operation — not as a skipped step.

---

## 5. §1–§5 immutability proof

| Check | Result |
|---|---|
| `§1–§5` byte length before / after | 6965 / 6965 |
| `§1–§5` SHA-256 before | `47ea97b67c06c5a1a8e67c43f84aa760df799ff0db0730370929c88e741f9adf` |
| `§1–§5` SHA-256 after | `47ea97b67c06c5a1a8e67c43f84aa760df799ff0db0730370929c88e741f9adf` |
| `current_after == current_before` | **TRUE** |
| Sections renumbered | none |
| `git diff -- aps/APS-200_CANONICAL_DATA_MODEL.md` | empty |

**PASS.** §1–§5 are byte-identical to their pre-execution state.

---

## 6. §6–§10 byte/content comparison

| Check | Result |
|---|---|
| `§6–§10` byte length (branch) | 4480 |
| `§6–§10` byte length (`origin/main`) | 4480 |
| `§6–§10` SHA-256 (branch) | `74de67d37ce8fcc84d85d03081e2c72e12fc05bf0f5d404b55f252bb3e027c37` |
| `§6–§10` SHA-256 (`origin/main`) | `74de67d37ce8fcc84d85d03081e2c72e12fc05bf0f5d404b55f252bb3e027c37` |
| `restored_content == origin_main_content` | **TRUE (byte-for-byte)** |
| Subsections reconstructed | **none** |

**PASS.**

---

## 7. Repository-wide reference inventory

### 7.1 Search scope (exact)

- **Repositories searched (all in-session, all on the designated branch):**
  `aura-specification`, `aura-poc-a-core-v3.3`, `aura-guard-v1.3`, `cargo`, `.github`.
- **File set:** git-tracked files only (`git ls-files` per repository) — 3 517 files total (168 + 179 + 122 + 3 046 + 2).
- **Excluded by extension** (generated/binary/vendor material):
  `.pdf .png .jpg .jpeg .gif .zip .gz .whl .so .bin .ico .woff .woff2 .ttf`.
- **Excluded by content:** any file containing a NUL byte in its first 8 KiB.
- **Excluded implicitly:** files not containing the literal token `APS-200`.
- **Not searched:** `.git` internals; the root-level `APS-*.pdf` binaries. The root-level
  `APS-200 — Canonical Data Model_260723_192852.txt` **is** in the tracked set and was
  inspected directly (see §10.3) although it contains no `§`-form citations.
- **Match rule:** the literal token `APS-200`, followed on the same line by a section
  token naming 6–10 (optionally `.1`–`.9`), in the forms `§N`, `§N.M`, `Section N`,
  or a `/ , and ·`-joined chain such as `§4/§8`, `§8/§9`, `APS-200 §4, §8`. A candidate
  is rejected when another document identifier (`APS-0xx`/`APS-3xx`/`APS-5xx`, `SPEC-`,
  `ADR-`, `CONF-nnn`, `INV-n`, `AURA-CON`, `Article`, `VERSIONING`) intervenes between
  the `APS-200` anchor and the section token, so that e.g.
  `APS-200; APS-300 | §4; §5, §9` does not yield a spurious `APS-200 §9`.
  Additionally, `APS-200_CANONICAL_DATA_MODEL.md §8.x–§8.y` filename-anchored ranges are
  expanded to their individual members.

### 7.2 Totals

| Metric | Count |
|---|---:|
| Reference occurrences (file, line, target) | **129** |
| Distinct citation sites (file, line) | **108** |
| Distinct files containing a reference | **31** |

| Target | Occurrences | Target exists in restored APS-200 |
|---|---:|---|
| §6 | **0** | yes |
| §7 | **0** | yes |
| §8 (top level) | **75** | yes |
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
| **§8.1–§8.9 subtotal** | **49** | — |

> **Correction of record.** The earlier audit
> `ck003/dq-003-specification-reconciliation/APS-200-SECTION-6-10-REFERENCE-AUDIT.md`
> (branch `dq-003/specification-reconciliation`) tabulates references to APS-200 §6, §7
> and §10 in `closures/DQ-006_CLOSURE_PACKAGE.md`, `compliance/TRACEABILITY_MATRIX.md`,
> `invariants/INVARIANT_REGISTRY.md`, `specification/SPEC-002_…md`, `releases/README.md`,
> `ck003/evidence/core-v3.3/CORE_TO_SPEC_TRACEABILITY.md`,
> `ck003/handover-assessment/05_EVIDENCE_GAPS.md`, `06_IMPL_CONFORMANCE_CI_GAPS.md` and
> others. **None of those references exist.** `releases/README.md` and
> `05_EVIDENCE_GAPS.md` contain no occurrence of the string `APS-200` at all. That
> document also carries a `fileciteturn90file0L2-L2` residue in its §6 G-3 paragraph.
> It should be treated as unreliable evidence pending Custodian review. **This audit
> does not modify it** — it lives on a different branch and is outside the change scope.

### 7.3 Full citation inventory

Authority rank uses the CLAUDE.md precedence ladder (2 = Protocol Specification,
3 = Protocol Invariants, 5 = Conformance Matrix / approved Conformance Requirements,
6–9 = governance, evidence and closure material).

#### §8 — Serialization Requirements (top level) — target CURRENT

| File | Line | Ref | Context (abridged) | Artifact class | Rank | Status |
|---|---:|---|---|---|---:|---|
| `aps/APS-300_EVIDENCE_MODEL.md` | 75 | §8 | "canonical bytes as defined by APS-200 §8 … sole normative authority" | normative specification | 2 | CURRENT |
| `aps/APS-300_EVIDENCE_MODEL.md` | 94 | §8 | `canonical_bytes` \| Representation output of APS-200 §8 | normative specification | 2 | CURRENT |
| `aps/APS-300_EVIDENCE_MODEL.md` | 103 | §8 | "before APS-200 §8 bound the canonical serialization profile" | normative specification | 2 | CURRENT |
| `aps/APS-300_EVIDENCE_MODEL.md` | 105 | §8 | Traceability footer | normative specification | 2 | CURRENT |
| `specification/APS-001_PROTOCOL_SPECIFICATION.md` | 202 | §8 | "APS-200 §8 binds RFC 8785 JCS, UTF-8 canonical bytes and the SHA-256 / RFC 6962 domains" | normative specification | 2 | CURRENT |
| `specification/APS-001_PROTOCOL_SPECIFICATION.md` | 203 | §8 | "APS-300 §5.1 binds `evidence_hash` to APS-200 §8 canonical bytes" | normative specification | 2 | CURRENT |
| `specification/SPEC-002_CONSTITUTION_ARTIFACT_CONTRACT.md` | 416 | §8 | REQ-002-021 One canonical serialization format | draft contract (v0.3, normative effect NONE) | 8 | CURRENT |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | 8 | §8 | "Normative source: APS-200 §8" | conformance requirement | 5 | CURRENT |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | 17 | §8 | "exactly one canonical byte representation under APS-200 §8" | conformance requirement | 5 | CURRENT |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | 21 | §8 | "CONF-003 does not define canonical serialization. APS-200 §8 does." | conformance requirement | 5 | CURRENT |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | 28 | §8 | "APS-200 §8: canonical serialization profile (normative authority)" | conformance requirement | 5 | CURRENT |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | 160 | §8 | Normative source table | conformance requirement | 5 | CURRENT |
| `invariants/INVARIANT_REGISTRY.md` | 54 | §8 | INV-003 → Related APS: APS-200 §8 | invariant registry | 3 | CURRENT |
| `compliance/TRACEABILITY_MATRIX.md` | 20 | §8 | Explicit over Implicit \| APS-200 §4, §8 \| INV-003 | traceability matrix | 6 | CURRENT |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 6 | §8 | Authority header | closure package | 6 | CURRENT |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 25 | §8 | "normatively bound in APS-200 §8 and APS-300 §5" | closure package | 6 | CURRENT |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 43 | §8 | "Defined once, in APS-200 §8 … APS-200 §8 governs." | closure package | 6 | CURRENT |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 230 | §8 | Blast-radius tree, NORMATIVE AUTHORITY node | closure package | 6 | CURRENT |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 271 | §8 | Closure criterion 1 — MET | closure package | 6 | CURRENT |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 309 | §8 | CFL-001 — cross-corpus authority | closure package | 6 | CURRENT |
| `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 3, 6, 7, 31, 39, 48, 106 | §8 | ADR status / normative home / related / rule ownership / contract / realisation / checklist | ADR | 6 | CURRENT |
| `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 62 | §8 | "**Before this decision**, APS-200 §8 permitted JSON, CBOR and Protocol Buffers … `TODO`" | ADR | 6 | HISTORICAL (explicitly past-tense; accurate) |
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 30, 32, 36, 48, 50, 51, 52, 54, 61, 65, 93 | §8 | consistency-scan rows citing §8 as authority | consistency scan | 6 | CURRENT |
| `ck003/dq-006-final-closure-execution/DQ-006_FINAL_CLOSURE_EXECUTION_ORDER.md` | 6, 22, 23, 24, 155 | §8 | authority header; SETTLED rows; JCS profile reference | closure execution order | 6 | CURRENT |
| `ck003/README.md` | 28 | §8 | "normative canonical serialization rule lives in APS-200 §8" | index | 9 | CURRENT |
| `ck003/DQ-006_CLOSURE.md` | 5 | §8 | supersession banner | superseded record | 9 | CURRENT (as pointer) |
| `ck003/dq-006-closure/DQ-006-CLOSURE.md` | 5 | §8 | supersession banner | superseded record | 9 | CURRENT (as pointer) |
| `ck003/dq-006-closure/README.md` | 5 | §8 | supersession banner | superseded record | 9 | CURRENT (as pointer) |
| `evidence/DQ-006_CLOSURE_PACKAGE.md` | 5 | §8 | supersession banner | superseded record | 9 | CURRENT (as pointer) |
| `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | 31 | §8 | `"normative_authority": "APS-200 §8"` | **conformance fixture** | 5 | CURRENT |
| `CHANGELOG.md` | 26 | §8 | "APS-200 §8 now binds … **the cross-implementation byte-identity requirement, the scope boundary against event and version semantics**, and migration" | changelog | 9 | **AMBIGUOUS** — see §8.3 |
| `CHANGELOG.md` | 27 | §8 | "APS-300 §5 now binds … to APS-200 §8 canonical bytes" | changelog | 9 | CURRENT |
| `ck003/audit/2026-08-20_ARCHITECTURE_EXECUTION_AUDIT.md` | 70, 81 | §8 | dated execution audit, "§8 was reconciled" | dated audit | 9 | HISTORICAL |
| `ck003/gates/GATE_A_APS001_CLOSURE_MATRIX.md` | 12, 22, 45 | §8 | "reconciliation **on this branch** … INCORPORATION IN REVIEW" | dated gate matrix | 6 | HISTORICAL (incorporation since merged at `9682cf5`) |
| `ck003/handover-assessment/02_NORMATIVE_GRAPH.md` | 32 | §8 | "APS-200 §8 … PROPOSED — not frozen" | dated handover assessment | 9 | HISTORICAL |
| `ck003/handover-assessment/03_DECISIONS.md` | 85 | §8 | "APS-200 §8 PROPOSED" | dated handover assessment | 9 | HISTORICAL |
| `ck003/handover-assessment/08_RELEASE_BLOCKERS.md` | 38 | §8 | "APS-200 §8 is PROPOSED" | dated handover assessment | 9 | HISTORICAL |
| `ck003/dq-002-hash-domain/02_hash_domain_adr.md` | 13 | §8 | "does not yet define a complete byte-level … contract" | dated DQ-002 evidence | 9 | HISTORICAL |
| `ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` | 6 | §8 | Related: APS-200 §4/§8 | ADR | 6 | CURRENT |
| `ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` | 10, 75 | §8 | "§8 currently states … is TODO"; open checklist item | dated DQ-002 evidence | 9 | HISTORICAL |
| `ck003/dq-002-hash-domain/HASH_DOMAIN_EVIDENCE.md` | 11 | §8 | "canonical serialization … is **TODO**" | dated DQ-002 evidence | 9 | HISTORICAL |
| `ck003/dq-006-canonical-serialization/CANONICAL_SERIALIZATION_CLOSURE_STATE.md` | 4 | §8 | "APS-200 §8 and APS-300 §5 are bound" | closure-state note | 9 | CURRENT |
| `ck003/dq-006-canonical-serialization/CANONICAL_SERIALIZATION_CLOSURE_STATE.md` | 11, 22 | §8 | "leaves the canonical serialization format … as TODO"; "§8 normative amendment" pending | dated closure-state note | 9 | HISTORICAL |
| `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md` | 5 | §8 | "Profile: RFC 8785 JCS (normative — APS-200 §8)" | oracle evidence | 6 | CURRENT |
| `ck003/dq-006-canonical-serialization/APS-200-SECTION-8-PROPOSED.md` | 1, 4, 5, 51 | §8 | superseded proposal, banner-marked, barred from normative citation | superseded proposal | 9 | HISTORICAL |
| `ck003/evidence/CORE_EVIDENCE_CONSOLIDATION_INDEX.md` | 25 | §8 | "explicitly leaves canonical serialization … as TODO" | dated evidence index | 9 | HISTORICAL |
| `aura-poc-a-core-v3.3/review/2026-08-12_RD1_ARI_DECISION_READINESS/05_DEPENDENCY_GRAPH.md` | 257 | §8 | "APS-200 §8/§9 … `TODO` (`APS-200:218,224`)" | dated review, Normative effect: NONE | 9 | HISTORICAL (line locator also stale) |

#### §9 — JSON Schema — target CURRENT, two citations semantically mismatched

| File | Line | Ref | Context (abridged) | Artifact class | Rank | Status |
|---|---:|---|---|---|---:|---|
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 67 | §9 | "APS-200 entity schemas (§9) remain TODO" | consistency scan | 6 | CURRENT (assertion still holds: §9 requires entity schemas before APS-001 v1.0) |
| `invariants/INVARIANT_REGISTRY.md` | 140 | §9 | INV-009 **Version Consistency** → Related APS: APS-000 §9, APS-200 §9 | invariant registry | 3 | **AMBIGUOUS** — see §10.3 |
| `compliance/TRACEABILITY_MATRIX.md` | 26 | §9 | "Version Everything \| APS-000 §9, APS-200 §9 \| INV-009" | traceability matrix | 6 | **AMBIGUOUS** — see §10.3 |
| `aura-poc-a-core-v3.3/…/01_ARI_DECISION_REGISTER.md` | 229 | §9 | "APS-200 §9 JSON Schema is marked TODO" | dated review, Normative effect: NONE | 9 | HISTORICAL |
| `aura-poc-a-core-v3.3/…/05_DEPENDENCY_GRAPH.md` | 257 | §9 | "APS-200 §8/§9 … `TODO`" | dated review, Normative effect: NONE | 9 | HISTORICAL |

#### §6, §7, §10 — target CURRENT, zero citations

No file in any in-scope repository cites APS-200 §6, §7 or §10. The nearest matches are
`ck003/evidence/core-v3.3/CORE_TO_SPEC_TRACEABILITY.md:10` (`APS-001 §7`, not APS-200) and
`ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md:94` (`APS-001 §7.1` / `APS-001 §10`).

#### §8.1–§8.9 — target NOT PRESENT — all BROKEN (G-1b)

| File | Line | Ref | Context (abridged) | Artifact class | Rank | Status |
|---|---:|---|---|---|---:|---|
| `aps/APS-300_EVIDENCE_MODEL.md` | 84 | §8.4 | "hexadecimal text … never itself a digest input (APS-200 §8.4)" | normative specification | 2 | BROKEN |
| `aps/APS-300_EVIDENCE_MODEL.md` | 94 | §8.2 | `canonical_bytes` authority column | normative specification | 2 | BROKEN |
| `aps/APS-300_EVIDENCE_MODEL.md` | 96 | §8.5 | Merkle leaf hash `SHA-256(0x00 ‖ canonical_bytes)` | normative specification | 2 | BROKEN |
| `aps/APS-300_EVIDENCE_MODEL.md` | 97 | §8.5 | Merkle interior-node hash | normative specification | 2 | BROKEN |
| `aps/APS-300_EVIDENCE_MODEL.md` | 103 | §8.8 | pre-profile evidence retains its hash-profile identity | normative specification | 2 | BROKEN |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | 99 | §8.4 | "MUST NOT accept, as a digest input, **any form listed in APS-200 §8.4**" | conformance requirement | 5 | BROKEN — **no list exists to enforce** |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 55 | §8.4 | "Prohibited digest inputs … are enumerated in APS-200 §8.4" | closure package | 6 | BROKEN |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 230 | §8.1–§8.9 | `aps/APS-200_CANONICAL_DATA_MODEL.md §8.1–8.9  NORMATIVE AUTHORITY` | closure package | 6 | BROKEN (9 targets) |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 281 | §8.8 | Closure criterion 11 — MET | closure package | 6 | BROKEN |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 282 | §8.2 | Closure criterion 12 "Single normative authority" — MET | closure package | 6 | BROKEN |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | 310 | §8.7 | CFL-005 rationale | closure package | 6 | BROKEN |
| `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 42 | §8.5 | "hash/Merkle domain defined in APS-200 §8.5" | ADR | 6 | BROKEN |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 50 | §8.3 | member ordering by JCS | ADR | 6 | BROKEN |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 51 | §8.3 | no insignificant whitespace | ADR | 6 | BROKEN |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 52 | §8.3 | non-ASCII is raw UTF-8 | ADR | 6 | BROKEN |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 53 | §8.3 | `NaN`/`Infinity` rejected, never coerced | ADR | 6 | BROKEN |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 54 | §8.2(1) | schema-validated before canonicalization | ADR | 6 | BROKEN (numbered sub-item) |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 56 | §8.4 | hex digest strings never substituted for digest bytes | ADR | 6 | BROKEN |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 57 | §8.1 | alternate wire encodings are transport only | ADR | 6 | BROKEN |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 58 | §8.7 | canonicalization determines representation only | ADR | 6 | BROKEN |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 66 | §8.8 | compatibility event; historical evidence not reinterpreted | ADR | 6 | BROKEN |
| `…ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | 110 | §8.8 | "Version/migration semantics documented — DONE" | ADR | 6 | BROKEN |
| `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md` | 6 | §8.5 | "Hash domain: APS-200 §8.5 / DQ-002" | oracle evidence | 6 | BROKEN |
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 28 | §8.1–§8.9 | row 1 asserts `APS-200 …md §8.1–§8.9` as the amended target | consistency scan | 6 | BROKEN (9 targets) |
| `…DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 32 | §8.5 | "APS-200 §8.5 now attributes the domain model back to APS-001 §7.1" | consistency scan | 6 | BROKEN — **assertion is false against current §8** |
| `…DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 94 | §8.5 | "APS-200 §8.5 attributes it back" | consistency scan | 6 | BROKEN — assertion false |
| `…DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 95 | §8.5 | "APS-200 §8.5 defers to it [APS-300 §5.1]" | consistency scan | 6 | BROKEN — assertion false |
| `…DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 110 | §8.5 | DQ-002 PASS verdict rests on §8.5 | consistency scan | 6 | BROKEN |
| `…DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 55 | §8.7 | CFL-005 disposition | consistency scan | 6 | BROKEN |
| `…DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 56 | §8.7 | DQ-004 row "Unchanged — consistent with §8.7" | consistency scan | 6 | BROKEN |
| `…DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 57 | §8.7 | DQ-003 row "no regression; §8.7 excludes version semantics" | consistency scan | 6 | BROKEN |
| `…DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 108 | §8.7 | **DQ-003 PASS verdict rests on §8.7** | consistency scan | 6 | BROKEN |
| `…DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | 109 | §8.7 | **DQ-004 PASS verdict rests on §8.7** | consistency scan | 6 | BROKEN |

**No broken reference was repaired.** No `§8.x` heading was authored, restored or
renumbered in APS-200.

---

## 8. CURRENT / HISTORICAL / BROKEN / AMBIGUOUS classification

### 8.1 Classification rule applied

- **CURRENT** — the cited target exists in the restored APS-200 **and** the citing
  statement is true of the current text.
- **HISTORICAL** — the citation belongs to explicitly dated, superseded or past-tense
  material whose framing remains accurate at its own date; not a live normative dependency.
- **BROKEN** — the cited target does not exist in the restored APS-200, or the citing
  statement asserts something the current text does not say.
- **AMBIGUOUS** — the target exists but its authority or intended meaning cannot be
  resolved from the current corpus without a Custodian decision.

### 8.2 Counts by status

Counted per **reference occurrence** (file, line, target), n = 129. A single citation
site may carry two targets with different statuses — e.g.
`aps/APS-300_EVIDENCE_MODEL.md:94` cites `§8` (CURRENT) and `§8.2` (BROKEN) on one line —
so occurrences, not the 108 distinct sites, are the countable unit here.

| Status | Occurrences |
|---|---:|
| CURRENT | **54** |
| HISTORICAL | **23** |
| BROKEN | **49** |
| AMBIGUOUS | **3** |
| **Total** | **129** |

By target group:

| Target group | CURRENT | HISTORICAL | BROKEN | AMBIGUOUS | Total |
|---|---:|---:|---:|---:|---:|
| §6 | 0 | 0 | 0 | 0 | 0 |
| §7 | 0 | 0 | 0 | 0 | 0 |
| §8 (top level) | 53 | 21 | **0** | 1 | 75 |
| §8.1–§8.9 | 0 | 0 | **49** | 0 | 49 |
| §9 | 1 | 2 | **0** | 2 | 5 |
| §10 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **54** | **23** | **49** | **3** | **129** |

**Top-level §6–§10 reference integrity: 0 BROKEN.** This is the evidentiary basis for
closing G-1.

### 8.3 The one AMBIGUOUS top-level §8 citation

`CHANGELOG.md:26` states that APS-200 §8 "now binds … the cross-implementation
byte-identity requirement, the scope boundary against event and version semantics, and
migration." Current §8 contains **no** normative cross-implementation MUST (it records
RI-PY/RI-RS byte-identity as executed *evidence*, not as a requirement) and **no** scope
boundary clause at all. The changelog describes the `ff30e16` §8, not the `9682cf5` §8.
The target section exists, so this is not BROKEN in the structural sense; the assertion
is nonetheless untrue of the current text. Classified **AMBIGUOUS** and routed to the
Custodian together with G-1b, since the correct repair depends on which §8 structure is
adopted. **Not repaired here.**

---

## 9. Blast-radius matrix

Dependency classes: **N** normative · **C** conformance · **I** implementation ·
**T** test · **F** fixture · **A** audit/closure · **D** documentation-only.

| Dependent artifact | Cites | Class | Blast radius | Post-restore status |
|---|---|---|---|---|
| `aps/APS-300_EVIDENCE_MODEL.md` | §8 ×4 | N | evidence-hash byte domain binds to §8 | **CURRENT** |
| `aps/APS-300_EVIDENCE_MODEL.md` | §8.2, §8.4, §8.5 ×2, §8.8 | N | a **normative** specification binds authority to five absent numbered targets | **BROKEN** |
| `specification/APS-001_PROTOCOL_SPECIFICATION.md` | §8 ×2 | N | Appendix A closure dependency: profile owned by APS-200 §8 | **CURRENT** |
| `invariants/INVARIANT_REGISTRY.md` — INV-003 | §8 | N + C | INV-003 Canonical Serialization resolves to §8 | **CURRENT** |
| `invariants/INVARIANT_REGISTRY.md` — INV-009 | §9 | N + C | Version Consistency cites a JSON-Schema section | **AMBIGUOUS** (§10.3) |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | §8 ×5 | C | conformance test anchored to §8 | **CURRENT** |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | §8.4 | C | a **MUST NOT** clause whose enumerated prohibition list no longer exists → the requirement is unenforceable as written | **BROKEN — highest severity** |
| `closures/DQ-006_CLOSURE_PACKAGE.md` (authoritative record) | §8 ×6 | A | closure authority header, criterion 1 | **CURRENT** |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | §8.1–§8.9, §8.2, §8.4, §8.7, §8.8 | A + C | closure criteria 11 and 12 are **MET** against absent targets; blast-radius tree names `§8.1–8.9` as NORMATIVE AUTHORITY | **BROKEN** |
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | §8 ×11 | A | reconciliation evidence | **CURRENT** |
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | §8.1–§8.9, §8.5 ×5, §8.7 ×6 | A + C | **the DQ-003 and DQ-004 PASS verdicts (rows 108, 109) rest entirely on §8.7**; rows 32/94/95 assert attributions the current §8 does not make | **BROKEN — closure-verdict impact** |
| `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-…md` | §8 ×8 | A | decision record; normative home correctly named | **CURRENT** |
| `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-…md` | §8.1, §8.2(1), §8.3 ×4, §8.4, §8.5, §8.7, §8.8 ×2 | A | eleven traceability citations to absent targets | **BROKEN** |
| `ck003/dq-006-final-closure-execution/DQ-006_FINAL_CLOSURE_EXECUTION_ORDER.md` | §8 ×5 | A | execution-order authority | **CURRENT** |
| `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md` | §8 | A | oracle profile anchor | **CURRENT** |
| `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md` | §8.5 | A | hash-domain anchor | **BROKEN** |
| `ck003/dq-006-canonical-serialization/APS-200-SECTION-8-PROPOSED.md` | §8 ×4 | D | superseded proposal, banner-marked, barred from normative citation | **HISTORICAL** |
| `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | §8 | **F** | fixture declares `normative_authority: "APS-200 §8"` | **CURRENT** — fixture **not modified** |
| `compliance/TRACEABILITY_MATRIX.md` | §8 / §9 | D + C | INV-003 row resolves; INV-009 row does not | **CURRENT / AMBIGUOUS** |
| `CHANGELOG.md` | §8 ×2 | A + D | line 26 describes the pre-`9682cf5` §8 | **AMBIGUOUS / CURRENT** |
| `specification/SPEC-002_CONSTITUTION_ARTIFACT_CONTRACT.md` | §8 | D | draft, "Normative effect: NONE until APPROVED" | **CURRENT** |
| `ck003/gates/GATE_A_APS001_CLOSURE_MATRIX.md` | §8 ×3 | A | Gate A rows written while incorporation was in review | **HISTORICAL** |
| `ck003/handover-assessment/*` | §8 ×3 | D | dated assessment: "§8 PROPOSED — not frozen" | **HISTORICAL** |
| `ck003/dq-002-hash-domain/*` | §8 ×5 | A | dated DQ-002 evidence: "§8 … TODO" (change control bars editing) | **HISTORICAL** (1 of 5 CURRENT) |
| `ck003/evidence/CORE_EVIDENCE_CONSOLIDATION_INDEX.md` | §8 | A | dated index | **HISTORICAL** |
| `ck003/audit/2026-08-20_ARCHITECTURE_EXECUTION_AUDIT.md` | §8 ×2 | A | dated audit | **HISTORICAL** |
| `aura-poc-a-core-v3.3/review/2026-08-12_RD1_*` | §8, §9 ×2 | D | dated review packages, "Normative effect: NONE"; `APS-200:218,224` line locators are stale | **HISTORICAL** |
| `aura-guard-v1.3` | — | — | mentions `APS-200 integrity_hash / event_payload_hash / previous_record_hash` in a disclaimer only; **no §6–§10 citation** | **no dependency** |
| `cargo`, `.github` | — | — | no `APS-200` occurrence at all | **no dependency** |

**Restoration did not, by itself, resolve any reference.** Every status above was
verified against the restored text; none was assumed.

---

## 10. Findings

### 10.1 G-1 — top-level §6–§10 (in scope, resolved)

APS-200 §6–§10 exist on `origin/main` and on the recovery branch, byte-identical.
There are 0 references to §6, §7 or §10, 75 to §8, and 5 to §9 — and **not one
top-level reference is BROKEN**. Restoration is proven and reference integrity for
the top-level structure is demonstrated.

### 10.2 G-1b — §8.1–§8.9 (OPEN / CUSTODIAN INPUT REQUIRED)

**Status: G-1b = OPEN / CUSTODIAN INPUT REQUIRED.**

49 subsection references across 6 files do not resolve. The full enumeration with
file, line and context is the `§8.1–§8.9` table in §7.3. Dependent artifacts, by
severity:

1. `conformance/CONF-003_CANONICAL_SERIALIZATION.md:99` — a conformance **MUST NOT**
   whose enumerated prohibition list is gone.
2. `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md:108,109` — the
   **DQ-003 and DQ-004 non-regression PASS verdicts** rest on §8.7.
3. `aps/APS-300_EVIDENCE_MODEL.md:84,94,96,97,103` — a **normative** specification
   binding authority to absent numbered targets.
4. `closures/DQ-006_CLOSURE_PACKAGE.md:230,281,282` — closure criteria 11 and 12
   recorded **MET** against absent targets.
5. `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-…md` — 11 traceability
   citations.
6. `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md:6`.

**Critical correction to the G-1b premise.** These are **not** references to
subsections that never existed. §11.3 shows they were present in APS-200 on `main`
at `ff30e16` with titles matching every citation, and were removed at `9682cf5`.
Content survival in current §8:

| Former subsection | Title at `ff30e16` | Content in current §8 |
|---|---|---|
| §8.1 | Transport representations | **ABSENT** (JSON/CBOR/Protobuf transport rule gone) |
| §8.2 | Canonical serialization profile | **PARTIAL** — profile kept; the numbered 4-step procedure and the "single normative authority" declaration are gone |
| §8.3 | Properties fixed by the profile | **PARTIAL** — ordering/whitespace kept; raw-UTF-8 rule, RFC 8785 number rules, `NaN`/`Infinity` rejection and array-order rule gone |
| §8.4 | Prohibited digest inputs | **ABSENT as an enumeration** — only a general substitution clause remains |
| §8.5 | Hash and Merkle domains | **PARTIAL** — formulas kept; the APS-001 §7.1 ownership attribution and the APS-300 §5 deferral are gone |
| §8.6 | Cross-implementation requirement | **ABSENT as a requirement** — downgraded to a statement of executed evidence |
| §8.7 | Scope boundary | **ABSENT** |
| §8.8 | Compatibility and migration | **PARTIAL** — version-binding kept; the historical-evidence non-reinterpretation MUST is gone |
| §8.9 | Reference engines (informative) | **PRESENT in substance**, unnumbered |

G-1b is therefore not solely a renumbering problem. Several citations point at
normative content that no longer exists in any form in APS-200. **No content was
restored, authored or reconstructed by this audit.**

### 10.3 G-1c — APS-200 §9 semantic mismatch (NEW — reported, not remediated)

Discovered during the §9 reference sweep; recorded here because it falls inside the
§6–§10 reference-integrity mandate. **No remediation document was created and no
change was made.**

`invariants/INVARIANT_REGISTRY.md:140` (INV-009 — Version Consistency) and
`compliance/TRACEABILITY_MATRIX.md:26` (Version Everything → INV-009) both cite
**APS-200 §9** as the versioning authority. Current APS-200 §9 is **JSON Schema**;
APS-000 §9, cited alongside it, is **Traceability**. Neither is about versioning.

The root-level authoritative source
`APS-200 — Canonical Data Model_260723_192852.txt` has, at its line 134:

```text
9. Compatibility
Zmiany modelu danych podlegają wersjonowaniu semantycznemu.
Każda zmiana MUST określać:
• wpływ na zgodność,
• wymagane migracje,
• zgodność wsteczną (jeśli dotyczy).
```

The markdown canonicalization of APS-200 substituted "JSON Schema" for the source's
§9 "Compatibility" at the same section number. §6, §7, §8 and §10 of the markdown
faithfully render the source; **§9 is the sole divergence**. INV-009's citation is
therefore correct against the authoritative source text and incorrect against the
markdown.

**Status: AMBIGUOUS / CUSTODIAN INPUT REQUIRED.** This is a normative-content question
(was §9 Compatibility deliberately dropped, or lost in transcription?) and is
explicitly **not** resolved here. `9682cf5` also removed the
`*Source: Original text preserved in [APS-200 — Canonical Data Model_260723_192852.txt]*`
footer that linked the markdown to that source.

### 10.4 G-3, G-5, G-6

Re-confirmed as previously recorded, from primary sources only, with no new content
inferred:

- **G-3** — `aps/EVENT_TYPE_REGISTRY.md` remains `DRAFT — DQ-004 closure artifact`; no
  event token is promoted to final normative status while strict conformance must
  reject unregistered tokens. `CFL-005` (`closures/DQ-006_CLOSURE_PACKAGE.md:310`) is
  live. **OPEN / CUSTODIAN INPUT.** Not addressed here.
- **G-5** — session lifecycle semantics for `sequence_number` are not closed by any
  §6–§10 text. **OPEN / CUSTODIAN INPUT.** Not addressed here.
- **G-6** — chain-link documentation. Not a §6–§10 artifact; untouched. **OPEN.**

No remediation document was created for G-1b, G-3, G-5 or G-6.

---

## 11. Git-history regression evidence

### 11.1 Two divergent lineages

```text
                       9682cf5 ── c069a1b ── 8a27069 = origin/main
                          │                              = claude/aps-200-spec-recovery-b7wc2h
   (merge-base)           │                              §1–§10 present, §8 flat
                          │
                          └── 9b5c262 … 8d3f1fe ── bf33eb4 ── … ── 8de397b
                                                      ▲            = dq/dq-003-audit-record-hash-domain
                                                      │            = claude/dq-003-conformance-audit-4ok63x
                                            §6–§10 DELETED HERE     §6–§10 still absent at tip
```

`git merge-base origin/main origin/dq/dq-003-audit-record-hash-domain` = `9682cf5`.

### 11.2 Commit `bf33eb4` — confirmed regression

```
commit bf33eb40411d02ba30c68708f980b31747e6ac99
Author: Aura-IDToken <aura.idtokenkontakt@gmail.com>
Date:   Sat Aug 22 21:44:56 2026 +0200
    spec(dq-003): define EP-001 event payload contract

 aps/APS-200_CANONICAL_DATA_MODEL.md | 178 +++++++++-------------------
 1 file changed, 71 insertions(+), 107 deletions(-)
```

| Question | Evidence-based answer |
|---|---|
| What did it change? | Added `### 5.5 EP-001 — Event Payload Contract`; edited three ENT field rows; **deleted §6 Relationships, §7 Validation Rules, §8 Serialization Requirements (incl. the CANONICAL-001 reference vector), §9 JSON Schema and §10 Traceability in full**; and truncated the ENT-008 field table to its first row, dropping `implementation_id`, `implementation_name`, `implementation_version`, `aps_version` and `conformance_report_id`. |
| What did it claim to change? | Only "define EP-001 event payload contract". |
| Were §6–§10 intentionally deleted? | **No evidence of intent.** The message, the diff framing and the ENT-008 mid-table truncation are all consistent with an accidental tail overwrite while inserting §5.5. |
| Deprecation / replacement record? | **None.** No document on that branch records the removal, supersession or replacement of §6–§10 or of the ENT-008 rows. |
| Did dependent references remain live? | **Yes.** On that branch, §4 still says "Canonical bytes are defined by §8", §5.2 references §8, and the whole §8/§8.x citation graph in §7.3 remains, now pointing at nothing. |
| Repaired since? | **No.** Six later commits (`ac5d402`, `e109cff`, `65c5e76`, `35c1714`, `a7ab42b`, `68a9229`, `8de397b`) never noticed; the branch tip still ends mid-ENT-008 table. |

**Verdict: CONFIRMED REGRESSION**, not an intentional normative change, and it is
**confined to the DQ-003 branches**. `origin/main` and the designated recovery branch
are unaffected. History was not altered.

### 11.3 Commit `9682cf5` — the §8.1–§8.9 collapse (separate event)

`git log --all -- aps/APS-200_CANONICAL_DATA_MODEL.md`, counting `^###+ *8\.[0-9]`
headings per revision:

| Commit | `§8.x` headings | Subject |
|---|---:|---|
| `b68181e` | 0 | build complete canonical repository structure |
| `704832a` | 7 | CK-003: enact the canonical serialization contract in APS-200 §8 |
| `b9311d0` | 0 | incorporate DQ-006 canonical serialization contract into APS-200 |
| `a0df11a` | **9** | reconcile canonical serialization closure across APS-200/300, ADR, CONF-003 |
| **`ff30e16`** | **9** | **same, merged to `main` (#26)** |
| `7826db9` | 0 | merge `main` into `ck003/specification-integration-dq006` |
| **`9682cf5`** | **0** | **CK-003: reconcile APS-200 with DQ-006 and refresh closure controls (#25)** |
| `8d3f1fe`, `bf33eb4`, `e109cff` | 0 | DQ-003 branch descendants |

Structure at `ff30e16` (on `main`):

```
## 8. Serialization Requirements
### 8.1 Transport representations
### 8.2 Canonical serialization profile
### 8.3 Properties fixed by the profile
### 8.4 Prohibited digest inputs
### 8.5 Hash and Merkle domains
### 8.6 Cross-implementation requirement
### 8.7 Scope boundary
### 8.8 Compatibility and migration
### 8.9 Reference engines (informative)
```

Every citing artifact's wording matches these titles (e.g. ADR line 57 ↔ §8.1
"Transport representations"; ADR line 54 `§8.2(1)` ↔ item 1 of §8.2; CONF-003 line 99
↔ §8.4's six-item prohibition list; SCAN lines 108/109 ↔ §8.7 "Scope boundary").

`9682cf5` replaced this structure with a flat §8. Its commit message
("reconcile APS-200 with DQ-006 and refresh closure controls") does not mention
removing subsections, and **no deprecation, renumbering or migration record was
produced** in that commit or since.

**Verdict: `9682cf5` is AMBIGUOUS** — a deliberate rewrite of §8's prose whose
*structural* consequence (49 dangling citations plus the content losses in §10.2) was
evidently not analysed. This is the root cause of G-1b and is a **separate event** from
the `bf33eb4` regression. Neither history was altered.

---

## 12. Normative authority assessment

1. `origin/main` @ `8a27069` (APS-200 blob `0488eec`, introduced by `9682cf5`) is the
   authoritative APS-200 baseline. Nothing in the repository supersedes it.
2. `ff30e16` is **historical `main` content**, not a competing authority. It is cited
   here strictly as evidence that §8.1–§8.9 once existed. **It must not be treated as
   authority for restoring them** — that is a Custodian decision (§13).
3. The DQ-003 branches (`bf33eb4` lineage) are **not** an authoritative source for
   APS-200: they carry a confirmed unrepaired regression.
4. Within the specification corpus, current APS-200 §8 remains the single normative home
   for canonical serialization. That resolution is unaffected by G-1b: the *authority* is
   intact, the *citation targets* are not.
5. Frozen for this pass, unchanged by this audit: RFC 8785 JCS as the canonical profile;
   UTF-8 JCS output as canonical bytes; `SHA-256(0x00 ‖ B)` leaf and `0x01` interior
   domains; the DQ-003 `0x02` audit-record domain as a separate later addition;
   `integrity_hash` self-exclusion; `previous_record_hash[n+1] = audit_record_hash[n]`.
6. `ck003/dq-003-specification-reconciliation/APS-200-SECTION-6-10-REFERENCE-AUDIT.md`
   contains a fabricated §6/§7/§10 reference inventory and a tool-residue citation
   (§7.2). Its **conclusion** — that §6–§10 are present on `main` and that the live issue
   is §8.x reference integrity — is independently confirmed correct by this audit; its
   **inventory tables** are not reliable. Not modified here.

---

## 13. Remaining Custodian decisions

| # | Decision | Blocks | Cannot be inferred because |
|---|---|---|---|
| D-1 | **§8 structure.** (A) keep flat §8 and migrate all §8.x citations to semantic anchors; (B) reinstate numbered §8.1–§8.9; (C) define a different structure with an explicit citation migration. | G-1b, C4 | choosing any option is a normative structuring decision |
| D-2 | **§8 content restoration.** Independently of D-1: are the §8.1/§8.4/§8.6/§8.7 rules that no longer appear in any form (transport representations; the enumerated prohibited digest inputs; the cross-implementation MUST; the scope boundary) still normative? `CONF-003:99` is unenforceable as written until this is answered. | G-1b, CONF-003 | current §8 neither states nor repeals them |
| D-3 | **DQ-006 closure criteria 11 and 12** (`closures/DQ-006_CLOSURE_PACKAGE.md:281,282`) are recorded **MET** against §8.8 and §8.2. Re-affirm or re-open. | G-1b | re-recording a closure verdict is a Custodian act |
| D-4 | **DQ-003 / DQ-004 non-regression PASS verdicts** (`DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md:108,109`) rest on §8.7. Re-affirm or re-open. | G-1b, DQ-003, DQ-004 | the supporting text is absent |
| D-5 | **APS-200 §9** — was the source's §9 "Compatibility" deliberately replaced by "JSON Schema"? If deliberate, INV-009's and TRACEABILITY_MATRIX's §9 citations need a new target. | G-1c | requires knowing intent, not just text |
| D-6 | **`bf33eb4` regression on the DQ-003 branches** — whether to repair §6–§10 and the ENT-008 table on `dq/dq-003-audit-record-hash-domain` and `claude/dq-003-conformance-audit-4ok63x`. **Out of this task's branch scope**; recorded so it is not lost. | DQ-003 | those branches were outside the authorized change scope |
| D-7 | **G-3** event-type vocabulary; **G-5** session lifecycle; **G-6** chain-link diagram. | C4 | unchanged by this audit |

---

## 14. Explicit statement of what was NOT changed

Verified by `git status --porcelain` and `git diff` across all five repositories:

- **APS-200 §1–§5** — not modified (byte-identical, §5).
- **APS-200 §6–§10** — not rewritten, reformatted, paraphrased or renumbered; restored
  byte-for-byte from `origin/main` (§6).
- **No §8.1–§8.9 subsections were authored, restored or reconstructed.**
- **No broken reference was silently repaired** — not one of the 49 §8.x citations, and
  not the 3 AMBIGUOUS ones.
- **No section was renumbered** anywhere.
- **No other specification file was touched** — APS-000/001/100/300/400/500/900/950,
  EVENT_TYPE_REGISTRY, SPEC-002, CONF-001…CONF-015, the invariant registry, the
  traceability matrix, CHANGELOG, ADRs and all closure packages are unmodified.
- **Golden Fixture / conformance fixtures unchanged** — `fixtures/corpus/CANONICAL-001_jcs_evidence.json`,
  `fixtures/**`, `conformance/**` (other than the new audit file), and the DQ-003
  `AUDIT-CHAIN-001` fixtures on their own branches: untouched.
- **RI-PY unchanged** — no file in `aura-poc-a-core-v3.3` modified.
- **RI-RS unchanged** — no file in `aura-guard-v1.3` or `cargo` modified.
- **No implementation code of any kind changed** in any repository.
- **DQ-003 hash semantics unchanged** — `0x02 ‖ JCS(R_AR)`, `integrity_hash`
  self-exclusion and the chain rule are untouched; **DQ-003 remains OPEN**.
- **ENT-007 not implemented.** **EP-001 not implemented or moved.**
- **C4 not started.** No C4 artifact was created or advanced.
- **`origin/main` not amended.** No history rewritten, on any branch. `bf33eb4` and
  `9682cf5` were read only.
- **Prior audit artifacts not edited** — the reconciliation records on
  `dq-003/specification-reconciliation` and `specification-recovery/reconciliation-aps200`
  are untouched, including the one found unreliable in §12.6.
- **No remediation document created for G-1b, G-3, G-5 or G-6.**
- **Exactly one file added:** this audit.

---

## 15. Final G-1 verdict

```text
┌───────────────────────────────────────────────────────────────────────┐
│  G-1  = CLOSED                                                        │
│                                                                       │
│    §6  Relationships             PRESENT · byte-identical · 0 refs    │
│    §7  Validation Rules          PRESENT · byte-identical · 0 refs    │
│    §8  Serialization Reqs        PRESENT · byte-identical · 75 refs   │
│                                                    53 CURRENT         │
│                                                    21 HISTORICAL      │
│                                                     1 AMBIGUOUS       │
│                                                     0 BROKEN          │
│    §9  JSON Schema               PRESENT · byte-identical · 5 refs    │
│                                                     1 CURRENT         │
│                                                     2 HISTORICAL      │
│                                                     2 AMBIGUOUS       │
│                                                     0 BROKEN          │
│    §10 Traceability              PRESENT · byte-identical · 0 refs    │
│                                                                       │
│    Restoration proven (§4–§6) AND top-level reference integrity       │
│    demonstrated (§7–§9): every §6–§10 reference resolves against      │
│    the restored authoritative structure. ZERO broken top-level refs.  │
├───────────────────────────────────────────────────────────────────────┤
│  G-1b = OPEN / CUSTODIAN INPUT REQUIRED   — NOT merged into G-1       │
│         49 dangling §8.1–§8.9 references, 6 files, enumerated §7.3    │
│         Root cause: 9682cf5 collapsed §8.1–§8.9 with no migration     │
│         record. The subsections DID exist on main at ff30e16.         │
├───────────────────────────────────────────────────────────────────────┤
│  G-1c = OPEN / CUSTODIAN INPUT REQUIRED   — NEW, reported only        │
│         APS-200 §9 semantic mismatch vs. the authoritative source     │
├───────────────────────────────────────────────────────────────────────┤
│  DQ-003 = OPEN      C4 = NOT AUTHORIZED      ENT-007 = NOT IMPLEMENTED│
└───────────────────────────────────────────────────────────────────────┘
```

**G-1 is closed on evidence, not on the fact of restoration alone.** The two
findings the task required to be kept separate are kept separate:

- *"§6–§10 were deleted from the current branch"* — **FALSE for this branch and for
  `main`**; TRUE and confirmed as a regression for the DQ-003 branches (§11.2).
- *"references to §8 subsections that do not exist in the current APS-200"* — **TRUE**,
  49 of them, and — contrary to the working premise — those subsections **did** exist
  on `main` before `9682cf5` (§11.3).

---

## 16. Machine-checkable verification commands and results

All commands run from the `aura-specification` working tree on
`claude/aps-200-spec-recovery-b7wc2h`. `$F = aps/APS-200_CANONICAL_DATA_MODEL.md`.

### V-1 — baseline identity

```console
$ git rev-parse HEAD
8a2706969f65707817486a865af356f2398cf275
$ git rev-parse origin/main
8a2706969f65707817486a865af356f2398cf275
$ git rev-parse 9682cf5:$F origin/main:$F HEAD:$F | sort -u | wc -l
1                                    # one distinct blob → all three identical
```
**PASS**

### V-2 — §1–§5 immutability and §6–§10 equality

```console
$ python3 - <<'PY'
import hashlib,subprocess
p='aps/APS-200_CANONICAL_DATA_MODEL.md'; M=b'## 6. Relationships'
cur=open(p,'rb').read()
om=subprocess.run(['git','show','origin/main:'+p],capture_output=True).stdout
print('§1-§5  branch == pre-restore :', hashlib.sha256(cur[:cur.index(M)]).hexdigest())
print('§6-§10 branch == origin/main :', cur[cur.index(M):]==om[om.index(M):])
print('§6-§10 sha256                :', hashlib.sha256(om[om.index(M):]).hexdigest())
PY
§1-§5  branch == pre-restore : 47ea97b67c06c5a1a8e67c43f84aa760df799ff0db0730370929c88e741f9adf
§6-§10 branch == origin/main : True
§6-§10 sha256                : 74de67d37ce8fcc84d85d03081e2c72e12fc05bf0f5d404b55f252bb3e027c37
```
**PASS** — matches the pre-restore digests in §3.

### V-3 — restored section set

```console
$ grep -nE '^## (6|7|8|9|10)\.' $F
180:## 6. Relationships
202:## 7. Validation Rules
213:## 8. Serialization Requirements
272:## 9. JSON Schema
280:## 10. Traceability
```
**PASS** — 5 of 5 present.

### V-4 — no §8.x subsection invented

```console
$ grep -cE '^#{3,4} *8\.[0-9]' $F
0
```
**PASS**

### V-5 — dangling §8.x reference count (G-1b)

```console
$ for d in aura-specification aura-poc-a-core-v3.3 aura-guard-v1.3 cargo .github; do
    git -C $d grep -n -I -E '§+ ?8\.[0-9]' -- . ; done | wc -l
33            # 33 citation lines → 49 target occurrences after range expansion
```
**FAIL (expected)** — G-1b remains OPEN. Not repaired.

### V-6 — change scope firewall

```console
$ git status --porcelain
?? conformance/canonical/G-1-SPECIFICATION-RECOVERY-REFERENCE-AUDIT.md
$ git diff --stat
$ git diff -- aps/APS-200_CANONICAL_DATA_MODEL.md
$ git diff --name-only
```
**PASS** — APS-200 diff empty (restore is a proven no-op); the only new path is this audit.

### V-7 — sibling repositories untouched

```console
$ for d in ../aura-poc-a-core-v3.3 ../aura-guard-v1.3 ../cargo ../.github; do
    git -C $d status --porcelain; done
                                     # no output
```
**PASS** — RI-PY, RI-RS, cargo and .github unmodified.

### V-8 — regression localisation

```console
$ git show bf33eb4:$F | grep -cE '^## (6|7|8|9|10)\.'
0
$ git show origin/dq/dq-003-audit-record-hash-domain:$F | grep -cE '^## (6|7|8|9|10)\.'
0
$ git show origin/main:$F | grep -cE '^## (6|7|8|9|10)\.'
5
```
**Confirms** the loss is confined to the DQ-003 lineage.

### V-9 — §8.x historical existence

```console
$ git show ff30e16:$F | grep -cE '^#{3} *8\.[0-9]'
9
$ git show 9682cf5:$F | grep -cE '^#{3} *8\.[0-9]'
0
```
**Confirms** §8.1–§8.9 existed on `main` and were removed by `9682cf5`.

### Environment limitation — declared

`aura-specification` contains **no CI workflows, no test harness, no linter and no
executable reference-checking tool** (`.github/workflows/` is absent; `scripts/`
contains only `README.md`; there is no Makefile). The checks above — git blob identity,
SHA-256 region digests, structural `grep` assertions and the tracked-file reference
sweep of §7.1 — are the **strongest verifications this environment can execute**.
**No conformance suite, no RI-PY or RI-RS execution and no CI job was run, and none is
claimed.** Every result above was produced by the command shown.

---

*Produced under the CK-003 / DQ-003 specification-recovery mandate. Specification
reconciliation only. This document defines no protocol semantics and grants no
implementation authorization.*

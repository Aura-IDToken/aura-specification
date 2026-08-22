# DQ-003 — APS-200 §6–§10 Reference Audit

**Classification:** GOVERNANCE / TRACEABILITY — non-normative
**Branch:** `dq-003/specification-reconciliation`
**Base:** `main` @ `8a2706969f65707817486a865af356f2398cf275`
**Purpose:** inventory and classify repository references to APS-200 §§6–10 without modifying normative content.
**C4 status:** NOT AUTHORIZED
**DQ-003 status:** OPEN

---

## 1. Audit rule

This audit answers only:

> Where does the repository refer to APS-200 §§6–10, and does each reference resolve against the APS-200 document that exists on `main`?

No normative text is inferred, restored, renamed, or rewritten by this audit.

Classification:

- **CURRENT** — reference resolves to a section that exists in current `main` and is semantically compatible with the current APS-200 text.
- **HISTORICAL** — reference belongs to a superseded/deliberately retained historical artifact or explicitly dated evidence and is not an active normative dependency.
- **BROKEN** — reference names a section/subsection that does not exist in current APS-200, or otherwise points to a non-existent normative target.
- **AMBIGUOUS** — reference exists, but its authority/status cannot be resolved from the current corpus without a Custodian decision.

`§8.1`–`§8.9` are treated as individual targets. Current `APS-200_CANONICAL_DATA_MODEL.md` has a single `§8 — Serialization Requirements`; it does **not** currently expose numbered subsections `§8.1`–`§8.9`.

---

## 2. Current APS-200 target surface

Direct inspection of `main` establishes these current section targets:

| Target | Current status |
|---|---|
| APS-200 §6 | CURRENT — Relationships |
| APS-200 §7 | CURRENT — Validation Rules |
| APS-200 §8 | CURRENT — Serialization Requirements |
| APS-200 §9 | CURRENT — JSON Schema |
| APS-200 §10 | CURRENT — Traceability |
| APS-200 §8.1 | **NOT PRESENT** |
| APS-200 §8.2 | **NOT PRESENT** |
| APS-200 §8.3 | **NOT PRESENT** |
| APS-200 §8.4 | **NOT PRESENT** |
| APS-200 §8.5 | **NOT PRESENT** |
| APS-200 §8.6 | **NOT PRESENT** |
| APS-200 §8.7 | **NOT PRESENT** |
| APS-200 §8.8 | **NOT PRESENT** |
| APS-200 §8.9 | **NOT PRESENT** |

The current APS-200 §8 itself defines JCS/RFC 8785, UTF-8 canonical bytes, SHA-256 digesting, RFC 6962 leaf/interior domains, version binding, and migration semantics. Therefore references to **APS-200 §8** are resolvable; references to its former numbered children are not.

---

## 3. Direct §6–§10 reference inventory

### §6 — Relationships

| Location | Reference | Classification | Reason |
|---|---|---|---|
| `closures/DQ-006_CLOSURE_PACKAGE.md` | APS-200 §6–§10 scope/traceability references | CURRENT | §6 exists in current APS-200. |
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | APS-200 §6–§10 references | CURRENT | Target sections exist; scan is traceability evidence. |
| `specification/SPEC-002_CONSTITUTION_ARTIFACT_CONTRACT.md` | APS-200 §6 reference | CURRENT | Section exists; no conflicting authority identified. |

### §7 — Validation Rules

| Location | Reference | Classification | Reason |
|---|---|---|---|
| `ck003/evidence/core-v3.3/CORE_TO_SPEC_TRACEABILITY.md` | APS-200 §7 | CURRENT | Target exists. |
| `ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md` | APS-200 §7 | CURRENT | Target exists; used as validation/contract context. |
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | APS-200 §7 | CURRENT | Target exists. |
| `compliance/TRACEABILITY_MATRIX.md` | APS-200 §7 | CURRENT | Target exists. |
| `invariants/INVARIANT_REGISTRY.md` | APS-200 §7 | CURRENT | Target exists. |
| `specification/SPEC-002_CONSTITUTION_ARTIFACT_CONTRACT.md` | APS-200 §7 | CURRENT | Target exists. |

### §8 — Serialization Requirements

| Location | Reference | Classification | Reason |
|---|---|---|---|
| `aps/APS-200_CANONICAL_DATA_MODEL.md` | §8 from §4/§9/§10 | CURRENT | Self-reference to the existing normative serialization section. |
| `aps/APS-300_EVIDENCE_MODEL.md` | APS-200 §8 | CURRENT | §5.1 explicitly binds Evidence canonical bytes to APS-200 §8. |
| `aps/EVENT_TYPE_REGISTRY.md` | APS-200 serialization profile | CURRENT | §7 correctly delegates canonicalization to APS-200; no subsection dependency. |
| `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | APS-200 §8 | CURRENT | ADR explicitly states APS-200 §8 is the single normative home. |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | APS-200 §8 | CURRENT | Closure package explicitly identifies §8 as normative authority. |
| `conformance/CONF-003_CANONICAL_SERIALIZATION.md` | APS-200 §8 | CURRENT | Conformance requirement resolves to current section. |
| `invariants/INVARIANT_REGISTRY.md` | APS-200 §8 | CURRENT | Direct target exists. |
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | APS-200 §8 | CURRENT | Target exists. |
| `ck003/dq-006-canonical-serialization/APS-200-SECTION-8-PROPOSED.md` | proposed §8 | HISTORICAL | Explicitly superseded; retained as history and barred from normative citation. |

### §9 — JSON Schema

| Location | Reference | Classification | Reason |
|---|---|---|---|
| `releases/README.md` | APS-200 §9 | CURRENT | Target exists. |
| `ck003/handover-assessment/03_DECISIONS.md` | APS-200 §9 | CURRENT | Target exists; handover material is non-normative. |
| `ck003/handover-assessment/05_EVIDENCE_GAPS.md` | APS-200 §9 | CURRENT | Target exists. |
| `invariants/INVARIANT_REGISTRY.md` | APS-200 §9 | CURRENT | Target exists. |
| `specification/SPEC-002_CONSTITUTION_ARTIFACT_CONTRACT.md` | APS-200 §9 | CURRENT | Target exists. |
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | APS-200 §9 | CURRENT | Target exists. |
| `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md` | APS-200 §9 | CURRENT | Target exists. |

### §10 — Traceability

| Location | Reference | Classification | Reason |
|---|---|---|---|
| `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md` | APS-200 §10 | CURRENT | Target exists. |
| `closures/DQ-006_CLOSURE_PACKAGE.md` | APS-200 §10 | CURRENT | Target exists. |
| `ck003/dq-006-canonical-serialization/CANONICAL-001_INDEPENDENT_ORACLE.md` | APS-200 §10 | CURRENT | Target exists. |
| `ck003/handover-assessment/06_IMPL_CONFORMANCE_CI_GAPS.md` | APS-200 §10 | CURRENT | Target exists. |

---

## 4. G-1b — §8.1–§8.9 audit

This is the principal reconciliation finding.

### 4.1 Active documents with broken subsection references

#### `aps/APS-300_EVIDENCE_MODEL.md`

Current text contains explicit references to:

- APS-200 §8.2
- APS-200 §8.2(1)
- APS-200 §8.4
- APS-200 §8.5
- APS-200 §8.8

**Classification: BROKEN.**

These are not merely historical references because APS-300 is itself a current normative draft and uses them as authority bindings. The underlying concepts may still exist in current APS-200 §8, but the numbered targets do not.

This is a documentation/specification integrity defect. No correction is made here.

#### `ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md`

Current ADR contains references to:

- §8.1
- §8.2 / §8.2(1)
- §8.3
- §8.4
- §8.5
- §8.7
- §8.8

**Classification: BROKEN at reference level; ADR itself remains CURRENT as a decision record.**

The ADR explicitly says APS-200 §8 is the normative home, but several traceability citations point to subsection numbers absent from the current APS-200.

This is G-1b, not permission to rewrite the ADR's cited subsection numbers ad hoc.

#### `closures/DQ-006_CLOSURE_PACKAGE.md`

The current authoritative closure package contains a traceability statement referring to APS-200 §8.1–§8.9 and uses former subsection identifiers in its normative-contract discussion.

**Classification: BROKEN at subsection-reference level; closure record remains CURRENT as governance evidence.**

The closure record itself explicitly calls itself the authoritative DQ-006 closure record, so the broken internal references cannot simply be dismissed as historical.

#### `ck003/dq-006-closure/DQ-006_SPECIFICATION_CONSISTENCY_SCAN.md`

The scan records `aps/APS-200_CANONICAL_DATA_MODEL.md §8.1–§8.9` as if these subsections exist.

**Classification: BROKEN as a current traceability assertion.**

This is especially important because the scan was intended to reconcile the repository. Its historical audit result and its current target references must not be conflated.

---

## 5. Historical §8 artifacts

### `ck003/dq-006-canonical-serialization/APS-200-SECTION-8-PROPOSED.md`

**Classification: HISTORICAL.**

The repository's own DQ-006 consistency scan identifies this artifact as superseded and says its content was incorporated into APS-200 §8. It is therefore evidence of the evolution of the decision, not a live normative authority.

### Dated DQ-002 / DQ-006 evidence

Search results also locate former §8 references in DQ-002/DQ-006 evidence and handover artifacts. Where those documents explicitly describe an earlier state (for example, an APS-200 §8 TODO), they are **HISTORICAL**, not BROKEN, provided their historical framing remains explicit.

If a historical artifact is presented as current authority, that specific usage becomes **AMBIGUOUS/BROKEN** and must be handled separately.

---

## 6. Section 6–10 authority findings

### G-1

No evidence from the current `main` inspection supports a current absence of APS-200 §§6–10 themselves. The current APS-200 contains all five sections.

Therefore the earlier formulation "§6–§10 missing from main" is **not supported by current HEAD**.

The actual current integrity problem is narrower and more precise:

```text
APS-200 §6–§10                 PRESENT
        │
        └── APS-200 §8.1–§8.9  ABSENT
                 │
                 ├── APS-300 cites them
                 ├── ADR cites them
                 ├── closure record cites them
                 └── consistency scan cites them
```

**G-1 status should therefore be reframed from "§6–§10 absent" to "§6–§10 present; §8 subsection reference integrity unresolved" unless contrary evidence is supplied by the Custodian.**

No change to the existing G-1 label is made by this audit.

### G-1b

**CONFIRMED.** This is a live reference-integrity issue, not merely historical documentation drift.

### G-3

Outside the §6–§10 reference-integrity problem, the current registry independently confirms that no individual event token has final normative status and that unknown tokens must be rejected in strict conformance. `AUDIT_DECISION` therefore remains a Custodian decision and is not inferred from fixture usage. fileciteturn90file0L2-L2

### G-5

No section-number correction is inferred here. Session semantics remain a separate Custodian input.

### G-6

No section-number correction is inferred here. Chain-link semantics remain a separate specification issue.

---

## 7. Classification summary

| Category | Result |
|---|---|
| CURRENT section targets (§6–§10) | **CONFIRMED** |
| CURRENT direct §8 references | **CONFIRMED** |
| HISTORICAL proposed §8 artifact | **CONFIRMED** |
| BROKEN §8.1–§8.9 references in active documents | **CONFIRMED** |
| AMBIGUOUS normative meaning of missing §8 subsections | **OPEN / CUSTODIAN INPUT** |
| Evidence that current main lacks §6–§10 | **NOT FOUND** |
| Normative APS-200 text modified by this audit | **NONE** |
| C4 authorization | **NO** |

---

## 8. No-repair rule

The following actions are explicitly **NOT authorized by this audit**:

- renumbering APS-200 §8 subsections;
- inserting §8.1–§8.9 into APS-200 from the historical proposal;
- rewriting APS-300 citations;
- rewriting the ADR citations;
- changing closure evidence;
- changing Golden Fixtures;
- adding `AUDIT_DECISION`;
- implementing ENT-007;
- changing hash domains;
- changing RI-RS or RI-PY.

The audit produces a decision input, not a remediation patch.

---

## 9. Recommended Custodian decision packet

Before any repair, the Custodian should decide exactly one of the following for §8 structure:

### Option A — single-section §8

Keep current APS-200 §8 as one section and migrate all former §8.x authority references to semantic anchors within §8.

### Option B — restore numbered §8.x subsections

Formally reconstitute §8.1–§8.9 in APS-200 using an authoritative source and explicitly approve the resulting structure.

### Option C — replacement structure

Define a different normative subsection structure, with an explicit migration of all existing §8.x references.

**No option is selected by this audit.**

---

## 10. Exit criteria for G-1b

G-1b can close only when:

1. APS-200 §8 structure is explicitly decided by the Custodian;
2. every active §8.x reference resolves;
3. every historical §8.x reference is clearly marked historical/superseded;
4. APS-300's normative citations resolve;
5. ADR-CK003-DQ006's traceability citations resolve;
6. DQ-006 closure package citations resolve;
7. the consistency scan itself no longer asserts nonexistent current subsections;
8. no hash construction or semantic rule is changed merely to repair references;
9. C4 remains blocked until this gate is formally accepted.

---

## 11. Audit conclusion

The reference audit **does not justify a §6–§10 restore** on current `main`.

It **does justify a formal G-1b blocker**:

```text
APS-200 §6–§10
      │
      ├── §6 CURRENT
      ├── §7 CURRENT
      ├── §8 CURRENT
      │     └── §8.1–§8.9 NOT PRESENT
      ├── §9 CURRENT
      └── §10 CURRENT

Active documents still cite §8.1–§8.9
      ↓
BROKEN TRACEABILITY
      ↓
CUSTODIAN DECISION REQUIRED
      ↓
NO REPAIR YET
      ↓
C4 NOT AUTHORIZED
```

This is the state to carry forward into the Custodian decision record.
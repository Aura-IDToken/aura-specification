# CK-003 — Blocker Register

**Classification:** WORKING / CONTROLLED REGISTER  
**Status:** ACTIVE  
**Authority:** `ck003/README.md`, `closures/DQ-006_CLOSURE_PACKAGE.md`  
**Purpose:** Maintain one explicit CK-003 status register for the DQ items that still control specification stabilization.

---

## 1. Status model

This register uses only the following states:

- `OPEN` — the decision or closure work remains incomplete, but the next steps are known
- `BLOCKED` — final closure is prevented by a missing prerequisite outside the item itself
- `READY` — the semantic contract is sufficiently defined for the next controlled promotion step
- `CLOSED` — the item is explicitly closed by an authoritative record

The register does not itself grant closure. It summarizes the authoritative state already recorded elsewhere.

---

## 2. Active CK-003 DQ register

| Item | State | Why this state | Immediate blocker / next act | Governing source |
|---|---|---|---|---|
| DQ-002 — hash-domain closure | `CLOSED` | `closures/DQ-002_FINAL_CLOSURE.md` records `CLOSED / PASS`. The protocol hash-domain contract is frozen in the specification corpus. | No immediate specification-side action required for APS stabilization. Monitor only because DQ-006 records an inherited evidentiary caveat against the basis of the closure. | `closures/DQ-002_FINAL_CLOSURE.md` |
| DQ-003 — version semantics | `READY` | The semantic split between `protocol_version` and `schema_version` is already present in APS-001 / APS-200, and the repository now has an explicit compatibility matrix, a bound fixture, and a local CONF-008 gate. | Run the same matrix against RI-PY / RI-RS and promote it from local draft use to approved evidence. | `ck003/decisions/DQ-003/current_versioning_snapshot.md` |
| DQ-004 — event-type semantics | `READY` | The semantic contract is defined, the repository now has one controlled draft registry token, a bound fixture, and a local CONF-012 gate. | Extend the registry beyond the local draft token and collect RI-PY / RI-RS evidence before release-grade closure. | `ck003/DQ-004_EVENT_TYPE_SEMANTICS.md`, `aps/EVENT_TYPE_REGISTRY.md` |
| DQ-006 — canonical serialization closure | `OPEN` | The normative decision is settled in APS-200 §8 / APS-300 §5, but the conformance-evidence and procedural closure criteria remain unmet. | Execute R1–R4: discriminating fixture, single RI-RS boundary, reachable evidence, Chief Architect ratification. | `closures/DQ-006_CLOSURE_PACKAGE.md`, `ck003/dq-006-final-closure-execution/DQ-006_FINAL_CLOSURE_EXECUTION_ORDER.md` |

---

## 3. DQ-006 residual register

DQ-006 is the only CK-003 item whose remaining work is already decomposed into named residuals.

| Residual | State | Meaning | Source |
|---|---|---|---|
| DQ6-R1 — JCS-discriminating fixture | `OPEN` | CANONICAL-001 proves equality, but not RFC 8785 discrimination. A cross-language discriminating vector must be executed. | `closures/DQ-006_CLOSURE_PACKAGE.md` §13; `ck003/dq-006-final-closure-execution/DQ-006_FINAL_CLOSURE_EXECUTION_ORDER.md` §3 |
| DQ6-R2 — RI-RS boundary of record | `OPEN` | One authoritative RI-RS conformance boundary must be selected and competing implementations explicitly disposed of. | `closures/DQ-006_CLOSURE_PACKAGE.md` §13; `ck003/handover-assessment/04_CONFLICT_REGISTER.md` CFL-003 |
| DQ6-R3 — evidence reachability | `OPEN` | The cited RI-PY / RI-RS evidence is not reachable from default/reviewable branches. | `closures/DQ-006_CLOSURE_PACKAGE.md` §13; `ck003/handover-assessment/05_EVIDENCE_GAPS.md` EG-01 |
| DQ6-R4 — governance ratification | `OPEN` | No implementation evidence may self-promote DQ-006 to closed without Chief Architect ratification. | `closures/DQ-006_CLOSURE_PACKAGE.md` §13; `ck003/dq-006-final-closure-execution/DQ-006_FINAL_CLOSURE_EXECUTION_ORDER.md` §3 |

DQ-006 is **not BLOCKED** at the specification-decision layer. Its remaining work is executable and already named; what remains is evidence, reachability, and ratification.

---

## 4. Minimal DQ set required for further specification stabilization

The minimal CK-003 set that still controls further stabilization of the specification is:

1. **DQ-003**
   - needed for APS-001 §12, APS-200 version binding, compatibility rules, and version fixtures
2. **DQ-004**
   - needed for APS-200 `ENT-007`, CONF-012, event-type fixtures, and auditability closure
3. **DQ-006 residuals**
   - needed to convert canonical-serialization closure from settled contract + partial evidence into reviewable conformance closure

`DQ-002` does **not** need to be reopened as part of the minimal working set for current specification stabilization. It remains closed in the specification corpus, while any inherited evidentiary concern is already captured as a dependency note inside DQ-006.

---

## 5. Recommended execution order

For the specification repository, the controlled order is:

1. close **DQ-004** event-type registry + fixtures
2. execute **DQ6-R1…R4** for DQ-006
3. promote **DQ-003** from local draft gate to RI-backed approval evidence

This order best supports the current APS blockers:

- APS-001 §12 depends directly on DQ-003
- APS-200 `ENT-007` / audit semantics depend directly on DQ-004
- APS-200 §8 / APS-300 §5 already hold the normative DQ-006 contract, so the remaining DQ-006 work is evidentiary and procedural rather than semantic

---

## 6. Relationship to WP-3

This file is the WP-3 deliverable:

- one explicit CK-003 register
- one status per active DQ item using `OPEN / BLOCKED / READY / CLOSED`
- one minimal DQ set for continued specification stabilization

It records status; it does not itself resolve any blocker.

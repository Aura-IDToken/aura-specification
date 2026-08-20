# CK-003 Specification Closure Workspace

Controlled workspace for closing the Aura Protocol specification.

## Authority

Normative authority remains with the approved Constitution, APS documents, approved ADRs, and the specification itself. Artifacts in this directory are classified explicitly and do not become normative merely by being present here.

## Closure gates

- **GATE A — Specification Closure:** APS-001, DQ-002, DQ-003, DQ-004, semantic decision space, canonical serialization, hash-domain, version semantics, event-type semantics.
- **GATE B — Conformance:** INV-001…INV-015 mapping, canonical fixtures, RI-PY, RI-RS, and cross-language equality.
- **GATE C — Automation:** conformance runner, specification/core/guard CI gates, and evidence artifacts.
- **GATE D — Release:** traceability, security/threat review, regulatory mapping, architecture review, and freeze for Aura specification v1.0.

## Status vocabulary

`NORMATIVE` · `DECISION` · `EVIDENCE` · `TEST` · `WORKING` · `SUPERSEDED` · `OPEN` · `CLOSED` · `BLOCKED`

## Existing CK-003 evidence

DQ-002 already has a dedicated evidence package under `ck003/dq-002-hash-domain/`. DQ-003 work is maintained on its dedicated branch until consolidated into the closure branch.

## Canonical serialization — normative outcome

**The canonical serialization contract is `aps/APS-200_CANONICAL_DATA_MODEL.md` §8**
(RFC 8785 / JCS). It is the single authoritative source. Nothing in this directory
is normative, this README included.

CK-003 reconciliation, the fourteen-question answer table, the full matrix, the
CK003-001…010 register, the normative/informative boundary and the conflict
disposition are in `ck003/CK003_CANONICAL_SERIALIZATION_RECONCILIATION.md`.

Four artifacts under `ck003/dq-006-canonical-serialization/` are marked
SUPERSEDED and the governing ADR is marked ENACTED. All five are retained as the
decision trail; the superseded four must not be cited as current status.

## DQ-006 closure

`ck003/dq-006-closure/` contains the closure package for DQ-006 / CROSS-LANGUAGE-001. The package records independent RI-PY and RI-RS CANONICAL-001 execution, byte/SHA/leaf equality, negative controls, provenance and production-integrity evidence.

**DQ-006 status: CLOSED.**

This does not by itself close DQ-002, APS-001, INV-001…INV-015, or the release gate.

## Conflict register

`ck003/handover-assessment/04_CONFLICT_REGISTER.md` records five conflicts routed
to the Protocol Custodian. CK-003 resolved one by classification (CFL-002) and
left CFL-001, CFL-003, CFL-004 and CFL-005 open, with their disposition recorded
in §8 of the reconciliation document. No agent may resolve the remaining four.

## Operating rule

No production implementation change is implied by a CK-003 evidence artifact. Normative decisions are promoted only after review, fixture verification, and explicit closure status.

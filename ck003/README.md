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

## DQ-006 closure

`ck003/dq-006-closure/` contains the closure package for DQ-006 / CROSS-LANGUAGE-001. The package records independent RI-PY and RI-RS CANONICAL-001 execution, byte/SHA/leaf equality, negative controls, provenance and production-integrity evidence.

**DQ-006 status: CLOSED.** The repository-level decision of record, carrying the DQ6-C01…DQ6-C13 closure matrix, is `evidence/DQ-006_CLOSURE_PACKAGE.md`.

This does not by itself close DQ-002, APS-001, INV-001…INV-015, or the release gate.

## Operating rule

No production implementation change is implied by a CK-003 evidence artifact. Normative decisions are promoted only after review, fixture verification, and explicit closure status.

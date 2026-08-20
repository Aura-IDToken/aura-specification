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

The single authoritative DQ-006 record is [`closures/DQ-006_CLOSURE_PACKAGE.md`](../closures/DQ-006_CLOSURE_PACKAGE.md). Everything under `ck003/dq-006-closure/` and `ck003/dq-006-canonical-serialization/` is superseded working history and MUST NOT be cited as current status.

The normative canonical serialization rule lives in **APS-200 §8** (single authority), with the evidence-hash byte domain in **APS-300 §5**, the decision in **ADR-CK003-DQ006**, and the conformance requirement in **CONF-003**.

**DQ-006 status: CLOSED** (2026-08-20).

Cross-language byte, SHA-256 and RFC 6962 leaf equality is executed and PASS on **two** fixtures: CANONICAL-001 and the JCS-discriminating CANONICAL-002. CANONICAL-001 alone is JCS-degenerate — a sorted-JSON serializer reproduces its canonical bytes — so it evidences agreement; CANONICAL-002 separates RFC 8785 from that serializer and is what evidences conformance.

Consolidated evidence: [`dq-006-closure/DQ-006_EVIDENCE.md`](dq-006-closure/DQ-006_EVIDENCE.md). Traceability: [`dq-006-closure/DQ-006_TRACEABILITY.md`](dq-006-closure/DQ-006_TRACEABILITY.md). Carried items C-1…C-3 are listed in the closure package §13; all are repository hygiene, none qualifies the decision.

Both JCS engines remain conformance-scoped. This closure does not state that production Core or Guard uses JCS.

This does not by itself close DQ-002, APS-001, INV-001…INV-015, or the release gate.

## Operating rule

No production implementation change is implied by a CK-003 evidence artifact. Normative decisions are promoted only after review, fixture verification, and explicit closure status.

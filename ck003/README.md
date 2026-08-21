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

## DQ-002 closure

The single authoritative DQ-002 record is [`closures/DQ-002_FINAL_CLOSURE.md`](../closures/DQ-002_FINAL_CLOSURE.md). Everything under `ck003/dq-002-hash-domain/` is subordinate evidence and MUST NOT be cited as current status.

The normative hash-domain model lives in **APS-001 §7.1–§7.2** (single authority), with the input byte domain bound in **APS-200 §8.5** and the evidence/Merkle domain separation in **APS-300 §5.2**.

**DQ-002 status: BLOCKED** — contract settled, closure evidence insufficient.

Revalidated against the DQ-006 canonical boundary on 2026-08-21: DQ-006 introduces no new hash dependency and does not change the algorithm, the leaf domain or the node domain. Canonical bytes → SHA-256 → RFC 6962 leaf re-executes clean across RI-PY and RI-RS, with 41/41 revalidation checks and 18 negative controls. Closure is withheld because both DQ-002 ADRs are still `PROPOSED`, APS-001 §7.2 defers odd-node behaviour to an "approved Aura Merkle profile" that does not exist, `DEFECT-DQ002-F1/F2/F3` are open, no DQ-002 CI gate has ever executed successfully, and the depended-upon DQ-006 gate is itself OPEN. Residuals R-1…R-10 are listed in the closure record §12.

This does not by itself close APS-001, DQ-003, DQ-004, INV-001…INV-015, or the release gate.

## DQ-006 closure

The single authoritative DQ-006 record is [`closures/DQ-006_CLOSURE_PACKAGE.md`](../closures/DQ-006_CLOSURE_PACKAGE.md). Everything under `ck003/dq-006-closure/` and `ck003/dq-006-canonical-serialization/` is superseded working history and MUST NOT be cited as current status.

The normative canonical serialization rule lives in **APS-200 §8** (single authority), with the evidence-hash byte domain in **APS-300 §5**, the decision in **ADR-CK003-DQ006**, and the conformance requirement in **CONF-003**.

**DQ-006 status: OPEN** — specification closure complete; conformance evidence partial.

Cross-language byte, SHA-256 and RFC 6962 leaf equality on CANONICAL-001 is executed and PASS. Closure is withheld because CANONICAL-001 is JCS-degenerate (it cannot distinguish RFC 8785 from sorted JSON), the evidence is unmerged in both reference repositories, and the verdict is unratified. Residuals R1–R4 are listed in the closure package §13.

This does not by itself close DQ-002, APS-001, INV-001…INV-015, or the release gate.

## Operating rule

No production implementation change is implied by a CK-003 evidence artifact. Normative decisions are promoted only after review, fixture verification, and explicit closure status.

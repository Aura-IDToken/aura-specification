# CK-003 Architecture Execution Audit — 2026-08-20

**Classification:** Non-normative execution audit  
**Scope:** `aura-specification`, `aura-poc-a-core-v3.3`, `aura-guard-v1.3`  
**Purpose:** Reconcile the repository state after DQ-006/CROSS-LANGUAGE-001 and define the controlled execution sequence toward Aura Protocol v1.0.

## 1. Executive verdict

The project has crossed an important conformance boundary: CANONICAL-001 has been independently executed in RI-PY and RI-RS and CROSS-LANGUAGE-001 is PASS. DQ-006 is recorded CLOSED / PASS and DQ-002 is recorded CLOSED / PASS.

The repositories are **not yet release-ready** and `aura-specification v1.0` MUST remain unapproved. The principal remaining blockers are DQ-003 version binding, DQ-004 event-type vocabulary/registry approval, complete INV-001…INV-015 execution evidence, complete APS-500 fixture coverage, repository-native CI, and final Architecture Review.

## 2. Repository observations

### aura-specification

The repository contains the normative APS layer, conformance definitions, fixture corpus, CK-003 closure workspace, DQ-002/DQ-006 closure packages, reference implementation descriptions and a Gate A execution matrix.

The audit identified stale closure-state language in the Gate A and invariant matrix relative to the now-recorded DQ-002/DQ-006 closures. This branch reconciles those working-control documents without claiming full specification closure.

### aura-poc-a-core-v3.3

RI-PY has produced independent JCS conformance evidence for CANONICAL-001 using `rfc8785==0.1.4`. Production `core/` and `audit/` paths were reported unchanged by the CROSS-LANGUAGE-001 execution.

### aura-guard-v1.3

RI-RS has produced independent JCS conformance evidence for CANONICAL-001 using `serde_json_canonicalizer==0.3.2` in a conformance-only package. Production `src/`, root `Cargo.toml` and root `Cargo.lock` were reported unchanged by the CROSS-LANGUAGE-001 execution.

## 3. Closed decisions

| Decision | Status | Evidence basis |
|---|---|---|
| DQ-006 | CLOSED / PASS | RI-PY + RI-RS CANONICAL-001; CROSS-LANGUAGE-001 |
| DQ-002 | CLOSED / PASS | Independent hash-domain evidence + canonical-byte binding |

These closures are decision records. They do not imply full invariant or release conformance.

## 4. Open decisions / blockers

### DQ-003 — Version semantics

`protocol_version` identifies the normative protocol contract; `schema_version` identifies the representation/schema contract. The repository still requires an explicit compatibility matrix, binding fixtures and implementation evidence. No compatibility rule may be inferred from numeric version ordering.

### DQ-004 — Event-type semantics

The semantic contract and validation rules are defined, but the normative vocabulary is not approved. The event registry deliberately avoids promoting implementation-derived tokens into protocol authority. Final closure requires approved entries, payload contracts and executable positive/negative fixtures.

### APS-300 evidence binding

The canonical/hash closure is established, but Evidence Pack cryptographic binding still requires reconciliation against the frozen canonical-byte and hash-domain contract.

### INV-001…INV-015

All five previously missing CONF mappings are now defined (`CONF-011`…`CONF-015`) and corresponding fixtures exist. This is not equivalent to PASS. Each invariant still requires actual RI-PY/RI-RS evidence at the coverage level specified by its conformance contract.

### APS-500

The repository contains a partial corpus including the CK-003 invariant fixtures and CANONICAL-001. Full APS-500 coverage is not yet demonstrated.

### CI

A repository-native specification conformance gate is still required. The existence of conformance documents and fixtures is not itself a CI gate.

### Release

Architecture Review, final traceability, security/regulatory review and release evidence remain outstanding.

## 5. Changes executed on this branch

1. APS-200 §8 was reconciled with the verified DQ-006 canonical serialization/hash contract.
2. APS-200 now identifies RFC 8785 JCS as the current normative JSON canonicalization profile and records the canonical-byte, SHA-256 and RFC 6962 leaf boundaries.
3. APS-200 explicitly preserves the production boundary: the named JCS engines are conformance-only reference engines.
4. Gate A was refreshed to distinguish CLOSED decisions from incorporated normative APS text and remaining blockers.
5. INV-001…INV-015 matrix was reconciled with current DQ-002/DQ-006 evidence and the existence of CONF-011…CONF-015/fixtures.

No production implementation repository was modified by this specification-branch execution.

## 6. Controlled next sequence

```text
APS-200 §8 reconciliation
        ↓
DQ-003 version-binding closure
        ↓
DQ-004 event-type vocabulary closure
        ↓
APS-300 evidence-binding reconciliation
        ↓
INV-001…INV-015 execution closure
        ↓
complete APS-500 / canonical fixture corpus
        ↓
RI-PY full corpus
        ↓
RI-RS full corpus
        ↓
cross-language corpus equality
        ↓
specification CI gate
        ↓
core CI gate
        ↓
guard CI gate
        ↓
traceability + security/regulatory review
        ↓
Architecture Review
        ↓
FREEZE
        ↓
aura-specification v1.0
```

## 7. Architectural guardrails

- No production JCS dependency is authorized by DQ-006.
- No implementation behaviour may be promoted to normative semantics without an explicit specification decision.
- No PASS may be inferred from expected constants alone.
- BLOCKED remains distinct from PASS.
- Partial fixture coverage remains PARTIAL.
- Every release claim must terminate in executable evidence and traceability.

## 8. Final audit verdict

**Architecture state:** ADVANCING / NOT RELEASE-READY.  
**DQ-006:** CLOSED / PASS.  
**DQ-002:** CLOSED / PASS.  
**Gate A:** OPEN.  
**APS-001:** DRAFT / NOT APPROVED.  
**Aura Protocol v1.0:** NOT RELEASED.

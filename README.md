# Aura Protocol Specification

> **The single canonical source of truth for the Aura Protocol.**

[![Status: Active](https://img.shields.io/badge/status-active-green.svg)](CHANGELOG.md)
[![Constitution: FROZEN](https://img.shields.io/badge/constitution-FROZEN-blue.svg)](constitution/AURA_CONSTITUTION.md)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey.svg)](LICENSE)

---

## What Is This Repository?

`aura-specification` is the normative documentation repository for the **Aura Protocol** — an open, deterministic trust layer for AI systems. It contains no implementation code.

It is designed in the tradition of IETF RFCs, W3C specifications, and Kubernetes Enhancement Proposals: every protocol behavior is fully specified, versioned, and traceable before any implementation is written or changed.

**If documentation and implementation disagree, documentation wins.**

---

## Repository Map

```
aura-specification/
├── constitution/          Constitutional governance documents
├── specification/         Top-level protocol specification (APS-001)
├── aps/                   Numbered APS normative documents
├── invariants/            Protocol Invariant registry
├── conformance/           Conformance Test Matrix (APS-400)
├── fixtures/              Reference Fixtures (APS-500)
├── evidence/              Evidence Model and templates (APS-300)
├── compliance/            Compliance Mapping (APS-900)
├── adrs/                  Architecture Decision Records
├── rfcs/                  Requests for Comments
├── reference/             Reference Implementation Requirements (APS-950)
├── glossary/              Canonical terminology (APS-000)
├── diagrams/              Architecture and flow diagrams
├── templates/             Document templates
├── examples/              Usage examples and walkthroughs
├── scripts/               Tooling for traceability and validation
└── releases/              Release artifacts and conformance reports
```

---

## Current Repository State

- **Canonical / active**: `constitution/`, `specification/`, `aps/`, `invariants/`, `conformance/`, `fixtures/`, `evidence/`, `compliance/`, `reference/`, `adrs/`, `rfcs/`, `arc/`
- **Working / closure support**: `ck003/`, `closures/`, `docs/completion/` — these track remediation, evidence, and planning work; they are not authoritative protocol status by themselves
- **Historical / provenance-only**: root `*.pdf` / `*.txt` source imports and historical release snapshots under `releases/`; they are retained for provenance and audit, not as the current canonical state

When current status conflicts with a historical snapshot, use the canonical Markdown corpus and the current completion/roadmap documents.

Current status pointers:
- **Governance / status index**: [`GOVERNANCE_STATUS_INDEX.md`](GOVERNANCE_STATUS_INDEX.md)
- **Authority binding of record**: [`AUTHORITY_BINDING_RECORD_v1.1.md`](AUTHORITY_BINDING_RECORD_v1.1.md)
- **DQ-006 closure status of record**: [`closures/DQ-006_CLOSURE_PACKAGE.md`](closures/DQ-006_CLOSURE_PACKAGE.md)

---

## Specification Documents

| Document | Title | Status |
|----------|-------|--------|
| [AURA Constitution](constitution/AURA_CONSTITUTION.md) | Constitutional Governance | FROZEN |
| [APS-000](aps/APS-000_FOUNDATION_AND_TERMINOLOGY.md) | Foundation & Terminology | DRAFT |
| [APS-001](specification/APS-001_PROTOCOL_SPECIFICATION.md) | Protocol Specification | DRAFT — ARCHITECTURE REVIEW REQUIRED |
| [APS-100](aps/APS-100_PROTOCOL_INVARIANTS.md) | Protocol Invariants | DRAFT |
| [APS-200](aps/APS-200_CANONICAL_DATA_MODEL.md) | Canonical Data Model | DRAFT |
| [APS-300](aps/APS-300_EVIDENCE_MODEL.md) | Evidence Model | DRAFT |
| [APS-400](aps/APS-400_CONFORMANCE_TEST_MATRIX.md) | Conformance Test Matrix | DRAFT |
| [APS-500](aps/APS-500_REFERENCE_FIXTURES.md) | Reference Fixtures | DRAFT |
| [APS-900](aps/APS-900_COMPLIANCE_MAPPING.md) | Compliance Mapping | DRAFT |
| [APS-950](aps/APS-950_REFERENCE_IMPLEMENTATION_REQUIREMENTS.md) | Reference Implementation Requirements | DRAFT |

---

## Canonical Document Hierarchy

```
AURA Constitution (FROZEN)
        ↓
APS-001 Protocol Specification
        ↓
APS-100 Protocol Invariants
        ↓
APS-200 Canonical Data Model  ←→  APS-300 Evidence Model
        ↓
APS-400 Conformance Test Matrix
        ↓
APS-500 Reference Fixtures
        ↓
APS-900 Compliance Mapping
        ↓
APS-950 Reference Implementation Requirements
```

Higher documents have authority over lower documents. No implementation may contradict any document in this hierarchy.

---

## Traceability Model

Every protocol requirement is traceable end-to-end:

```
Constitution Principle
        ↓
APS Requirement
        ↓
Protocol Invariant (INV-xxx)
        ↓
Canonical Data Model Entity (ENT-xxx)
        ↓
Evidence Object (EVID-xxx)
        ↓
Conformance Test (CONF-xxx)
        ↓
Reference Fixture (FIX-xxx)
        ↓
Reference Implementation
        ↓
Release + Conformance Report
```

See [compliance/TRACEABILITY_MODEL.md](compliance/TRACEABILITY_MODEL.md) for the full model.

---

## Protocol Invariants

15 invariants govern all conformant implementations. A violation of any invariant is a conformance failure.

| ID | Title | Class |
|----|-------|-------|
| INV-001 | Deterministic Evaluation | Critical |
| INV-002 | Bit-Perfect Replay | Critical |
| INV-003 | Canonical Serialization | Critical |
| INV-004 | Immutable Evidence | Critical |
| INV-005 | Evidence Traceability | Critical |
| INV-006 | Platform Independence | Critical |
| INV-007 | Zero Float Runtime | Critical |
| INV-008 | Fail Closed | Critical |
| INV-009 | Version Consistency | Major |
| INV-010 | Conformance Completeness | Critical |
| INV-011 | Cryptographic Integrity | Critical |
| INV-012 | Auditability | Critical |
| INV-013 | Policy Determinism | Critical |
| INV-014 | Reference Compatibility | Critical |
| INV-015 | Canonical Identity | Major |

See [invariants/INVARIANT_REGISTRY.md](invariants/INVARIANT_REGISTRY.md) for full definitions.

---

## Reference Implementations

| ID | Repository | Language | Role |
|----|-----------|----------|------|
| RI-PY | [aura-poc-a-core](https://github.com/AuraIDToken/aura-poc-a-core-v3.3) | Python | Deterministic measurement engine (Layer 0) |
| RI-RS | [aura-guard](https://github.com/AuraIDToken/aura-guard-v1.3) | Rust | Audit middleware with hash-chained evidence log |

See [reference/README.md](reference/README.md) for conformance status.

---

## Governance

- **Chief Architect**: holds sole approval authority over canonical documents
- **AI Assistants**: may propose, implement, and test — may not approve or freeze documents
- **ADR process**: all architectural decisions documented in [adrs/](adrs/)
- **RFC process**: all protocol change proposals documented in [rfcs/](rfcs/)

See [GOVERNANCE.md](GOVERNANCE.md) for the full governance model.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose changes, author specifications, and submit RFCs.

See [STYLE_GUIDE.md](STYLE_GUIDE.md) for document formatting conventions.

---

## Organization

| Repository | Description |
|------------|-------------|
| [`AuraIDToken/aura-specification`](https://github.com/AuraIDToken/aura-specification) | This repository |
| [`AuraIDToken/aura-poc-a-core-v3.3`](https://github.com/AuraIDToken/aura-poc-a-core-v3.3) | Python reference implementation |
| [`AuraIDToken/aura-guard-v1.3`](https://github.com/AuraIDToken/aura-guard-v1.3) | Rust reference implementation |

---

## Motto

> *Specification creates trust.*
> *Conformance preserves trust.*
> *Evidence proves trust.*

---

## License

Documentation: [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).

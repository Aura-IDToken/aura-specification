# Diagrams

This directory contains architecture and flow diagrams for the Aura Protocol.

## Naming

- Mermaid source: `DIAGRAM-NNN_TITLE.mermaid`
- SVG/PNG exports: `DIAGRAM-NNN_TITLE.svg`
- Companion description: `DIAGRAM-NNN_TITLE.md`

## Current Diagrams

| ID | Title | Format |
|----|-------|--------|
| DIAGRAM-001 | Canonical Document Hierarchy | Mermaid |
| DIAGRAM-002 | Traceability Chain | Mermaid |
| DIAGRAM-003 | Protocol Execution Lifecycle | TODO |
| DIAGRAM-004 | Evidence Pack Structure | TODO |

---

## DIAGRAM-001 — Canonical Document Hierarchy

```mermaid
graph TD
    CON["AURA Constitution (FROZEN)"]
    APS001["APS-001 Protocol Specification (DRAFT)"]
    APS100["APS-100 Protocol Invariants"]
    APS200["APS-200 Canonical Data Model"]
    APS300["APS-300 Evidence Model"]
    APS400["APS-400 Conformance Test Matrix"]
    APS500["APS-500 Reference Fixtures"]
    APS900["APS-900 Compliance Mapping"]
    APS950["APS-950 Ref. Impl. Requirements"]

    CON --> APS001
    APS001 --> APS100
    APS100 --> APS200
    APS100 --> APS300
    APS200 --> APS400
    APS300 --> APS400
    APS400 --> APS500
    APS500 --> APS900
    APS900 --> APS950
```

---

## DIAGRAM-002 — Traceability Chain

```mermaid
graph TD
    CP["Constitution Principle"]
    REQ["APS Requirement"]
    INV["Protocol Invariant (INV-xxx)"]
    ENT["Data Model Entity (ENT-xxx)"]
    EVID["Evidence (EVID-xxx)"]
    CONF["Conformance Test (CONF-xxx)"]
    FIX["Reference Fixture (FIX-xxx)"]
    RI["Reference Implementation"]
    REL["Release (REL-xxx)"]

    CP --> REQ
    REQ --> INV
    INV --> ENT
    ENT --> EVID
    EVID --> CONF
    CONF --> FIX
    FIX --> RI
    RI --> REL
```

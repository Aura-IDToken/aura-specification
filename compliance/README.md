# Compliance

This directory contains the Compliance Mapping artifacts, supplementing APS-900.

## Documents

| File | Description |
|------|-------------|
| [TRACEABILITY_MODEL.md](TRACEABILITY_MODEL.md) | Full description of the traceability model |
| [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) | Machine-readable traceability matrix |
| [DQ-002_TRACEABILITY_MATRIX.md](DQ-002_TRACEABILITY_MATRIX.md) | DQ-002 hash-domain traceability matrix (evidence, non-normative) |
| [DQ-002_TRACEABILITY_REVIEW.md](DQ-002_TRACEABILITY_REVIEW.md) | DQ-002 traceability audit findings (evidence, non-normative) |

## Purpose

Compliance Mapping connects every normative requirement to its evidence of fulfillment. A complete traceability chain is required for certification.

## Full Traceability Chain

```
AURA Constitution Principle
        ↓
APS Requirement (APS-001 through APS-950)
        ↓
Protocol Invariant (INV-xxx)
        ↓
Canonical Data Model Entity (ENT-xxx)
        ↓
Evidence Object / Evidence Pack (APS-300)
        ↓
Conformance Test (CONF-xxx)
        ↓
Reference Fixture (FIX-xxx)
        ↓
Reference Implementation
        ↓
Release (REL-xxx)
```

A missing link anywhere in this chain means an incomplete compliance path.

See [../aps/APS-900_COMPLIANCE_MAPPING.md](../aps/APS-900_COMPLIANCE_MAPPING.md) for the full specification.

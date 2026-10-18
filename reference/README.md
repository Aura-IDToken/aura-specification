# Reference Implementations

This directory contains conformance status and documentation for Aura Protocol Reference Implementations, as defined in APS-950.

## Implementations

| ID | Repository | Language | Role | APS-950 Status |
|----|-----------|----------|------|----------------|
| [RI-PY](RI-PY_AURA_POC_A_CORE.md) | [aura-poc-a-core-v3.3](https://github.com/AuraIDToken/aura-poc-a-core-v3.3) | Python | Deterministic measurement engine (Layer 0) | PARTIAL |
| [RI-RS](RI-RS_AURA_GUARD.md) | [aura-guard-v1.3](https://github.com/AuraIDToken/aura-guard-v1.3) | Rust | Audit middleware with hash-chained evidence log | PARTIAL |
| RI-TEST | Planned | TBD | Cross-implementation fixture validation | PLANNED |

## Conformance Summary

> **Status**: Neither implementation is yet fully conformant with the complete APS. The specification remains authoritative; RI-PY and RI-RS are assessed against it and do not redefine it. See individual files for detailed gap analysis.

## Adding a New Implementation

A new implementation MAY be recognised as a Reference Implementation only after:
1. Passing all mandatory APS-400 Conformance Tests
2. Generating a valid Evidence Pack (APS-300)
3. Satisfying all APS-950 requirements
4. Completing an Architecture Review (ARR published)
5. Chief Architect approval

See [../aps/APS-950_REFERENCE_IMPLEMENTATION_REQUIREMENTS.md](../aps/APS-950_REFERENCE_IMPLEMENTATION_REQUIREMENTS.md).

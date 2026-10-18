# APS-950 — Reference Implementation Requirements

Document ID: APS-950  
Version: 1.0-DRAFT  
Status: DRAFT  
Classification: Normative Implementation Specification  
Authority: APS-001 §9, §13 · APS-100 · APS-200 · APS-300 · APS-400 · APS-500 · APS-900  
Last Review: 2026-09-26

---

## 1. Purpose

APS-950 defines the requirements for Reference Implementations of the Aura Protocol.

A Reference Implementation serves as the conformance exemplar for all other implementations.

---

## 2. Objectives

A Reference Implementation MUST:
- Implement all mandatory APS requirements
- Pass the full Conformance Test suite (APS-400)
- Generate a valid Evidence Pack (APS-300)
- Maintain full Protocol Invariant compliance (APS-100)
- Enable independent audit

---

## 3. Required Components

| ID | Component | Status |
|----|-----------|--------|
| RI-001 | Protocol Engine | REQUIRED |
| RI-002 | Validation Layer | REQUIRED |
| RI-003 | Evidence Generator | REQUIRED |
| RI-004 | Conformance Runner | REQUIRED |
| RI-005 | Fixture Loader | REQUIRED |
| RI-006 | Audit Interface | REQUIRED |
| RI-007 | Version Information | REQUIRED |

---

## 4. Repository Requirements

A Reference Implementation repository MUST contain:

```
/docs          — Architecture and design documentation
/spec          — Links or copies of applicable APS documents
/tests         — All test types (unit, integration, conformance, replay, evidence, security)
/fixtures      — APS-500 canonical fixtures
/src           — Source code
/examples      — Usage examples
/LICENSE       — License file
/CHANGELOG     — Version history
/README        — Entry point documentation
```

---

## 5. Coding Requirements

Implementation MUST:
- Be deterministic (INV-001)
- Be replayable (INV-002)
- Not violate Protocol Invariants
- Have complete unit tests
- Have APS-400 Conformance Tests

---

## 6. Build Requirements

The build process MUST:
- Be reproducible (same source → same binary/artifact)
- Be versioned
- Document all dependencies
- Support a clean build from source

---

## 7. Test Requirements

Before release, an implementation MUST pass:
- Unit Tests
- Integration Tests
- Conformance Tests (all CONF-xxx)
- Replay Tests
- Evidence Validation
- Security Validation

---

## 8. Documentation Requirements

Each implementation MUST include:
- README with build and run instructions
- Architecture description
- APS mapping (which APS requirements are implemented)
- List of supported protocol versions
- Known limitations

---

## 9. Release Requirements

Each release MUST include:
- Semantic version number
- Compatibility Statement (which APS version is supported)
- Conformance Report
- Evidence Pack from Conformance Run
- Release Notes

---

## 10. Certification

An implementation MAY be marked Aura Reference Implementation if:
- All APS-950 requirements are satisfied
- All mandatory APS-400 tests return PASS
- Complete documentation is present
- An Architecture Review has been conducted (ARR published)

---

## 11. Supported Reference Implementations

| ID | Repository | Language | Role | Status |
|----|-----------|----------|------|--------|
| RI-PY | [aura-poc-a-core](https://github.com/AuraIDToken/aura-poc-a-core-v3.3) | Python | Deterministic measurement engine (Layer 0) | Active |
| RI-RS | [aura-guard](https://github.com/AuraIDToken/aura-guard-v1.3) | Rust | Audit middleware with hash-chained evidence log | Active |
| RI-TEST | Reference Fixtures Runner | TBD | Cross-implementation fixture validation | Planned |

A new implementation MAY be added only after passing the full APS conformance process.

---

## 12. Governance

Changes to Reference Implementations:
- MUST be consistent with APS
- MUST pass Architecture Review
- MUST maintain Protocol Invariant compliance
- MUST be documented in ADRs and CHANGELOG

---

*Source: Original text preserved in [`APS-950 — Reference Implementation Requirements_260723_194507.txt`](../APS-950%20%E2%80%94%20Reference%20Implementation%20Requirements_260723_194507.txt)*

# Roadmap

This document describes the planned evolution of the Aura Protocol Specification.

It is maintained by the Chief Architect and updated after each Architecture Review.

---

## Current State (v0.1.x — Specification Bootstrap)

| Item | Status |
|------|--------|
| AURA Constitution | ✅ FROZEN |
| APS-000 Foundation & Terminology | 🟡 DRAFT |
| APS-001 Protocol Specification | 🟡 DRAFT — Architecture Review Required |
| APS-100 Protocol Invariants | 🟡 DRAFT |
| APS-200 Canonical Data Model | 🟡 DRAFT |
| APS-300 Evidence Model | 🟡 DRAFT |
| APS-400 Conformance Test Matrix | 🟡 DRAFT |
| APS-500 Reference Fixtures | 🟡 DRAFT |
| APS-900 Compliance Mapping | 🟡 DRAFT |
| APS-950 Ref. Impl. Requirements | 🟡 DRAFT |
| Invariant Registry | 🟡 DRAFT |
| Canonical Fixture Set | ❌ TODO |
| Conformance Runner Spec | ❌ TODO |
| Traceability Matrix | 🟡 DRAFT |

---

## Milestone 1 — APS-001 and Full Review (Target: v0.2.0)

Priority: **Critical** — APS-001 is the root normative draft and remains the principal blocker until reviewed and approved.

- [ ] Stabilize APS-001 Protocol Specification draft
- [ ] Architecture Review of APS-001
- [ ] Align APS-100 through APS-950 authority citations to APS-001
- [ ] Advance APS-000 to Approved status

### Milestone 1 — Initial Increment (M1-I1)

Scope for the first execution increment:

- [x] Define APS-001 section baseline for synchronization: §2 Execution Model, §5 Policy Model, §8 Error Handling, §9 Conformance, §11 Traceability
- [x] Synchronize authority citations in APS-100, APS-200, APS-300, APS-400, APS-500, APS-900, APS-950 to explicit APS-001 section references
- [x] Create formal change artifact for this increment in `rfcs/`
- [x] Update traceability links where APS-001 section placeholders were marked TODO
- [ ] Complete Architecture Review record (ARR) for APS-001 increment acceptance

---

## Milestone 2 — Canonical Data Model and Evidence Pack (Target: v0.3.0)

Priority: **High** — blocking conformance testing.

- [ ] Define additional APS-200 entity/profile schemas beyond the current draft working profile
- [ ] Define APS-300 canonical Evidence Pack schema with exact field names and cryptographic algorithm
- [x] Publish JSON Schema for all APS-200 entities
- [x] Publish JSON Schema for APS-300 Evidence Pack
- [ ] Advance APS-200 and APS-300 to Approved status

---

## Milestone 3 — Conformance Test Suite (Target: v0.4.0)

Priority: **High** — enables formal certification.

- [ ] Define and evidence CONF-001 through CONF-015 with full test procedures and pass/fail criteria
- [ ] Promote the working fixture corpus into a canonical APS-500 reference fixture set
- [ ] Publish machine-readable fixture format
- [ ] Advance APS-400 and APS-500 to Approved status

---

## Milestone 4 — Compliance Mapping and First Certification (Target: v1.0.0)

Priority: **Medium**.

- [ ] Automate traceability matrix generation
- [ ] Define Compliance Report format
- [ ] Conduct first Architecture Review of reference implementations against full APS
- [ ] Publish first Conformance Reports for RI-PY and RI-RS
- [ ] Advance all APS documents to Approved or Frozen status
- [ ] Release v1.0.0 of aura-specification

---

## Production Readiness Gates

Aura is **not production-ready** until all of the following are evidenced:

- [ ] APS-001 completes Architecture Review and becomes the stable root normative reference
- [ ] APS-200 and APS-300 publish exact machine-verifiable schemas and release-grade expected digests/evidence values
- [ ] APS-400 and APS-500 move from draft definitions to executable conformance coverage with canonical fixtures
- [ ] APS-900 traceability is complete from requirement to fixture, evidence, implementation, and release
- [ ] Repository-native CI enforces structural and conformance gates
- [ ] RI-PY and RI-RS complete objective certification against the same canonical fixture corpus
- [ ] Release evidence for `v1.0.0` is published without unresolved critical blockers

---

## Future Considerations

- Binary evidence envelope format
- Cross-language Evidence verifiers
- Formal verification of Protocol Invariants
- APS-600 (TODO — reserved for future use)
- APS-700 (TODO — reserved for future use)
- Kubernetes-style Enhancement Proposal (AEP) process
- Public certification program

---

## Deprecation Schedule

Historical material already exists and must remain clearly separated from active authority:

- Root `*.pdf` / `*.txt` source imports are provenance copies, not active canonical documents
- `releases/v0.1.0/` is a historical release snapshot and does not define current draft status
- Superseded or archived working records must stay out of active indexes unless explicitly restored through review

See [VERSIONING.md](VERSIONING.md) for the deprecation policy.

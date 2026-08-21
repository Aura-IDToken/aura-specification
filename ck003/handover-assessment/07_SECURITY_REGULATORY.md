# I — Security and Regulatory Gaps

**Classification:** EVIDENCE — NON-NORMATIVE

---

## I.1 What exists

| Artifact | Location | State |
|---|---|---|
| `APS-900 — Compliance Mapping` | `aps/APS-900_COMPLIANCE_MAPPING.md` | `1.0-DRAFT`, last reviewed 2026-07-23. Defines the traceability *mechanism*; carries no completed mapping. |
| Traceability matrix | `compliance/TRACEABILITY_MATRIX.md` | `1.0-DRAFT`. **Zero rows verified** for either implementation. |
| ARC → SPEC mapping | `compliance/ARC_TO_SPEC_MAPPING.md`, `compliance/arc_to_spec_mapping.yaml` | *"Reserved. Mapping will be established when SPEC-001 is approved."* **SPEC-001 does not exist.** The YAML is `mappings: []`. |
| Threat model (RI-RS) | `aura-guard-v1.3/docs/THREAT_MODEL.md` | Implementation-scoped |
| Threat model (RI-PY) | `aura-poc-a-core-v3.3/docs/threat_model.md` | Implementation-scoped |
| Regulatory notes (RI-PY) | `aura-poc-a-core-v3.3/docs/regulatory_compliance.md` | Implementation-scoped |
| Supply-chain controls (RI-RS) | `deny.toml` (license allowlist, `yanked = "deny"`, registry restricted to crates.io, `openssl-sys` banned), `cargo audit`, `cargo deny`, CodeQL, semgrep, SBOM, `attest-build-provenance` on release | **Genuinely strong** — the best-controlled surface in the program. |

## I.2 Gaps

| Gap | Verdict |
|---|---|
| **No protocol-level threat model.** Both threat models are implementation-scoped. Nothing analyses the *protocol* — canonicalization ambiguity, digest-domain confusion, version-discriminator absence, replay across protocol versions. | **OPEN** |
| **No regulatory mapping.** APS-900 defines the mechanism; the mapping is not populated, and its prerequisite (SPEC-001) does not exist. | **BLOCKED** |
| **No architecture review record.** `GOVERNANCE.md` §8 requires ARRs at `/adrs/ARR-NNN_TITLE.md`; none exist. APS-001 `0.2-DRAFT` is banner-marked *"ARCHITECTURE REVIEW REQUIRED"* and has never received one. | **BLOCKED** |
| **No signed-release integrity for the specification.** `releases/README.md` requires `CHECKSUMS.sha256` per release; `releases/v0.1.0/` has none, and no `CONFORMANCE_REPORT.md`. `SECURITY.md` names "authenticity of signed releases" as an objective with no mechanism behind it. | **OPEN** |
| **No RI-PY supply-chain controls.** `pyproject.toml` declares no dependencies and pins nothing; there is no audit, SBOM or lockfile on `main`. The asymmetry with RI-RS is total. | **OPEN** |
| **PR #59 would introduce an unaudited crate into a production dependency graph.** See CFL-003. In a program whose stated purpose is auditability, a conformance-only engine entering the production graph of the audit component is a supply-chain regression, not a paperwork detail. | **CONFLICT** |

## I.3 A scope observation worth recording

The program's stated non-goals — no recommender system, no autonomous decision engine, no
persistent social reputation, no social scoring, no identity aggregation — are actively enforced
in the implementation, not merely declared. `CONSTITUTIONAL_DECREE.md` Article I forbids
reputation aggregation and identity persistence and names `owner_id` / `wallet_id` / `user_id`
as prohibited fields, and `core/test_cr003_statelessness.py` tests history independence
executably.

This is the one place where the chain *specification → invariant → executable test* actually
holds end to end in this program. It is worth citing as the model for the rest.

---

*This document records gaps and fills none of them. It confers no normative semantics.*

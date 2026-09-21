# F / G / H — Implementation, Conformance and CI Gaps

**Classification:** EVIDENCE — NON-NORMATIVE

---

## F — Implementation gaps

### F.1 RI-PY (`aura-poc-a-core-v3.3` @ `64bf959`)

| Gap | Evidence | Status |
|---|---|---|
| Three incompatible canonicalizations | `audit/merkle.py:85` (`separators=(",",":")`) · `compliance/certificate.py:69` (default separators) · `core/merkle.py:8` (default separators) | Recorded as D-7 / P1-4 / NB-010 in the repository's own baseline audit. **BLOCKED** — resolving it selects a canonical encoding, which is exactly what D-3 forbids an agent from doing. |
| Merkle is not RFC-6962 | `audit/merkle.py:163` `sha256(left + right)` over concatenated **hex digest strings**, no domain byte; odd node duplicated at `:162` | **OPEN.** Byte-incompatible with RI-RS by construction. |
| No `protocol_version` in code | zero occurrences in any `.py` | **OPEN** — DQ-003 has no implementation surface to bind to. |
| No event-type handling | zero occurrences of `event_type` in any `.py` | **OPEN** — DQ-004 has no implementation surface. |
| `schema_version` inconsistency | `compliance/certificate.py:50` emits `"1.0.0"` (inside the fingerprint preimage); `compliance/certificate_schema.json:2` says `"1.0"`, and that schema file has zero code references | **OPEN.** |
| Package version | `pyproject.toml` `version = "0.1.0"` vs instrument "v3.3" | Open item in `RELEASE_CLOSURE_REPORT.md`. |
| No dependency pins at all | `pyproject.toml` declares no dependencies, no extras, no groups; no `requirements*.txt` on `main` | **OPEN** — the conformance-only pin the handover describes exists only on an unmerged branch. |

**Constraint on remediation.** `CONSTITUTIONAL_DECREE.md` declares this repository a frozen
regulatory measurement instrument, and Article III's Entropy Principle rejects any change that
is not a security fix, a mathematical correction, a constitutional-violation fix, or an
authorized task. Unifying the three canonicalizations is none of those until a canonical
encoding is decided. **Do not "fix" the canonicalization divergence.**

### F.2 RI-RS (`aura-guard-v1.3` @ `cd3494b`)

| Gap | Evidence | Status |
|---|---|---|
| Preimage documentation divergence | `src/models.rs:95` documents **7** fields; `src/chain.rs` implements **9** (adds `policy_hash`, `context`) | **OPEN**, verified, tracked as D-3.4. A verifier written from the docstring would compute the wrong hash. |
| No JCS boundary on `main` | no `serde_json_canonicalizer` in `Cargo.toml` or `Cargo.lock` | **OPEN** — exists only on unmerged branches, in three incompatible forms (CFL-003). |
| Chain preimage is not JSON | nine fields joined by `"\|"`, `src/chain.rs` | Not a defect — but it means DQ-006/JCS has **no bearing on the production audit chain**, which is a scope fact the closure package does not state. |
| Stale blocker document | `D3_REAL_CHAIN_EXECUTION_BLOCKER.md:15-17` says two artifacts are "deliberately absent"; both exist at repo root | **OPEN** — never amended or retracted. |
| Signer map iteration order | `src/policy.rs:104,116-119` uses `HashMap`; lookup-only today | Note, not a defect. |

**Credit where due.** This repository's fixture discipline is the strongest in the program:
every fixture carries `"DQ-002 and DQ-006 unresolved; these bytes carry no specification
standing."` and the regression harness pins that disclaimer string so it cannot be quietly
dropped. Nothing here overclaims.

---

## G — Conformance gaps

| Gap | State |
|---|---|
| Invariant closure | **0 of 15 PASS.** All OPEN; INV-003 BLOCKED on APS-200 serialization. |
| CONF coverage | CONF-001…015 exist, all DRAFT. `conformance/README.md` indexes only 001–010. CONF-009 is dual-mapped (INV-004 · INV-005) while the registry maps INV-010 → CONF-009 — the two disagree. |
| Fixture corpus | `FIX-001`'s every value is the literal `"TODO"`. Four of the five `FIX-INV-*` fixtures are self-declared blocked or parametric. `CK003-001…010` absent. `FIX-DQ004-001…004` absent. Five fixture category directories drawn in `APS-500` §10 and `fixtures/README.md` do not exist. |
| Conformance runner | Does not exist in any repository. |
| Cross-language coverage | One vector, and it does not discriminate the profile it evidences (EG-02). |
| Negative-control methodology | **Sound and worth preserving.** The RI-PY gate independently recomputes `SHA-256(bytes)` and `SHA-256(0x00 \|\| bytes)` rather than comparing two implementations' constants, and runs mutation controls. Extend this pattern; do not weaken it. |

---

## H — CI gaps

| Repository | Workflows | Conformance gate? |
|---|---|---|
| `aura-specification` | **none — `.github/workflows/` does not exist** | No. Nothing in the specification corpus is machine-verified. |
| `aura-poc-a-core-v3.3` | one: `execution-checks.yml` (determinism checks on x86_64 + arm64, cross-architecture bit-identity comparison) | No conformance, canonicalization or evidence gate. CHECKs 7–8 need Docker/pgvector that the workflow never provisions. |
| `aura-guard-v1.3` | eight: `ci` (fmt, clippy `-D warnings`, build+test `--locked`, `cargo audit`, `cargo deny`, SBOM, `d3-evidence`), `codeql`, `coverage`, `semgrep`, `rust`, `docker-image`, `release`, `ibm` | No conformance gate. The `d3-evidence` job is self-described as temporary/instrumentation-only, and it regenerates the committed artifacts without diffing them, so artifact drift would not fail CI. |

Additional CI defects:

- `aura-guard-v1.3/.github/workflows/docker-image.yml:21` runs `docker build . --file Dockerfile`;
  there is no root `Dockerfile` (only `deploy/Dockerfile`). **This workflow cannot succeed.**
- Toolchain pins disagree within one repository: `ci.yml` pins 1.86.0, `coverage.yml` pins
  1.87.0, `rust.yml` pins nothing and omits `--locked`.
- `ibm.yml` deploys to `environment: production` with a placeholder cluster name.

**The structural point.** The handover's Gate C ("conformance runner → specification CI gate →
core CI gate → guard CI gate → evidence artifacts") has not begun in the repository that most
needs it. A specification whose every claim is prose-asserted cannot gate a release.

---

*This document records gaps and fills none of them. It confers no normative semantics.*

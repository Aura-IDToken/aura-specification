# AURA — Reference Hygiene Audit (2026-10-15)

## Scope and pinned baseline

- Repository: vaidt/aura-specification
- Branch: main
- Audited baseline commit: 4a02a9edda4d5b7022e5d29f4ab89bd6897ed89d
- Snapshot: complete Git tree (316 entries, not truncated), with 231 text-bearing files fetched and decoded successfully; 165 Markdown documents were in the baseline.
- Method: local Markdown destination resolution, Markdown heading-anchor checks, empty/reference-definition checks, and scanning text artifacts for environment-dependent absolute workspace paths.

This is a repository-structure audit. It does not adjudicate normative status, authority, or conformance. External HTTP URLs were not probed for 404/redirect status in this pass.

## Findings and disposition

### Fixed in this PR

| Finding | Baseline evidence | Repair |
|---|---|---|
| Four local links pointed at planned example directories that do not exist in the Git tree | examples/README.md:13-16; the section marked each example TODO, and the only tracked file under examples/ was examples/README.md | Changed the directory labels to non-clickable planned-path text. A TODO entry should not render as a live link to a nonexistent target. |
| One stale runner-workspace path pointed to the CK-003 blocker register | docs/completion/00_MASTER_COMPLETION_PLAN.md:269 | Replaced the environment-specific filesystem path with a repository-relative Markdown link to ck003/CK003_BLOCKER_REGISTER.md. |
| One container-root path obscured a runtime-relative verifier entrypoint | traceability/AURA_PROTOCOL_IMPLEMENTATION_BINDING_MATRIX_v1.0.md:166 | Normalized the runner entrypoint to py_verifier/aura_verify.py relative to the verifier runtime root. The surrounding text still states that exact source and command evidence must be pinned per execution. |

### Intentionally not rewritten

Five absolute-path occurrences are part of three historical primary execution records, not current navigational references:

- Cross-receiver comparison record: ../../conformance/boundary/evidence/controlled-p01-handoff/CROSS-RECEIVER-COMPARISON.txt, line 2.
- RI-PY execution log: ../../conformance/boundary/evidence/controlled-p01-handoff/RI-PY-P01-EXECUTION-LOG.txt, lines 5 and 25.
- RI-RS execution log: ../../conformance/boundary/evidence/controlled-p01-handoff/RI-RS-P01-EXECUTION-LOG.txt, lines 5 and 24.

These paths record where the issued fixture was read or a receipt was written during the historical execution. Rewriting them in place would alter a source evidence record. The checker therefore preserves only the exact known path strings in these exact files; it does not make a general exception for their directories.

Two other apparent reference defects were confirmed as intentional template placeholders, not live documentation defects: APS-xxx_... and #inv-xxx in the ADR/RFC templates. The automated checker recognizes symbolic xxx/ellipsis placeholders rather than treating them as missing production targets.

## Baseline counts

| Check | Result |
|---|---:|
| Markdown files | 165 |
| Link destinations checked in the initial static pass | 294 |
| Empty link destinations | 0 |
| Undefined reference-style destinations | 0 |
| Missing local targets before repair | 4 actionable planned-directory links + 2 template placeholders |
| Non-placeholder broken Markdown anchors | 0 |
| Environment-path occurrences | 7 total: 2 repaired in Markdown, 5 retained in primary execution records |

## Automation and verification

A dependency-free checker was added at scripts/check-reference-hygiene.py with focused unit tests in tests/test_reference_hygiene.py. The existing Draft Conformance workflow now runs it and stores a machine-readable JSON report alongside the draft conformance report.

The checker fails CI on empty destinations, missing local targets, broken non-placeholder Markdown anchors, undefined reference-style links, unreadable text inputs, and unapproved environment-dependent paths. It excludes only known symbolic template placeholders and the exact historical paths enumerated above.

External URL availability remains outside this report's scope. This report and the checks are non-normative tooling; they do not change DQ-006, governance status, or implementation authorization.

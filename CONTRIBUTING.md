# Contributing to Aura Protocol Specification

Thank you for contributing to the Aura Protocol.

This repository contains **normative documentation only**. Before contributing, read the [AURA Constitution](constitution/AURA_CONSTITUTION.md), [GOVERNANCE.md](GOVERNANCE.md), and [STYLE_GUIDE.md](STYLE_GUIDE.md).

---

## Core Rule

**Specification is the source of truth. Implementation follows specification.**

Never propose changes to specifications to match existing implementations. Proposals must be justified by protocol requirements, not implementation convenience.

---

## Types of Contribution

| Type | Process |
|------|---------|
| Typo / formatting fix | Pull request → 1 review |
| Clarification (non-normative) | Pull request → 1 review |
| Draft-stage closure of an explicitly open `DRAFT` canonical contract | Pull request updating the affected APS/schema/fixture/traceability files together |
| New APS section / requirement | RFC → Architecture Review → PR |
| New Protocol Invariant | RFC → Architecture Review → PR |
| New Conformance Test | RFC → PR referencing RFC |
| New Reference Fixture | PR with fixture file + test linkage |
| Constitution amendment | RFC → Architecture Review → Chief Architect approval |

---

## Before You Start

1. Check the [ROADMAP.md](ROADMAP.md) to see if your contribution is already planned
2. Check open RFCs in [rfcs/](rfcs/) to avoid duplicate proposals
3. Review the [STYLE_GUIDE.md](STYLE_GUIDE.md) before authoring

---

## Pull Request Requirements

Every pull request that modifies a normative document MUST:

- [ ] Reference the APS section(s) affected
- [ ] Reference any Protocol Invariants affected
- [ ] Update `CHANGELOG.md`
- [ ] Update the `Last Review` date in affected document headers
- [ ] Update `compliance/TRACEABILITY_MATRIX.md` if traceability links change
- [ ] Follow the style guide

For draft-stage canonical closure work, the pull request MUST also:

- [ ] Keep the edited canonical documents in `DRAFT`
- [ ] Avoid modifying any `FROZEN` artifact
- [ ] Mark any non-release hash/checksum placeholders as draft-only rather than authoritative publication values

---

## Authoring an RFC

1. Copy [`templates/RFC_TEMPLATE.md`](templates/RFC_TEMPLATE.md)
2. Name it `RFC-NNN_SHORT_TITLE.md` (use the next available number from [rfcs/README.md](rfcs/README.md))
3. Place it in `rfcs/`
4. Fill all sections — do not leave normative sections blank
5. Open a pull request — this starts the comment period (minimum 14 days)
6. Respond to feedback by updating the RFC document
7. Do not merge your own RFC

---

## Authoring an ADR

1. Copy [`templates/ADR_TEMPLATE.md`](templates/ADR_TEMPLATE.md)
2. Name it `ADR-NNN_SHORT_TITLE.md`
3. Place it in `adrs/`
4. Fill all sections including Status, Decision, and Consequences
5. ADRs document *decisions already made* — not proposals (use RFC for proposals)

---

## What NOT to Do

- Do not invent protocol behavior — if it is not in the spec, it does not exist
- Do not write implementation code in this repository
- Do not modify FROZEN documents
- Do not merge your own non-trivial pull requests
- Do not reference external sources as authoritative (only APS documents are authoritative)
- Do not use ambiguous language — use MUST/SHOULD/MAY per RFC 2119

---

## Questions

Open a GitHub Discussion or Issue tagged with the relevant APS document number.

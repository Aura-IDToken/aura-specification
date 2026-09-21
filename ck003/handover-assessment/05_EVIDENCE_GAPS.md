# E — Evidence Gaps

**Classification:** EVIDENCE — NON-NORMATIVE

---

## EG-01 — The DQ-006 evidence base is unreachable from any default branch

**Verdict: EVIDENCE GAP**

| Cited in the closure | Repository | Commit | Reachable from `main`? | PR |
|---|---|---|---|---|
| RI-PY execution | `aura-poc-a-core-v3.3` | `49d0e4f` | **no** | none |
| RI-PY evidence | `aura-poc-a-core-v3.3` | `3e8e0e3` | **no** | none |
| RI-RS execution | `aura-guard-v1.3` | `4e9e228` | **no** | none |
| RI-RS evidence | `aura-guard-v1.3` | `420653e` | **no** | none |

The commits are real and their content is substantive — the RI-PY side adds an emitter, an
equality gate that never invokes a canonicalizer, and negative controls run against mutated
temporary copies; the RI-RS side adds a `conformance/` package with its own workspace root and
lockfile, and a `build.rs` that resolves the engine version from `Cargo.lock` rather than a
literal. This is careful work.

But evidence that lives only on an unmerged, un-PR'd branch is evidence a reviewer cannot find.
`aura-specification` also has no `conformance/corpus/` directory, so the `ri-py.json` and
`ri-rs.json` artifacts the closure references are in neither the specification repository nor
either implementation's default branch.

**What would close it:** open pull requests for both branches; land them; then reference the
merged commits.

---

## EG-02 — CANONICAL-001 does not discriminate the decision it evidences

**Verdict: EVIDENCE GAP** — full derivation in `10_INDEPENDENT_VERIFICATION.md`.

For the frozen CANONICAL-001 input, ordinary Python
`json.dumps(obj, sort_keys=True, separators=(",", ":"))` produces bytes **identical** to the
RFC 8785 output. Verified by execution.

Therefore CANONICAL-001 cannot distinguish a conforming JCS engine from a non-conforming sorted
JSON serializer: both produce the frozen bytes, the frozen SHA-256 and the frozen leaf. The
cross-language equality result is real — it demonstrates that RI-PY and RI-RS agree — but it
does not demonstrate that either implements RFC 8785, which is the decision it is cited for.

The RI-PY `test_jcs_behavior.py` suite (on branch `claude/ri-py-jcs-conformance-5anw9q`) does
carry discriminating cases per its commit record. The **cross-language bridge** does not. The
gap is at the bridge, which is the artifact the closure rests on.

**What would close it:** at least one cross-language vector whose JCS output differs from naive
sorted JSON. Candidates in `10_` §4 — offered as candidates requiring execution, not as
established values.

---

## EG-03 — `CK003-001…010` do not exist

**Verdict: EVIDENCE GAP**

`fixtures/ck003/manifest.json` lists ten fixtures, every one with `path: null` and
`LEGACY_REFERENCE_UNRESOLVED`. `fixtures/ck003/expected_digests.json` has `expected_digest:
null` for all ten. `ck003/legacy/CK003_EVIDENCE_RECONCILIATION.md:47` states:
**"CK003-001…010: NOT RECOVERED."**

Ten fixtures referenced, zero on disk. The handover is explicit that these must not be
fabricated, and they have not been. The correct next act is classification —
`LEGACY` / `SUPERSEDED` / `UNRESOLVED` — not reconstruction.

---

## EG-04 — The event-type registry is empty

**Verdict: EVIDENCE GAP** — conflict consequences in CFL-005.

`aps/EVENT_TYPE_REGISTRY.md` defines the token contract, validation semantics, the seven
required properties of an event definition record, version binding and a six-row conformance
mapping. It registers **zero tokens**. `fixtures/schemas/event_types.json` is a JSON Schema for
the registry container, not a populated registry. `FIX-DQ004-001…004`, referenced by the DQ-004
conformance mapping, do not exist.

The document is honest about this: §9 records
`DQ-004: SEMANTIC CONTRACT DEFINED / VOCABULARY REGISTRY PENDING NORMATIVE ENTRIES` and states
*"This document MUST NOT be used to claim DQ-004 PASS."*

---

## EG-05 — Zero machine verification in the specification repository

**Verdict: EVIDENCE GAP**

`.github/workflows/` **does not exist** in `aura-specification`. There are no workflows, no
gates, and none of the five validation scripts named in `scripts/README.md`
(`check-traceability.sh`, `validate-fixtures.sh`, `generate-traceability-matrix.py`,
`check-doc-headers.sh`, `check-ids.sh`) exists.

Every status, mapping and closure claim in this repository is therefore asserted by prose and
verified by nobody. `scripts/check-ids.sh` was intended to catch identifier collisions; in its
absence, three files claim `ADR-001` (`adrs/ADR-001_REPOSITORY_STRUCTURE.md`,
`adrs/ADR-001_DOCUMENT_MODEL.md`, `docs/adr/001-document-model.md`).

---

## EG-06 — Traceability records the implementations as unverified

**Verdict: EVIDENCE GAP**

`compliance/TRACEABILITY_MATRIX.md` (last reviewed 2026-07-23) shows **`NOT VERIFIED` for both
RI-PY and RI-RS on all fifteen rows**, and still shows `TODO` in the CONF column for INV-007,
012, 013, 014, 015 — which now have CONF-011…015 assigned. The matrix is both stale and, on the
substance, the most accurate statement of program state in the repository: no invariant has
implementation evidence.

---

## EG-07 — Governance-process evidence gaps carried forward

**Verdict: EVIDENCE GAP** — established by the core repository's own packages; recorded here so
they are visible from the specification side.

- `GOVERNANCE.md` §5.2 requires RFC → 14-day comment → ARB assessment → Chief Architect
  approval for changes affecting protocol behaviour. `rfcs/` is empty. CONF-011…015 were added
  without that path.
- No `ARR-NNN` architecture review record exists; APS-001 requires an Architecture Review it
  has never received.
- The Two-Key Gate, cited throughout the P0-6 records, has no repository-normative basis in
  either corpus (OQ-A-010: `EVIDENCE GAP`).
- The Custodian signature required by the Decree for `core/` changes has never been produced.

---

*This document records gaps and fills none of them. It confers no normative semantics.*

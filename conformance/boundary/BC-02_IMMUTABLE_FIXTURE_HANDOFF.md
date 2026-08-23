# BC-02 — IMMUTABLE FIXTURE HANDOFF

Document ID: BC-02
Version: 1.0-CONSTRUCTION
Status: CONSTRUCTION — NOT VALIDATED
Classification: **Engineering Boundary Contract — NON-NORMATIVE**
Layer: Boundary / transport. Not protocol authority.
Authority consumed: Fixture Registry (issuance), Boundary Specification v1 (interface shape)
Authority created: **NONE**
Date: 2026-08-23

---

## Authority notice

This document is an **engineering interface contract**. It is not a protocol
specification, not a conformance requirement, and not evidence.

It defines nothing normative. Where it appears to define a rule, that rule is a
transport-layer engineering obligation on the boundary implementation only. It
does not bind protocol semantics, does not constrain RI-PY or RI-RS protocol
behaviour, and does not create, restate, extend or reinterpret any requirement
of the Constitution, APS-000/100/200/300/400/500/900/950, the Protocol
Invariants, CONF-003, or any Conformance Test Matrix entry.

Every digest construction, status enumeration, field name and encoding rule
introduced below is a **transport artifact**, explicitly marked non-normative,
and is domain-separated from every protocol hash domain (see §5.6).

Nothing in this document authorizes conformance execution. See §18.

---

## 1. Purpose

BC-02 establishes the engineering contract under which **exactly one immutable
fixture artifact** is transferred to two independent reference implementations
(RI-PY and RI-RS), such that it can later be demonstrated — from recorded
artifacts alone — that both implementations received *the same octets*, rather
than two independently reconstructed representations that merely appear
semantically equivalent.

The question BC-02 exists to answer is narrow and precise:

> Given two implementation-side records, can an auditor conclude that the input
> was **transferred**, and rule out that it was **reconstructed**?

BC-02 answers that question and nothing else. In particular BC-02 does not, and
must not, answer:

- whether either implementation behaved correctly;
- whether a digest was produced or withheld;
- whether the fixture's declared expectation was met;
- whether any conformance requirement is satisfied.

### 1.1 Why this is needed — AS-IS observation

The current arrangement is **local-copy, not transfer**. Two concrete facts
observed in the repositories in scope:

| Observation | Location | SHA-256 of file as committed |
|---|---|---|
| RI-RS holds a repository-resident copy of the CANONICAL-001 protocol object | `Aura-IDToken/aura-guard-v1.3` → `conformance/canonical/CANONICAL-001.json` | `649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261` |
| The specification-side artifact for the same fixture identity | `Aura-IDToken/aura-specification` → `fixtures/corpus/CANONICAL-001_jcs_evidence.json` | `a6181087a85c7ae0f992362d91ab59d598b2f2db3e716f9d8ead16a2c38445d7` |

These are not the same octets, and neither is issued to the other. RI-PY carries
no resident CANONICAL-001 artifact on its default branch at all; the recorded
RI-PY execution artifact is marked `reachable_from_default_branch: false` in
`fixtures/corpus/CANONICAL-001_jcs_evidence.json`.

Under that arrangement, byte-identical outputs from the two implementations are
consistent with transfer **and** consistent with two independent local copies
that happen to agree. The evidence does not discriminate. BC-02 exists to remove
that ambiguity structurally, before any conformance execution occurs.

This observation is recorded as `BC-02-OBS-007` (§19). It is an AS-IS
observation of the engineering arrangement. It is **not** a conformance finding,
does not re-open CROSS-LANGUAGE-001, and does not alter any recorded verdict.

---

## 2. Scope

BC-02 covers, and only covers:

1. Issuance of an immutable fixture artifact from the Fixture Registry into the
   boundary.
2. Sealing of that artifact's octet identity.
3. Transfer of the identical octets to the RI-PY boundary and the RI-RS boundary.
4. Independent receipt verification on each side.
5. Emission of a deterministic `BoundaryHandoffRecord` per (fixture,
   implementation) pair.
6. Isolation of Registry-declared expected values from the execution channel.
7. Preservation of PRESENT / ABSENT / UNKNOWN distinctions across the boundary.
8. Engineering validation assertions B-VAL-011 … B-VAL-020.
9. Engineering failure classification for handoff-layer failures.

---

## 3. Non-scope

BC-02 does **not** cover, define, produce or authorize:

| Excluded | Belongs to |
|---|---|
| Execution of the implementation under test | BC-03 / BC-04 (adapters) |
| Observation of implementation output | Observation layer |
| Normalization of observed output | Normalization layer |
| Comparison of observed against expected | Validation layer |
| Conformance verdicts (PASS / FAIL / PARTIAL / INCONCLUSIVE) | Conformance layer |
| Evidence generation (`EVID-CORE` or otherwise) | APS-300 / evidence layer |
| P-01, N-01 … N-08 | Conformance execution — **BLOCKED** |
| CONF-003 §4.5 prohibited-input controls | Conformance execution — **BLOCKED** |
| Definition of canonical serialization | APS-200 §8 |
| Definition of hash domains for protocol objects | APS-200 §8 · APS-300 §5 |
| Definition of fixture content or expectations | Fixture Registry |
| Digest absence / presence determination | Observation layer — see §11.3 |
| Any DQ-003, DQ-004, ENT-007, APS-300, ARI or C4 material | Their own gates |

A boundary that emits any artifact in the left column is out of contract.

---

## 4. Inputs

### 4.1 Consumed authorities

| Input | Role | Binding state |
|---|---|---|
| `CONFORMANCE_FIXTURE_REGISTRY_v1` | Authoritative fixture issuance contract | **UNBOUND** — see `BC-02-DEP-001` |
| Boundary Specification v1 | Boundary interface shape | **UNBOUND** — see `BC-02-DEP-004` |
| Core Interface Spec v1 | RI-side interface signature | **UNBOUND** — see `BC-02-DEP-004` |
| BC-01 (accepted) | Preceding boundary construction package | **UNBOUND** — see `BC-02-DEP-004` |

The declared construction baseline records Fixture Registry v1, Core Interface
Spec v1, Boundary Specification v1 and BC-01 as ACCEPTED. None of these
artifacts is resolvable in any repository in scope
(`aura-specification`, `aura-poc-a-core-v3.3`, `aura-guard-v1.3`,
`.github`), on any branch reachable from those repositories' remotes, under any
name, and no artifact in scope contains the token `fixture_hash`.

BC-02 is therefore constructed **parametrically** over the Registry contract:
every field reference below is written against the fixture artifact field set
declared in the BC-02 construction order, and each carries an explicit binding
obligation that must be discharged against the real Registry contract before
BC-02 validation can be entered. See §19 and §16.

BC-02 does not invent Registry fields. Where BC-02 requires a property the
declared field set does not supply, that is recorded as a gap (§19), not
resolved by assumption.

### 4.2 Fixture artifact fields consumed

From the declared Registry fixture artifact:

| Field | BC-02 use | Passed to adapter? |
|---|---|---|
| `fixture_id` | Identity label; equality assertion B-VAL-011 | Yes (label only) |
| `fixture_hash` | Registry-declared identity value; carried verbatim | No |
| `raw_input` | The execution input — transferred as octets | **Yes — the only execution input** |
| `input_characterization` | Routing/traceability metadata | Yes (as opaque, non-executable metadata) |
| `expected_acceptance` | Declaration only | **No — firewalled, §10** |
| `expected_digest_output` | Declaration only | **No — firewalled, §10** |
| provenance / artifact identity | Traceability | Yes (label only) |

### 4.3 Transport fields introduced by BC-02

The following are **engineering transport fields**, explicitly non-normative,
introduced because octet-exact transfer cannot be demonstrated without them.
They carry no protocol meaning and MUST NOT be interpreted as fixture content.

| Field | Reason it is required |
|---|---|
| `input_segment_sha256` | The load-bearing transfer proof; nothing in the declared field set is an independently recomputable digest over the octets actually delivered |
| `raw_input_encoding` | Octet-exact transfer is undefined without a declared encoding |
| `receipt_digest` | Recomputation on the receiving side is what distinguishes transfer from copy |
| `issuance_id` | Binds two per-implementation records to one issuance event |
| `handoff_status`, `handoff_error` | Engineering outcome, distinct from every conformance outcome (§13) |
| `presence` tagging | Required to preserve UNKNOWN without using `null` (§11) |

No other field is introduced. Each is marked `non-normative` in the record
schema (§7).

---

## 5. Fixture identity contract

### 5.1 The artifact is octets

The fixture artifact is, for BC-02 purposes, an **opaque octet sequence** —
`fixture_artifact_bytes` — exactly as issued by the Registry. It is not a JSON
document, an object, or a value. It becomes a document only inside a read-only
view (§6.2), and that view is never a source of transferred content.

### 5.2 Artifact identity

```text
fixture_artifact_identity = SHA-256( fixture_artifact_bytes )
```

Computed over the raw issued octets. Hex-encoded lowercase in the record.

**Canonical serialization MUST NOT be applied here.** The fixture artifact is a
transport container, not a protocol object. Applying RFC 8785 to it would
require `parse → re-serialize`, which §6.1 forbids, and would silently absorb
exactly the mutations (member order, number form, escaping, whitespace) that
BC-02 is built to detect. APS-200 §8 is not in force at this boundary and BC-02
does not invoke it.

### 5.3 Input segment identity — the load-bearing value

The execution input is sealed separately from the artifact as a whole:

```text
input_segment_bytes  = the octets of raw_input, after decoding raw_input_encoding
input_segment_sha256 = SHA-256( input_segment_bytes )
```

This value is:

- computed once by the issuer at seal time;
- recomputed **independently** by each adapter over the octets it actually
  received, before any use;
- recorded in both `BoundaryHandoffRecord`s.

Equality of the two independently recomputed values is the only assertion in
BC-02 that constitutes *evidence of transfer*. Everything else is a label.

### 5.4 Declared vs. computed identity

Three values must never be collapsed:

| Value | Origin | What it proves |
|---|---|---|
| `fixture_id` | Registry declaration | Nothing. A label. |
| `fixture_hash` | Registry declaration, carried verbatim | Nothing until the Registry's hash rule is bound (`BC-02-DEP-002`) |
| `input_segment_sha256` | Computed by each receiver over received octets | That the same octets arrived on both sides |

A boundary that verifies `fixture_hash` by comparing the Registry's declared
value against itself has verified nothing. Until the Registry defines what
octets `fixture_hash` covers and under what encoding, the verification state of
`fixture_hash` is **UNKNOWN**, and MUST be recorded as UNKNOWN — never as
verified, never as absent, never as `null` (§11).

### 5.5 Traceability chain

```text
Registry entry
    → issuance_id
    → fixture_artifact_bytes            (immutable from this point)
    → fixture_artifact_identity         (issuer-computed)
    → input_segment_sha256              (issuer-computed)
        ├→ RI-PY receipt → recomputed input_segment_sha256 → BoundaryHandoffRecord(PY)
        └→ RI-RS receipt → recomputed input_segment_sha256 → BoundaryHandoffRecord(RS)
```

Every arrow is recorded. An auditor holding only the two records and the
Registry entry must be able to walk the chain in both directions.

### 5.6 Domain separation — mandatory

The BC-02 transport digests are SHA-256 over octets with **no domain prefix**,
and BC-02 MUST NOT use, reuse, imitate or extend any protocol hash domain. In
particular, the RFC 6962 domains `0x00` (leaf) and `0x01` (interior node)
defined in APS-200 §8 are **prohibited** in the handoff layer.

Where a composite digest over multiple BC-02 transport values is unavoidable,
it MUST be domain-separated by the ASCII tag `aura-bc02-transport-v1` followed
by a single `0x1f` octet, so that no BC-02 digest can ever collide with, be
mistaken for, or be substituted into a protocol hash domain. No such composite
digest is required by this version of BC-02.

---

## 6. Immutability contract

### 6.1 The permitted pipeline

After issuance, the only operations permitted on the fixture artifact are:

```text
READ  →  HASH  →  FORWARD
```

The following are **forbidden** on the transfer path:

- `parse → modify → serialize → execute`
- re-serialization of the artifact or of `raw_input` in any form
- canonicalization, pretty-printing, minification, key reordering
- character-set transcoding, line-ending normalization, BOM insertion or removal
- number reformatting, string re-escaping
- schema-driven coercion, defaulting, or field injection
- any mutation of the artifact after seal, in memory or on disk

### 6.2 The read-only view

The boundary MAY parse the artifact into a **read-only view** in order to locate
segments and read routing metadata. That view is subject to two absolute rules:

1. Nothing that reaches an adapter may originate from the view. All transferred
   content is carved from `fixture_artifact_bytes` by offset and length, or
   decoded from `raw_input` per §6.3.
2. The view is discarded before transfer. It is never serialized.

### 6.3 The single declared transport transformation

Exactly one transformation is permitted, and it is declared, bounded and
auditable:

```text
raw_input (encoded, as issued)  --decode(raw_input_encoding)-->  input_segment_bytes
```

Constraints:

- `raw_input_encoding` MUST be one of `identity`, `base64`, `base16`. Nothing
  else is permitted in this version.
- The decode MUST be a total, deterministic, byte-exact inverse of the
  Registry's encode. It MUST NOT be a JSON parse.
- The original `raw_input` field octets and `fixture_artifact_bytes` MUST be
  retained unchanged alongside the decoded form.
- Both the pre-decode and post-decode digests are recorded.

If `raw_input` is issued as a **JSON sub-document rather than an octet-exact
encoded field**, octet-exact transfer is not achievable: extracting it requires
`parse → re-serialize`, which §6.1 forbids. That condition is a **FIXTURE GAP**,
not a boundary defect, and BC-02 MUST refuse the handoff with
`handoff_status = HANDOFF_REJECTED`, `handoff_error.class = ENCODING_INVALID`.
It MUST NOT silently re-serialize.

> This condition holds for the fixture material currently present in scope: the
> corpus fixtures under `fixtures/corpus/` carry their input as a JSON
> sub-object (`"input": { … }`), with no octet-exact encoded form. Recorded as
> `BC-02-DEP-003`.

### 6.4 Seal enforcement

After `fixture_artifact_identity` is computed, the artifact MUST be held in
storage the boundary cannot write to (read-only mount, content-addressed store,
or in-process immutable buffer with no exposed mutator). Immutability MUST be
enforced structurally, not by convention.

Immediately before each transfer and immediately after each receipt, the digest
is recomputed and compared. A mismatch at either point is
`HANDOFF_REJECTED` / `RECEIPT_DIGEST_MISMATCH` and terminates that handoff. It
is never repaired, retried silently, or downgraded.

---

## 7. Handoff data model

### 7.1 `BoundaryHandoffRecord`

One record per `(issuance_id, implementation_id)`. Non-normative engineering
artifact.

```jsonc
{
  "record_type": "BoundaryHandoffRecord",
  "record_version": "BC-02/1.0",
  "normative": false,

  // ---- Fixture identity (§5) ----
  "fixture_id":                 "<Registry-declared label>",
  "fixture_hash":               { "presence": "PRESENT", "value": "<Registry-declared, verbatim>" },
  "fixture_hash_verification":  { "presence": "UNKNOWN", "reason": "Registry hash rule unbound (BC-02-DEP-002)" },
  "fixture_artifact_identity":  "<hex SHA-256 of fixture_artifact_bytes, issuer-computed>",
  "issuance_id":                "<opaque, unique per issuance event>",

  // ---- Transferred input (§5.3, §6.3) ----
  "raw_input_reference": {
    "raw_input_encoding":    "identity | base64 | base16",
    "encoded_field_sha256":  "<hex SHA-256 of raw_input octets as issued>",
    "input_segment_sha256":  "<hex SHA-256 of decoded octets — RECOMPUTED BY THIS RECEIVER>",
    "input_segment_length":  0
  },

  // ---- Receipt verification (§5.3) ----
  "receipt": {
    "receipt_digest":        "<hex SHA-256 recomputed over the buffer actually received>",
    "receipt_digest_source": "RECEIVER_RECOMPUTED",
    "matches_issued_digest": true
  },

  // ---- Characterization (§4.2) ----
  "input_characterization": { "presence": "PRESENT", "value": { } },

  // ---- Implementation provenance (§12) ----
  "implementation_id":       "RI-PY | RI-RS",
  "implementation_version":  "<version>",
  "source_commit":           "<40-hex>",
  "source_worktree_clean":   true,

  // ---- Adapter provenance (§12) ----
  "adapter_id":              "<adapter identity>",
  "adapter_version":         "<version>",
  "adapter_source_digest":   "<hex SHA-256 over adapter source>",

  // ---- Environment (§12) ----
  "execution_environment": {
    "os":        "<os>",
    "arch":      "<arch>",
    "toolchain": "<interpreter/compiler and version>"
  },

  // ---- Engineering outcome (§13) ----
  "handoff_status": "HANDOFF_TRANSFERRED | HANDOFF_REJECTED | HANDOFF_ERROR",
  "handoff_error":  { "presence": "ABSENT" }
}
```

### 7.2 Fields deliberately absent

The record has **no** field for, and MUST NOT be extended to carry:

- observed acceptance, decision, verdict, or outcome;
- observed digest, digest presence, or digest absence;
- `expected_acceptance` or `expected_digest_output` (§10);
- `PASS`, `FAIL`, `INCONCLUSIVE`, or any conformance classification;
- wall-clock timestamps or any other value that varies between runs of an
  otherwise identical handoff (§14, B-VAL-020).

Absence here is structural. A field that does not exist cannot be contaminated,
cannot be inferred, and cannot leak a normative claim through an engineering
record.

### 7.3 Presence-tagged values

Every field whose value may be unavailable is a **presence-tagged object**, never
a bare value and never `null`:

```jsonc
{ "presence": "PRESENT", "value": <any> }
{ "presence": "ABSENT" }
{ "presence": "UNKNOWN", "reason": "<why the boundary cannot determine this>" }
```

`null` is not a permitted value anywhere in the record. See §11.

This mirrors the rule already established for expected digests in
`fixtures/ck003/expected_digests.json`: *"null is intentional and MUST NOT be
interpreted as zero, empty digest, or PASS."* BC-02 goes one step further and
removes `null` from the record entirely, so the rule cannot be forgotten by a
later reader.

### 7.4 Deterministic serialization

The record is serialized as UTF-8 JSON under RFC 8785 (JCS), with the schema
above.

This is an **engineering serialization choice only**. It does not make the
handoff record a protocol object, does not place it under APS-200 §8 authority,
does not constitute canonical serialization in the protocol sense, and produces
no value that may be used as, or substituted for, a protocol digest.

Determinism obligation: two serializations of the same handoff, one in the same
process and one in a fresh process on a different host, MUST be byte-identical.
Because the record carries no timestamp, no path, no hostname and no counter,
this is achievable; a boundary that cannot achieve it has introduced a volatile
field and is out of contract.

---

## 8. RI-PY handoff contract

The RI-PY boundary receives, per handoff:

1. `input_segment_bytes` — an octet buffer. Not a string, not a parsed object,
   not a file path into the Registry.
2. `fixture_id`, `fixture_artifact_identity`, `issuance_id` — opaque labels,
   echoed into the record, never used to derive input.
3. `input_characterization` — opaque metadata, never used to derive input.

The RI-PY adapter MUST:

- recompute `SHA-256(input_segment_bytes)` on receipt, before any other use, and
  record it as `receipt.receipt_digest` with source `RECEIVER_RECOMPUTED`;
- halt with `HANDOFF_REJECTED` / `RECEIPT_DIGEST_MISMATCH` on any mismatch;
- treat the buffer as immutable — no in-place decoding, trimming, or
  re-encoding;
- emit its `BoundaryHandoffRecord` **before** invoking the implementation, so a
  divergence is recorded rather than suppressed (the discipline already
  established in CONF-003 §4.1 step 7).

The RI-PY adapter MUST NOT:

- hold a Registry reference, path, client, credential or cache;
- read any repository-resident fixture copy;
- reconstruct input from `input_characterization`, from `fixture_id`, or from
  any description of the fixture;
- receive, read, import or be linked against `expected_acceptance` or
  `expected_digest_output` (§10);
- write to `fixture_artifact_bytes` or any derived buffer.

---

## 9. RI-RS handoff contract

Identical in every respect to §8, with `implementation_id = "RI-RS"`.

The symmetry is a requirement, not a convenience: the two contracts MUST be
byte-for-byte the same obligations, differing only in implementation identity,
version, commit, adapter identity and environment. Any asymmetry in what the two
sides receive invalidates B-VAL-013 and MUST be recorded as a BOUNDARY GAP.

In particular, the following present-day asymmetry MUST be removed before
validation: RI-RS currently holds a repository-resident fixture copy
(`aura-guard-v1.3/conformance/canonical/CANONICAL-001.json`) while RI-PY holds
none. A resident copy on either side makes B-VAL-019 unfalsifiable, because the
adapter retains a reconstruction source. See `BC-02-OBS-007`.

---

## 10. Expected-value firewall

### 10.1 The rule

Registry expected values are **declarations about what should later be
observed**. They are not inputs, not instructions, and not available to anything
on the execution path.

```text
   FORBIDDEN                          REQUIRED

   expected_acceptance = REJECT       fixture + characterization
        ↓                                    ↓
   adapter reads it                   RI implementation
        ↓                                    ↓
   adapter produces REJECT            observed result
                                             ↓
                                      (much later, other layer)
                                      comparison against expectation
```

### 10.2 Structural enforcement

The firewall is enforced by **construction, not by discipline**:

1. `expected_acceptance` and `expected_digest_output` are never placed in the
   channel that reaches an adapter. They remain in the issuer's expectation
   segment.
2. The `BoundaryHandoffRecord` schema has no field for them (§7.2). There is no
   place to put them.
3. The adapter interface accepts an octet buffer plus opaque labels. There is no
   parameter through which an expectation could arrive.
4. The adapter has no Registry access (§8), so it cannot fetch them.

A firewall that depends on an adapter *choosing* not to read a value it
possesses is not a firewall. BC-02 requires that the adapter not possess it.

### 10.3 Recording

The issuer MAY record, outside the handoff record, that an expectation segment
existed and its digest — for later use by the validation layer. That record MUST
NOT be transferred, MUST NOT be readable by any adapter, and MUST NOT be
referenced from the `BoundaryHandoffRecord`.

---

## 11. UNKNOWN / ABSENT preservation

### 11.1 Three states, never two

| State | Meaning |
|---|---|
| `PRESENT` | The boundary observed the value and records it |
| `ABSENT` | The boundary observed, with sufficient observability, that the value is not there |
| `UNKNOWN` | The boundary could not determine presence — the interface does not expose enough to tell |

### 11.2 Prohibited conversions

The following MUST NOT occur anywhere in the handoff layer:

```text
UNKNOWN  →  ABSENT          (fabricates an observation)
ERROR    →  REJECT          (converts an engineering failure into a semantic one)
ABSENT   →  null            (destroys the distinction)
UNKNOWN  →  null            (destroys the distinction)
null     →  ABSENT          (invents an observation from a placeholder)
missing field → ABSENT      (silence is not observation)
```

`null` MUST NOT appear in a `BoundaryHandoffRecord`. A validator MUST reject a
record containing `null` at any depth.

### 11.3 BC-02 never determines digest absence

BC-02 has no visibility into implementation output and therefore **cannot**
determine whether a digest was produced or withheld. It MUST NOT record, infer,
default, or imply digest presence or absence.

This is enforced structurally: the record has no digest-output field at all
(§7.2). Digest presence/absence is an observation-layer determination made after
execution, under an authority BC-02 does not hold.

### 11.4 Where UNKNOWN is currently mandatory

Given the unbound Registry contract, the following MUST be recorded as UNKNOWN
with a reason, not as verified and not as absent:

- `fixture_hash_verification` — the Registry's hash rule is unbound
  (`BC-02-DEP-002`);
- `input_characterization` — where the Registry supplies no characterization
  vocabulary (`BC-02-DEP-005`).

---

## 12. Provenance requirements

Each `BoundaryHandoffRecord` MUST carry provenance sufficient for an auditor to
reconstruct the handoff without access to the running system.

| Axis | Required fields | Rationale |
|---|---|---|
| Fixture | `fixture_id`, `fixture_hash`, `fixture_artifact_identity`, `issuance_id` | Binds the record to one Registry entry and one issuance |
| Implementation | `implementation_id`, `implementation_version`, `source_commit`, `source_worktree_clean` | Identifies exactly what received the octets |
| Adapter | `adapter_id`, `adapter_version`, `adapter_source_digest` | The adapter is part of the trusted path and must itself be identified |
| Environment | `execution_environment.os`, `.arch`, `.toolchain` | Distinguishes environment-induced divergence from implementation divergence |
| Transfer | `raw_input_reference.*`, `receipt.*` | The transfer evidence itself |

Rules:

1. `source_commit` MUST be a full 40-hex commit that exists in the named
   implementation repository. A short hash, a tag, or a branch name is
   insufficient.
2. `source_worktree_clean = false` MUST NOT be silently tolerated; a dirty
   worktree makes `source_commit` non-identifying and MUST be surfaced.
3. The two records for one issuance MUST declare **distinct** implementations,
   repositories and adapters. Two records naming the same implementation are not
   a cross-implementation handoff. (This mirrors the C8 discipline of
   CONF-003 §4.2, at the engineering layer; it is not that check.)
4. Provenance is recorded, never inferred. A field the boundary cannot determine
   is `UNKNOWN` with a reason.

---

## 13. Handoff status semantics

### 13.1 Values

Engineering states only. Namespaced so they cannot be confused with, or
substituted into, any conformance vocabulary:

| Value | Meaning | Says about conformance |
|---|---|---|
| `HANDOFF_TRANSFERRED` | The octets reached the implementation boundary and the receipt digest matched the issued digest | **Nothing** |
| `HANDOFF_REJECTED` | The boundary deterministically refused the handoff for a declared, attributable reason | **Nothing** |
| `HANDOFF_ERROR` | The handoff did not complete for a reason the boundary cannot attribute | **Nothing** |

> **Refinement note.** The construction order proposed `TRANSFERRED` /
> `REJECTED` / `ERROR`. BC-02 prefixes each with `HANDOFF_` in serialization.
> The reason is concrete: the Registry vocabulary contains
> `expected_acceptance = REJECT`, and a bare `REJECTED` in an engineering record
> is one careless `==` away from being read as a semantic rejection. The
> namespacing makes the confusion prohibited by §11.2 structurally harder to
> commit. Semantics are unchanged.

### 13.2 Prohibited as handoff status

`PASS`, `FAIL`, `INCONCLUSIVE`, `PARTIAL`, `NOT APPLICABLE`, `ACCEPT`, `REJECT`,
`CONFORMANT`, `NON-CONFORMANT`, and any APS-400 / CONF-00x outcome token.

These belong to the validation and conformance classification layers. A handoff
record that emits one is out of contract and its output MUST be discarded rather
than reinterpreted.

### 13.3 `handoff_error`

Present only when `handoff_status != HANDOFF_TRANSFERRED`. Presence-tagged
(§7.3). Structure:

```jsonc
{ "presence": "PRESENT", "value": { "class": "<enum>", "detail": "<free text>" } }
```

Closed enumeration:

| Class | Status | Meaning |
|---|---|---|
| `RECEIPT_DIGEST_MISMATCH` | `HANDOFF_REJECTED` | Received octets differ from issued octets |
| `ENCODING_INVALID` | `HANDOFF_REJECTED` | `raw_input_encoding` absent, unsupported, or not octet-exact (§6.3) |
| `REQUIRED_FIELD_MISSING` | `HANDOFF_REJECTED` | The issued artifact lacks a field BC-02 requires |
| `ARTIFACT_UNREADABLE` | `HANDOFF_REJECTED` | The artifact could not be read as octets |
| `SEAL_VIOLATION` | `HANDOFF_REJECTED` | The artifact changed after seal |
| `TRANSPORT_FAILURE` | `HANDOFF_ERROR` | Transfer did not complete |
| `ADAPTER_UNAVAILABLE` | `HANDOFF_ERROR` | The receiving boundary could not be reached |
| `TIMEOUT` | `HANDOFF_ERROR` | No completion within the declared bound |
| `UNATTRIBUTED` | `HANDOFF_ERROR` | Failure observed, cause not determinable |

No class in this table maps to a conformance outcome. A downstream layer that
maps one MUST do so under its own authority and record the mapping; BC-02
neither performs nor authorizes it.

---

## 14. Validation assertions B-VAL-011 … B-VAL-020

Engineering validation assertions. **Not** P-01, **not** N-01 … N-08, **not**
CONF-003 §4.5, **not** conformance results, **not** certification evidence.
Their satisfaction is evidence about the boundary, and about nothing else.

Notation: `R_PY` and `R_RS` are the two `BoundaryHandoffRecord`s for one
`issuance_id`.

| ID | Assertion | Formal condition | Evidence class |
|---|---|---|---|
| **B-VAL-011** | `fixture_id` preserved | `R_PY.fixture_id == R_RS.fixture_id == Registry.fixture_id` | Label equality |
| **B-VAL-012** | `fixture_hash` preserved | `R_PY.fixture_hash.value == R_RS.fixture_hash.value == Registry.fixture_hash`, **and** `R_PY.raw_input_reference.input_segment_sha256 == R_RS.raw_input_reference.input_segment_sha256`, each independently recomputed by its own receiver | **Transfer evidence** |
| **B-VAL-013** | Same artifact identity across RI-PY / RI-RS | `R_PY.fixture_artifact_identity == R_RS.fixture_artifact_identity` **and** `R_PY.issuance_id == R_RS.issuance_id` | Traceability, **not** independent evidence — see note below |
| **B-VAL-014** | Raw input preserved | `receipt.receipt_digest == input_segment_sha256` on **both** sides, with `receipt_digest_source == RECEIVER_RECOMPUTED`; and `raw_input_encoding ∈ {identity, base64, base16}` | **Transfer evidence** |
| **B-VAL-015** | Input characterization preserved | `R_PY.input_characterization == R_RS.input_characterization`, presence-tagged, byte-equal under §7.4 serialization | Metadata integrity |
| **B-VAL-016** | Expected values non-authoritative to adapters | Neither record contains `expected_acceptance` or `expected_digest_output` at any depth; neither adapter's dependency closure reaches the expectation segment; §10.2(3) interface has no parameter admitting one | **Firewall evidence** |
| **B-VAL-017** | Fixture immutable after handoff | Post-transfer recomputation of `fixture_artifact_identity` equals the sealed value; the artifact store rejects writes (§6.4) | Immutability |
| **B-VAL-018** | Handoff failure distinguishable from conformance failure | `handoff_status ∈ {HANDOFF_TRANSFERRED, HANDOFF_REJECTED, HANDOFF_ERROR}`; no §13.2 token appears anywhere in either record | Layer separation |
| **B-VAL-019** | Adapter does not reconstruct from semantic description | The adapter has no Registry reference, no resident fixture copy, and no code path from `input_characterization` or `fixture_id` to `input_segment_bytes`; demonstrated by BNC-2 (§15.3) | **Structural evidence** |
| **B-VAL-020** | Handoff record deterministically serializable | Serializing each record twice — same process, and a fresh process on a different host — yields byte-identical UTF-8 output; no `null` at any depth; no volatile field present | Determinism |

### 14.1 What B-VAL-013 does and does not establish

B-VAL-013 holds **by construction** whenever both records descend from one
issuance, because both echo an issuer-supplied label. It therefore proves
traceability and rules out cross-issuance mix-ups — and nothing more. It is
**not** evidence that the same octets arrived.

The evidence that the same octets arrived is B-VAL-012 together with B-VAL-014:
two digests, each recomputed by a different receiver over the buffer that
receiver actually holds, found equal.

This distinction is deliberate and MUST NOT be flattened in any downstream
summary. Recording B-VAL-013 as proof of transfer would reproduce, at the
engineering layer, exactly the error CONF-003 §5 warns against: *"Two
implementations agreeing on a digest they both read from the same file
demonstrates nothing."*

### 14.2 Coverage of B-INV-01

B-INV-01 requires `fixture_hash_PY == fixture_hash_RS` and
`fixture_id_PY == fixture_id_RS`, and end-to-end traceability from Registry
entry through both handoffs.

| B-INV-01 element | Covered by | Coverage state |
|---|---|---|
| `fixture_id` equality | B-VAL-011 | Covered |
| `fixture_hash` equality (declared value carried identically) | B-VAL-012, first conjunct | Covered |
| `fixture_hash` equality (verified against the Registry's hash rule) | B-VAL-012, `fixture_hash_verification` | **UNKNOWN** — `BC-02-DEP-002` |
| Same octets actually received | B-VAL-012 second conjunct + B-VAL-014 | Covered |
| Reconstruction excluded | B-VAL-019 | Covered structurally |
| Registry → artifact → hash → PY → RS traceability | §5.5 + B-VAL-013 | Covered |
| Immutability across the chain | B-VAL-017 | Covered |

B-INV-01 is **contract-covered** by BC-02. It is **not demonstrated**: no
validation has been executed, and the `fixture_hash` verification limb resolves
to UNKNOWN under the current unbound Registry contract. Per §11.2 that UNKNOWN
is preserved, not converted.

---

## 15. Validation procedure

To be executed at BC-02 VALIDATION, after §19 dependencies are discharged. Not
authorized by this document.

### 15.1 Preconditions

| ID | Precondition |
|---|---|
| VE-01 | `CONFORMANCE_FIXTURE_REGISTRY_v1` resolvable, versioned, and field-bound |
| VE-02 | Registry `fixture_hash` rule declared: covered octets and encoding |
| VE-03 | At least one fixture issues `raw_input` in an octet-exact encoded form (§6.3) |
| VE-04 | Boundary Specification v1 / Core Interface Spec v1 resolvable; adapter interface signature fixed |
| VE-05 | No repository-resident fixture copy on either implementation side (§9) |

Validation MUST NOT begin with an unmet precondition. An unmet precondition is
recorded and returned to Custodian review; it is not worked around.

### 15.2 Positive procedure

1. Resolve one Registry entry. Record `registry_id`, `registry_version`,
   `registry_entry_ref`.
2. Issue the fixture artifact. Record `issuance_id`.
3. Seal: compute `fixture_artifact_identity` and `input_segment_sha256` over raw
   octets (§5.2, §5.3). Place the artifact in write-denied storage (§6.4).
4. Transfer `input_segment_bytes` plus labels to the RI-PY boundary. Do not
   transfer the expectation segment.
5. Transfer the identical buffer to the RI-RS boundary, from the sealed store —
   not from the RI-PY path, not from a re-read of the Registry.
6. Each side independently recomputes its receipt digest and emits its
   `BoundaryHandoffRecord` **before** any implementation invocation.
7. Evaluate B-VAL-011 … B-VAL-020 against the two records and the Registry entry.
8. Recompute `fixture_artifact_identity` from the sealed store (B-VAL-017).
9. Re-serialize both records in a fresh process on a different host (B-VAL-020).

No implementation is executed. Steps 1–9 complete without invoking RI-PY or
RI-RS protocol behaviour beyond accepting the buffer.

### 15.3 Engineering negative controls

A validation that only demonstrates the happy path demonstrates nothing about
the boundary's ability to detect failure. Each control MUST be shown to be
caught by the named assertion.

| ID | Injected condition | MUST be caught by |
|---|---|---|
| BNC-1 | Flip one octet of the buffer delivered to one side only | B-VAL-012, B-VAL-014 |
| BNC-2 | Have one adapter build its input from `input_characterization` instead of the received buffer | B-VAL-019 (and B-VAL-012 if the reconstruction is not byte-exact) |
| BNC-3 | Attempt to write to the artifact after seal | B-VAL-017 (`SEAL_VIOLATION`) |
| BNC-4 | Place `expected_acceptance` in the adapter channel | B-VAL-016 |
| BNC-5 | Sever the transport mid-handoff | B-VAL-018 — status MUST be `HANDOFF_ERROR`, never `HANDOFF_REJECTED`, never any §13.2 token |
| BNC-6 | Replace an `UNKNOWN` presence tag with `null` | B-VAL-020 (record validator rejects) |
| BNC-7 | Emit both records naming the same `implementation_id` | §12 rule 3 |

Controls MUST be applied to temporary copies. They MUST NOT remain in any
committed artifact. Sealed-store digests MUST be re-verified after the controls
run. (Discipline adopted from CONF-003 §4.4; these are not those controls.)

### 15.4 Output of validation

A `BC-02 Boundary Validation Report` containing: the two records verbatim, the
per-assertion results for B-VAL-011 … B-VAL-020, the negative-control results,
and the unmet-precondition list if any.

That report is an **engineering validation report**. It is not `EVID-CORE`, not
conformance evidence, and MUST NOT be cited as such. It does not enter the
APS-300 evidence chain.

---

## 16. Failure classification

A failed assertion is an **observation**. It is not automatically an
implementation defect.

| Observation | Classification |
|---|---|
| Registry contract does not supply a property BC-02 requires | **FIXTURE GAP** |
| `raw_input` not issued octet-exactly (§6.3) | **FIXTURE GAP** |
| Registry `fixture_hash` rule undeclared | **FIXTURE GAP** |
| Boundary re-serializes, canonicalizes or reconstructs | **BOUNDARY GAP** |
| Adapter retains Registry access or a resident fixture copy | **BOUNDARY GAP** |
| Expectation reaches the execution channel | **BOUNDARY GAP** |
| Record non-deterministic, or contains `null` | **BOUNDARY GAP** |
| Implementation cannot accept an octet buffer at its interface | **IMPLEMENTATION GAP** |
| Implementation mutates the received buffer | **IMPLEMENTATION GAP** |
| Required authority (Registry, Boundary Spec, Core Interface Spec) unresolvable | **GOVERNANCE GAP** |
| Interface exposes too little to distinguish ABSENT from UNKNOWN | **SPECIFICATION GAP** |
| Validation report cannot be produced or retained | **EVIDENCE GAP** |
| Observation not attributable to any of the above | **OBSERVATION → UNRESOLVED / INCONCLUSIVE → CUSTODIAN REVIEW** |

Rules:

1. An observation that cannot be attributed to an existing authority MUST NOT
   become a new normative requirement. It is returned unresolved.
2. No classification in this table is a conformance verdict.
3. BC-02 does not repair implementation behaviour on the basis of a
   classification. Repair is a separate, separately authorized work package.

---

## 17. Definition of Done

| # | Requirement | State |
|---|---|---|
| 1 | Fixture identity contract defined | **MET** — §5 |
| 2 | Artifact immutability contract defined | **MET** — §6 |
| 3 | Identical RI-PY / RI-RS handoff contract defined | **MET** — §8, §9 |
| 4 | Raw input preservation defined | **MET** — §5.3, §6.3 |
| 5 | Input characterization preservation defined | **MET** — §4.2, B-VAL-015 |
| 6 | Provenance requirements defined | **MET** — §12 |
| 7 | Expected-value isolation defined and structurally enforced | **MET** — §10 |
| 8 | Handoff failure isolated from conformance failure | **MET** — §13 |
| 9 | Deterministic handoff record defined | **MET** — §7 |
| 10 | Validation assertions B-VAL-011 … B-VAL-020 defined | **MET** — §14 |
| 11 | B-INV-01 demonstrably covered | **PARTIAL** — contract-covered (§14.2); `fixture_hash` verification limb resolves to **UNKNOWN** under `BC-02-DEP-002` |
| 12 | Contract bound to the authoritative Registry contract (§4) | **NOT MET** — `BC-02-DEP-001` |
| 13 | Contract bound to Boundary Specification v1 / Core Interface Spec v1 | **NOT MET** — `BC-02-DEP-004` |
| 14 | At least one fixture issuable under §6.3 | **NOT MET** — `BC-02-DEP-003` |

Items 12–14 are **input bindings**, not drafting work. The contract text is
complete and internally consistent; it cannot be finalized against authorities
that are not resolvable.

BC-02 completion does **not** authorize conformance execution under any
circumstance (§18).

---

## 18. Explicit execution firewall

The following remain prohibited and were not performed in the construction of
this document:

| Prohibited | Performed? |
|---|---|
| Execute P-01 | NO |
| Execute N-01 … N-08 | NO |
| Execute CONF-003 §4.5 | NO |
| Generate conformance evidence | NO |
| Generate a conformance verdict | NO |
| Modify APS-200 | NO |
| Modify CONF-003 | NO |
| Modify D-2.3 / D-2.4 | NO |
| Create N-09 | NO |
| Create new prohibited classes | NO |
| Create fixtures for DQ-003 / DQ-004 / ENT-007 / APS-300 | NO |
| Create ARI normative semantics | NO |
| Authorize C4 | NO |
| Change authority anchors | NO |
| Modify RI-PY normative semantics | NO |
| Modify RI-RS normative semantics | NO |
| Infer protocol requirements from implementation behaviour | NO |
| Open a recovery / reconciliation gate | NO |

Frozen baseline state is unchanged by this document:

```text
D-1                          CLOSED
APS-200                      FROZEN / ACCEPTED
CONF-003 §4.5 rebinding      ACCEPTED
Fixture Registry v1          ACCEPTED
Boundary Specification v1    CONSTRUCTION AUTHORIZED
BC-01                        ACCEPTED
BC-02                        CONSTRUCTION AUTHORIZED

RI-PY / RI-RS qualification  NOT QUALIFIED
§4.5 execution               BLOCKED
Conformance                  NO RESULT
Evidence                     NOT GENERATED
DQ-003                       OPEN
DQ-004                       OPEN / BLOCKED
ENT-007                      NO-GO
C4                           NOT AUTHORIZED
```

---

## 19. Open dependencies

### Blocking — BC-02 validation cannot be entered

**`BC-02-DEP-001` — Fixture Registry contract unbound.** *GOVERNANCE GAP.*
`CONFORMANCE_FIXTURE_REGISTRY_v1` is recorded ACCEPTED in the construction
baseline but is not resolvable in any repository in scope, on any branch, under
any name. No artifact in scope contains the token `fixture_hash`. §4 declares
the Registry contract authoritative; BC-02 is therefore written parametrically
and its field bindings are provisional. *Discharge:* supply the Registry
contract and confirm the §4.2 field mapping. Blocks VE-01.

**`BC-02-DEP-002` — `fixture_hash` rule undeclared.** *FIXTURE GAP.*
What octets `fixture_hash` covers, and under what encoding, is undefined.
Verifying a declared value against itself is not verification (§5.4), so
`fixture_hash_verification` resolves to UNKNOWN and B-INV-01's verification limb
is uncovered (§14.2). *Discharge:* declare the hash rule in the Registry
contract. Blocks VE-02.

**`BC-02-DEP-003` — No octet-exact fixture input available.** *FIXTURE GAP.*
Fixture material in scope carries input as a JSON sub-document
(`fixtures/corpus/FIX-INV-*.json` → `"input": { … }`), with no octet-exact
encoded form. Under §6.3 such a fixture cannot be handed off without
`parse → re-serialize`, which §6.1 forbids; BC-02 must reject it. No fixture in
scope can currently satisfy B-VAL-014. *Discharge:* Registry issues at least one
fixture with `raw_input` + `raw_input_encoding` in an octet-exact form. Blocks
VE-03.

**`BC-02-DEP-004` — Boundary and interface specifications unbound.**
*GOVERNANCE GAP.* Boundary Specification v1, Core Interface Spec v1 and BC-01
are recorded ACCEPTED but are not resolvable in any repository in scope. The
adapter interface signature assumed by §8 and §9 is therefore unconfirmed.
*Discharge:* supply the three artifacts and confirm the interface shape. Blocks
VE-04 and BC-03 entry.

**`BC-02-DEP-005` — `input_characterization` vocabulary undefined.**
*SPECIFICATION GAP.* B-VAL-015 asserts preservation but has no value domain to
preserve. Recorded as UNKNOWN per §11.4 until the Registry supplies the
vocabulary. *Discharge:* Registry declares the characterization value domain.

### Non-blocking observations — returned to Custodian, not acted on

**`BC-02-OBS-006` — Baseline / repository reachability observation.**
The construction baseline records D-1 CLOSED, APS-200 FROZEN / ACCEPTED, and the
CONF-003 §4.5 rebinding ACCEPTED. In `Aura-IDToken/aura-specification` as
checked out for this work package:

- `aps/APS-200_CANONICAL_DATA_MODEL.md` on `main` does not contain the D-1
  physical edit (no representation boundary, cross-implementation determinism,
  digest-input boundary or serialization-scope paragraph). That edit is
  reachable only from `claude/aps-200-spec-recovery-b7wc2h` (commit `c749a7c`,
  evidence `84e4962`).
- APS-200 has no §8.4. `conformance/CONF-003_CANONICAL_SERIALIZATION.md:99`
  still reads *"any form listed in APS-200 §8.4"*. The D-1 evidence record
  itself states this reference was deliberately left unrepaired and deferred to
  a separate reference-repair authorization.

This is a **branch-reachability / integration observation**, not a normative
contradiction: the accepted content exists and is identified, it is simply not
reachable from the default branch of the checkout used here. No recovery or
reconciliation gate is opened. BC-02 does not depend on APS-200 §8.4 and did not
modify APS-200 or CONF-003. Returned as
**OBSERVATION → UNRESOLVED → CUSTODIAN REVIEW**.

**`BC-02-OBS-007` — Present arrangement is local-copy, not transfer.**
*BOUNDARY GAP (AS-IS).* Documented in §1.1 and §9 with digests. RI-RS holds a
repository-resident fixture copy; RI-PY holds none; the specification-side
artifact is a third, distinct file. While any resident copy exists on either
side, B-VAL-019 is unfalsifiable, because a reconstruction source remains
available to the adapter. *Discharge:* VE-05. This observation does not re-open
CROSS-LANGUAGE-001 and alters no recorded verdict.

---

## 20. Next authorized work package

```text
BC-02  (this document — construction)
   ↓
[ discharge BC-02-DEP-001 … BC-02-DEP-005 ]
   ↓
BC-02 BOUNDARY VALIDATION      — execute §15; produce the Boundary Validation Report
   ↓
BC-03 — RI-PY ADAPTER
   ↓
BC-04 — RI-RS ADAPTER          (implied by §9 symmetry; not authorized here)
```

BC-02 VALIDATION is **not authorized by this document**. It requires a separate
Custodian authorization and cannot be entered while any §19 blocking dependency
is open.

Conformance execution — P-01, N-01 … N-08, CONF-003 §4.5 — remains **BLOCKED**
and is not reachable from this work package under any completion state of BC-02
or BC-03.

---

## Traceability

| Field | Value |
|---|---|
| Package ID | BC-02 |
| Boundary invariant | B-INV-01 |
| Assertions | B-VAL-011 … B-VAL-020 |
| Negative controls | BNC-1 … BNC-7 |
| Classification | Engineering boundary contract — non-normative |
| Authority created | NONE |
| Predecessor | BC-01 (unresolved — `BC-02-DEP-004`) |
| Successor | BC-02 BOUNDARY VALIDATION → BC-03 |
| Conformance status | NO RESULT |
| Evidence status | NOT GENERATED |
| Disposition | **BLOCKED — BC-02 CONSTRUCTION GAP** (§19 blocking dependencies) |

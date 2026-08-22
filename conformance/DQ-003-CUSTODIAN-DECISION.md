# DQ-003 — Custodian Decision: RI-RS JCS Surface

**Status:** DECISION RECORDED — DQ-003 remains OPEN  
**Authority:** Protocol Custodian / Architecture Owner  
**Scope:** RI-RS canonical serialization surface only  
**Date:** 2026-08-22  
**Production code change:** NONE  
**Normative APS-200 change:** NONE  

---

## 1. RI-RS JCS Surface

### 1.1 Observed implementation

The RI-RS repository contains:

```text
conformance/canonical/jcs.rs
```

The module exposes exactly one transformation:

```text
serde_json::Value -> RFC 8785 JCS -> Vec<u8>
```

The implementation delegates canonical serialization to:

```text
serde_json_canonicalizer::to_vec(value)
```

The source explicitly describes this module as a conformance-only surface and states that it is not wired into the production runtime or `src/` path. It does not modify the existing hash or Merkle semantics. [Observed source: aura-guard-v1.3/conformance/canonical/jcs.rs]

### 1.2 Dependency status

`serde_json_canonicalizer = "=0.3.2"` is currently declared under `[dev-dependencies]` in `aura-guard-v1.3/Cargo.toml`.

The repository comments explicitly classify it as a conformance-harness dependency and state that the runtime hash/Merkle path is untouched.

Therefore the current state is:

```text
JCS implementation       PRESENT
JCS fixture/conformance  PRESENT
Production wiring        ABSENT
Production dependency   ABSENT
```

### 1.3 Fixture reproduction

The DQ-003 execution evidence establishes that the existing JCS surface reproduced the expected Golden Fixture bytes.

This proves fixture reproduction for the exercised case.

It does **not** by itself prove complete RFC 8785/JCS conformance across the full allowed ENT-007 input domain.

Accordingly:

```text
fixture PASS
    !=
full JCS conformance
```

### 1.4 Normative context

The existing D3 evidence records that APS-200 §8 leaves the canonical serialization format for RI-PY/RI-RS interoperability unresolved, while requiring preservation of semantics and deterministic serialization where required. fileciteturn3file15

The specification completion matrix independently classifies canonical serialization as a P0 unresolved item and cross-language equivalence as not verified. fileciteturn3file6

---

## 2. Custodian Decision

### Decision: PROMOTE EXISTING JCS SURFACE

The Custodian approves the **existing RFC 8785 JCS implementation surface** as the candidate production canonicalization primitive for RI-RS, subject to the conformance conditions below.

This decision means:

1. RI-RS MUST NOT introduce a second independent JCS implementation merely to satisfy the production path.
2. The existing `conformance/canonical/jcs.rs` implementation is the designated implementation candidate for production promotion.
3. Production integration, when authorized, MUST use the existing JCS primitive rather than reimplementing RFC 8785 semantics.
4. Promotion does not constitute a declaration that full JCS or APS-200 conformance has already been proven.
5. The promotion remains gated by verification that the implementation covers the complete permitted ENT-007 input domain and by the required Golden Fixture / cross-language comparisons.

### Rationale

The existing surface already provides the required RFC 8785 transformation and is intentionally isolated from production code. The source-level evidence shows that it delegates canonicalization to a pinned JCS implementation rather than approximating JCS with ordinary `serde_json` serialization. fileciteturn5file0

The current dependency placement is deliberately non-production: `serde_json_canonicalizer` is pinned under `[dev-dependencies]` and the repository explicitly identifies it as a conformance-harness dependency. fileciteturn6file0

The correct architectural action is therefore promotion of the existing primitive, not creation of a second canonicalizer.

---

## 3. Promotion Conditions

The following conditions remain mandatory before production wiring is considered complete:

### C1 — JCS coverage

Verify RFC 8785 behavior over the complete input/value domain permitted by the ENT-007 contract, not only the existing Golden Fixture.

### C2 — Dependency closure

If C1 passes, move the pinned JCS dependency from the conformance-only dependency surface into the production dependency surface without changing the pinned version implicitly.

### C3 — Minimal adapter

The production adapter MUST remain composition-only:

```text
existing JCS
    + existing SHA-256
    + ENT-007 field selection
    + domain prefix 0x02 where normatively required
    + verification rules
```

The adapter MUST NOT reimplement cryptographic primitives or canonicalization semantics.

### C4 — Golden Fixture

The promoted surface MUST reproduce the normative Golden Fixture byte-for-byte.

### C5 — Cross-language evidence

Promotion to a fully verified conformance state requires comparison against the RI-PY surface using the same normative fixture/domain.

---

## 4. Consequences

### 4.1 RI-RS

Next action:

```text
JCS coverage verification
        ↓
production dependency promotion
        ↓
minimal ENT-007 composition adapter
        ↓
Golden Fixture comparison
```

No adapter implementation is authorized by this decision document alone.

### 4.2 RI-PY

RI-PY remains a separate remediation track.

The existing evidence identifies missing ENT-007 fields and unresolved canonical/hash-domain mappings. The D3 evidence specifically records gaps including `object_type`, `protocol_version`, `event_type`, and `event_payload_hash`, while `prev_hash`, `policy_hash`, and `input_hash` have identified correspondences. fileciteturn3file8

RI-PY remediation MUST therefore begin with a conformance-surface specification, not by copying the RI-RS implementation structure.

### 4.3 DQ-001 / DQ-002

This decision does not resolve the existing hash-domain questions.

The prior D3-S5 baseline explicitly records DQ-001 and DQ-002 as OPEN and states that no semantic or architectural decision has been made. fileciteturn3file5

In particular, this document does **not** establish any equality between:

```text
chain_hash
integrity_hash
event_payload_hash
```

Those remain separate decision/evidence tracks.

### 4.4 DQ-003

DQ-003 remains **OPEN** after this decision.

This artifact closes only the Custodian decision regarding the existing RI-RS JCS surface. It does not close adapter implementation, cross-language conformance, or the complete DQ-003 gate.

---

## 5. Governance Boundary

This document records an architectural decision about the RI-RS implementation surface. It does not amend APS-200, APS-100, SPEC-002, or any other normative protocol text.

The project governance baseline requires specification before implementation and distinguishes observed implementation behavior from normative protocol semantics. fileciteturn3file0

If the promotion changes normative protocol semantics, the corresponding normative specification change MUST be recorded in the appropriate APS/SPEC artifact; this document MUST NOT substitute for that normative amendment. The specification completion matrix explicitly identifies the governance path as evidence → human architectural decision → normative APS/SPEC amendment where semantics change → fixtures/tests → implementation → independent conformance. fileciteturn3file6

---

## 6. Decision Summary

```text
RI-RS JCS surface
        │
        ▼
fixture reproduction = PASS
        │
        ▼
existing RFC 8785 implementation = ACCEPTED CANDIDATE
        │
        ▼
CUSTODIAN DECISION = PROMOTE EXISTING JCS SURFACE
        │
        ├── no second canonicalizer
        ├── no adapter yet
        ├── no hash-domain decision
        └── no DQ-003 closure
                │
                ▼
JCS full-domain verification
                │
                ▼
minimal ENT-007 adapter
                │
                ▼
cross-language fixture comparison
                │
                ▼
DQ-003 closure gate
```

**END — DQ-003 Custodian Decision**

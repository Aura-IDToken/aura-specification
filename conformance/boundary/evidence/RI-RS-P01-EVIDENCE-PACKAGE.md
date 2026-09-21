# CONTROLLED P-01 HANDOFF — RI-RS RECEIVER SIDE — EVIDENCE PACKAGE

**Scope:** RI-RS receiver-side execution of the authorized Controlled P-01 Handoff.
**Authority:** NONE. This document records observed evidence only.
**B-VAL-014:** NOT EXECUTED
**§4.5:** NO RESULT
**CONFORMANCE:** NOT DETERMINED / BLOCKED

This package is an evidence input. It is not a conformance result, and it does
not establish PASS, FAIL, CONFORMANT, NON_CONFORMANT, acceptance state, a §4.5
result, or a B-VAL-014 result.

## 1. Execution environment

| Item | Value |
|---|---|
| Platform | `Linux-x86_64-6.18.44-fc-v21` |
| Host triple | `x86_64-unknown-linux-gnu` |
| rustc | `rustc 1.94.1 (e408947bf 2026-03-25)` |
| cargo | `cargo 1.94.1 (29ea6fb6a 2026-03-24)` |
| Environment id | `aura-ccr-linux-x86_64-rust-1.94.1` |
| Execution timestamp (UTC) | `2026-08-23T20:05:18Z` |

The repository declares no Rust toolchain pin (`rust-toolchain.toml` absent in
`aura-specification`; no workspace `Cargo.toml`). The stable toolchain present
in the execution environment was used.

## 2. P-01 artifact identity

| Item | Value |
|---|---|
| `fixture_id` | `FIX-DIGEST-P01` |
| Artifact | `FIX-DIGEST-P01.canonical.json` |
| Representation | raw UTF-8 octets |
| Octet length | 15 |
| Trailing newline | NONE (final octet `0x7d`) |
| Octets (hex) | `7b2261223a312c2262223a2278227d` |
| Issued-artifact SHA-256 | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` |
| Path | `conformance/boundary/p01/FIX-DIGEST-P01.canonical.json` |

**Artifact provenance note.** `FIX-DIGEST-P01.canonical.json` was not present in
any in-scope repository at the start of this execution. The artifact octets were
materialized byte-exactly from the issuance values carried by the authorized
handoff instruction and were then digest-verified against the stated
issued-artifact SHA-256. The digest agrees, so the octets consumed by RI-RS are
octet-identical to the issued artifact.

The artifact was **not** reconstructed from a parsed JSON object, pretty-printed,
normalized, re-serialized, or newline-terminated.

## 3. RI-RS execution

The BC-02.3 construction artifact `conformance/boundary/ri_rs_receiver.rs` was
**not modified**. It was referenced in place by an execution harness.

| Item | Value |
|---|---|
| Receiver source | `conformance/boundary/ri_rs_receiver.rs` (unmodified) |
| Source commit | `49e848a007b18b78240100246f7cc348cf9ebd62` |
| Receiver blob (git SHA-1) | `b2117f295902ae966e27ef99da8c574f057a7338` |
| Harness package | `conformance/boundary/ri-rs` (`ri-rs-boundary` v1.0.0, `publish = false`) |
| Adapter | `conformance/boundary/ri-rs/src/bin/p01_handoff.rs` |

### Commands

```
cd conformance/boundary/ri-rs
cargo build
cargo test
cargo run --bin p01_handoff -- \
    ../p01/FIX-DIGEST-P01.canonical.json \
    ../evidence/RI-RS-P01-RECEIPT.json
```

### Results

- `cargo build` — succeeded. One pre-existing `non_camel_case_types` style
  warning originating in the construction artifact; not corrected, because
  BC-02.3 is CONSTRUCTED and outside this task's authority.
- `cargo test` — **12 passed, 0 failed** (BC-02.3 construction tests
  `r_val_001`…`r_val_012`, synthetic material).
- `cargo run --bin p01_handoff` — exit code `0`.

### Octet intake

The adapter reads the artifact with `std::fs::read`, yielding `Vec<u8>`, and
passes those octets directly to `ri_rs_receiver::receive`. `receive()` computes
`Sha256::digest(&raw_octets)` over that byte sequence.

No expected digest, parsed object, reconstructed JSON, hexadecimal text, or
Base64 text was used as digest input. `receive()`'s signature accepts no digest
parameter, so a supplied digest is structurally impossible.

| Observation | Value |
|---|---|
| Octets read | 15 |
| Octets (hex) | `7b2261223a312c2262223a2278227d` |
| Receiver-derived SHA-256 | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` |

The receiver-derived digest equals the issued-artifact digest. This is recorded
as an observed fact about the handoff, not as a conformance determination.

## 4. Receipt

BC-02.1 deterministic transport form (§12: UTF-8, lexicographic member order,
compact, explicit fields, Base64 transport encoding of `raw_octets`, no `null`):

```json
{"adapter":{"adapter_id":"BC-02.3-RS-P01-HANDOFF-ADAPTER","adapter_version":"1.0.0"},"environment":{"environment_id":"aura-ccr-linux-x86_64-rust-1.94.1","platform":"Linux-x86_64-6.18.44-fc-v21 (x86_64-unknown-linux-gnu)","runtime":"rustc 1.94.1 (e408947bf 2026-03-25) / cargo 1.94.1 (29ea6fb6a 2026-03-24)"},"fixture":{"fixture_artifact_identity":"FIX-DIGEST-P01.canonical.json","fixture_id":"FIX-DIGEST-P01"},"handoff":{"method":"local-octet-file-transfer","status":"TRANSFERRED"},"received":{"octet_length":15,"raw_octets":"eyJhIjoxLCJiIjoieCJ9","recomputed_sha256":"ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667"},"receiver":{"implementation_id":"aura-ri-rs","implementation_version":"1.0.0","language":"Rust","receiver_id":"RI-RS","source_commit":"49e848a007b18b78240100246f7cc348cf9ebd62"},"schema_id":"BC-02.1-COMMON-RECEIPT","schema_version":1}
```

`raw_octets` is carried as Base64 per BC-02.1 §6 and §12.8. `eyJhIjoxLCJiIjoieCJ9`
decodes to exactly the 15 received octets; the digest is computed over the
decoded octets, never over the Base64 characters.

**Serialization-layer note.** The `serde` derive on the BC-02.3 construction
artifact emits `raw_octets` as a JSON integer array. BC-02.1 §12.8 requires the
Base64 transport encoding, and §12.4 requires lexicographic member order. The
adapter performs that transport serialization at the adapter boundary, per
BC-02.1 §8, which defines the adapter as an independent engineering artifact.
The construction artifact was not changed.

## 5. R-VAL-001…012

Schema/receipt validation only. These are **not** B-VAL-014 cases, and they do
not execute §4.5 or determine protocol conformance.

| ID | Scope | Result | Observation |
|---|---|---|---|
| R-VAL-001 | schema identity/version present | PASS | `schema_id=BC-02.1-COMMON-RECEIPT`, `schema_version=1` |
| R-VAL-002 | fixture identity fields present | PASS | `fixture_id=FIX-DIGEST-P01`, `fixture_artifact_identity=FIX-DIGEST-P01.canonical.json` |
| R-VAL-003 | handoff state in closed domain | PASS | `status=TRANSFERRED`; no prohibited value present |
| R-VAL-004 | received length explicit | PASS | `octet_length=15` = intake 15 = `raw_octets` 15 = Base64-decoded 15 |
| R-VAL-005 | recomputed hash receiver-derived | PASS | receiver-derived digest equals independent recomputation over the intake octets; `validate_schema()` returned `Ok` |
| R-VAL-006 | receiver identity preserved | PASS | `receiver_id=RI-RS`, `language=Rust` |
| R-VAL-007 | implementation identity preserved | PASS | `implementation_id=aura-ri-rs`, `implementation_version=1.0.0`, `source_commit=49e848a…`; distinct from `receiver_id` |
| R-VAL-008 | adapter identity preserved | PASS | `adapter_id=BC-02.3-RS-P01-HANDOFF-ADAPTER`, `adapter_version=1.0.0`; distinct from `implementation_id` |
| R-VAL-009 | environment identity preserved | PASS | `environment_id`, `platform`, `runtime` all explicit |
| R-VAL-010 | raw material not silently reconstructed | PASS | receipt octets byte-equal the octets read from the issued artifact; Base64 transport decodes to the same octets |
| R-VAL-011 | deterministic serialization possible | PASS | repeat serialization identical; keys lexicographic at every level; no insignificant whitespace; `null`-free; 870 octets |
| R-VAL-012 | no conformance-result authority | PASS | no forbidden key; no `PASS`/`FAIL`/`CONFORMANT`/`NON_CONFORMANT` value; field set exactly the BC-02.1 set |

All twelve are schema/receipt validation statuses. They do not establish
protocol conformance for RI-RS.

## 6. RI-PY / RI-RS evidence comparison

| Item | RI-PY | RI-RS |
|---|---|---|
| Received octets | 15 | 15 (observed) |
| Receiver-derived SHA-256 | `ecf9e98e…d4e65667` | `ecf9e98e…d4e65667` (observed) |
| Receipt | reported generated | generated, repository-resident |

**Evidence gap.** The BC-02.2 RI-PY receiver implementation and its P-01 receipt
are not present in any of the five in-scope repositories. The RI-PY column above
reproduces values reported by the handoff instruction; it was not reproduced
from a repository-resident RI-PY artifact and is not independently verifiable
from current repository state.

The two receiver observations agree. Agreement between receiver observations is
**not** conformance and is not treated as one.

## 7. Authority isolation check

| Check | Result |
|---|---|
| Receipt contains `conformance_result` | NO |
| Receipt contains PASS/FAIL/CONFORMANT/NON_CONFORMANT | NO |
| Receipt contains acceptance result | NO |
| Receipt contains §4.5 result | NO |
| Receipt contains B-VAL-014 result | NO |
| Receipt contains digest-output state | NO |
| Receipt field set exceeds BC-02.1 | NO |
| Normative specification modified | NO |
| Fixture modified | NO |
| Construction artifact `ri_rs_receiver.rs` modified | NO |

`validate_schema()` returns a construction-validity `Result`. It is not a
conformance result.

## 8. Controlled P-01 Handoff status

```text
BC-02.1 Common Receipt Schema      CONSTRUCTED
BC-02.2 RI-PY Receiver             CONSTRUCTED (per BC-02.3 §7; artifact absent from repository)
BC-02.3 RI-RS Receiver             CONSTRUCTED
Controlled P-01 Handoff (RI-RS)    EXECUTED
B-VAL-014                          NOT EXECUTED
§4.5                               NO RESULT
Conformance                        BLOCKED
```

## 9. Explicit non-execution

- **B-VAL-014 NOT EXECUTED**
- **§4.5 NO RESULT**
- **CONFORMANCE NOT DETERMINED**

Not run: B-VAL-014, §4.5 verification, conformance suite, acceptance suite,
protocol PASS/FAIL, canonicalization experiments, digest-input redesign, fixture
modification, specification recovery, normative edits.

## 10. Evidence artifacts

See `RI-RS-P01-EVIDENCE-MANIFEST.json` for SHA-256 and octet length of every
evidence file, the issued artifact, the construction artifact, the harness
sources, and the BC-02.1 / BC-02.3 specification artifacts as read.

| File | Role |
|---|---|
| `conformance/boundary/p01/FIX-DIGEST-P01.canonical.json` | issued P-01 artifact (15 octets) |
| `conformance/boundary/evidence/RI-RS-P01-RECEIPT.json` | BC-02.1 receipt |
| `conformance/boundary/evidence/RI-RS-P01-EXECUTION-LOG.txt` | execution transcript |
| `conformance/boundary/evidence/RI-RS-P01-EXECUTION-TIMESTAMP.txt` | UTC execution timestamp |
| `conformance/boundary/evidence/RI-RS-P01-EVIDENCE-MANIFEST.json` | evidence file hashes |
| `conformance/boundary/ri-rs/` | execution harness (non-normative) |

## 11. Reported discrepancies (for Protocol Custodian)

Reported, not reconciled, per CLAUDE.md authority precedence:

1. **Issued artifact absent from repository.** `FIX-DIGEST-P01.canonical.json`
   did not exist in any in-scope repository. It was materialized from the
   issuance values in the authorized instruction and digest-verified. No P-01
   issuance record exists in the repository to cross-check against.
2. **BC-02.2 RI-PY artifact absent.** No RI-PY receiver implementation and no
   RI-PY P-01 receipt exist in any in-scope repository, though the RI-PY side is
   declared CONSTRUCTED and executed.
3. **Gate-state inconsistency between construction artifacts.** BC-02.1 §18
   records `BC-02.2 RI-PY  NOT STARTED`; BC-02.3 §7 records
   `BC-02.2 RI-PY Receiver  CONSTRUCTED`.
4. **Transport-encoding gap in the construction artifact.** The BC-02.3 `serde`
   derive does not by itself satisfy BC-02.1 §12.4 (lexicographic order) or
   §12.8 (Base64 `raw_octets`). Handled at the adapter boundary here; left
   unmodified in BC-02.3.

None of these were silently reconciled, and none altered the octets consumed by
RI-RS.

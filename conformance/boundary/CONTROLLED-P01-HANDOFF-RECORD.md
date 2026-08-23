# CONTROLLED P-01 HANDOFF RECORD — RI-PY + RI-RS

**Event:** First controlled real-material P-01 handoff through both independent receivers
**Fixture:** `FIX-DIGEST-P01`
**Date (UTC):** 2026-08-23
**Disposition:** **COMPLETE — real P-01 evidence captured by both independent receivers**

## Authority notice

Non-normative engineering record. This is an **evidence-generation event, not a
conformance decision**.

```text
issued artifact
      ↓
 actual handoff
      ↓
RI-PY receipt ─────┐
                   ├── evidence comparison
RI-RS receipt ─────┘
      ↓
 observation only
```

**P-01 = EXECUTED (handoff) · B-VAL-014 = NOT EXECUTED · CONF-003 §4.5 = NO RESULT · CONFORMANCE = NOT DETERMINED**

No `conformance_result` was created. No PASS/FAIL, CONFORMANT/NON_CONFORMANT, or
acceptance result was assigned. R-VAL results below are receipt/schema
validation and MUST NOT be read as protocol PASS.

## 1. Issued artifact

| Property | Value |
|---|---|
| Path | `conformance/boundary/p01/FIX-DIGEST-P01.canonical.json` |
| `fixture_id` | `FIX-DIGEST-P01` |
| `fixture_artifact_identity` | `FIX-DIGEST-P01.canonical.json` |
| Octet length | 15 |
| Octets (hex) | `7b2261223a312c2262223a2278227d` |
| SHA-256 | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` |
| Trailing newline | none (final octet `0x7d`) |
| Git blob | `b45ffa980a1a776b6143d7fcb255fbfa8a436582` |

### 1.1 Pre-intake verification (before either receiver ran)

All seven checks performed outside both receivers:

| # | Check | Result |
|---|---|---|
| 1 | Read in binary mode | ok |
| 2 | Actual octet length | 15 |
| 3 | Actual octets / hex | `7b2261223a312c2262223a2278227d` |
| 4 | Independent SHA-256 computed outside the receivers | `ecf9e98e…d4e65667` |
| 5 | Matches issued-artifact identity | **yes** |
| 6 | No trailing newline | confirmed, final octet `0x7d` |
| 7 | Repository path and fixture identity | confirmed |

Worktree blob equals committed blob; zero uncommitted modifications. The
artifact was **not** reconstructed, created from an object, pretty-printed,
newline-terminated, normalized, or parsed and re-serialized before intake.

The expected digest was used **only** as an issuance identity check. It was not
supplied to either receiver as digest input.

## 2. RI-PY execution identity

| Field | Value |
|---|---|
| `receiver_id` | `RI-PY` |
| `implementation_id` | `aura-ri-py` |
| `language` | `Python` |
| `implementation_version` | `1.0.0` |
| `source_commit` | `d943807c359af982fd573ec4ff690b7fa265dc42` |
| `adapter_id` | `BC-02.2-RI-PY-BOUNDARY-ADAPTER` |
| `adapter_version` | `1.0.0` |
| `environment_id` | `ri-py-linux-x86_64-cpython-3.11.15` |
| `platform` | `Linux-x86_64-6.18.44-fc-v21` |
| `runtime` | `CPython 3.11.15` |
| `handoff.status` | `TRANSFERRED` |
| `handoff.method` | `repository-resident-octet-file-transfer` |
| `octet_length` | 15 |
| `raw_octets` transport | `eyJhIjoxLCJiIjoieCJ9` (Base64, BC-02.1 §12.8) |
| Receiver-derived SHA-256 | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` |
| Executed at (UTC) | `2026-08-23T21:36:53Z` |
| Implementation repo / checkout | `aura-poc-a-core-v3.3` @ `b86a38261fad507b9f2cfda3447d71dce8f211f6` |
| `ri_py_receiver.py` blob | `708cc01b1f74080f3cf0f95e1b402851cdd77178` — identical at baseline, HEAD, worktree |

Command:

```
python3 -m conformance.boundary.ri_py_adapter <artifact> \
  --fixture-id FIX-DIGEST-P01 \
  --fixture-artifact-identity FIX-DIGEST-P01.canonical.json \
  --source-commit d943807c359af982fd573ec4ff690b7fa265dc42 \
  --method repository-resident-octet-file-transfer \
  --environment-id ri-py-linux-x86_64-cpython-3.11.15 \
  --receipt-out <evidence>/RI-PY-P01-RECEIPT.json
```

Exit code 0. The adapter opened the artifact in binary mode, passed the octets
unchanged, and supplied no digest — `receive()` exposes no digest parameter
(`receive_accepts_digest_parameter=False`, checked at runtime by R-VAL-005).

## 3. RI-RS execution identity

| Field | Value |
|---|---|
| `receiver_id` | `RI-RS` |
| `implementation_id` | `aura-ri-rs` |
| `language` | `Rust` |
| `implementation_version` | `1.0.0` |
| `source_commit` | `49e848a007b18b78240100246f7cc348cf9ebd62` |
| `adapter_id` | `BC-02.3-RS-P01-HANDOFF-ADAPTER` |
| `adapter_version` | `1.0.0` |
| `environment_id` | `ri-rs-linux-x86_64-rust-1.94.1` |
| `platform` | `Linux-x86_64-6.18.44-fc-v21` |
| `runtime` | `rustc 1.94.1 (e408947bf 2026-03-25)` |
| `handoff.status` | `TRANSFERRED` |
| `handoff.method` | `repository-resident-octet-file-transfer` |
| `octet_length` | 15 |
| `raw_octets` transport | `eyJhIjoxLCJiIjoieCJ9` (Base64, BC-02.1 §12.8) |
| Receiver-derived SHA-256 | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` |
| Executed at (UTC) | `2026-08-23T21:37:11Z` |
| Implementation repo / checkout | `aura-specification` @ `5f226e6b5bbeacd7af38e17816936eddc46b589f` |
| `ri_rs_receiver.rs` blob | `b2117f295902ae966e27ef99da8c574f057a7338` — identical at baseline, HEAD, worktree |

Command: `cargo run --bin p01_handoff -- <artifact> <receipt-out>` with identity
supplied through the adapter's environment interface. Exit code 0. The receiver
independently took `Sha256::digest(&raw_octets)` over the intake `Vec<u8>`; the
adapter applied the already-audited BC-02.1 transport serialization afterwards.
No digest was supplied to the receiver — `receive()` accepts no digest argument.

## 4. Cross-receiver comparison

### A. Received octets

```text
RI-PY : 7b2261223a312c2262223a2278227d
RI-RS : 7b2261223a312c2262223a2278227d
```

| Comparison | Result |
|---|---|
| RI-PY octets == RI-RS octets | **identical** |
| RI-PY octets == issued artifact file | **identical** |
| RI-RS octets == issued artifact file | **identical** |

### B. Octet length

RI-PY 15 · RI-RS 15 · issued 15 · both Base64 transports decode to 15. All equal.

### C. Receiver-derived digest

| Source | Value |
|---|---|
| RI-PY receiver-derived | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` |
| RI-RS receiver-derived | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` |
| Independent SHA-256 of received octets | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` |
| Issued-artifact identity | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` |

All four equal. Negative control: neither digest equals `SHA256(Base64 characters)`,
confirming the digest was taken over the octets, not over the transport text.

### D. Fixture identity

Both receipts carry `fixture_id = FIX-DIGEST-P01` and
`fixture_artifact_identity = FIX-DIGEST-P01.canonical.json`. Neither derived
identity from a parsed object.

### E. Provenance — independent, as intended

Seven fields differ between the two receipts. Every one is provenance or
language, which BC-02.1 does not require to match:

| Field | RI-PY | RI-RS |
|---|---|---|
| `receiver.receiver_id` | `RI-PY` | `RI-RS` |
| `receiver.implementation_id` | `aura-ri-py` | `aura-ri-rs` |
| `receiver.language` | `Python` | `Rust` |
| `receiver.source_commit` | `d943807c…65dc42` | `49e848a0…d4e65667`* |
| `adapter.adapter_id` | `BC-02.2-RI-PY-BOUNDARY-ADAPTER` | `BC-02.3-RS-P01-HANDOFF-ADAPTER` |
| `environment.environment_id` | `ri-py-linux-x86_64-cpython-3.11.15` | `ri-rs-linux-x86_64-rust-1.94.1` |
| `environment.runtime` | `CPython 3.11.15` | `rustc 1.94.1 (e408947bf 2026-03-25)` |

\* full value `49e848a007b18b78240100246f7cc348cf9ebd62`.

Everything observed about the **material** is identical; everything that differs
is *who observed it*. That is the intended shape of two-implementation evidence.

All provenance fields are present and non-empty in both receipts, and in both
`receiver_id`, `implementation_id` and `adapter_id` are three distinct values.

### F. Receipt schema

| Property | RI-PY | RI-RS |
|---|---|---|
| `schema_id` / `schema_version` | `BC-02.1-COMMON-RECEIPT` / `1` | `BC-02.1-COMMON-RECEIPT` / `1` |
| Field set exactly the BC-02.1 set | yes | yes |
| Lexicographic member order, every level | yes | yes |
| Compact, no insignificant whitespace | yes | yes |
| `null`-free | yes | yes |
| `handoff.status` in closed domain | `TRANSFERRED` | `TRANSFERRED` |

### G. Authority isolation

| Check | RI-PY | RI-RS |
|---|---|---|
| Forbidden keys (`conformance_result`, `acceptance_result`, `result`, `verdict`, …) | none | none |
| Forbidden values (`PASS`, `FAIL`, `CONFORMANT`, `NON_CONFORMANT`) | none | none |
| §4.5 result / B-VAL-014 result / digest-output state | absent | absent |

## 5. R-VAL-001…012 — both receipts

Receipt/schema validation only. **Not** conformance results.

| ID | Scope | RI-PY | RI-RS |
|---|---|---|---|
| R-VAL-001 | schema identity/version present | PASS | PASS |
| R-VAL-002 | fixture identity fields present | PASS | PASS |
| R-VAL-003 | handoff state in closed domain | PASS | PASS |
| R-VAL-004 | received length explicit | PASS | PASS |
| R-VAL-005 | hash receiver-derived | PASS | PASS |
| R-VAL-006 | receiver identity preserved | PASS | PASS |
| R-VAL-007 | implementation identity preserved | PASS | PASS |
| R-VAL-008 | adapter identity preserved | PASS | PASS |
| R-VAL-009 | environment identity preserved | PASS | PASS |
| R-VAL-010 | raw material not silently reconstructed | PASS | PASS |
| R-VAL-011 | deterministic serialization possible | PASS | PASS |
| R-VAL-012 | no conformance-result authority | PASS | PASS |

24 of 24 assertions PASS across the two receipts.

## 6. Receipt representation — logical bytes vs file termination (A-OBS-01)

Per §10 of the authorization, the distinction is stated explicitly and the
serialization contract was **not** altered:

| Receipt | Logical serialized receipt | Stored file |
|---|---|---|
| RI-PY | 802 octets, SHA-256 `34eb945c1c8d47e837e14bb19801fa4db1ad27e256b4d994f53373cea2e692b2` | 803 octets, trailing `0x0A` |
| RI-RS | 816 octets, SHA-256 `b4f0fdacd295d2154e5ce2eec11beae3fb4c0032ba33c49f6b9f202d97c7c624` | 817 octets, trailing `0x0A` |

The **logical serialized receipt** is the BC-02.1 §12 transport form and carries
no insignificant whitespace. The stored file is that form plus one POSIX line
terminator — a file termination convention, not part of the receipt
serialization. Both manifests record both representations. No adapter or
serialization logic was modified to remove it.

## 7. A-OBS-02 — recorded as encountered

The RI-RS adapter's R-VAL-002 additionally requires
`fixture_id == "FIX-DIGEST-P01"`, exceeding BC-02.1 §15. On this handoff the
fixture *is* `FIX-DIGEST-P01`, so the condition is satisfied and the reported
RI-RS R-VAL-002 PASS is sound. The implementation was **not** modified.

## 8. Prior evidence preserved

The earlier RI-RS-only execution evidence remains at
`conformance/boundary/evidence/RI-RS-P01-*` and was **not** overwritten or
rewritten. This handoff's evidence is written to a separate directory:

```text
conformance/boundary/evidence/controlled-p01-handoff/
```

## 9. Evidence artifacts

| File | SHA-256 | Octets |
|---|---|---|
| `RI-PY-P01-RECEIPT.json` | `7356537db900d058a65640a036919a69cc7bbb0bac5abb8b573baa4610ab17f3` | 803 |
| `RI-PY-P01-EXECUTION-LOG.txt` | `dc23f41c915e86490ded12bf0265766aa55fa4f3c0ca629b6e81c877c08a4ae2` | 3176 |
| `RI-PY-P01-EXECUTION-TIMESTAMP.txt` | `6c9994aaa9e4c2040bd22f3d8e12f3ac87ef5e4ff3fc13a78eff0cb8575aafa5` | 45 |
| `RI-PY-P01-EVIDENCE-MANIFEST.json` | see file | — |
| `RI-RS-P01-RECEIPT.json` | `e270df49a11a1efb86137bfbffe5b40c0d6bc669423306b0a4449b9663449cff` | 817 |
| `RI-RS-P01-EXECUTION-LOG.txt` | `890f66b4563b1704471fc016f0ac4b8ef454c4df21fa2bec712f6119dd4a4560` | 2977 |
| `RI-RS-P01-EXECUTION-TIMESTAMP.txt` | `3383720af3d925031618c13f4d4ba5193c0c17b05ee5289f4ab1d7f7632d177f` | 45 |
| `RI-RS-P01-EVIDENCE-MANIFEST.json` | see file | — |
| `CROSS-RECEIVER-COMPARISON.txt` | `1520f50a059a29429bfeb32162fea9269eaafb56ff25429041c2cd5d644c3384` | 5124 |
| `conformance/boundary/p01/FIX-DIGEST-P01.canonical.json` | `ecf9e98ec0641e23113ff3ce8bdc78d0ddd249886517fd4a7f68cc83d4e65667` | 15 |

## 10. Commit and branch provenance

| Repository | Branch | Commit at execution |
|---|---|---|
| `Aura-IDToken/aura-specification` | `claude/ri-rs-p01-handoff-ga84l6` | `5f226e6b5bbeacd7af38e17816936eddc46b589f` |
| `Aura-IDToken/aura-poc-a-core-v3.3` | `claude/ri-rs-p01-handoff-ga84l6` | `b86a38261fad507b9f2cfda3447d71dce8f211f6` |

Both receiver implementations were verified unmodified before execution: blob
identical at audited baseline, at HEAD, and in the working tree, with zero
uncommitted modifications.

## 11. Explicit non-execution

The following remain unexecuted:

- **B-VAL-014**
- **CONF-003 §4.5**
- conformance suite; acceptance suite
- protocol PASS/FAIL; CONFORMANT/NON_CONFORMANT determination
- canonicalization experiments; digest-input redesign
- normative specification changes

Nothing was modified in this task: BC-02.1, the BC-02.2 receiver and adapter,
the BC-02.3 receiver, the RI-RS adapter, `FIX-DIGEST-P01`, canonicalization
rules, digest-input rules, BC-02.1 §18, and the normative specification are all
unchanged. Only new evidence files were added.

## 12. Status

```text
CONTROLLED P-01 HANDOFF — COMPLETE

meaning: real P-01 evidence successfully captured by both independent receivers.

NOT meaning: conformance pass.

B-VAL-014        NOT EXECUTED
CONF-003 §4.5    NO RESULT
Conformance      NOT DETERMINED
```

Do not proceed to B-VAL-014 on the basis of this record. Agreement between two
receiver observations is evidence that the same octets were received and
independently digested. It is not a protocol result.

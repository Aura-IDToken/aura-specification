# BC-02 — CROSS-RECEIVER PRE-EXECUTION AUDIT

**Work package:** BC-02 cross-receiver pre-execution audit (authorized)
**Date (UTC):** 2026-08-23T21:17:18Z
**Disposition:** **BLOCKED — RI-PY source_commit provenance is not the implementation baseline**

## Authority notice

Non-normative engineering record. Creates no protocol authority, alters no
recorded verdict, and determines no conformance.

**P-01 = NOT EXECUTED · B-VAL-014 = NOT EXECUTED · §4.5 = NO RESULT · CONFORMANCE = NOT DETERMINED**

## 1. Scope

Close the two outstanding audit items before the Controlled P-01 Handoff:
RI-RS BC-02.1 §12 serialization conformity, and RI-PY receipt source-commit
provenance. Then compare both receivers against BC-02.1 only, record custodian
construction state, and determine the execution gate.

No P-01 artifact was handed to any receiver in this audit. All executable
evidence below was produced from **synthetic** material. The repository-resident
P-01 receipt was **inspected as a stored artifact**, not regenerated.

## 2. Repositories and commits inspected

| Repository | Commit | Role |
|---|---|---|
| `Aura-IDToken/aura-specification` | `1ccd58795e514cea8394b59b1724a95b8ddd2084` | BC-02.1, BC-02.3, RI-RS adapter, RI-RS P-01 evidence |
| `Aura-IDToken/aura-poc-a-core-v3.3` | `d943807c359af982fd573ec4ff690b7fa265dc42` | BC-02.2 RI-PY receiver, adapter, evidence |
| `Aura-IDToken/aura-guard-v1.3` | `35082d7b4880dad780fb55a1a5f3ac0ef4322674` | inspected; carries no BC-02 boundary artifact |

Synthetic audit material: 43 octets,
`42432d30322e322073796e74686574696320636f6e737472756374696f6e206d6174657269616c2000feff`,
SHA-256 `de2c1a21f4518514d8f172245ae83f3bea3f4841c15a6bc62b50bcd0678a2981`.
Contains NUL and `0xFE 0xFF`; not valid UTF-8; not any issued fixture.

## 3. RI-RS serialization path

```text
issued octets (Vec<u8>)
      ↓
ri_rs_receiver.rs:92   Sha256::digest(&raw_octets)      <- digest taken HERE
      ↓
BoundaryReceipt { received.raw_octets: Vec<u8>, recomputed_sha256 }
      ↓
p01_handoff.rs:74      B64.encode(&r.received.raw_octets)   <- transport encoding
      ↓
p01_handoff.rs:215     serde_json::to_string(&json)
      ↓
p01_handoff.rs:409     fs::write(receipt_out, format!("{serialized}\n"))
```

| Component | Path |
|---|---|
| Receiver (BC-02.3, unmodified) | `conformance/boundary/ri_rs_receiver.rs` |
| Adapter | `conformance/boundary/ri-rs/src/bin/p01_handoff.rs` |
| Transport mapping | `transport_json()`, same file |

### 3.1 The receiver's own serde output is NOT BC-02.1 §12 compliant

Compliance was **not** inferred from `serde_json::to_vec()`. A probe was run
against the receiver's derived `Serialize` implementation directly:

```text
serde raw_octets JSON type : ARRAY of integers
serde raw_octets value     : [66,67,45,48,50,46,50,32,115,121,110,116,104,101,116,105,99]
serde top-level key order  : ["adapter","environment","fixture","handoff",
                              "received","receiver","schema_id","schema_version"]
```

The derived form violates BC-02.1 §12.8: `raw_octets` is an integer array, not
the declared Base64 transport encoding. Key ordering happens to be lexicographic
because `serde_json` 1.0.151 is resolved **without** the `preserve_order`
feature — `Cargo.lock` contains no `indexmap` entry — so `serde_json::Map` is a
`BTreeMap`. That ordering is therefore a property of the resolved dependency
graph, not of the derive.

The probe was removed after use and is not repository-resident.

### 3.2 The adapter performs the required conversion

`transport_json()` builds the transport object independently of the derive and
applies `B64.encode` at the `raw_octets` member. Verified from adapter output,
not from source reading alone.

## 4. RI-RS serialization findings

Verified against three artifacts: the RI-RS adapter run on synthetic material,
the RI-PY adapter run on the same synthetic material, and the repository-resident
RI-RS P-01 receipt inspected as stored.

| # | BC-02.1 §12 requirement | RI-RS synthetic | RI-PY synthetic | RI-RS P-01 (stored) |
|---|---|---|---|---|
| 1 | UTF-8 encoding | PASS | PASS | PASS |
| 2 | Lexicographic member order, every level | PASS | PASS | PASS |
| 3 | Compact JSON | PASS | PASS | PASS |
| 4 | No insignificant whitespace (serialization) | PASS | PASS | PASS |
| 5 | All required fields explicit | PASS | PASS | PASS |
| 6 | No `null` | PASS | PASS | PASS |
| 7 | `raw_octets` as declared Base64 transport | PASS | PASS | PASS |
| 8 | Base64 confined to transport representation | PASS | PASS | PASS |
| 9 | SHA-256 over logical octets **before** transport encoding | PASS | PASS | PASS |
| 10 | No `conformance_result` or equivalent authority field | PASS | PASS | PASS |

Requirement 9 was checked positively and negatively: the recorded digest equals
`SHA256(decoded octets)` and does **not** equal `SHA256(Base64 characters)`.
Requirement 7/8 were checked by decoding the transport value back to the exact
octets.

```text
RI-RS BC-02.1 serialization: PASS
```

### 4.1 A-OBS-01 — trailing newline in the stored receipt file

Both adapters append `0x0A` when writing the receipt to disk
(`p01_handoff.rs:409`; `ri_py_adapter.py` `main()`).

| Artifact | Serialization | Stored file |
|---|---|---|
| RI-RS synthetic | 804 octets | 805 octets |
| RI-PY synthetic | 806 octets | 807 octets |
| RI-RS P-01 (stored) | 870 octets | 871 octets |

The **serialization** carries no insignificant whitespace and satisfies §12.5.
The **stored file** is the serialization plus a POSIX line terminator. If the
file is read as the transport artifact, that terminator is insignificant
whitespace outside the §12 form.

This does not affect any digest: the receipt is never a digest input, and
`recomputed_sha256` is taken over the received octets, not over the receipt.
Both implementations behave identically, so it introduces no cross-receiver
asymmetry.

Smallest remediation, if the custodian rules the stored file to be the transport
artifact: drop the `\n` at `p01_handoff.rs:409` and in `ri_py_adapter.py`'s write
call. Not applied — outside this task's authority.

### 4.2 A-OBS-02 — RI-RS adapter R-VAL-002 is over-constrained

`p01_handoff.rs` R-VAL-002 asserts:

```rust
!receipt.fixture.fixture_id.is_empty()
    && !receipt.fixture.fixture_artifact_identity.is_empty()
    && receipt.fixture.fixture_id == "FIX-DIGEST-P01"
```

BC-02.1 §15 defines R-VAL-002 as *"Fixture identity fields are present."* The
third conjunct additionally requires one specific fixture identity, so the
adapter's R-VAL-002 is a P-01 identity assertion, not the BC-02.1 schema
assertion. Observed directly: on synthetic material the adapter reports
`R-VAL-002 FAIL` while both fixture identity fields are present and non-empty.

Effect on recorded evidence: **none**. On the P-01 path the fixture identity is
`FIX-DIGEST-P01`, so the conjunct holds and the recorded RI-RS P-01 R-VAL-002
PASS is sound. The RI-PY implementation does not carry this constraint.

Smallest remediation: drop the third conjunct so the assertion matches BC-02.1
§15. Not applied — outside this task's authority.

Neither observation blocks the gate. Both are recorded for custodian disposition.

## 5. RI-PY provenance finding

The BC-02.2 construction evidence and the synthetic construction receipt record:

```text
source_commit = 64bf959b1d23fbd5433723476c611ab66d423953
```

Verified against the repository:

| Check | Result |
|---|---|
| `git cat-file -e 64bf959:conformance/boundary/ri_py_receiver.py` | **ABSENT** — path does not exist in that commit |
| Commit `64bf959` subject | `Delete .github/workflows/python-package-conda.yml` (2026-08-17) |
| Full history of `conformance/boundary/ri_py_receiver.py` | a single commit: `d943807c359af982fd573ec4ff690b7fa265dc42` (2026-08-23) |
| Is `64bf959` an ancestor of `d943807`? | yes — it is the pre-construction parent |

`64bf959` is the repository HEAD **before** BC-02.2 was constructed. It contains
no RI-PY receiver, so it cannot be the implementation baseline for
`implementation_version = 1.0.0`. The value was captured by `git rev-parse HEAD`
during the construction run, which necessarily preceded the commit that
introduced the implementation.

```text
RI-PY source provenance: BLOCKED
correct provenance value: d943807c359af982fd573ec4ff690b7fa265dc42
```

The correct value is **not** being asserted merely because it is the construction
commit. It is correct because it is the only commit in which
`conformance/boundary/ri_py_receiver.py` exists, and the implementation baseline
must be a commit that contains the implementation. Here the implementation
source commit and the construction commit coincide, because the implementation
was introduced by the construction:

```text
implementation source commit  d943807
        ↓ (same commit)
BC-02.2 construction commit   d943807
        ↓
construction evidence         conformance/boundary/evidence/BC-02.2-*
```

Not corrected in this task: amending the recorded value means editing
`BC-02.2-CONSTRUCTION-EVIDENCE.md` §2 and `BC-02.2-RVAL-REPORT.txt`, which are
BC-02.2 artifacts. Separate authorization required.

### 5.1 RI-RS provenance — contrast check

The same check was applied to the peer, which passes:

| Check | Result |
|---|---|
| `49e848a:conformance/boundary/ri_rs_receiver.rs` | **PRESENT** |
| Blob at `49e848a` | `b2117f295902ae966e27ef99da8c574f057a7338` |
| Blob in working tree | `b2117f295902ae966e27ef99da8c574f057a7338` — identical |

The RI-RS P-01 receipt's `source_commit = 49e848a…` is a correct implementation
baseline. The defect is confined to RI-PY.

## 6. Cross-receiver comparison

Both receivers were given identical synthetic octets and identical fixture,
receiver, implementation, adapter and environment identity values. Their
deterministic transport serializations were compared field by field.

**Result: exactly one differing field.**

```text
.receiver.language    RI-PY = "Python"    RI-RS = "Rust"
```

That difference is required by BC-02.1 §3, which mandates `receiver.language` as
a distinct field describing the implementation. Identical values there would be
a defect, not compatibility.

| BC-02.1 element | RI-PY | RI-RS | Compatible |
|---|---|---|---|
| `schema_id` | `BC-02.1-COMMON-RECEIPT` | `BC-02.1-COMMON-RECEIPT` | yes |
| `schema_version` | `1` | `1` | yes |
| Fixture identity | preserved verbatim | preserved verbatim | yes |
| Handoff domain | `TRANSFERRED`/`NOT_TRANSFERRED`/`ERROR` | same closed domain | yes |
| `raw_octets` semantics | octets; Base64 at transport | octets; Base64 at transport | yes |
| `octet_length` | 43, equals decoded count | 43, equals decoded count | yes |
| Receiver-derived SHA-256 | `de2c1a21…678a2981` | `de2c1a21…678a2981` | yes |
| Receiver identity | preserved | preserved | yes |
| Implementation identity | preserved, distinct from receiver | preserved, distinct from receiver | yes |
| `source_commit` | field present and preserved | field present and preserved | yes (field; see §5 for the recorded value) |
| Adapter identity | preserved, distinct | preserved, distinct | yes |
| Environment | `environment_id`/`platform`/`runtime` | same three fields | yes |
| Authority isolation | no result field | no result field | yes |
| Deterministic transport | stable, lexicographic, compact, Base64 | stable, lexicographic, compact, Base64 | yes |

Implementation architecture differs substantially — class-bound provenance versus
a 13-argument free function, full assertion report versus first-error `Result`,
receiver-side versus adapter-side transport encoding. None of that was required
to match, and none of it produced a semantic divergence.

```text
Cross-receiver semantic compatibility with BC-02.1: PASS
```

## 7. Custodian reconciliation

Current authoritative construction state:

```text
BC-02.1 Common Receipt Schema   CONSTRUCTED
BC-02.2 RI-PY Receiver           CONSTRUCTED
BC-02.3 RI-RS Receiver           CONSTRUCTED
```

**Stale declaration recorded, not modified.** `BC-02.1-COMMON-RECEIPT-SCHEMA-v1.md`
§18 currently reads:

```text
BC-02.2 RI-PY               NOT STARTED
BC-02.3 RI-RS               NOT STARTED
```

Both statements are stale. BC-02.3 was constructed at `49e848a` and BC-02.2 at
`d943807`. BC-02.1 §18 is a gate snapshot taken at BC-02.1 construction time; it
was accurate when written. This record supersedes it as the current custodian
state. BC-02.1 was **not** modified in this task.

The related inconsistency previously reported — BC-02.3 §7 declaring
`BC-02.2 RI-PY Receiver CONSTRUCTED` before any RI-PY artifact existed — is now
resolved by fact rather than by edit: BC-02.2 exists as of `d943807`. BC-02.3 §7
was premature when written; it is now accurate.

## 8. Unresolved issues

| ID | Issue | Severity | Blocks gate |
|---|---|---|---|
| B-BLOCK-01 | RI-PY `source_commit` records `64bf959`, which does not contain the implementation. Correct value `d943807`. | blocking | **yes** |
| A-OBS-01 | Stored receipt files carry a trailing `0x0A` beyond the §12 serialization (both adapters). | observation | no |
| A-OBS-02 | RI-RS adapter R-VAL-002 additionally requires `fixture_id == "FIX-DIGEST-P01"`, exceeding BC-02.1 §15. | observation | no |
| D-OBS-01 | BC-02.1 §18 gate snapshot is stale for BC-02.2 and BC-02.3. | observation | no |
| C-OPEN-01 | The RI-PY P-01 execution declared before BC-02.2 existed remains unsubstantiated; see `evidence/RI-PY-P01-EVIDENCE-GAP-RECORD.md`. No RI-PY P-01 receipt exists. | open | no — RI-PY P-01 is simply not yet executed |

## 9. Execution gate

| # | Gate condition | State |
|---|---|---|
| 1 | RI-RS BC-02.1 serialization verified | **met** — §4, all ten requirements PASS |
| 2 | RI-PY source provenance verified | **verified and FAILING** — §5, B-BLOCK-01 |
| 3 | Cross-receiver semantic compatibility passes | **met** — §6 |
| 4 | No BC-02.1 change required | **met** |
| 5 | No BC-02.3 modification required | **met** |
| 6 | No unresolved authority-isolation issue | **met** — no result authority in either receiver |

Five of six met. Condition 2 fails.

```text
CONTROLLED P-01 HANDOFF: BLOCKED
```

Required to reach READY: correct the RI-PY `source_commit` in
`BC-02.2-CONSTRUCTION-EVIDENCE.md` §2 and `BC-02.2-RVAL-REPORT.txt` from
`64bf959b1d23fbd5433723476c611ab66d423953` to
`d943807c359af982fd573ec4ff690b7fa265dc42`, under separate authorization. No
other gate condition needs work.

A correct `source_commit` also has to be supplied to the RI-PY adapter at
handoff time — it is a required CLI argument, so the wrong value cannot be
inherited silently, but it can be re-entered incorrectly.

## 10. Explicit non-execution

- **P-01 = NOT EXECUTED.** No issued artifact was handed to any receiver. The
  stored RI-RS P-01 receipt was read as a file; it was not regenerated, and no
  RI-PY P-01 handoff was performed.
- **B-VAL-014 = NOT EXECUTED.**
- **§4.5 = NO RESULT.**
- **CONFORMANCE = NOT DETERMINED.**

No conformance result was created. BC-02.1 schema semantics, the BC-02.3
receiver implementation, the RI-RS adapter, the BC-02.2 artifacts, all fixtures
and the normative specification are unmodified by this audit. The temporary
serde probe in §3.1 was deleted and is not repository-resident.

# DQ-003 — Entry-Point Execution Attempt

**Fixture under test:** `DQ-003-AUDIT-CHAIN-001` (`conformance/DQ-003-AUDIT-CHAIN-001.json`, `status: GOLDEN-FIXTURE`)
**Mode:** READ-ONLY CONFORMANCE EXECUTION ATTEMPT
**Question answered:** *Can the EXISTING implementation, without semantic modification, produce the exact bytes/hashes required by DQ-003-AUDIT-CHAIN-001?*
**Question NOT answered:** *Can the implementation be adapted to produce them?*

**DQ-003 status after this execution: OPEN / CONFORMANCE GAP.** No remediation was performed. No fixture, specification, or implementation file was modified.

---

## A. Execution environment

### A.1 Commits

| Repository | Role | Branch | Commit SHA |
|---|---|---|---|
| `Aura-IDToken/aura-specification` | Golden Fixture (authority) | `dq/dq-003-audit-record-hash-domain` | `8de397b26250c8c0a767f86302baf8c99d31ff04` |
| `Aura-IDToken/aura-poc-a-core-v3.3` | RI-PY (implementation under test) | working checkout | `64bf959b1d23fbd5433723476c611ab66d423953` |
| `Aura-IDToken/aura-guard-v1.3` | RI-RS (implementation under test) | working checkout | `35082d7b4880dad780fb55a1a5f3ac0ef4322674` |

Both implementation checkouts were clean (`git status --short` empty) before and after execution. No source file in either implementation repository was created, edited, or deleted.

### A.2 Runtimes

| Component | Version |
|---|---|
| Python | 3.11.15 (main, Mar 3 2026, 09:26:23) [GCC 13.3.0] |
| `hashlib` / `json` | CPython 3.11 stdlib |
| rustc | 1.94.1 (e408947bf 2026-03-25) |
| cargo | 1.94.1 (29ea6fb6a 2026-03-24) |
| `sha2` | 0.10 (RI-RS declared dependency) |
| `serde_json_canonicalizer` | `=0.3.2` (RI-RS **dev**-dependency, conformance harness only) |
| Platform | Linux 6.18.44 x86_64 |

### A.3 Execution method

Three read-only harnesses were run from a scratchpad directory **outside** every repository. Each harness only *imports and calls* existing public entry points and prints what they return. No harness was committed to any repository, and no adapter, shim, or new hash function was added to `aura-poc-a-core-v3.3` or `aura-guard-v1.3`.

| # | Harness | Command | Exit code |
|---|---|---|---|
| 1 | Fixture self-verification | `python3 verify_fixture.py` | `0` |
| 2 | RI-PY entry-point execution | `python3 ripy_exec.py` / `python3 ripy_both.py` (with `sys.path.insert(0, "/home/user/aura-poc-a-core-v3.3")`) | `0` |
| 3 | RI-RS entry-point execution | `cargo run --quiet` in a scratchpad crate with `aura-guard = { path = "/home/user/aura-guard-v1.3" }` | `0` |

Exit code `0` means *the harness ran to completion*. It does **not** mean conformance. Conformance is decided solely by the byte comparisons in section D.

### A.4 Fixture authority check (precondition)

Before any implementation was executed, the Golden Fixture was independently re-derived from its own declared `generation_rules` and compared against its own frozen `expected` block and `canonical_preimages`.

```
FIXTURE SELF-VERIFICATION: PASS   (exit 0)
```

All six expected digests, all six canonical preimages, and the `record-001.previous_record_hash == record-000.audit_record_hash` linkage reproduced exactly. The fixture is internally coherent and is used unmodified as the sole authority for every comparison below.

### A.5 Fixture-selection note (observation, no change made)

Branch `dq/dq-003-audit-record-hash-domain` carries **three** files named `DQ-003-AUDIT-CHAIN-001.json`:

| Path | SHA-256 of file | Declared status | Records |
|---|---|---|---|
| `conformance/DQ-003-AUDIT-CHAIN-001.json` | `986564ccaa5e2c57dc27f645797bd16a7e62b191dda209f0344f15b2891b3d19` | **`GOLDEN-FIXTURE`** | `record-000`, `record-001` |
| `conformance/fixtures/DQ-003-AUDIT-CHAIN-001.json` | `7e01a25551910a886a1e43e48d1319f0975246ced05b7a299b40256358aa9af0` | `EXPERIMENTAL` | `dq003-record-0..2` |
| `fixtures/dq-003/DQ-003-AUDIT-CHAIN-001.json` | `eefa365b6be2a0cd6ffce996fc95e7d4404b54a182fa1b8f8be298944924f63d` | `EXPERIMENTAL_ONLY` (placeholder hashes) | 3 records |

Only `conformance/DQ-003-AUDIT-CHAIN-001.json` declares `GOLDEN-FIXTURE` and only it has the `record-000` / `record-001` structure required by DQ-003. It is therefore the authority used throughout this document. The other two files carry different `object_id`, `object_type`, `schema_version`, `event_type` and timestamp values and would yield different digests. **This fixture-identifier collision is reported, not resolved**; disambiguation is a Protocol Custodian decision.

---

## B. RI-PY execution — `aura-poc-a-core-v3.3` @ `64bf959`

### B.1 Surfaces inspected

| Path | Identified entry points |
|---|---|
| `compliance/certificate.py` | `AuraEventCertificate` (frozen dataclass), `.to_dict()`, `.fingerprint()` |
| `compliance/renderer.py` | `json.dumps(cert.to_dict(), indent=2, sort_keys=True)` — rendering only |
| `audit/merkle.py` | `sha256(data: str) -> str`, `MerkleTree`, `MerkleTree.get_proof`, `MerkleTree.create_etc`, `verify_proof`, `EventTrustCertificate.{to_dict,_signing_payload,sign,verify,verify_signature}` |
| `audit/verify.py` | `verify_proof`, `verify_etc` |
| `audit/signing.py` | `Signer` / `Verifier` (HMAC-SHA256) |
| `core/merkle.py` | `MerkleAttestor.generate_leaf(data: dict)`, `MerkleAttestor.generate_etc` |
| `core/` (evaluator, policy, embedding, normalizer) | ARI measurement surface — not an audit-record hashing surface |

### B.2 Symbol search — ENT-007 / APS-200 audit-record surface

Repository-wide `grep` over `*.py` (RI-PY @ `64bf959`):

| Symbol | Hits |
|---|---|
| `previous_record_hash` | **0 — ABSENT** |
| `audit_record_hash` | **0 — ABSENT** |
| `integrity_hash` | **0 — ABSENT** |
| `event_payload_hash` | **0 — ABSENT** |
| `chain_preimage` | **0 — ABSENT** |
| `verify_chain` | **0 — ABSENT** |
| `prev_hash` | **0 — ABSENT** |
| `sequence_number` | **0 — ABSENT** |
| `genesis` | **0 — ABSENT** |

Repository-wide search for `ENT-007`, `RFC 8785`, `rfc8785`, `JCS` outside `.git` returns hits **only** in three narrative review documents under `review/`; there is no RFC 8785 implementation and no RFC 8785 dependency (`pyproject.toml` declares no runtime dependencies).

### B.3 T1 — Can `AuraEventCertificate` represent an ENT-007 Audit Record?

```
AuraEventCertificate(**record-000.audit_record)
→ TypeError: AuraEventCertificate.__init__() got an unexpected keyword argument 'object_id'
```

The certificate dataclass accepts `agent_id, timestamp, ari_score, drift, status, merkle_root, leaf_hash`. The ENT-007 field set (`object_id, object_type, protocol_version, schema_version, created_at, event_type, sequence_number, previous_record_hash, event_payload_hash, audit_record_hash, integrity_hash`) is disjoint from it apart from an unrelated `timestamp`. **The ENT-007 Audit Record object is not representable in RI-PY.**

### B.4 T2 — `AuraEventCertificate.fingerprint()` in its own native domain

Executed with placeholder certificate values to observe the domain, not to claim conformance:

```
to_dict()      : {"agent_id": "fixture-subject", "ari": {"drift": 0.0, "score": 0.0, "status": "COMPLIANT"},
                  "audit": {"leaf_hash": "000…0", "merkle_root": "000…0"},
                  "schema_version": "1.0.0", "timestamp": "2026-01-01T00:00:00Z"}
fingerprint()  : 87d28c2b4d03047edb1218b7c739ecfdabf7cf0bff558bd65ebe0883bf9ef60a
```

Preimage is `json.dumps(to_dict(), sort_keys=True)` — Python default separators `", "` / `": "`, **not** RFC 8785 JCS, and no domain-separator octet. Certificate domain ≠ audit-record domain.

### B.5 T3–T5 — `core.merkle.MerkleAttestor.generate_leaf()` against the fixture

`generate_leaf` = `SHA-256(json.dumps(data, sort_keys=True).encode())` — sorted keys, **Python default separators**, no domain octet.

| Input | Actual | Expected | Match |
|---|---|---|---|
| `event_payload` (record-000) | `8d1c93a3fa2a40f3999500a3379dbb57a66a27aed0a4ef368b0a4db0b8f20f8b` | `a303ba4e3edd8659dfe653f2173e9671375972dce77d3f5d57bc42702b45ebde` | **NO** |
| `R_AR` (record-000) | `d05c0e72b5805f38d41b64ab6e2eb6f42db4075623ea48ce108340b7d01747a3` | `cbbc5104a848650d4b6cea175462b50779b40077c815cf3622875e8fc5689e79` | **NO** |
| `R_I` (record-000) | `0be5890ba15ebacf8c64ee08ffe80d3064935f1ed3823109585686b05f1c093b` | `70526acd3dd66f435a4051e7a6c4d1f892fd170be8ea4d00f40347a01febe57a` | **NO** |
| `event_payload` (record-001) | `47e037e23335e8124b081a284adeca74d7f3c01d9c2bd972bb0b83f824346feb` | `fabc602b7e214526b7cd2175cc0163ff6ad51268776972bd9c326ad15f2224a1` | **NO** |
| `R_AR` (record-001) | `d3c0e43ca9a42385d978f6cfa7ed11e296b62d97927e7ee731f9cd7c5708825b` | `08704c4ea7d361e99592bed22e52f60a0c6c9c80f158ec8c126fc56015268902` | **NO** |
| `R_I` (record-001) | `8c4728958a73c1ffbeb0a850071580f97522111b3b50686a456005c67bf85afe` | `748de582b5f801cc74340f5daa8c9e1d3cef272902bcb46c3d2b4624da9c6591` | **NO** |

### B.6 T6 — `audit.merkle.sha256()` primitive fed the **fixture's own** JCS strings

`audit.merkle.sha256(data: str)` is a bare `SHA-256` over `data.encode('utf-8')`. The JCS inputs below were taken **from the fixture**, because RI-PY cannot produce them.

| Call | Actual | Expected | Match |
|---|---|---|---|
| `sha256(event_payload_jcs)` r000 | `a303ba4e…45ebde` | `a303ba4e…45ebde` | **YES** |
| `sha256(event_payload_jcs)` r001 | `fabc602b…2224a1` | `fabc602b…2224a1` | **YES** |
| `sha256(audit_record_jcs)` r000 — no `0x02` | `0da60d9b13bb95245470935e123aa5b86d26b652dda44ad9957a9342acce4480` | `cbbc5104…689e79` | **NO** |
| `sha256(audit_record_jcs)` r001 — no `0x02` | `e612d3f18b6203e4c6f43ae4648613761cc81ec1840cb780b57bc4b732dafed1` | `08704c4e…268902` | **NO** |
| `sha256(integrity_jcs)` r000 | `70526acd…be57a` | `70526acd…be57a` | **YES** |
| `sha256(integrity_jcs)` r001 | `748de582…9c6591` | `748de582…9c6591` | **YES** |

**Interpretation.** The SHA-256 primitive is exact. The three `YES` rows prove only that *if* RI-PY had an RFC 8785 canonicalizer, its hash primitive would be correct for the two un-prefixed domains. They do **not** show RI-PY producing the values, because the canonical bytes were supplied by the fixture. The two `NO` rows isolate the `0x02` domain separator, which has no source in RI-PY at all.

### B.7 RI-PY missing surfaces

1. **RFC 8785 JCS canonicalization — ABSENT.** No `canonicalize`/`canonical_bytes` function exists (`grep "def canonical|def to_canonical|canonicalize"` → 0 hits) and no RFC 8785 dependency is declared. A compact-separator idiom (`json.dumps(..., sort_keys=True, separators=(",", ":"))`) appears **inline** in `audit/merkle.py:85` (`EventTrustCertificate._signing_payload`, hard-wired to exactly three fields), in `scripts/generate_determinism_report.py:101`, and in three test files. None of these is a general canonicalizer over an arbitrary object, and none is claimed or tested as RFC 8785 (number formatting, `\u` escaping and UTF-16 code-unit key ordering are unaddressed).
2. **`0x02` audit-record domain separator — ABSENT.** No domain-separation octet of any kind exists in RI-PY.
3. **ENT-007 Audit Record object — ABSENT.**
4. **Integrity object / integrity preimage — ABSENT.**
5. **Sequential audit chain (`previous_record_hash`, genesis, chain verification) — ABSENT.** RI-PY's audit model is a Merkle tree plus certificate fingerprint, not a hash chain.

No failure or exception occurred other than the deliberate `TypeError` in B.3.

---

## C. RI-RS execution — `aura-guard-v1.3` @ `35082d7`

### C.1 Surfaces inspected

| Path | Identified entry points |
|---|---|
| `src/chain.rs` | `chain_preimage(...)`, `compute_chain_hash(...)`, `recompute_for_entry(&AuditEntry)`, `verify_chain(&[AuditEntry])`, `const SEP = "\|"` |
| `src/crypto.rs` | `sha256_hex(&str)`, `sha256_bytes_hex(&[u8])`, `genesis_hash()`, `parse_pubkey_hex`, `verify_signature` |
| `src/merkle.rs` | `leaf_hash` (`SHA-256(0x00 \|\| data)`), `node_hash` (`SHA-256(0x01 \|\| l \|\| r)`), `empty_root` |
| `src/models.rs` | `AuditEntry` (Serialize/Deserialize), `Violation` |
| `src/segment.rs` | `SegmentManifest::segment_chain_preimage`, `segment_genesis_hash` |
| `conformance/canonical/jcs.rs` | `canonical_bytes(&serde_json::Value) -> Result<Vec<u8>, serde_json::Error>` — RFC 8785 via `serde_json_canonicalizer` **=0.3.2** |
| `tests/hash_domains.rs`, `tests/byte_representations.rs`, `tests/golden.rs`, `src/chain.rs` `mod tests` | chain verification / hash-domain observation tests |

### C.2 Symbol search — ENT-007 / APS-200 audit-record surface

Repository-wide `grep` over `*.rs`/`*.toml` (excluding `target/`) for `previous_record_hash`, `audit_record_hash`, `integrity_hash`, `event_payload_hash`, `ENT-007`, `object_id`: the only hits are two **disclaimers** in the test suite —

- `tests/hash_domains.rs:697` — *"No relationship is claimed between these constructions and APS-200 integrity_hash, event_payload_hash or previous_record_hash."*
- `tests/regression.rs:35` — same disclaimer form.

There is **no implementation** of any APS-200 audit-record hash in RI-RS. Domain octets present in the repository are `0x00` and `0x01` (RFC 6962 Merkle, `src/merkle.rs:31,40`). **`0x02` is not used as a hash-domain separator anywhere.**

### C.3 R1 — Can `models::AuditEntry` represent an ENT-007 Audit Record?

```
serde_json::from_value::<AuditEntry>(record-000.audit_record)
→ ERROR: missing field `schema`
```

| `AuditEntry` fields | ENT-007 fields |
|---|---|
| `schema, seq, audit_id, request_id?, timestamp, decision, policy_set, policy_hash, context, input_hash, shadow_hash, violations, prev_hash, chain_hash` | `object_id, object_type, protocol_version, schema_version, created_at, event_type, sequence_number, previous_record_hash, event_payload_hash, audit_record_hash, integrity_hash` |

The field sets are disjoint. **The ENT-007 Audit Record object is not representable in RI-RS.**

### C.4 R2 — `crypto::genesis_hash()`

```
expected (fixture) : 0000000000000000000000000000000000000000000000000000000000000000
actual   (RI-RS)   : b93b4ade8c758fa0086b464ac445fe6109681da57a99760eeb7f7bce3623562d
match              : NO
```

RI-RS genesis is `SHA-256("AURA-GUARD-GENESIS-v1.3")`; the fixture genesis is 64 zero nibbles. Different genesis anchors.

### C.5 R3 — `chain::chain_preimage()` / `compute_chain_hash()` (native domain, recorded exactly)

The existing preimage is, verbatim:

```text
prev_hash | decision | policy_set | policy_hash | context | input_hash | shadow_hash | seq | timestamp
```

joined with `SEP = "|"`, hashed as `SHA-256(utf8(joined))`. Six of the nine slots (`decision`, `policy_set`, `policy_hash`, `context`, `input_hash`, `shadow_hash`) have **no ENT-007 source field**; they were supplied as empty strings purely to make the call executable.

```
preimage (str) : "0000000000000000000000000000000000000000000000000000000000000000|||||||0|2026-01-01T00:00:00Z"
preimage (hex) : 3030303030303030303030303030303030303030303030303030303030303030
                 3030303030303030303030303030303030303030303030303030303030303030
                 7c7c7c7c7c7c7c307c323032362d30312d30315430303a30303a30305a
compute_chain_hash → d6cc2e73b5f052660163cf882a36632152e2b8c633c58e780dff48cd8bad4c80
expected audit_record_hash → cbbc5104a848650d4b6cea175462b50779b40077c815cf3622875e8fc5689e79
match: NO
```

This is recorded as-is and is **not** translated into the APS-200 domain.

### C.6 R4 — `recompute_for_entry()` / `verify_chain()`

```
recompute_for_entry(e0) → 3ea12e5ded57a48ed46311f8c75b0b0133cc37534e4e2edd32bfdb1f7be0d030
expected audit_record_hash → cbbc5104a848650d4b6cea175462b50779b40077c815cf3622875e8fc5689e79
match: NO

verify_chain([e0, e1])
→ Err(CHAIN BREAK DETECTED at entry #0:
      expected prev_hash=b93b4ade8c758fa0086b464ac445fe6109681da57a99760eeb7f7bce3623562d,
      got 0000000000000000000000000000000000000000000000000000000000000000)
```

`verify_chain` **rejects** the fixture chain at the genesis check, before any hash-domain question is reached. Exit code of the harness: `0` (the rejection is a returned `Err`, not a process failure).

### C.7 R5 — `crypto::sha256_hex()` / `sha256_bytes_hex()` / `merkle::leaf_hash()` on fixture-supplied JCS

| Call (record-000 / record-001) | Match |
|---|---|
| `sha256_hex(JCS(event_payload))` vs `event_payload_hash` | **YES / YES** |
| `sha256_hex(JCS(R_AR))` — no `0x02` — vs `audit_record_hash` | **NO / NO** (`0da60d9b…` / `e612d3f1…`) |
| `sha256_bytes_hex(0x02 \|\| JCS(R_AR))` vs `audit_record_hash` | **YES / YES** |
| `sha256_hex(JCS(R_I))` vs `integrity_hash` | **YES / YES** |
| `merkle::leaf_hash(JCS(R_AR))` — `0x00` domain — vs `audit_record_hash` | **NO / NO** (`26574f39…` / `8a4aca93…`) |

`sha256_bytes_hex` accepts arbitrary bytes, so the `0x02` prefix is expressible as caller-side byte concatenation. The concatenation itself exists nowhere in RI-RS; it was performed by the harness.

### C.8 R6 — `conformance/canonical/jcs.rs::canonical_bytes()` against the fixture

`canonical_bytes` is **not exported by the `aura_guard` library**; it is a module of the `canonical_001` test target only. The harness included the file verbatim by path (`#[path = ".../conformance/canonical/jcs.rs"] mod ri_rs_jcs;`), unmodified, to observe its output.

| Value | record-000 | record-001 |
|---|---|---|
| `canonical_bytes(event_payload)` vs fixture `event_payload_jcs` | **byte-identical** | **byte-identical** |
| `SHA-256(that)` vs `event_payload_hash` | **YES** | **YES** |
| `canonical_bytes(R_AR)` vs fixture `audit_record_jcs` | **byte-identical** | **byte-identical** |
| `SHA-256(0x02 \|\| that)` vs `audit_record_hash` | **YES** | **YES** |
| `canonical_bytes(R_I)` vs fixture `integrity_jcs` | **byte-identical** | **byte-identical** |
| `SHA-256(that)` vs `integrity_hash` | **YES** | **YES** |

**This is the decisive RI-RS result.** Every cryptographic and serialization primitive the fixture requires already exists in `aura-guard-v1.3` and reproduces the frozen values byte-for-byte. What is missing is the *composition* and the *ENT-007 object*, not the mathematics.

### C.9 RI-RS missing surfaces

1. **ENT-007 Audit Record type — ABSENT.**
2. **Field-exclusion rules** (`R_AR` excludes `audit_record_hash` + `integrity_hash`; `R_I` excludes `integrity_hash` only) — **ABSENT**; performed by the harness.
3. **`0x02` domain-separator composition — ABSENT** (`0x00`/`0x01` exist for Merkle; `0x02` does not).
4. **`event_payload_hash` / `audit_record_hash` / `integrity_hash` named entry points — ABSENT.**
5. **JCS is not reachable from the library** — `conformance/canonical/jcs.rs` is documented as *"not wired into the production runtime… not reachable from `src/`"* and `serde_json_canonicalizer` is a **`[dev-dependencies]`** entry only.
6. **Genesis anchor and chain domain differ** from APS-200; `verify_chain` rejects the fixture at entry #0.

---

## D. Byte-level comparison — expected vs actual

Every expected value below is read verbatim from the Golden Fixture and was independently re-derived in A.4.

### D.1 record-000

**Canonical Event Payload**

```
expected (JCS, UTF-8): {"action":"ALLOW","resource":"fixture-resource","subject":"fixture-subject"}
expected hex         : 7b22616374696f6e223a22414c4c4f57222c227265736f75726365223a22666978747572652d7265736f75726365222c227375626a656374223a22666978747572652d7375626a656374227d

RI-PY actual         : {"action": "ALLOW", "resource": "fixture-resource", "subject": "fixture-subject"}
RI-PY actual hex     : 7b22616374696f6e223a2022414c4c4f57222c20227265736f75726365223a2022666978747572652d7265736f75726365222c20227375626a656374223a2022666978747572652d7375626a656374227d
byte match           : NO   (RI-PY emits ", " and ": "; JCS requires "," and ":")

RI-RS actual         : {"action":"ALLOW","resource":"fixture-resource","subject":"fixture-subject"}
byte match           : YES  (conformance/canonical/jcs.rs — test target, not library)
```

Field ordering (`action` < `resource` < `subject`), UTF-8 encoding, and included/excluded fields agree in both implementations; **only the separators differ in RI-PY**, and that alone changes the digest.

**`event_payload_hash`**

```
expected: a303ba4e3edd8659dfe653f2173e9671375972dce77d3f5d57bc42702b45ebde
RI-PY   : 8d1c93a3fa2a40f3999500a3379dbb57a66a27aed0a4ef368b0a4db0b8f20f8b   match: NO
RI-RS   : a303ba4e3edd8659dfe653f2173e9671375972dce77d3f5d57bc42702b45ebde   match: YES (jcs.rs + sha256_bytes_hex, composed by the harness)
```

**Audit Record preimage** (`0x02 || JCS(R_AR)`)

```
expected hex: 027b22637265617465645f6174223a22323032362d30312d30315430303a30303a30305a222c226576656e745f7061796c6f61645f68617368223a2261333033626134653365646438363539646665363533663231373365393637313337353937326463653737643366356435376263343237303262343565626465222c226576656e745f74797065223a2241554449545f4445434953494f4e222c226f626a6563745f6964223a2230303030303030302d303030302d343030302d383030302d303030303030303030303030222c226f626a6563745f74797065223a2241756469745265636f7264222c2270726576696f75735f7265636f72645f68617368223a2230303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030222c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30222c2273657175656e63655f6e756d626572223a307d

RI-PY actual hex (json.dumps sort_keys, default separators, NO domain octet):
              7b22637265617465645f6174223a2022323032362d30312d30315430303a30303a30305a222c20226576656e745f7061796c6f61645f68617368223a202261333033626134653365646438363539646665363533663231373365393637313337353937326463653737643366356435376263343237303262343565626465222c20226576656e745f74797065223a202241554449545f4445434953494f4e222c20226f626a6563745f6964223a202230303030303030302d303030302d343030302d383030302d303030303030303030303030222c20226f626a6563745f74797065223a202241756469745265636f7264222c202270726576696f75735f7265636f72645f68617368223a202230303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030222c202270726f746f636f6c5f76657273696f6e223a2022312e30222c2022736368656d615f76657273696f6e223a2022312e30222c202273657175656e63655f6e756d626572223a20307d
byte match  : NO   (missing leading 02; ", "/": " separators)

RI-RS actual (native chain domain, chain_preimage):
              "0000…0000|||||||0|2026-01-01T00:00:00Z"
          hex 30303030…30307c7c7c7c7c7c7c307c323032362d30312d30315430303a30303a30305a
byte match  : NO   (different field set, "|" separator, no JSON, no domain octet)

RI-RS actual (jcs.rs canonical_bytes(R_AR), harness-prefixed with 0x02):
byte match  : YES
```

**`audit_record_hash`**

```
expected               : cbbc5104a848650d4b6cea175462b50779b40077c815cf3622875e8fc5689e79
RI-PY generate_leaf    : d05c0e72b5805f38d41b64ab6e2eb6f42db4075623ea48ce108340b7d01747a3   match: NO
RI-RS compute_chain_hash: d6cc2e73b5f052660163cf882a36632152e2b8c633c58e780dff48cd8bad4c80   match: NO
RI-RS recompute_for_entry: 3ea12e5ded57a48ed46311f8c75b0b0133cc37534e4e2edd32bfdb1f7be0d030  match: NO
RI-RS merkle::leaf_hash (0x00): 26574f39b270b3968c9192947790a59c594e2fca8f4f230df2025acc34e9d00c match: NO
RI-RS jcs.rs + 0x02 + sha256_bytes_hex: cbbc5104a848650d4b6cea175462b50779b40077c815cf3622875e8fc5689e79 match: YES (harness-composed)
no-domain control SHA-256(JCS(R_AR)): 0da60d9b13bb95245470935e123aa5b86d26b652dda44ad9957a9342acce4480 match: NO
```

The no-domain control proves the `0x02` octet is load-bearing: omitting it changes the digest completely. **`chain_hash` is not `audit_record_hash`.**

**Integrity preimage and `integrity_hash`**

```
expected preimage: {"audit_record_hash":"cbbc5104…689e79","created_at":"2026-01-01T00:00:00Z","event_payload_hash":"a303ba4e…45ebde","event_type":"AUDIT_DECISION","object_id":"00000000-0000-4000-8000-000000000000","object_type":"AuditRecord","previous_record_hash":"0000…0000","protocol_version":"1.0","schema_version":"1.0","sequence_number":0}
expected hash    : 70526acd3dd66f435a4051e7a6c4d1f892fd170be8ea4d00f40347a01febe57a

RI-PY generate_leaf(R_I): 0be5890ba15ebacf8c64ee08ffe80d3064935f1ed3823109585686b05f1c093b   match: NO
RI-PY sha256(fixture integrity_jcs): 70526acd…be57a   match: YES (canonical bytes supplied by fixture, not by RI-PY)
RI-RS jcs.rs canonical_bytes(R_I): byte-identical to expected preimage   match: YES
RI-RS sha256_hex(that): 70526acd3dd66f435a4051e7a6c4d1f892fd170be8ea4d00f40347a01febe57a   match: YES (harness-composed)
```

**`previous_record_hash`**

```
expected (genesis): 0000000000000000000000000000000000000000000000000000000000000000
RI-PY             : ABSENT — no such field or concept
RI-RS genesis_hash(): b93b4ade8c758fa0086b464ac445fe6109681da57a99760eeb7f7bce3623562d   match: NO
```

### D.2 record-001

```
Canonical Event Payload
  expected : {"action":"DENY","resource":"fixture-resource","subject":"fixture-subject"}
  RI-PY    : {"action": "DENY", "resource": "fixture-resource", "subject": "fixture-subject"}   byte match: NO
  RI-RS    : byte-identical                                                                     byte match: YES

event_payload_hash
  expected : fabc602b7e214526b7cd2175cc0163ff6ad51268776972bd9c326ad15f2224a1
  RI-PY    : 47e037e23335e8124b081a284adeca74d7f3c01d9c2bd972bb0b83f824346feb   NO
  RI-RS    : fabc602b7e214526b7cd2175cc0163ff6ad51268776972bd9c326ad15f2224a1   YES (harness-composed)

audit_record_hash
  expected : 08704c4ea7d361e99592bed22e52f60a0c6c9c80f158ec8c126fc56015268902
  RI-PY    : d3c0e43ca9a42385d978f6cfa7ed11e296b62d97927e7ee731f9cd7c5708825b   NO
  RI-RS 0x02||JCS : 08704c4ea7d361e99592bed22e52f60a0c6c9c80f158ec8c126fc56015268902   YES (harness-composed)
  RI-RS no-domain control : e612d3f18b6203e4c6f43ae4648613761cc81ec1840cb780b57bc4b732dafed1   NO
  RI-RS leaf_hash (0x00)  : 8a4aca93895c56dbb0be9cd05d12cf22e67c4087a1b596bd598ff5a03bc70eef   NO

integrity_hash
  expected : 748de582b5f801cc74340f5daa8c9e1d3cef272902bcb46c3d2b4624da9c6591
  RI-PY    : 8c4728958a73c1ffbeb0a850071580f97522111b3b50686a456005c67bf85afe   NO
  RI-RS    : 748de582b5f801cc74340f5daa8c9e1d3cef272902bcb46c3d2b4624da9c6591   YES (harness-composed)

previous_record_hash (MUST equal record-000.audit_record_hash)
  expected : cbbc5104a848650d4b6cea175462b50779b40077c815cf3622875e8fc5689e79
  RI-PY    : ABSENT
  RI-RS    : linkage field exists (AuditEntry.prev_hash) but targets chain_hash;
             verify_chain rejected the fixture at entry #0 before reaching this link.
```

### D.3 Comparison-dimension summary

| Dimension | RI-PY | RI-RS |
|---|---|---|
| Raw canonical bytes | differ (separators) | identical (jcs.rs) |
| Hexadecimal representation | differs | identical |
| SHA-256 digest | differs | identical when composed |
| Field ordering | lexicographic — agrees | lexicographic — agrees |
| Separators | `", "` / `": "` — **differs** | `","` / `":"` — agrees |
| UTF-8 encoding | agrees | agrees |
| Domain prefix (`0x02`) | **absent** | **absent** (`0x00`/`0x01` only); expressible via `sha256_bytes_hex` |
| Included fields | n/a — no ENT-007 object | n/a — no ENT-007 object |
| Excluded fields (`R_AR`, `R_I` rules) | **absent** | **absent** |

---

## E. Result matrix

| Requirement | RI-PY entry point | RI-RS entry point | Expected | Actual | Byte match | Classification |
|-------------|-------------------|-------------------|----------|--------|------------|----------------|
| Event Payload | none (`AuraEventCertificate(**record)` → TypeError) | none (`from_value::<AuditEntry>` → missing field `schema`); `serde_json::Value` accepted generically by `jcs.rs` | ENT-007 Event Payload object | RI-PY: not representable · RI-RS: untyped `Value` only | n/a | RI-PY **ABSENT** · RI-RS **PARTIAL** |
| Canonical Payload | `core.merkle.MerkleAttestor.generate_leaf` (`json.dumps(sort_keys=True)`) | `conformance/canonical/jcs.rs::canonical_bytes` | `{"action":"ALLOW",…}` (JCS) | RI-PY: `{"action": "ALLOW", …}` · RI-RS: byte-identical | RI-PY **NO** · RI-RS **YES** | RI-PY **ANALOGOUS** · RI-RS **EXACT** (test target only) |
| event_payload_hash | `audit.merkle.sha256` (primitive only) | `crypto::sha256_bytes_hex` + `jcs.rs` | `a303ba4e…` / `fabc602b…` | RI-PY `8d1c93a3…` / `47e037e2…` · RI-RS `a303ba4e…` / `fabc602b…` | RI-PY **NO** · RI-RS **YES** (harness-composed) | RI-PY **PARTIAL** · RI-RS **PARTIAL** (primitives EXACT, composition absent) |
| Audit Record | none | none (`models::AuditEntry` field set disjoint) | ENT-007 object, 11 fields | not representable in either | **NO** | **ABSENT** (both) |
| Audit Record Preimage | none | `chain::chain_preimage` (pipe-joined 9 fields) | `0x02 \|\| JCS(R_AR)` | RI-PY: sorted JSON, no octet · RI-RS: `"0000…\|\|\|\|\|\|\|0\|2026-01-01T00:00:00Z"` | **NO** (both) | RI-PY **ABSENT** · RI-RS **PARTIAL** (JCS exact; `0x02` + exclusion rules absent) |
| audit_record_hash | none | `chain::compute_chain_hash` / `recompute_for_entry` | `cbbc5104…` / `08704c4e…` | RI-PY `d05c0e72…` · RI-RS `d6cc2e73…` / `3ea12e5d…` | **NO** (both) | RI-PY **ABSENT** · RI-RS **ANALOGOUS** |
| Integrity object | none | none | ENT-007 object incl. `audit_record_hash`, excl. `integrity_hash` | not representable in either | **NO** | **ABSENT** (both) |
| Integrity preimage | none | `jcs.rs::canonical_bytes` (no exclusion rule) | `JCS(R_I)` | RI-PY: n/a · RI-RS: byte-identical when R_I is built by caller | RI-PY **NO** · RI-RS **YES** | RI-PY **ABSENT** · RI-RS **PARTIAL** |
| integrity_hash | `audit.merkle.sha256` (primitive only) | `crypto::sha256_hex` + `jcs.rs` | `70526acd…` / `748de582…` | RI-PY `0be5890b…` / `8c472895…` (own serializer) · RI-RS `70526acd…` / `748de582…` | RI-PY **NO** · RI-RS **YES** (harness-composed) | RI-PY **PARTIAL** · RI-RS **PARTIAL** |
| previous_record_hash | none (0 grep hits) | `models::AuditEntry.prev_hash` + `chain::verify_chain` | `0000…0000` / `cbbc5104…` | RI-PY: absent · RI-RS: links predecessor `chain_hash` | **NO** (both) | RI-PY **ABSENT** · RI-RS **ANALOGOUS** |
| Genesis | none | `crypto::genesis_hash()` | `0000000000000000000000000000000000000000000000000000000000000000` | RI-PY: absent · RI-RS: `b93b4ade8c758fa0086b464ac445fe6109681da57a99760eeb7f7bce3623562d` | **NO** (both) | RI-PY **ABSENT** · RI-RS **ANALOGOUS** |
| Re-computation | `AuraEventCertificate.fingerprint()` | `chain::recompute_for_entry()` | recompute `audit_record_hash` from record | RI-PY: certificate fingerprint `87d28c2b…` · RI-RS: `3ea12e5d…` | **NO** (both) | **ANALOGOUS** (both) |
| Verification | `audit.verify.verify_proof` / `verify_etc` (Merkle) | `chain::verify_chain()` | chain accepted, links validated | RI-PY: Merkle-proof model, no chain · RI-RS: `Err(CHAIN BREAK at entry #0: expected b93b4ade…, got 0000…)` | **NO** (both) | **ANALOGOUS** (both) |

---

## F. Conformance conclusion

### RI-PY (`aura-poc-a-core-v3.3` @ `64bf959`) — **CONFORMANCE GAP**

A thin adapter is **not** technically possible. RI-PY is missing an entire normative layer, not a naming layer:

- **RFC 8785 JCS canonicalization does not exist** in the repository — no function, no dependency, no test. Its only deterministic serializer (`json.dumps(..., sort_keys=True)`) emits different bytes than JCS for *every* value in the fixture. Introducing RFC 8785 is new normative serialization semantics, which exceeds an adapter and is explicitly out of scope here.
- **The `0x02` audit-record domain separator does not exist** in any form.
- **The ENT-007 Audit Record and Integrity objects are not representable** — the certificate dataclass rejects `object_id` outright.
- **There is no sequential audit chain at all** — no `previous_record_hash`, no genesis anchor, no chain verification. RI-PY's audit model is Merkle-tree evidence plus a certificate fingerprint, an architecturally different construct.

Only the SHA-256 primitive (`audit.merkle.sha256`) is exact, and it is exact only when it is handed canonical bytes that RI-PY itself cannot produce.

### RI-RS (`aura-guard-v1.3` @ `35082d7`) — **THIN ADAPTER POSSIBLE** (technically), with a governance precondition

Every byte the fixture requires was reproduced from primitives that already exist in the repository, unmodified:

- `conformance/canonical/jcs.rs::canonical_bytes` produced the fixture's `event_payload_jcs`, `audit_record_jcs`, and `integrity_jcs` **byte-for-byte, for both records**.
- `crypto::sha256_bytes_hex` / `sha256_hex` reproduced all six frozen digests once those bytes were supplied, including the `0x02`-prefixed audit-record domain.

No new cryptographic or serialization semantics would be required. What is missing is composition and typing: an ENT-007 record type, the two field-exclusion rules, the `0x02` prefix concatenation, and three named entry points.

Three constraints qualify this conclusion and are **not** resolved here:

1. `jcs.rs` is documented in-tree as *"not wired into the production runtime… not reachable from `src/`"*, and `serde_json_canonicalizer` is a **`[dev-dependencies]`** entry. Making it reachable promotes a conformance-only surface into the protocol path — a governance decision, not an adapter.
2. RI-RS's existing chain domain (`chain_hash` over the pipe-joined 9-field preimage) and genesis anchor (`SHA-256("AURA-GUARD-GENESIS-v1.3")`) are **not** the APS-200 domain. An adapter must sit beside them, not reinterpret them.
3. The in-tree disclaimers at `tests/hash_domains.rs:697` and `tests/regression.rs:35` explicitly deny any relationship between current constructions and APS-200 `integrity_hash` / `event_payload_hash` / `previous_record_hash`. Nothing in this execution contradicts those disclaimers.

### DQ-003 decision

Not every required field and hash domain matches byte-for-byte through an existing entry point. Applying the DQ-003 decision rule:

> **DQ-003 status = OPEN / CONFORMANCE GAP**

DQ-003 is **not** closed by this document, and no remediation was performed.

---

## G. Semantic gap summary

### EXACT

| Surface | Implementation | Note |
|---|---|---|
| RFC 8785 JCS canonical bytes | RI-RS `conformance/canonical/jcs.rs::canonical_bytes` | byte-identical to all six fixture preimages; reachable only from the `canonical_001` test target |
| SHA-256 over UTF-8 string | RI-RS `crypto::sha256_hex`, RI-PY `audit.merkle.sha256` | correct primitive; produces correct digests only from externally-supplied canonical bytes |
| SHA-256 over arbitrary bytes | RI-RS `crypto::sha256_bytes_hex` | the only surface in either implementation able to express a `0x02` domain prefix |

### ANALOGOUS

| Surface | Implementation | Why not EXACT |
|---|---|---|
| `compute_chain_hash` / `chain_preimage` | RI-RS `src/chain.rs` | `SHA-256(prev\|decision\|policy_set\|policy_hash\|context\|input_hash\|shadow_hash\|seq\|timestamp)`; different field set, separator, encoding, no domain octet |
| `recompute_for_entry` | RI-RS `src/chain.rs` | recomputes the chain digest, not `audit_record_hash` |
| `verify_chain` | RI-RS `src/chain.rs` | correct chain *shape* (genesis → linkage → recompute), wrong domain and wrong genesis anchor; rejected the fixture at entry #0 |
| `genesis_hash()` | RI-RS `src/crypto.rs` | `b93b4ade…` ≠ fixture `0000…0000` |
| `AuditEntry.prev_hash` | RI-RS `src/models.rs` | links predecessor `chain_hash`, not `audit_record_hash` |
| `MerkleAttestor.generate_leaf` / `json.dumps(sort_keys=True)` | RI-PY `core/merkle.py` | deterministic but non-JCS byte contract |
| `AuraEventCertificate.fingerprint()` | RI-PY `compliance/certificate.py` | certificate domain, disjoint field set |
| `verify_proof` / `verify_etc` / `MerkleTree` | RI-PY `audit/` | Merkle-inclusion evidence model, not a sequential record chain |
| `merkle::leaf_hash` / `node_hash` | RI-RS `src/merkle.rs` | RFC 6962 `0x00`/`0x01` domains — correct *technique*, wrong domain for ENT-007 |

### PARTIAL

| Requirement | Present | Missing |
|---|---|---|
| `event_payload_hash` (RI-RS) | JCS bytes exact, SHA-256 exact | no named entry point composing them; no typed Event Payload |
| `integrity_hash` (RI-RS) | JCS bytes exact, SHA-256 exact | no `R_I` construction (exclude `integrity_hash`, include `audit_record_hash`); no named entry point |
| Audit Record preimage (RI-RS) | JCS bytes exact | `0x02` prefix not composed anywhere; `R_AR` exclusion rule absent |
| Event Payload (RI-RS) | untyped `serde_json::Value` accepted | no ENT-007 Event Payload type; duplicate-member rejection and top-level-object requirement not enforced on this path |
| `event_payload_hash` (RI-PY) | SHA-256 primitive exact | RFC 8785 canonicalization entirely absent |
| `integrity_hash` (RI-PY) | SHA-256 primitive exact | RFC 8785 canonicalization and `R_I` construction absent |

### ABSENT

| Requirement | RI-PY | RI-RS |
|---|---|---|
| ENT-007 Audit Record object | ABSENT | ABSENT |
| Integrity object | ABSENT | ABSENT |
| `0x02` domain separator | ABSENT | ABSENT (as a composed construction) |
| `audit_record_hash` entry point | ABSENT | ABSENT (only `chain_hash`) |
| `integrity_hash` entry point | ABSENT | ABSENT |
| `event_payload_hash` entry point | ABSENT | ABSENT |
| RFC 8785 JCS | ABSENT (no function, no dependency) | present but out-of-library (dev-dependency, test target) |
| `previous_record_hash` field | ABSENT | ABSENT (only `prev_hash` over `chain_hash`) |
| APS-200 genesis anchor | ABSENT | ABSENT (different anchor) |
| ENT-007 chain verification | ABSENT | ABSENT (different domain) |

---

## H. Scope statement

- The Golden Fixture is the authority. It was read, self-verified, and **not modified, regenerated, or reinterpreted**.
- `main`, RI-PY, RI-RS, APS-200 and all fixtures are **unmodified**. The only file added by this task is this document.
- **No adapter was created.** No `adapter.py`, `adapter.rs`, `audit_record_hash()`, `integrity_hash()` or `event_payload_hash()` was added to any repository. All composition shown above happened in throwaway scratchpad harnesses that call existing entry points and were never committed.
- No missing field or hash was invented. Where the fixture supplied canonical bytes that an implementation could not produce, that is stated explicitly at every occurrence.
- DQ-003 remains **OPEN**. Whether to build the RI-RS thin adapter, and whether to promote `serde_json_canonicalizer` out of `[dev-dependencies]`, are decisions for the Protocol Custodian, not consequences of this execution.

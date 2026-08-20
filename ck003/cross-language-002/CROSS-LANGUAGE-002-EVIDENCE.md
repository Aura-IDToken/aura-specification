# CROSS-LANGUAGE-002 — Merkle Node / Root / Proof Conformance

**Workstream:** CK-003 Remediation  
**Depends on:** DQ-006 CLOSED, DQ-002 proposed hash-domain decision  
**Branch:** `ck003/cross-language-002`  
**Status:** OPEN — execution gate not yet PASS

> **Reconciled 2026-08-20.** The dependency line above records `DQ-006 CLOSED`, and that is
> now the status of record — see
> [`closures/DQ-006_CLOSURE_PACKAGE.md`](../../closures/DQ-006_CLOSURE_PACKAGE.md).
> This gate's own status is unchanged and remains **OPEN**.
>
> **Identifier collision.** The reference-implementation repositories also use the name
> `CROSS-LANGUAGE-002` for the CANONICAL-002 canonicalization equality gate, which is a
> different gate over a different contract and which is PASS. To prevent that from being
> read as a pass for *this* Merkle gate, the specification refers to the canonicalization
> gate as `CROSS-LANGUAGE-CANONICAL-002`. Renaming the RI-side identifier is carried as
> item C-3 in the DQ-006 closure package §13.

## 1. Objective

Establish byte-level cross-language conformance for the DQ-002 RFC 6962 Merkle contract beyond the DQ-006 canonicalization/leaf boundary.

The gate MUST independently demonstrate, for the same normative fixture:

1. identical leaf digests;
2. identical interior-node digest;
3. identical Merkle root;
4. valid inclusion proof for every leaf;
5. rejection of controlled mutations;
6. provenance of the actual RI-PY and RI-RS executions.

## 2. Normative contract under test

For canonical/raw leaf bytes `B`:

`leaf(B) = SHA-256(0x00 || B)`

For two child digests `L` and `R`:

`node(L,R) = SHA-256(0x01 || L || R)`

where `L` and `R` are raw 32-byte digests, never hexadecimal text.

Tree construction follows the RFC 6962 recursive split. A lone node is promoted; the last node is not duplicated.

## 3. Fixture

Fixture: `FIX-CK003-DQ002-RFC6962-2LEAF`

Inputs:

- leaf A UTF-8: `a`
- leaf A bytes: `61`
- leaf B UTF-8: `b`
- leaf B bytes: `62`

Expected independent values:

- leaf A: `022a6979e6dab7aa5ae4c3e5e45f7e977112a7e63593820dbec1ec738a24f93c`
- leaf B: `57eb35615d47f34ec714cacdf5fd74608a5e8e102724e80b24b287c0c27b6a31`
- root: `b137985ff484fb600db93107c77b0365c80d78f5b429ded0fd97361d077999eb`

For a two-leaf tree the expected audit paths are:

- leaf A (index 0): sibling = leaf B, direction = `right`;
- leaf B (index 1): sibling = leaf A, direction = `left`.

## 4. Preflight evidence

### Normative vector calculation

The expected leaf and root values above were independently recomputed from the byte-domain formulas. They match the existing DQ-002 fixture values.

### RI-PY source preflight

The current RI-PY implementation inspected for DQ-002 does not implement the proposed RFC 6962 contract. It hashes ordinary string leaves directly, concatenates hexadecimal digest strings for interior nodes, and duplicates the final node for odd counts. Therefore it cannot pass this gate without a remediation change after DQ-002 approval.

A local execution against the uploaded RI-PY source produced a two-leaf root of:

`fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603`

This is intentionally recorded as **negative preflight evidence**, not as conformance evidence.

### RI-RS source preflight

The inspected `src/merkle.rs` implements the required RFC 6962 leaf domain, node domain, recursive tree shape, audit path generation and proof verification. Full execution evidence still requires running the actual Rust test/conformance harness in the RI-RS repository.

The current analysis environment does not contain `cargo`, so no RI-RS execution result is claimed here.

## 5. Gate status

| Check | Status |
|---|---|
| Fixture identity | PASS |
| Independent expected leaf A | PASS |
| Independent expected leaf B | PASS |
| Independent expected root | PASS |
| RI-PY source conforms | FAIL — remediation required |
| RI-RS source conforms | PASS at source inspection |
| RI-PY actual execution | NOT PASS |
| RI-RS actual execution | NOT RUN |
| Root equality | NOT ESTABLISHED |
| Proof verification | NOT ESTABLISHED cross-language |
| Negative controls | NOT ESTABLISHED cross-language |
| Provenance ledger | INCOMPLETE |
| CROSS-LANGUAGE-002 | **OPEN** |

## 6. Closure criteria

CROSS-LANGUAGE-002 MUST NOT be marked PASS until:

- DQ-002 has been approved as the normative contract;
- RI-PY remediation implements the approved contract;
- RI-PY and RI-RS independently execute the fixture;
- leaf, node and root artifacts are independently re-hashed;
- both inclusion proofs verify;
- wrong-leaf, wrong-node-domain and mutated-root controls reject;
- execution/source commit provenance is recorded for both implementations;
- the resulting evidence is independently replayable.

No production implementation is modified by this evidence package.

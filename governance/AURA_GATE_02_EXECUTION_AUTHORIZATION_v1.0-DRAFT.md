# AURA GATE-02 Execution Authorization — Draft

Artifact ID: AURA-GATE-02-AUTH-v1.0
Status: PROPOSED GOVERNANCE ACT — NOT APPROVED — NOT EFFECTIVE
Classification: EXECUTION AUTHORIZATION REQUEST
Repository of record: vaidt/aura-specification
Preparation branch: governance/gate-02-authorization-draft-2026-09-26

> This document is a draft for human ratification. It does not itself authorize B-VAL-014 or BNC-1. The Custodian Agent cannot convert this document to EFFECTIVE status.

## 1. Purpose

Provide a narrowly scoped governance act that, after explicit ratification, may authorize execution of GATE-02 without first resolving the entire AG-001 protocol-authority question.

The act is intentionally limited to B-VAL-014 and BNC-1 execution and its associated conformance/evidence boundary.

## 2. Decision class

Decision class: HUMAN-ONLY.

Reason: the governing operating instructions classify authority changes and new delegations that are not already explicitly delegated as human-only matters. The Agent may prepare and route the act but may not issue the delegation.

## 3. Requested authority

Requested outcome:

EXECUTION_AUTHORITY(B-VAL-014, BNC-1) = GRANTED

only after the ratifying authority, effective date, repository scope, conformance boundary, evidence boundary, and preconditions below are explicitly accepted.

This requested authority does not:

- resolve AG-001 generally;
- establish or replace Protocol Authority;
- alter the normative protocol contract;
- authorize production/runtime changes;
- authorize constitutional changes;
- authorize sealing or release;
- authorize unrelated conformance work.

## 4. Exact technical scope

### BNC-1

Authorize the defined boundary-corruption control in which one input octet is intentionally flipped on one side and the gate must detect the mismatch.

Required outcome: the corruption MUST be detected by the applicable B-VAL-012 and B-VAL-014 controls. No control may be silently merged with another gate.

### B-VAL-014

Authorize execution only against the controlling BC-02 §14 definition.

Required assertions:

- receipt.receipt_digest == input_segment_sha256 on both sides;
- receipt_digest_source == RECEIVER_RECOMPUTED on both sides;
- raw_input_encoding is one of identity, base64, or base16;
- H_PY(received_octets) == H_RS(received_octets) == H_ISSUED where those values are in scope;
- the generated evidence is preserved without rewriting the observed values.

These statements are the execution target, not a new protocol definition.

## 5. Preconditions

Execution remains prohibited until every precondition is evidenced:

PRE-01 — Schema binding:
BC-02 §14 vocabulary is explicitly bound to the actual receipt fields consumed by the test.

PRE-02 — BNC-1 execution readiness:
The exact fixture, mutation rule, receiver(s), and expected gate behavior are identified before execution. Expected cryptographic values must be produced by execution, not pre-authored from assumption.

PRE-03 — Repository/corpus binding:
The ratification record names the exact repository/repositories, ref/commit, and paths in which the authorized execution will occur.

PRE-04 — Conformance boundary:
The ratification record names which conformance gate owns the result and confirms that execution evidence does not redefine the protocol.

PRE-05 — Evidence authority:
The ratification record identifies the authoritative evidence location and the artifact that will be considered the receipt of execution.

## 6. Repository and scope boundary

Governance record:
`vaidt/aura-specification`

Execution repository/corpus:
NOT YET BOUND — MUST BE EXPLICITLY NAMED IN THE RATIFICATION RECORD.

Allowed mutation scope:
Only conformance fixtures, test harnesses, evidence artifacts, and metadata strictly necessary to execute BNC-1 and B-VAL-014.

Forbidden scope:

- production runtime code;
- constitutional artifacts and constants;
- authority model;
- protocol semantics unrelated to BC-02 §14;
- unrelated conformance gates;
- historical artifact deletion;
- force-push or history rewriting;
- sealing/release operations.

## 7. Evidence contract

Every execution must preserve:

1. exact repository and ref/commit;
2. fixture identifier and source digest;
3. receiver implementation identity;
4. raw received octets or an unambiguous representation of them;
5. computed digest values;
6. gate exit/status;
7. negative-control result for BNC-1;
8. execution timestamp and toolchain metadata where available;
9. statement of which assertions are evidence versus normative requirements.

No PASS may be declared from an unexecuted fixture, inferred digest, or cross-repository narrative alone.

## 8. Exit criteria

GATE-02 may be reported PASS only when:

- PRE-01 through PRE-05 are all evidenced;
- BNC-1 executes and detects the defined corruption;
- B-VAL-014 executes against the controlling definition;
- required receipt/digest relationships are observed;
- evidence is stored at the authorized boundary;
- no production/runtime mutation occurs;
- the execution record identifies exact refs and commits;
- the result is independently reviewable.

Otherwise:

GATE-02 = BLOCKED / INCOMPLETE.

## 9. Relationship to AG-001

This act is designed as a scoped delegation, not a resolution of the general protocol-authority dispute.

Therefore:

AG-001 MAY REMAIN OPEN
while
GATE-02 MAY BECOME AUTHORIZED
only if the ratified act explicitly establishes the scoped authority required by Sections 4–8.

If the ratifying authority determines that this scoped delegation cannot be valid while AG-001 remains open, this draft must remain NOT EFFECTIVE and no GATE-02 execution may occur.

## 10. Ratification record

Ratifying authority: TBD
Authority basis: TBD
Ratification decision ID: TBD
Ratification date: TBD
Effective date: TBD
Authorized execution repository/ref: TBD
Authorized evidence location: TBD
Conformance authority: TBD
Evidence authority: TBD

Required human determination:

Accept / Reject / Return for amendment

## 11. Agent disposition

The Agent records this as:

PROPOSAL PREPARED
DELEGATION NOT ISSUED
EXECUTION NOT AUTHORIZED

END OF DRAFT
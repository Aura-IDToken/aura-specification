# CHIEF ARCHITECT → CUSTODIAN SCOPE BRIDGE

## Q1 Decision-Surface Designation

**Status:** DRAFT — AUTHORITY INSTRUMENT PREPARATION  
**Class:** GOVERNANCE / JURISDICTION  
**Purpose:** Establish bounded jurisdiction for the subsequent Q1 Selection Act  
**Decision exercised by this document:** NONE  
**Package selected:** NONE

> **Important:** This document is a proposed bridge instrument. It does not itself constitute the Chief Architect's approval or delegation. It becomes binding only through the competent governance act/approval required by the existing governance hierarchy.

---

## 1. Purpose

This Scope Bridge establishes, subject to explicit approval by the competent authority, a bounded delegation from the Chief Architect to the Protocol Custodian concerning one decision class only:

> **designation of Q1 Decision Surface**

The bridge exists to close the jurisdictional gap identified by the preceding authority and jurisdiction audits.

It does not answer Q1.

It establishes only the authority channel through which the Q1 decision may subsequently be made.

This narrowness is consistent with the existing Custodian decision model, under which normative decisions are explicitly recorded as controlled state transitions and their effects are bounded rather than inferred beyond their stated domain.

---

## 2. Delegating Authority

**Delegator:**

> **Chief Architect**

The Chief Architect is the delegating governance authority for this bridge.

The bridge does not create or redefine the general governance hierarchy.

---

## 3. Receiving Authority

**Delegate:**

> **Protocol Custodian**

The Protocol Custodian receives only the bounded authority expressly defined in §4.

The existence of general Custodian authority does not expand this bridge beyond its stated scope.

The existing Custodian register demonstrates that Custodian authority can operate as a defined decision class—for example, the 2026-08-23 register identifies the decision authority as Custodian and the decision class as normative reconciliation / state transition.

That precedent is used here only to establish the governance pattern of bounded decision authority. It does not itself establish Q1 jurisdiction.

---

## 4. Delegated Decision Class

The delegated decision class is:

> **DESIGNATION OF Q1 DECISION SURFACE**

For purposes of this bridge, Q1 means:

> determining which existing prepared artifact, if any, shall constitute the **designated Q1 Decision Surface** for the subsequent consideration of the unresolved BC-02 A/B questions.

The delegation concerns designation only.

It does not delegate authority to determine the substantive answers contained within the designated surface.

---

## 5. Closed Outcome Set

The Protocol Custodian's authority under this bridge is limited to exactly three possible dispositions:

### Package #1

The decision surface identified as:

`conformance/boundary/BC-02.1-CUSTODIAN-DECISION-PACKAGE-A-B.md`

at the exact artifact identity established by the preceding evidence record.

### Package #2

The decision surface identified as:

`conformance/boundary/BC-02-CUSTODIAN-DECISION-PACKAGE-A-B-v1.md`

at the exact artifact identity established by the preceding evidence record.

### Neither

Neither existing package is designated as the Q1 Decision Surface.

No fourth disposition is created by this bridge.

In particular, the following are not independent outcomes:

- latest
- preferred
- more complete
- successor
- superseding
- merged package
- combined package

Those classifications cannot be inferred from chronology, size, identifier coverage, review activity, or branch topology.

---

## 6. Exercise of Delegated Authority

The delegated authority is exercised only by a subsequent Custodian Selection Act.

The Selection Act must identify the selected disposition by exact artifact identity where applicable.

The Selection Act shall constitute the formal record of the exercise of the delegated jurisdiction.

The bridge itself is not the Selection Act.

Therefore:

```text
SCOPE BRIDGE
     │
     │ establishes jurisdiction
     ▼
PROTOCOL CUSTODIAN
     │
     │ exercises jurisdiction
     ▼
SELECTION ACT
     │
     └── records Package #1 / Package #2 / Neither
```

---

## 7. Minimum Selection-Act Identity

Where Package #1 or Package #2 is selected, the subsequent Selection Act shall identify at minimum:

1. exact path;
2. exact commit;
3. exact blob;
4. exact SHA-256;
5. Q1 identifier;
6. selected disposition;
7. delegated-authority reference to this Scope Bridge;
8. Custodian identity;
9. date;
10. required approval/signature record.

The Selection Act shall not rely upon an unqualified expression such as:

> "the A/B package"

because the evidence establishes two distinct artifacts with materially different A/B taxonomies.

---

## 8. Effect of Designation

Designation establishes only:

> which prepared artifact defines the surface through which Q1's underlying questions are subsequently routed.

Designation does **not** establish that any proposition contained within the selected artifact is correct, normative, conformant, executable, or implemented.

Designation does **not** incorporate the selected artifact into the normative protocol corpus.

Accordingly:

```text
DESIGNATION
     ≠
SUBSTANTIVE RESOLUTION
```

and:

```text
SELECTION OF SURFACE
     ≠
APPROVAL OF CONTENT
```

This boundary follows the existing Custodian model, which explicitly distinguishes normative decision from implementation and conformance effects.

---

## 9. Explicit Exclusions

Nothing in this Scope Bridge delegates authority to:

### 9.1 Decision A

The substantive resolution of Decision A remains outside this bridge.

### 9.2 Decision B

The substantive resolution of Decision B remains outside this bridge.

### 9.3 C-1

C-1 remains an independent authority question.

### 9.4 C-2

C-2 remains an independent authority/hierarchy question.

No outcome under this bridge shall be construed as evidence for, against, or dispositive of C-1 or C-2.

### 9.5 ARI semantics

This bridge neither defines nor interprets ARI semantics.

### 9.6 Implementation

This bridge does not authorize implementation activity.

### 9.7 Conformance

This bridge does not establish, execute, or determine conformance.

### 9.8 Fixture operations

This bridge does not authorize:

- fixture creation;
- fixture issuance;
- fixture modification;
- B-VAL execution;
- BNC execution;
- controlled re-handoff.

### 9.9 Canonical protocol modification

This bridge does not amend, replace, supersede, freeze, or otherwise modify a normative protocol requirement.

---

## 10. Authority-Leakage Firewall

Nothing in this Scope Bridge:

(a) determines the substance of Decision A or Decision B;

(b) resolves C-1 or C-2;

(c) defines, determines, or interprets ARI semantics;

(d) authorizes implementation activity;

(e) establishes or determines conformance;

(f) modifies, supersedes, amends, or freezes any normative protocol requirement;

(g) converts a selected package into normative authority merely by designating it as the Q1 Decision Surface;

(h) authorizes execution of any downstream validation or conformance gate;

(i) establishes authority for any artifact referenced by a selected package;

(j) converts historical or engineering evidence into normative authority.

The distinction is material: artifact existence, content addressing, implementation behavior, and historical evidence do not by themselves establish upstream normative authority.

---

## 11. Reachability Boundary

Selection under this bridge does not alter repository state.

In particular:

> designation of a branch-local package does not make that package reachable from `origin/main`.

Selection and integration are separate governance events.

No merge, cherry-pick, branch modification, commit, or file modification is authorized by this bridge.

---

## 12. Non-Supersession Rule

Designation of Package #1 does not, by itself, establish that Package #2 was erroneous, superseded, deprecated, or historically invalid.

Likewise, designation of Package #2 does not establish that Package #1 was erroneous, superseded, deprecated, or historically invalid.

If the Custodian selects one package, the competing package remains a separate historical/preparatory artifact unless a subsequent authority act provides another disposition.

---

## 13. C-1 / C-2 Independence

The Q1 designation jurisdiction established by this bridge is independent of C-1 and C-2.

Accordingly:

```text
Q1 Scope Bridge
       │
       ├── Q1 jurisdiction
       │
       └── does NOT resolve
              ├── C-1
              └── C-2
```

Neither C-1 nor C-2 is implicitly incorporated into the delegation.

---

## 14. ARI Independence

The bridge creates no authority concerning:

- ARI definition;
- ARI semantic interpretation;
- ARI decision taxonomy;
- ARI protocol/instrument classification;
- ARI conformance;
- ARI implementation.

ARI remains an independent governance surface.

---

## 15. Formal Governance Chain

If and only if this bridge receives the required binding approval, the intended governance chain becomes:

```text
CHIEF ARCHITECT
      │
      │ approval / delegation act
      ▼
SCOPE BRIDGE
      │
      │ establishes bounded jurisdiction
      ▼
PROTOCOL CUSTODIAN
      │
      │ exercises jurisdiction
      ▼
SELECTION ACT
      │
      ├── PACKAGE #1
      ├── PACKAGE #2
      └── NEITHER
```

The resulting Selection Act is an exercise of delegated authority, not a new source of delegation.

---

## 16. Post-Bridge Gate State

Before binding approval:

> **Q1 Jurisdiction: NOT ESTABLISHED**

After binding approval:

> **Q1 Jurisdiction: ESTABLISHED — BOUNDED**

Only then:

> **Q1 Selection Gate: OPEN**

The bridge therefore does not produce a Q1 answer.

It changes only the jurisdictional state required to permit the later Q1 Selection Act.

---

## 17. Status and Approval

**Current status of this document:**

> **DRAFT — NON-BINDING PREPARATION**

**Authority exercised by this document:**

> **NONE**

**Delegation effective:**

> **NO — pending competent approval**

**Package selected:**

> **NONE**

**Decision A:**

> **OPEN**

**Decision B:**

> **OPEN**

**C-1:**

> **OPEN**

**C-2:**

> **OPEN**

**ARI semantics:**

> **OPEN / UNRESOLVED**

**Implementation:**

> **UNAUTHORIZED**

**Conformance:**

> **UNDETERMINED / UNAUTHORIZED BY THIS BRIDGE**

---

## 18. Approval Record

### CHIEF ARCHITECT → CUSTODIAN SCOPE BRIDGE

**Delegating Authority:**  
`[CHIEF ARCHITECT]`

**Receiving Authority:**  
`[PROTOCOL CUSTODIAN]`

**Delegated Decision Class:**  
`[DESIGNATION OF Q1 DECISION SURFACE]`

**Permitted Outcomes:**  
`[PACKAGE #1 / PACKAGE #2 / NEITHER]`

**Effective Date:**  
`[DATE]`

**Chief Architect:**  
`[NAME / ROLE]`

**Approval / Signature:**  
`[REQUIRED GOVERNANCE RECORD]`

**Custodian Acknowledgement:**  
`[REQUIRED RECORD, IF GOVERNANCE MODEL REQUIRES]`

**Status:**  
`[APPROVED / NOT APPROVED]`

---

## Final Classification

This is the proposed governance artifact for submission to the competent authority.

It is deliberately narrower than the Custodian Decision Register.

The existing register demonstrates that Custodian decisions can be bounded by explicit decision class and explicit non-effects; it does not itself establish Q1 jurisdiction.

No Q1 Selection should occur until the Status above is changed from:

> **DRAFT — NON-BINDING PREPARATION**

to an actually binding approved state.

**Boundary invariant:**

> This Scope Bridge establishes only the bounded jurisdiction to designate the Q1 Decision Surface. It does not resolve Decision A, Decision B, C-1, C-2, ARI semantics, implementation, or conformance.

# AURA-ACT-001 — Crisis Resolution Act
## Rozstrzygnięcie konfliktu statusu M1 i bramki G1

**Act ID:** AURA-ACT-001  
**Short name:** ACRA-001  
**Version:** 0.1-DRAFT  
**Status:** PROPOSED · NON-CONSTITUTIVE · NOT RATIFIED  
**Normative effect:** NONE UNTIL COMPETENT RATIFICATION, SIGNATURE VERIFICATION AND REGISTRATION  
**Effective date:** PENDING  
**Preparation date:** 2026-10-17  
**Scope:** vaidt/Kt-ry-Program; vaidt/aura-specification  
**Document class:** Proposed crisis-resolution governance act; not an external legal opinion  
**Authority to issue this act:** NOT ESTABLISHED — G1 REMAINS BLOCKED  
**Current authorization state:** NOT AUTHORIZED

> **Important status boundary:** This document proposes a controlled resolution. It does not establish its own authority, invalidate a record by its own presence, ratify Article XIII, or authorize Stage 3. The resolutions below have no binding effect unless the competent issuer and applicable ratification mechanism are independently established, the exact act revision is validly signed and verified, and the decision is registered with an effective date.

---

## 1. Metadata and context

### 1.1 Purpose

This proposed Act addresses the conflict between the closure declarations in AURA_M1_CLOSURE_RECORD_v1.0.md and the source-level evidence currently available for the asserted authority chain and the constitutional procedure associated with Article XIII.

The goal is to preserve every historical record, prevent an unsupported status declaration from being used as conclusive authority for new decisions, define a controlled proposed disposition, and make future state transitions dependent on independently reviewable evidence.

The term “split-brain” is used here as a description of conflicting repository status assertions. It is not a finding that any external legal act is automatically void.

### 1.2 Identifiers and frozen observations

The following values identify the reviewed snapshot used to prepare this draft. They are evidence locators, not signatures, ratification, or proof of authority.

| Item | Observed reference |
|---|---|
| AURA specification main commit | 8f0cd6be94a68a3728e69a1d21d49237c9d8bd05 |
| AURA_M1_CLOSURE_RECORD_v1.0.md Git blob SHA-1 | 2a729379f8d306a1f371db26d0ec4577cf8701b6 |
| Article XIII source-evidence package | vaidt/aura-specification PR #32, draft, HEAD c9933a3014cf5241fced26a5b87da9bf89cfb490 |
| Stage 3 proposal | vaidt/Kt-ry-Program PR #21, HEAD d269323421e1dbfc5fa64fc6da9d6b61071ef9f4 |
| Dual-track governance proposal | vaidt/Kt-ry-Program PR #12, HEAD 183cfc54c9e0f81823f92d67f7f4a7a47ca804e9 |
| Kt-ry-Program main commit | 8b62cca211cd8969040aa90ac501db5fa6649bca |
| Kt-ry-Program integration commit | bd9d59b93a661a987b8c848e5767103cf7ff3fad |
| Integration ruleset | ID 25306960, “ASIG integration — R&D protection” |

All references must be re-read and their digests refreshed before any ratification decision. A branch name or a mutable URL alone is insufficient to identify the content being approved.

### 1.3 Scope and exclusions

This proposed Act concerns governance records and repository controls in vaidt/aura-specification and vaidt/Kt-ry-Program.

It does not:
- amend the frozen AURA Constitution;
- establish the validity or invalidity of Article XIII under external law;
- create a new constitutional authority or make the author of this Act its own competent issuer;
- close CAPA NC-ASIG-2026-10-17-PR10;
- authorize runtime implementation, normative specification changes, conformance claims, release activity, or production credential use;
- alter any live GitHub ruleset or branch-protection setting merely by stating a requirement.

### 1.4 Related draft with a distinct identifier

As of the preparation snapshot, vaidt/aura-specification PR #33 contains a separate non-constitutive draft titled AURA Crisis Resolution Act and identified as AURA-CRA-001.

AURA-ACT-001 / ACRA-001 is a distinct identifier. This document must not silently replace or supersede AURA-CRA-001. Before either draft is ratified, an authorized reviewer must record whether the drafts are to be consolidated, one withdrawn, or maintained as distinct proposals. Two conflicting crisis-act identifiers must not be represented as concurrent effective authority.

---

## 2. Findings of fact

These findings are limited to the inspected repository records and API snapshots. “Not established” means the reviewed evidence does not prove a proposition; it is not, by itself, a finding of external legal invalidity.

### F-01 — The M1 closure record asserts closure and proven authority continuity

At the observed specification main commit, AURA_M1_CLOSURE_RECORD_v1.0.md declares:
- Status: RATIFIED;
- Ratification_Status: EXECUTED;
- M1_Governance_Gate: CLOSED;
- Authority_Continuity: PROVEN;
- Decision_Gaps: RESOLVED;
- Implementation_Authorization_Eligibility: UNLOCKED.

The file identifies GENESIS_DECLARATION.txt and AUTHORITY_BINDING_RECORD_v1.1.md as components of the constitutive evidence chain. These are material status declarations. Their presence in a designated closure record does not independently resolve contradictory source-level findings.

### F-02 — The source-level review does not establish the Article XIII amendment procedure

The non-merged draft evidence package at vaidt/aura-specification PR #32 records that the reviewed insertion of Article XIII into the frozen Constitution v1.0 did not itself evidence the amendment steps specified in Article XI, including an RFC, Architecture Review, impact analysis, dependent-document updates, and approval.

That source-level disposition is “PROCEDURAL EFFECT NOT ESTABLISHED FROM THE SOURCES REVIEWED.” This is a bounded evidentiary finding, not a claim of final external legal invalidity.

### F-03 — The cryptographic result does not establish constitutional competence

The current PR #32 draft reports that the Genesis declaration's detached signature verified mathematically over the inspected preimage through Python cryptography, the OpenSSL CLI, and Node.js crypto. It also states:
- the three tool paths do not establish three independent machines or independent cryptographic backends;
- canonical OpenSSH ssh-keygen -Y verify was not run in the preparation environment;
- signing time, key-revocation status, and independent natural-person identity binding are not established;
- cryptographic relation to a key does not itself establish the key holder's constitutional competence.

The source-evidence package remains a draft and is not itself a constitutive act.

### F-04 — The separate Authority instrument does not independently complete the authority chain

The inspected Authority Kamil Krasiński Aura-IDToken.md instrument identifies “Twórca i Właściciel projektu AURA” as the basis of competence, names a holder, and states a scope and date. The inspected document does not, by itself, establish the upstream primary source that empowered its issuer, the issuer's own competence, or an independently verified person-to-key binding sufficient for the constitutional authority asserted.

It is a candidate source for continued examination, not a conclusive authority instrument merely because it exists in Git.

### F-05 — PR #21 remains a non-constitutive proposal and the Stage 3 authority gate is explicitly blocked

PR #21 proposes AURA-STAGE3-AUTH-001. Its current text identifies G1 as NOT PROVEN / BLOCKED, leaves ratification and registration fields pending, and states effective authorization as NOT AUTHORIZED. The PR is open and unmerged, and no submitted formal review was returned by the inspected review endpoint.

Passing CI validates only the tested commit and its configured checks; it does not establish the competence of a ratifier or satisfy the constitutive requirements of this Act.

### F-06 — The dual-track policy is limited to infrastructure preparation; the observed integration ruleset does not require an approving review

PR #12 records a limited operational acceptance for CI/security-infrastructure preparation only. Its comment expressly states that it is not an approving review, does not activate integration for experimental merges, and does not close CAPA or authorize runtime work or AURA conformance.

The active Kt-ry-Program integration ruleset ID 25306960 has seven required status-check contexts and no bypass actors. Its pull-request rule reports required_approving_review_count = 0, required_reviewers = [], and require_code_owner_review = false. Thus the currently observed ruleset does not technically require an approving review before merging into integration.

The main branch was reported as protected with four required status checks. The available integration could not independently read the main branch's enforce_admins value. This limitation must not be converted into a PASS claim.

### F-07 — The governance status conflict has not been resolved by the inspected material

The M1 closure record asserts CLOSED / PROVEN while the source-level Article XIII audit and the Stage 3 proposal record a material unresolved authority and procedure gap. PR #32 remains unmerged and non-constitutive. The PR #12 operational preparation decision does not resolve this conflict.

No inspected material establishes a competent, independent decision that reconciles the conflicting assertions and authorizes a binding M1 state transition.

---

## 3. Proposed binding resolutions

The following resolutions are proposals only. They are not effective unless the authorization and registration conditions in Section 5 are satisfied. On entry into force, they would govern future reliance and repository status reporting within the stated scope, subject to the competent issuer's established authority.

### Z-01 — Deprecation for future reliance; preservation of history

Upon valid entry into force, AURA_M1_CLOSURE_RECORD_v1.0.md is to be classified as a historical record whose declarations CLOSED / PROVEN / RESOLVED / UNLOCKED are DEPRECATED FOR FUTURE GOVERNANCE RELIANCE pending the required evidence reconciliation.

The original record, blob, commit history, signatures, and historical references must be preserved. Deprecation must not be implemented by deleting, rewriting, or concealing the original evidentiary content.

This resolution does not assert that the historical document never existed, nor does it independently determine the external legal validity of past acts. Its effect is to prevent the unresolved closure assertions from being treated as conclusive authority for new governance decisions after the Act becomes effective.

### Z-02 — Proposed G1 disposition

Upon valid entry into force, the operational disposition for new decisions requiring the disputed authority chain is to be recorded as:

- Authority continuity: NOT PROVEN;
- Governance closure for the affected gate: BLOCKED;
- Ratification eligibility dependent on the disputed authority: NOT ESTABLISHED;
- Implementation authorization dependent on that authority: NOT GRANTED.

This does not authorize an unsupported edit of a past record. The authoritative status index and closure-state register must be reconciled through a competent, traceable decision and must retain a link to the preserved historical M1 record.

### Z-03 — Stage 3 authorization hold

Until G1 has been independently established and the exact Stage 3 act is validly ratified by a competent issuer, AURA-STAGE3-AUTH-001 must remain PROPOSED and NOT AUTHORIZED.

No PR merge, CI result, account permission, document label, or signature alone may be used as proof that the proposed authorization is effective. No runtime implementation, normative mutation, conformance claim, or release action may rely on the proposed Stage 3 authorization while the gate remains blocked.

### Z-04 — No self-authorization or status-by-declaration

This Act must not be used to establish its own issuer's competence. Repository ownership, administrator access, historical code authorship, a cryptographic key relationship, or a declaration in Markdown is not automatically equivalent to constitutional authority.

A valid signature can authenticate the signed content under a key. It cannot by itself prove the signer's competent authority, current holder status, scope, or the procedural effectiveness of the act.

### Z-05 — Independent resolution of draft identity and status

Before any crisis-resolution Act is ratified, the relationship between this draft AURA-ACT-001 and the separate AURA-CRA-001 proposal in PR #33 must be explicitly recorded. The selected canonical act identifier, exact content digest, and disposition of the other draft must be included in the competent decision record.

---

## 4. Execution directives

These are proposed execution instructions. They must not be represented as binding commands before this Act validly enters into force. Routine evidence preservation and compliance with already-effective repository controls remain subject to their existing authority.

### E-01 — Preserve and bind the evidence snapshot

Before implementation, capture and retain:
- the exact M1 record blob and its containing commit;
- the exact main/base and proposed-branch commit identifiers for the relevant repositories;
- the current PR #21, PR #12, PR #32, and PR #33 metadata, diffs, comments, reviews, and required-check results;
- the current GitHub rulesets and branch-protection configuration, including explicit read-back of administrator enforcement by an appropriately authorized administrator;
- hashes, retrieval timestamps, tool versions, and any limitations in evidence collection.

The evidence package must distinguish current repository state from historical observations and unmerged drafts.

### E-02 — Add an accurate, non-constitutive warning to the M1 record

The proposed change in this PR adds a warning at the top of AURA_M1_CLOSURE_RECORD_v1.0.md. Until valid ratification, the warning must say that deprecation is proposed and not effective. It must not assert that AURA-ACT-001 has already invalidated the record.

After valid entry into force, the warning and status index may be updated under the registered execution procedure to identify the exact Act revision, decision record, effective date, and relevant content digests. The historical closure fields must remain recoverable from the preserved record and Git history.

### E-03 — Require effective review controls on governance changes

An authorized repository administrator must review the live rulesets and branch-protection settings in both in-scope repositories. Before any new governance-document merge relying on this Act, the applicable protected or governance-critical branches must enforce at least one approving review, as well as the applicable required status checks.

For Kt-ry-Program integration, this specifically requires correcting the observed ruleset approval count of zero. For aura-specification main, the reviewed API snapshot reported the branch as not protected; the protection state must be independently read back and resolved through the ordinary authorized repository-control process.

After each authorized change, read back the configuration and preserve the before/after state and verification results. Do not infer configuration from a policy file or ruleset name alone. This Act does not itself authorize changing any live setting before it is effective and properly approved.

### E-04 — Communicate the unresolved gate without overstating authority

PR #21 and PR #12 should receive a traceable cross-reference to this Act proposal. Before this Act is effective, any comment must describe it as a PROPOSED, NON-CONSTITUTIVE review item and must not say that work is halted “by order of ACRA-001.”

Only after valid ratification and registration may an authorized operator post a binding-effect notice. Such a notice must link to the exact registered Act revision and decision evidence. It must not retrospectively characterize a proposed draft as having been effective when the comment was written.

### E-05 — Obtain primary authority evidence and independent review

The authority-evidence package must establish, from a competent primary source:
1. the instrument or rule from which the asserted authority originates;
2. the competence of the issuer of that instrument;
3. the current holder and independently established identity;
4. the scope of authority covering the precise decision and repositories;
5. the effective date, continued validity, and applicable succession, delegation, or revocation terms.

An independent reviewer must assess the source chain and the Article XI procedure. If a detached signature is relied upon, its exact signed preimage and signature must be verified with standards-conforming tooling, and the result must identify tool versions, digests, and limitations. Technical signature success and authority competence must be reported as distinct findings.

### E-06 — Preserve CAPA independence

CAPA NC-ASIG-2026-10-17-PR10 remains a separate, open disposition until its own closure criteria are evidenced. This Act proposal does not close it, remove the recorded deviation, convert AI-assisted review into an independent human approval, or authorize a break-glass change to branch protection.

### E-07 — Apply a gated state transition

The required order is:

PRESERVE EVIDENCE
→ RECONCILE PRIMARY AUTHORITY SOURCE
→ INDEPENDENT AUTHORITY AND PROCEDURE REVIEW
→ COMPETENT ISSUER ESTABLISHED
→ ACT-SPECIFIC RATIFICATION
→ SIGNATURE AND CONTENT DIGEST VERIFIED
→ RATIFICATION REGISTERED WITH EFFECTIVE DATE
→ M1 STATUS INDEX RECONCILED
→ RELEVANT REPOSITORY CONTROLS READ BACK
→ SEPARATE STAGE 3 DECISION, IF ELIGIBLE

Stop at the first unmet prerequisite. Exhausting the available search does not mean the authority question has been resolved.

---

## 5. Authorization, signature, and registration

### 5.1 Conditions for effectiveness

This Act must remain PROPOSED, NON-CONSTITUTIVE, and NOT RATIFIED unless all of the following are established and preserved:

1. A competent issuer is independently identified from a primary authority source independent of the disputed claim, or a competent independent decision resolves the disputed authority chain.
2. The issuer's current competence and its scope over this exact Act are evidenced.
3. The exact approved Act revision and SHA-256 content digest are identified.
4. The applicable ratification mechanism is identified and followed.
5. The issuer's signature is verified against the exact approved content. The signature algorithm, key fingerprint, trust basis, verification tool and version, timestamp evidence if available, revocation checks, and residual limitations are recorded.
6. The ratification decision, effective date, conditions, and registration location are recorded in the designated repository.
7. An independent reviewer verifies that the registered artifact, signature, decision record, and resulting status agree.

A Git commit signature, Sigstore attestation, CI result, PR approval, repository ownership, or the presence of this file does not alone satisfy these conditions.

### 5.2 Ratification record — intentionally pending

- Competent issuer: PENDING — NOT ESTABLISHED
- Primary authority source: PENDING
- Independent authority reviewer and report: PENDING
- Decision and ratification mechanism: PENDING
- Approved Act version: 0.1-DRAFT — NOT RATIFIED
- Approved content SHA-256: PENDING
- Signature type and key fingerprint: PENDING
- Signature verification result: PENDING
- Key revocation and identity-binding evidence: PENDING
- Ratification registration commit and location: PENDING
- Effective date and conditions: PENDING
- Independent registration verification: PENDING
- Disposition of AURA-CRA-001 draft PR #33: PENDING

### 5.3 Current determination

**ACRA-001:** PROPOSED · NON-CONSTITUTIVE · NOT RATIFIED  
**M1 record deprecation:** PROPOSED · NOT EFFECTIVE  
**G1 authority continuity:** NOT PROVEN / BLOCKED for new decisions relying on the disputed authority chain  
**AURA-STAGE3-AUTH-001:** PROPOSED · NOT AUTHORIZED  
**Runtime implementation / normative changes / release authorization:** NOT GRANTED BY THIS DRAFT

If a competent issuer and valid source of authority cannot be independently established, this document remains a non-constitutive evidence and resolution proposal. No self-authorizing state transition is permitted.

---

**End of proposed Act.**

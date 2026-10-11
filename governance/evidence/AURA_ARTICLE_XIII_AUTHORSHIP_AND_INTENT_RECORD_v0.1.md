# AURA — Article XIII: Author Intent and Source Evidence Record

Document_ID: AURA-ARTICLE-XIII-INTENT-EVIDENCE-001  
Version: 0.1  
Record_Date: 2026-10-11  
Status: DRAFT · NON-CONSTITUTIVE · NOT RATIFIED  
Normative_Effect: NONE  
Constitutional_Amendment: NO  
Author_Statement_Authentication: NOT CRYPTOGRAPHICALLY BOUND  
Review_Mode: READ-ONLY SOURCE REVIEW  
Review_Result: PROCEDURAL EFFECT NOT ESTABLISHED FROM THE SOURCES REVIEWED

---

## 1. Purpose and boundaries

This record preserves the requester's clarification that the decision to introduce Article XIII was intentional, and records the source-level evidence reviewed to distinguish authorial intent, repository history, cryptographic integrity, authority, and normative effect.

This is an evidentiary and review artifact only. It does not:

- ratify, enact, amend, validate, or repeal Article XIII;
- amend or replace the frozen AURA Constitution v1.0;
- establish the identity, authority, or continuity of any constitutional office-holder;
- ratify P-008 or any other protocol decision;
- close, reopen, or otherwise change the authoritative state of M1;
- replace an RFC, Architecture Review, impact analysis, approval, or independent governance decision.

The record must not be cited as constitutive authority.

## 2. Statement of intent — captured, not signed

On 2026-10-11, the requester explicitly selected the interpretation that the decision to introduce Article XIII was intentional: the requester meant to establish Article XIII, and now requests that the intent be documented and the effectiveness of the amendment independently assessed.

This records the requester's statement as received in the working conversation. It is not a cryptographically signed author attestation, and this record does not independently establish the real-world identity of the person making the statement.

### Proposed first-person confirmation for author review

> I confirm that my decision to introduce Article XIII — Genesis and Succession was intentional. I request that this intent be preserved in the evidence record and that the amendment's procedural and normative effectiveness be independently assessed. This statement of intent does not, by itself, assert or establish that Article XIII entered into force under the AURA governance procedure.

Author signature: **PENDING**  
Independent identity binding for the statement: **PENDING**  
Date of signed confirmation: **PENDING**

No signature or date is to be inferred from this draft or from its repository commit.

## 3. Source snapshot examined

Repository: `vaidt/aura-specification`  
Observed `main` HEAD: `36f30297709334d3935f98d2fe7c84d09f3ceec9`  
Observed `main` protection: disabled  
Required status checks: enforcement off; no required contexts returned  
Constitution path: `constitution/AURA_CONSTITUTION.md`  
Constitution blob SHA: `ae121ce247066fb2cc920fb7114e6547fd4f7398`

The review is limited to the source artifacts and GitHub API responses listed in this record. “Not found in the reviewed source set” means **not established by this review**, not proof that no off-repository evidence exists.

## 4. Findings from source artifacts

### 4.1 Article XIII insertion commit

Source: [commit a53ef122f9cedbf110f30ed57ddd7ef1db6f1491](https://github.com/vaidt/aura-specification/commit/a53ef122f9cedbf110f30ed57ddd7ef1db6f1491)

- Commit message: `Add Article XIII on Genesis and Succession`.
- GitHub's commit API reports `verification.verified = true`, reason `valid`, at `2026-09-21T19:32:54Z`.
- The change modifies only `constitution/AURA_CONSTITUTION.md`, adding the Article XIII section.
- The commit does not change the Constitution version field, does not remove the `FROZEN` status, and does not itself include the RFC, Architecture Review, impact analysis, or dependent-document updates required by Article XI.
- The GitHub associated-pull-requests endpoint returned an empty list for this commit in the read-only query.

**What this establishes:** the repository contains a technically signed commit that adds Article XIII, and GitHub reports its commit signature as verified.

**What this does not establish:** compliance with the constitutional amendment procedure, the competence of the signer to amend the Constitution, or normative effectiveness.

### 4.2 Frozen Constitution and Article XI

Source: [current Constitution](https://github.com/vaidt/aura-specification/blob/main/constitution/AURA_CONSTITUTION.md)

The current file declares:

- `Version: 1.0`
- `Status: FROZEN`
- frozen content is immutable and amendments require a new version under Article XI.

Article XI says constitutional amendment requires:
1. an RFC;
2. an Architecture Review;
3. an impact analysis;
4. updates to dependent documents; and
5. approval by the Chief Architect.

The insertion commit changes the frozen file directly while retaining the v1.0 / FROZEN header. The inspected commit does not evidence the listed procedural steps. Their performance is therefore **NOT ESTABLISHED by the evidence reviewed here**. This is not a final finding that no additional evidence can exist elsewhere.

### 4.3 Genesis declaration

Source: [GENESIS_DECLARATION.txt](https://github.com/vaidt/aura-specification/blob/main/GENESIS_DECLARATION.txt)  
Source commit: [89de18afc41e79afc0259116df861928dfae8cba](https://github.com/vaidt/aura-specification/commit/89de18afc41e79afc0259116df861928dfae8cba)

The declaration says the signer converts technical ownership into constitutional Genesis Authority, enacts Article XIII, appoints Kamil Krasiński as initial Chief Architect, and grants broad authority to ratify protocol changes and authorize implementations.

GitHub's commit API reports the declaration-registration commit as `verification.verified = false`, reason `unknown_key`. This is the Git commit signature status; it is distinct from the detached SSH signature stored alongside the declaration.

The declaration's current UTF-8 payload has SHA-256:

`6b5a4c4eaa258eef27452fe6a2f2d752484ae6c88968a039b0b40ca0ac8f2bb6`

This matches the digest referenced by `AURA_M1_CLOSURE_RECORD_v1.0.md`.

#### Detached SSHSIG inspection

The detached file `GENESIS_DECLARATION.txt.sig` was parsed and its embedded Ed25519 signature bytes were independently checked against the exact declaration payload using Python's `cryptography` Ed25519 implementation.

Results:

- direct Ed25519 signature check over the reconstructed SSHSIG signed payload: **PASS**;
- public-key fingerprint calculated from the complete SSH public-key blob: `SHA256:u9HaNYWZGQYvGET5ZaX2c/V56MzL0Xo7Ilg9M1pZRwU`, matching the fingerprint claimed in the authority-binding record;
- SSHSIG inner signature-algorithm field in the retrieved file decodes to `sshoed25519`, not the standard `ssh-ed25519` identifier;
- an OpenSSH `ssh-keygen -Y verify` check could not be run in this environment.

Accordingly, the Ed25519 signature bytes validate when interpreted under the embedded Ed25519 key, but strict, standards-compliant acceptance of the complete SSHSIG envelope is **NOT ESTABLISHED**. The anomalous inner algorithm identifier must be resolved and the signature must be checked with a standards-compliant independent verifier before treating the detached signature as a conformant SSHSIG artifact.

Even a valid signature would establish a cryptographic relation between the payload and a key; it would not, by itself, establish the key holder's constitutional competence or the effectiveness of an appointment.

### 4.4 Authority and identity binding record

Source: [AUTHORITY_BINDING_RECORD_v1.1.md](https://github.com/vaidt/aura-specification/blob/main/AUTHORITY_BINDING_RECORD_v1.1.md)

The record is labelled `RATIFIED`, binds the name Kamil Krasiński to fingerprint `SHA256:u9HaNYWZGQYvGET5ZaX2c/V56MzL0Xo7Ilg9M1pZRwU`, and declares that signatures under the `aura-genesis` and `aura-governance` namespaces carry constitutive authority.

The matching fingerprint confirms internal consistency between that record and the key embedded in the Genesis signature. The public key and `allowed_signers` entry are also present in the same repository. These facts do **not** independently establish the real-world identity of the key holder or a prior, competent source granting the key constitutional authority. A record cannot establish its own authority merely by labelling itself `RATIFIED`.

### 4.5 M1 closure and P-008 status conflict

Source: [AURA_M1_CLOSURE_RECORD_v1.0.md](https://github.com/vaidt/aura-specification/blob/main/AURA_M1_CLOSURE_RECORD_v1.0.md)

The closure record claims `M1_Governance_Gate: CLOSED`, `Authority_Continuity: PROVEN`, and P-008 ratification as executed.

However, the currently inspected [P-008 Ratification Record](https://github.com/vaidt/aura-specification/blob/main/AURA_P008_RATIFICATION_RECORD_v1.0.md) declares in its header:

- `Status: READY_FOR_EXECUTION`;
- `Ratification_Status: PENDING_EXECUTION`.

Its body also labels `Normative_Effect.status: EFFECTIVE`. These declarations conflict internally and with the M1 closure record's `EXECUTED` claim. The conflict cannot be resolved by selecting the most favourable status label.

### 4.6 Current AFI authority-evidence procedure draft

Source: [AURA-AFI-AEP-001 v0.1-DRAFT](https://github.com/vaidt/aura-specification/blob/main/governance/AURA-AFI-AEP-001_FOUNDING_INSTRUMENT_AND_AUTHORITY_EVIDENCE_PROCEDURE_v0.1-DRAFT.md)

The draft explicitly declares:

- `PROPOSED · NON-CONSTITUTIVE · NOT RATIFIED`;
- `Normative Effect: NONE`;
- `Genesis Authorization: NOT GRANTED`;
- `Authority Basis: NOT PROVEN`.

It states that a cryptographic signature, repository ownership, a Markdown status, or a hash is not by itself proof of competence. It requires a primary competence basis, a source-to-holder authority chain, and independent review.

This AFI document is itself a draft, so it is not treated here as a binding decision. Its declared status is nevertheless an unresolved conflict with the later closure record's claims of proven authority continuity and completed M1 closure.

## 5. Evidence disposition

| Question | Assessment | Basis / limitation |
|---|---|---|
| Was Article XIII added to the repository? | **ESTABLISHED** | Commit `a53ef12` adds the section to the Constitution. |
| Does GitHub report the Article XIII commit signature as verified? | **YES** | API reports `verified: true`, reason `valid`. |
| Was the decision intentional according to the requester? | **RECORDED** | Explicit clarification on 2026-10-11; this record is not a signed author attestation. |
| Is the Article XI amendment procedure evidenced in the inspected sources? | **NOT ESTABLISHED** | Required steps are not evidenced by the insertion commit or source set reviewed here. |
| Does the Genesis declaration match the SHA-256 referenced by the closure record? | **YES** | Exact payload digest matches the recorded digest. |
| Is the Genesis SSHSIG cryptographically valid? | **PARTIAL** | Raw Ed25519 signature bytes validate; the SSHSIG inner algorithm identifier is anomalous, and standards-compliant envelope validation remains outstanding. |
| Is the key holder's constitutional competence independently established? | **NOT PROVEN** | No independently sourced primary basis of competence was established in this review. |
| Is Article XIII's normative effectiveness established? | **NOT ESTABLISHED** | Procedure is not evidenced; authority and closure records conflict. |
| Is M1 status resolved by this record? | **NO** | This record has no authority to close or reopen M1; source claims remain conflicted. |

## 6. Overall conclusion

The review supports a narrow conclusion: **Article XIII was deliberately introduced as a repository change, and the requester now confirms that the intent was deliberate.** This does not establish that Article XIII was validly enacted or became normatively effective.

On the material inspected, constitutional amendment compliance and the primary basis of Genesis authority remain **NOT ESTABLISHED**. The source corpus also contains unresolved conflicting claims about authority continuity and P-008 execution. The Genesis detached signature requires standards-compliant SSHSIG validation because the retrieved envelope contains an anomalous algorithm identifier, even though the raw Ed25519 signature bytes validate.

This conclusion is not a finding that the amendment is definitively void; evidence outside the inspected source set may exist. Until competent independent review resolves the conflicts, this record must not be used as evidence that Article XIII is effective, that authority continuity is proven, or that M1 is closed.

## 7. Required follow-up evidence

1. Obtain the author's separately signed confirmation of the intent statement above; verify the identity-to-key binding through a channel independent of this repository.
2. Re-verify all relevant detached signatures with a standards-compliant OpenSSH implementation and resolve the `sshoed25519` identifier in the Genesis signature envelope.
3. Locate and bind the primary authority source, competent issuer, holder, scope, effective date, and present validity. Do not use the Genesis declaration or identity-binding record as their own independent authority basis.
4. Locate the RFC, Architecture Review, impact analysis, dependent-document updates, and approval evidence required by Article XI—or formally record which items remain unavailable.
5. Reconcile the M1 closure record, P-008 record, AFI draft, and any other records claiming conflicting authority or ratification states through an independently competent process.

## 8. Record integrity and status

This document is a draft prepared for review on a non-main branch. Its repository presence, commit, or eventual merge would establish neither ratification nor constitutional effect.

No history rewrite, Constitution edit, status change, or M1 closure/reopening is authorized by this record.

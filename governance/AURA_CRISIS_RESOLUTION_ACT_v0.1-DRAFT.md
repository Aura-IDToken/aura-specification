# AURA Crisis Resolution Act — Draft for Human Decision

**Document ID:** AURA-CRA-001  
**Version:** 0.1-DRAFT  
**Status:** PROPOSED · NON-CONSTITUTIVE · NOT RATIFIED  
**Normative effect:** NONE  
**Effective authorization:** NOT AUTHORIZED  
**Prepared:** 2026-10-17  
**Preparation baseline:** `vaidt/aura-specification@8f0cd6be94a68a3728e69a1d21d49237c9d8bd05`  
**Related act:** `AURA-STAGE3-AUTH-001`  
**Related review package:** [`vaidt/aura-specification#32`](https://github.com/vaidt/aura-specification/pull/32) — draft, not merged

> This is a proposed crisis-containment and governance-recovery act. It cannot establish its own authority, bypass G1, ratify Article XIII, or authorise AURA-STAGE3-AUTH-001 merely by being signed or registered.

## 1. Purpose

This draft proposes a controlled response to the unresolved G1 authority and constitutional-procedure conflict. It separates (a) technical containment and evidence preservation, (b) determination of the competent human decision-maker, and (c) any later constitutive decision.

The proposed outcome is **resolution of the authority-evidence gap without circular self-authorisation**. It is not a shortcut around the gap.

## 2. Baseline and state

At preparation, the recorded baseline is:

- `vaidt/aura-specification` main: `8f0cd6be94a68a3728e69a1d21d49237c9d8bd05`.
- `AURA-STAGE3-AUTH-001` remains proposed in [`vaidt/Kt-ry-Program#21`](https://github.com/vaidt/Kt-ry-Program/pull/21); its effective authorization remains `NOT AUTHORIZED`.
- The Genesis-signature and Article XIII source-audit evidence package is submitted for review in [`vaidt/aura-specification#32`](https://github.com/vaidt/aura-specification/pull/32), currently a draft PR and not merged.
- The reviewed API snapshot reported repository `main` branch protection disabled. That is a technical governance-control weakness, not proof of constitutional competence.

This draft does not amend those states.

## 3. Authority limitation — prerequisite to any ratification

**Competent ratifier for this Act: NOT ESTABLISHED.**

A GitHub repository owner, administrator, funder, original code author, cryptographic key holder, Protocol Custodian, and Chief Architect are distinct role or capability claims. Some may be held by the same person, but their equivalence and the scope of authority cannot be inferred from account ownership, repository permissions, contribution history, a key fingerprint, or a declaration that asserts its own authority.

The ratifier must first provide primary evidence establishing:
1. the source instrument or rule from which the ratifier's competence originates;
2. the issuer and its competence to establish that instrument;
3. the identity of the current holder, including any relevant succession or delegation;
4. the scope of authority covering this specific crisis act;
5. the effective date, current validity, and any constraints or revocation conditions.

The source must be independent of the disputed Article XIII chain, unless a separate competent review has already resolved that chain. A document signed by the disputed root key can prove a cryptographic relationship to that key; by itself, it cannot independently prove that the key holder possessed the constitutional authority being asserted.

If no such primary basis can be established, this Act remains non-constitutive and the state remains `G1 = NOT PROVEN / BLOCKED`.

## 4. Proposed interim containment measures

Subject to ordinary repository permissions and applicable independent approval, the following actions may be considered as technical containment only:

1. Preserve immutable references to the current `main`, `integration`, PR heads, source artefacts, detached signatures, logs, and repository-control settings.
2. Do not force-push, rewrite or delete the historical Genesis, Constitution, Authority Binding, M1, or decision records.
3. Keep `AURA-STAGE3-AUTH-001` in proposal state; do not merge PR #21 or start runtime implementation while G1 remains blocked.
4. Keep evidence reports and proposed crisis-resolution material on isolated branches and draft PRs until independently reviewed.
5. Request repository administrators to review branch protection on `main`, require PR review and suitable status checks, and record the resulting settings. These are repository integrity controls only; they do not grant protocol authority.
6. Preserve disagreements and unresolved findings as explicit `OPEN / BLOCKED / NOT ESTABLISHED` items rather than rewriting past records to present the conflict as resolved.

No item in this section authorises protocol implementation, normative changes, production credential use, release, or retrospective ratification.

## 5. Required independent review

The review must be split into two clearly scoped workstreams.

### 5.1 Technical and cryptographic review

Review the exact byte-level results in `GENESIS_SIGNATURE_VERIFICATION_RECORD.md` from the proposed evidence package. The review must distinguish:
- preimage integrity and SSHSIG mathematical verification;
- canonical OpenSSH `ssh-keygen -Y verify` interoperability, which was not run in the preparing environment;
- cryptographic implementation diversity (Python `cryptography`, OpenSSL CLI, and Node.js `crypto` are not three separate machines or necessarily three independent primitive implementations);
- signing-time evidence, revocation status, and identity binding, which are separate claims.

The reviewer must independently reproduce relevant checks from frozen source artefacts and issue a signed or otherwise attributable report naming exact refs, digests, tools and results.

### 5.2 Constitutional and authority review

An independent reviewer must assess the primary authority source, the adoption process for Article XIII, the frozen-v1.0/Article-XI conflict, the claimed Genesis appointment, and the M1 closure assertions. The reviewer must explicitly state the source and limits of their own competence. This Act must not designate the reviewer as an authority merely by naming them.

The review must issue one of:
- `AUTHORITY BASIS PROVEN WITHIN STATED SCOPE`;
- `AUTHORITY BASIS NOT PROVEN`;
- `CONFLICTED / UNRESOLVED`.

A technical signature PASS cannot substitute for this disposition.

## 6. Prohibited transitions

This proposed Act does **not** authorise any “bypass” of G1 or the governance evidence requirements. In particular, it MUST NOT be used to:

- set Article XIII to `RATIFIED` or `EFFECTIVE` without the required competence and adoption evidence;
- retroactively validate a modification to the frozen Constitution v1.0;
- resolve the M1 conflict by choosing the favourable status field alone;
- treat repository owner/admin permissions as automatic constitutional sovereignty;
- set `AURA-STAGE3-AUTH-001` to `RATIFIED` or `S3-DESIGN AUTHORIZED`;
- merge PR #21 while the required authority and ratification conditions are unmet;
- authorise runtime implementation, normative protocol changes, conformance claims, release, or production operations.

A technical GitHub bypass is not a governance decision. A new act that declares itself empowered to override the disputed authority source would repeat the same circularity the audit identified.

## 7. Proposed decision sequence

The proposed state sequence is:

`CRISIS CONTAINMENT`
→ `PRIMARY AUTHORITY EVIDENCE COLLECTED`
→ `INDEPENDENT AUTHORITY REVIEW`
→ `AUTHORITY BASIS PROVEN WITHIN SCOPE`
→ `COMPETENT HUMAN DECISION`
→ `ACT-SPECIFIC RATIFICATION AND REGISTRATION`
→ `G1 DISPOSITION RECORDED`

The sequence stops at the first unmet condition. If the primary authority basis is not established, the outcome is:

`G1 = NOT PROVEN / BLOCKED`  
`AURA-STAGE3-AUTH-001 = PROPOSED`  
`EFFECTIVE AUTHORIZATION = NOT AUTHORIZED`

If a competent basis is independently established, the authorised human decision-maker may choose a bounded remedy. Any prospective reconstitution of AURA governance must be treated as a separate act with its own authority basis, adoption mechanism, effective date, scope, and versioning. It must not be represented as proof that disputed historical acts were valid when originally recorded.

## 8. Act-specific ratification record — intentionally pending

- Ratifying issuer and capacity: `PENDING — COMPETENCE NOT ESTABLISHED`
- Primary authority instrument: `PENDING`
- Independent reviewer and report reference: `PENDING`
- Exact approved Act revision and SHA-256: `PENDING`
- Decision: `PENDING — ACCEPT / REJECT / RETURN FOR EVIDENCE`
- Signature type, namespace and verification result: `PENDING`
- Registration repository, path and commit: `PENDING`
- Effective date and conditions: `PENDING`
- G1 disposition after review: `PENDING`

No fields may be completed by inference from a Markdown status, successful CI run, account privileges, or the presence of this draft.

## 9. Current determination

`AURA-CRA-001`: `PROPOSED · NON-CONSTITUTIVE · NOT RATIFIED`  
`G1`: `NOT PROVEN / BLOCKED`  
`AURA-STAGE3-AUTH-001`: `PROPOSED`  
`Effective authorization`: `NOT AUTHORIZED`

**End of draft.**

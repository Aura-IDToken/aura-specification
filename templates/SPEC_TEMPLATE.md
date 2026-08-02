# SPEC Template

Use this template to create a SPEC document derived from an ARC baseline.

---
ID: SPEC-XXX
Title: Short title
Status: DRAFT / REVIEW / APPROVED / FROZEN
Owner: Role / Name (Protocol Custodian / Chief Architect)
Date: YYYY-MM-DD

Authority:
- Derived from: ARC-YYY (list all source ARC IDs)
- Aggregated into: APS-001 (umbrella Protocol Specification)

Purpose:
A concise statement of what this SPEC formalizes and why.

Normative Requirements:
- REQ-001: MUST ...
- REQ-002: MUST NOT ...
- REQ-003: SHOULD ...
- REQ-004: MAY ...

Traceability (ARC → SPEC):
- ARC-YYY: brief mapping note (which parts of the arc translate to which requirements)

Related APS references:
- APS-000, APS-200, APS-300 (as applicable)

Acceptance criteria:
- The SPEC must be accepted by the Protocol Custodian.
- All normative requirements must be individually traceable to ARC baseline elements.

Change history:
- YYYY-MM-DD Owner: created

---

Notes:
- SPEC documents are normative. Keep text precise and unambiguous. Avoid design or implementation guidance that would belong in Reference Implementation or ADR.

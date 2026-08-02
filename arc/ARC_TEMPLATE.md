# ARC Template

Use this template to author an Architecture Baseline (ARC) document.

---
ID: ARC-XXX
Title: Short title of the architecture baseline
Status: ACCEPTED
Owner: Organization / Role / Name
Date: YYYY-MM-DD

Summary:
A concise summary of the architectural baseline and its scope.

Rationale:
Explain why this baseline was accepted and the problems it addresses.

Impact on SPEC:
List SPEC sections (SPEC-001 …) that implement or depend on this ARC. Use the mapping format defined in compliance/arc_to_spec_mapping.yaml.

Scope & Non-goals:
Define the architecture scope and explicit non-goals.

Related ADRs / References:
- ADR-xxx if relevant
- Links to external documents

Acceptance Evidence:
Describe what counts as acceptance for this ARC (meeting minutes, signatures, board resolution).

Change History:
- YYYY-MM-DD Owner: created

---

Notes:
- ARC documents are immutable records of an accepted baseline. Do not edit an ACCEPTED ARC; instead create a new ARC revision with a new ID and link to the superseded one.

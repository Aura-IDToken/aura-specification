# Traceability Matrix

Document ID: COMP-TM-002  
Version: 1.0-DRAFT  
Authority: APS-900 §7  
Last Review: 2026-09-26

---

> **Status**: This matrix is in DRAFT. Entries marked NOT VERIFIED indicate that the traceability link exists in specification but has not been validated against a running implementation.

---

## Matrix

| Constitution Principle | APS Section | INV | ENT | CONF | FIX | EVID Type | RI-PY Status | RI-RS Status |
|------------------------|-------------|-----|-----|------|-----|-----------|-------------|-------------|
| Determinism by Design | APS-001 §2 | INV-001 | ENT-002, ENT-003 | CONF-001 | FIX-001 | EVID-CORE | NOT VERIFIED | NOT VERIFIED |
| Determinism by Design | APS-001 §2 | INV-002 | ENT-003, ENT-005, ENT-006 | CONF-002 | FIX-001 | EVID-CORE, EVID-CHAIN | NOT VERIFIED | NOT VERIFIED |
| Explicit over Implicit | APS-200 §4, §8 | INV-003 | All ENT | CONF-003 | CANONICAL-001, CANONICAL-002 | EVID-CORE | PARTIAL | PARTIAL |
| Immutable Evidence | APS-300 §3 | INV-004 | ENT-005 | CONF-004 | FIX-001 | EVID-CORE | NOT VERIFIED | NOT VERIFIED |
| Evidence Before Trust | APS-300 §11 | INV-005 | ENT-005, ENT-006 | CONF-005 | FIX-001 | EVID-CORE | NOT VERIFIED | NOT VERIFIED |
| Determinism by Design | APS-001 §2 | INV-006 | ENT-003, ENT-005 | CONF-006 | FIX-001 | EVID-CORE | NOT VERIFIED | NOT VERIFIED |
| Determinism by Design | APS-001 §3 | INV-007 | ENT-002, ENT-003 | CONF-011 | FIX-INV-007 | EVID-CORE | NOT VERIFIED | NOT VERIFIED |
| Fail Closed by Default | APS-001 §8 | INV-008 | ENT-001 | CONF-007 | FIX-ERROR (TODO) | EVID-CORE | NOT VERIFIED | NOT VERIFIED |
| Version Everything | APS-000 §9, APS-200 §9 | INV-009 | ENT-002, ENT-003, ENT-005, ENT-006, ENT-008 | CONF-008 | FIX-COMPAT-001 | EVID-CORE | NOT VERIFIED | NOT VERIFIED |
| Conformance Before Features | APS-400 | INV-010 | — | CONF-009 | all FIX | EVID-CONF | NOT VERIFIED | NOT VERIFIED |
| Evidence Before Trust | APS-300 §7 | INV-011 | ENT-005 | CONF-010 | FIX-001 | EVID-CORE | NOT VERIFIED | NOT VERIFIED |
| Documentation is Product | APS-300 | INV-012 | ENT-007 | CONF-012 | FIX-INV-012 | EVID-AUDIT | NOT VERIFIED | NOT VERIFIED |
| Determinism by Design | APS-001 §5 | INV-013 | ENT-004 | CONF-013 | FIX-INV-013 | EVID-CORE | NOT VERIFIED | NOT VERIFIED |
| Conformance Before Features | APS-500 | INV-014 | — | CONF-014 | FIX-INV-014 | EVID-CONF | NOT VERIFIED | NOT VERIFIED |
| Explicit over Implicit | APS-000 §4, APS-200 §4 | INV-015 | All ENT | CONF-015 | FIX-INV-015 | EVID-CORE | NOT VERIFIED | NOT VERIFIED |

---

## Legend

| Status | Meaning |
|--------|---------|
| PASS | Verified against implementation |
| FAIL | Verification failed |
| NOT VERIFIED | Not yet verified |
| TODO | Blocking prerequisite missing |
| PARTIAL | Partially implemented or verified |

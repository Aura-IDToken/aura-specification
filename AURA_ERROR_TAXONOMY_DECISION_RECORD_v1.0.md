# AURA PROTOCOL DECISION RECORD: ERROR TAXONOMY
Artifact_ID: AURA-DEC-ERR-v1.0
Domain: Error Classification & Taxonomy Governance

Status: READY_FOR_EXECUTION
Ratification_Status: PENDING_EXECUTION

Authority:
  role: Chief Architect
  holder: Kamil Krasiński

Constitutive_Basis:
  artifact: AURA GENESIS BOOTSTRAPPING DECLARATION
  effective_date: 2026-09-24
  declaration_sha256: 6b5a4c4eaa258eef27452fe6a2f2d752484ae6c88968a039b0b40ca0ac8f2bb6
  signer_fingerprint: SHA256:u9HaNYWZGQYvGET5ZaX2c/V56MzL0Xo7Ilg9M1pZRwU
  canonical_repository_ref: vaidt/aura-specification@e7f2128

Effective_Date: 2026-09-24

Supersedes:
  - informal proposals and unratified drafts of error codes for Wave 1

---

### 1. Klasyfikacja Kodów Diagnostycznych (Wave 1 Scope)

Niniejszym ustala się status kodów diagnostycznych w architekturze ewaluacyjnej Wave 1:

1. **Aktywne Kody Błędów (ACTIVE):**
   * `E_SCHEMA_INVALID`: Naruszenie kontraktu składniowego JSON Schema Draft-07 (powiązane z A-026).
   * `E_EMPTY_SET`: Naruszenie zasady pustego zbioru wektorów/asercji (powiązane z A-016).
   * `E_DIGEST_MISMATCH`: Niezgodność skrótu kryptograficznego payloadu.
   * `E_SIGNATURE_INVALID`: Błąd weryfikacji kryptograficznej podpisu.
   * `E_CANONICALIZATION_ERROR`: Błąd procesu kanonikalizacji danych wejściowych.
   * `E_UNSUPPORTED_ALGORITHM`: Algorytm kryptograficzny spoza profilu bazowego.

2. **Kody Odroczone (RESERVED_FOR_FUTURE_WAVE):**
   * Kody dotyczące zaawansowanego cyklu życia, unieważnień certyfikatów i łańcuchów delegacji (np. `E_REVOCATION_*`, `E_DELEGATION_*`) uzyskują status `RESERVED`. 
   * Kody te nie mogą być raportowane jako wymagane asercje w suite testowym Wave 1.

---

### 2. Skutek Normatywny i Wdrożeniowy

* **Normative_Effect:**
  * status: EFFECTIVE
  * scope:
    - P-012 Conformance Error Mapping
    - Wave 1 Test Suite Diagnostic Expectations
* **Implementation_Authorization:**
  * status: NOT_GRANTED
  * basis: separate formal authorization upon final M1 closure review


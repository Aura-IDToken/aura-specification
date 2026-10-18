# AURA PROTOCOL IMPLEMENTATION AUTHORIZATION: WAVE 1
Artifact_ID: AURA-AUTH-W1-v1.2
Domain: Implementation Migration & Schema Harmonization Authorization

Status: EXECUTED
Execution_Status: AUTHORIZED
Repository_Mutation: PERMITTED_IN_SCOPE

Authority:
  role: Chief Architect
  holder: Kamil Krasiński
  binding_artifact: AUTHORITY_BINDING_RECORD_v1.1.md (ref: vaidt/aura-specification@6028ceda886db062488b29578d573f5826968d32)

Baseline_Reference:
  repository: vaidt/aura-specification
  branch: main
  commit: 6028ceda886db062488b29578d573f5826968d32

Constitutive_Prerequisites:
  - Genesis_Authority:
      artifact: GENESIS_DECLARATION.txt
      ref: vaidt/aura-specification@89de18afc41e79afc0259116df861928dfae8cba
      sha256: 6b5a4c4eaa258eef27452fe6a2f2d752484ae6c88968a039b0b40ca0ac8f2bb6
  - Identity_Binding:
      artifact: AUTHORITY_BINDING_RECORD_v1.1.md
      ref: vaidt/aura-specification@6028ceda886db062488b29578d573f5826968d32
      verification_exit_code: 0
  - Governance_Consolidation:
      artifact: AURA_M1_CLOSURE_RECORD_v1.0.md
      ref: vaidt/aura-specification@6028ceda886db062488b29578d573f5826968d32
      status: CLOSED
      verification_exit_code: 0

Consolidated_Decisions_Semantics:
  P008:
    historical_state: PENDING_EXECUTION_at_original_registration
    current_state: EXECUTED_VIA_M1_CONSOLIDATION
  NOT_APPLICABLE:
    historical_state: PENDING_EXECUTION_at_original_registration
    current_state: EXECUTED_VIA_M1_CONSOLIDATION
  ERROR_TAXONOMY:
    historical_state: PENDING_EXECUTION_at_original_registration
    current_state: EXECUTED_VIA_M1_CONSOLIDATION

Target_Wave: WAVE_1

---

### 1. Execution Trigger

Przejście ze stanu `NOT_YET_AUTHORIZED` do stanu `EXECUTED` następuje wyłącznie pod warunkiem łącznego spełnienia kryteriów:
* **Wymagane:**
  1. Złożenie ważnego podpisu SSH (Ed25519) w przestrzeni `aura-governance` przez posiadacza klucza Root Identity.
  2. Rejestracja pliku dekretu wraz z plikiem `.sig` w repozytorium `vaidt/aura-specification`.
  3. Jawna zmiana flagi `Execution_Status` na `EXECUTED` w zatwierdzonym akcie.
* **Zabronione:**
  - Uznanie samego podpisu lokalnego za skuteczną autoryzację.
  - Implikowanie autoryzacji wdrożeniowej bez zarejestrowanego rekordu.

---

### 2. Authorized Targets & Permitted Paths (Single Repository Scope)

Autoryzacja po wykonaniu uprawnia wyłącznie do modyfikacji ściśle wyznaczonych ścieżek w jednym repozytorium:

* **Repository:** `vaidt/aura-specification`
* **Branch:** `main`
* **Baseline Commit:** `6028ceda886db062488b29578d573f5826968d32`
* **Allowed Paths:**
  - `fixtures/schemas/` (integracja NOT_APPLICABLE w kanonicznych schematach Draft-07)
  - `specification/APS-001_PROTOCOL_SPECIFICATION.md` (harmonizacja semantyki wyników z P-008)
  - `fixtures/corpus/` (dostosowanie wektorów testowych do algebry P-008)
  - `fixtures/core/` (wektory ewaluacyjne)

*Wszelkie inne repozytoria implementacyjne podlegają odrębnemu dekretowi i są wyłączone z niniejszego aktu.*

---

### 3. Prohibited Mutations

Zabrania się pod rygorem natychmiastowego `AUTHORIZATION_VIOLATION`:
1. Zmiany `protocol_version` (pozostaje `unspecified` lub w bieżącej wartości bazowej).
2. Modyfikacji plików historycznych i konstytutywnych (`GENESIS_DECLARATION.*`, `AUTHORITY_BINDING_RECORD_*`, `AURA_M1_CLOSURE_RECORD_*`, dotychczasowych rekordów decyzyjnych).
3. Implementacji funkcji oznaczonych jako `RESERVED_FOR_FUTURE_WAVE` (np. procedury unieważnień certyfikatów, obsługa łańcuchów delegacji).
4. Modyfikacji modelu władzy ustrojowej (Authority Model).
5. Modyfikacji jakichkolwiek plików spoza listy `Allowed Paths`.

---

### 4. Binary Acceptance Criteria

Migracja inżynieryjna zostanie uznana za pomyślnie zrealizowaną wyłącznie po spełnieniu wszystkich warunków binarnych:
* `AC-01`: Wszystkie zmodyfikowane schematy w `fixtures/schemas/` przechodzą walidację JSON Schema Draft-07 (PASS).
* `AC-02 (SROF Definition)`: Każdy syntaktycznie niepoprawny wektor testowy generuje dokładnie jeden błąd pierwotny w tablicy błędów (`errors.length == 1`), dokładnie jeden kod z aktywnej taksonomii Wave 1 oraz brak błędów kaskadowych.
* `AC-03`: Zestawy wektorów zgodności GV-V-001 (algebra agregacji P-008) oraz GV-V-002 (walidacja schematowa) uzyskują status PASS.
* `AC-04`: Pusty pakiet asercji/wektorów zwraca wynik FAIL (A-016).
* `AC-05`: Dane wejściowe naruszające schemat blokują ewaluację semantyczną (A-026).
* `AC-06 (Path Scope Audit)`: Weryfikacja poleceniem `git diff --name-only 6028ceda HEAD` wykazuje, że 100% zmodyfikowanych plików mieści się w `Allowed Paths`.

---

### 5. Rollback Procedure

W przypadku wystąpienia `AUTHORIZATION_VIOLATION` lub niespe
ienia kryteriów akceptacji:
* **Procedura dozwolona:**
  - Utworzenie commitu wycofującego (`git revert <commit_sha>`).
  - Stan docelowy: czyste przywrócenie drzewa do commita `6028ceda886db062488b29578d573f5826968d32`.
  - Jeżeli `git revert` zakończy się konfliktem niemożliwym do automatycznego rozwiązania, proces przechodzi w stan `ROLLBACK_FAILED` i zatrzymuje wszelkie działania do decyzji Chief Architecta.
* **Procedury bezwzględnie zabronione:**
  - `git push --force`.
  - Przepisywanie historii gałęzi zdalnej (`git rebase`, `git reset --hard` na remote).
  - Usuwanie artefaktów dowodowych lub logów weryfikacji.

---

### 6. Independent Conformance Separation

Niniejsza autoryzacja stanowi wyłącznie zezwolenie na migrację inżynieryjną w wyzna

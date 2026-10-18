# AURA — WAVE 1 — CONTRACT CLOSURE ADDENDUM v1

## ERRATA / CONTRACT RECONCILIATION AMENDMENT v1.1

**Artifact:** `AURA_WAVE1_CONTRACT_CLOSURE_ERRATA_v1.1.md`  
**Artifact Class:** CONTRACT RECONCILIATION / ERRATA  
**Effect:** NON-CONSTITUTIVE  
**Purpose:** Record technical reconciliation only  
**Storage Repository:** `vaidt/aura-specification`  
**Target Artifacts Repository:** `vaidt/Aura-Conformance-Kit`  
**Date:** 2026-09-24  
**Status:** TECHNICAL RECONCILIATION · NON-CONSTITUTIVE  
**Governance:** PROPOSED / NOT RATIFIED

> Navigation: this errata is non-constitutive; see [`GOVERNANCE_STATUS_INDEX.md`](GOVERNANCE_STATUS_INDEX.md) for the current routing of governance/status records.

## 1. Purpose & Scope

Niniejsza errata stanowi techniczny dokument rekoncyliacyjny, którego celem jest usunięcie rozbieżności pomiędzy tekstowym opisem kontraktu **AURA — WAVE 1 — Contract Closure Addendum v1** a jego zwalidowaną maszynowo reprezentacją w ramach schematów JSON Schema Draft-07.

Zakres erraty jest ściśle ograniczony do dostosowania powierzchni interfejsu CLI, semantyki wyników weryfikacji (`verification_result`) oraz wyznaczenia operacyjnego podzbioru taksonomii błędów. Dokument rejestruje wyłącznie techniczny stan architektoniczny oparty na empirycznym dowodzie meta-walidacji.

Errata nie ustanawia nowej normy protokołu, nie rozstrzyga kompetencji governance i nie stanowi aktu ratyfikacyjnego.

## 2. Terminology Mapping — Superseding Technical Clarification

W toku implementacji schematów doszło do zmiany identyfikatorów semantycznych względem dokumentu źródłowego. Ustanawia się następujące mapowanie zastępujące na poziomie roboczej reprezentacji schematowej:

| Termin w źródłowym Addendum v1 | Termin w zwalidowanym Schemacie | Charakter Zmiany |
|---|---|---|
| `MATCH` | `MATCHED` | Potwierdzone mapowanie kontraktowe |
| `MISMATCH` | `MISMATCHED` | Potwierdzone mapowanie kontraktowe |
| `REJECTED` | `REJECTED` | Zachowany |
| `UNDETERMINED` | `UNDETERMINED` | Zachowany |
| `NOT_APPLICABLE` | Brak w schemacie | OPEN — luka kontraktowa względem źródła |

Decyzja dotycząca wycofania lub pełnej integracji statusu `NOT_APPLICABLE` w W1 pozostaje **OPEN** i wymaga odrębnego rozstrzygnięcia kontraktowego.

Niniejsza errata nie usuwa `NOT_APPLICABLE` ze źródłowego kontraktu i nie uznaje go za deprecated.

## 3. Fixture / Result / Exit-code Relationship — Superseding Technical Clarification

Zastępuje się pierwotną powierzchnię CLI określoną w Addendum:

```
0 = PASS/MATCH
1 = FAIL/MISMATCH
2 = SCHEMA ERROR
```

nową, zweryfikowaną macierzą relacyjną, która rozdziela kod wyjścia procesu od merytorycznego wyniku weryfikacji:

| `verification_result` | `process_exit_code` | `expected_error_code` |
|---|---:|---|
| `MATCHED` | 0 | `null` |
| `MISMATCHED` | 0 | `E_DIGEST_MISMATCH` lub `E_CANONICAL_BYTES_MISMATCH` |
| `REJECTED` | 0 lub 1 | `E_SCHEMA_INVALID` lub `E_FIXTURE_NOT_FOUND` |
| `UNDETERMINED` | 2 | `E_INTERNAL_VERIFIER_ERROR` |

Powyższa macierz stanowi **working technical contract** zweryfikowany przez aktualny fixture/meta-validation corpus. Nie stanowi samodzielnego aktu normatywnego.

## 4. Phase-1 Operational Error Taxonomy — Active Subset

W ramach aktualnego kontraktu walidacyjnego (fixture/meta-validation contract), aktywny podzbiór kodów błędów obejmuje:

- `E_SCHEMA_INVALID`
- `E_DIGEST_MISMATCH`
- `E_CANONICAL_BYTES_MISMATCH`
- `E_FIXTURE_NOT_FOUND`
- `E_INTERNAL_VERIFIER_ERROR`

Pozostałe identyfikatory z **Error Taxonomy v1** pozostają zdefiniowane w kontrakcie źródłowym i nie są niniejszą erratą ani usuwane, ani uznawane za deprecated.

Ich ewentualne wycofanie, zmiana znaczenia lub aktywacja w kolejnym profilu wykonawczym wymaga odrębnego rozstrzygnięcia kontraktowego.

## 5. Validation Evidence & Scope of Proof

Architektura schematowa została poddana walidacji maszynowej z wykorzystaniem:

```
jsonschema.Draft7Validator
FormatChecker
```

**Dowód:**

```
VALIDATION_REPORT_DRAFT7_PATCHED.json
```

**SHA-256:**

```
07a81b0baa43f439d648554cd87d8e2c8b2997006ea320c6987bd402039c3a53
```

**Wynik:**

```
45/45 expected behavior matches
0 expected-behavior mismatches
```

### Additional Validation Observation

The 45/45 corpus validity criterion **PASSED**.

A separate **Single Reason of Failure** criterion did **NOT** fully pass. The validation report records 33 negative vectors, of which 27 produce exactly one schema error and 6 produce multiple schema errors.

Therefore:

> The 45/45 result SHALL NOT be interpreted as proof that every negative vector fails for exactly one schema reason.

Wynik 45/45 potwierdza wyłącznie zgodność oczekiwanej i rzeczywistej ważności instancji względem zastosowanych schematów JSON Schema Draft-07 w określonym korpusie.

Nie dowodzi on:

- kompletności semantycznej całego kontraktu W1, w tym obsługi `NOT_APPLICABLE`;
- poprawności implementacji niezależnego weryfikatora;
- poprawności rzeczywistych kodów wyjścia CLI w systemie operacyjnym;
- spełnienia Evidence Completeness Gate;
- poprawności provenance, deterministic replay lub integralności obliczonych artefaktów;
- Protocol Conformance;
- Implementation Authorization.

## 6. Schema Alignment & Non-normative Effect Statement

This errata reconciles the textual Wave 1 contract description with the technically validated schema and fixture semantics.

Dla zachowania pełnej audytowalności dowodów ustanawia się formalną barierę poziomów semantycznych:

```
schema validity
    ≠
runtime verification result
    ≠
test status
    ≠
process exit semantics
    ≠
evidence status
    ≠
normative authorization
```

W szczególności techniczny `PASS` korpusu nie oznacza automatycznie `MATCHED` jako wyniku protokołowego ani nie stanowi decyzji governance.

This errata does not constitute normative ratification, does not establish authority continuity, and does not grant implementation authorization.

## 7. Relationship to Source Addendum

Niniejsza errata pozostaje dokumentem rekoncyliacyjnym względem **AURA — WAVE 1 — Contract Closure Addendum v1.0**.

W zakresie objętym sekcją 3 powyższa macierz stanowi proponowane, superseding technical clarification dla roboczej powierzchni CLI.

W zakresie Error Taxonomy sekcja 4 definiuje wyłącznie aktywny podzbiór Phase-1 operational contract i nie usuwa identyfikatorów istniejących w źródłowej taksonomii.

W zakresie `NOT_APPLICABLE` źródłowy status pozostaje nierozstrzygnięty na poziomie aktualnego schematu i wymaga odrębnej decyzji.

## 8. Final Governance & Engineering Status

```
A2 META-VALIDATION GATE = PASS / CLOSED

A2 OVERALL             = REASSESSMENT REQUIRED / OPEN

Single Reason of Failure = NOT FULLY SATISFIED
NOT_APPLICABLE           = OPEN
Implementation Auth.     = NOT GRANTED
Normative Effect         = NONE
M1                       = OPEN / BLOCKED
Governance               = PROPOSED / NOT RATIFIED
```

## 9. Disposition

Niniejszy dokument może zostać zarejestrowany jako **PROPOSED / NON-CONSTITUTIVE technical reconciliation artifact**.

Rejestracja artefaktu nie jest równoznaczna z:

- ratyfikacją kontraktu;
- ustanowieniem authority continuity;
- zamknięciem M1;
- udzieleniem implementation authorization;
- ustanowieniem normative protocol change.

**End of Errata v1.1**

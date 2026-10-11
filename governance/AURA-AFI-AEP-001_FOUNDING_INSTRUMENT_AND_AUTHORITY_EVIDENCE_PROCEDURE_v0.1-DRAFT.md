# AURA Founding Instrument and Authority Evidence Procedure

Document ID: AURA-AFI-AEP-001<br>
Version: 0.1-DRAFT<br>
Status: PROPOSED · NON-CONSTITUTIVE · NOT RATIFIED<br>
Normative Effect: NONE<br>
Genesis Authorization: NOT GRANTED<br>
Authority Basis: NOT PROVEN  
Intended Use: Przegląd organizacyjny, prawny i dowodowy

---

## 1. Cel

Niniejszy dokument definiuje proponowaną procedurę ustalenia i udokumentowania pierwotnej kompetencji do ustanowienia korzenia zaufania AURA (Genesis).

Celem procedury jest ustalenie:

1. czy istnieje pierwotna, wiążąca podstawa kompetencji do ustanowienia początkowego governance AURA;
2. kto jest uprawniony do podjęcia tej decyzji;
3. jaki zakres kompetencji przysługuje tym osobom lub organom;
4. jakie dowody potwierdzają ich tożsamość, umocowanie i skuteczność podjętej decyzji;
5. czy materiał dowodowy może zostać niezależnie zweryfikowany przed rozpoczęciem ceremonii Genesis.

Dokument nie ustanawia samodzielnie kompetencji żadnej osoby ani organu. Nie nadaje kluczom kryptograficznym uprawnień, których istnienie nie zostało wcześniej wykazane.

## 2. Status i granice

Niniejszy projekt ma charakter przygotowawczy i niekonstytutywny.

Nie stanowi:

- aktu ustanawiającego Genesis;
- ratyfikacji Konstytucji AURA ani kontraktu protokołu;
- dowodu ciągłości wcześniejszego umocowania;
- powołania kustoszy Genesis;
- zgody na wygenerowanie lub uruchomienie klucza głównego;
- autoryzacji zmian normatywnych lub migracji implementacji.

Wszystkie czynności wykonywane na podstawie niniejszego projektu przed formalnym zatwierdzeniem należy traktować jako przygotowanie techniczne, analizę dowodową lub przegląd organizacyjny.

## 3. Zasady dowodowe

Procedura opiera się na następujących rozróżnieniach:

```text
EXISTS ≠ REACHABLE ≠ CURRENT ≠ AUTHORITATIVE ≠ NORMATIVE ≠ EFFECTIVE
```

Istnienie dokumentu, jego dostępność w repozytorium, aktualność, autorytatywność, moc normatywna i skuteczność stanowią odrębne twierdzenia wymagające odrębnego uzasadnienia.

```text
EXHAUSTED ≠ RESOLVED
```

Zakończenie poszukiwania dostępnych dowodów nie oznacza rozwiązania luki kompetencyjnej.

Ponadto:

- podpis kryptograficzny dowodzi związku podpisanej treści z określonym kluczem, ale nie ustanawia samodzielnie kompetencji prawnej ani organizacyjnej;
- skrót kryptograficzny potwierdza integralność wskazanych danych względem danego skrótu, lecz nie dowodzi ich prawdziwości ani autorytatywności;
- status zapisany w Markdown nie jest samodzielnym dowodem zatwierdzenia;
- obecność dokumentu w repozytorium, jego właściciel lub historia commitów nie stanowią same przez się podstawy kompetencji;
- dowód czasu nie zastępuje dowodu tożsamości, umocowania ani prawidłowości procedury decyzyjnej.

## 4. Zakres wymaganych ustaleń

Przed zatwierdzeniem aktu ustanawiającego Genesis należy przeprowadzić i udokumentować poniższe kontrole.

### 4.1. Pierwotna podstawa kompetencji

Należy wskazać konkretny akt, umowę, uchwałę lub inną podstawę organizacyjną bądź prawną, z której wynika kompetencja do ustanowienia początkowego governance AURA.

Dla każdego dokumentu należy ustalić:

- pochodzenie i źródło;
- kompetencję jego wystawcy;
- tożsamość stron lub osób podejmujących decyzję;
- zakres i warunki udzielonego umocowania;
- datę ustanowienia oraz warunki skuteczności;
- aktualny status oraz ewentualne zmiany, wygaśnięcie lub unieważnienie.

Nie wolno zastępować brakującej podstawy kompetencji dokumentem, który jedynie deklaruje własną autorytatywność.

### 4.2. Ciągłość umocowania

Należy odtworzyć łańcuch:

```text
Źródło kompetencji → właściwy wystawca → aktualny posiadacz kompetencji → zakres → data wejścia w życie → aktualna ważność
```

Każde przejście wymaga dowodu. Jeśli któregokolwiek przejścia nie można wykazać, wynik pozostaje nierozstrzygnięty.

### 4.3. Zakres decyzji ustanawiającej

Należy ustalić, czy kompetentny organ ma prawo:

- ustanowić początkową strukturę governance AURA;
- określić sposób powołania kustoszy Genesis;
- zatwierdzić zasady kworum i delegowania uprawnień;
- określić procedurę rotacji i unieważniania kluczy;
- zdefiniować procedurę późniejszych zmian w korzeniu zaufania.

Kompetencji tych nie wolno domniemywać z ogólnego tytułu, funkcji technicznej ani wcześniejszego udziału w projekcie.

## 5. Procedura przygotowania i oceny dowodów

### Etap 1 — Inwentaryzacja

Należy zebrać dokumenty potencjalnie stanowiące pierwotną podstawę kompetencji, bez przypisywania im z góry statusu autorytatywnego.

Każdy artefakt powinien mieć identyfikator, źródło, wersję lub datę, skrót treści oraz opis ograniczeń dowodowych.

### Etap 2 — Ocena źródła

Dla każdego artefaktu należy ocenić, czy wykazano jego pochodzenie, kompetencję wystawcy, zakres i skuteczność.

Raport wtórny może wskazywać miejsce poszukiwania pierwotnego źródła, lecz nie zastępuje tego źródła.

### Etap 3 — Rekonstrukcja kompetencji

Należy utworzyć macierz przypisującą każdemu twierdzeniu o kompetencji konkretny dowód pierwotny i wynik jego weryfikacji.

Brak dowodu należy zapisać jako `NOT PROVEN`, a sprzeczne lub niejednoznaczne dowody jako `CONFLICTED` albo `UNRESOLVED`.

### Etap 4 — Przegląd niezależny

Materiał musi zostać poddany niezależnemu przeglądowi organizacyjnemu oraz prawnemu odpowiednio do faktycznej formy i podstawy działania projektu.

Recenzent powinien mieć możliwość odtworzenia wniosków bez polegania wyłącznie na deklaracji autora dokumentacji.

### Etap 5 — Decyzja o dopuszczalności ustanowienia Genesis

Dopiero po pozytywnym rozstrzygnięciu kwestii kompetencji można przygotować odrębny akt ustanawiający Genesis i przejść do procedury jego formalnego zatwierdzenia.

Niniejszy dokument nie przesądza, kto jest uprawniony do podjęcia tej decyzji. To musi wynikać z dowodów ustalonych w poprzednich etapach.

## 6. Pakiet dowodowy

Docelowy pakiet powinien przechowywać co najmniej:

- pierwotne dokumenty ustanawiające kompetencję;
- dowody tożsamości i umocowania sygnatariuszy w zakresie koniecznym do przeprowadzenia weryfikacji;
- dokumentację ciągłości kompetencji;
- rejestr konfliktów, braków i nierozstrzygniętych kwestii;
- raport niezależnego przeglądu;
- manifest wskazujący dokładne wersje i skróty zatwierdzanych dokumentów;
- podpisy i dowody ich weryfikacji, jeżeli są wymagane;
- dowody czasu i publikacji, jeśli zostaną zastosowane;
- maszynowo czytelny raport końcowy.

Dostęp do danych osobowych i informacji poufnych należy ograniczyć zgodnie z właściwymi wymaganiami prawnymi i organizacyjnymi. Publiczny manifest może zawierać skróty i identyfikatory, podczas gdy poufne dowody źródłowe pozostają w kontrolowanym depozycie.

## 7. Wyniki procedury

Procedura powinna generować jednoznaczny wynik.

| Status | Znaczenie |
|---|---|
| `EVIDENCE-COLLECTION` | Trwa gromadzenie i klasyfikacja materiału. |
| `AUTHORITY-BASIS-NOT-PROVEN` | Brak wystarczającego dowodu pierwotnej kompetencji. |
| `AUTHORITY-BASIS-CONFLICTED` | Materiał zawiera sprzeczności wymagające rozstrzygnięcia. |
| `INDEPENDENT-REVIEW-PENDING` | Materiał oczekuje na niezależny przegląd. |
| `AUTHORITY-BASIS-VERIFIED` | Niezależnie potwierdzono określoną podstawę, zakres i ciągłość kompetencji. |
| `GENESIS-ESTABLISHMENT-ELIGIBLE` | Spełniono warunki wstępne do rozpoczęcia odrębnej, formalnej procedury ustanowienia Genesis. |

`AUTHORITY-BASIS-VERIFIED` nie oznacza automatycznie `GENESIS-APPROVED`. Oznacza wyłącznie, że określona podstawa kompetencji została wykazana w ustalonym zakresie.

`GENESIS-ESTABLISHMENT-ELIGIBLE` również nie ustanawia Genesis. Dopuszcza jedynie przejście do osobnej procedury zatwierdzenia.

## 8. Kryteria blokujące

Procedura musi zakończyć się wynikiem blokującym, jeżeli:

- nie można wskazać pierwotnej podstawy kompetencji;
- tożsamość lub kompetencja sygnatariusza pozostaje niewykazana;
- zakres umocowania nie obejmuje decyzji o ustanowieniu Genesis;
- istnieje nierozstrzygnięty konflikt pomiędzy dowodami;
- dowody integralności lub podpisy są nieprawidłowe;
- wynik zależy wyłącznie od tekstowego statusu dokumentu;
- mechanizm weryfikacji może zostać zastąpiony lub pominięty bez niezależnie autoryzowanej kontroli.

Wyniku blokującego nie wolno zastępować akceptacją na podstawie samego upływu czasu, zakończenia inwentaryzacji ani pomyślnego wyniku testów technicznych.

## 9. Warunki zatwierdzenia niniejszej procedury

Przed nadaniem procedurze jakiegokolwiek skutku normatywnego należy niezależnie wykazać:

1. kto ma kompetencję do jej zatwierdzenia;
2. na jakiej podstawie kompetencja ta wynika;
3. czy procedura pozostaje zgodna z nadrzędnymi, skutecznie ustanowionymi dokumentami AURA;
4. jaki formalny mechanizm nada jej skuteczność;
5. jak będzie weryfikowana integralność, autentyczność i aktualność zatwierdzonej wersji.

Do czasu wykazania powyższych warunków status pozostaje:

```text
PROPOSED · NON-CONSTITUTIVE · NOT RATIFIED · NORMATIVE EFFECT NONE
```

## 10. Stan końcowy

Niniejszy dokument definiuje procedurę dochodzenia do dowodu kompetencji. Nie rozstrzyga samodzielnie, kto jest aktualnie uprawniony do ustanowienia Genesis.

Dopiero pierwotny dowód kompetencji, pozytywny niezależny przegląd i odrębnie zatwierdzony akt mogą stanowić podstawę rozpoczęcia ceremonii Genesis.

Obowiązująca reguła bezpieczeństwa: jeśli umocowanie nie zostało wykazane, ceremonia Genesis pozostaje zablokowana.

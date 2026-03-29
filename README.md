# Linked List, Hypermarket a TreeSort

Projekt je zameraný na vztvorenie zreťazených zoznamov (Linked List), ich implementáciu do projektu Hypermarket a analýzu zoradzovacieho algoritmu TreeSort.

## Obsah
- [Linked List](#linked_list)
- [Výhody a nevýhody linked listu](#vyhody_a_nevyhody_linked_listu)
- [Tree Sort analýza](#tree_sort_analyza)

## Linked List
Linked List je dynamické usporiadanie, ktoré obsahuje „odkaz“ na štruktúru s nasledujúcimi prvkami. 

Je to súbor štruktúr, ktoré nie sú zoradené podľa ich fyzickej polohy v pamäti (ako pole), ale podľa logických odkazov, ktoré sú uložené priamo v údajoch každej štruktúry.

Viazený zoznam je ďalší spôsob, ako zhromaždiť podobné údaje. Na rozdiel od poľa však nie sú jeho prvky uložené v po sebe idúcich miestach v pamäti. Skladá sa z uzlov, ktoré sú prepojené pomocou ukazovateľov.

## Výhody a nevýhody linked listu
Výhody:

	•	Dynamický: Rastie a zmenšuje sa za behu, nepotrebuješ určiť veľkosť vopred.
	•	Žiadna strata pamäte: Používa len toľko pamäte, koľko treba.
	•	Rýchle pridávanie/odstraňovanie: Len zmeníš link, nič neposúvaš.
	•	Flexibilný: Prvky nie sú na po sebe idúcich miestach.
	•	Dobré pre veľké dáta: Ľahko sa prispôsobí.
  
Nevýhody:

	•	Viac pamäte: Každý uzol potrebuje odkaz na ďalší.
	•	Pomalé prehľadávanie: Musíš ísť od začiatku, žiadny priamy prístup.
	•	Žiadne cúvanie: V jednosmernom nemôžeš ísť dozadu.
	•	Žiadny náhodný prístup: Nemôžeš skočiť na konkrétny prvok.
	•	Zložitejšia implementácia: Viac kódu ako pri poli.
	•	Nevhodné pre malé dáta: Pole je lepšie.

## Tree Sort analýza
V meraniach som zistila, že Tree Sort správne „sedí“ iba pri náhodnom zozname (random), kde časové nároky výsledne vyzerali podobne teoretickej zložitosti .

Random Up (kolísavo rastúci zoznam)

Pri zozname typu random up, kde prvky sa väčšinou zvyšovali, ale s menšími výkyvmi, bol namierený čas približne dvojnásobný oproti očakávanému správaniu. Vysvetlením je, že vstup bol skoro zoradený, a strom sa čiastočne vytvoril ako „strmé“ jednostranné vetvenie (napr. viac prvkov v pravom podstrome), čím sa reálne zväčšila priemerná výška stromu a zvyšil sa počet rekurzívnych volaní.

Random Down (kolísavo klesajúci zoznam)

Podobný efekt som pozorovala aj pri random down, kde sa prvky väčšinou znižovali. Aj tu bol čas přibližne dvojnásobný oproti predpokladu, pretože vkladanie sa výraznejšie vychýlilo na jednu stranu stromu (napr. ľavé vetvenie). Strom sa tak opäť stal menej vyváženým, čo spôsobilo dlhšie vkladanie a prechod, hoci algoritmus naďalej teoreticky zostal v triede .
Kombináciou skoro zoradeného vstupu a naturálnej nerovnomernosti pri vytváraní stromu sa teda v meraniach pre random up a random down ukázalo zhoršené správanie, aj keď Tree Sort sa v týchto prípadoch stále umiestnil pred jednoduchšími algoritmami ako Bubble a Insert sort.

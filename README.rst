========
Sejmy.py
========

Moduł pythona ułatwiajacy korzystanie z API sejmometr.pl
(http://sejmometr.pl/api/api)

Struktura
===============

Posiedzenia::

    Posiedzenie.lista() - Lista obiektow typu ''Posiedzenie''

    Posiedzenie(<id>) - ''Posiedzenie'' o id = <id>

    posiedzenie.id - Numer ID posiedzenia

    posiedzenie.info.tytul - Tytuł posiedzenia
    posiedzenie.info.data_start - Data rozpoczęcia posiedzenia
    posiedzenie.info.data_stop - Data zakończenia posiedzenia
    posiedzenie.info.ilosc_punktow - Ilość punktów porządku dziennego, rozpatrywanych na posiedzeniu
    posiedzenie.info.ilosc_glosowan - Ilość głosowań, przeprowadzonych podczas posiedzeniu

    posiedzenie.punkty - Lista obiektów typu ''Punkt''
    posiedzenie.dni - Lista obiektów typu ''Dzien''
    posiedzenie.rozpatrywania - Lista obiektów typu ''Rozpatrywanie''
    posiedzenie.wystapienia - Lista obiektów typu ''Wystapienie''
    posiedzenie.glosowania - Lista obiektów typu ''Glosowanie''


Punkty::

    Punkt.lista() - Lista obiektów typu ''Punkt''

    Punkt(<id>) - Punkt porządku dziennego o nr = <id>

    punkt.id - Numer ID punktu porządku dziennego

    punkt.info.nr - Numer porządkowy punktu
    punkt.info.tytul - Tytuł punktu
    punkt.info.posiedzenie_id - Numer ID posiedzenia
    punkt.info.posiedzenie - obiekt typu ''Posiedzenie''
    punkt.info.typ_id - Typ punktu
    punkt.info.druk_id - Numer ID druku, będącego przedmiotem punktu
    punkt.info.druk - obiekt typu ''Druk'', będący przedmiotem punktu
    punkt.info.druk_akcja_id - Typ podjętych akcji dotyczących druku
    punkt.info.glosowanie_id - Numer ID głosowania nad drukiem
    punkt.info.glosowanie - Obiekt typu ''Glosowanie'', będący głosowaniem nad drukiem

    punkt.rozpatrywania - Lista obiektów typu ''Rozpatrywanie'' dla danego punktu porządku dziennego
    punkt.druki - Lista obiektów typu ''Druk'' związanych z punktem porządku dziennego


Dni posiedzeń::

    Dzien.lista() - Lista obiektów typu ''Dzien''

    Dzien(<id>) - Dzień posiedzenia sejmu o numerze = <id>

    dzien.id - Numer ID dnia posiedzenia sejmu

    dzien.info.posiedzenie_id - Numer ID posiedzenia
    dzien.info.posiedzenie - Obiekt typu ''Posiedzenie''
    dzien.info.data - Data
    dzien.info.time_start - Czas rozpoczęcia obrad <type: str>
    dzien.info.time_stop - Czas zakończenia obrac <type: str>
    dzien.info.dokument_id - Numer ID dokumentu zawierącego stenogram obrad
    dzien.info.dokument - Obiektu typu ''Dokument''

    dzien.rozpatrywania - Lista obiektów typu ''Rozpatrywanie''
    dzien.wystapienia - Lista obiektów typu ''Wystapienie''
    dzien.glosowania - Lista obiektów typu ''Glosowanie''
    

Rozpatrywania::

    Rozpatrywanie.lista() - Lista obiektów typu ''Rozpatrywanie''

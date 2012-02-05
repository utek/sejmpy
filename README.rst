========
Sejmy.py
========

Moduł pythona ułatwiajacy korzystanie z API sejmometr.pl
(http://sejmometr.pl/api/api)

Przykład użycia
===============

Posiedzenia::
    import sejmometr

    lista_posiedzen = sejmometr.Posiedzenie.lista()

    posiedzenie = lista_posiedzien[0]

    print posiedzenie.tytul
    print posiedzenie.ilosc_punktow
    print len(posiedzenie.lista_punktow)

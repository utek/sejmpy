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
    print u"Ilość posiedzeń:", len(lista_posiedzen)

    for posiedzenie in lista_posiedzen:
        print u"Tytuł: ", posiedzenie.info.tytul
        print u"Data rozpoczęcia: ", posiedzenie.info.data_start
        print u"Data zakończenia: ", posiedzenie.info.data_stop
        print u"Liczba punktów porządku dziennego: ", posiedzenie.info.ilosc_punktow
        print u"Liczba głosowań: ", posiedzenie.info.ilosc_glosowan
        print "---"
        for punkt in posiedzenie.punkty:
            print u"\tPunkt nr: ", punkt.info.nr
            print u"\tTytuł: ", punkt.info.tytul.encode("utf-8")
            print u"\tTyp: ", punkt.info.typ_id
            print "\t---"

# -*- coding: utf-8 -*-

import sejmometr

lista_posiedzen = sejmometr.Posiedzenie.lista()
print(("Ilość posiedzeń:", len(lista_posiedzen)))

for posiedzenie in lista_posiedzen:
    print(("Tytuł: ", posiedzenie.info.tytul))
    print(("Data rozpoczęcia: ", posiedzenie.info.data_start))
    print("Data zakończenia: ", posiedzenie.info.data_stop)
    print("Liczba punktów porządku dziennego: ", posiedzenie.info.ilosc_punktow)
    print("Liczba głosowań: ", posiedzenie.info.ilosc_glosowan)
    print("---")
    for punkt in posiedzenie.punkty:
        print("\tPunkt nr: ", punkt.info.nr)
        print("\tTytuł: ", punkt.info.tytul.encode("utf-8"))
        print("\tTyp: ", punkt.info.typ_id)
        print("\t---")

================
Posiedzenie
================

.. currentmodule:: sejmometr

.. autoclass:: Posiedzenie(id)
    :members: lista

    Klasa opisująca Posiedzenia sejmu
    
    :param id: Numer id posiedzenia
    :type id: int

    .. attribute:: id

        Numer ID posiedzenia
        <``int``>

    .. attribute:: info

        Obiekt zawierający informacje o posiedzeniu.
        Posiada następujące atrybuty:

        .. attribute:: tytul

            Tytuł posiedzenia.
            <``unicode``>

        .. attribute:: data_start

            Data rozpoczęcia posiedzenia.
            <``datetime.date``>

        .. attribute:: data_stop

            Data zakończenia posiedzenia.
            <``datetime``>

        .. attribute:: ilosc_punktow

            Ilość punktów porządku dziennego, rozpatrywanych na posiedzeniu.
            <``int``>

        .. attribute:: ilosc_glosowan

            Ilość głosowań, przeprowadzonych podczas posiedzeniu.
            <``int``>

    .. attribute:: punkty

        Lista obiektów typu :class:`Punkt`

    .. attribute:: dni

        Lista obiektów typu :class:`Dzien`

    .. attribute:: rozpatrywania

        Lista obiektów typu :class:`Rozpatrywanie`

    .. attribute:: wystapienia

        Lista obiektów typu :class:`Wystapienie`

    .. attribute:: glosowania

        Lista obiektów typu :class:`Glosowanie`

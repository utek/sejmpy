================
Rozpatrywanie
================

.. currentmodule:: sejmometr

.. class:: Rozpatrywanie(id)

    .. attribute:: info

        Informacje o rozpatrywaniu:

        .. attribute:: posiedzenie_id

            Numer ID posiedzenia.
            <``int``>

        .. attribute:: posiedzenie

            Obiekt typu :class:`Posiedzenie` o id = :attr:`posiedzenie_id`.

        .. attribute:: dzien_id

            Numer ID dnia posiedzenia.
            <``int``>

        .. attribute:: dzien

            Obiekt typu :class:`Dzien` o id = :attr:`dzien_id`.

        .. attribute:: punkt_id

            Numer ID punktu porządku dziennego.
            <``int``>

        .. attribute:: punkt

            Obiekt typu :class:`Punkt` o id = :attr:`punkt_id`

        .. attribute:: tytul

            Tytuł rozpatrywania.
            <``unicode``>

        .. attribute:: ilosc_wystapien

            Ilość wystąpień
            <``int``>

        .. attribute:: ilosc_glosowan

            Ilość głosowań
            <``int``>

        .. attribute:: time_start

            Czas rozpoczęcia rozpatrywania.
            <``unicode``>

        .. attribute:: time_stop

            Czas zakończenia rozpatrywania.
            <``unicode``>

    .. attribute:: wystapienia

        Lista obiektów typu :class:`Wystapienie`

    .. attribute:: glosowania

        Lista obiektów typu :class:`Glosowanie`

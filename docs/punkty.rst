================
Punkt
================

.. currentmodule:: sejmometr

.. class:: Punkt(id)

    Klasa opisująca Punkt porządku dziennego dla określonego posiedzenia.

    :param id: Numer id punktu
    :type id: int

    .. classmethod:: lista()

        Zwraca listę obietków typu :class:`Punkt` dla wszystkich posiedzeń sejmu

    .. attribute:: id

        Numer id punktu porządku dziennego.
        <``int``>

    .. attribute:: info

        Obiekt zawierający informacje o punkcie porządku dziennego.
        Posiada następujace atrybuty.

        .. attribute:: nr

            Numer porządkowy punktu.
            <``int``>

        .. attribute:: tytul

            Tytuł punktu.
            <``unicode``>

        .. attribute:: posiedzenie_id

            Numer id posiedzenia.
            <``int``>

        .. attribute:: posiedzenie

            Obiekt typu :class:`Posiedzenie` o id = :attr:`posiedzenie_id`.

        .. attribute:: typ_id

            Typ punktu.
            <``int``>

        .. attribute:: druk_id

            Numer id druku, będącego przedmiotem punktu.
            <``int``>

        .. attribute:: druk

            Obiekt typu :class:`Druk` o id = :attr:`druk_id`, będący przedmiotem punktu.

        .. attribute:: druk_akcja_id

            Typ podjętych akcji dotyczących druku.
            <``int``>

        .. attribute:: glosowanie_id

            Numer id głosowania nad drukiem.
            <``int``>

        .. attribute:: glosowanie

            Obiekt typu :class:`Glosowanie` o id = :attr:`glosowanie_id`, będący
            głosowaniem nad punktem.


    .. attribute:: rozpatrywania

        Lista obiektów typu :class:`Rozpatrywanie` dla danego punktu porządku
        dziennego

    .. attribute:: druki

        Lista obiektów typu :class:`Druk` związanych z punktem porządku dziennego

================
Wystąpienie
================

.. currentmodule:: sejmometr

.. class:: Wystapienie(id)

    Klasa opisująca wystąpenia w ramach posiedzenia

    :param id: Numer id dnia wystąpienia
    :type id: int

    .. attribute:: info

        Obiekt zawierający informacje o wystąpieniu

        .. attribute:: posiedzenie_id

            Numer ID posiedzenia
            <``int``>

        .. attribute:: posiedzenie

            Obiekt typu :class:`Posiedzenie` o id = :attr:`posiedzenie_id`

        .. attribute:: dzien_id

            Numer id dnia posiedzenia
            <``int``>

        .. attribute:: dzien

            Obiekt typu :class:`Dzien` o id = :attr:`dzien_id`

        .. attribute:: punkt_id

            Numer id punktu porządku dziennego
            <``int``>

        .. attribute:: punkt

            Obiekt typu :class:`Punkt` o id = :attr:`punkt_id`

        .. attribute:: rozpatrywanie_id

            Numer id rozpatrywania
            <``int``>

        .. attribute:: rozpatrywanie

            Obiekt typu :class:`Rozpatrywanie` o id = :attr:`rozpatrywanie_id`

        .. attribute:: mowca_funkcja_id

            Numer id funkcji, w jakiej występuje mówca
            <``int``>

        .. attribute:: mowca_id

            Numer id mówcy
            <``int``>

        .. attribute:: posel_id

            Numer id posła.

            .. note::
                Dostępne tylko gdy mówca jest również posłem

        .. attribute:: posel

            Obiekt typu :class:`Posel` o id = :attr:`posel_id`.

            .. note::
                Dostępne tylko gdy mówca jest również posłem

        .. attribute:: time_start

            Czas rozpoczęcia wystąpienia.
            <``datetime``>

        .. attribute:: time_stop

            Czas zakończenia wystąpienia
            <``datetime``>


    .. attribute:: tekst

        Tekst wystąpienia.
        <``unicode``>

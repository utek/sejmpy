================
Dzień
================

.. currentmodule:: sejmometr

.. class:: Dzien(id)

    Klasa opisująca dni posiedzeń

    :param id: Numer id dnia posiedzenia
    :type id: int

    .. attribute:: info

        Obiekt zawierający informacje o dniu

        .. attribute:: posiedzenie_id

            Numer ID posiedzenia

        .. attribute:: posiedzenie

            Obiekt typu :class:`Posiedzenie` o id = :attr:`posiedzenie_id`

        .. attribute:: data

            Data <``datetime``>

        .. attribute:: time_start

            Czas rozpoczęcia obrad.
            <``unicode``>

        .. attribute:: time_stop

            Czas zakończenia obrad.
            <``unicode``>

        .. attribute:: dokument_id

            Numer ID dokumentu zawierącego stenogram obrad.
            <``int``>

        .. attribute:: dokument

            Obiektu typu :class:`Dokument` o id = :attr:`dokument_id`

    .. attribute:: rozpatrywania

        Lista obiektów typu :class:`Rozpatrywanie`

    .. attribute:: wystapienia

        Lista obiektów typu :class:`Wystapienie`

    .. attribute:: glosowania

        Lista obiektów typu :class:`Glosowanie`

====================
Kluby parlamentarne
====================

.. currentmodule:: sejmometr

.. autoclass:: Klub

    .. attribute:: info

        Obiekt zawierający informacje o punkcie porządku dziennego.
        Posiada następujace atrybuty:

        .. attribute:: id

            Numer id klubu
            <``int``>

        .. attribute:: nazwa

            Nazwa klubu parlamentarnego
            <``unicode``>

        .. attribute:: skrot

            Skrót nazwy.
            <``unicode``>

========================
Mówca
========================

.. autoclass:: Mowca

    .. attribute:: info

        .. attribute:: id

            Numer id mówcy.
            <``int``>

        .. attribute:: nazwa

            Imię i nazwisko mówcy.
            <``unicode``>

        .. attribute:: posel_id

            Numer id posła.
            <``int``>

            .. note::

                Tylko jeżeli mówca jest także posłem

        .. attribute:: posel

            Obiekt typu :class:`Posel` o id = :attr:`posel_id`

            .. note::

                Tylko jeżeli mówca jest także posłem


===============
Komisje semowe
===============

.. autoclass:: Komisja

    .. attribute:: info

        .. attribute:: id

            Numer id komisji.
            <``int``>

        .. attribute:: nazwa

            Nazwa komisji sejmowej.
            <``unicode``>

        .. attribute:: kod

            Kod. <``unicode``>

        .. attribute:: kontakt

            Dane kontaktowe.
            <``unicode``>

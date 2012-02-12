==============
Dokumenty
==============

.. currentmodule:: sejmometr

.. class:: Dokument(id)

    Klasa opisująca dokumenty

    :param id: Numer id druku
    :type id: int

    .. attribute:: info

        Zwraca obiekt typu :class:`Info` zawierający następujące atrybuty:

        .. attribute:: url

            Adres url pliku zawierającego dokument.
            <``unicode``>

        .. attribute:: scribd_id

            Numer id dokumentu w http://scribd.com
            <``int``>

        .. attribute:: scribd_access_key

            Klucz dostępu do dokumentu w http://scribd.com

    .. attribute:: tekst

        Treść dokumentu.
        <``unicode``>

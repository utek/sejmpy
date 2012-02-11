==============
Druk
==============

.. currentmodule:: sejmometr

.. class:: Druk(id)

    Klasa opisująca druki sejmowe

    :param id: Numer id druku
    :type id: int

    .. attribute:: nr

        Numer druku.
        <``unicode``>

    .. attribute:: tytul

        Tytuł druku.
        <``unicode``>

    .. attribute:: opis

        Opis druku.
        <``unicode``>

    .. attribute:: dokument_id

        Numer id dokumentu druku.
        <``int``>

    .. attribute:: dokument

        Obiekt klasy :class:`Dokument` o id = :attr:`dokument_id`

    .. attribute:: typ_id

        Typ druku.
        <``int``>

        :1: projekt ustawy
        :2:  projekt uchwały
        :3:  wniosek
        :5:  inny dokument
        :6:  ratyfikacja w formie zawiadomienia
        :7:  sprawozdanie komisji
        :8:  stanowisko Senatu
        :9:  dodatkowe sprawozdanie komisji

    .. attribute:: autor_typ_id

        Określenie autora druku.
        <``int``>

        :1: Rada Ministrów
        :2: Obywatele (projekt obywatelski)
        :3: Komisje sejmowe
        :4: Senat
        :5: Posłowie (projekty poselskie)
        :6: Prezydent
        :7: Prezydium Sejmu

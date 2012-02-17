================
Poseł
================

.. currentmodule:: sejmometr

.. autoclass:: Posel(id)

    Klasa opisująca posła.

    .. attribute:: info

        .. attribute:: info

            Obiekt zawierający informacje o pośle

            .. attribute:: slug

                Fraza używana przez Sejmometr do generowania adresów
                stron profilowych posłów.
                <``unicode``>

            .. attribute:: nazwa

                Imię i nazwisko posła.
                <``unicode``>

            .. attribute:: imie

                Imię posła.
                <``unicode``>

            .. attribute:: nazwisko

                Nazwisko posła.
                <``unicode``>

            .. attribute:: data_urodzenia

                Data urodzenia posła.
                <``date``>

            .. attribute:: miejsce_urodzenia

                Miejsce urodzenia posła.
                <``unicode``>

            .. attribute:: klub_id

                Identyfikator klubu parlamentarnego, do którego należy poseł
                w danej chwili.
                <``int``>

            .. attribute:: klub

                Obiekt typu :class:`Klub` o id = :attr:`klub_id`

            .. attribute:: pkw_nr_okregu

                Numer okręgu (w nomenklaturze PKW), z którego poseł dostał się
                do Sejmu.
                <``unicode``>

            .. attribute:: pkw_liczba_glosow

                Liczba głosów, którą poseł uzyskał w wyborach.
                <``unicode``>

            .. attribute:: pkw_zawod

                Zawód posła (według informacji podanej przez posła w zgłoszeniu
                do PKW)
                <``unicode``>

        .. attribute:: wystapienia

            Lista obiektów typu :class:`Wystapienie` będacych wszystkimi
            występieniami posła

        .. attribute:: glosowania

            Lista obiektów typu :class:`Glosowanie` w których poseł miał
            obowiązek uczestniczyć

        .. attribute:: komisje

            Komisje sejmowe, do których poseł należy/należał
            Lista obiektów typu :class:`Info` zawierających następujące atrybuty:

            .. attribute:: komisja_id

                Numer id komisji.
                <``int``>

            .. attribute:: komisja

                Obiekt typu :class:`Komisja` o id = :attr:`komisja_id`

            .. attribute:: od

                Data dołączenia do komisji przez posła.
                <``date``>

            .. attribute:: do

                Data zakończenia przez posła pracy w komisji.
                <``date``>

                .. note::

                    Jeżeli poseł nie zakończył jeszcze pracy w komisji
                    atrybut ten przyjmuje wartość ``None``


        .. attribute:: osiadczenia_majatkowe

            Lista słowników zawierająćych oświadczenia majątkowe posła.
            <``[{'data': <unicode>, 'dokument_id':<int>}, ...]``>

        .. attribute:: rejestr_korzysci

            Lista słowników zawierających rejestr korzyści majątkowych posła
            <``[{'data': <unicode>, 'tytul':<unicode>, 'dokument_id':<int>}, ...]``>

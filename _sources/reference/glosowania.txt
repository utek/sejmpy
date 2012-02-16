================
Głosowanie
================

.. currentmodule:: sejmometr

.. class:: Glosowanie(id)

    Klasa opisująca głosowania w ramach posiedzenia

    :param id: Numer id głosowania
    :type id: int

    .. attribute:: info

        Obiekt zawierający informacje o głosowaniu

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

        .. attribute:: tytul

            Tytuł głosowania. <``unicode``>

        .. attribute:: nr

            Numer głosowania. <``int``>

        .. attribute:: wystapienie_id

            Numer id wystąpienia powiązanego z głosowaniem. <``int``>

        .. attribute:: wystapienie

            Obiekt typu :class:`Wystapienie` o id = :attr:`wystapienie_id`

        .. attribute:: time

            Czas głosowania. <``datetime``>

        .. attribute:: wynik

            Wynik głosowania. <``int``>
                :1: Za
                :2: Przeciw
                :3: Kworum

        .. attribute:: l

            Liczba posłów uprawnionych do wzięcia udziału w głosowaniu.
            <``int``>

        .. attribute:: g

            Liczba posłów, którzy wzieli udział w głosowaniu.
            <``int``>

        .. attribute:: wb

            Wielkość bezwzględna
            <``int``>

        .. attribute:: z

            Liczba głosów "Za"
            <``int``>

        .. attribute:: p

            Liczba głosów "Przeciw"
            <``int``>

        .. attribute:: w

            Liczba "Wstrzymań od głosu"
            <``int``>

        .. attribute:: n

            Liczba posłów, którzy nie głosowali
            <``int``>


    .. attribute:: wyniki

        Lista słowników wyników głosowania.
        <``[{'posel_id':<int>, 'klub_id':<id>, 'glos':<int>},...]``>

        **posel_id**
            Numer ID posła

        **klub_id**
            Numer ID klubu, do którego poseł należał w chwili głosowania

        **glos**
            :1: Za
            :2: Przeciw
            :3: Wstrzymał się od głosu
            :4: Nieobecny

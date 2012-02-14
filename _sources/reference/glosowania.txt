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

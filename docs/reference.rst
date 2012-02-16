=================
Struktura
=================

.. toctree::
    :maxdepth: 2

    reference/posiedzenia
    reference/punkty
    reference/dni
    reference/rozpatrywania
    reference/druki
    reference/wystapienia
    reference/glosowania
    reference/poslowie
    reference/dokumenty
    reference/kluby

.. currentmodule:: sejmometr

.. function:: get_data(url)

    Funkcja pobierająca dane z Sejmometr API. Jeżeli w systemie zainstalowana
    jest biblioteka `httplib2` funkcja ta jest równa :func:`get_data_httplib2`,
    jeżeli `httplib2` jest niedostępne to funkcja jest równa
    :func:`get_data_urllib2`.

.. function:: get_data_httplib2(url)

    Funkcja wykorzystująca :mod:`httplib2` do pobierania danych z Sejmometr API

.. function:: get_data_urllib2(url)

    Funkcja wykorzystująca :mod:`urllib2` do pobierania danych z Sejmometr API

.. autoclass:: Common
    :members:
    :private-members:

    Klasa implementująca metody i atrybuty wspólne dla pozostałych klas.

.. autoclass:: Info

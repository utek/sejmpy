# -*- coding: utf-8 -*-
from datetime import datetime
import urllib2
try:
    import json
except ImportError:
    import simplejson as json


def get_data(url, *args, **kwargs):
    response = None
    try:
        response = urllib2.urlopen(url).read()
    except Exeption as e:
        print e
    return response


class Posiedzenie(object):
    def __init__(self, id=None, *args, **kwargs):
        self.__id = id
        self.__tytul = None
        self.__data_start = None
        self.__data_stop = None
        self.__ilosc_punktow = None
        self.__ilosc_glosowan = None
        self.__count = 0
        self.__punkty = None
        self.__glosowania = None

    def __str__(self):
        return str(self.id)

    @property
    def id(self):
        return self.__id

    @property
    def tytul(self):
        if self.__tytul is None:
            self.__info()
        return self.__tytul

    @property
    def data_start(self):
        if self.__data_start is None:
            self.__info()
        return self.__data_start

    @property
    def data_stop(self):
        if self.__data_stop is None:
            self.info()
        return self.__data_stop

    @property
    def ilosc_punktow(self):
        if self.__ilosc_punktow is None:
            self.__info()
        return self.__ilosc_punktow

    @property
    def ilosc_glosowan(self):
        if self.__ilosc_glosowan is None:
            self.__info()
        return self.__ilosc_glosowan


    @staticmethod
    def lista():
        """Zwraca listę posiedzeń"""
        url = 'http://api.sejmometr.pl/posiedzenia'
        data = get_data(url)
        obj = json.loads(data)
        tab = []
        for i in obj:
            tab.append(Posiedzenie(i))
        return tab

    def __p(self, id, rest):
        if id is None:
            return None
        url = 'http://api.sejmometr.pl/posiedzenie/%s/%s'
        url = url % (id, rest)
        data = get_data(url)
        self.__count += 1
        return data

    def __info(self):
        """Podstawowe informacje o posiedzeniu"""
        obj = json.loads(self.__p(self.__id, "info"))
        self.__tytul = obj['tytul']
        self.__data_start = datetime.strptime(obj['data_start'], "%Y-%m-%d").date()
        self.__data_stop = datetime.strptime(obj['data_stop'], "%Y-%m-%d").date()
        self.__ilosc_punktow = int(obj['ilosc_punktow'])
        self.__ilosc_glosowan = int(obj['ilosc_glosowan'])
        return True

    def __call__(self):
        return self.__count

    @property
    def punkty(self):
        if self.__punkty is None:
            obj = json.loads(self.__p(self.__id, "punkty"))
            self.__punkty = []
            for elem in obj:
                self.__punkty.append(Punkt(elem))
        return self.__punkty

    @property
    def glosowania(self):
        if self.__glosowania is None:
            obj = json.loads(self.__p(self.__id, "glosowania"))
            self.__glosowania = []
            for elem in obj:
                self.__glosowania.append(Glosowanie(elem))
        return self.__glosowania


class Punkt(object):

    def __init__(self, id=None, *args, **kwargs):
        nr = kwargs.get("nr", None)
        if nr is not None:
            self.__id = nr
        else:
            self.__id = id
        self.__tytul = None
        self.__posiedzenie_id = None
        self.__typ_id = None
        self.__druk_id = None
        self.__druk_akcja_id = None
        self.__glosowanie_id = None

    @property
    def id(self):
        return self.__id
    nr = id

class Glosowanie(object):

    def __init__(self, id=None, *args, **kwargs):
        nr = kwargs.get("nr", None)
        if nr is not None:
            self.__id = nr
        else:
            self.__id = id
        self.__posiedzenie_id = None
        self.__dzien_id = None
        self.__punkt_id = None
        self.__rozpatrywanie_id = None
        self.__tytul = None
        self.__wystapienie_id = None
        self.__time = None
        self.__wynik = None
        self.__l = None #liczba posłów uprawionych do wzięcia udziału w głosowaniu
        self.__g = None # liczba posłów, którzy wzieli udział w głosowaniu
        self.__wb = None # większość bezwzględna
        self.__z = None # liczba glosów "za"
        self.__p = None # liczba głosów "przeciw"
        self.__w = None # liczba "Wstrzymań"
        self.__n = None # liczba posłów, którzy nie głosowali

    @property
    def id(self):
        return self.__id
    nr = id

if __name__ == '__main__':
    a = Posiedzenie(1)
    print a.punkty
    print a.punkty
    print a.punkty
    print a.ilosc_punktow, len(a.punkty)
    print a()


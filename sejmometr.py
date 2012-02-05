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

class Common(object):
    def _p(self, id, rest):
        if id is None:
            return None
        url = 'http://api.sejmometr.pl/%s/%s/%s'
        url = url % (self._class_._name_.lower(), id, rest)
        data = get_data(url)
        self._count += 1
        return data
    pass

    @property
    def id(self):
        return self._id
    nr = id


class Posiedzenie(Common):
    def __init__(self, id=None, *args, **kwargs):
        self._id = id
        self._tytul = None
        self._data_start = None
        self._data_stop = None
        self._ilosc_punktow = None
        self._ilosc_glosowan = None
        self._count = 0
        self._punkty = None
        self._glosowania = None

    def __str__(self):
        return str(self.id)

    @property
    def id(self):
        return self._id

    @property
    def tytul(self):
        if self._tytul is None:
            self._info()
        return self._tytul

    @property
    def data_start(self):
        if self._data_start is None:
            self._info()
        return self._data_start

    @property
    def data_stop(self):
        if self._data_stop is None:
            self.info()
        return self._data_stop

    @property
    def ilosc_punktow(self):
        if self._ilosc_punktow is None:
            self._info()
        return self._ilosc_punktow

    @property
    def ilosc_glosowan(self):
        if self._ilosc_glosowan is None:
            self._info()
        return self._ilosc_glosowan


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

    #def _p(self, id, rest):
    #    if id is None:
    #        return None
    #    url = 'http://api.sejmometr.pl/posiedzenie/%s/%s'
    #    url = url % (id, rest)
    #    data = get_data(url)
    #    self._count += 1
    #    return data

    def _info(self):
        """Podstawowe informacje o posiedzeniu"""
        obj = json.loads(self._p(self._id, "info"))
        self._tytul = obj['tytul']
        self._data_start = datetime.strptime(obj['data_start'], "%Y-%m-%d").date()
        self._data_stop = datetime.strptime(obj['data_stop'], "%Y-%m-%d").date()
        self._ilosc_punktow = int(obj['ilosc_punktow'])
        self._ilosc_glosowan = int(obj['ilosc_glosowan'])
        return True

    def __call__(self):
        return self._count

    @property
    def punkty(self):
        if self._punkty is None:
            obj = json.loads(self._p(self._id, "punkty"))
            self._punkty = []
            for elem in obj:
                self._punkty.append(Punkt(elem))
        return self._punkty

    @property
    def glosowania(self):
        if self._glosowania is None:
            obj = json.loads(self._p(self._id, "glosowania"))
            self._glosowania = []
            for elem in obj:
                self._glosowania.append(Glosowanie(elem))
        return self._glosowania


class Punkt(Common):
    def __init__(self, id=None, *args, **kwargs):
        nr = kwargs.get("nr", None)
        if nr is not None:
            self._id = nr
        else:
            self._id = id
        self._tytul = None
        self._posiedzenie_id = None
        self._typ_id = None
        self._druk_id = None
        self._druk_akcja_id = None
        self._glosowanie_id = None

class Glosowanie(Common):
    def __init__(self, id=None, *args, **kwargs):
        nr = kwargs.get("nr", None)
        if nr is not None:
            self._id = nr
        else:
            self._id = id
        self._posiedzenie_id = None
        self._dzien_id = None
        self._punkt_id = None
        self._rozpatrywanie_id = None
        self._tytul = None
        self._wystapienie_id = None
        self._time = None
        self._wynik = None
        self._l = None #liczba posłów uprawionych do wzięcia udziału w głosowaniu
        self._g = None # liczba posłów, którzy wzieli udział w głosowaniu
        self._wb = None # większość bezwzględna
        self._z = None # liczba glosów "za"
        self._p = None # liczba głosów "przeciw"
        self._w = None # liczba "Wstrzymań"
        self._n = None # liczba posłów, którzy nie głosowali


if __name__ == '__main__':
    a = Glosowanie(1)
    print a.nr

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

    def lista(self):
        """Zwraca listę posiedzeń"""
        url = 'http://api.sejmometr.pl/posiedzenia'
        data = get_data(url)
        obj = json.loads(data)
        return obj

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

    def dni(self):
        """Lista dni w ramach posiedzenia"""
        obj = json.loads(self.__p(self.__id, "dni"))
        return obj

    def projekty(self):
        """Lista projektow rozpatrywanych w ramach posiedzenia"""
        obj = json.loads(self.__p(self.__id, "projekty"))
        return obj

    def bunty(self):
        """Lista posłów, któzy zagłosowali niezgodnie z linią swoich klubów"""
        obj = json.loads(self.__p(self.__id, "bunty"))
        return obj

    def nieobecni(self):
        """Nieobecni posłowie"""
        obj = json.loads(self.__p(self.__id, "nieobecni"))
        return obj

    def __call__(self):
        return self.__count




if __name__ == '__main__':
    p = Posiedzenie(1)
    print "id:\t\t\t", p.id
    print "tytul:\t\t\t", p.tytul
    print "data start:\t\t", p.data_start
    print "data stop:\t\t", p.data_stop
    print "ilosc punktow:\t\t", p.ilosc_punktow
    print "ilosc glosowan:\t\t", p.ilosc_glosowan
    print "ilosc zapytan do api:\t", p()
    

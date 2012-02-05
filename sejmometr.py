# -*- coding: utf-8 -*-
from datetime import datetime, date
import urllib2
try:
    import json
except ImportError:
    import simplejson as json


def get_data(url, *args, **kwargs):
    response = None
    try:
        response = urllib2.urlopen(url).read()
    except Exception as e:
        print e
    return response

class Info(object):
    pass

class Common(object):
    types = {"data": date,
             "time_start":datetime,
             "time_stop":datetime,
             "tytul":unicode,
             "time":datetime,
             "nr": unicode,
             "data_start": date,
             "data_stop": date,
             }
    _count = 0
    _info = None
    @property
    def info(self):
        if self._info is None:
            self._get_info()
        return self._info

    def _get_data(self, id, rest):
        if id is None:
            return None
        url = 'http://api.sejmometr.pl/%s/%s/%s'
        url = url % (self.__class__.__name__.lower(), id, rest)
        data = get_data(url)
        self._count += 1
        return data

    def _get_info(self):
        obj = json.loads(self._get_data(self._id, "info"))
        self._info = Info()
        for k,v in obj.iteritems():
            if self.types.has_key(k):
                _type = self.types[k]
            else:
                _type = int
            val = None
            if v is not None:
                if _type is datetime:
                    try:
                        val = datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        val = unicode(v)
                elif _type is date:
                    val = datetime.strptime(v, "%Y-%m-%d").date()
                else:
                    val = _type(v)
            setattr(self._info, "%s" % k, val)
        return True

    @property
    def id(self):
        return self._id
    nr = id

    #def __getattribute__(*args):
    #    _lookup = "_%s" % args[1]
    #    try:
    #        val = object.__getattribute__(args[0], _lookup)
    #        if val is None:
    #            pass
    #    except AttributeError:
    #        val = object.__getattribute__(*args)
    #    return val


class Posiedzenie(Common):

    def __init__(self, id=None, *args, **kwargs):
        self._info = None
        self._id = id

        self._punkty = None
        self._glosowania = None
        self._dni = None
        self._wystapienia = None
        self._rozpatrywania = None

    def __str__(self):
        return str(self._id)

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

    def __call__(self):
        return self._count

    @property
    def punkty(self):
        if self._punkty is None:
            obj = json.loads(self._get_data(self._id, "punkty"))
            self._punkty = []
            for elem in obj:
                self._punkty.append(Punkt(elem))
        return self._punkty

    @property
    def glosowania(self):
        if self._glosowania is None:
            obj = json.loads(self._get_data(self._id, "glosowania"))
            self._glosowania = []
            for elem in obj:
                self._glosowania.append(Glosowanie(elem))
        return self._glosowania

    @property
    def dni(self):
        if self._dni is None:
            obj = json.loads(self._get_data(self._id, "dni"))
            self._dni = []
            for elem in obj:
                self._dni.append(Dzien(elem))
        return self._dni

    @property
    def rozpatrywania(self):
        if self._rozpatrywania is None:
            obj = json.loads(self._get_data(self._id, "rozpatrywania"))
            self._rozpatrywania = []
            for elem in obj:
                self._rozpatrywania.append(Rozpatrywanie(elem))
        return self._rozpatrywania

    @property
    def wystapienia(self):
        if self._wystapienia is None:
            obj = json.loads(self._get_data(self._id, "wystapienia"))
            self._wystapienia = []
            for elem in obj:
                self._wystapienia.append(Wystapienie(elem))
        return self._wystapienia

class Punkt(Common):
    def __init__(self, id=None, *args, **kwargs):
        self._id = id

class Glosowanie(Common):
    def __init__(self, id=None, *args, **kwargs):
        self._id = id

class Dzien(Common):
    def __init__(self, id=None, *args, **kwargs):
        self._id = id

class Rozpatrywanie(Common):
    def __init__(self, id=None, *args, **kwargs):
        self._id = id

def Wystapienie(Common):
    def __init__(self, id=None, *args, **kwargs):
        self._id = id

if __name__ == '__main__':
    lista_posiedzen = Posiedzenie.lista()
    posiedzenie = lista_posiedzen[0]
    print posiedzenie.info.tytul
    print posiedzenie.info.ilosc_punktow
    print len(posiedzenie.punkty)
    print posiedzenie()

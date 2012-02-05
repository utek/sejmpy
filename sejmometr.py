# -*- coding: utf-8 -*-

__version__ = "0.5"

import sys
from datetime import datetime, date
import urllib2
try:
    import json
except ImportError:
    import simplejson as json

def get_data(url, *args, **kwargs):
    response = None
    user_agent = "sejmpy/%s" % __version__
    headers = {"User-Agent":user_agent}
    try:
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req).read()
    except Exception as e:
        print e
    return response

class Info(object):
    pass

def get_class( cls ):
    return getattr(sys.modules[__name__], cls)

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
    _all = "common"

    @classmethod
    def lista(cls):
        "Zwraca liste obiektow"
        url = 'http://api.sejmometr.pl/%s' % cls._all
        data = get_data(url)
        obj = json.loads(data)
        tab = []
        for i in obj:
            tab.append(cls(i))
        return tab

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

    def __call__(self):
        return self._count

    def __getattr__(self, name):
        _lookup = "_%s" % name
        _class_name = "%s_class" % _lookup
        cls = getattr(self, _class_name)
        cls_ = get_class(cls)
        try:
            val = self.__getattribute__(_lookup)
            if val is not None:
                return val
        except AssertionError:
            raise AssertionError
        obj = json.loads(self._get_data(self._id, name))
        tab = []
        for elem in obj:
            tab.append(cls_(elem))
        return tab

class Posiedzenie(Common):
    _all = "posiedzenia"
    _punkty_class = "Punkt"
    _glosowania_class = "Glosowanie"
    _dni_class = "Dzien"
    _wystapienia_class = "Wystapienie"
    _rozpatrywania_class = "Rozpatrywanie"

    def __init__(self, id=None, *args, **kwargs):
        self._id = id

        self._punkty = None
        self._glosowania = None
        self._dni = None
        self._wystapienia = None
        self._rozpatrywania = None

class Punkt(Common):
    _all = "punkty"
    _rozpatrywania_class = "Rozpatrywanie"

    def __init__(self, id=None, *args, **kwargs):
        self._id = id
        self._rozpatrywania = None

class Glosowanie(Common):
    _all = "glosowania"
    def __init__(self, id=None, *args, **kwargs):
        self._id = id

class Dzien(Common):
    _all = "dni"

    _glosowania_class = "Glosowanie"
    _wystapienia_class = "Wystapienie"
    _rozpatrywania_class = "Rozpatrywanie"

    def __init__(self, id=None, *args, **kwargs):
        self._id = id
        self._glosowania = None
        self._rozpatrywania = None
        self._wystapienia = None

class Rozpatrywanie(Common):
    _all = "rozpatrywania"

    _glosowania_class = "Glosowanie"
    _wystapienia_class = "Wystapienie"

    def __init__(self, id=None, *args, **kwargs):
        self._id = id
        self._glosowania = None
        self._wystapienia = None

class Wystapienie(Common):
    _all = "wystapienia"
    def __init__(self, id=None, *args, **kwargs):
        self._id = id
        self._tekst = None

    @property
    def tekst(self):
        if self._tekst is None:
            self._tekst = unicode(self._get_data(self.id, "tekst"))
        return self._tekst


if __name__ == '__main__':
    pass

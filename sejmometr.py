# -*- coding: utf-8 -*-
__version__ = "0.7.1"

import json
import sys, re
from datetime import datetime, date


reg = re.compile("(.+)_id")

def get_data_httplib2(url, *args, **kwargs):
    response = None
    user_agent = "sejmpy/{}".format( __version__)
    headers = {"User-Agent":user_agent,
               'cache-control':'3600'}
    try:
        response, content = http.request(url, headers=headers)
    except Exception as e:
        print e
    return content.decode("utf-8")

def get_data_urllib(url, *args, **kwargs):
    response = None
    user_agent = "sejmpy/%s" % __version__
    headers = {"User-Agent":user_agent}
    try:
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req).read()
    except Exception as e:
        print e
    return response

try:
    import httplib2
    http = httplib2.Http(".sejmometr_cache")
    get_data = get_data_httplib2
except ImportError:
    import urllib2
    get_data = get_data_urllib


class Info(object):
    """Klasa pojemnik. Nie implementuje żadnych metod czy atrybutów."""
    pass


def get_class(cls):
    return getattr(sys.modules[__name__], cls)




class Common(object):
    #fix dla latwiejszej konwersji dla py3k
    str_ = unicode
    #str_ = str

    types = {"data": date,
             "time_start":datetime,
             "time_stop":datetime,
             "tytul":str_,
             "time":datetime,
             "nr": str_,
             "data_start": date,
             "data_stop": date,
             "slug":str_,
             "nazwa":str_,
             "imie":str_,
             "nazwisko":str_,
             "data_urodzenia":date,
             "miejsce_urodzenia":str_,
             "nr_okregu":str_,
             "pkw_liczba_glosow":str_,
             "pkw_zawod":str_,
             "skrot": str_,
             "od": date,
             "do": date,
             "funkcja": str_,
             }
    _count = 0
    _info = None
    _all = "common"


    @classmethod
    def lista(cls):
        "Zwraca liste obiektow"
        url = "http://api.sejmometr.pl/{}".format(cls._all)
        data = get_data(url)
        obj = json.loads(data)
        tab = []
        for i in obj:
            tab.append(cls(i))
        return tab


    @property
    def info(self):
        """obiekt typu :class:`Info` zawierający informacje o obiekcie"""
        if self._info is None:
            self._get_info()
        return self._info


    def _get_data(self, id, rest):
        """Funkcja pobiera dane z API Sejmometru"""
        if id is None:
            return None
        url_dict = {"name": self.__class__.__name__.lower(), "id": id,
                    "rest": rest}
        url = "http://api.sejmometr.pl/{name}/{id}/{rest}".format(**url_dict)
        data = get_data(url)
        self._count += 1
        obj = json.loads(data)
        return obj


    def _get_info(self):
        """Funkcja zwracająca obiekt typu :class:`Info`"""
        obj = self._get_data(self._id, "info")
        self._info = self._get_data_from_list(obj)


    def _get_data_from_list(self, list_):
        """Funkcja parsuje slownik i zwraca obiekt typu :attr:`Info`
        gdzie klucze słownika są atrybutami obiektu"""
        _info = Info()
        _cls_list = dir(sys.modules[__name__])
        for k,v in list(list_.items()):
            if k in self.types:
                _type = self.types[k]
            else:
                _type = int
            val = None
            if v is not None:
                if _type is datetime:
                    try:
                        val = datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        val = str(v)
                elif _type is date:
                    if v == "0000-00-00":
                        val = None
                    else:
                        val = datetime.strptime(v, "%Y-%m-%d").date()
                else:
                    val = _type(v)
            setattr(_info, "%s" % k, val)
            r = reg.match(k)
            if r is not None:
                _atr_name = r.groups()[0]
                _cls_name = _atr_name.capitalize()
                if _cls_name in _cls_list:
                    setattr(_info, "%s" % _atr_name, get_class(_cls_name)(val))
        return _info


    @property
    def id(self):
        return self._id
    nr = id


    def __call__(self):
        return self._count


    def __getattr__(self, name):
        if name.rfind('class') >= 0:
            raise AttributeError(name.replace("_class", "")[1:] +
                                 " does not exist")
        _lookup = "_{}".format(name)
        _class_name = "{}_class".format(_lookup)
        try:
            cls = getattr(self, _class_name)
        except RuntimeError:
            raise AttributeError
        cls_ = get_class(cls)
        try:
            val = self.__getattribute__(_lookup)
            if val is not None:
                return val
        except AttributeError:
            raise AttributeError
        obj = self._get_data(self._id, name)
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
    _druki_class = "Druk"


    def __init__(self, id=None, *args, **kwargs):
        self._id = id
        self._rozpatrywania = None
        self._druki = None


class Wynik():
    def __init__(self, data=None, *args, **kwargs):
        self.posel = Posel(data['posel_id'])
        self.klub = Klub(data['klub_id'])
        self.glos = data['glos']


class Glosowanie(Common):
    _all = "glosowania"
    _wyniki_class = "Wynik"

    def __init__(self, id=None, *args, **kwargs):
        self._id = id
        self._wyniki = None #po dopisaniu poslow uwzglednic w metodzie.


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
            self._tekst = self._get_data(self.id, "tekst")
        return self._tekst

class Druk(Common):
    _all = "druki"

    def __init__(self, id=None, *args, **kwargs):
        self._id = id

class Dokument(Common):
    def __init__(self, id=None, *args, **kwargs):
        self._id = id
        self._tekst = None

    @property
    def tekst(self):
        if self._tekst is None:
            self._tekst = self._get_data(self.id, "tekst")
        return self._tekst

class Posel(Common):
    _all = "poslowie"

    _glosowania_class = "Glosowanie"
    _wystapienia_class = "Wystapienie"

    def __init__(self, id=None, *args, **kwargs):
        self._id = id
        self._wystapienia = None
        self._glosowania = None
        self._komisje = None
        self._oswiadczenia_majatkowe = None
        self._rejestr_korzysci = None

    @property
    def rejestr_korzysci(self):
        if self._rejestr_korzysci is None:
            self._rejestr_korzysci = self._get_data(self.id, "rejestr_korzysci")
        return self._rejestr_korzysci

    @property
    def oswiadczenia_majatkowe(self):
        if self._oswiadczenia_majatkowe is None:
            self._oswiadczenia_majatkowe = self._get_data(self.id, "oswiadczenia_majatkowe")
        return self._oswiadczenia_majatkowe

    @property
    def komisje(self):
        if self._komisje is None:
            self._komisje = []
            komisje = self._get_data(self.id, "komisje")
            for obj in komisje:
                self._komisje.append(self._get_data_from_list(obj))
        return self._komisje

class Klub(Common):
    """Klasa opisująca kluby parlamentarne"""

    _all = "kluby"

    def __init__(self, id=None, *args, **kwargs):
        self._id = id


class Mowca(Common):
    """Klasa opisujaca mówcę"""

    def __init__(self, id=None, *args, **kwargs):
        self._id = id

class Komisja(Common):
    """Klasa opisująca komisje sejmowe"""

    def __init__(self, id=None, *args, **kwargs):
        self._id = id



if __name__ == '__main__':
    i = Punkt(1)
    print dir(i.info)
    print i.info.posiedzenie.id, i.info.posiedzenie.info.tytul

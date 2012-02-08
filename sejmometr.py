__version__ = "0.6"

import json
import sys
from datetime import datetime, date

import httplib2


http = httplib2.Http(".sejmometr_cache")

def get_data(url, *args, **kwargs):
    response = None
    user_agent = "sejmpy/{}".format( __version__)
    headers = {"User-Agent":user_agent}
    
    try:
        response, content = http.request(url, headers=headers)
    except Exception as e:
        print(e)
    return content.decode("utf-8")


class Info(object):
    pass


def get_class(cls):
    return getattr(sys.modules[__name__], cls)


class Common(object):
    types = {"data": date,
             "time_start":datetime,
             "time_stop":datetime,
             "tytul":str,
             "time":datetime,
             "nr": str,
             "data_start": date,
             "data_stop": date,
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
        if self._info is None:
            self._get_info()
        return self._info


    def _get_data(self, id_, rest):
        if id_ is None:
            return None
        url_dict = {"name": self.__class__.__name__.lower(), "id": id_,
                    "rest": rest}
        url = "http://api.sejmometr.pl/{name}/{id}/{rest}".format(**url_dict)
        data = get_data(url)
        self._count += 1
        return data


    def _get_info(self):
        obj = json.loads(self._get_data(self._id, "info"))
        self._info = Info()
        for k,v in list(obj.items()):
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
                    val = datetime.strptime(v, "%Y-%m-%d").date()
                else:
                    val = _type(v)
            setattr(self._info, "%s" % k, val)
        return True


    @property
    def id_(self):
        return self._id
    nr = id_


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


    def __init__(self, id_=None, *args, **kwargs):
        self._id = id_

        self._punkty = None
        self._glosowania = None
        self._dni = None
        self._wystapienia = None
        self._rozpatrywania = None


class Punkt(Common):
    _all = "punkty"
    _rozpatrywania_class = "Rozpatrywanie"
    _druki_class = "Druk"


    def __init__(self, id_=None, *args, **kwargs):
        self._id = id_
        self._rozpatrywania = None
        self._druki = None


    @property
    def info(self):
        info_ = super(Punkt, self).info
        self._info.posiedzenie = Posiedzenie(self._info.posiedzenie_id)
        self._info.glosowanie = Glosowanie(self._info.glosowanie_id)
        self._info.druk = Druk(self._info.druk_id)
        return self._info


class Glosowanie(Common):
    _all = "glosowania"
    
    def __init__(self, id_=None, *args, **kwargs):
        self._id = id_


class Dzien(Common):
    _all = "dni"

    _glosowania_class = "Glosowanie"
    _wystapienia_class = "Wystapienie"
    _rozpatrywania_class = "Rozpatrywanie"

    def __init__(self, id_=None, *args, **kwargs):
        self._id = id_
        self._glosowania = None
        self._rozpatrywania = None
        self._wystapienia = None

class Rozpatrywanie(Common):
    _all = "rozpatrywania"

    _glosowania_class = "Glosowanie"
    _wystapienia_class = "Wystapienie"

    def __init__(self, id_=None, *args, **kwargs):
        self._id = id_
        self._glosowania = None
        self._wystapienia = None


class Wystapienie(Common):
    _all = "wystapienia"
    def __init__(self, id_=None, *args, **kwargs):
        self._id = id_
        self._tekst = None

    @property
    def tekst(self):
        if self._tekst is None:
            self._tekst = str(self._get_data(self.id_, "tekst"))
        return self._tekst


class Druk(Common):
    _all = "druki"

    def __init__(self, id_=None, *args, **kwargs):
        self._id = id_


class Dokument(Common):
    def __init__(self, id_=None, *args, **kwargs):
        self._id = id_
        self._tekst = None


    @property
    def tekst(self):
        if self._tekst is None:
            self._tekst = str(self._get_data(self.id_, "tekst"))
        return self._tekst


if __name__ == '__main__':
    pass

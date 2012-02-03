# -*- coding: utf-8 -*-

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

    def lista(self):
        url = 'http://api.sejmometr.pl/posiedzenia/'
        data = get_data(url)
        obj = json.loads(data)
        return obj

    def __p(self, id, rest):
        url = 'http://api.sejmometr.pl/posiedzenia/%s/%s'
        url = url % (id, rest)
        data = get_data(url)
        return data

    def info(self, id):
        obj = json.loads(self.__p(id, "info"))
        print __name__
        return obj

    def dni(self, id):
        obj = json.loads(self.__p(id, "dni"))
        return obj

    def projekty(self, id):
        obj = json.loads(self.__p(id, "projekty"))
        return obj

    def bunty(self, id):
        obj = json.loads(self.__p(id, "bunty"))
        return obj

    def nieobecni(self, id):
        obj = json.loads(self.__p(id, "nieobecni"))
        return obj

    def __call__(self):
        return self.lista()




if __name__ == '__main__':
    p = Posiedzenie()
    print p()
    #print p.dni("YXbTY")
    #print p.info("YXbTY")
    #print p.projekty("YXbTY")
    #print p.bunty("YXbTY")
    #print p.nieobecni("YXbTY")
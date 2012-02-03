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
        """Zwraca listę posiedzeń"""
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
        """Podstawowe informacje o posiedzeniu"""
        obj = json.loads(self.__p(id, "info"))
        print __name__
        return obj

    def dni(self, id):
        """Lista dni w ramach posiedzenia"""
        obj = json.loads(self.__p(id, "dni"))
        return obj

    def projekty(self, id):
        """Lista projektow rozpatrywanych w ramach posiedzenia"""
        obj = json.loads(self.__p(id, "projekty"))
        return obj

    def bunty(self, id):
        """Lista posłów, któzy zagłosowali niezgodnie z linią swoich klubów"""
        obj = json.loads(self.__p(id, "bunty"))
        return obj

    def nieobecni(self, id):
        """Nieobecni posłowie"""
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
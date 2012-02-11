=================
Przykład użycia
=================

>>> import sejmometr
>>> lista_posiedzen = sejmometr.Posiedzenie.lista()
>>> lista_posiedzen
[<sejmometr.Posiedzenie object at 0x02A41E30>, <sejmometr.Posiedzenie object at 0x02A414D0>, <sejmometr.Posiedzenie object at 0x02A41930>, <sejmometr.Posiedzenie object at 0x02A41E70>, <sejmometr.Posiedzenie object at 0x02A41E90>, <sejmometr.Posiedzenie object at 0x02A41DD0>, <sejmometr.Posiedzenie object at 0x02A41EF0>]
>>> posiedzenie = lista_posiedzen[-1] #ostatnie posiedzenie
>>> posiedzenie
<sejmometr.Posiedzenie object at 0x02A41EF0>
>>> dir(posiedzenie)
['__call__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__','_all', '_count', '_dni', '_dni_class', '_get_data', '_get_info', '_glosowania', '_glosowania_class', '_id', '_info', '_punkty', '_punkty_class', '_rozpatrywania', '_rozpatrywania_class', '_wystapienia', '_wystapienia_class', 'id', 'info', 'lista', 'nr', 'str_', 'types']
>>> dir(posiedzenie.info)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'data_start', 'data_stop','id', 'ilosc_glosowan', 'ilosc_punktow', 'tytul']
>>> print posiedzenie.info.tytul
7
>>> print posiedzenie.info.ilosc_glosowan
200
>>> print posiedzenie.info.ilosc_punktow
2
>>> print posiedzenie.punkty
[<sejmometr.Punkt object at 0x02A2C190>, <sejmometr.Punkt object at 0x02A2C0D0>]
>>> print posiedzenie.punkty[0]
<sejmometr.Punkt object at 0x029C6BB0>
>>> punkt = posiedzenie.punkty[0]
>>> dir(punkt)
['__call__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__','_all', '_count', '_druki', '_druki_class', '_get_data', '_get_info', '_id', '_info', '_rozpatrywania', '_rozpatrywania_class', 'id', 'info', 'lista', 'nr', 'str_', 'types']
>>> punkt.info.tytul
u'Sprawozdanie Komisji Finans\xf3w Publicznych o rz\u0105dowym projekcie ustawy bud\u017cetowej na rok 2012 \u2013 trzecie czytanie'

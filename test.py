import unittest

from sejmometr import *

class TestPosiedzenia(unittest.TestCase):

    def setUp(self):
        self.p = Posiedzenie(1)

    def test_info(self):
        self.assertEqual(self.p.id, 1)
        self.assertEqual(self.p(), 0)
        from datetime import date
        d = date(2012, 1, 1)
        count = self.p()
        self.assertEqual(type(self.p.info.tytul), type(u"a"))
        self.assertEqual(type(self.p.id), type(1))
        self.assertEqual(type(self.p.info.data_start), type(d))
        self.assertEqual(type(self.p.info.data_stop), type(d))
        self.assertEqual(type(self.p.info.ilosc_punktow), type(1))
        self.assertEqual(type(self.p.info.ilosc_glosowan), type(1))
        #sprawdzenie czy tylko jedno zapytanie do api
        self.assertEqual(count+1, self.p())

    def test_punkty(self):
        self.assertEqual(self.p.info.ilosc_punktow, len(self.p.punkty))
        self.assertNotEqual(self.p.info.ilosc_punktow, None)
        self.assertNotEqual(self.p.info.ilosc_punktow, [])

    def test_glosowania(self):
        self.assertNotEqual(self.p.glosowania, None)
        self.assertNotEqual(self.p.glosowania, [])
        self.assertEqual(self.p.info.ilosc_glosowan, len(self.p.glosowania))

    def test_dni(self):
        self.assertNotEqual(self.p.dni, None)
        self.assertNotEqual(self.p.dni, [])

    def test_rozpatrywania(self):
        self.assertNotEqual(self.p.rozpatrywania, None)
        self.assertNotEqual(self.p.rozpatrywania, [])

    def test_wystapienia(self):
        self.assertNotEqual(self.p.wystapienia, None)
        self.assertNotEqual(self.p.wystapienia, [])

class TestPunkty(unittest.TestCase):
    def setUp(self):
        self.pkt = Punkt(1)

    def test_info(self):
        self.assertEqual(self.pkt.id, 1)
        self.assertNotEqual(self.pkt.info.posiedzenie_id, None)

class TestGlosowania(unittest.TestCase):
    def setUp(self):
        self.g = Glosowanie(1)

    def test_info(self):
        self.assertEqual(self.g.id, 1)
        self.assertNotEqual(self.g.info.posiedzenie_id, None)

class TestDni(unittest.TestCase):
    def setUp(self):
        self.d = Dzien(1)

    def test_info(self):
        self.assertEqual(self.d.id, 1)
        self.assertNotEqual(self.d.info.posiedzenie_id, None)

class TestRozpatrywan(unittest.TestCase):
    def setUp(self):
        self.r = Rozpatrywanie(1)

    def test_info(self):
        self.assertEqual(self.r.id, 1)
        self.assertNotEqual(self.r.info.posiedzenie_id, None)

#class TestWystapien(unittest.TestCase):
#
#    def setUp(self):
#        self.w = Wystapienie(1)
#
#    def test_info(self):
#        self.assertEqual(self.w.id, 1)
#        self.assertNotEqual(self.w.info.posiedzenie_id, None)

if __name__ == '__main__':
    unittest.main()

import unittest

from sejmometr import *
import datetime

class TestPosiedzenia(unittest.TestCase):

    def setUp(self):
        self.p = Posiedzenie(1)

    def test_info(self):
        self.assertEqual(self.p.id, 1)
        self.assertEqual(self.p(), 0)
        from datetime import date
        d = date(2012, 1, 1)
        count = self.p()
        self.assertIsInstance(self.p.info.tytul, unicode)
        self.assertIsInstance(self.p.id, int)
        self.assertIsInstance(self.p.info.data_start, date)
        self.assertIsInstance(self.p.info.data_stop, date)
        self.assertIsInstance(self.p.info.ilosc_punktow, int)
        self.assertIsInstance(self.p.info.ilosc_glosowan, int)
        #sprawdzenie czy tylko jedno zapytanie do api
        self.assertEqual(count+1, self.p())

    def test_punkty(self):
        self.assertEqual(self.p.info.ilosc_punktow, len(self.p.punkty))
        self.assertNotEqual(self.p.info.ilosc_punktow, None)
        self.assertNotEqual(self.p.info.ilosc_punktow, [])
        self.assertIsInstance(self.p.punkty[0], Punkt)


    def test_glosowania(self):
        self.assertNotEqual(self.p.glosowania, None)
        self.assertNotEqual(self.p.glosowania, [])
        self.assertEqual(self.p.info.ilosc_glosowan, len(self.p.glosowania))
        self.assertIsInstance(self.p.glosowania[0], Glosowanie)

    def test_dni(self):
        self.assertNotEqual(self.p.dni, None)
        self.assertNotEqual(self.p.dni, [])
        self.assertIsInstance(self.p.dni[0], Dzien)

    def test_rozpatrywania(self):
        self.assertNotEqual(self.p.rozpatrywania, None)
        self.assertNotEqual(self.p.rozpatrywania, [])
        self.assertIsInstance(self.p.rozpatrywania[0], Rozpatrywanie)

    def test_wystapienia(self):
        self.assertNotEqual(self.p.wystapienia, None)
        self.assertNotEqual(self.p.wystapienia, [])
        self.assertIsInstance(self.p.wystapienia[0], Wystapienie)

    def test_lista(self):
        lst = Posiedzenie.lista()
        self.assertNotEqual(lst, None)
        self.assertNotEqual(lst, [])
        self.assertIsInstance(lst[0], Posiedzenie)

class TestPunkty(unittest.TestCase):
    def setUp(self):
        self.pkt = Punkt(14)

    def test_info(self):
        self.assertEqual(self.pkt.id, 14)
        self.assertNotEqual(self.pkt.info.posiedzenie_id, None)

    def test_info_add(self):
        self.assertIsInstance(self.pkt.info.posiedzenie, Posiedzenie)
        self.assertIsInstance(self.pkt.info.glosowanie, Glosowanie)
        self.assertIsInstance(self.pkt.info.druk, Druk)

    def test_lista(self):
        self.assertNotEqual(Punkt.lista(), None)
        self.assertNotEqual(Punkt.lista(), [])

    def test_rozpatrywania(self):
        self.assertNotEqual(self.pkt.rozpatrywania, None)
        self.assertNotEqual(self.pkt.rozpatrywania, [])
        self.assertIsInstance(self.pkt.rozpatrywania[0], Rozpatrywanie)

    def test_druki(self):
        self.assertNotEqual(self.pkt.druki, None)
        self.assertNotEqual(self.pkt.druki, [])
        self.assertIsInstance(self.pkt.druki[0], Druk)

class TestGlosowania(unittest.TestCase):
    def setUp(self):
        self.g = Glosowanie(1)

    def test_info(self):
        self.assertEqual(self.g.id, 1)
        self.assertNotEqual(self.g.info.posiedzenie_id, None)

    def test_lista(self):
        self.assertNotEqual(Glosowanie.lista(), None)
        self.assertNotEqual(Glosowanie.lista(), [])

class TestDni(unittest.TestCase):
    def setUp(self):
        self.d = Dzien(1)

    def test_info(self):
        self.assertEqual(self.d.id, 1)
        self.assertNotEqual(self.d.info.posiedzenie_id, None)

    def test_lista(self):
        self.assertNotEqual(Dzien.lista(), None)
        self.assertNotEqual(Dzien.lista(), [])

class TestRozpatrywan(unittest.TestCase):
    def setUp(self):
        self.r = Rozpatrywanie(1)

    def test_lista(self):
        self.assertNotEqual(Rozpatrywanie.lista(), None)

    def test_info(self):
        self.assertEqual(self.r.id, 1)
        self.assertNotEqual(self.r.info.posiedzenie_id, None)

class TestWystapien(unittest.TestCase):
    def setUp(self):
        self.wy = Wystapienie(1)

    def test_info(self):
        self.assertEqual(self.wy.id, 1)
        self.assertNotEqual(self.wy.info.posiedzenie_id, None)

class TestPoslow(unittest.TestCase):
    def setUp(self):
        self.obj = Posel(460)

    def test_lista(self):
        self.assertNotEqual(Posel.lista(), None)

    def test_info(self):
        self.assertEqual(self.obj.id, 460)
        self.assertIsInstance(self.info.data_urodzenia, datetime.date)

if __name__ == '__main__':
    unittest.main()

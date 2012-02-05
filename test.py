import unittest

from sejmometr import Posiedzenie

class TestPosiedzenia(unittest.TestCase):

    def setUp(self):
        self.p = Posiedzenie(1)


    def test_info(self):
        self.assertEqual(self.p.id, 1)
        self.assertEqual(self.p(), 0)
        from datetime import date
        d = date(2012, 1, 1)
        count = self.p()
        self.assertEqual(type(self.p.tytul), type(u"a"))
        self.assertEqual(type(self.p.id), type(1))
        self.assertEqual(type(self.p.data_start), type(d))
        self.assertEqual(type(self.p.data_stop), type(d))
        self.assertEqual(type(self.p.ilosc_punktow), type(1))
        self.assertEqual(type(self.p.ilosc_glosowan), type(1))
        #sprawdzenie czy tylko jedno zapytanie do api
        self.assertEqual(count+1, self.p())



if __name__ == '__main__':
    unittest.main()

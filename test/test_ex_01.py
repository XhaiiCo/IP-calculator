import unittest

from model.ex01 import find_class
from util import classfull


class Test(unittest.TestCase):
    def test_find_class(self):
        classe_0 = classfull.tab[0]
        classe_a = classfull.tab[1]
        classe_127 = classfull.tab[2]
        classe_b = classfull.tab[3]
        classe_c = classfull.tab[4]
        classe_d = classfull.tab[5]
        classe_e = classfull.tab[6]

        self.assertEqual(find_class("0.0.0.0"), classe_0)
        self.assertEqual(find_class("1.0.0.0"), classe_a)
        self.assertEqual(find_class("126.255.255.255"), classe_a)
        self.assertEqual(find_class("127.255.255.255"), classe_127)
        self.assertEqual(find_class("129.12.255.255"), classe_b)
        self.assertEqual(find_class("192.12.255.255"), classe_c)
        self.assertEqual(find_class("224.12.255.255"), classe_d)
        self.assertEqual(find_class("240.12.255.255"), classe_e)
        self.assertEqual(find_class("255.255.255.255"), classe_e)




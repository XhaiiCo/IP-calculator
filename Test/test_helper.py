import unittest

from util.helper import verifIP, verifMasque


class Test(unittest.TestCase):
    def test_verif_ip(self):
        self.assertEqual(verifIP("0.0.0.0"), True)
        self.assertEqual(verifIP(""), False)
        self.assertEqual(verifIP("0."), False)
        self.assertEqual(verifIP("0.0"), False)
        self.assertEqual(verifIP("0.0.0"), False)
        self.assertEqual(verifIP("0.0.0.0"), True)
        self.assertEqual(verifIP("001.001.001.001"), True)
        self.assertEqual(verifIP("255.255.255.255"), True)
        self.assertEqual(verifIP("256.434.0.0"), False)
        self.assertEqual(verifIP("-23.-23.0.0"), False)
        self.assertEqual(verifIP("..."), False)

    def test_verif_masque(self):
        self.assertEqual(verifMasque("255.255.255.0"), True)
        self.assertEqual(verifMasque("255.255..0"), False)
        self.assertEqual(verifMasque("223.0.255.0"), False)
        self.assertEqual(verifMasque("255.-255.0.0"), False)
        self.assertEqual(verifMasque("255.255.0.0"), True)
        self.assertEqual(verifMasque("256.255.0.0"), False)
        self.assertEqual(verifMasque("255.255.12.0"), False)
        self.assertEqual(verifMasque("255.255.252.0"), True)


import unittest
from model.ex02 import valid_masque_for_classe


class Test(unittest.TestCase):
    def test_valid_masque_for_classe(self):
        self.assertEqual(valid_masque_for_classe("255.0.0.0", "A"), True)
        self.assertEqual(valid_masque_for_classe("252.0.0.0", "A"), False)
        self.assertEqual(valid_masque_for_classe("255.255.0.0", "B"), True)
        self.assertEqual(valid_masque_for_classe("255.252.0.0", "B"), False)
        self.assertEqual(valid_masque_for_classe("255.255.255.0", "C"), True)
        self.assertEqual(valid_masque_for_classe("255.255.252.0", "C"), False)
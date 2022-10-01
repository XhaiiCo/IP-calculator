import unittest
from model.ex02 import valid_masque_for_classe, ex02, broadcast, reseau
from util import message


class Test(unittest.TestCase):
    def test_valid_masque_for_classe(self):
        self.assertEqual(valid_masque_for_classe("255.0.0.0", "A"), True)
        self.assertEqual(valid_masque_for_classe("252.0.0.0", "A"), False)
        self.assertEqual(valid_masque_for_classe("255.255.0.0", "B"), True)
        self.assertEqual(valid_masque_for_classe("255.252.0.0", "B"), False)
        self.assertEqual(valid_masque_for_classe("255.255.255.0", "C"), True)
        self.assertEqual(valid_masque_for_classe("255.255.252.0", "C"), False)

    def test_broadcast(self):
        self.assertEqual(broadcast("192.0.0.0", "255.255.255.0"), "192.0.0.255")
        self.assertEqual(broadcast("128.0.0.0", "255.255.0.0"), "128.0.255.255")
        self.assertEqual(broadcast("1.0.0.0", "255.0.0.0"), "1.255.255.255")

    def test_reseau(self):
        self.assertEqual(reseau("192.0.0.0", "255.255.255.0"), "192.0.0.0")
        self.assertEqual(reseau("128.0.0.0", "255.255.0.0"), "128.0.0.0")
        self.assertEqual(reseau("1.0.0.0", "255.0.0.0"), "1.0.0.0")
        self.assertEqual(reseau("129.32.23.1", "255.255.192.0"), "129.32.0.0")
        self.assertEqual(reseau("20.234.231.20", "255.252.0.0"), "20.232.0.0")

    def test_ex02(self):
        result_message = message.tab["2"]
        # Invalid ip
        self.assertEqual(ex02("0.0.0.0", "255.0.0.0"), [result_message["IP invalid"].format("réservée")])
        self.assertEqual(ex02("127.0.0.0", "255.0.0.0"), [result_message["IP invalid"].format("réservée")])
        self.assertEqual(ex02("224.0.0.0", "255.0.0.0"), [result_message["IP invalid"].format("D")])
        self.assertEqual(ex02("240.0.0.0", "255.0.0.0"), [result_message["IP invalid"].format("E")])

        # Invalid masque
        self.assertEqual(ex02("1.0.0.0", "192.0.0.0"), [result_message["masque invalid"].format("A")])
        self.assertEqual(ex02("128.0.0.0", "255.252.0.0"), [result_message["masque invalid"].format("B")])
        self.assertEqual(ex02("192.0.0.0", "255.255.252.0"), [result_message["masque invalid"].format("C")])


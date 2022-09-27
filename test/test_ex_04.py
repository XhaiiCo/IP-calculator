import unittest

from model.ex04 import compare_address_and_network
from util import message


class Test(unittest.TestCase):
    def test_compare_address_and_network(self):
        result_message = message.tab["4"]
        self.assertEqual(compare_address_and_network("192.168.20.1", "255.255.0.0", "192.168.128.255", "255.255.192.0"), [result_message["2in1"], result_message["1notin2"]])
        self.assertEqual(compare_address_and_network("192.32.20.4", "255.255.192.0", "192.32.1.1", "255.255.0.0"), [result_message["2in1"], result_message["1in2"]])
        self.assertEqual(compare_address_and_network("128.11.128.42", "255.255.192.0", "128.11.72.3", "255.255.0.0"), [result_message["2notin1"], result_message["1in2"]])
        self.assertEqual(compare_address_and_network("192.32.21.1", "255.255.0.0", "191.234.212.2", "255.0.0.0"), [result_message["2notin1"], result_message["1notin2"]])
import unittest
from model.ex03 import is_ip_in_network, ex03
from util import message


class Test(unittest.TestCase):
    def test_is_ip_in_network(self):
        self.assertEqual(is_ip_in_network("192.168.0.1", "255.255.0.0", "192.168.255.255"), True)
        self.assertEqual(is_ip_in_network("192.168.0.1", "255.255.0.0", "192.169.255.255"), False)
        self.assertEqual(is_ip_in_network("192.168.20.1", "255.255.192.0", "192.168.32.255"), True)
        self.assertEqual(is_ip_in_network("192.168.20.1", "255.255.192.0", "192.168.128.2"), False)


    def test_ex03(self):
        result_message = message.tab["3"]
        self.assertEqual(ex03("192.168.0.1", "255.255.0.0", "192.168.255.255"), [result_message["IP in"]])
        self.assertEqual(ex03("192.168.0.1", "255.255.0.0", "192.169.255.255"), [result_message["IP out"]])




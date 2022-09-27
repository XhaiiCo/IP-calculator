import unittest

from model.ex05 import nb_hotes_tot, nb_max_hote, nb_max_sr
from util import message


class Test(unittest.TestCase):
    def test_nb_hotes_tot(self):
        self.assertEqual(nb_hotes_tot("255.255.0.0"), 65534)
        self.assertEqual(nb_hotes_tot("255.255.192.0"), 16382)
        self.assertEqual(nb_hotes_tot("255.128.0.0"), 8388606)

    def test_nb_max_hote(self):
        result_message = message.tab["5"]["sousreseaux"]

        self.assertEqual(nb_max_hote("255.255.0.0", 5), result_message["possible"].format(8190))
        self.assertEqual(nb_max_hote("255.255.192.0", 10), result_message["possible"].format(1022))
        self.assertEqual(nb_max_hote("255.255.255.192", 16), result_message["possible"].format(2))
        self.assertEqual(nb_max_hote("255.255.255.192", 17), result_message["impossible"])
        self.assertEqual(nb_max_hote("255.255.255.252", 1), result_message["possible"].format(2))
        self.assertEqual(nb_max_hote("255.255.255.254", 1), result_message["impossible"])
        self.assertEqual(nb_max_hote("255.255.192.0", 30), result_message["possible"].format(510))
        self.assertEqual(nb_max_hote("255.255.128.0", 24), result_message["possible"].format(1022))
        self.assertEqual(nb_max_hote("255.255.255.0", 64), result_message["possible"].format(2))
        self.assertEqual(nb_max_hote("255.255.255.0", 65), result_message["impossible"])
        self.assertEqual(nb_max_hote("255.255.255.192", 1), result_message["possible"].format(62))
        self.assertEqual(nb_max_hote("255.255.255.252", 1), result_message["possible"].format(2))
        self.assertEqual(nb_max_hote("255.255.255.0", 0), result_message["erreur"]["<=0"])

    def test_nb_max_sr(self):
        result_message = message.tab["5"]["hotes"]
        self.assertEqual(nb_max_sr("255.0.0.0", 1048574), result_message["possible"].format(15))
        self.assertEqual(nb_max_sr("255.0.0.0", 1048572), result_message["possible"].format(15))
        self.assertEqual(nb_max_sr("255.255.0.0", 350), result_message["possible"].format(127))
        self.assertEqual(nb_max_sr("255.255.255.0", 100), result_message["possible"].format(1))
        self.assertEqual(nb_max_sr("255.255.255.0", 200), result_message["impossible"])
        self.assertEqual(nb_max_sr("255.255.255.0", 1), result_message["possible"].format(63))
        self.assertEqual(nb_max_sr("255.255.255.192", 1), result_message["possible"].format(15))
        self.assertEqual(nb_max_sr("255.255.255.252", 1), result_message["impossible"])
        self.assertEqual(nb_max_sr("255.255.255.0", 0), result_message["erreur"]["<=0"])






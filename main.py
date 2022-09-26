# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import app
from model.ex01 import ex01
from model.ex02 import ex02
from model.ex03 import ex03
from model.ex04 import compareAddressAndNetwork
from model.ex05 import ex05
from util import console as cons
from util.helper import verifIP, verifMasque


def test_ex_01():
    cons.affiche(ex01(cons.demanderIP()))


def test_ex_02():
    ip = "223.2.33.123"
    masque = "120.2.0.0"

    if not verifIP(ip):
        print("Erreur IP")
    elif not verifMasque(masque):
        print("Erreur masque")
    else:
        cons.affiche(ex02(ip, masque))


def test_ex_03():
    cons.affiche(ex03("192.168.0.0", "255.255.225.252", "193.168.0.0"))


def test_ex_04():
    ip1 = "192.168.192.0"
    mask1 = "255.255.128.0"

    ip2 = "192.168.128.0"
    mask2 = "255.255.192.0"

    print(compareAddressAndNetwork(ip1, mask1, ip2, mask2))


def test_ex_05():
    Ip = "212.51.7.0"
    mask = "255.255.255.240"
    nbSr = 2
    nbHote = 12
    cons.affiche(ex05(nbSr, nbHote, Ip, mask))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
<<<<<<< HEAD
    app.start()
    #test_ex_01()
=======
    #app.start()
    test_ex_02()
>>>>>>> 311b1ef099aea17d14043e84955c7781e3d60dd8


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
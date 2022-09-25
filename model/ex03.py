# test si les arguments sont valides
# compte le nombre de 1 du masque de l'ip et ajoute les .
# test si les x(donné par le masque) premiers chifres de l'ip et du network sont égaux

from util import helper as h

def ex03(addressIp, maskAddress, networkIp):
    if isIpInNetwork(addressIp, maskAddress, networkIp):
        return [{"title": "L'IP est dans le réseau", "value": None}]

    return [{"title": "L'IP n'est pas dans le réseau", "value": None}]

def isIpInNetwork(addressIp, maskAddress, networkIp) :
    if not h.verifMasque(maskAddress) : return False
    if not (h.verifIP(addressIp) and h.verifIP(networkIp)) : return False

    addressIpBinary = h.toBinary(addressIp)
    networkIpBinary = h.toBinary(networkIp)

    srIp = h.SR(addressIpBinary, h.toBinary(maskAddress))
    srNetIp = h.SR(networkIpBinary, h.toBinary(maskAddress))

    if (srIp == srNetIp) :
        return True

    return False
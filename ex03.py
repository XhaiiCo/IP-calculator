# test si les arguments sont valides
# compte le nombre de 1 du masque de l'ip et ajoute les .
# test si les x(donné par le masque) premiers chifres de l'ip et du network sont égaux

import helper as h

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

# print(isIpInNetwork("192.168.225.111", "255.255.224.0", "192.168.192.255"))
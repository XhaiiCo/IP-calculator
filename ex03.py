# test si les arguments sont valides
# compte le nombre de 1 du masque de l'ip et ajoute les .
# test si les x(donné par le masque) premiers chifres de l'ip et du network sont égaux

import helper
import math

def isIpInNetwork(addressIp, maskAddress, networkIp) :
    if not helper.verifMasque(maskAddress) : return False
    if not (helper.verifIP(addressIp) and helper.verifIP(networkIp)) : return False

    nb1InMask = helper.toBinary(maskAddress).count("1") # Compte le nombre de 1 pour comparer les ips
    nb1InMask += math.trunc(nb1InMask / 8) # Compte le nomre de .
    addressIpBinary = helper.toBinary(addressIp)    # Binaire
    maskAddressBinary = helper.toBinary(networkIp)  # Binaire

    if addressIpBinary[0:nb1InMask] == maskAddressBinary[0:nb1InMask] :
        return True

    return False

# print(isIpInNetwork("192.168.230.255", "255.255.192.0", "192.168.192.255"))
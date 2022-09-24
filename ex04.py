import math
import helper as h
        
def isIpInNetwork(addressIp1, maskAddress1, addressIp2) :
    if not h.verifMasque(maskAddress1) : return False
    if not (h.verifIP(addressIp1) and h.verifIP(addressIp2)) : return False

    nb1InMask = h.toBinary(maskAddress1).count("1") # Compte le nombre de 1 pour comparer les ips
    nb1InMask += math.trunc(nb1InMask / 8) # Compte le nomre de .
    addressIp1Binary = h.toBinary(addressIp1)  # Binaire
    addressIp2Binary = h.toBinary(addressIp2)  # Binaire

    if addressIp1Binary[0:nb1InMask] == addressIp2Binary[0:nb1InMask] :
        return True

    return False

def compareAddressAndNetwork(ip1, mask1, ip2, mask2) :
    str = ""
    if (isIpInNetwork(ip1, mask1, ip2)) :
        str += "La première IP considère que la deuxième IP est dans son réseau\n"
    else :
        str += "La première IP ne considère pas que la deuxième IP est dans son réseau\n"

    if (isIpInNetwork(ip2, mask2, ip1)) :
        str += "La deuxième IP considère que la première IP est dans son réseau"
    else :
        str += "La deuxième IP ne considère pas que la première IP est dans son réseau"
        
    return str

    

ip1 =   "192.168.128.0"
mask1 = "255.255.128.0"

ip2 =   "192.168.192.0"
mask2 = "255.255.192.0"

print(compareAddressAndNetwork(ip1, mask1, ip2, mask2))

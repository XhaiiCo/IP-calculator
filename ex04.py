import helper as h
import ex03

def compareAddressAndNetwork(ip1, mask1, ip2, mask2) :
    str = ""
    if (ex03.isIpInNetwork(ip1, mask1, ip2)) :
        str += "La première IP considère que la deuxième IP est dans son réseau\n"
    else :
        str += "La première IP ne considère pas que la deuxième IP est dans son réseau\n"

    if (ex03.isIpInNetwork(ip2, mask2, ip1)) :
        str += "La deuxième IP considère que la première IP est dans son réseau"
    else :
        str += "La deuxième IP ne considère pas que la première IP est dans son réseau"
        
    return str

    

ip1 =   "192.168.192.0"
mask1 = "255.255.128.0"

ip2 =   "192.168.128.0"
mask2 = "255.255.192.0"

# print(compareAddressAndNetwork(ip1, mask1, ip2, mask2))

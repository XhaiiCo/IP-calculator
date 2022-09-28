# test si les arguments sont valides
# compte le nombre de 1 du masque de l'ip et ajoute les .
# test si les x(donné par le masque) premiers chifres de l'ip et du network sont égaux

from util import helper as h, message
from util.helper import verif_ip_reseau


def ex03(address_ip, mask_address, network_ip):
    result_message = message.tab["3"]

    if not verif_ip_reseau(network_ip):
        return [result_message["error"]["ipreseau"]]
    if is_ip_in_network(address_ip, mask_address, network_ip):
        return [result_message["IP in"]]

    return [result_message["IP out"]]


def is_ip_in_network(address_ip, mask_address, network_ip):
    address_ip_binary = h.toBinary(address_ip)
    network_ip_binary = h.toBinary(network_ip)

    sr_ip = h.SR(address_ip_binary, h.toBinary(mask_address))
    sr_net_ip = h.SR(network_ip_binary, h.toBinary(mask_address))

    if sr_ip == sr_net_ip:
        return True

    return False

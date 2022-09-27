from model import ex03
from util import message


def compare_address_and_network(ip1, mask1, ip2, mask2):
    result = []
    result_message = message.tab["4"]

    if ex03.is_ip_in_network(ip1, mask1, ip2):
        result.append(result_message["2in1"])
    else:
        result.append(result_message["2notin1"])

    if ex03.is_ip_in_network(ip2, mask2, ip1):
        result.append(result_message["1in2"])

    else:
        result.append(result_message["1notin2"])

    return result

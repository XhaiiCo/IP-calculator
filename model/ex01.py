from util import classfull


def find_class(ip):
    for c in classfull.tab:
        min_first = int(c["ipMin"].split(".")[0])
        max_first = int(c["ipMax"].split(".")[0])
        ip_first = int(ip.split(".")[0])
        if min_first <= ip_first <= max_first:
            return c

    return None


def ex01(ip):
    c = find_class(ip)
    if c:
        result = [
            "Classe {}".format(c["classe"]),
            "Nombre de reseaux : {}".format(c["reseaux"]),
            "Nombre d'hotes : {}".format(c["hotes"])]
        return result

    return ["Erreur"]

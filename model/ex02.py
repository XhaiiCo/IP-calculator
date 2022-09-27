# Exercice 02
# Si le masque correspond au masque de la classfull alors masque de reseau sinon masque de sous reseau
from model import ex01
from util import helper as h, message


def valid_masque_for_classe(masque, classe):
    spitted_masque = masque.split(".")
    if classe == "A":
        if spitted_masque[0] == "255":
            return True
    if classe == "B":
        if spitted_masque[1] == "255":
            return True
    if classe == "C":
        if spitted_masque[2] == "255":
            return True

    return False


def ex02(ip, masque):
    result = []
    result_message = message.tab["2"]

    # trouve la classe en fonction de l'ip (classfull)
    classe = ex01.find_class(ip)
    if not classe: return ["Erreur"]

    # On est bien en classe A, B ou C
    if classe["classe"] not in ["A", "B", "C"]:
        return [result_message["IP invalid"]]

    # Le masque est valide par rapport à la classe de l'ip
    if not valid_masque_for_classe(masque, classe["classe"]): return [result_message["masque invalid"]]

    # adresse de broadcast
    broadcast = h.toPointer(h.broadcast(h.toBinary(ip), h.toBinary(classe["masque"])))
    result.append(result_message["broadcast"].format(broadcast))

    # Adresse du réseau
    reseau = h.toPointer(h.SR(h.toBinary(ip), h.toBinary(classe["masque"])))
    result.append(result_message["reseau"].format(reseau))

    # Si adresse en sous-réseau
    if masque != classe["masque"]:
        sr = h.toPointer(h.SR(h.toBinary(ip), h.toBinary(masque)))
        result.append(result_message["sr"].format(sr))
    else:
        result.append(result_message["no sr"])

    return result

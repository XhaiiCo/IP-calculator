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


def broadcast(ip, masque):
    broadcast = h.toPointer(h.broadcast(h.toBinary(ip), h.toBinary(masque)))
    return broadcast


def reseau(ip, masque):
    reseau = h.toPointer(h.SR(h.toBinary(ip), h.toBinary(masque)))
    return reseau


def ex02(ip, masque):
    result = []
    result_message = message.tab["2"]

    # trouve la classe en fonction de l'ip (classfull)
    classe = ex01.find_class(ip)
    if not classe: return ["Erreur"]

    # On est bien en classe A, B ou C
    if classe["classe"] not in ["A", "B", "C"]:
        return [result_message["IP invalid"].format(classe["classe"])]

    # Le masque est valide par rapport à la classe de l'ip
    if not valid_masque_for_classe(masque, classe["classe"]): return [result_message["masque invalid"].format(classe["classe"])]

    # adresse de broadcast
    result.append(result_message["broadcast"].format(broadcast(ip, classe["masque"])))

    # Adresse du réseau
    result.append(result_message["reseau"].format(reseau(ip, classe["masque"])))

    # Si adresse en sous-réseau
    if masque != classe["masque"]:
        sr = reseau(ip, masque)
        result.append(result_message["sr"].format(sr))
    else:
        result.append(result_message["no sr"])

    return result

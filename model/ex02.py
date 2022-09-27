# Exercice 02
# Si le masque correspond au masque de la classfull alors masque de reseau sinon masque de sous reseau
from model import ex01
from util import helper as h


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
    # trouve la classe en fonction de l'ip (classfull)
    classe = ex01.findClasse(ip)
    if classe:
        if classe["classe"] == "D" or classe["classe"] == "E" : return
        if not valid_masque_for_classe(masque, classe["classe"]): return
        # adresse de broadcast
        result.append({
            "title": "Adresse de broadcast du réseau",
            "value": h.toPointer(h.broadcast(h.toBinary(ip), h.toBinary(classe["masque"])))
        })
        # Adresse du réseau
        result.append({
            "title": "Adresse de réseau",
            "value": h.toPointer(h.SR(h.toBinary(ip), h.toBinary(classe["masque"])))
        })
        # Si adresse en sous-réseau
        if masque != classe["masque"]:
            result.append({
                "title": "Adresse de sous-réseau",
                "value": h.toPointer(h.SR(h.toBinary(ip), h.toBinary(masque)))
            })
        else:
            result.append({
                "title": "Adresse de sous-réseau",
                "value": "Pas de découpe en sous-réseau"
            })

    return result

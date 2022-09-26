# Exercice 02
# Si le masque correspond au masque de la classfull alors masque de reseau sinon masque de sous reseau
from model import ex01
from util import helper as h


def ex02(ip, masque):
    result = []
    # trouve la classe en fonction de l'ip (classfull)
    classe = ex01.findClasse(ip)
    if classe:
        if classe["classe"] == "D" or classe["classe"] == "E" : return
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

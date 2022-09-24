import ex01
import helper as h
import console as c
# Exercice 02
# Si le masque correspond au masque de la classfull alors masque de reseau sinon masque de sous reseau


def ex02(ip, masque):
    result = []
    # trouve la classe en fonction de l'ip (classfull)
    classe = ex01.findClasse(ip)
    if classe:
        # adresse de broadcast
        result.append({
            "title": "Adresse de broadcast du réseau",
            "value": h.toPointer(h.broadcast(h.toBinary(ip), h.toBinary(classe["masque"])))
        })
        # Adresse du réseau
        result.append({
            "title": "Adresse de réseau",
            "value": h.toPointer(h.SR(h.toBinary(ip),h.toBinary(classe["masque"])))
        })
        # Si adresse en sous-réseau
        if masque != classe["masque"]:
            result.append({
                "title": "Adresse de sous-réseau", 
                "value": h.toPointer(h.SR(h.toBinary(ip), h.toBinary(masque)))
            })
        else:
            result.append({
                "title" : "Adresse de sous-réseau",
                "value": "Pas de découpe en sous-réseau"
            })


    return result


ip = "10.2.33.123"
masque = "255.255.255.0"

# c.affiche(ex02(ip, masque))
import ex01
import helper as h
import console as c
# Exercice 02
# Si le masque correspond au masque de la classfull alors masque de reseau sinon masque de sous reseau

# Donne l'adresse du sous réseau en binaire
# params: ip en binaire et masque en binaire


def SR(ip, masque):
    result = ""

    for i in range(len(ip)):
        if(ip[i] == '.'):
            result += '.'

        elif(masque[i] == '1'):
            result += ip[i]
        else:
            result += '0'

    return result

# Donne l'adresse broadcast du réseau en binaire
# params: id en binaire, masque en binaire


def broadcast(ip, masque):
    result = ""

    for i in range(len(ip)):
        if(ip[i] == '.'):
            result += '.'

        elif(masque[i] == '1'):
            result += ip[i]
        else:
            result += '1'

    return result


def ex02(ip, masque):
    result = []
    # trouve la classe en fonction de l'ip (classfull)
    classe = ex01.findClasse(ip)
    if classe:
        # adresse de broadcast
        result.append({
            "title": "Adresse de broadcast du réseau",
            "value": h.toPointer(broadcast(h.toBinary(ip), h.toBinary(classe["masque"])))
        })
        # Adresse du réseau
        result.append({
            "title": "Adresse de réseau",
            "value": h.toPointer(SR(h.toBinary(ip),h.toBinary(classe["masque"])))
        })
        # Si adresse en sous-réseau
        if masque != classe["masque"]:
            result.append({
                "title": "Adresse de sous-réseau", 
                "value": h.toPointer(SR(h.toBinary(ip), h.toBinary(masque)))
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
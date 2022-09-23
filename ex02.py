import ex01
import helper as h
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
    classe = ex01.findClasse(ip)
    if classe and classe["masque"] == masque:
        return classe["masque"]

    return h.toPointer(SR(h.toBinary(ip), h.toBinary(masque)))


ip = "130.234.234.234"
masque = "255.12.0.0"
print(ex02(ip, masque))
print(h.toPointer(broadcast(h.toBinary(ip), h.toBinary(masque))))

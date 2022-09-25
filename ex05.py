# ex5

import helper as h
import console as c
def init(nbSRDemande, nbHoteParSR, Ip, maskDepart) :
    result = [
        {# 5.1
            "title": "Nombre d'hotes total",
            "value": calculNbHoteTot(maskDepart)
        }
    ]

    # # 5.2
    # result.append(nbMaxHote(nbSRDemande, maskDepart))

    # # 5.3
    # result.append(nbMaxSR(nbHoteParSR, maskDepart))

    return result

# 5.1
def calculNbHoteTot(maskDepart) :
    nbZero = maskDepart.count("0")
    return (2**nbZero)-2

# 5.2
def nbMaxHote(nbSRDemande, maskDepart) :
    # nombre de 0 qu'il y a dans le masque
    nb0 = maskDepart.count("0") 

    # s'il y moins de trois 0 dans le masque, il n'y a pas assez de place pour faire des sous réseaux
    if nb0 < 3 :
        return "Il n'est pas possible de réaliser une découpe classique sur base du nombre de sous réseaux car il n'y a pas assez de bit disponible dans le masque pour pouvoir faire la découpe"

    # calcul du nombre de sous réseau disponible avec le nombre de 0
    nbSRDispo = 2**(nb0-2) # -2 car il faut au moins trois 0 pour faire des SR
    # print(nbSRDispo)

    if (nbSRDispo >= nbSRDemande) :
        # calcul du nombre d'hote par SR
        # print(2**nbSRDemande-2)
        return "Il est possible de réaliser une découpe classique, le nombre maximal d'hôtes par sous réseau est de : " + str(2**nbSRDemande-2)

    return "Il n'est pas possible de réaliser une découpe classique sur base du nombre de sous réseaux car le nombre de sous réseaux maximal est inférieur au nombre de sous réseau demandé"

# 5.3
def nbMaxSR(nbHoteDemande, maskDepart) :
    maxDecimalForNbBit = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]

    # nombre de 0 qu'il y a dans le masque
    nb0 = maskDepart.count("0") 

    # s'il y moins de trois 0 dans le masque, il n'y a pas assez de place pour faire des sous réseaux
    if nb0 < 3 :
        return "Il n'est pas possible de réaliser une découpe classique sur base d'IP car il n'y a pas assez de bit disponible dans le masque pour pouvoir faire la découpe"

    # prend l'exposant de 2 supérieur au nb d'hotes demandé pour la passer en binaire afin de connaitre le nombre de bits nécessaire
    for i in maxDecimalForNbBit :
        if nbHoteDemande <= i :
            decimalValOfNbBit = i
            break

    # calcule le nombre de bit que ça prend de mettre ce nombre d'hote par sr
    nbBitNeeded = h.toBinary(str(decimalValOfNbBit)).count("1")

    # calcule le nombre de bit qu'il reste pour la découpe en SR
    # print(maskDepart)
    # print("nb bit needed for hotes : ", nbBitNeeded)
    # print("Nb bit restant : ", nb0 - nbBitNeeded)

    nbSRPossible = 2**(nb0 - nbBitNeeded)-1

    if nbSRPossible > 0 :
        return "Le nombre maximal de sous réseaux pouvant être créés est de : " + str(nbSRPossible)
    else :
        return "Il n'est pas possible de réaliser une découpe classique sur base d'IP car le nombre de bit nécessaire à faire la découpe est insuffisant"


Ip = h.toBinary("192.168.0.255")
mask = h.toBinary("255.255.240.0")

c.affiche(init(16, 16, Ip, mask))
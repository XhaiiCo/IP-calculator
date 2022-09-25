# ex5

import helper as h
import console as c
# ip et maskDepart en binaire 
def init(nbSRDemande, nbHoteParSR, Ip, maskDepart) :
    result = [
        {# 5.1
            "title": "Nombre d'hotes total",
            "value": calculNbHoteTot(maskDepart)
        },
        {# 5.2
            "title": nbMaxHote(nbSRDemande, maskDepart),
            "value": None
        }
    ]

    # # 5.2
    # result.append(nbMaxHote(nbSRDemande, maskDepart))

    # # 5.3
    # result.append(nbMaxSR(nbHoteParSR, maskDepart))

    return result

# 5.1 maskDepart en binaire
def calculNbHoteTot(maskDepart) :
    nbZero = maskDepart.count("0")
    return (2**nbZero)-2

# 5.2
def nbMaxHote(nbSRDemande, maskDepart) :
    # nombre de 0 qu'il y a dans le masque
    nb0 = maskDepart.count("0") 
    # s'il y moins de trois 0 dans le masque, il n'y a pas assez de place pour faire des sous réseaux
    if nb0 < 2 :
        return "Il n'est pas possible de réaliser une découpe classique sur base du nombre de sous réseaux car il n'y a pas assez de bit disponible dans le masque pour pouvoir faire la découpe"
   
    (n, nbSr) = nbSR(nb0, nbSRDemande)
    
    if nbSr == -1 or nb0 - n <= 0:
        return "Il n'est pas possible de réaliser une découpe classique sur base du nombre de sous réseaux car le nombre de sous réseaux maximal est inférieur au nombre de sous réseau demandé"

    return "Il est possible de réaliser une découpe classique, le nombre maximal d'hôtes par sous réseau est de : " + str(2**(nb0-n)-2)

def nbSR(nb0, nbSRDemande):
    for n in range(0, nb0):
        nbSr = (2**n)-1
        if(nbSr >= nbSRDemande):
            return (n, nbSr)#n : nombre de bits pour la numérotation des SRs et nbSr le nombre de sous réseau possible
    
    return (-1, -1) ;

# 5.3
def nbMaxSR(nbHoteDemande, maskDepart) :
    maxDecimalForNbBit = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]

    # nombre de 0 qu'il y a dans le masque
    nb0 = maskDepart.count("0") 

    # s'il y moins de trois 0 dans le masque, il n'y a pas assez de place pour faire des sous réseaux
    if nb0 < 2 :
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


Ip = h.toBinary("212.51.7.0")
mask = h.toBinary("255.255.0.0")
nbSr = 7
nbHote = 2
print("mask", mask)
c.affiche(init(nbSr, nbHote, Ip, mask))
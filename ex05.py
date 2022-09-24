# ex5

import helper as h

# = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]

def init(nbSRDemande, nbHoteParSR, Ip, maskDepart) :
    result = []

    # 5.1
    result.append(calculNbHoteTot(Ip, maskDepart))

    # 5.2
    result.append(canDecouperEnSR(nbSRDemande, maskDepart))

    # 5.3

    return result

# 5.1
def calculNbHoteTot(Ip, maskDepart) :
    adresseSR = h.SR(Ip, maskDepart)

# 5.2
def canDecouperEnSR(nbSRDemande, maskDepart) :
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

Ip = h.toBinary("192.168.0.255")
mask = h.toBinary("255.255.255.192")
print(mask)

print(init(17, 0, Ip, mask))
# ex5
from util import helper as h, message


<<<<<<< HEAD
def ex05(nbSRDemande, nbHoteParSR, Ip, maskDepart):
    Ip = h.toBinary(Ip)
    maskDepart = h.toBinary(maskDepart)
    result = [
        #{# 5.1
        #    "title": "Nombre d'hotes total",
        #    "value": calculNbHoteTot(maskDepart)
        #},
        #{# 5.2
        #    "title": nbMaxHote(nbSRDemande, maskDepart),
        #    "value": None
        #},
        #{# 5.3
        #    "title": nbMaxSR(nbHoteParSR, maskDepart),
        #    "value": None
        #}
        "Nombre d'hôtes total : " + str(calculNbHoteTot(maskDepart)),
        nbMaxHote(nbSRDemande, maskDepart),
        nbMaxSR(nbHoteParSR, maskDepart)
    ]
=======
def ex05(nb_sr_demande, nb_hote_par_sr, ip, mask_depart):
    result = [
            # 5.1
            message.tab["5"]["hotes total"].format(nb_hotes_tot(mask_depart)),
            # 5.2
            nb_max_hote(mask_depart, nb_sr_demande),
            # 5.3
            nb_max_sr(mask_depart, nb_hote_par_sr )
        ]

>>>>>>> 1d2727ad523a70df1dec5edcf5b9f9a6bdf9a5fa
    return result


# 5.1
def nb_hotes_tot(mask_depart):
    mask_depart = h.toBinary(mask_depart)
    nb_zero = mask_depart.count("0")
    return (2 ** nb_zero) - 2


# 5.2
def nb_max_hote(mask_depart, nb_sr_demande):
    mask_depart = h.toBinary(mask_depart)
    result_message = message.tab["5"]["sousreseaux"]

    if nb_sr_demande <= 0:
        return result_message["erreur"]["<=0"]

    # nombre de 0 qu'il y a dans le masque
<<<<<<< HEAD
    nb0 = maskDepart.count("0") 
    # s'il y moins de trois 0 dans le masque, il n'y a pas assez de place pour faire des sous réseaux
    if nb0 < 3 :
        return "Il n'est pas possible de réaliser une découpe classique sur base du nombre \nde sous réseaux car il n'y a pas assez de bit disponible dans \nle masque pour pouvoir faire la découpe"
   
    (n, nbSr) = nbSR(nb0, nbSRDemande)
    
    if nbSr == -1 or nb0 - n <= 0:
        return "Il n'est pas possible de réaliser une découpe classique sur base du nombre \nde sous réseaux car le nombre de sous réseaux maximal est \ninférieur au nombre de sous réseau demandé"

    return "Il est possible de réaliser une découpe classique,\n le nombre maximal d'hôtes par sous réseau est de : " + str(2**(nb0-n)-2)

def nbSR(nb0, nbSRDemande):
    for n in range(0, nb0):
        nbSr = (2**n)-1
        nbSRDemande = int(nbSRDemande)
        if(nbSr >= nbSRDemande):
            return (n, nbSr)#n : nombre de bits pour la numérotation des SRs et nbSr le nombre de sous réseau possible
    
    return (-1, -1) ;
=======
    nb0 = mask_depart.count("0")

    (n, nbSr) = nb_sr(nb0 - 2, nb_sr_demande)# -2 car on ne peut aller au dessus de .252

    if nbSr == -1 or nb0 - n <= 0:
        return result_message["impossible"]

    return result_message["possible"].format(str(2 ** (nb0 - n) - 2))


def nb_sr(nb0, nb_sr_demande):
    for n in range(0, (nb0+1)):
        nb_sr = (2 ** n)

        if nb_sr >= nb_sr_demande:
            return n, nb_sr  # n : nombre de bits pour la numérotation des SRs et nb_sr le nombre de sous réseau possible

    return -1, -1

>>>>>>> 1d2727ad523a70df1dec5edcf5b9f9a6bdf9a5fa

# 5.3
def nb_max_sr(mask_depart, nb_hote_demande):
    mask_depart = h.toBinary(mask_depart)
    result_message = message.tab["5"]["hotes"]

<<<<<<< HEAD
    # s'il y moins de deux 0 dans le masque, il n'y a pas assez de place pour faire des sous réseaux
    if nb0 < 3:
        return "Il n'est pas possible de réaliser une découpe classique sur base d'IP \ncar il n'y a pas assez de bit disponible dans le masque pour \npouvoir faire la découpe"
=======
    if nb_hote_demande <= 0:
        return result_message["erreur"]["<=0"]
    # nombre de 0 qu'il y a dans le masque
    nb0 = mask_depart.count("0")
>>>>>>> 1d2727ad523a70df1dec5edcf5b9f9a6bdf9a5fa

    # prend l'exposant de 2 supérieur au nb d'hotes demandé pour la passer en binaire afin de connaitre le nombre de bits nécessaire
    decimal_val_of_nb_bit = 0
    i = 0
<<<<<<< HEAD
    nbHoteDemande = int(nbHoteDemande)
    while nbHoteDemande > decimalValOfNbBit:
=======
    while nb_hote_demande >= decimal_val_of_nb_bit:
>>>>>>> 1d2727ad523a70df1dec5edcf5b9f9a6bdf9a5fa
        i += 1
        decimal_val_of_nb_bit = (2 ** i) - 1

    # calcule le nombre de bit que ça prend de mettre ce nombre d'hote par sr
    nb_bit_needed = h.toBinary(str(decimal_val_of_nb_bit)).count("1")

    # calcule le nombre de bit qu'il reste pour la découpe en SR
    nb_sr_possible = 2 ** (nb0 - nb_bit_needed) - 1

<<<<<<< HEAD
    nbSRPossible = 2**(nb0 - nbBitNeeded)-1

    if nbSRPossible > 0:
        return "Le nombre maximal de sous réseaux pouvant être créés est de : " + str(nbSRPossible)
    else :
        return "Il n'est pas possible de réaliser une découpe classique sur base d'IP \ncar le nombre de bit nécessaire à faire la découpe est insuffisant"
=======
    if nb_sr_possible > 0:
        return result_message["possible"].format(str(nb_sr_possible))
    else:
        return result_message["impossible"]
>>>>>>> 1d2727ad523a70df1dec5edcf5b9f9a6bdf9a5fa

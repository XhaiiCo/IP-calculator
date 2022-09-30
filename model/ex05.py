# ex5
from util import helper as h, message


def ex05(nb_sr_demande, nb_hote_par_sr, ip, mask_depart):
    result_message = message.tab["5"]
    try:
        nb_sr_demande = int(nb_sr_demande)
    except:
        return [result_message["error"]["nbsr"]]

    try:
        nb_hote_par_sr = int(nb_hote_par_sr)
    except:
        return [result_message["error"]["nbhotes"]]

    result = [
        # 5.1
        result_message["hotes total"].format(nb_hotes_tot(mask_depart)),
        # 5.2
        nb_max_hote(mask_depart, nb_sr_demande),
        # 5.3
        nb_max_sr(mask_depart, nb_hote_par_sr)
    ]

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
    nb0 = mask_depart.count("0")

    # -2 car on ne peut aller au dessus de .252
    (n, nbSr) = nb_sr(nb0 - 2, nb_sr_demande)

    if nbSr == -1 or nb0 - n <= 0:
        return result_message["impossible"]

    return result_message["possible"].format(str(2 ** (nb0 - n) - 2))


def nb_sr(nb0, nb_sr_demande):
    for n in range(0, (nb0+1)):
        nb_sr = (2 ** n)-1

        if nb_sr >= nb_sr_demande:
            return n, nb_sr  # n : nombre de bits pour la numérotation des SRs et nb_sr le nombre de sous réseau possible

    return -1, -1


# 5.3
def nb_max_sr(mask_depart, nb_hote_demande):
    mask_depart = h.toBinary(mask_depart)
    result_message = message.tab["5"]["hotes"]

    if nb_hote_demande <= 0:
        return result_message["erreur"]["<=0"]
    # nombre de 0 qu'il y a dans le masque
    nb0 = mask_depart.count("0")

    # prend l'exposant de 2 supérieur au nb d'hotes demandé pour la passer en binaire afin de connaitre le nombre de bits nécessaire
    decimal_val_of_nb_bit = 0
    i = 0
    while nb_hote_demande >= decimal_val_of_nb_bit:
        i += 1
        decimal_val_of_nb_bit = (2 ** i) - 1

    # calcule le nombre de bit que ça prend de mettre ce nombre d'hote par sr
    nb_bit_needed = h.toBinary(str(decimal_val_of_nb_bit)).count("1")

    # calcule le nombre de bit qu'il reste pour la découpe en SR
    nb_sr_possible = 2 ** (nb0 - nb_bit_needed) - 1

    if nb_sr_possible > 0:
        return result_message["possible"].format(str(nb_sr_possible))
    else:
        return result_message["impossible"]

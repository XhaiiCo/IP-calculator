import helper as h
import classfull
import console as c
# Reseaux: Nombre de réseaux possible dans la classe
# hotes: Nombre machine max - 2

# Exercice 01


def findClasse(ip):
    for classe in classfull.tab:
        minFirst = (int) (classe["ipMin"].split(".")[0])
        maxFirst = (int) (classe["ipMax"].split(".")[0])
        ipFirst = (int) (ip.split(".")[0])
        if(ipFirst >= minFirst and ipFirst <= maxFirst):
            return classe
    
    return None

# c.afficherClasse(findClasse(c.demanderIP()))

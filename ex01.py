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
            result = [{
                "title": "Classe",
                "value": classe["classe"]
            },
            {
                "title": "Nombre de reseaux",
                "value": classe["reseaux"]
            },
            {
                "title": "Nombre d'hotes",
                "value": classe["hotes"]
            }]
            return result 
    
    return None

# c.affiche(findClasse(c.demanderIP()))

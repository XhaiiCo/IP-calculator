import helper as h
import classfull
import console as c
# Reseaux: Nombre de réseaux possible dans la classe
# hotes: Nombre machine max - 2

# Exercice 01


def findClasse(ip):
    for classe in classfull.tab:
        minFirst = classe["ipMin"].split(".")[0]
        maxFirst = classe["ipMax"].split(".")[0]
        ipFirst = ip.split(".")[0]
        if(ipFirst >= minFirst and ipFirst <= maxFirst):
            return classe


def afficherClasse(classe):
    print("Classe", classe["classe"])
    print("----------------------")
    print("   ", h.formaterNombre(classe["reseaux"]), "reseaux")
    print("   ", h.formaterNombre(classe["hotes"]), "hotes")
    print("----------------------")


afficherClasse(findClasse(c.demanderIP()))

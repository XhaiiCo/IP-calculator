import helper as h


def demanderIP():
    userIP = input("Entrer votre IP>")
    while(h.verifIP(userIP) != True):
        print("IP incorrect")
        userIP = input("Veuillez entrer une IP correct>")

    return userIP

def affiche(tab):
    for item in tab:
        print(item["title"], " : ", item["value"])

def afficherClasse(classe):
    print("Classe", classe["classe"])
    print("----------------------")
    print("   ", h.formaterNombre(classe["reseaux"]), "reseaux")
    print("   ", h.formaterNombre(classe["hotes"]), "hotes")
    print("----------------------")

def afficherMainMenu():
    print("---------------------------------------------------")
    print("MENU")
    print("---------------------------------------------------")
    print("Trouver la classe....................1")
    print("Broadcast, reseau, sous-reseau.......2")
    print("IP dans reseau.......................3")
    print("Exercice 4...........................4")
    print("Exercice 5...........................5")

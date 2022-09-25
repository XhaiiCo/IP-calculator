from util import helper


def demanderIP():
    userIP = input("Entrer votre IP>")
    while(helper.verifIP(userIP) != True):
        print("IP incorrect")
        userIP = input("Veuillez entrer une IP correct>")

    return userIP

def affiche(tab):
    for item in tab:
        result = item["title"]
        if item["value"]:
            result += " : " + str(item["value"])
        
        print(result)

def afficherMainMenu():
    print("---------------------------------------------------")
    print("MENU")
    print("---------------------------------------------------")
    print("Trouver la classe....................1")
    print("Broadcast, reseau, sous-reseau.......2")
    print("IP dans reseau.......................3")
    print("Exercice 4...........................4")
    print("Exercice 5...........................5")

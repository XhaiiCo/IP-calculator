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

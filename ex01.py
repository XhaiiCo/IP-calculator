import helper
# Reseaux: Nombre de réseaux possible dans la classe
# hotes: Nombre machine max - 2

# Exercice 01

classfull = [
    {
        "classe": "A",
        "reseaux": 256,
        "hotes": 16777214,
        "ipMin": "1.0.0.0",
        "ipMax": "126.255.255.255",
    },
    {
        "classe": "B",
        "reseaux": 65536,
        "hotes": 65534,
        "ipMin": "128.0.0.0",
        "ipMax": "191.255.255.255",
    },
    {
        "classe": "C",
        "reseaux": 16777216,
        "hotes": 254,
        "ipMin": "192.0.0.0",
        "ipMax": "224.255.255.255",
    }
]


def findClasse(ip):
    for classe in classfull:
        minFirst = classe["ipMin"].split(".")[0]
        maxFirst = classe["ipMax"].split(".")[0]
        ipFirst = ip.split(".")[0]
        if(ipFirst >= minFirst and ipFirst <= maxFirst):
            return classe


ip = "193.23.234.234"


def demanderIP():
    userIP = input("Entrer votre IP>")
    while(helper.verifIP(userIP) != True):
        print("IP incorrect")
        userIP = input("Veuillez entrer une IP correct>")

    return userIP


def afficherClasse(classe):
    print("Classe", classe["classe"])
    print("----------------------")
    print("   ", helper.formaterNombre(classe["reseaux"]), "reseaux")
    print("   ", helper.formaterNombre(classe["hotes"]), "hotes")
    print("----------------------")


afficherClasse(findClasse(demanderIP()))

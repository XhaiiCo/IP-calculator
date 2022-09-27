from tkinter import *
from tkinter import ttk

from model import ex01, ex02, ex03, ex04, ex05


def main_window(window):
    window.title("Menu principal")

    # Menu gauche
    leftMenu = Frame(window, padx=80, width=200)
    leftMenu.pack(side="left", fill="y", expand=False)
    # Menu doite en bas
    rightOutputContainer = Frame(window, padx=80, height=200)
    rightOutputContainer.pack(side="bottom", fill="x")
    rightOutputContainer.pack_propagate(False)
    # Menu droit en haut
    rightInputContainer = Frame(window, padx=80)
    rightInputContainer.pack(side="right", fill="both", expand=True)
    rightInputContainer.pack_propagate(False)

    # Container Menu gauche
    leftMenuContainer = Frame(leftMenu)
    leftMenuContainer.pack(expand=True)

    # "Déterminer la classe d'une IP"
    ttk.Button(leftMenuContainer, text="Exercice 1",
               command=lambda: display(1, rightInputContainer, rightOutputContainer))\
        .grid(column=1, row=1, sticky=E, pady=3)

    # "Déterminer l'adresse réseau + broadcast"
    ttk.Button(leftMenuContainer, text="Exercice 2",
               command=lambda: display(2, rightInputContainer, rightOutputContainer)) \
        .grid(column=1, row=2, sticky=E, pady=3)

    # "Déterminer si une IP appartient à un réseau"
    ttk.Button(leftMenuContainer, text="Exercice 3",
               command=lambda: display(3, rightInputContainer, rightOutputContainer)) \
        .grid(column=1, row=3, sticky=E, pady=3)

    # "Déterminer si 2 machines se considère dans le même réseau"
    ttk.Button(leftMenuContainer, text="Exercice 4",
               command=lambda: display(4, rightInputContainer, rightOutputContainer)) \
        .grid(column=1, row=4, sticky=E, pady=3)

    #
    ttk.Button(leftMenuContainer, text="Exercice 5",
               command=lambda: display(5, rightInputContainer, rightOutputContainer)) \
        .grid(column=1, row=5, sticky=E, pady=3)


def display(exo, frameInput, frameOutput):
    # Reset les frames
    for widget in frameInput.winfo_children():
        widget.destroy()
    for widget in frameOutput.winfo_children():
        widget.destroy()

    # Container droit Input
    rightInputContainer = Frame(frameInput)
    rightInputContainer.pack(expand=True)

    if exo == 1:
        ttk.Label(rightInputContainer, text="Entrez l'IP").grid(column=1, row=1, sticky=W)
        ip = StringVar()
        ip_entry = ttk.Entry(rightInputContainer, width=30, textvariable=ip)
        ip_entry.grid(column=1, row=2, sticky=W)

        ttk.Button(rightInputContainer, text="Text",
                   command=lambda: displayOutput(ex01.ex01(ip.get()), frameOutput))\
            .grid(column=1, row=3, sticky=E, pady=3)

    elif exo == 2:
        ttk.Label(rightInputContainer, text="Entrez l'IP").grid(column=1, row=1, sticky=W)
        ip = StringVar()
        ip_entry = ttk.Entry(rightInputContainer, width=30, textvariable=ip)
        ip_entry.grid(column=1, row=2, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque").grid(column=1, row=3, sticky=W, pady=(5, 0))
        masque = StringVar()
        masque_entry = ttk.Entry(rightInputContainer, width=30, textvariable=masque)
        masque_entry.grid(column=1, row=4, sticky=W)

        ttk.Button(rightInputContainer, text="Text",
                   command=lambda: displayOutput(ex02.ex02(ip.get(), masque.get()), frameOutput))\
            .grid(column=1, row=5, sticky=E, pady=(7, 0))

    elif exo == 3:
        ttk.Label(rightInputContainer, text="Entrez l'adresse IP").grid(column=1, row=1, sticky=W)
        ip = StringVar()
        ip_entry = ttk.Entry(rightInputContainer, width=30, textvariable=ip)
        ip_entry.grid(column=1, row=2, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque").grid(column=1, row=3, sticky=W, pady=(5, 0))
        masque = StringVar()
        masque_entry = ttk.Entry(rightInputContainer, width=30, textvariable=masque)
        masque_entry.grid(column=1, row=4, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez l'adresse du réseau").grid(column=1, row=5, sticky=W, pady=(5, 0))
        reseau = StringVar()
        reseau_entry = ttk.Entry(rightInputContainer, width=30, textvariable=reseau)
        reseau_entry.grid(column=1, row=6, sticky=W)

        ttk.Button(rightInputContainer, text="Text",
                   command=lambda: displayOutput(ex03.ex03(ip.get(), masque.get(), reseau.get()), frameOutput))\
            .grid(column=1, row=7, sticky=E, pady=(7, 0))

    elif exo == 4:
        ttk.Label(rightInputContainer, text="Entrez la première adresse IP").grid(column=1, row=1, sticky=W)
        ip1 = StringVar()
        ip1_entry = ttk.Entry(rightInputContainer, width=40, textvariable=ip1)
        ip1_entry.grid(column=1, row=2, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque de la première adresse IP").grid(column=1, row=3, sticky=W, pady=(5, 0))
        masque1 = StringVar()
        masque1_entry = ttk.Entry(rightInputContainer, width=40, textvariable=masque1)
        masque1_entry.grid(column=1, row=4, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez la deuxième adresse IP").grid(column=1, row=5, sticky=W)
        ip2 = StringVar()
        ip2_entry = ttk.Entry(rightInputContainer, width=40, textvariable=ip2)
        ip2_entry.grid(column=1, row=6, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque de la deuxième  adresse IP").grid(column=1, row=7, sticky=W, pady=(5, 0))
        masque2 = StringVar()
        masque2_entry = ttk.Entry(rightInputContainer, width=40, textvariable=masque2)
        masque2_entry.grid(column=1, row=8, sticky=W)

        ttk.Button(rightInputContainer, text="Text",
                   command=lambda: displayOutput(ex04.compare_address_and_network(ip1.get(), masque1.get(), ip2.get(), masque2.get()), frameOutput))\
            .grid(column=1, row=9, sticky=E, pady=(7, 0))

    elif exo == 5:
        ttk.Label(rightInputContainer, text="Entrez un nombre de sous réseau").grid(column=1, row=1, sticky=W)
        nbSR = StringVar()
        nbSR_entry = ttk.Entry(rightInputContainer, width=40, textvariable=nbSR)
        nbSR_entry.grid(column=1, row=2, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez un nombre d'hôte par réseau").grid(column=1, row=3, sticky=W, pady=(5, 0))
        nbHParSR = StringVar()
        nbHParSR_entry = ttk.Entry(rightInputContainer, width=40, textvariable=nbHParSR)
        nbHParSR_entry.grid(column=1, row=4, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez une adresse IP").grid(column=1, row=5, sticky=W)
        ip = StringVar()
        ip_entry = ttk.Entry(rightInputContainer, width=40, textvariable=ip)
        ip_entry.grid(column=1, row=6, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque de départ").grid(column=1, row=7, sticky=W, pady=(5, 0))
        masque = StringVar()
        masque_entry = ttk.Entry(rightInputContainer, width=40, textvariable=masque)
        masque_entry.grid(column=1, row=8, sticky=W)

        ttk.Button(rightInputContainer, text="Text",
                   command=lambda: displayOutput(ex05.ex05(nbSR.get(), nbHParSR.get(), ip.get(), masque.get()), frameOutput))\
            .grid(column=1, row=9, sticky=E, pady=(7, 0))


def displayOutput(exoReturn, frameOutput):
    for widget in frameOutput.winfo_children():
        widget.destroy()

    # Container droit output
    rightOutputContainer = Frame(frameOutput)
    rightOutputContainer.pack(expand=True)

    for i, output in enumerate(exoReturn):
        ttk.Label(rightOutputContainer, text=output).grid(column=1, row=i, sticky=W, padx=5)

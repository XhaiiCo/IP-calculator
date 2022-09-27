from tkinter import *
from tkinter import ttk

from model import ex01


def main_window(window):
    window.title("Menu principal")

    # Menu gauche
    leftMenu = Frame(window, background="black", padx=80, width=200)
    leftMenu.pack(side="left", fill="y", expand=False)
    # Menu doite en bas
    rightOutputContainer = Frame(window, background="blue", padx=80, height=150)
    rightOutputContainer.pack(side="bottom", fill="x")
    # Menu droit en haut
    rightInputContainer = Frame(window, background="yellow", padx=80)
    rightInputContainer.pack(side="right", fill="both")

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

    # Déterminer si une IP appartient à un réseau
    ttk.Button(leftMenuContainer, text="Exercice 3",
               command=lambda: display(3, rightInputContainer, rightOutputContainer)) \
        .grid(column=1, row=3, sticky=E, pady=3)

    # Déterminer si 2 machines se considère dans le même réseau
    ttk.Button(leftMenuContainer, text="Exercice 4",
               command=lambda: display(4, rightInputContainer, rightOutputContainer)) \
        .grid(column=1, row=4, sticky=E, pady=3)

    # ""
    ttk.Button(leftMenuContainer, text="Exercice 5.1",
               command=lambda: display(5, rightInputContainer, rightOutputContainer)) \
        .grid(column=1, row=5, sticky=E, pady=3)

    # ""
    ttk.Button(leftMenuContainer, text="Exercice 5.2",
               command=lambda: display(6, rightInputContainer, rightOutputContainer)) \
        .grid(column=1, row=6, sticky=E, pady=3)

    # ""
    ttk.Button(leftMenuContainer, text="Exercice 5.3",
               command=lambda: display(7, rightInputContainer, rightOutputContainer)) \
        .grid(column=1, row=7, sticky=E, pady=3)


def display(exo, frameInput, frameOutput):
    # Container Menu gauche
    rightInputContainer = Frame(frameInput)
    rightInputContainer.pack(expand=True)

    if exo == 1:
        ttk.Label(rightInputContainer, text="Entrez l'IP").grid(column=1, row=1, sticky=W, padx=5)
        ip = StringVar()
        ip_entry = ttk.Entry(rightInputContainer, width=30, textvariable=ip)
        ip_entry.grid(column=1, row=2, sticky=W)

        ttk.Button(rightInputContainer, text="Text", command=lambda: displayOutput(ex01.ex01(ip.get()), frameOutput)).grid(column=1, row=3, sticky=E, pady=3)
    """elif exo == 2:
    elif exo == 3:
    elif exo == 4:
    elif exo == 5:
    elif exo == 6:
    elif exo == 7:"""


def displayOutput(exoReturn, frameOuput):
    pass

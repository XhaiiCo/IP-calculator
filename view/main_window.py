from tkinter import *
from tkinter import ttk


def main_window(window):
    window.title("Menu principal")

    loginframe = ttk.Frame(window, padding="3 3 12 12")
    loginframe.pack(expand=YES)

    # "Déterminer la classe d'une IP"
    ttk.Button(loginframe, text="Exercice 1", command=lambda: ex1())\
        .grid(column=1, row=1, sticky=E, pady=3)

    # "Déterminer l'adresse réseau + broadcast"
    ttk.Button(loginframe, text="Exercice 2", command=lambda: ex1()) \
        .grid(column=1, row=2, sticky=E, pady=3)

    # Déterminer si une IP appartient à un réseau
    ttk.Button(loginframe, text="Exercice 3", command=lambda: ex1()) \
        .grid(column=1, row=3, sticky=E, pady=3)

    # Déterminer si 2 machines se considère dans le même réseau
    ttk.Button(loginframe, text="Exercice 4", command=lambda: ex1()) \
        .grid(column=1, row=4, sticky=E, pady=3)

    # ""
    ttk.Button(loginframe, text="Exercice 5", command=lambda: ex1()) \
        .grid(column=1, row=5, sticky=E, pady=3)

    print()


def ex1():
    pass

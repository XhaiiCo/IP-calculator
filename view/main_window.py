from tkinter import *
from tkinter import ttk, messagebox
from tkinter import font as tkf

from model import ex01, ex02, ex03, ex04, ex05
from util import message
from util.helper import verifIP, verifMasque, verif_ip_reseau

def main_window(window):
    window.title("Menu principal")

    # Menu gauche
    leftMenu = Frame(window, padx=40)
    leftMenu.pack(side="left", fill="y", expand=False)
    # Menu doite en bas
    rightOutputContainer = Frame(window, padx=80, height=150)
    rightOutputContainer.pack(side="bottom", fill="x")
    rightOutputContainer.pack_propagate(False)
    # Menu droit en haut
    rightInputContainer = Frame(window)
    rightInputContainer.pack(side="right", fill="both", expand=True)
    rightInputContainer.pack_propagate(False)

    # Container Menu gauche
    leftMenuContainer = Frame(leftMenu)
    leftMenuContainer.pack(expand=True)

    # "Déterminer la classe d'une IP"
    fontButton = tkf.Font(family='MS Sans Serif', size=10, weight='bold')
    button1 = Button(leftMenuContainer, text="Déterminer la classe d'une IP", font=fontButton, background="white", width=35, height=2,
                     command=lambda: display(1, rightInputContainer, rightOutputContainer, "Déterminer la classe d'une IP"))
    button1.grid(column=1, row=1, sticky=E, pady=5)

    # "Déterminer l'adresse réseau + broadcast"
    button2 = Button(leftMenuContainer, text="Déterminer l'adresse réseau & broadcast", background="white", font=fontButton, width=35, height=2,
                     command=lambda: display(2, rightInputContainer, rightOutputContainer, "Déterminer l'adresse réseau & broadcast"))
    button2.grid(column=1, row=2, sticky=E, pady=5)

    # "Déterminer si une IP appartient à un réseau"
    button3 = Button(leftMenuContainer, text="Déterminer si une IP appartient à un réseau", background="white", font=fontButton, width=35, height=2,
                     command=lambda: display(3, rightInputContainer, rightOutputContainer, "Déterminer si une IP appartient à un réseau"))
    button3.grid(column=1, row=3, sticky=E, pady=5)

    # "Déterminer si 2 machines se considère dans le même réseau"
    button4 = Button(leftMenuContainer, text="Déterminer si 2 machines se considère \ndans le même réseau", background="white", font=fontButton, width=35, height=2,
                     command=lambda: display(4, rightInputContainer, rightOutputContainer, "Déterminer si 2 machines se considère \ndans le même réseau"))
    button4.grid(column=1, row=4, sticky=E, pady=5)

    #
    button5 = Button(leftMenuContainer, text="Vérification découpe classique", background="white", font=fontButton, width=35, height=2,
                     command=lambda: display(5, rightInputContainer, rightOutputContainer, "Vérification découpe classique"))
    button5.grid(column=1, row=5, sticky=E, pady=5)


def display(exo, frameInput, frameOutput, label):
    result_message = message.tab
    # Reset les frames
    for widget in frameInput.winfo_children():
        widget.destroy()
    for widget in frameOutput.winfo_children():
        widget.destroy()

    # Container droit Input
    rightInputContainer = Frame(frameInput)
    rightInputContainer.pack(pady=(70, 0), padx=(100, 0), side=TOP, anchor=NW)
    fontLabel = tkf.Font(family='MS Sans Serif', size=11, weight="bold")

    fontTitle = tkf.Font(family='MS Sans Serif', size=15, weight="bold")
    ttk.Label(rightInputContainer, text=label, font=fontTitle).grid(column=1, row=0, sticky=W, pady=(0, 20))

    if exo == 1:
        ttk.Label(rightInputContainer, text="Entrez l'IP", font=fontLabel).grid(column=1, row=1, sticky=W)
        ip_value = StringVar()
        ip_entry = ttk.Entry(rightInputContainer, width=40, textvariable=ip_value)
        ip_entry.grid(column=1, row=2, sticky=W)

        ttk.Button(rightInputContainer, text="Calculer",
                   command=lambda: submit()) \
            .grid(column=1, row=3, sticky=W, pady=3, padx=(171, 0))

        def submit():
            ip = ip_value.get()
            if not verifIP(ip):
                display_output([result_message["error"]["ip"]], frameOutput)
                return
            display_output(ex01.ex01(ip), frameOutput)

    elif exo == 2:
        ttk.Label(rightInputContainer, text="Entrez l'IP", font=fontLabel).grid(column=1, row=1, sticky=W)
        ip_value = StringVar()
        ip_entry = ttk.Entry(rightInputContainer, width=40, textvariable=ip_value)
        ip_entry.grid(column=1, row=2, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque", font=fontLabel).grid(column=1, row=3, sticky=W, pady=(5, 0))
        masque_value = StringVar()
        masque_entry = ttk.Entry(rightInputContainer, width=40, textvariable=masque_value)
        masque_entry.grid(column=1, row=4, sticky=W)

        ttk.Button(rightInputContainer, text="Calculer",
                   command=lambda: submit()) \
            .grid(column=1, row=5, pady=(7, 0), padx=(171, 0), sticky=W)

        def submit():
            ip = ip_value.get()
            masque = masque_value.get()
            if not verifIP(ip):
                display_output([result_message["error"]["ip"]], frameOutput)
                return
            if not verifMasque(masque):
                display_output([result_message["error"]["masque"]], frameOutput)
                return

            display_output(ex02.ex02(ip, masque), frameOutput)

    elif exo == 3:
        ttk.Label(rightInputContainer, text="Entrez l'adresse IP", font=fontLabel).grid(column=1, row=1, sticky=W)
        ip_value = StringVar()
        ip_entry = ttk.Entry(rightInputContainer, width=40, textvariable=ip_value)
        ip_entry.grid(column=1, row=2, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque", font=fontLabel).grid(column=1, row=3, sticky=W, pady=(5, 0))
        masque_value = StringVar()
        masque_entry = ttk.Entry(rightInputContainer, width=40, textvariable=masque_value)
        masque_entry.grid(column=1, row=4, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez l'adresse du réseau", font=fontLabel).grid(column=1, row=5, sticky=W, pady=(5, 0))
        reseau_value = StringVar()
        reseau_entry = ttk.Entry(rightInputContainer, width=40, textvariable=reseau_value)
        reseau_entry.grid(column=1, row=6, sticky=W)

        ttk.Button(rightInputContainer, text="Calculer",
                   command=lambda: submit()) \
            .grid(column=1, row=7, pady=(7, 0), padx=(171, 0), sticky=W)

        def submit():
            ip = ip_value.get()
            masque = masque_value.get()
            reseau = reseau_value.get()
            if not verifIP(ip):
                display_output([result_message["error"]["ip"]], frameOutput)
                return
            if not verifMasque(masque):
                display_output([result_message["error"]["masque"]], frameOutput)
                return
            if not verif_ip_reseau(reseau):
                display_output([result_message["error"]["ipreseau"]], frameOutput)
                return

            display_output(ex03.ex03(ip, masque, reseau), frameOutput)


    elif exo == 4:
        ttk.Label(rightInputContainer, text="Entrez la première adresse IP", font=fontLabel).grid(column=1, row=1, sticky=W)
        ip1_value = StringVar()
        ip1_entry = ttk.Entry(rightInputContainer, width=40, textvariable=ip1_value)
        ip1_entry.grid(column=1, row=2, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque de la première adresse IP", font=fontLabel).grid(column=1, row=3,
                                                                                               sticky=W, pady=(5, 0))
        masque1_value = StringVar()
        masque1_entry = ttk.Entry(rightInputContainer, width=40, textvariable=masque1_value)
        masque1_entry.grid(column=1, row=4, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez la deuxième adresse IP", font=fontLabel).grid(column=1, row=5, sticky=W)
        ip2_value = StringVar()
        ip2_entry = ttk.Entry(rightInputContainer, width=40, textvariable=ip2_value)
        ip2_entry.grid(column=1, row=6, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque de la deuxième  adresse IP", font=fontLabel).grid(column=1, row=7,
                                                                                                sticky=W, pady=(5, 0))
        masque2_value = StringVar()
        masque2_entry = ttk.Entry(rightInputContainer, width=40, textvariable=masque2_value)
        masque2_entry.grid(column=1, row=8, sticky=W)

        ttk.Button(rightInputContainer, text="Calculer",
                   command=lambda: submit()) \
            .grid(column=1, row=9, pady=(7, 0), padx=(171, 0), sticky=W)

        def submit():
            ip1 = ip1_value.get()
            masque1 = masque1_value.get()
            ip2 = ip2_value.get()
            masque2 = masque2_value.get()
            if not verifIP(ip1):
                display_output([result_message["error"]["ip"]], frameOutput)
                return
            if not verifMasque(masque1):
                display_output([result_message["error"]["masque"]], frameOutput)
                return
            if not verifIP(ip2):
                display_output([result_message["error"]["ip"]], frameOutput)
                return
            if not verifMasque(masque2):
                display_output([result_message["error"]["masque"]], frameOutput)
                return

            display_output(ex04.compare_address_and_network(ip1, masque1, ip2, masque2), frameOutput)

    elif exo == 5:
        ttk.Label(rightInputContainer, text="Entrez un nombre de sous réseau", font=fontLabel).grid(column=1, row=1, sticky=W)
        nbSR = StringVar()
        nbSR_entry = ttk.Entry(rightInputContainer, width=40, textvariable=nbSR)
        nbSR_entry.grid(column=1, row=2, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez un nombre d'hôte par réseau", font=fontLabel).grid(column=1, row=3, sticky=W,
                                                                                       pady=(5, 0))
        nbHParSR = StringVar()
        nbHParSR_entry = ttk.Entry(rightInputContainer, width=40, textvariable=nbHParSR)
        nbHParSR_entry.grid(column=1, row=4, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez une adresse IP", font=fontLabel).grid(column=1, row=5, sticky=W)
        ip_value = StringVar()
        ip_entry = ttk.Entry(rightInputContainer, width=40, textvariable=ip_value)
        ip_entry.grid(column=1, row=6, sticky=W)

        ttk.Label(rightInputContainer, text="Entrez le masque de départ", font=fontLabel).grid(column=1, row=7, sticky=W, pady=(5, 0))
        masque_value = StringVar()
        masque_entry = ttk.Entry(rightInputContainer, width=40, textvariable=masque_value)
        masque_entry.grid(column=1, row=8, sticky=W)

        ttk.Button(rightInputContainer, text="Calculer",
                   command=lambda: submit()) \
            .grid(column=1, row=9, pady=(7, 0), padx=(171, 0), sticky=W)

        def submit():
            ip = ip_value.get()
            masque = masque_value.get()

            if not verif_ip_reseau(ip):
                display_output([result_message["error"]["ipreseau"]], frameOutput)
                return
            if not verifMasque(masque):
                display_output([result_message["error"]["masque"]], frameOutput)
                return

            display_output(ex05.ex05(nbSR.get(), nbHParSR.get(), ip, masque), frameOutput)


def display_output(exo_return, frame_output):
    for widget in frame_output.winfo_children():
        widget.destroy()

    # Container droit output
    right_output_container = Frame(frame_output)
    right_output_container.pack(expand=True)
    fontLabel = tkf.Font(family='MS Sans Serif', size=11, weight="bold")

    for i, output in enumerate(exo_return):
        lab = Label(right_output_container, text=output, font=("Bahnschrift", 10))
        lab.grid(column=1, row=i, sticky=W, padx=5)
        lab.configure(font=fontLabel)


from tkinter import *
from tkinter import ttk
from tkinter import font as tkf
from util import auth
from view import app


def view(window):
    window.title("Connexion")

    loginframe = ttk.Frame(window, padding="3 3 12 12")
    loginframe.pack(expand=YES)

    login = StringVar()
    login_entry = ttk.Entry(loginframe, width=30, textvariable=login)
    login_entry.grid(column=2, row=1, sticky=W)

    pwd = StringVar()
    pwd_entry = ttk.Entry(loginframe, width=30, textvariable=pwd, show='*')
    pwd_entry.grid(column=2, row=2, sticky=W, pady=3)

    fontLabel = tkf.Font(family='MS Sans Serif', size=11, weight="bold")

    ttk.Label(loginframe, text="Nom d'utilisateur", font=fontLabel).grid(column=1, row=1, sticky=W, pady=5)
    ttk.Label(loginframe, text="Mot de passe", font=fontLabel).grid(column=1, row=2, sticky=W, padx=(0, 15))

    ttk.Button(loginframe, text="Se connecter", command=lambda: logIn(window, loginframe, login.get(), pwd.get(),
                                                                login_entry, pwd_entry)).grid(column=2, row=3,
                                                                                              sticky=E, pady=3)

    login_entry.focus()


def logIn(window, loginframe, lblLogin, lblPassword, login_entry, pwd_entry):
    log = str(lblLogin)
    passw = str(lblPassword)
    if auth.login(log, passw):
        app.main(window)
    else:
        ttk.Label(loginframe, text="Mauvais nom d'utilisateur ou mot de passe", foreground='red')\
            .grid(column=1, columnspan=2, row=3, sticky=W, padx=(0, 10))

        login_entry.delete(0, END)
        login_entry.insert(0, "")
        pwd_entry.delete(0, END)
        pwd_entry.insert(0, "")

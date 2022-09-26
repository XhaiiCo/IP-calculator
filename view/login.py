from tkinter import *
from tkinter import ttk

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

    ttk.Button(loginframe, text="Log in", command=lambda: logIn(login.get(), pwd.get(), window)).grid(column=2, row=3,
                                                                                                      sticky=E, pady=3)

    ttk.Label(loginframe, text="Login").grid(column=1, row=1, sticky=W, pady=5)
    ttk.Label(loginframe, text="Password").grid(column=1, row=2, sticky=W, padx=(0, 10))

    login_entry.focus()


def logIn(login, password, window):
    log = str(login)
    passw = str(password)
    if auth.login(log, passw):
        app.main(window)
    else:
        print("Erreur")

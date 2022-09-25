import auth 
from tkinter import *
from tkinter import ttk

def logIn():
    log = str(login.get())
    passw = str(pwd.get())
    if auth.login(log, passw):
         print("loged")
    else:
         print("Erreur")

# fenetre
root = Tk()
root.title("Connexion")
root.geometry("600x400")

loginframe = ttk.Frame(root, padding="3 3 12 12")
loginframe.pack(expand=YES)

login = StringVar()
login_entry = ttk.Entry(loginframe, width=30, textvariable=login)
login_entry.grid(column=2, row=1, sticky=(W, E))

pwd = StringVar()
pwd_entry = ttk.Entry(loginframe, width=30, textvariable=pwd, show='*')
pwd_entry.grid(column=2, row=2, sticky=(W, E), pady=3)

ttk.Button(loginframe, text="Log in", command=logIn).grid(column=2, row=3, sticky=W, pady=3)

ttk.Label(loginframe, text="Login").grid(column=1, row=1, sticky=W, pady=3)
ttk.Label(loginframe, text="Password").grid(column=1, row=2, sticky=W)

login_entry.focus()
root.bind("<Return>", logIn)

# Affichage
root.mainloop()
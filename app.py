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

        #Tester le mdp et le login

root = Tk()
root.title("Connexion")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

login = StringVar()
login_entry = ttk.Entry(mainframe, width=10, textvariable=login)
login_entry.grid(column=2, row=1, sticky=(W, E))

pwd = StringVar()
pwd_entry = ttk.Entry(mainframe, width=10, textvariable=pwd, show='*')
pwd_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Log in", command=logIn).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Login").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Password").grid(column=3, row=2, sticky=W)

login_entry.focus()
root.bind("<Return>", logIn)

root.mainloop()
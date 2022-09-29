import tkinter as tk

from view import login
from view.clear_frame import clear
from view.main_window import main_window


def start():
    root = tk.Tk()
    root.geometry("950x500")
    root.resizable(False, False)

    #login.view(root)
    main_window(root) # pour tester sans avoir besoin de se co

    root.mainloop()


def main(root):
    clear(root)
    main_window(root)

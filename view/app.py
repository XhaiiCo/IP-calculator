import tkinter as tk

from view import login
from view.clear_frame import clear
from view.main_window import main_window


def start():
    # fenetre
    root = tk.Tk()
    root.geometry("600x400")
    root.resizable(False, False)

    #login.view(root)
    main_window(root)
    root.mainloop()


def main(root):
    clear(root)
    main_window(root)

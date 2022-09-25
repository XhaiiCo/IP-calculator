from tkinter import Tk

from view import login
from view.clear_frame import clear
from view.main_window import main_window


def start():
    # fenetre
    root = Tk()
    root.geometry("600x400")

    login.view(root)
    root.mainloop()


def main(window):
    clear(window)
    main_window(window)

import tkinter as tk

from view.clear_frame import clear
from view.main_window import main_window


def start():
    root = tk.Tk()
    root.geometry("600x400")

    view(root)
    root.mainloop()


def view(window):
    tk.Label(text="Position 1", width=10).grid(row=0, column=0)
    tk.Label(text="Position 2", width=10).grid(row=0, column=1)
    tk.Label(text="Position 3", width=10).grid(row=1, column=0)
    tk.Label(text="Position 4", width=10).grid(row=1, column=1)


start()

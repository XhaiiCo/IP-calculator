def clear(comp):
    for widget in comp.winfo_children():
        widget.destroy()
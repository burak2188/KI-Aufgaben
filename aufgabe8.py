# -----------------------------------------------------------------------------------

# ------------------------------ Aufgabe 8: Eine Liste anzeigen
#
# Ziel: Zeige eine Liste von Elementen in einer GUI und lasse den Benutzer neue Elemente hinzufügen.
#
# Anforderungen:
#
#     Zeige eine leere Liste in einem Textfeld oder Listbox.
#     Füge ein Eingabefeld hinzu, in das der Benutzer ein neues Element eingeben kann.
#     Füge einen Button mit der Beschriftung "Hinzufügen" hinzu, der das Element zur Liste hinzufügt.

# --------------------------------------------------------------------------------------

import tkinter as tk

def add_item():
    new_item = entry.get()
    if new_item:
        list_box.insert(tk.END, new_item)
        entry.delete(0, tk.END)

window = tk.Tk()
window.title("Liste")

list_box = tk.Listbox(window)
list_box.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window.wm_minsize(200,200), text="Hinzufügen", command=add_item,bg="lightgreen")
button.pack()

window.mainloop()
# -----------------------------------------------------------------------------------------

# ------------------------------ Aufgabe 5: Ein Zähler
#
# Ziel: Erstelle ein Fenster mit einem Button, der bei jedem Klick einen Zähler um 1 erhöht.
#
# Anforderungen:
#
#     Zeige einen Startwert von "0" in einem Label an.
#     Füge einen Button hinzu mit der Beschriftung "Erhöhe".
#     Jedes Mal, wenn der Button geklickt wird, erhöht sich der Zähler im Label um 1.

# -----------------------------------------------------------------------------------------

import tkinter as tk


def increment_counter():
    global counter
    counter += 1
    label.config(text=str(counter))

def reset_counter():
    global counter
    counter =0
    label.config(text=str(counter))


# Erstelle das Hauptfenster
window = tk.Tk()
window.title("Zähler")

# Initialisiere den Zähler
counter = 0

# Erstelle ein Label für den Zähler
label = tk.Label(window, text=str(counter))
label.pack()

# Erstelle einen Button
button = tk.Button(window.wm_minsize(200, 200), text="Erhöhe", command=increment_counter)
button.pack()
button1 = tk.Button(text="auf Null setzen", command=reset_counter)
button1.pack()
# Starte die Ereignisschleife
window.mainloop()

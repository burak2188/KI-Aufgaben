# --------------------------------------------------------------------------------

# ------------------------------ Aufgabe 10: Zufallszahl generieren
#
# Ziel: Erstelle eine GUI, die eine Zufallszahl in einem Bereich generiert.
#
# Anforderungen:
#
#     Füge zwei Eingabefelder für die Unter- und Obergrenze der Zufallszahl hinzu.
#     Füge einen Button mit der Beschriftung "Generieren" hinzu.
#     Zeige die generierte Zufallszahl in einem Label an.

# ------------------------------------------------------------------------------

import tkinter as tk
import random

def zufallszahl():
    try:
        untere_grenze = int(entry_lower.get())
        obere_grenze = int(entry_upper.get())

        if untere_grenze > obere_grenze:
            result_label.config(text="Untere Grenze < obere Grenze .")
        else:
            random_number = random.randint(untere_grenze, obere_grenze)
            result_label.config(text=f"Zufällige Zahl: {random_number}")
    except ValueError:
        result_label.config(text="Bitte geben Sie gültige Zahlen ein.")

window = tk.Tk()
window.title("Zufallszahl")

label_lower = tk.Label(window, text="Untere Grenze:")
label_lower.pack()
entry_lower = tk.Entry(window)
entry_lower.pack()

label_upper = tk.Label(window, text="Obere Grenze:")
label_upper.pack()
entry_upper = tk.Entry(window)
entry_upper.pack()

button = tk.Button(window, text="Generieren", command=zufallszahl)
button.pack()

result_label = tk.Label(window.wm_minsize(200,200), text="",bg="lightgreen")
result_label.pack()

window.mainloop()

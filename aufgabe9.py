#----------------------------------------------------------------------------------------------

# ------------------------------ Aufgabe 9: Checkboxen erstellen
#
# Ziel: Erstelle eine GUI mit Checkboxen, die den ausgewählten Status anzeigen.
#
# Anforderungen:
#
#     Erstelle drei Checkboxen (z. B. "Option 1", "Option 2", "Option 3").
#     Füge einen Button mit der Beschriftung "Zeige Auswahl" hinzu.
#     Beim Klicken auf den Button wird der Status der Checkboxen (aktiviert/deaktiviert) in einem Label angezeigt.

#-------------------------------------------------------------------------------------------------

import tkinter as tk

def show_selection():
    selected_options = []
    if var1.get():
        selected_options.append("Option 1")
    if var2.get():
        selected_options.append("Option 2")
    if var3.get():
        selected_options.append("Option 3")

    if selected_options:
        label.config(text="Ausgewählt: " + ", ".join(selected_options))
    else:
        label.config(text="Keine Option ausgewählt")

# Erstelle das Hauptfenster
window = tk.Tk()
window.title("Checkbox-Beispiel")

# Erstelle Variablen für die Checkboxen
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

# Erstelle die Checkboxen
checkbutton1 = tk.Checkbutton(window, text="Option 1", variable=var1)
checkbutton2 = tk.Checkbutton(window, text="Option 2", variable=var2)
checkbutton3 = tk.Checkbutton(window, text="Option 3", variable=var3)

# Ordne die Checkboxen an
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

# Erstelle einen Button
button = tk.Button(window, text="Zeige Auswahl", command=show_selection)
button.pack()

# Erstelle ein Label für die Ausgabe
label = tk.Label(window.wm_minsize(250,200), text="")
label.pack()

# Starte die Ereignisschleife
window.mainloop()


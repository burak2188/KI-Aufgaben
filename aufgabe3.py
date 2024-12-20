
# ------------------------------------------------------------------------------
# Aufgabe 3: Eine Eingabe und Ausgabe
#
# Ziel: Lass den Benutzer einen Text eingeben und zeige ihn nach dem Klicken auf einen Button an.
#
# Anforderungen:
#
#     Füge ein Eingabefeld (Entry) hinzu.
#     Füge einen Button mit der Beschriftung "Anzeigen" hinzu.
#     Zeige den eingegebenen Text in einem Label an, wenn der Button geklickt wird.

import tkinter as tk

root = tk.Tk()

def text_ausgeben():
    text = eingabefeld_wert.get()
    textausgabe = tk.Label(root, text=text, bg="yellow")
    textausgabe.pack()

eingabefeld_wert=tk.StringVar()
eingabefeld=tk.Entry(root, textvariable=eingabefeld_wert,bg="lightblue")
eingabefeld.pack()

button = tk.Button(root, text="Anzeigen", command=text_ausgeben)
button.pack()

root.mainloop()
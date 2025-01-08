#----------------------------------------------------------------------------------------
# Aufgabe 4: Ein einfacher Taschenrechner (Addition)
#
# Ziel: Erstelle ein Fenster, in dem zwei Zahlen eingegeben und addiert werden können.
#
# Anforderungen:
#
#     Füge zwei Eingabefelder (Entry) für die Zahlen hinzu.
#     Füge einen Button mit der Beschriftung "Berechnen" hinzu.
#     Zeige das Ergebnis der Addition in einem Label an, wenn der Button geklickt wird.
#
#------------------------------------------------------------------------------------------

import tkinter as tk

root = tk.Tk()

def taschenrechner():
    text = eingabefeld1_wert.get() + eingabefeld2_wert.get()
    textausgabe = tk.Label(root, text=text, bg="yellow")
    textausgabe.pack()


eingabefeld1_wert = tk.IntVar()
eingabefeld = tk.Entry(root, textvariable=eingabefeld1_wert, bg="lightblue")
eingabefeld.pack()
eingabefeld2_wert = tk.IntVar()
eingabefeld = tk.Entry(root, textvariable=eingabefeld2_wert, bg="pink")
eingabefeld.pack()

summe = (eingabefeld1_wert, eingabefeld2_wert)

button = tk.Button(root, text="Anzeigen", command=taschenrechner)
button.pack()

root.mainloop()

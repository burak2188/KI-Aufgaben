
# --------------------------------------------------------------------------------
# Aufgabe 6: Hintergrundfarbe ändern
#
# Ziel: Erstelle ein Fenster mit Buttons, um die Hintergrundfarbe des Fensters zu ändern.
#
# Anforderungen:
#
#     Füge drei Buttons hinzu: "Rot", "Grün", und "Blau".
#     Beim Klicken auf einen Button ändert sich die Hintergrundfarbe des Fensters entsprechend.

from tkinter import *

def aendere_hintergrundfarbe(farbe):
    fenster.configure(bg=farbe)

fenster = Tk()
fenster.title("mein erstes GUI")
fenster.wm_minsize(400, 300)



button = Button(master=fenster, text="Rot", command=lambda: aendere_hintergrundfarbe("red"), bg="red")
button1 = Button(master=fenster, text="Grün", command=lambda: aendere_hintergrundfarbe("green"), bg="green")
button2 = Button(master=fenster, text="Blau", command=lambda: aendere_hintergrundfarbe("purple"), bg="blue")

button.pack()
button1.pack()
button2.pack()

fenster.mainloop()

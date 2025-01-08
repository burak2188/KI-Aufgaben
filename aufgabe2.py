
# ----------------------------------------------------------------------------------------------------------#
# Aufgabe 2: Ein Button, der Text anzeigt
#
# Ziel: Erstelle ein Fenster mit einem Button, der beim Klicken eine Nachricht anzeigt.
#
# Anforderungen:
#
#     Füge einen Button mit der Beschriftung "Klicke mich!" hinzu.
#     Wenn der Button geklickt wird, erscheint eine Textnachricht (z. B. "Hallo, Welt!") in einem Label.
# ----------------------------------------------------------------------------------------------------------#
from tkinter import *
from cProfile import label

SPRUCH = "HALLO WELT"


def Spruch():
    label.config(text=SPRUCH)


fenster = Tk()
fenster.title("mein erstes GUI")
fenster.wm_minsize(400, 300)

label = Label(master=fenster, font=("Arial", 13), text="")
label.pack()

button = Button(master=fenster, text="Klick mich", command=Spruch)

button.pack()
fenster.mainloop()

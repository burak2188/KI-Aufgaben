# -----------------------------------------------------------------------------#
#Aufgabe 1:

# Ziel: Zeige ein leeres Fenster mit einem Titel.
#
# Anforderungen:
#
# Erstelle ein Fenster mit einem beliebigen Titel (z. B. "Mein erstes GUI").
# Setze die Größe des Fensters auf 400x300 Pixel.
# ------------------------------------------------------------------------------#

from tkinter import Tk

fenster = Tk()
fenster.title("mein erstes GUI")
fenster.wm_minsize(400,300)

fenster.mainloop()

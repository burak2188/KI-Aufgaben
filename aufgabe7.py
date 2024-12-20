#----------------------------------------------------------------------------------------------

# Aufgabe 7: Einfache Passwortprüfung
#
# Ziel: Überprüfe, ob ein Benutzer das richtige Passwort eingibt.
#
# Anforderungen:
#
#     Füge ein Eingabefeld (Entry) für das Passwort hinzu.
#     Füge einen Button mit der Beschriftung "Prüfen" hinzu.
#     Wenn das Passwort "geheim" ist, zeige "Zugriff erlaubt" in einem Label an, andernfalls "Zugriff verweigert".

#-----------------------------------------------------------------------------------------------
import tkinter as tk

def check_password():
    password = entry.get()
    if password == "geheim":
        label.config(text="Zugriff erlaubt")
    else:
        label.config(text="Zugriff verweigert")

window = tk.Tk()
window.title("Passwortprüfung")

label_password = tk.Label(window, text="Bitte geben Sie das Passwort ein:")
label_password.pack()

entry = tk.Entry(window, show="*")
entry.pack()

button = tk.Button(window, text="Prüfen", command=check_password)
button.pack()

label = tk.Label(window.wm_minsize(200,200 ), text="")
label.pack()

window.mainloop()
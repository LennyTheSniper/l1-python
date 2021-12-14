import tkinter as tk

def appui_touche(event):
    print("Tu as appuyé sur la touche", event.char)

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="black", height=500, width=500)



racine.bind("<KeyPress>", appui_touche)
canvas.grid()
racine.mainloop() # Lancement de la boucle principale
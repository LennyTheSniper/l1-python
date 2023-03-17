"""
Ok alors je t'explique maintenant comment on va faire fonctionner ça:
Il va falloir en premier déterminer chaque étape à réaliser et bien se les répartir.
Une fois qu'on a bien répartit, on va bosser petit à petit sur le projet chaqun de notre côté.
Si t'es confus et tu sais pas quoi faire, envoie moi un message via Discord: LennyTheSniper#2929

Sinon, à chaque fois que tu termine de faire ton truc et que tu a besoin que je fasse ma partie
pour progresser, tu marque juste en bas de ce commentaire dans le deuxième set de guillemet quelle
est la prochaine étape.
Voilà voilà, bonne chance!
"""


"""

"""
######################
# Import des librairies

import tkinter as tk
from typing import Text
#from unittest import result
import math

###############################
# 1er set des variables de base

CANVAS_WIDTH, CANVAS_HEIGHT = 390, 75


#################################################
# Définition des programmes ajoutant des chiffres

def go():
    global buttonState, bouton
    bouton.config(text="Stop", command=stop)

def stop():
    bouton.config(text="Go",command=go)

##########################
# Ajout des boutons/canvas

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")
bouton = tk.Button(root, text="Go", font=("Arial", "50"), command=go, bg="white")

###########################################
# Ajout de l'emplacement des boutons/canvas

bouton.grid(row=1, column=0)

########################
# création de la fênetre

canvas.grid(row=0, column=0)
root.mainloop()
import tkinter as tk
import random as rd

CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def Aleatoire():
    for i in range (0, CANVAS_WIDTH):
        for j in range (0, CANVAS_HEIGHT):
            DrawPixel(i, j, get_color(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)))

def DegradeGris():
    for i in range (0, CANVAS_WIDTH):
        for j in range (0, CANVAS_HEIGHT):
            DrawPixel(i, j, get_color(i, i, i))


def Degrade2D():
    for i in range (0, CANVAS_WIDTH):
        for j in range (0, CANVAS_HEIGHT):
            DrawPixel(i, j, get_color(i, 0, j))


root = tk.Tk()
root.title("Mon Dégradé")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")
bouton1 = tk.Button(root, text="Aléatoire", padx=7, font=("helvetica", "30"), command=Aleatoire, bg="white",fg="blue")
bouton2 = tk.Button(root, text="Dégradé gris", padx=7, font=("helvetica", "30"), command=DegradeGris, bg="white",fg="blue")
bouton3 = tk.Button(root, text="Dégradé 2D", padx=7, font=("helvetica", "30"), command=Degrade2D, bg="white",fg="blue")

def DrawPixel(x, y, color):
    canvas.create_line(x, y, x+1, y, width=1, fill=color)


DrawPixel(128,128,"#FFFFFF")

bouton1.grid(row=0, column=0, sticky='n',pady=5)
bouton2.grid(row=0, column=0)
bouton3.grid(row=0, column=0, sticky='s',pady=5)
canvas.grid(row=0, column=1)
root.mainloop()
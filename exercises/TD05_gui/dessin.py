import tkinter as tk
import random as rd

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 450

Color = ''

def Couleur():
    global Color
    Color = input("Quelle couleur souhaitez vous que les prochains objets soient?")

def Cercle():
    Centrex = rd.randint(20,CANVAS_WIDTH-20)
    Centrey = rd.randint(20,CANVAS_HEIGHT-20)
    if Color == '':
        canvas.create_oval(Centrex+50,Centrey+50,Centrex-50,Centrey-50,width=5,outline="blue")
    else:
        canvas.create_oval(Centrex+50,Centrey+50,Centrex-50,Centrey-50,width=5,outline=Color)

def Carre():
    Centrex = rd.randint(20,CANVAS_WIDTH-20)
    Centrey = rd.randint(20,CANVAS_HEIGHT-20)
    if Color == '':
        canvas.create_rectangle(Centrex+50,Centrey+50,Centrex-50,Centrey-50,width=5,outline="red")
    else:
        canvas.create_rectangle(Centrex+50,Centrey+50,Centrex-50,Centrey-50,width=5,outline=Color)

def Croix():
    Centrex = rd.randint(20,CANVAS_WIDTH-20)
    Centrey = rd.randint(20,CANVAS_HEIGHT-20)
    if Color == '':
        canvas.create_line(Centrex+50,Centrey,Centrex-50,Centrey,width=5,fill="yellow")
        canvas.create_line(Centrex,Centrey+50,Centrex,Centrey-50,width=5,fill="yellow")
    else:
        canvas.create_line(Centrex+50,Centrey,Centrex-50,Centrey,width=5,fill=Color)
        canvas.create_line(Centrex,Centrey+50,Centrex,Centrey-50,width=5,fill=Color)



root = tk.Tk()
root.title("Mon Dessin")

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")
bouton1 = tk.Button(root, text="Choisir une couleur", padx=7, font=("helvetica", "30"), command=Couleur, bg="white")
bouton2 = tk.Button(root, text="Cercle", padx=7, font=("helvetica", "30"), command=Cercle, bg="blue")
bouton3 = tk.Button(root, text="Carré", padx=7, font=("helvetica", "30"), command=Carre, bg="red")
bouton4 = tk.Button(root, text="Croix", padx=7, font=("helvetica", "30"), command=Croix, bg="yellow")



bouton1.grid(row=0, column=1)
bouton2.grid(row=1, column=0, sticky='n',pady=50)
bouton3.grid(row=1, column=0)
bouton4.grid(row=1, column=0, sticky='s',pady=50)
canvas.grid(row=1, column=1,)
root.mainloop()
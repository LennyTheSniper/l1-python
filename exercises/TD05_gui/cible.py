import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

NumberOfCircles = int(input("Combien de cercles voulez vous dans la cible?"))
Step = CANVAS_WIDTH/2/NumberOfCircles
Color = ["blue", "green", "black", "yellow", "magenta", "red"]

root = tk.Tk()
root.title("Ma cible")

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")

for i in range(NumberOfCircles):
    canvas.create_oval(Step*i,Step*i,CANVAS_WIDTH-(Step*i),CANVAS_HEIGHT-(Step*i),fill=Color[i],width=0)
    if Color[i] == "red":
        Color += Color

canvas.grid()
root.mainloop()
import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Mon test de clic")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")
clics = 0 ; clic1 = 0,0 ; clic2 = 0,0

def clic(event):
    global clic1, clic2, clics
    if clics == 0:
        clic1 = event
        clics += 1
    elif clics == 1:
        clic2 = event
        clics -= 1
        line(clic1,clic2)

def line(clic1,clic2):
    if (clic1.x < CANVAS_WIDTH/2 and clic2.x < CANVAS_WIDTH/2) or (clic1.x > CANVAS_WIDTH/2 and clic2.x > CANVAS_WIDTH/2):
        canvas.create_line(clic1.x, clic1.y, clic2.x+1, clic2.y, width=4, fill="#0000FF")
    elif clic1.x == CANVAS_WIDTH/2 or clic2.x == CANVAS_WIDTH/2:
        canvas.create_line(clic1.x, clic1.y, clic2.x+1, clic2.y, width=4, fill="#FF00FF")
    else:
        canvas.create_line(clic1.x, clic1.y, clic2.x+1, clic2.y, width=4, fill="#FF0000")

canvas.create_line(CANVAS_WIDTH/2, 0, CANVAS_WIDTH/2, CANVAS_HEIGHT, width=2, fill="#FFFFFF")

root.bind("<Button-1>", clic)
canvas.grid()
root.mainloop()
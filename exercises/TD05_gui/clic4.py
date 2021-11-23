import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Mon test de clic")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")
clics = 0

def clic(event):
    global clics
    clics += 1
    if clics % 2 == 1:
        canvas.create_rectangle(CANVAS_WIDTH/3, CANVAS_HEIGHT/3, 2*CANVAS_WIDTH/3, 2*CANVAS_HEIGHT/3, width=2, outline="#FFFFFF", fill="#FFFFFF")
    else:
        canvas.create_rectangle(CANVAS_WIDTH/3, CANVAS_HEIGHT/3, 2*CANVAS_WIDTH/3, 2*CANVAS_HEIGHT/3, width=2, outline="#FFFFFF", fill="#000000")
    if clics >= 10:
        root.destroy()

canvas.create_rectangle(CANVAS_WIDTH/3, CANVAS_HEIGHT/3, 2*CANVAS_WIDTH/3, 2*CANVAS_HEIGHT/3, width=2, outline="#FFFFFF")

root.bind("<Button-1>", clic)
canvas.grid()
root.mainloop()
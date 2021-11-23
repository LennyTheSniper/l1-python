import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Mon test de clic")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")

def clic(event):
    canvas.create_line(event.x, event.y, event.x+1, event.y, width=1, fill="#FF0000")


root.bind("<Button-1>", clic)
canvas.grid()
root.mainloop()
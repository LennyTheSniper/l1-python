import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Mon test de clic")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")

def clic(event):
    if event.x >= CANVAS_WIDTH/2:
        canvas.create_oval(event.x+50, event.y+50, event.x-50, event.y-50, width=4, outline="#FF0000")
    else:
        canvas.create_oval(event.x+50, event.y+50, event.x-50, event.y-50, width=4, outline="#0000FF")

canvas.create_line(CANVAS_WIDTH/2, 0, CANVAS_WIDTH/2, CANVAS_HEIGHT, width=2, fill="#FFFFFF")

root.bind("<Button-1>", clic)
canvas.grid()
root.mainloop()
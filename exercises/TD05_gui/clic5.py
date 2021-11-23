import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Mon test de clic")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")
clics = 0 ; cercles = []

def clic(event):
    global clics
    clics += 1
    if clics <= 8:
        cercles.append(canvas.create_oval(event.x+50, event.y+50, event.x-50, event.y-50, width=0, fill="#FF0000"))
    elif clics == 9:
        for i in range (len(cercles)):
            canvas.itemconfig(cercles[i],fill="#FFFF00")
    if clics >= 10:
        canvas.create_rectangle(-10, -10, CANVAS_WIDTH+10, CANVAS_HEIGHT+10, fill="#000000")
        clics = 0



root.bind("<Button-1>", clic)
canvas.grid()
root.mainloop()
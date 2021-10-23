from tkinter import Canvas, Grid, Tk, ttk
from Engine import grid
from GameOfLife import *

def drawGrid(grid: grid, cnv: Canvas):

    cnvWidth = cnv.winfo_reqwidth()
    wstep = cnvWidth/grid.width
    cnvHeight = cnv.winfo_reqheight()
    hstep = cnvHeight/grid.height

    for i in range(grid.width):
        
        cnv.create_line(i*wstep, 0, i*wstep, cnvHeight)

    for j in range(grid.height):

        cnv.create_line(0, j*hstep, cnvWidth, j*hstep)

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

cnv = Canvas(root, width=root.winfo_screenwidth()*0.8, height=root.winfo_screenheight()*0.8, bg="ivory")
cnv.grid()
drawGrid(gameOfLife.grid, cnv)

root.mainloop()
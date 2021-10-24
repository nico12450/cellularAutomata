from tkinter import Canvas, Grid, Tk, ttk
from Engine import grid
from GameOfLife import *

def drawGrid(grid: grid, cnv: Canvas):

    cnv.delete('all')
    cnvWidth = cnv.winfo_reqwidth()
    wstep = cnvWidth/grid.width
    cnvHeight = cnv.winfo_reqheight()
    hstep = cnvHeight/grid.height

    for i in range(grid.width):
        
        cnv.create_line(i*wstep, 0, i*wstep, cnvHeight)

    for j in range(grid.height):

        cnv.create_line(0, j*hstep, cnvWidth, j*hstep)

    for i in range(len(grid.grid)):
        for j in range(len(grid.grid[i])):

            if grid.get(j, i):

                x = j * wstep
                y = cnvHeight - (i * hstep)

                cnv.create_rectangle(x, y, x + wstep, y + hstep, fill = 'black')

def next(grid: grid, cnv: Canvas):

    gameOfLife.nextState()
    drawGrid(grid, cnv)

def click(event, grid: grid, cnv: Canvas):

    cnvWidth = cnv.winfo_reqwidth()
    wstep = cnvWidth/grid.width
    cnvHeight = cnv.winfo_reqheight()
    hstep = cnvHeight/grid.height

    j = int(event.x/wstep)
    i = grid.height - int(event.y/hstep)

    grid.toggle(j, i)
    drawGrid(grid, cnv)


root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

cnv = Canvas(root, width=root.winfo_screenwidth()*0.8, height=root.winfo_screenheight()*0.8, bg="ivory")
cnv.bind("<Button-1>", lambda event: click(event, gameOfLife.grid, cnv))
cnv.grid()
drawGrid(gameOfLife.grid, cnv)

ttk.Button(frm, text="Next", command=lambda: next(gameOfLife.grid, cnv)).grid(column=0, row=0)

root.mainloop()
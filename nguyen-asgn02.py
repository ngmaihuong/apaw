#Name: Huong (Sierra) Nguyen
#Course: CIS 2300
#Professor: Trevor Moores
#Date last updated: 10/4/2020
#Assignment 2: Conway's Game of Life

from tkinter import *
import time
import random

WIN_W = 520
WIN_H = 520
CELL_W = 40
GRIDSIZE = int(WIN_W/CELL_W)-2
SPEED = 0.1

tk = Tk()
canvas = Canvas(tk, width = WIN_W, height = WIN_H) #specify the window that canvas is associated with
tk.title("Game of Life - Sierra Nguyen")
canvas.pack() #show the defined window

#Generate an initial grid of random ON/OFF values
def create_grid(flag=None): #Define a function to create a grid
    global GRIDSIZE

    grid = []
    for row in range(GRIDSIZE+2):
        grid.append([])
            
        for col in range(GRIDSIZE+2):
            if row == 0 or row == GRIDSIZE+1:
                grid[row].append(0)
            elif col == 0 or col == GRIDSIZE+1:
                grid[row].append(0)
            else:
                if flag == 'cells':
                    grid[row].append(random.randrange(2))
                else:
                    grid[row].append(0)
                    
    return grid
    
cells = create_grid('cells')

#Display the initial grid using different colors to denote ON/OFF
for row in range(1, GRIDSIZE+1):
    for col in range(1, GRIDSIZE+1):
        if cells[row][col] == 1:
            cell_color = 'maroon'
        else:
            cell_color = 'white'
        canvas.create_rectangle(CELL_W*col, CELL_W*row, \
                                CELL_W+(CELL_W*col), CELL_W+(CELL_W*row), \
                                fill=cell_color)
tk.update()
time.sleep(SPEED)

neighbors = create_grid()

#Count the number of neighbors
while True:       
    for row in range(1, GRIDSIZE+1):
        for col in range(1, GRIDSIZE+1):
            score = 0
            for x in range(-1, 2):
                score += cells[row+x][col-1:col+2].count(1)
            score -= cells[row][col]
            neighbors[row][col] = score

#Apply the Conway rules
    for row in range(1, GRIDSIZE+1):
        for col in range(1, GRIDSIZE+1):
            if neighbors[row][col] == 2:
                continue
            elif neighbors[row][col] == 3:
                cells[row][col] = 1
            else:
                cells[row][col] = 0

#Update the grid
    for row in range(1, GRIDSIZE+1):
            for col in range(1, GRIDSIZE+1):
                if cells[row][col] == 1:
                    cell_color = 'maroon'
                else:
                    cell_color = 'white'
                canvas.create_rectangle(CELL_W*col, CELL_W*row, \
                                        CELL_W+(CELL_W*col), CELL_W+(CELL_W*row), \
                                        fill=cell_color)
    tk.update()
    time.sleep(SPEED)
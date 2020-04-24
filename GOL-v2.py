#-------------------------------------------------------------------------------
#NAME:  Huong (Sierra) Nguyen
#DATE:  April 22, 2020
#TITLE: Implementation of Conway's "Game of Life," version 2.
#       Using a list of rectangles, whose color is updated as their status
#       changes (from live to dead, or dead to live).
#-------------------------------------------------------------------------------

from tkinter import *
import time
import random

WIN_W = 520
WIN_H = 520
CELL_W = 10
GRIDSIZE = int(WIN_W/CELL_W)-2
SPEED = 0.1

#Initialization of Tile object, default cell is off
class Tile:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.shape = canvas.create_rectangle(x1, y1, x2, y2, fill='white')
        self.status = 0
        self.canvas = canvas
    #Changing the status of the tile (also changes the color)
    def change_status(self):
        if self.status == 0:
            self.status = 1
            self.canvas.itemconfig(self.shape, fill='orange')
        else:
            self.status = 0
            self.canvas.itemconfig(self.shape, fill='white')

#Creating a padded (randomized or empty) grid of a certain size
def create_grid(flag=None):
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

def main():
    #Construction of canvas
    root = Tk()
    root.title('Game of Life v3 - Sierra Nguyen')
    c = Canvas(root, width=WIN_W, height=WIN_H)
    c.pack()
    
    #Creation of initial 'cells' and 'neighbors' grid
    cells = create_grid('cells')
    neighbors = create_grid()

    #Creation of board of Tile objects
    board = []
    for row in range(GRIDSIZE):
        board.append([])
        for col in range(GRIDSIZE):
            board[row].append(
                Tile(c,
                    CELL_W*(col+1), CELL_W*(row+1),
                    CELL_W+(CELL_W*(col+1)), CELL_W+(CELL_W*(row+1))
                    )
                )
            
    #Loop through iterations of game until user quits 
    while True:
        
        #Update Tile status (if needed)
        for row in range(GRIDSIZE):
            for col in range(GRIDSIZE):
                if board[row][col].status != cells[row+1][col+1]:
                    board[row][col].change_status()
                
        root.update()
        time.sleep(SPEED)
        
        #Count number of neighbors for each cell
        for row in range(1, GRIDSIZE+1):
            for col in range(1, GRIDSIZE+1):
                score = 0
                for x in range(-1, 2):
                    score += cells[row+x][col-1:col+2].count(1)
                score -= cells[row][col]
                neighbors[row][col] = score
        
        #Update grid by applying the Conway rules
        for row in range(1, GRIDSIZE+1):
            for col in range(1, GRIDSIZE+1):
                if neighbors[row][col] == 2:
                    continue
                elif neighbors[row][col] == 3:
                    cells[row][col] = 1
                else:
                    cells[row][col] = 0

if __name__ == '__main__':
    main()

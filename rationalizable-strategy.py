# Try to write a program to find the set of rationalizable strategies in Chapter 7 games (Game Theory)
# Create a grid/matrix

#Note: Very raw code I am still trying to figure out
# Create a grid/matrix
COL_SIZE = 5
ROW_SIZE = 5
print('Grid Size =', ROW_SIZE, "x", COL_SIZE)
"""
#start draft
def create_grid():
    global COL_SIZE
    global ROW_SIZE
    print('Grid Size =', COL_SIZE, "x", ROW_SIZE)
    grid = []
    
    for row in range(ROW_SIZE):
        grid.append([])
        for col in range(COL_SIZE):
            grid[row].append([]) 
    return grid
#end draft

grid = create_grid()
for row in grid:
    print(row)
    
print('\n')
"""
game = []
P2_CHOICE = ['a','b','c','d']
P1_1 = ['w', [5,4], [4,4], [4,5], [12,2]] 
P1_2 = ['x', [3,7], [8,7], [5,8], [10,6]]
P1_3 = ['y', [2,10], [7,6], [4,6], [9,5]]
P1_4 = ['z', [4,4], [5,9], [4,10], [10,9]]

for row in range(ROW_SIZE):
    game.append([])
    game[0] = [(1,2)]
    for col in range(0, 1):
        game[0].extend(P2_CHOICE)
game[1].extend(P1_1)
game[2].extend(P1_2)
game[3].extend(P1_3)
game[4].extend(P1_4)

for row in game:
    print(row)
print('\n')
#Find dominant strategies for P2

compr = []

for row in range(ROW_SIZE):
    compr.append([])
    compr[0] = [(1,2)]
    for col in range(0, 1):
        compr[0].extend(P2_CHOICE)
compr[1].extend(['w', [0,0], [0,0], [0,0], [0,0]])
compr[2].extend(['x', [0,0], [0,0], [0,0], [0,0]])
compr[3].extend(['y', [0,0], [0,0], [0,0], [0,0]])
compr[4].extend(['z', [0,0], [0,0], [0,0], [0,0]])

for row in compr:
    print(row)
print('\n')

for row in range(1, ROW_SIZE):
    if game[row][1][1] > game[row][2][1]:
        compr[row][1][1] = 'Y'
    else:
        compr[row][1][1] = 'N'
"""
if game[1][1][1] > game[1][2][1]:
    compr[1][1][1] = 'Y'
else:
    compr[1][1][1] = 'N'
    
if game[2][1][1] > game[2][2][1]:
    compr[2][1][1] = 'Y'
else:
    compr[2][1][1] = 'N'  
if game[3][1][1] > game[3][2][1]:
    compr[3][1][1] = 'Y'
else:
    compr[3][1][1] = 'N'
if game[4][1][1] > game[4][2][1]:
    compr[4][1][1] = 'Y'
else:
    compr[4][1][1] = 'N'
"""
print(compr)

"""
offset = 2
while offset < ROW_SIZE:
    for row in range(1, ROW_SIZE):
#        compr.append([])
#        for col in range(1, COL_SIZE):
        if game[row][1][1] > game[row][offset][1]:
            compr[row][1][1] = 'Y'
        else:
            compr[row][1][1] = 'N'
    offset += 1
print(compr)
"""
"""
next_gen = []
for row in range(GRIDSIZE+2):
    next_gen.append([])
    for col in range(GRIDSIZE+2):
        if row == 0 or row == (GRIDSIZE+1):
            next_gen[row].append(0)
        elif col == 0 or col == (GRIDSIZE+1):
            next_gen[row].append(0)
        else:
            score = 0
            for x in range(-1, 2):
                score += grid[row+x][col-1:col+2].count(1)
            score -= grid[row][col]
            next_gen[row].append(score)
"""

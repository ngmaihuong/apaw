# Try to write a program to find the set of rationalizable strategies in Chapter 7 games (Game Theory)
# Create a grid/matrix

#Note: Very raw code I am still trying to figure out
COL_SIZE = 5
ROW_SIZE = 5
print('Grid Size =', ROW_SIZE, "x", COL_SIZE)
"""
#draft
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
"""
grid = create_grid()
for row in grid:
    print(row)
    
print('\n')

game = []
P2_CHOICE = ['a','b','c','d']
P1_1 = ['w', (5,4), (4,4), (4,5), (12,2)] 
P1_2 = ['x', (3,7), (8,7), (5,8), (10,6)]
P1_3 = ['y', (2,10), (7,6), (4,6), (9,5)]
P1_4 = ['z', (4,4), (5,9), (4,10), (10,9)]

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
#Find dominant strategies for P2
offset = 1
while offset <= ROW_SIZE:
    for row in range(1, ROW_SIZE):
        if game[row][offset][1] > game[row][offset+1][1]:
            print("Y")
        else:
            print("N")
    print("\n")
    offset += 1   

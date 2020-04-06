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

#Find dominant strategies for P2
print("\nRound/Row 1 Count")
ct = []
for row in range(1, ROW_SIZE):
    if game[row][1][1] > game[row][2][1]:
        ct.append('Y')
    else:
        ct.append('N')
        
    if ct.count('Y') == 4:
        del game[row][2]
    else:
        pass
print(ct)
ct = []
for row in range(1, ROW_SIZE):
    if game[row][1][1] > game[row][3][1]:
        ct.append('Y')
    else:
        ct.append('N')
        
    if ct.count('Y') == 4:
        del game[row][3]
    else:
        pass 
print(ct)
ct = []
for row in range(1, ROW_SIZE):
    if game[row][1][1] > game[row][4][1]:
        ct.append('Y')
    else:
        ct.append('N')
        
    if ct.count('Y') == 4:
        del game[row][4]
    else:
        pass
print(ct)
print("\nRound/Row 2 Count")
ct = []
for row in range(1, ROW_SIZE):
    if game[row][2][1] > game[row][3][1]:
        ct.append('Y')
    else:
        ct.append('N')
        
    if ct.count('Y') == 4:
        del game[row][3]
    else:
        pass
print(ct)
ct = []
for row in range(1, ROW_SIZE):
    if game[row][2][1] > game[row][4][1]:
        ct.append('Y')
    else:
        ct.append('N')
        
    if ct.count('Y') == 4:
        del game[row][4]
        print('Delete this row')
    else:
        pass
print(ct)
print("\nRound/Row 3 Count")
ct = []
for row in range(1, ROW_SIZE):
    if game[row][3][1] > game[row][4][1]:
        ct.append('Y')
    else:
        ct.append('N')
        
    if ct.count('Y') == 4:
        del game[1][4]
        del game[2][4]
        del game[3][4]
        del game[4][4]
        print(ct, 'Delete this row')
    else:
        pass
print('\n')
for row in game:
    print(row)

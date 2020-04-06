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
pov = 1
i = pov + 1

print("\nRound/Row", pov, "Count Executed")
ct = []
offset = 1
for row in range(1, ROW_SIZE):
    if game[row][pov][1] > game[row][i][1]:
        ct.append('Y')
    else:
        ct.append('N')
    
    while ct.count('Y') == 4 and offset in range(1, ROW_SIZE):
        del game[offset][i]
        offset += 1
    while ct.count('N') == 4 and offset in range(1, ROW_SIZE):
        del game[offset][pov]
        offset += 1        

#print('\n')
for row in game:
    print(row)

pov = 2
i = pov + 1

print("\nRound/Row", pov, "Count Executed")
ct = []
offset = 1
for row in range(1, ROW_SIZE):
    if game[row][pov][1] > game[row][i][1]:
        ct.append('Y')
    else:
        ct.append('N')
    
    while ct.count('Y') == 4 and offset in range(1, ROW_SIZE):
        del game[offset][i]
        offset += 1
    while ct.count('N') == 4 and offset in range(1, ROW_SIZE):
        del game[offset][pov]
        offset += 1 

#print('\n')
for row in game:
    print(row)

#pov = 3
#i = pov + 1

print("\nRound/Row", pov, "Count Executed")
ct = []
offset = 1
for row in range(1, ROW_SIZE):
    if game[row][pov][1] > game[row][i][1]:
        ct.append('Y')
    else:
        ct.append('N')
    
    while ct.count('Y') == 4 and offset in range(1, ROW_SIZE):
        del game[offset][i]
        offset += 1
    while ct.count('N') == 4 and offset in range(1, ROW_SIZE):
        del game[offset][pov]
        offset += 1

#print('\n')
for row in game:
    print(row)

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
    game[0] = [[1,2]]
    for col in range(0, 1):
        game[0].extend(P2_CHOICE)
game[1].extend(P1_1)
game[2].extend(P1_2)
game[3].extend(P1_3)
game[4].extend(P1_4)

for row in game:
    print(row)

def transpose(grid): 
    new_grid = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]
    a, b = grid[0][0].index(1), grid[0][0].index(2)
    grid[0][0][b], grid[0][0][a] = grid[0][0][a], grid[0][0][b]
    return new_grid

#Find dominant strategies for P2

for pov in range(1, len(game[-1])):
    if pov+1 < len(game[-1])-1:
        for i in range(pov+1, len(game[-1])-1): #hidden error: i=4 in range (4,3)     
            print("\nComparing all with column", pov)
            ct = []
            offset = 0
            for row in range(1, len(game)):
                if game[row][pov][1] > game[row][i][1]:
                    ct.append('Y')
                else:
                    ct.append('N')
                    
                while ct.count('Y') == ROW_SIZE-1 and offset in range(len(game)):
                    del game[offset][i]
                    offset += 1
                while ct.count('N') == ROW_SIZE-1 and offset in range(len(game)):
    #                print('Delete strategy', game[0][pov], 'because it is dominated.')
                    del game[offset][pov]
                    offset += 1              

    elif COL_SIZE > pov+1 > len(game[-1])-1:
        for i in range(len(game[-1])-1, pov+1): #hidden error: i=4 in range (4,3)     
            print("\nComparing all with column", pov)
            #hidden error: should change this to player's choice rather than the column index
            ct = []
            offset = 0
            for row in range(1, len(game)): #hidden error: counting the number of columns, not rows.
                #This is why the use of len(game[-1]) is quite consistent throughout (FIXED)
                if game[row][pov-1][1] > game[row][i][1]: #hidden error: pov = 3, i=3. Comparing the same column.
                    ct.append('Y')
                else:
                    ct.append('N')
                    
                while ct.count('Y') == ROW_SIZE-1 and offset in range(len(game)):
                    del game[offset][i]
                    offset += 1
                while ct.count('N') == ROW_SIZE-1 and offset in range(len(game)):
    #                print('Delete strategy', game[0][pov], 'because it is dominated.')
                    del game[offset][pov]
                    offset += 1  
    else:
        game = transpose(game)

print('\nUndominated Strategies for Player 2')
for row in game:
    print(row)
    

#Find dominant strategies for P1

for pov in range(1, len(game[-1])):
    if pov+1 < len(game[-1])-1:
        for i in range(pov+1, len(game[-1])-1):    
            print("\nComparing all with column", pov)
            ct = []
            offset = 0
            for row in range(1, len(game)):
                if game[row][pov][0] > game[row][i][0]:
                    ct.append('Y')
                else:
                    ct.append('N')
                    
                while ct.count('Y') == len(game)-1 and offset in range(len(game)):
                    del game[offset][i]
                    offset += 1
                while ct.count('N') == len(game)-1 and offset in range(len(game)):
                    del game[offset][pov]
                    offset += 1              

    elif COL_SIZE > pov+1 > len(game[-1])-1:
        for i in range(len(game[-1])-1, pov+1):    
            print("\nComparing all with column", pov)
            ct = []
            offset = 0
            for row in range(1, len(game)): 
                if game[row][pov-1][0] > game[row][i][0]:
                    ct.append('Y')
                else:
                    ct.append('N')
                    
                while ct.count('Y') == len(game)-1 and offset in range(len(game)):
                    del game[offset][i]
                    offset += 1
                while ct.count('N') == len(game)-1 and offset in range(len(game)):
                    del game[offset][pov]
                    offset += 1  
    else:
        game = transpose(game)

print('\nUndominated Strategies for Player 1')
for row in game:
    print(row)

for pov in range(1, len(game[-1])):
    if pov+1 < len(game[-1]):
        for i in range(pov+1, len(game[-1])-1):    
            print("\nComparing all with column", pov)
            ct = []
            offset = 0
            for row in range(1, len(game)):
                if game[row][pov][1] > game[row][i][1]:
                    ct.append('Y')
                else:
                    ct.append('N')
                    
                while ct.count('Y') == len(game)-1 and offset in range(len(game)):
                    del trans_game[offset][i]
                    offset += 1
                while ct.count('N') == len(game)-1 and offset in range(len(game)):
                    del trans_game[offset][pov]
                    offset += 1              

    elif COL_SIZE > pov+1 > len(game[-1])-1:
        for i in range(len(game[-1])-1, pov+1):    
            print("\nComparing all with column", pov)
            ct = []
            offset = 0
            for row in range(1, len(game)): 
                if game[row][pov-1][1] > game[row][i][1]:
                    ct.append('Y')
                else:
                    ct.append('N')
                    
                while ct.count('Y') == len(game)-1 and offset in range(len(game)):
                    del game[offset][i]
                    offset += 1
                while ct.count('N') == len(game)-1 and offset in range(len(game)):
                    del game[offset][pov-1] #what's the better index than pov-1?
                    offset += 1  
    else:
        game = transpose(game)

print('\nUndominated Strategies for Player 2')
for row in game:
    print(row)

for pov in range(1, len(game[-1])):
    if pov+1 < len(game[-1])-1:
        for i in range(pov+1, len(game[-1])-1):    
            print("\nComparing all with column", pov)
            ct = []
            offset = 0
            for row in range(1, len(game)-1):
                if game[row][pov][0] > game[row][i][0]:
                    ct.append('Y')
                else:
                    ct.append('N')
                    
                while ct.count('Y') == len(game)-1 and offset in range(len(game)):
                    del game[offset][i]
                    offset += 1
                while ct.count('N') == len(game)-1 and offset in range(len(game)):
                    del game[offset][pov]
                    offset += 1              

    elif COL_SIZE > pov+1 > len(game[-1])-1:
        for i in range(len(game[-1])-1, pov+1):    
            print("\nComparing all with column", pov)
            ct = []
            offset = 0
            for row in range(1, len(game)-1): 
                if game[row][pov][0] > game[row][i][0]:
                    ct.append('Y')
                else:
                    ct.append('N')
                    
                while ct.count('Y') == len(game)-1 and offset in range(len(game)):
                    del game[offset][i]
                    offset += 1
                while ct.count('N') == len(game)-1 and offset in range(len(game)):
                    del game[offset][pov]
                    offset += 1  
    else:
        game = transpose(game)

print('\nUndominated Strategies for Player 1')
for row in game:
    print(row)

#The real question is how to make the program reiterate...

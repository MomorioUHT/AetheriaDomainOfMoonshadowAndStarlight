def tiltUp(grid: list):
    for col in range(len(grid[0])):
        stack = []
        for row in range(len(grid)):
            if grid[row][col] != ".":
                stack.append(grid[row][col])
        
        for row in range(len(grid)):
            grid[row][col] = stack[row] if row < len(stack) else "."
            
    return grid


def tiltDown(grid: list):
    for col in range(len(grid[0])): 
        stack = []
        for row in range(len(grid) - 1, -1, -1):
            if grid[row][col] != ".":
                stack.append(grid[row][col])
        
        for row in range(len(grid)):
            grid[len(grid) - 1 - row][col] = stack[row] if row < len(stack) else "."
            
    return grid


def tiltLeft(grid: list):
    for row in range(len(grid)):
        stack = []
        for col in range(len(grid[row])):
            if grid[row][col] != ".":
                stack.append(grid[row][col])
        
        for col in range(len(grid[row])):
            grid[row][col] = stack[col] if col < len(stack) else "."
            
    return grid


def tiltRight(grid: list):
    for row in range(len(grid)):
        stack = []
        for col in range(len(grid[row]) - 1, -1, -1):
            if grid[row][col] != ".":
                stack.append(grid[row][col])
        
        for col in range(len(grid[row])):
            grid[row][len(grid[row]) - 1 - col] = stack[col] if col < len(stack) else "."
            
    return grid

def printGrid(grid: list):
    print("-"*(cols+2))
    for i in grid:
        lines = "".join(i)
        print(f"|{lines}|")
    print("-"*(cols+2))


rows, cols = map(int, str(input()).split(" "))
mode, moves = map(str, str(input()).split(" "))
moves = int(moves)
grid = []

for i in range(rows):
    lines = list(str(input()))
    grid.append(lines)
    
    
if (mode == "CLOCKWISE"):      
    for i in range(1,moves+1):
        if (i%4 == 1):
            grid = tiltLeft(grid)
        elif (i%4 == 2):
            grid = tiltUp(grid)
        elif (i%4 == 3):
            grid = tiltRight(grid)
        elif (i%4 == 0):
            grid = tiltDown(grid)
elif (mode == "COUNTER_CLOCKWISE"):
    for i in range(1,moves+1):
        if (i%4 == 1):
            grid = tiltRight(grid)
        elif (i%4 == 2):
            grid = tiltUp(grid)
        elif (i%4 == 3):
            grid = tiltLeft(grid)
        elif (i%4 == 0):
            grid = tiltDown(grid)       
            
printGrid(grid)
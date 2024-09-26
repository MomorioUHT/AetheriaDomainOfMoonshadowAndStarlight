rows, cols = map(int, input().split())
grid = []
trap_types = {}
traps = 0

for i in range(rows):
    row = list(map(str, input().split()))
    grid.append(row)
    
def markTraps(r: int, c: int):
    if r<0 or r>=rows or c<0 or c>=cols or not grid[r][c].isalpha(): return
    
    curr = grid[r][c]
    
    if curr not in trap_types:
        trap_types[curr] = 1
    else:
        trap_types[curr] += 1  
          
    grid[r][c] = "0"
    
    markTraps(r+1,c)
    markTraps(r-1,c)
    markTraps(r,c+1)
    markTraps(r,c-1)
    
for i in range(rows):
    for j in range(cols):
        if grid[i][j].isalpha():
            traps += 1
            markTraps(i,j)

if traps == 1:
    print(f"Number of Trap sets {traps} trap")
else:
    print(f"Number of Trap sets {traps} traps")
    
print(f"Trap Types:")
for key in sorted(trap_types.keys()):
    print(f"Type {key} -> {trap_types[key]}")
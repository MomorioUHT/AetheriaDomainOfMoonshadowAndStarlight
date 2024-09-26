def bfs(maze: list, start, rows, cols):
    visited = [start]  
    queue = [start]    
    
    parent = {}

    while len(queue) > 0:
        x, y = queue.pop(0)  

        if maze[x][y] == 'P':
            path = []
            current = (x, y)
            while (current != start):
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_x, next_y = x + dx, y + dy

            if 0 <= next_x < rows and 0 <= next_y < cols:
                if maze[next_x][next_y] != '#' and (next_x, next_y) not in visited:
                    visited.append((next_x, next_y))
                    queue.append((next_x, next_y)) 
                    parent[(next_x, next_y)] = (x, y)

    return -1 

def get_user_input():
    rows, cols = map(int, input().split())
    mana = int(input())
    
    maze = []
    for _ in range(rows):
        row = [" " if i == "0" else i for i in input().split(" ")]
        maze.append(row)
    
    return maze, mana, rows, cols

maze, mana, rows, cols = get_user_input()

rows,cols = len(maze),len(maze[0])
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == "S":
            start = (i, j)
        if maze[i][j] == "P":
            end = (i, j)

result = bfs(maze, start, rows, cols)

if (result == -1):
    print("NOT POSSIBLE")
    print("The maze was collapsed!")
else:
    useMana = len(result) - 2
    if (mana - (useMana) >= 0):
        print("THERE IS A WAY OUT!")
        print("Luna's Path:")
        for (i,j) in result:
            maze[i][j] = "x"
            
        maze[start[0]][start[1]] = "S"
        maze[end[0]][end[1]] = "P"
        
        for i in maze:
            print(*i)
            
        manaLeft = mana - useMana
        print(f"Mana used {useMana}, left {manaLeft}")
    else:
        print("NOT POSSIBLE")
        print(f"Not enough mana! (requires {useMana}, having {mana})")
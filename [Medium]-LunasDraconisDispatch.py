import math
points = {}

def findDistanceBetweenPoints(x1: int, y1: int, x2: int, y2: int):
    delta = (y2-y1)**2 + (x2-x1)**2
    return math.sqrt(delta)

def getXY(name: str):
    return points[name][0], points[name][1]

pointAmount = int(input())
startPoint = str(input())
amount = int(input())

for i in range(pointAmount):
    name,x,y = str(input()).split(" ")
    points[name] = [int(x),int(y)]

currPoint = startPoint
currX,currY = getXY(currPoint)

visited = []

for i in range(amount):
    max_distance = 0
    for name,coords in points.items():
        
        if (name == currPoint) or (name in visited):
            continue

        currDistance = findDistanceBetweenPoints(currX, currY, coords[0], coords[1]) 
        if currDistance > max_distance:
            max_distance = currDistance
            tempPoint = name
            tempX, tempY = getXY(tempPoint)


    visited.append(currPoint)
    currPoint = tempPoint
    currX = tempX
    currY = tempY

path = " -> ".join(visited)

print(f"{path}")
amount = int(input())
data = [int(i) for i in str(input()).split(" ")]

map = {}

for i in range(amount): 
    map[i%amount] = [] 

for i in data: 
    map[i%amount].append(i)

for key,val in map.items(): 
    print(f"{key}: {val}")
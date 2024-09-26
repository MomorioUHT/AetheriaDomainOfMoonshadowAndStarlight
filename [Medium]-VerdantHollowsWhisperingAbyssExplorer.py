n = int(input())
people = [i for i in range(1,n+1)]
num = int(input())

killed = []

index = 0

for i in range(n):
    while people[index] == 0:
        index += 1
        if index == n: index = 0
    
    count = 1
    
    while (count < num):
        index += 1
        if index == n: index = 0
        if people[index] == 0: continue
        count += 1
        
    killed.append(people[index])
    people[index] = 0

print(*killed)
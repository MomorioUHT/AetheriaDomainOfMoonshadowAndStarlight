def isCursedWord(word: str):
    if not word[-1].isdigit():
        return False

    for i in range(0,len(word)):
        if i%2 == 0:
            if not word[i].isdigit():
                return False
        else:
            if i == len(word)-2:
                if not word[i].isupper():
                    return False
            elif not word[i].islower():
                return False
            
    return True

def translateCursedWord(word: str):
    temp = word[::-1]
    result = ''
    
    for i in temp:
        if i.isalpha():
            result += i

    return result

data = []

while True:
    x = str(input())
    if x == "EXIT": break
    data.append(x.split(" "))
    
for i in data:
    for j in range(len(i)):
        if isCursedWord(i[j]):
            i[j] = translateCursedWord(i[j])
            
for i in data:
    print(" ".join(i))
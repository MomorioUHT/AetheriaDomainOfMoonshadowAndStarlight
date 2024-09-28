garden = []
newGarden = []
days = 1
FoundRainbow = False
rainbowCount = 0

def extractFlower(fw: str):
    number,fw_name = '',''
    
    for i in fw:
        if i.isdigit(): number += i
        else: fw_name += i
            
    return int(number), fw_name

def emptyGarden(garden: list):
    for i in garden:
        if len(i) != 0:
            return False
    print("-----")
    print("IMPOSSIBLE")
    return True

def printGarden(garden: list):
    print(f"day{days}:")
    for i in garden:
        line = ' '.join(i)
        if (len(i) == 0):
            print("[] -> DEAD")
        else:
            print(f"[{line}]")
            
def printRainbowInfo(rainbowAmount: int):
    day_s = ''
    rainbow_s = ''
    
    if (days != 1):
        day_s = 's'
    if (rainbowAmount != 1):
        rainbow_s = 's'
        
    print("-----")
    print(f"{days} day{day_s}: {rainbowAmount} rainbow{rainbow_s}")
        
def red(amount: int):
    greenAmount = int(0.2*amount)
    blueAmount = int(0.8*amount)
    
    temp = []
    if (greenAmount >= 1):
        name = str(greenAmount) + "g"
        temp.append(name)
    if (blueAmount >= 1):
        name = str(blueAmount) + "b"
        temp.append(name)

    newGarden.append(temp)
    
def green(amount: int):
    redAmount = int(0.1*amount)
    yellowAmount = int(0.2*amount)
    greenAmount = int(0.7*amount)
    
    temp = []
    if (redAmount >= 1):
        name = str(redAmount) + "r"
        temp.append(name)
    if (yellowAmount >= 1):
        name = str(yellowAmount) + "y"
        temp.append(name)
    if (greenAmount >= 1):
        name = str(greenAmount) + "g"
        temp.append(name)
        
    newGarden.append(temp)

def blue(amount: int):
    global FoundRainbow
    global rainbowCount
    
    rainbowAmount = int(0.05*amount)
    redAmount = int(0.95*amount)
    
    temp = []
    if (rainbowAmount >= 1):
        name = str(rainbowAmount) + "rb"
        temp.append(name)
        FoundRainbow = True
        rainbowCount = rainbowAmount
    if (redAmount >= 1):
        name = str(redAmount) + "r"
        temp.append(name)
    
    newGarden.append(temp)

def yellow(amount: int):
    yellowAmount = int(0.5*amount)
    
    temp = []
    if (yellowAmount >= 1):
        name = str(yellowAmount) + "y"
        temp.append(name)
        
    newGarden.append(temp)
    
type, amount = map(str, str(input()).split(" "))
amount = int(amount)

if (type == "r"):
    red(amount)
elif (type == "g"):
    green(amount)
elif (type == "b"):
    blue(amount)
elif (type == "y"):
    yellow(amount)
               
garden = newGarden.copy()
newGarden = [] 

printGarden(garden)
    
while (not emptyGarden(garden) and not FoundRainbow):
    for i in garden:
        for j in i:
            amount, type = extractFlower(j)
            if (type == "r"):
                red(amount)
            elif (type == "g"):
                green(amount)
            elif (type == "b"):
                blue(amount)
            elif (type == "y"):
                yellow(amount)
                
    garden = newGarden.copy()
    newGarden = []
    
    days += 1
                
    printGarden(garden)

if (FoundRainbow):
    printRainbowInfo(rainbowCount)
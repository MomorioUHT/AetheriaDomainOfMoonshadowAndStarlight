months = {
    "JANUARY": 1,
    "FEBRUARY": 2,
    "MARCH": 3,
    "APRIL": 4,
    "MAY": 5,
    "JUNE": 6,
    "JULY": 7,
    "AUGUST": 8,
    "SEPTEMBER": 9,
    "OCTOBER": 10,
    "NOVEMBER": 11,
    "DECEMBER": 12,
}

def getMonthNumber(name: str):
    return months[name.upper()]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

def day_of_week(year, month, day):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    return (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7

def print_calendar(year, month):
    print("--[============================]--")
    print("Su | Mo | Tu | We | Th | Fr | Sa |")
    
    start_day = day_of_week(year, month, 1)
    days = days_in_month(month, year)
    last_day_position = (start_day + days - 1) % 7
    
    for _ in range(start_day):
        print("   |", end=" ")
    
    for day in range(1, days + 1):
        print(f"{day:2} |", end=" ")
        start_day = (start_day + 1) % 7
        if start_day == 0:
            print() 
    
    if last_day_position != 6:
        for _ in range(6 - last_day_position):
            print("   |", end=" ")
        print() 

    print("--[============================]--")

x, year = str(input("")).split(" ")
month = getMonthNumber(x)
year = int(year)

print_calendar(year, month)
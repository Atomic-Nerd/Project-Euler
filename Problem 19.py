totaldays = 36889
months = [31,28,31,30,31,30,31,31,30,31,30,31]
year = 1900
sundays = 0
day = 0

while year < 2001:
    Leap = False
    if year % 4 == 0:
        if year % 100 != 0:
            Leap = True
        else:
            if year % 400 == 0:
                Leap = True

    print (year,Leap)

    if Leap == True:
        months[1] == 29
    else:
        months[1] == 28

    for i in range(0,12):
        month = i
        for i in range(0,months[month]):
            day += 1

        if month == 0 and day%7 == 0:
            sundays += 1
            print (year,day)
    year += 1
print (sundays)
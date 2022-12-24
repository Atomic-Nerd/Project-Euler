amicablenumber = []

for i in range(1,10000):
    factors = []
    sumoffactors = 0
    factors2 = []
    sumoffactors2 = 0

    if i in amicablenumber:
        continue
    if i == 1 or i == 6 or i == 28:
        continue

    number = i
    for i in range(1,number+1):
        if number%i == 0:
            factors.append(i)
    factors.remove(factors[len(factors)-1])

    for i in range(0,len(factors)):
        sumoffactors += factors[i]

    for i in range(1,sumoffactors+1):
        if sumoffactors%i == 0:
            factors2.append(i)
    factors2.remove(factors2[len(factors2)-1])

    for i in range(0,len(factors2)):
        sumoffactors2 += factors2[i]

    if number == sumoffactors2 and number != sumoffactors:
        print ("PAIR",number,sumoffactors)
        amicablenumber.append(sumoffactors)
        amicablenumber.append(sumoffactors2)

amicablenumberstotal = 0
for i in range(0,len(amicablenumber)):
    amicablenumberstotal += amicablenumber[i]
print (amicablenumberstotal)
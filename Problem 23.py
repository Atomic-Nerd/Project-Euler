abundant_numbers = []
print ("Section 1")
for i in range(4,14000):
    factors = []
    number = i
    val = 0
    for i in range(1,number):
        if number%i == 0:
            val += i

    if val > number:
        abundant_numbers.append(number)

numbercount = []
print ("Section 2")
for i in range(1,28124):
    number = i
    skip = False
    for i in range(0,len(abundant_numbers)):
        check1 = abundant_numbers[i]
        for i in range(0,len(abundant_numbers)):
            check2 = abundant_numbers[i]
            newnum = check1+check2
            if number == newnum:
                skip = True
                continue
        if skip == True:
            continue
    if skip != True:
        numbercount.append(number)

print ("Section 3")
total = 0
for i in range(0,len(numbercount)):
    total += numbercount[i]

print (total)
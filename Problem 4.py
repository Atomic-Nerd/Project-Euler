num = 0
largestnum = 0
correct = True

for i in range(100,1000):
    x = i
    for z in range(100,1000):
        correct = True
        num = x * z
        num = str(num)
        for i in range (0,len(num)-1):
            if num[i] != num[len(num)-1-i]:
                correct = False
        if correct == True:
            if int(num) > largestnum:
                largestnum = int(num)

print (largestnum)



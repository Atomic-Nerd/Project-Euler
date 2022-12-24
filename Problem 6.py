total1 = 0
total2 = 0
difference = 0
for i in range(1,101):
    total1 += i**2
    total2 += i

squaresum = total2**2
difference = squaresum - total1
print (difference)

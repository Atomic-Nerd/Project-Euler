x = 2**1000
y = str(x)
total = 0
for i in range(0,len(y)):
    total += int(y[i])
print (total)
total = 0
x = 2

while x < 2000000:

    correct = True

    for i in range(2,1000):
        if i != x and x%i == 0:
            correct = False

    if correct == True:
        total += x

    x += 1
    print (x)

print (total)
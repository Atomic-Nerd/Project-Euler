run = True
x = 232792500


while run:

    wrong = False
    x += 1

    print ("Run:"   ,x)

    for i in range(1,21):
        if x % i != 0:
            wrong = True

    if wrong != True:
        run = False

print (x)

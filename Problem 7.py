Primes = []

x = 2

while len(Primes) < 10003:

    correct = True

    for i in range(2,1000):
        if i != x and x%i == 0:
            correct = False

    if correct == True:
        Primes.append(x)
        print (len(Primes)-1,"<--")
        print (Primes[len(Primes)-1])

    x += 1



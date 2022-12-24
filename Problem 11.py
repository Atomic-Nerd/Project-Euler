for i in range(0,10000000):
    divisors = []
    total = 0
    for x in range(1,i):
        total += x
    for i in range(0,total+1):
        if i != 0:
            if total%i == 0:
                divisors.append(i)
    print (len(divisors),total)



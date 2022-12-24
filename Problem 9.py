for i in range(200,1000):
    a = i
    for i in range(1,1000):
        b = i
        for i in range(1,1000):
            c = i

            if a**2 + b**2 == c**2:
                print ("Triplet",a,b,c)
                if a + b + c == 1000:
                    print ("Perfect Triplet",a,b,c)
                    print (a*b*c)
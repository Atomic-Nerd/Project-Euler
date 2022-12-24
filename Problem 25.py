fibbonaci = [1,1]
for i in range(0,5000):
    if len(str(fibbonaci[i])) == 1000:
        print (i)
        continue
    n1 = fibbonaci[i]
    n2 = fibbonaci[i+1]
    fibbonaci.append(n1+n2)

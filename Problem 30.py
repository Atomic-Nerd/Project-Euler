numbersArr = []

for i in range(10):
    for j in range(10):
        for c in range(10):
            for d in range(1,10):
                numbers = [str(i),str(j),str(c),str(d)]
                num = i**4 + j**4 + c**4 + d**4
                print (num,i,j,c,d)
                num = str(num)
                valid = True
                for z in range(len(num)):
                    if num[z] not in numbers:
                        valid = False
                    else:
                        pass
                if valid:
                    numbersArr.append(num)

print (numbersArr)
MaxChain = 0
for i in range(800000,1000000):
    Chain = []
    number = i
    SaveNumber = i
    while number > 1:
        if number%2 == 0:
            number = number/2
            Chain.append(number)
        else:
            number = (number*3)+1
            Chain.append(number)

    ChainVal = len(Chain)
    if ChainVal > MaxChain:
        MaxChain = ChainVal
        print ("New Max",SaveNumber,":",len(Chain))

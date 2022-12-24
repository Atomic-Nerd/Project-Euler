L1 =                 [75]
L2 =                [95,64]
L3 =               [17,47,82]
L4 =              [18,35,87,10]
L5 =             [20,4,82,47,65]
L6 =            [19,1,23,75,3,34]
L7 =           [88,2,77,73,7,63,67]
L8 =          [99,65,4,28,6,16,70,92]
L9 =        [41,41,26,56,83,40,80,70,33]
L10 =      [41,48,72,33,47,32,37,16,94,29]
L11 =    [53,71,44,65,25,43,91,52,97,51,14]
L12 =   [70,11,33,28,77,73,17,78,39,68,17,57]
L13 =  [91,71,52,38,17,14,91,43,58,50,27,29,48]
L14 = [63,66,4,68,89,53,67,30,73,16,69,87,40,31]
L15 = [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

test = 0
total = 0
while test != L15:
    maxval = 0
    if test == 0:
        test = L1
    elif test == L1:
        test = L2
    elif test == L2:
        test = L3
    elif test == L3:
        test = L4
    elif test == L4:
        test = L5
    elif test == L5:
        test = L6
    elif test == L6:
        test = L7
    elif test == L7:
        test = L8
    elif test == L8:
        test = L9
    elif test == L9:
        test = L10
    elif test == L10:
        test = L11
    elif test == L11:
        test = L12
    elif test == L12:
        test = L13
    elif test == L13:
        test = L14
    elif test == L14:
        test = L15

    if test == L1:
        lastpos = 0
        total += 75
    else:
        newtest = test[pos1:pos2]
        print (newtest)
        for i in range(0,2):
            if newtest[i] > maxval:
                maxval = newtest[i]
                lastpos = test.index(maxval)
        if newtest.index(maxval) == 0:
            print ("left")
        else:
            print ("right")
        total += maxval
    pos1 = lastpos
    pos2 = lastpos+2

print (total)
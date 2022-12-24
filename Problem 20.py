import math
factoral = math.factorial(100)
stringfactoral = str(factoral)
total = 0
for i in range(0,len(stringfactoral)):
    value = int(stringfactoral[i])
    total += value
print (total)
Fibonacci = [1,2]
total = 0
count = 0

while count < 100000:
    Fibonacci.append(Fibonacci[count]+Fibonacci[count+1])
    count += 1
    if Fibonacci[len(Fibonacci)-1] > 4000000:
        Fibonacci.remove(Fibonacci[len(Fibonacci)-1])
        count = 99999999999999

for i in range(0,len(Fibonacci)):
    if Fibonacci[i]%2 == 0:
        total += Fibonacci[i]

print (total)
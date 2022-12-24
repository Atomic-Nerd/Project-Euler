import num2word
total = 0
for i in range(1,1001):
    print (num2word.word(i))
    num = len(num2word.word(i))
    total += num
print (total)
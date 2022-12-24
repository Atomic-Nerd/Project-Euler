sequence = []

for i in range(2,101):
    for j in range(2,101):
        if i**j in sequence:
            pass
        else:
            sequence.append(i**j)

print (len(sequence))
print (sequence[0:10])
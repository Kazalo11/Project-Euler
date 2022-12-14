
def splitting(x):
    return [int(i) for i in str(x)]

count = 0
total = 1
i = 1
while count <= 1000000:
    for digit in splitting(i):
        count += 1
        if count == 1 or count == 10 or count == 100 or count == 1000 or count == 10000 or count == 100000 or count == 1000000:
            total *= digit
    i += 1

print(total)





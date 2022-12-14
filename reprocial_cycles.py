value = 0
biggest = 0

for i in range(2,1000):
    digits = []
    decimal = 1/i*1000
    if decimal % 1 == 0:
        continue
    remainder = str(decimal % 1)[2:]
    remainder = list(remainder)
    print(remainder)




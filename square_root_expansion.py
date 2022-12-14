from decimal import *

getcontext().prec = 1000


def total_digits(x):
    x = str(x)
    point = x.index('.')
    x = x.replace('.','')
    digits = [int(i) for i in x[:100]]
    return sum(digits)


count = 0

for i in range(100):
    root = Decimal(i).sqrt()
    if root % 1 != 0:
        count += total_digits(root)

print(count)

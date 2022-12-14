import math
def smallest_factorial_divisior(x):
    m = 1
    while math.factorial(m) % x != 0:
        m+=1
    return m

def summation(n):
    total = 0
    for i in range(2,n+1):
        print(i)
        total+=smallest_factorial_divisior(i)
    return total

print(summation(100000000))



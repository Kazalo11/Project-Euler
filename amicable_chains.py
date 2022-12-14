import math


def sum_divisors(x: int) -> int:
    factors = 1
    j = 2
    while j <= math.sqrt(x):
        if x % j == 0:
            if x / j == j:
                factors += j
            else:
                factors += j
                factors += x / j
        j += 1
    return factors


biggest_chain = []
numbers_checked = []

for i in range(1, 1000000):
    chain = []
    next_number = i
    if next_number not in numbers_checked:
        while sum_divisors(next_number) not in chain and sum_divisors(next_number) <= 1000000:
            numbers_checked.append(next_number)
            chain.append(sum_divisors(next_number))
            next_number = sum_divisors(next_number)
    numbers_checked.append(next_number)
    if sum_divisors(next_number) <= 1000000:
        if len(chain) > len(biggest_chain):
            biggest_chain = chain
    print(i)

print(min(biggest_chain))

import math
def divisors(x: int) -> int:
    total = 1
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            if i == x / i:
                total += i
            else:
                total = total + i + x / i
        i += 1
    return total


def abundant(x: int) -> bool:
    return divisors(x) > x


abundant_numbers = []

for i in range(1,28123):
    if abundant(i):
        abundant_numbers.append(i)


def abundant_pair(x: int) -> bool:
    find_pair = {}
    for number in abundant_numbers:
        if number*2 == x:
            return True
        if number not in find_pair.values():
            find_pair[number] = x-number
        else:
            return True
    return False

result = 0

for i in range(28123):
    if not abundant_pair(i):
        result+=i
    print(i)
print(result)
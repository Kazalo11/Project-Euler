def sum_reversible(x: int) -> int:
    reverse_x = str(x)
    reverse_x = reverse_x[::-1]
    reverse_x = int(reverse_x)
    return x + reverse_x


def all_odd(x: int) -> bool:
    if x % 10 == 0:
        return False
    x = sum_reversible(x)
    while x > 10:
        remainder = x % 10
        if (remainder % 2 == 0):
            return False
        x = x//10
    return x % 2 != 0

count = 0

for i in range(1,1000000000):
    if all_odd(i):
        count+=1
        print(f'i: {i}, property = {sum_reversible(i)}, count: {count}')
print(count)
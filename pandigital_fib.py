numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def pandigital(x: int) -> bool:
    x = [int(i) for i in str(x)]
    first = x[:9]
    last = x[-9:]
    first.sort()
    last.sort()
    return first == numbers and last == numbers

fib_a = 0
fib_b = 1
for i in range(10000):
    if fib_a > 1e18:
        if pandigital(fib_a):
            print(i)
            break
    test = fib_a + fib_b
    fib_a = fib_b
    fib_b = test



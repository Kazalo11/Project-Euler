def isprime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if (x % i) == 0:
            return False
    return True


primes = []

for i in range(1,1000000):
    if isprime(i):
        primes.append(i)



def isprime(test_prime_number: int) -> bool:
    for number in range(2, int(test_prime_number ** 0.5) + 1):
        if test_prime_number % number == 0:
            return False
    return True


total = 2
for j in range(3, 2000000):
    if isprime(j):
        total += j

print(total)

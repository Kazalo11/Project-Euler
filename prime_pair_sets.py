from itertools import permutations
primes = []

def isprime(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

for i in range(2,1000):
    if isprime(i):
        primes.append(i)

prime_permutations = list(permutations(primes,5))
print(prime_permutations)
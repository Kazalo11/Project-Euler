from itertools import permutations


def primes(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

prime = 0
test = [1,2,3,4,5,6,7,8,9]
for i in range(1,len(test)):
	poss = list(permutations(test[0:i+1]))
	for j in poss:
		j = int(''.join(map(str,j)))
		if primes(j):
			prime = j
print(prime)
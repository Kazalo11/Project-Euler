def primes(x):
	if x <= 0:
		return False
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

def count_primes(a,b):
	i = 0
	prime = i**2 + a*i + b
	while primes(prime):
		i+=1
		prime = i**2 + a*i + b
	return i

list_of_primes = []
for i in range(2,1000):
	if primes(i):
		list_of_primes.append(i)

coefficients = [0,0]
biggest = 0
for i in list_of_primes:
	for j in range(-999,1000):
		if count_primes(j,i) > biggest:
			coefficients[0] = j
			coefficients[1] = i
			biggest = count_primes(j,i)

print(coefficients)


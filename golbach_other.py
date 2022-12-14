def primes(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

def list_of_primes(x):
	prime = []
	for i in range(2,x):
		if primes(i) and i % 2 == 1:
			prime.append(i)
	return prime

def test(x):
	if primes(x):
		return True
	testing = list_of_primes(x)
	for i in testing:
		if (((x - i)/2)**0.5).is_integer():
			return True
	return False

i = 5
while test(i):
	i+=2
print(i)
		
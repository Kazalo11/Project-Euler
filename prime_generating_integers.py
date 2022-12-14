def divisors(x):
	factors = [1]
	for i in range(2,int(x//2)+1):
		if x % i == 0:
			factors.append(i)
	factors.append(x)
	return factors

def primes(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

def generate(x):
	for i in x:
		if not primes(i + x[-1]/i):
			return False
	return True

total = 0
for i in range(2,100000000,2):
	if i % 4 != 0:
		if generate(divisors(i)):
			total+=i
			print(i)

print(total)

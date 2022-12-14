
def primes(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

def prime_factors(x):
	count = 0
	for i in range(2,int(x//2)+1):
		if (x % i) == 0 and primes(i):
			count+=1

	return count
num = 0
for i in range(2,1000000):
	
	if prime_factors(i) == 4:
		num+=1
		if num == 4:
			print(i-3)
			break
	else:
		num = 0
	print(num)
def primes(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

count = 1
j = 3
while count < 10001:
	if primes(j):
		count+=1
	j+=1
print(j)

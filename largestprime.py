def isprime(x):
	for i in range(2,int(x**0.5)+1):
		if (x % i) == 0:
			return False
	return True
big = 0
for j in range(2,int(600851475143**0.5)+1):
	if isprime(j):
		if (600851475143 % j == 0) and (j > big):
			big = j
print(big)
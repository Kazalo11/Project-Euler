def primes(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

def truncate(x):
	x = str(x)[:-1]
	return int(x)


def divisible(x):
	if x < 10:
		return True
	y = sum([int(i) for i in x])
	return x % y == 0

count = 0

def harshad(x):
	


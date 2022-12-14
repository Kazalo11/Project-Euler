def divisors(x):
	numbers = []
	for i in range(1,x//2+1):
		if (x % i == 0):
			numbers.append(i)
	numbers.append(x)
	return numbers

def primes(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

count = 0
generate = True
for i in range(1,100000000):
	test = divisors(i)
	for j in range(0,len(test)//2+1):
		extra = test[j] + test[-1]/test[j]
		if not primes(test[j]) or not primes(extra):
			generate = False
	if generate:
		count+= test[-1]
	generate = True
	print(count)
print(count)


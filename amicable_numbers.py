def factors(x):
	total = 0
	for i in range(1,x//2+1):
		if x % i == 0:
			total+=i
	return total

amicable = 0
for i in range(2,10000):
	if i == factors(factors(i)) and i != factors(i):
		amicable+=i
print(amicable)
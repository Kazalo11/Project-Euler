
import math


def split(x):
	total = 0
	x = [int(i) for i in str(x)]
	for j in x:
		total += math.factorial(j)
	return total

def chain(n):
	if n == 145:
		return 1
	count = []
	while n not in count:
		count.append(n)
		n = split(n)
	return len(count)

num = 0	
for i in range(2,1000000):
	if chain(i) == 60:
		num+=1
print(num)





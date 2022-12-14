import math
def digit(x):
	y = [int(i) for i in str(x)]
	total = 0
	for i in y:
		total+= math.factorial(i)
	return x == total

num = 0
for i in range(3,1000000):
	if digit(i):
		num+=i
print(num)

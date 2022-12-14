import math
def max_square(n):
	for i in range(n,0,-1):
		if (math.sqrt(i).is_integer()) and (n % i == 0):
			return i

total = 0
for i in range(1,100001):
	total+= max_square(i)
	
print(total)
	
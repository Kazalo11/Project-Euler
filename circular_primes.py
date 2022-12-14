import math
def isprime(x):
	for i in range(2,int(x**0.5)+1):
		if (x % i) == 0:
			return False
	return True


def circular(x):
	y = [int(i) for i in str(x)]
	length = len(y)
	y = y+y
	for i in range(length):
		num = y[i:i+length]
		new_num = int("".join(map(str, num)))
		if not isprime(new_num):
			return False
	return True


total = 0
for i in range(2,1000000):
	if circular(i):
		total+=1
print(total)
	

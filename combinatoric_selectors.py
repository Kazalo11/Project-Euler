import math

def comb(x,y):
	return (math.factorial(x)/(math.factorial(y)*math.factorial(x-y)))

total = 0

for i in range(10,101):
	for j in range(0,i):
		if comb(i,j) > 1000000:
			total+=1

print(total)
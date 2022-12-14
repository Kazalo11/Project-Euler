import math
def digits(n):
	return int(math.log10(n))+1

count = 1
total = 0
for i in range(1,10):
	while digits(math.pow(i,count)) >= count:
		if digits(math.pow(i,count)) == count:
			total+=1
			count+=1
	count=1
print(total)



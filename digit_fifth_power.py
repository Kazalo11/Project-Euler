def powers(x):
	y = [int(i) for i in str(x)]
	total = 0
	for i in y:
		total+= pow(i,5)
	return total == x

num = 0
for i in range(2,1000000):
	if powers(i):
		num+=i

print(num)
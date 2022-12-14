def chain(x):
	while True:
		total = 0
		x = [int(i)**2 for i in str(x)]
		x = sum(x)
		if x == 1 or x == 89:
			return x

count = 0
for i in range(1,10000000):
	if chain(i) == 89:
		count+=1
print(count)


def reversible(x):
	x = x + int(str(x)[::-1])
	if x % 2 == 0:
		return False
	x = [int(i) for i in str(x)]
	for i in x:
		if i % 2 == 0:
			return False
	return True

total = 0
for i in range(0,1000):
	if reversible(i):
		total+=1

print(total)
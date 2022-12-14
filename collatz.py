def collatz(x):
	count = 1
	while x != 1:
		if x % 2 == 0:
			x = x//2
		else:
			x = 3*x+1
		count+=1
	return count


big = 0
number = 1
for i in range(2,1000000):
	if collatz(i) > big:
		big = collatz(i)
		number = i

print(number)

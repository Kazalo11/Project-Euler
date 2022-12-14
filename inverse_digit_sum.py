from cgitb import small


def sum_digits(x):
	digits = [int(i) for i in str(x)]
	return sum(digits)


def smallest_num(x):
	i = 1
	while True:
		if sum_digits(i) == x:
			return i
			break
		else:
	
			i+=1

def summation(k):
	total = 0
	for i in range(1,k+1):
		total+= smallest_num(i)
	return total

def fib():
	start = [0,1]
	i = 1
	while len(start) <= 90:
		number = start[i] + start[i-1]
		start.append(number)
		i+=1
	return start

sequence = fib()
overall = 0
for i in range(2,91):
	overall+=summation(sequence[i])
		
print(overall % 1000000007)




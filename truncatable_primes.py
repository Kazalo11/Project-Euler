def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n % f == 0: return False
		if n % (f+2) == 0: return False
		f += 6
	return True  

def truncate(x,y):
	x = [int(i) for i in str(x)]
	if y == "r":
		x = x[:-1]
	elif y == "l":
		x = x[1:]
	x = int(''.join(map(str,x)))
	return x

total = 0
count = 0
def test(x):
	y = x
	while x > 10:
		if is_prime(x):
			x = truncate(x,"l")
		else:
			return False
	while y > 10:
		if is_prime(y):
			y = truncate(y,"r")
		else:
			return False
	return (is_prime(x) == True and is_prime(y) == True)
	


for i in range(11,1000000):
	if test(i):
		total+=i
		count+=1
	if count == 11:
		break	
	print(count)
print(total)
	
	
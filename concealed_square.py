def compare(x):
	x = str(x)
	if len(x) != 19:
		return False
	x = x[::2]
	return x == '1234567890'

for i in range(10**9,10**10):
	if compare(i**2):
		print(i)

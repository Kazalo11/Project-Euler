def reverse(x):
	x = str(x)
	if x == x[::-1]:
		return True
	else:
		return False

big = 0
for i in range(100,1000):
	for j in range(100,1000):
		if reverse((i*j)) and ((i*j) > big):
			big = i*j
print(big)
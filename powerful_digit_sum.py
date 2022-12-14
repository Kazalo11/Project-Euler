def digit_sum(x):
	x = str(x)
	total = 0
	for i in x:
		total+=int(i)
	return total

maxi = 0
for i in range(2,100):
	for j in range(2,100):
		y = pow(i,j)
		if maxi < digit_sum(y):
			maxi = digit_sum(y)
print(maxi)
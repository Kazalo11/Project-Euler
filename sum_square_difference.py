
sum_square = 0
for i in range(101):
	sum_square+=(i**2)
square_sum = 0
for j in range(101):
	square_sum+=j
print(square_sum**2 - sum_square)
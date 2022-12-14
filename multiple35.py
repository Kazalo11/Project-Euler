fibonacci = 0
first = 1
second = 2
while first <= 4000000:
	if (first % 2) == 0:
		fibonacci+=first
	elif (second % 2) == 0:
		fibonacci+=second
	print(first,second)
	first+=second
	second+=first
	
print(fibonacci)
def factors(x):
	count = 0
	if x == 1:
		return(int(1))
	for i in range(1,int(x**0.5)+1):
		if i*i == x:
			count+=1
		elif x % i == 0:
			count+=2
	return count

j = 1 
start = 1
x = factors(start)
while x < 500:
	j+=1
	start+=j
	x = factors(start)
	print(x)
print(start)


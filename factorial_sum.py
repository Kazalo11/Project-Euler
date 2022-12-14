i = 1
j = 1
count = 1
while len(str(i)) < 1000:
	i+=j
	j+=i
	count+=2
	
print(count,len(str(i)))
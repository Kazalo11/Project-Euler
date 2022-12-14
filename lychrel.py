num = 0

def reversal(x):
	return x + int(str(x)[::-1])

lychrel = True
for i in range(1,10000):
	lychrel = True
	for j in range(49):
		i = reversal(i)
		if str(i) == str(i)[::-1]:
			lychrel = False
			break
	if lychrel:
		num+=1
		
	
print(num)

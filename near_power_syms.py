def power_sum(x):
	k =1
	t = sum([int(i)**k for i in str(x)])
	if t == 1 or t == 2:
		return False
	while t <= x+1:
		k+=1
		t = sum([int(i)**k for i in str(x)])
		if abs(t-x)==1:
			return True
	return abs(t-x)== 1

max = 0
for i in range(12,1000000):
	if power_sum(i):
		max+=i
print(max)
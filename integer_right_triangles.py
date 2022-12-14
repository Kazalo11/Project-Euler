from typing import Counter


def right_angles(x,p):
	count = 0
	for i in range(x,0,-1):
		t = (x**2 - i**2)**0.5
		if t.is_integer():
			if i+t+x == p:
				count+=1
	return count//2


total = 0
num = 0
for i in range(100,1001):	
	equal = 0
	for j in range(1,i):
		equal+= right_angles(j,i)
	if equal > total:
		total = equal
		num = i

print(num)


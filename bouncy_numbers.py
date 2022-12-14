from turtle import back


def bouncy(x):
	x = [int(i) for i in str(x)]
	forward = sorted(x)
	backward = sorted(x,reverse=True)
	return (x == forward or x == backward)

count = 0

for i in range(1,100000000):
	if not bouncy(i):
		count+=1
	if count/i >= 0.99:
		print(count)
		print(i)
		break
	
	


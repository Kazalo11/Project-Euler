from itertools import permutations
test = [0,1,2,3,4,5,6,7,8,9]
test2 = [0,1,2]
alpha = [8,5,4,9,1,7,6,3,2,0]

def alpha_position(x):
	return alpha.index(x)
def num_order(x):
	forward = sorted(x)
	backward = sorted(x,reverse=True)
	if list(x) == forward or list(x) == backward:
		return True
	return False

def alpha_order(x):
	forward = sorted(x,key=lambda i: alpha_position(i))
	backward = sorted(x, reverse=True, key = lambda i: alpha_position(i))
	if list(x) == forward or list(x) == backward:
		return True
	return False
count = 0
for i in range(2,3):
	poss = list(permutations(test2,i+1))
	for number in poss:
		if num_order(number) or alpha_order(number):
			count+=1
			print(number)
		if count == 1000000:
			print(number)
			exit

print(count)
		



	

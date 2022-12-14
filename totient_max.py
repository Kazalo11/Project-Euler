import math
#too slow need to optimise it
def n_phi_function(x):
	count = 1
	for i in range(2,x):
		if math.gcd(x,i) == 1:
			count+=1
	return x/count

answer = 0
biggest = 0

for i in range(2,1000000):
	print(i)
	test = n_phi_function(i)
	if test > biggest:
		biggest = test
		answer = i

print(f'Answer is {answer}')



from itertools import permutations

primes = [2,3,5,7,11,13,17]
poss = list(permutations([0,1,2,3,4,5,6,7,8,9]))

def create_number(num,index):
	number = int(''.join(map(str,num[index:index+3])))
	return number

total = 0
substring = True
for i in poss:
	for j in range(len(primes)):
		number = create_number(i,j+1)
		if (number % primes[j] != 0):
			substring = False
	if substring:
		total = total + int(''.join(map(str,i)))
	substring = True
			

			

print(total)

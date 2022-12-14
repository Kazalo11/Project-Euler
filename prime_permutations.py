from itertools import permutations


def primes(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True
#
# def confirm(x):
# 	new = []
# 	for i in x:
# 		i = int(''.join(map(str,x)))
# 		if primes(i):
# 			new.append(i)
# 	return new
#
#
#
# found = False
# numbers = []
# long = []
# for i in range(1000,10000):
# 	if primes(i):
# 		numbers.append(i)
# 		long.append(sorted(int(x) for x in list(str(i))))
#
# following = []
# for j in long:
# 	if j not in following:
# 		following.append(j)
#
# for test in following:
# 	combin = list(permutations(test))
# 	print(confirm(combin))
#

frequency = dict()
for i in range(1000,10000):
	if primes(i):
		temp = str(i)
		temp = ''.join(sorted(temp))
		if temp in frequency.keys():
			frequency[temp].append(i)
		else:
			frequency[temp] = [i]


def test_sequence(x):
	count = 0
	digits = set()
	if len(x) < 3:
		return False
	for j in range(len(x)-1):
		for k in range (j+1,len(x)):
			test = x[k]-x[j]
			if test == 3330:
				count+=1
				digits.add(x[k])
				digits.add(x[j])
			if count==2:
				return digits
	return False

for values in frequency.values():
	if test_sequence(values):
		print(test_sequence(values))






		
		

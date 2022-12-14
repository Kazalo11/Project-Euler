from itertools import permutations

def generate_perm(x):
	x = [int(i) for i in str(x)]
	perms = list(permutations(x))
	return perms

def check_cubic(x):
	count = 0
	for i in x:
		number = int(''.join(map(str,i)))
		if number**(1/3).is_integer():
			count+=1
	return count


for i in range(300,400):
	total = 0
	number = i**3
	numbers = generate_perm(number)
	total += check_cubic(numbers)
	if total == 3:
		print(i)
		break


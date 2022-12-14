count = 0

def palindrome(x):
	x = str(x)
	return x == x[::-1]


for i in range(1000000):
	if palindrome(i):
		x = bin(i)[2:]
		if palindrome(x):
			count+=i
print(count)
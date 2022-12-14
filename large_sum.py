f = open('numbers.txt','r')
total = 0
for x in f:
	total+=int(x)
print(total)
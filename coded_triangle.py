with open('p042_words.txt','r') as f:
	f = f.read()
	names = [x.strip('""') for x in f.split(',')]


def solve(x):
	return (-1+(1+8*x)**0.5)/(2*1)


count = 0

for i in names:
	total = 0
	for j in i:
		total+= ord(j)
		total-=64
	if solve(total).is_integer():
		count+=1
	
print(count)
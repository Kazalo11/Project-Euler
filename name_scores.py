with open('p022_names.txt','r') as f:
	f = f.read()
	names = [x.strip('""') for x in f.split(',')]

names.sort()
total = 0
for i,j in enumerate(names,start=1):
	count = 0
	for x in j:
		count+= ord(x)
		count-=64
	total+=(count*i)

print(total)



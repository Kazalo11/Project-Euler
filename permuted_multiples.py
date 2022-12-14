def compare(items):
	for i in range(len(items)-1):
		if sorted(str(items[i])) != sorted(str(items[i+1])):
			return False
	return True
		

adding = [1,2,3,4,5,6]
start = [1,2,3,4,5,6]
while not compare(start):
	start = [x+y for x,y in zip(adding,start)]

print(start[0])




distinct = set()
for i in range(2,101):
	for j in range(2,101):
		distinct.add(pow(i,j))

print(len(distinct))
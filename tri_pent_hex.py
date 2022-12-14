numbers = dict()

def triangle(x):
	return x*(x+1)*0.5
def pentagon(x):
	return x*(3*x-1)*0.5
def hexagon(x):
	return x * (2*x-1)

for i in range(200,10000000):
	if triangle(i) not in numbers:
		numbers[triangle(i)] = 1
	else:
		numbers[triangle(i)]+=1
	if pentagon(i) not in numbers:
		numbers[pentagon(i)] = 1
	else:
		numbers[pentagon(i)] +=1
	if hexagon(i) not in numbers:
		numbers[hexagon(i)] = 1
	else:
		numbers[hexagon(i)] +=1
	for key,value in numbers.items():
		if value == 3:
			print(key)
			exit


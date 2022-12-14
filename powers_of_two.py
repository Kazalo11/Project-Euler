count = 0
correct = 0
for i in range(5000000):
	num = 2**i
	num = str(num)
	if num.startswith("123"):
		count+=1
	if count == 678910:
		correct = i
		break

print(correct)
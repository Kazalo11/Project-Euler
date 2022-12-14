highest = 0
count = 0
line_number = 0
import math


f = open('p099_base_exp.txt') 
for line in f:
	count+=1
	line = line.rstrip('\n')
	number = line.split(',')
	test = int(number[1])*math.log(int(number[0]))
	if test > highest:
		highest = test
		line_number = count
print(line_number)
		



	
        
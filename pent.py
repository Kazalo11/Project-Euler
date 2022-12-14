from cgi import test
from turtle import pen
import numpy as np
def pentagon(x):
	return x*(3*x-1)*0.5

def test_pent(x):
	sol = (np.sqrt(24*x+1)+1)/6
	return sol.is_integer()

pent_numbers = []
length = 10000
for i in range(1,length):
	pent_numbers.append(pentagon(i))
diff = 1e12
add_count = 0
minus_count = 0
# for i in range(length-1):
# 	for j in range(i+1,length):
# 		if test_pent(pent_numbers[i]+pent_numbers[j]) and test_pen(pent_numbers[i] - pent_numbers[j]) in pent_numbers:
# 				count+=1
# 				if abs((pent_numbers[i] - pent_numbers[j])) < diff:
# 					diff = abs((pent_numbers[i] - pent_numbers[j]))
# print(count)
# print(diff)

for i in range(length-2):
	for j in range(i+1,length-1):
		add = pent_numbers[i] + pent_numbers[j]
		minus = pent_numbers[j]-pent_numbers[i]
		if test_pent(minus):
			add_count+=1
			if test_pent(add):
				minus_count+=1
				if minus < diff:
					diff = minus
				break
print(add_count)
print(minus_count)
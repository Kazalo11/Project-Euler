import numpy as np
total = 1
for i in range(1,21):
	if total% i != 0:
		total = np.lcm(total,i)
print(total)
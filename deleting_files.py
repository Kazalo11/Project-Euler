import os

for filename in os.listdir():
	if filename.startswith('P1B'):
		print(filename)
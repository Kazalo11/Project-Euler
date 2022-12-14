from math import prod
with open('grid.txt') as f:
    data = [list(map(int, line.strip().split())) for line in f]

largest = 0
for i in range(20):
    for j in range(17):
        if prod(data[i][j:j+4]) > largest:
            largest = prod(data[i][j:j+4])


for i in range(17):
    for j in range(20):
        item = [data[i][j],data[i+1][j],data[i+2][j],data[i+3][j]]
        if prod(item) > largest:
            largest = prod(item)

for i in range(20):
    for j in range(20):
        try:
            item = [data[i][j], data[i + 1][j+1], data[i + 2][j+2], data[i + 3][j+3]]
            if prod(item) > largest:
                largest = prod(item)
            item = [data[i][j], data[i + 1][j-1], data[i + 2][j-2], data[i + 3][j-3]]
            if prod(item) > largest:
                largest = prod(item)
        except:
            print("Out of bounds")

print(largest)



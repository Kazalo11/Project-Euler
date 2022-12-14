def square(x):
    return (x ** 0.5) % 1 != 0


D = list(filter(square, range(10000)))

print(D)

from fractions import Fraction

denominator = 2
count = 0
for i in range(1,1001):
    fraction = Fraction(1 + 1/denominator).limit_denominator(10000000000000)
    denominator = 2 + 1/denominator
    if (len(str(fraction.numerator)) > len(str(fraction.denominator))):
        count+=1
print(count)



import math
answer = 28433*(2**7830457)+1
digits = []
digit = 0
while len(digits) <= 10:
    digit = answer % 10
    digits.append(digit)
    answer /= 10
print(digits)

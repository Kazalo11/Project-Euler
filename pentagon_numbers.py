from math import sqrt
def pentagon(x):
    return x*(3*x-1)/2.0

def test_pent(x):
    n = (1 + sqrt(24 * x + 1)) / 6
    return (n- int(n) == 0)

pent_numbers = [pentagon(i) for i in range(100000000)]
minimum = 1e16

for i in range(1,100000000):
    for j in range(i+1,99):
        total = pent_numbers[i] + pent_numbers[j]
        minus = pent_numbers[j]-pent_numbers[i]
        if test_pent(total) and test_pent(minus):
            minimum = min(minimum,minus)
            print(pent_numbers[i],pent_numbers[j])

print(minimum)

numerals = []
with open('p089_roman.txt') as f:
    for x in f:
        numerals.append(x.rstrip())

conversion = {
    "M": 1000,
    "CM":900,
    "D": 500,
    "CD":400,
    "C": 100,
    "XC":90,
    "L": 50,
    "XL":40,
    "X": 10,
    "IX":9,
    "V": 5,
    "IV":4,
    "I": 1,
}


def roman_to_decimal(x):
    count = 0
    for i in range(len(x) - 1):
        if conversion[x[i]] < conversion[x[i+1]]:
            count-=conversion[x[i]]
        else:
            count+=conversion[x[i]]
    count+=conversion[x[-1]]
    return count

def convert_roman(x):
    roman_numeral = ""
    for key,value in conversion.items():
        div = x // value
        x %= value
        roman_numeral = roman_numeral + div*key
        if x == 0:
            return roman_numeral

total = 0

for numeral in numerals:
    number = roman_to_decimal(numeral)
    minimum_numeral = convert_roman(number)
    total = total + len(minimum_numeral) - len(numeral)

print(total)

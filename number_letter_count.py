conversion = {
    1: "one",
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}
count = 0
for i in range(1,1000):
    hundreds = i//100
    remainder = i % 100
    if hundreds != 0:
        count += len(conversion[hundreds])
        count += len('hundred')
        if remainder == 0:
            continue
        else:
            count += len('and')
    if remainder % 10 == 0 or remainder < 20:
        count += len(conversion[remainder])
    else:
        tens = (remainder // 10)*10
        count += len(conversion[tens])
        remainder %= 10
        print(i)
        count += len(conversion[remainder])

count += len('onethousand')
print(count)


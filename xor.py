import string

with open('p059_cipher.txt') as f:
    numbers = [int(i) for i in f.read().split(',')]

passcode = []


result = string.ascii_lowercase
word = ""
for a in result:
    for b in result:
        for z in result:
           word = "god"
           answer = []
           solution = [c for c in word]
           i=0
           for number in numbers:
            test = number ^ ord(solution[i])
            answer.append(chr(test))
            if i == 0:
                i=1
            elif i==1:
                i=2
            elif i== 2:
                i = 0
        print(''.join(answer))
        print("----------------------------------------------------------")





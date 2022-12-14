from math import floor
from decimal import *
import numpy as np



def concentation(x):
    answer = "2."
    for i in range(1,len(x)):
        answer+=str(x[i])
    return Decimal(answer).quantize(Decimal('1e-24'))


i = 2.1
b = [i]
a = [floor(i)]
while concentation(a) != b[0]:
    i+=1e-24
    b = [i]
    a = [floor(i)]
    temp = 0
    for n in range(1,20):
        temp = floor(b[n-1])*(b[n-1]-floor(b[n-1])+1)
        b.append(temp)
        a.append(floor(temp))
    if concentation(a) == b[0]:
        print(b[0])
        exit



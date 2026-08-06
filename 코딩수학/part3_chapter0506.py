import numpy as np
from fractions import Fraction

a = 10
c = 0
while a > 0:
    c += a
    #print(c)
    #print(a)
    a -= 1
    
#print(c)

x = (5+3) / 2
print(x)

def linear_eq(a, b, c):
    if a == 0:
        if b == 0:
            return "No solution"
        else:
            return -c / b
    else:
        return (-b + np.sqrt(b**2 - 4*a*c)) / (2*a), (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)

print(linear_eq(1, 2, -3))

ㅇㄷㄹ 
import numpy as np
from  fractions import Fraction

print(Fraction(5/2))
print(Fraction(5, 2))  # 분자, 분모를 직접 지정하여 생성
print(Fraction(2.5))

print(Fraction(7, 9).numerator)
print(Fraction(7, 9).denominator)

print(Fraction(2, 4))  # 약분되어 1/2로 출력

print(Fraction(1, 4) + Fraction(4, 7))

print(Fraction(1, 4)**2)

print(np.sqrt(4))  # 제곱근 계산

a = Fraction(9, 16)
a = float(a)  # Fraction을 float으로 변환
print(a)
print(np.sqrt(a))  # 제곱근 계산
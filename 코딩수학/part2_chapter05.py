import numpy as np
import math as math

a = [1, 2, 3, 4, 5]
b = np.array(a)

print(type(b))
print(b[1:3])

c = b + 5
print(c)
print(a * 2)
print(b * 2)

d = np.array([1, 2, 3])
e = np.array([4, 5, 6])
print(np.multiply(d, e))
print(np.argmax(d))
print(np.argmin(e))

print('난수 만들기')
f = np.random.randint(1, 46, 6)
print(f)


def diIsPrime(num):
    #num이 소수인지 판별하여 반환한다.
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError("정수만 허용됩니다.")
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2

    for i in range(3, math.isqrt(num) + 1, 2):
        if num % i == 0:
            return False
    return True

primes = []
for i in range(1, 101):
    if diIsPrime(i):
        primes.append(i)
print(primes)
print(len(primes))
gap = 0
gap_pair = (0, 0)
for i in range(len(primes)-1):
    k = primes[i+1] - primes[i]
    if gap < k:
        gap = k
        gap_pair = (primes[i], primes[i+1])

print(f"가장 큰 소수의 차이는 {gap}이고, 그 소수 쌍은 {gap_pair}입니다.")

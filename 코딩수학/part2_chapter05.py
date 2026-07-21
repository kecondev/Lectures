import numpy as np
import math as math
import diMath as diM

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

#print(f"가장 큰 소수의 차이는 {gap}이고, 그 소수 쌍은 {gap_pair}입니다.")

def diPrimeFactor(number):
    """정수를 소인수분해하여 소인수 목록을 반환합니다."""
    if number < 2 or not isinstance(number, int):
        raise ValueError("2 이상의 정수를 입력해주세요.")

    factors = []
    divisor = 2

    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1

    if number > 1:
        factors.append(number)

    return factors

print(diPrimeFactor(60))  # 예제: 60의 소인수분해 결과 출력

def factorization(n):
    """ 약수 구하기 """
    if n < 1 or not isinstance(n, int):
        raise ValueError("1 이상의 정수를 입력해주세요.")

    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)

    return sorted(factors)

print(factorization(60))  # 예제: 60의 약수 구하기

from math import isqrt


def divisors(n):
    """1 이상의 정수가 가진 모든 약수를 오름차순으로 반환합니다."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("1 이상의 정수를 입력해주세요.")

    small = []
    large = []

    for divisor in range(1, isqrt(n) + 1):
        if n % divisor == 0:
            small.append(divisor)

            paired_divisor = n // divisor
            if divisor != paired_divisor:
                large.append(paired_divisor)

    return small + large[::-1]

print(divisors(60))  # 예제: 60의 약수 구하기

def gcd(a, b):
    """두 정수의 최대공약수를 반환합니다."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("정수를 입력해주세요.")

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a

print(gcd(-20, 48))  # 예제: 48과 18의 최대공약수 구하기

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

print(lcm(36, 96))  # 예제: 48과 18의 최대공약수 구하기
print(lcm(4, 7))  # 예제: 48과 18의 최대공약수 구하기

from functools import reduce

def lcm_many(numbers):
    return reduce(lcm, numbers)

print(lcm_many([4, 6, 8]))  # 24


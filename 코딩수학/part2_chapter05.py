import numpy as np

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
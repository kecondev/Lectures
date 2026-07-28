import numpy as np

a = [1, 2, 3, 4, 5]
b = np.array(a)
#print(a)
#print(type(a))
#print(b)
#print(type(b))

c = np.array([[1, 2, 3, 4, 5], 
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]])
#print(c.shape)

#print(c[1, 1])
#print(c[:, 3])
#print(c[1, :])
#print(c[2:4, 1:3])

c = range(1, 26)
c = np.array(c)
#print(c.shape)
#print(c)
c = c.reshape(5, 5)
#print(c)

#print(np.zeros(5))
#print(np.ones((3, 5)))

d = range(1, 10, 2)
d = np.array(d)
#print(d)

a = np.zeros((5, 5))
for idx1, val1 in enumerate(range(0, 25, 5)):
    for idx2, val2 in enumerate(range(1, 10, 2)):
        a[idx1, idx2] = val1 = val2

#print(a)

b = [3, 4, 5, 6, 7]
#print(type(b))
#print(b.index(7))

c = np.array(b)
#print(np.where(c == 7))
#print(c[4])

e = [3, 4, 5, 3, 7, 8, 3, 9]
f = np.array(e)
g = np.where(f == 3)
print(g)
print(g[0])
print(g[0][2])

h = np.array([-3, 4, 7, 2, 0])
print(np.max(h))
print(np.min(h))

c = range(1, 26)
c = np.array(c)
c = c.reshape(5, 5)
print(np.max(c))
print(np.where(c == np.max(c)))

print(np.arange(10))
print(np.arange(10) + 1)
e = [1, 2, ['Math', 'Coding']]

print(type(e))
print(len(e))
print(e.count(1))

print(e[2][1])
print(e[2][:])

a = [1, 2, 3]
b = [4, 5, 6]

print(a * 2 + b * 2)

a[2] = 9

print(a)

del a[2]
print(a)
a.remove(2)
print(a)
a = a + [2] + [3]
print(a)
a.reverse()
print(a)
print(a.index(2))
print(1 in a)
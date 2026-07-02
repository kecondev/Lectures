def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

print(plus(3, 4))
#print(minus("a", "b"))

def union(a, b):
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    c = c + b
    return sorted(c)

print(union([1, 2, 3], [2, 3, 4]))
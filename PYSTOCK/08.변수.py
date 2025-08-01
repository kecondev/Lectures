a = 10

def test1():
    b = a
    c = 20
    print(a)
    print(b)
    b = 15
    print(b)
    print(a)

print(a)

def test2():
    globals()['a'] = 30
    print(a)

test1()
test2()
print(a)
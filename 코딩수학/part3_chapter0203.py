a = [2*x for x in [3,5,6,8,9]]
print(a)
b = [x%7 for x in range(10, 20)]
print(b)
c = [2*x for x in [3,5,6,8,9] if x%2 == 0]
print(c)

a = 3
b = 10
print((a > 0) and (b > 5))

for i in range(2, 100):
    if (i%4 == 1) and (i%5 == 1) and (i%6) == 1:
        print(i)

for i in range(1, 31):
    if (i%2 == 0) or (i%3 == 0):
        print(i)
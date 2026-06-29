a = [1,2,3,1,2,3]
new_a = []

for i in a:
    if i not in new_a:
        new_a.append(i)
print(new_a)

b = [3,4,5]
c = []

for i in new_a:
    if i not in b:
        c.append(i)

c = c + b
c.sort()

print(c)

d = new_a.copy()
print(d)

for i in b:
    if i in new_a:
        d.remove(i)

print(d)
a = [0,1,2,3,4]
for i in a:
    print(i)

b = 0
for i in a:
    b += i
print('리스트 a의 요소합은 {} 입니다.'.format(b))

c = []
for i in a:
    c.append(i)
print(c)

d = [10, 20, 30, 40, 50]
ad = []
for i in a:
    for j in d:
        ad.append(i+j)
print(ad)
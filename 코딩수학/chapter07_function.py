#더하기
def plus(a, b):
    if isinstance(a, str) or isinstance(b, str):
        raise TypeError("문자는 허용되지 않습니다.")
    return a + b
#print(plus('a', 4))

#빼기
def minus(a, b):
    if isinstance(a, str) or isinstance(b, str):
        raise TypeError("문자는 허용되지 않습니다.")
    return a - b
#print(minus(3, 4))

#합집합
def union(a, b):
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    c = c + b
    return sorted(set(c))
#print(union([1, 1, 5], [5, 5, 2]))

def union1(a, b):
    # 리스트의 합집합을 정렬하여 반환한다.
    #return sorted(set(a) | set(b))
    #return sorted(set(a).union(set(b)))
    return sorted(set(a).union(b))
#print(union1([1, 1, 5], [5, 5, 2]))

def intersection(a, b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    #return sorted(c)
    return sorted(set(a).intersection(b))
#print(intersection([1, 2, 5], [5, 4, 2]))

def diDifference(a, b):
    return sorted(set(a).difference(b))
print(diDifference([1, 2, 5, 1], [5, 4, 2, 2]))

def union(*lists):
    """여러 리스트의 합집합을 정렬된 리스트로 반환한다."""
    result = set()
    for lst in lists:
        result.update(lst)
    return sorted(result)

a = [1, 2, 3]
b = [3, 4, 5]
c = [5, 6, 7]
d = [2, 7, 8]

print(union(a, b, c, d))
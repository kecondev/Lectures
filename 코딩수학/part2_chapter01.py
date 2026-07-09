a = [3,4,5,6,7]
print(type(1 in a))

b = 'apple'
c = ['tomato', 'potato', 'banana', 'apple', 'grape']
print(b in c)
print('watermelon' in c)

def diOdd_Even(num):
    #num이 홀수인지 짝수인지 판별하여 반환한다.
    if not isinstance(num, int):
        raise TypeError("정수만 허용됩니다.")
    return "홀수" if num % 2 != 0 else "짝수"
print(diOdd_Even(3))

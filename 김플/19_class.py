class User:
    name = ""
    age = 0
    def __init__(self, name, age):
        User.name = name
        User.age = age

    def greet(self):
        print(f"안녕하세요, 제 이름은 {User.name}이고, 나이는 {User.age}세입니다.")

user_1 = User("이상용", 52)
user_1.greet()

user_2 = User("김혜경", 46)
user_2.greet()

temp = [1, 2, 3, 4, 5]

print(type(temp))
print(type(user_1))
# def greet(username='name'):
#     print('Hello, ' + username + '!')
# greet(input('Please enter your name: '))

# def pet(type='dog', name='Tom'):
#     print('I have a ' + type + ', his name is ' + name +'.')
# pet()

# 有返回值的函数
# def add(number1, number2):
#     return number1 + number2
# print('计算结果为：' + str(add(int(input('被加数：')),int(input('加数：')))))

# 传递列表
# def add(numbers):
#     return numbers[0] + numbers[1]
# numbers = [int(input('被加数：')),int(input('加数：'))]
# print(add(numbers))

# 禁止函数修改列表
# def add(numbers):
#     numbers[0] += 1
#     numbers[1] -= 1
#     return numbers[0] + numbers[1]
# numbers = [int(input('被加数：')),int(input('加数：'))]
# print(numbers)
# add(numbers[:])
# print(numbers)

# 任意数量实参
def add(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(add(1,2,3,4,5,6))


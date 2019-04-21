# number = 0
# while int(number) != 15:
#     print('This number is ' + str(number))
#     number = input('guess the number: ')
# print('You are right!')

# active = True
# while active == True:
#     message = input('Please enter words: ')
#     if message == 'quit':
#         active = False

# 使用while循环录入一个字典
dictionary = {}
while True:
    key = input("Please enter the KEY, or enter 'exit' to exit: ")
    if key == 'exit':
        break
    value = input('Please enter the VALUE: ')
    dictionary[key] = value
print(dictionary)

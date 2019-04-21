# 读整个文件
# with open(r'M:\code\PycharmProjects\PythonStudy\chapter10\files\test.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# 逐行读取
# with open('files/test.txt') as file_object:
#     for line in file_object:
#         print(line)

# 写文件
# filename = 'files/test2.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write("This is a file...")

# 写json数据
import json
numbers = {1:2, 2:3}
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# 读json数据
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(type(numbers))
for key, value in numbers.items():
    if value > 2:
        print('key: ' + key)
        print('value: ' + str(value))

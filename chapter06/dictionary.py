alien_0  = {'color': 'green', 'point': 5}
alien_0['x'] = 20
alien_0['y'] = 20
# print(alien_0['x'])
# alien_0['x'] = 10
# print(alien_0['x'])

# 删除
# del alien_0['point']
# print(alien_0)

# 遍历
# for key, value in alien_0.items():
#     print('key: ' + key)
#     print('value: ' + str(value)+'\n')

# 遍历键
# for key in alien_0.keys():
#     print('key: ' + key)
# for key in sorted(alien_0.keys(),reverse=True):
#     print('key: ' + key)

# 遍历值
# for value in set(alien_0.values()):
#     print('value: ' + str(value))

# 列表嵌套字典
# alien_1  = {'color': 'blue', 'point': 10, 'x': 20}
# alien_2  = {'color': 'red', 'point': 5, 'x': 30}
# alien_3  = {'color': 'yellow', 'point': 12, 'x': 40}
# aliens = [alien_1, alien_2, alien_3]
# for alien in aliens:
#     print('===================')
#     for key, value in alien.items():
#         print('key: ' + key)
#         print('value: ' + str(value))
#         print('---------')

# 字典嵌套列表
# books = ['book1', 'book2', 'book3']
# pens = ['pen1', 'pen2']
# schoolbag = {'books': books, 'pens': pens}
# for key, value in schoolbag.items():
#     print('-----------')
#     print('key: ' + key)
#     for thing in value:
#         print(thing)

# 字典嵌套字典
jf = {'name': 'wqf', 'weight': 100, 'height': 180}
vb = {'name': 'ybh', 'weight': 110, 'height': 175}
sg = {'name': 'wsg', 'weight': 120, 'height': 170}
ws = {'name': 'ys', 'weight': 130, 'height': 165}
VBs = {'jf': jf, 'vb': vb, 'sg': sg, 'ws': ws}
for thisVBKey, thisVBValues in VBs.items():
    print('==========')
    print('简称：'+thisVBKey)
    for thisVBThisKey, thisVBThisValue in thisVBValues.items():
        if thisVBThisKey == 'name':
            print('全名：'+ thisVBThisValue)
        if thisVBThisKey == 'height':
            print('身高：'+ str(thisVBThisValue))
        if thisVBThisKey == 'weight':
            print('体重：'+ str(thisVBThisValue))

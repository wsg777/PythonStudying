'''
Heros beta-0.2
Jeremy
str map 2018-4-5
'''

welcome = 'welcome to Heros world!'
mapmsg = '#######'
mapins = "\n-*- the worle is like this -*-\n %s \n the '*' is you " % (mapmsg,)
map = ['#','#','#','#','#','#','#']
instruction = '''
contrl your hero:
| 'a' for left | 'd' for right |'''

print(welcome)

name = input('input your name:')
hp = 100

if not name:
    name = 'player01'
usermsg = {'name':name,'hp':hp}

print("your hero's name is:",usermsg['name'],'Hp is:',usermsg['hp'])
print(mapins,instruction)

point = 0
while 1:
    map[point] = '*'
    print('you are here:',"".join(map))
    userinput = input('go or quit:')

    if userinput == 'd' and point < 6:
        map[point] = '#'
        point += 1

    if userinput == 'a' and point > 0 :
        map[point] = '#'
        point -= 1
    elif userinput == 'quit':
        print('goodbey!!')
        break
    else:
        print(instruction)

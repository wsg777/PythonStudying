# 模拟掷骰子
from random import randint
class Die():
    """表示一个骰子的表"""
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.number_sides=num_sides
    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1, self.number_sides)

die1 = Die()
# 掷骰子，并将结果存储在一个列表中
results1 = []
for roll_number1 in range(10000):
    result1 = die1.roll()
    results1.append(result1)
# 掷骰子，并将结果存储在一个列表中
die2 = Die()
# 掷骰子，并将结果存储在一个列表中
results2 = []
for roll_number2 in range(10000):
    result2 = die2.roll()
    results2.append(result2)
# 求和
results3 = []
for i in range(10000):
    result3 = results1[i] + results2[i]
    results3.append(result3)

# 分析结果
frequencies = []
for value in range(2, die1.number_sides*2+1):
    frequency = results3.count(value)
    frequencies.append(frequency)
print(frequencies)

# 绘制直方图
import pygal
# 可视化
hist = pygal.Bar()
hist.title = "模拟同时掷两个骰子的点数之和 10000次"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "点数之和"
hist.y_title = "出现的次数"
hist.add('D6', frequencies)
hist.render_to_file('die_visvual.svg')
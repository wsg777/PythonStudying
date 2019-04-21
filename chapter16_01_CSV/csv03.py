# 绘制气温图表

import csv
filenmae = 'sitka_weather_07-2014.csv'
with open(filenmae) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 获取最高气温
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)

# 绘制气温图表
from matplotlib import pyplot as plt
plt.plot(highs, c='red')
plt.show()

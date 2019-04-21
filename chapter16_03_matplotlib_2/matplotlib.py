# 与前一个包相比，涵盖了更多时间，添加了最低气温

# 使用模块datetime
from datetime import datetime
import csv

# 获得日期和温度
filenmae = 'sitka_weather_2014.csv'
with open(filenmae) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 获取气温和日期
    highs = []
    lows = []
    dates = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
        date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(date)

# 绘制气温图表
from matplotlib import pyplot as plt
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='pink', linewidth=0.5)
plt.plot(dates, lows, c ='lightGreen', linewidth=0.5)
# 填充中间部分
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.3)
# 倾斜日期标签
fig.autofmt_xdate()
plt.savefig("test1701.png")
plt.show()

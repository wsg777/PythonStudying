# 使用模块datetime
from datetime import datetime
import csv

# 获得日期和温度
filenmae = 'sitka_weather_07-2014.csv'
with open(filenmae) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 获取最高气温和日期
    highs = []
    dates = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
        date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(date)

# 绘制气温图表
from matplotlib import pyplot as plt
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')
# 倾斜日期标签
fig.autofmt_xdate()
plt.savefig("test1601.png")
plt.show()

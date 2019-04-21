# JSON数据可视化-基本
import json
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件获取数据
datas = []
dates = []
closes = []
with open('btc_close_2017.json') as f_obj:
    datas =json.load(f_obj)
for data in datas:
    for key, value in data.items():
        if key == 'date':
            value = datetime.strptime(value, '%Y-%m-%d')
            dates.append(value)
        if key == 'close':
            value = float(value)
            closes.append(value)

# print(dates)
# print(closes)
plt.plot(dates, closes, linewidth=2)
plt.show()

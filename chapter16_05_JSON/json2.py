# JSON数据可视化-Pygal进阶-折线图
import json
from datetime import datetime
import pygal

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
print(dates)
# 顺时针倾斜20读，不显示所有标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20
# 每隔20天显示一个标签
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', closes)
line_chart.render_to_file('收盘价折线图.svg')

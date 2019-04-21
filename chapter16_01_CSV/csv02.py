# 提取并读取数据

import csv
# 从文件中获取最高气温
filenmae = 'sitka_weather_07-2014.csv'
with open(filenmae) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        highs.append(row[1])
    print(highs)


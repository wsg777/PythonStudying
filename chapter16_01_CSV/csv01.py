# 打印头文件
# import csv
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)

# 打印头文件及其位置
import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, comlumn_header in enumerate(header_row):
        print(index, comlumn_header)
# 自动计算数据

import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# edgecolors：删除颜色
# s：点的大小
# c：点的颜色
# plt.scatter(x_values, y_values, edgecolors='none', s=5, c='red')
plt.scatter(x_values, y_values, edgecolors='none', s=5, c=y_values, cmap=plt.cm.Blues)
# 保存文件
plt.savefig('squares_plot.png', bbox_inches='tight')
# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.savefig("test1504.png")
plt.show()

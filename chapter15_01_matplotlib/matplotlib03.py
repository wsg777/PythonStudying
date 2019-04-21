# 绘制散点图

import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, 100)
plt.savefig("test1503.png")
plt.show()
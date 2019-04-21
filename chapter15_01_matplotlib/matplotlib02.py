# 修改标签文字和线条粗细

import matplotlib.pyplot as plt
inout_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 设置线的宽度
plt.plot(inout_values, squares, linewidth=3)
# 设置标题
plt.title("This is Title", fontsize=24, color='red')
# 给坐标轴加上标签
plt.xlabel("This is X", color='green')
plt.ylabel("This is Y", color='green')
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("test1502.png")
plt.show()
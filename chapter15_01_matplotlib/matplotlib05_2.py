import matplotlib.pyplot as plt

from chapter15_01_matplotlib.matplotlib05 import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()
plt.figure(dpi=80, figsize=(10, 6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s=4, c=point_numbers, cmap='Reds', edgecolors='none')
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.savefig("test1505.png")
plt.show()

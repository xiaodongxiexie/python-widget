# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import permutations

import numpy as np

# %matplotlib inline

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')


x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
xx, yy = np.meshgrid(x, y)
for a, b, c in permutations([xx, yy, 0], 3):
    ax.plot_surface(a, b, c)
for a, b, c in permutations([xx, yy, 10], 3):
    ax.plot_surface(a, b, c)
ax.set_xlim3d(-10, 20, 20)
ax.set_zlim3d(-10, 20, 20)
ax.set_ylim3d(-10, 20, 20);
plt.show()
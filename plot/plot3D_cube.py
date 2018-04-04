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


def plot_opaque_cube(x=0, y=0, z=0, dx=10, dy=10, dz=10):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')


    x = np.linspace(x, x+dx, 5)
    y = np.linspace(y, y+dy, 5)
    xx, yy = np.meshgrid(x, y)
    for a, b, c in permutations([xx, yy, z], 3):
        ax.plot_surface(a, b, c)
    for a, b, c in permutations([xx, yy, z+dz], 3):
        ax.plot_surface(a, b, c)
    # ax.set_xlim3d(-dx, dx*2, 20)
    # ax.set_xlim3d(-dx, dx*2, 20)
    # ax.set_xlim3d(-dx, dx*2, 20)
    plt.title("Cube")
    plt.show()



def plot_linear_cube(x, y, z, dx, dy, dz, color='red'):
    fig = plt.figure()
    ax = Axes3D(fig)
    xx = [x, x, x+dx, x+dx, x]
    yy = [y, y+dy, y+dy, y, y]
    kwargs = {'alpha': 1, 'color': color}
    ax.plot3D(xx, yy, [z]*5, **kwargs)
    ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
    ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)
    plt.title('Cube')
    plt.show()


if __name__ == "__main__":
    plot_linear_cube(0, 0, 0, 100, 120, 130)
    plot_opaque_cube()
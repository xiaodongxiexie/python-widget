# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

# %matplotlib inline

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']


def plot_opaque_cube(x=10, y=20, z=30, dx=40, dy=50, dz=60):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')


    xx = np.linspace(x, x+dx, 2)
    yy = np.linspace(y, y+dy, 2)
    zz = np.linspace(z, z+dz, 2)

    xx, yy = np.meshgrid(xx, yy)

    ax.plot_surface(xx, yy, z)
    ax.plot_surface(xx, yy, z+dz)

    yy, zz = np.meshgrid(yy, zz)
    ax.plot_surface(x, yy, zz)
    ax.plot_surface(x+dx, yy, zz)

    xx, zz = np.meshgrid(xx, zz)
    ax.plot_surface(xx, y, zz)
    ax.plot_surface(xx, y+dy, zz)
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
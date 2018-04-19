# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide

from matplotlib import pyplot as plt
from matplotlib.patches import Arrow

import math

"""
给绘图增加任意角度箭头配置
"""

def text(x, y, label, rot, f=None, **kwargs):
    """
    :param x: x location
    :param y: y location
    :param label: the text label
    :param rot: rotation
    :param f: matplotlib figure object

    """
    inch = (f.axes.get_xlim()[-1] - f.axes.get_xlim()[0])/5 if f is not None else 1
    width = (f.axes.get_xlim()[-1] - f.axes.get_xlim()[0])/ 25 if f is not None else 1
    rot = rot/180*math.pi
    arrow = Arrow(x, y, inch*math.cos(rot), inch*math.sin(rot), width=width, color='red')
    if f is None:
        plt.text(x, y, label, **kwargs)
        plt.gca().add_patch(arrow)
        plt.gca().axis('equal');
    else:
        f.axes.text(x, y, label, **kwargs)
        f.axes.add_patch(arrow);
    plt.show()


if __name__ == "__main__":
    text(0, 1, 'test', 22)
    f, = plt.plot(range(50, 100))
    text(0, 55, 'just for test', 25, f)
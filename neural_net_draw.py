# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-03-22 14:05:27
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-03-22 14:34:49

import random
import graphviz as gz


def neural_graph(inp=3, hide=10, outp=3, inp_label='input', hide_label='hide', outp_label='output', dropout=True, style='h', size='2, 1'):
    """
    绘制简易神经网络图（有向图）
    :param inp: 输入神经元个数
    :param hide: 隐藏层神经元个数
    :param outp: 输出神经元个数
    :param inp_label: 输入名称显示
    :param hide_label: 隐藏层名称显示
    :param outp_label: 输出名称显示
    :param dropout: 是否全连接
    :param style: 水平或垂直显示， 可选项为 'h', 'v'
    :param size: 图像显示大小
    :return: 有向图
    """

    dot = gz.Digraph(name='neural network')
    dot.attr(size=size)
    if style == 'v':
        dot.attr(rankdir='LR')

    def draw(enter, exit, label1, label2):
        for i in range(enter):
            for j in range(exit):
                if random.randint(0, max(enter, exit)):
                    dot.edge('%s%s' % (label1, i), '%s%s' % (label2, j))
    draw(inp, hide, inp_label, hide_label)
    draw(hide, outp, hide_label, outp_label)
    # return dot
    return dot.view()


if __name__ == '__main__':
    neural_graph(style='v', size=('0.1,1'))

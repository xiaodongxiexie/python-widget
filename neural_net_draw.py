# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-03-22 14:05:27
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-03-22 14:07:06

import graphviz as gz

def neural_graph(inp=3, hide=10, outp=3, inp_label='input', hide_label='hide', outp_label='output'):

    dot = gz.Digraph(name='neural network')

    def draw(enter, exit, label1, label2):
        for i in range(enter):
            for j in range(exit):
                dot.edge('%s%s'%(label1, i), '%s%s'%(label2,j))
    draw(inp, hide, inp_label, hide_label)
    draw(hide, outp, hide_label, outp_label)
    return dot.view()


if __name__ == '__main__':
	neural_graph()
# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-10-27 17:17:14
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-10-27 17:19:19

#计算距离
def calc_distance(seq1, seq2):
    return sum(map(lambda x, y: ((x-y)**2)**0.5, seq1, seq2))

#计算相似度
def calc_similarity(seq1, seq2):
    return 1/(1+sum(map(lambda x, y: ((x-y)**2)**0.5, seq1, seq2)))

if __name__ == '__main__':
    x = range(5)
    y = range(5, 10)
    print (calc_similarity(x, y))

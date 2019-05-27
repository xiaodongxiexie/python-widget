# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-10-27 18:20:05
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-10-27 18:22:32

#计算皮尔逊相关系数

#计算方式为：
# x 和 y 的协方差 除以 （x 的标准差 * y的标准差）
#协方差计算方式为：
# x - x的均值 与 y - y的均值的内积再取均值
def pearsonr(seq1, seq2):
    import numpy as np
    arr1 = np.array(seq1)
    arr2 = np.array(seq2)
    fenzi = ((arr1-arr1.mean()) * (arr2-arr2.mean())).mean()
    fenmu = arr1.std() * arr2.std()
    return round(fenzi / fenmu, 2) if fenmu != 0 else 0


if __name__ == '__main__':
	x = range(5)
	y = range(5, 10)
	print (pearsonr(x, y))
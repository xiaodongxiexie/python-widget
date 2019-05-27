#coding: utf-8

'''
程序运行时如果需要存储过多数据容易出现崩溃，
可以通过设置断点进行达到一定量后即保存。
'''


import numpy as np
from pandas import Series, DataFrame

ser = Series()
flag = 0
n = 0

dataTrue = DataFrame(np.random.randn(10000000,4))

for i in dataTrue.values:
    if len(ser) > 1000 and flag == 0:
        ser.to_csv('%s.csv' % n)
        n += 1
        ser = Series()
        flag = 1
    else:
        ser = ser.append(Series(i[1]))
        if len(ser) > 1000:
            flag = 0

#coding: utf-8

#该脚本用于对差分后的数据进行还原

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

class handle_diff:
    
    '''
    提供差分和还原的类，用于时间序列的平稳性处理的中间步骤处理
    args:
        ser - 可迭代类型，（若为单数字差分会失败）
        diff - 差分
    function:
        produceDiff - 产生指定阶数差分
        restoreDiff - 将原差分序列还原
    '''
    
    def __init__(self, ser, diff):
        try:
            ser = Series(ser)
        except:
            raise 
        self.ser = ser
        self.diff = diff
        
    def produceDiff(self):
        return self.ser.diff(self.diff)

    def restoreDiff(self):
        diff = self.diff
        ser2 = self.produceDiff()
        before = self.ser.iloc[:diff]
        ser_ = Series()
        for i in range(diff):
            after = self.ser.iloc[i] + ser2[i::diff].cumsum()     
            ser_ = ser_.append(after).replace(np.nan, self.ser.iloc[i])
        ser_ = ser_.sort_index()
        return ser_
    
 #or
 diff = 1
 ser = ser.shift(diff) + ser.diff(diff)
    

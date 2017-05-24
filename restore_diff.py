#coding: utf-8

#该脚本用于对差分后的数据进行还原

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#差分
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


def produceDiff(ser, diff=1):
    return ser.diff(diff)

ser = Series(range(10))
ser2 = produceDiff(ser, diff=2)


#差分后还原
def restoreDiff(ser2, diff=1):
    before = ser.iloc[:diff]
    ser_ = Series()
    for i in range(diff):
        after = ser.iloc[i] + ser2[i::diff].cumsum()     
        ser_ = ser_.append(after).replace(np.nan, ser.iloc[i])
    ser_ = ser_.sort_index()
    return ser_
    
 #or
 diff = 1
 ser = ser.shift(diff) + ser.diff(diff)
    

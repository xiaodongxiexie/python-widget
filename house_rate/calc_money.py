# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-10-12 00:02:26
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-10-12 00:04:07


#计算月利息，月利率为9.5%
def output(year=6,ratio=0.095):
    month = year * 12
    sum_ = 0
    sum2_ = 0
    for i in range(month):
        sum_ += (2000-i*15)*(1+ratio/12)**(month-i)
    for i in range(month):
        sum2_ += 2000 - i * 15
    return sum_ - sum2_


#计算日利息， 月利率默认为9.5%
 def output2(year=6,ratio=0.095):
    month = year * 12
    sum_ = 0
    sum2_ = 0
    for i in range(month):
        for ii in range(30):
            sum_ += (2000-i*15)*(1+ratio/12/30)**(month*30-i*30-ii)
            break
    for i in range(month):
        sum2_ += 2000 - i * 15
    return sum_ - sum2_
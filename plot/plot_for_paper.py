# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-03-20 21:49:28
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-03-21 11:06:29
import numpy as np
import pandas as pd
import scipy as sp
from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings('ignore')

#%matplotlib inline
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def example():
    f = sp.polyfit([0,1,2],[-5,-4,3],3)
    p = sp.poly1d(f)

    x = range(5,100)
    plt.figure(figsize=(14,6))
    plt.plot(x,p(x)+50000,lw=2,ls='--',color='green')
    plt.plot(x,-p(x)-50000,lw=2,ls='--',color='red')
    plt.xticks([])
    plt.yticks([])
    plt.gca().invert_xaxis()
    plt.axhline(0,ls='-',alpha=.2)
    plt.title(u'均值回归概念',fontsize=15)
    plt.ylabel(u'市场收益',fontsize=15)
    plt.xlabel(u'时间',fontsize=15)
    plt.text(70,400000,u'高收益具有\n向下回归趋势',color='green',fontsize=14)
    plt.text(70,-500000,u'低收益具有\n向上回归趋势',color='red',fontsize=14)
    plt.show()
example()
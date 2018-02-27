# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-02-27 17:37:48
# @Last Modified by:   xiaodong
# @Last Modified time: 2018-02-27 17:42:13
import numpy as np

"""
utils:
    用于截取连续的测试集及剩余作为训练集
"""

def trunc(arr, start, end):
    sample = arr[start:end]
    remainder = np.delete(arr, np.s_[start:end], axis=0)
    return sample, remainder

def trunc2(arr, start, end):
    rows = arr.shape[0]
    sample = arr.take(range(start, end), axis=0)
    remaind = arr.take(list(set(range(rows)) - set(range(start, end))), axis=0)
    return sample, remaind

def trunc3(arr, start, end):
    head, middle, tail = np.split(arr, (start, end))
    head_tail = np.r_[head, tail]
    return middle, head_tail

if __name__ == "__main__":
    arr = np.arange(24).reshape(6, 4)
    print(trunc(arr, 2, 5))
    print(trunc2(arr, 2, 5))
    print(trunc3(arr, 2, 5))
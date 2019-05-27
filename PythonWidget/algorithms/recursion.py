# -*- coding: utf-8 -*-
# @Author: liangxiaodong
# @Date:   2017-12-08 15:57:16
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
def sum(seq):
    if seq == []:
        return 0
    return seq[0] + sum(seq[1:])

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

def max_(seq):
    if len(seq) == 2:
        return seq[0] if seq[0] > seq[1] else seq[1]
    sum_max = max_(seq[1:])
    return seq[0] if seq[0] > sum_max else sum_max

def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    pivot = seq[0]
    left, right = [], []
    for ele in seq[1:]:
        if ele < pivot:
            left.append(ele)
        else:
            right.append(ele)
    return quick_sort(left) + [pivot] + quick_sort(right)

def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


import os, glob
from typing import Generator

def penetrate(root: os.path) -> Generator:
    for path in glob.glob(os.path.join(root, '*')):
        if os.path.isdir(path):
            yield path
            yield from penetrate(path)
        else:
            yield path

if __name__ == '__main__':
    seq = [1, 3, 5, 3, 4, 6]
    print (sum(seq))
    print (factorial(3))
    print (max_(seq))
    print (quick_sort(seq))
    print(list(penetrate('.')))
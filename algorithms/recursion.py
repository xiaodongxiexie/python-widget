# -*- coding: utf-8 -*-
# @Author: liangxiaodong
# @Date:   2017-12-08 15:57:16
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2017-12-08 16:29:59
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

if __name__ == '__main__':
	seq = [1, 3, 5, 3, 4, 6]
	print (sum(seq))
	print (factorial(3))
	print (max_(seq))
	print (quick_sort(seq))
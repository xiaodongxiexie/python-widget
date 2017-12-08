# -*- coding: utf-8 -*-
# @Author: liangxiaodong
# @Date:   2017-12-08 15:57:16
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2017-12-08 15:59:35
def sum(seq):
	if seq == []:
		return 0
	return seq[0] + sum(seq[1:])

def factorial(x):
	if x == 1:
		return 1
	return x * factorial(x-1)


if __name__ == '__main__':
	seq = [1, 3, 5, 3, 4, 6]
	print (sum(seq))
	print (factorial(3))
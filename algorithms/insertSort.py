# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-12-09 10:04:09
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2017-12-09 10:06:06
def insertSort(seq):
	for i in range(1, len(seq)):
		key = seq[i]
		j = i - 1
		while j >= 0 and seq[j] > key:
			seq[j+1] = seq[j]
			j -= 1
		seq[j+1] = key
	return seq


if __name__ == '__main__':
	import random
	seq = [random.randint(0, 10) for _ in range(20)]
	print (seq)
	print (insertSort(seq))
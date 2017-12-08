# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-12-08 15:35:51
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-12-08 15:40:04
def findSmallest(seq):
	smallest = seq[0]
	smallest_index = 0
	for i in range(1, len(seq)):
		if seq[i] < smallest:
			smallest = seq[i]
			smallest_index = i
	return smallest_index


def selectSort(seq):
	new_seq = []
	for i in range(len(seq)):
		smallest = findSmallest(seq)
		new_seq.append(seq.pop(smallest))
	return new_seq

if __name__ == '__main__':
	seq = [1, 1, 6, 4, 3, 6, 9, 10, 10, 6, 6, 4, 7]
	seq2 = []
	print (selectSort(seq))
	print (selectSort(seq2))
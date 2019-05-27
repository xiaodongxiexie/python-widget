# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-12-08 15:35:51
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2017-12-09 10:30:04

#method 1:
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

#method 2:
def select_sort(seq):
	le = len(seq)
	for i in range(le-1):
		minIndex = i
		for j in range(i, le):
			if seq[minIndex] > seq[j]:
				minIndex = j
		if i != minIndex:
			seq[i], seq[minIndex] = seq[minIndex], seq[i]
	return seq

if __name__ == '__main__':

	seq = [1, 1, 6, 4, 3, 6, 9, 10, 10, 6, 6, 4, 7]
	seq2 = []
	print (selectSort(seq))
	print (selectSort(seq2))

	seq = [1, 1, 6, 4, 3, 6, 9, 10, 10, 6, 6, 4, 7]
	print (select_sort(seq))

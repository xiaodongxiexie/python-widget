#coding: utf-8


def bubble_sort(seq):
    length = len(seq)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq
    
    

#coding: utf-8

#排序后就地改变
def gnome_sort(seq):
    if len(seq) <= 1:
        return seq
    i = 1
    while i < len(seq):
        if seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1
            if i == 0:
                i = 1
               

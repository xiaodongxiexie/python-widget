#coding: utf-8


def binary_search(lists, value):
    
    length = len(lists)
    index = length // 2
    
    while value != lists[index]:
        temp = index
        if value < lists[index]:
            index /= 2
        else:
            index += (length - index) // 2
        if temp == index:
            break
    if value != lists[index]:
        return 
    else:
        return index

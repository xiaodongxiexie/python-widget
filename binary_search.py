#coding: utf-8


#wrong 


############################################
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
############################################  



#right
def binary_search(lists, value):
    low = 0
    high = len(lists) - 1
    
    while high >= low:
        mid = (high - low) // 2
        if lists[mid] > value:
            high -= 1
        elif lists[mid] < value:
            low += 1
        else:
            return mid

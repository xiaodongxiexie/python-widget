#encoding: utf-8

#quick sort


def quickSort(lists, left, right):
    
    if left >= right:
        return lists
    
    key = lists[left]
    low = left
    high = right
    
    while left < right:
    
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
        
    lists[right] = lists[left]
    
    quickSort(lists, low, left-1)
    quickSort(lists, left+1, high)
    
    return lists

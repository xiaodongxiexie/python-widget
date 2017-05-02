#encoding: utf-8

#quick sort

#method 1
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


#method 2

def quickSort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.
    :param seq: A list of integers
    :rtype: A list of sorted integers
    """
    
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
    return sort(left) + [pivot] + sort(right)

def shellsort(values):
    values = values.copy()
    if len(values) <= 1: return values
    mid = len(values) // 2
    while mid > 0:
        for i in range(mid, len(values)):
            temp = values[i]
            j = i
            while j >= mid and values[j - mid] > temp:
                values[j] = values[j - mid]
                j -= mid
            values[j] = temp
        mid //= 2
    return values
    

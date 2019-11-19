# 维护最小堆
# 算法复杂度 n * lg(k)
def topk(seq, k=1):
    dq = seq[:k]
    rest = seq[k:]
    dq.sort(reverse=True)
    for ele in rest:
        if ele > dq[-1]:
            dq[-1] = ele
            dq.sort(reverse=True)
    return dq
    

# 冒泡查找
# 算法复杂度 n * k
def topk2(seq, k=1):
    dq = []
    locs = set()
    while len(dq) < k:
        pivot = seq[0]
        loc = 0
        for i, ele in enumerate(seq):
            if ele > pivot and i not in locs:
                pivot = ele
                loc = i 
        locs.add(loc)
        dq.append(pivot)
    return dq


def python_builtin_topk(seq, k=1):
    import heapq
    return heapq.nlargest(k, seq)


if __name__ == "__main__":
    import random
    seq = [random.randint(0, 100) for _ in range(20)]
    print(topk(seq, 5))
    print(topk(seq, 10))
    
    print(topk2(seq, 5))
    print(topk2(seq, 10))

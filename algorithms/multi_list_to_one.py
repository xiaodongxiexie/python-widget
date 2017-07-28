#coding: utf-8

'''
example:
    将多重镶嵌列表转换为单个列表：
    test = [[1,2,3], [3], [4,5],[23,1],[1,2,3,4],1]
    转换为：
    [1,2,3,3,4,5,23,1,1,2,3,4,1]
    
    test
    Out[1]: [[1, 2, 3], [2, 3, 4, 5, 6], [2], 1]

    to_transform(test)
    Out[2]: [1, 2, 3, 2, 3, 4, 5, 6, 2, 1]
'''
def to_transform(seq):
    return list(map(int, str(seq).replace('[', '').replace(']', '').split(',')))

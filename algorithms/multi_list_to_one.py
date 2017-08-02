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

#method 1:
#attention: 若嵌套列表中存在嵌套空列表，则该方法失效
def to_transform(seq):
    return list(map(int, str(seq).replace('[', '').replace(']', '').split(',')))


#method 2:
#source code: python 2.7 compiler.ast.flatten
def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
       #if isinstance(t, (tuple, list)):
            for elt2 in flatten(elt):
                l.append(elt2)
        else:
            l.append(elt)
    return l

#method2 变形：
def flat2(seq):
    L = []
    for ele in seq:
        if isinstance(ele, (list, tuple)):
            L.extend(flat2(ele))
        else:
            L.append(ele)
    return L

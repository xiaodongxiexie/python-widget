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

#method 3: 这个没看懂。。。不过确实能实现
flat=lambda L: sum(map(flat,L),[]) if isinstance(L,list) else [L]


#python 3
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
            
'''
#防止字符串被继续展开
>>> items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
>>> for x in flatten(items):
...     print(x)
...
Dave
Paula
Thomas
Lewis
'''

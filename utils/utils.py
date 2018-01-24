import time
from functools import wraps
from collections import Iterable

from compat import PY2, PY3


def total_time(func):
    '''
    统计程序耗时
    :param func:
    :return:
    '''
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.process_time() if PY3 else time.time()
        result = func(*args, **kwargs)
        end = time.process_time() if PY3 else time.time()
        print('%s 耗时：%s' % (func.__name__, end - start))
        return result
    return wrapped


def flatten(seq, ignore_type=(str, bytes)):
    '''
    将嵌套列表展开
    :param seq:
    :param ignore_type:
    :return:
    '''
    for ele in seq:
        if isinstance(ele, Iterable) and not isinstance(ele, ignore_type):
            yield from flatten(ele)
        else:
            yield ele


def flatten2(seq, ignore_type=(str, bytes)):
    '''

    :param seq:
    :param ignore_type:
    :return:
    '''
    item = []
    for ele in seq:
        if isinstance(ele, Iterable) and not isinstance(ele, ignore_type):
            item.extend(flatten2(ele))
        else:
            item.append(ele)
    return item

flatten3 = lambda L: sum(map(flatten3,L),[]) if isinstance(L,list) else [L]


def compress_nearest(seq, k=2, fill=0, whole=False):
    '''
    邻近压缩
    :param seq:
    :param k:
    :param fill:
    :param whole:
    :return:
    '''
    if PY2:
        from itertools import izip_longest
        if whole:
            return list(izip_longest(*[iter(seq)] * k, fillvalue=fill))
        return zip(*[iter(seq)] * k)
    elif PY3:
        from itertools import zip_longest
        if whole:
            return list(zip_longest(*[iter(seq)] * k, fillvalue=fill))
        return list(zip(*[iter(seq)] * k))


class S:
    '''
    将字典取值转为属性取值（不支持嵌套字典）
    '''
    def __init__(self, d):
        self.__dict__ = d


if __name__ == '__main__':
    f = lambda x: pow(x, 2) - abs(x)
    f2 = total_time(f)
    print(f2(10))

    seq = [1, [], [2, 3, [[], 2, [], 4, [4, []]]], ['abc', '1']]
    print(list(flatten(seq)))
    print(flatten2(seq))
    print(flatten3(seq))

    print(compress_nearest(range(10), 3, whole=True, fill=1000))

    d = {'a': 10, 'b': 20}
    sd = S(d)
    print(sd.a)


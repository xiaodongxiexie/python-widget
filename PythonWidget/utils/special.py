# -*- coding: utf-8 -*-
# @Author: liangxiaodong
# @Date:   2018-03-27 11:33:24
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-03-27 11:42:33
"""
一个 x != +x
的例子。
"""

if __name__ == "__main__":
    from collections import Counter

    d = {'a': 1, 'b': 2, 'c': 10, 'd': -2}
    cd = Counter(d)
    print(cd == +cd)
    print(cd)
    print(+cd)
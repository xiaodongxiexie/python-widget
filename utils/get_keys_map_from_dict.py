# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-03-27 11:28:24
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-03-27 11:30:14
from operator import itemgetter

if __name__ == "__main__":
    d = dict(zip(list('abcd'), range(4)))
    print(d)

    print(itemgetter(*list('abcd'))(d))
    print(itemgetter('a','b','c')(d))
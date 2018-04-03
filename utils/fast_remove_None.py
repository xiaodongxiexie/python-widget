# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide


if __name__ == "__main__":
    test = [1,2,3, None, 4, None, None, 5, 6, None, None]
    test2 = filter(None, test)
    print(list(test2))
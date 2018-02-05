# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-02-05 16:48:16
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-02-05 16:57:02
"""
define some constant that can't be changed when it born
"""

class Const:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise ConstError("constant %s can't be changed." % name)
        if not name.isupper():
            raise ConstCaseError("constant \"%s\" is not all upper." % name)
        self.__dict__[name] = value


class ConstError(TypeError):pass


class ConstCaseError(ConstError):pass


if __name__ == "__main__":
    import traceback

    c = Const()
    c.TOTAL = 100
    try:
        c.all = 101
    except:
        print(traceback.format_exc())

    try:
        c.NOt = 'test'
    except:
        print(traceback.format_exc())
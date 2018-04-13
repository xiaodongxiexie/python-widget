# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import re

class Pdir:
    def __init__(self, module):
        self.module = module

    def find_attr(self, key):
        comp = re.compile('^{}.*'.format(key))
        rets = []
        for ele in dir(self.module):
            rets.extend(comp.findall(ele))
        return rets

    def startswith(self, key):
        return list(filter(lambda x: x.startswith(key), dir(self.module)))

    def __getattr__(self, key):
        return self.startswith(key)


class ExtendPdir(Pdir):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # super(ExtendPdir, self).__init__(*args, **kwargs)

    def find_upper_attr(self):
        return self.find_attr('[A-Z]')

    def find_lower_attr(self):
        return self.find_attr('[a-z]')

    def __getattr__(self, key):
        if key == 'UPPER_':
            return self.find_upper_attr()
        elif key == 'LOWER_':
            return self.find_lower_attr()
        else:
            return self.startswith(key)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    pdir = ExtendPdir(plt)
    print(pdir.find_upper_attr())
    print(pdir.startswith('a'))
    print(pdir.b)
    print(pdir.ddd)
    print(pdir.LOWER_)
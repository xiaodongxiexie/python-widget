# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
def find_upper_attr(module):
    import re
    comp = re.compile('^[A-Z].*')
    rets = []
    for ele in dir(module):
        rets.extend(comp.findall(ele))
    return rets

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    print(find_upper_attr(plt))
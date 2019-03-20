# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide

import os
from glob import glob

d = {}

def stat(path):
    """
    统计给定目录下所有文件及对应的文件名。
    """
    for ele in glob(os.path.join(path, "*")):
        if os.path.isdir(ele):
            stat(ele)
        else:
            d[os.path.dirname(path)] = len(os.listdir(os.path.dirname(path)))
    return d


if __name__ == "__main__":
    result = stat("../")
    print(result)


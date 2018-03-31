# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import re


if __name__ == "__main__":

    pat = re.compile('[\u4e00-\u9fa5]+')
    pat2 = re.compile('[\u4e00-\u9fa5；，？。‘“”’]+')

    str_test = 'zhongguo China 中国， 世界， World, 长城'

    print(pat.findall(str_test))
    print(pat2.findall(str_test))


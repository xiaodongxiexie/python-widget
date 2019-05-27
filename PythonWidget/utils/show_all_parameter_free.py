# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
def show_all_parameter_free(function):
    for attr in dir(function):
        try:
            print("{} : {}".format(attr, getattr(function, attr)))
        except:
            try:
                print("{} : {}".format(attr, getattr(function, attr)()))
            except:pass
# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-10-25 10:11:06
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-10-25 10:11:29
import copy


# 只扩大dx
def expand_dx(L, addx=300, threshold=100):
    '''
    L: 为转换前存放信息字典的列表
    '''
    L2 = []
    LL = copy.deepcopy(L)

    for value in LL:
        if value['ot'] == '区域':
            value2 = copy.deepcopy(value)

    for value in LL:
        if value['ot'] == '区域':
            value['dx'] = value['dx'] + addx  # 扩大的 300mm

        else:
            if min(abs(value['x'] + value['dx'] - value2['x'] - value2['dx']), abs(value['x'] - value2['x'] - value2['dx'])) < threshold:
                value['x'] = value['x'] + addx
        L2.append(value)

    return L2

# 只扩大dy


def expand_dy(L, addx=300, threshold=100):
    L3 = []
    LL = copy.deepcopy(L)

    for value in LL:
        if value['ot'] == '区域':
            value2 = copy.deepcopy(value)

    for value in LL:
        if value['ot'] == '区域':
            value['dy'] = value['dy'] + addx
        else:
            if min(abs(value['y'] + value['dy'] - value2['y'] - value2['dy']), abs(value['y'] - value2['y'] - value2['dy'])) < threshold:
                value['y'] = value['y'] + addx
        L3.append(value)
    return L3


# 同时扩大dx， dy
def expand_dx_dy(L, addx=300, addy=300, threshold=100):
    L4 = []
    LL = copy.deepcopy(L)

    for value in LL:
        if value['ot'] == '区域':
            value2 = copy.deepcopy(value)

    for value in LL:
        if value['ot'] == '区域':
            value['dx'] = value['dx'] + addx
            value['dy'] = value['dy'] + addy
        else:
            if min(abs(value['x'] - value2['dx'] - value2['x']), abs(value['x'] + value['dx'] - value2['x'] - value2['dx'])) < threshold:
                value['x'] = value['x'] + addx
            if min(abs(value['y'] - value2['dy'] - value2['y']), abs(value['y'] + value['dy'] - value2['y'] - value2['dy'])) < threshold:
                value['y'] = value['y'] + addy
        L4.append(value)
    return L4

# 只缩小dx


def reduce_dx(L, minusx=300):
    L5 = []
    LL = copy.deepcopy(L)

    for value in LL:
        if value['ot'] == '区域':
            value2 = copy.deepcopy(value)

    for value in LL:
        if value['ot'] == '区域':
            value['dx'] = value['dx'] - minusx
        else:
            if min(abs(value['x'] - value2['x'] - value2['dx']), abs(value['x'] + value['dx'] - value2['x'] - value2['dx'])) <= minusx:
                value['x'] = value['x'] - minusx

        L5.append(value)
    return L5


# 只缩小dy
def reduce_dy(L, minusy=300):
    L6 = []
    LL = copy.deepcopy(L)

    for value in LL:
        if value['ot'] == '区域':
            value2 = copy.deepcopy(value)

    for value in LL:
        if value['ot'] == '区域':
            value['dy'] = value['dy'] - minusy
        else:
            if min(abs(value['y'] - value2['y'] - value2['dy']), abs(value['y'] + value['dy'] - value2['y'] - value2['dy'])) <= minusy:
                value['y'] = value['y'] - minusy
        L6.append(value)
    return L6


# 同时缩小dx， dy
def reduce_dx_dy(L, minusx=300, minusy=300):
    L7 = []
    LL = copy.deepcopy(L)

    for value in LL:
        if value['ot'] == '区域':
            value2 = copy.deepcopy(value)

    for value in LL:
        if value['ot'] == '区域':
            value['dx'] = value['dx'] - minusx
            value['dy'] = value['dy'] - minusy
        else:
            if min(abs(value['x'] - value2['x'] - value2['dy']), abs(value['x'] + value['dx'] - value2['x'] - value2['dx'])) < minusx:
                value['x'] = value['x'] - minusx
            if min(abs(value['y'] - value2['y'] - value2['dy']), abs(value['y'] + value['dy'] - value2['y'] - value2['dy'])) < minusy:
                value['y'] = value['y'] - minusy

        L7.append(value)
    return L7


# 扩大dx，同时缩小dy
def expand_dx_reduce_dy(L, addx=300, minusy=300, threshold1=100):
    L8 = []
    LL = copy.deepcopy(L)

    for value in LL:
        if value['ot'] == '区域':
            value2 = copy.deepcopy(value)

    for value in LL:
        if value['ot'] == '区域':
            value['dx'] = value['dx'] + addx
            value['dy'] = value['dy'] - minusy
        else:
            if min(abs(value['x'] - value2['x'] - value2['dx']), abs(value['x'] + value['dx'] - value2['x'] - value2['dx'])) < threshold1:
                value['x'] = value['x'] + addx
            if min(abs(value['y'] - value2['y'] - value2['dy']), abs(value['y'] + value['dy'] - value2['y'] - value2['dy'])) < minusy:
                value['y'] = value['y'] - minusy
        L8.append(value)
    return L8


# 缩小dx， 同时扩大dy
def reduce_dx_expand_dy(L, minusx=300, addy=300, threshold2=100):
    L9 = []
    LL = copy.deepcopy(L)

    for value in LL:
        if value['ot'] == '区域':
            value2 = copy.deepcopy(value)

    for value in LL:
        if value['ot'] == '区域':
            value['dx'] = value['dx'] - minusx
            value['dy'] = value['dy'] + addy
        else:
            if min(abs(value['x'] - value2['x'] - value2['dx']), abs(value['x'] + value['dx'] - value2['x'] - value2['dx'])) < minusx:
                value['x'] = value['x'] - minusx
            if min(abs(value['y'] - value2['y'] - value2['dy']), abs(value['y'] + value['dy'] - value2['y'] - value2['dy'])) < threshold2:
                value['y'] = value['y'] + addy
        L9.append(value)
    return L9

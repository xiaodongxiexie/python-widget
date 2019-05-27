# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-10-23 18:25:51
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-10-27 12:07:29
import copy, os, json

from itertools import combinations

import pandas as pd

# 重叠检测并解决冲突


def check(d1, d2, debug=False):
    # 优先移动小的
    x, y, dx, dy = d1['x'], d1['y'], d1['dx'], d1['dy']  # 小
    x2, y2, dx2, dy2 = d2['x'], d2['y'], d2['dx'], d2['dy']  # 大
    d11, d22 = copy.deepcopy(d1), copy.deepcopy(d2)
    if x <= x2 and x + dx >= x2:
        # 左上
        if y2 + dy2 > y >= y2 and y + dy >= y2 + dy2:
            if debug:
                print('左上')
            xx = x2 - dx
            yy = x2 + dy2 - dy

        # 左中
        elif y >= y2 and y + dy < y2 + dy2:
            if debug:
                print('左中')
            xx = x2 - dx
            yy = y
        # 左下
        elif y <= y2 and y + dy >= y:
            if debug:
                print('左下')
            xx = x2 - dx
            yy = y2

    elif x > x2 and x + dx < x2 + dx2:
        # 中上
        if y2 + dy2 > y >= y2 and y + dy >= y2 + dy2:
            if debug:
                print('中上')
            xx = x
            yy = y2 + dy2
        # 中下
        elif y <= y2 and y2 < y + dy < y2 + dy2:
            if debug:
                print('中下')
            xx = x
            yy = y2 - dy
    elif x > x2 and x + dx > x2 + dx2:
        # 右上
        if y2 + dy2 > y >= y2 and y + dy >= y2 + dy2:
            if debug:
                print('右上')
            xx = x2 + dx2
            yy = y2 + dy2 - dy
        # 右中
        elif y >= y2 and y + dy < y2 + dy2:
            if debug:
                print('右中')
            xx = x2 + dx2
            yy = y
        # 右下
        elif y < y2 and y + dy >= y2:
            if debug:
                print('右下')
            xx = x2 + dx2
            yy = y2
    try:
        d11['x'] = xx
        d11['y'] = yy
    except:
        pass
    return d11, d22


def change(seq2):
    seq = seq2[:]
    comb = combinations(range(len(seq)), 2)
    while True:
        for x, y in comb:
            #print (x, y)
            d1 = seq[x]
            d2 = seq[y]
            if d1['dx'] * d1['dy'] > d2['dx'] * d2['dy']:
                d22, d11 = check(d2, d1)
                if d22 != d2:
                    seq[y] = d22
            else:
                d11, d22 = check(d1, d2)
                if d11 != d1:
                    seq[x] = d11
        else:
            break
    return seq


def all_change(seq2):
    seq = seq2[:]
    first = change(seq)
    second = change(first)
    num = 0
    while first != second and num < 5:
        first = change(second)
        second = change(first)
        num += 1
    return second


##################龙哥写的关于碰撞检测及解决冲突###################
def HitObjs(o1,o2,debug=False):
    cross_rect=[]
    L = o1["x"]
    R = L + o1["dx"]
    T = o1["y"]
    B = T + o1["dy"]
    _L = o2["x"]
    _R = _L + o2["dx"]
    _T = o2["y"]
    _B = _T + o2["dy"]
    if min(_R, R) > max(_L, L) and min(_B, B) > max(_T, T):
        if debug:
            print("hit")
        corss_rect=[min(_R, R) - max(_L, L),min(_B, B) - max(_T, T)]
        return True,corss_rect
    else:
        if debug:
            print("not hit")
        return False,cross_rect

def MoveObj(o1,o2,k=100,debug=False):
    hit,cross_rect = HitObjs(o1,o2)
    if not hit:
        if debug:
            print("无需修改")
        return
    L = o1["x"]
    R = L + o1["dx"]
    T = o1["y"]
    B = T + o1["dy"]
    _L = o2["x"]
    _R = _L + o2["dx"]
    _T = o2["y"]
    _B = _T + o2["dy"]
    if cross_rect[0]<cross_rect[1]:
        if L<_L:
            if R>_L:
                o2["x"]=R+k
                if debug:
                    print("修改o2[x]")
        else:
            if _R>L:
                o1["x"]=_R+k
                if debug:
                    print("修改o1[x]")
    else:
        if T<_T:
            if B>_T:
                o2["y"]=B+k
                if debug:
                    print("修改o2[y]")
        else:
            if _B>T:
                o1["y"]=_B+k
                if debug:
                    print("修改o1[y]")

def HitTestAndChange(D,change=False,space=100):
    k=0
    for i in range(len(D)-1):
        for j in range(i+1,len(D)):
            o1=D[i]
            o2=D[j]
            #print(o1,"\n",o2)
            hit,rect = HitObjs(o1,o2,debug=False)
            if hit:
                # print(rect)
                # print(o1)
                # print(o2)
                k+=1
                if change:
                    MoveObj(o1,o2,k=space)
#     print(k)
    return k

def FinallyOutput(L):
    import copy
    D2=copy.deepcopy(L)
    num = 0
    while True and num < 10:
        hc = HitTestAndChange(D2,True,space=10)
        num += 1
        if hc==0:
            break
    return D2
#################################################################################


# 对齐检测
def aline(which, rely):
    '''
    which:  被对齐物品
    rely：对齐参照物
    '''
    x, y, dx, dy = which['x'], which['y'], which['dx'], which['dy']
    x2, y2, dx2, dy2 = rely['x'], rely['y'], rely['dx'], rely['dy']
    which2 = copy.deepcopy(which)

    if dx2 > dy2:
        # 此时床头柜位于上下
        if abs(x2 - x) < abs(x2 + dx2 - x - dx):
            xx = x2
            yy = y
            # 位于左
        else:
            # 位于右
            xx = x2 + dx2 - dx
            yy = y
            #print ('here')
    elif dx2 < dy2:
        # 此时床头柜位于左右
        if abs(y + dy - y2 - dy2) < abs(y - y2):
            # 位于上
            xx = x
            yy = y2 + dy2 - dy

        else:
            # 位于下
            xx = x
            yy = y2
            #print ('here2')

    else:
        #dx2 == dy2
        # 此时床头柜可位于上下或左右
        pass

    which2['x'] = xx
    which2['y'] = yy
    return which2, rely


# 区域大小放缩
def expand_reduce(L, ddx, ddy):
    '''
    L: 原输出
    ddx: 输入区域dx
    ddy：输入区域dy
    '''
    L8 = []
    LL = copy.deepcopy(L)

    for value in L:
        if value['ot'] == '区域':
            dx, dy = copy.deepcopy(value['dx']), copy.deepcopy(value['dy'])
    #对区域进行放大缩小
    addx = ddx - dx
    addy = ddy - dy

    print ('Attention'.center(50, '&'))
    print (addx, addy)

    if addx > 0:
        threshold1 = 100  #设定增大时阈值为100mm范围内物品移动
    else:
        threshold1 = -addx

    if addy > 0:
        threshold2 = 100
    else:
        threshold2 = - addy
    for value in LL:
        if value['ot'] == '区域':
            value2 = copy.deepcopy(value)

    for value in LL:
        if value['ot'] == '区域':
            value['dx'] = value['dx'] + addx
            value['dy'] = value['dy'] + addy
        else:
            if min(abs(value['x'] - value2['x'] - value2['dx']), abs(value['x'] + value['dx'] - value2['x'] - value2['dx'])) < threshold1:
                value['x'] = value['x'] + addx
            if min(abs(value['y'] - value2['y'] - value2['dy']), abs(value['y'] + value['dy'] - value2['y'] - value2['dy'])) < threshold2:
                value['y'] = value['y'] + addy
        L8.append(value)
    return L8


def choose_file(i, area=7000000):
    d = {1: 'bedroom', 2: 'hall', 3:'dining', 4:'kitchen',
         5:'toilet', 6:'balcony', 7:'studyroom'}
    data = pd.read_csv('records/database_%s_features.csv'%d[i+1], encoding='gbk')

    if i == 0:
        import optimization
        if os.path.exists('area.json'):
            pass
        else:
            optimization.main()
        num = optimization.collect(area)
        indexs = json.load(open('area.json', 'r'))['area%s' % num]
        num2 = num+1 if num < 14 else num
        num3 = num - 1 if num > 0 else num
        indexs += json.load(open('area.json', 'r'))['area%s' % num2]
        indexs += json.load(open('area.json', 'r'))['area%s' % num3]
        data = data.iloc[indexs, :]
        return data, 'database_%s'%d[i+1]

    return data, 'database_%s'%d[i+1]
# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide


def gentle_show(seq, *, column=4):
    seq = list(map(str, seq))
    max_len = len(max(seq, key=len))

    for index, ele in enumerate(seq):
        if index % column == 0:
            print('-' * max_len * column + '-' * (column - 1))
            print(ele.center(max_len, ' '), end='|')
        else:
            if (index - column + 1) % column == 0:
                print(ele.center(max_len, ' '))
            else:
                print(ele.center(max_len, ' '), end='|')
    print('\n')

if __name__ == "__main__":
    gentle_show(dir([]), column=6)
    gentle_show(range(10))
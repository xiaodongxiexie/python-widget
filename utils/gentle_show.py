# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
try:
    from colorama import Fore, Style
except ImportError:
    class Temp:
        def __getattr__(self, x):
            return ''
    Fore = Style = Temp()


def gentle_show(seq, *, column=4):
    seq = list(map(str, seq))
    max_len = len(max(seq, key=len))

    for index, ele in enumerate(seq):
        if index % column == 0:
            print(Fore.RED, '-' * max_len * column + '-' * (column - 1), Style.RESET_ALL)
            print(ele.center(max_len, ' '), end='|')
        else:
            if (index - column + 1) % column == 0:
                print(ele.center(max_len, ' '))
            else:
                print(ele.center(max_len, ' '), end='|')
    print('\n')

if __name__ == "__main__":
    gentle_show(dir([]), column=3)
    gentle_show(range(10))
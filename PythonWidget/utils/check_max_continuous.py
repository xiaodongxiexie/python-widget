# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2019/11/22

"""
用来非重数组中最大连续序列
"""


def check_max_continuous(seq):
    from itertools import groupby
    msg = "the input seq not allow repeat number."
    assert len(seq) == len(set(seq)), msg

    seq = list(seq)
    seq.sort()

    if len(seq) == 1:
        return seq

    pre = seq[:-1]
    post = seq[1:]
    diff = list(map(lambda a, b: a - b, post, pre))
    ptr = 0
    index = 0
    max_groups_length = 0
    for k, vs in groupby(diff):
        vs = list(vs)
        index += len(vs)
        if k == 1:
            if len(vs) > max_groups_length:
                max_groups_length = len(vs)
                ptr = index - len(vs)
    return seq[ptr:ptr + max_groups_length + 1]


if __name__ == "__main__":
    seq = [1, 2, 3, 5, 6]
    seq2 = [1, 3, 5]
    seq3 = [1, 2, 4, 5, 6, 7, 9, 10, 11]
    print(check_max_continuous(seq))
    print(check_max_continuous(seq2))
    print(check_max_continuous(seq3))

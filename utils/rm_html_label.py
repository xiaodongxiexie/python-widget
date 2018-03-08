# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-03-08 18:16:24
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-03-08 18:25:50
def parse(chars):
    char = ''
    flag = 1
    for ele in chars:
        if ele == '<':
            flag = 0
        elif ele == '>':
            flag = 1
            continue
            # ele = ' '
        if flag == 1:
            char += ele
    return char


def parse2(chars):
    import re
    pat = re.compile('<[^>]+>', re.S)
    return pat.sub('', chars)


def parse3(chars):
    import re
    pat = re.compile('>(.*)?<')
    return ' '.join(pat.findall(chars))


def parse4(chars):
    import re
    pat = re.compile('(?<=\>).*?(?=\<)')
    return ' '.join(pat.findall(chars))


if __name__ == "__main__":

    chars = """
            <p>just for test</p>
            <font color="red">for test</font>
            <b>today is a good day</b>
            """
    print(parse(chars))
    print(parse2(chars))
    print(parse3(chars))
    print(parse4(chars))
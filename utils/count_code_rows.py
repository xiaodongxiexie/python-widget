# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-12-18 18:54:56
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-12-18 19:05:10

'''
简易统计Python代码行数
'''
def count_code_nums(file):
    with open(file,encoding='utf-8') as data:
        count, flag = 0, 0
        begin = ('"""', "'''")
        for line in data:
            line2 = line.strip()
            if line2.startswith('#'):continue
            elif line2.startswith(begin):
                if line2.endswith(begin) and len(line2) > 3:
                    flag = 0
                    continue
                elif flag == 0:
                    flag = 1
                else:
                    flag = 0
                    continue
            elif flag == 1 and line2.endswith(begin):
                flag = 0
                continue
            if flag == 0 and line2:
                count += 1
    return count


if __name__ == '__main__':
    print (count_code_nums(__file__))
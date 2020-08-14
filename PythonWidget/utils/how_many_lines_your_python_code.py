# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/8/13

"""
统计python有效代码行数。
    - 去除注释
    - 去除空行
    - 去除文档
"""

import os
import re
import glob


def codes(root="."):
    count = 0
    for file in glob.glob(os.path.join(root, "*")):
        if os.path.isdir(file):
            count += codes(file)
        else:
            if not file.endswith(".py"):
                continue
            count += how_many_rows(file)
    return count


def how_many_rows(file):
    with open(file, encoding="utf-8", errors="ignore") as file:
        lines = file.read()
        lines = re.sub("[u]?'''.*?'''", "", lines, flags=re.M | re.DOTALL)
        lines = re.sub('[u]?""".*?"""', "", lines, flags=re.M | re.DOTALL)
        lines = lines.split("\n")
        count = 0
        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                continue
            elif (line.startswith("'") or line.startswith("u'")) and line.endswith("'"):
                continue
            elif (line.startswith('"') or line.startswith('u"')) and line.endswith('"'):
                continue
            if not line:
                continue
            count += 1
        return count


if __name__ == "__main__":

    print(codes("."))


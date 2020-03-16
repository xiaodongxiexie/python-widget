# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/3/16


import os
import re
import glob
import argparse


ALLOWED = [".py", ".txt"]


def search(root, keyword, nums=None, count=[0]):
    for file in glob.glob(os.path.join(root, "*")):
        if os.path.isdir(file):
            search(file, keyword, nums=nums, count=count)
        elif os.path.isfile(file):
            if not file.endswith(tuple(ALLOWED)):
                continue
            if file == os.path.abspath(__file__):
                continue
            with open(file, encoding="utf-8") as f:
                lines = f.readlines()
                for i, line in enumerate(lines, 1):
                    v = re.findall(keyword, line, re.I)
                    if v:
                        count[0] += 1
                        print("="*50)
                        for _v in v:
                            print("----->  ", _v)
                        print(file, " ==> ", i)
                        print("\n")
                    if nums:
                        if count[0] >= nums:
                            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='search keyword by given dir')
    parser.add_argument(
        'keyword', metavar='str',  type=str,
        help='which keyword you want to search...')
    parser.add_argument(
        'root', metavar='str', type=str,
        help='which dir you want to start')
    parser.add_argument(
        '--nums', default=None, metavar='int', type=int,
        help='max find nums')
    args = parser.parse_args()

    search(args.root,
           args.keyword,
           nums=args.nums)

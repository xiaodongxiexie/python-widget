# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import os
import glob
import json
import datetime

from typing import Iterable

"""
监视指定目录下文件变更
"""

def penetrate(root: os.path) -> Iterable:
    for ele in glob.glob(os.path.join(root, '*')):
        if os.path.isdir(ele):
            yield from penetrate(os.path.abspath(ele))
        else:
            yield ele


def update(s: set, exists: bool=False, mode: str='w') -> None or dict :
    with open('file_records.json', encoding='utf-8', mode=mode) as file:
        if not exists:
            json.dump({'datetime': str(datetime.datetime.now()),
                       'files': list(s)}, file, ensure_ascii=False, indent=10)
        else:
            return json.load(file)


def main(s: set=set(), root: os.path='.')-> None:
    for path in penetrate(root):
        s.add(path)

    if not os.path.exists('file_records.json'):
        update(s)
    else:
        d = update(None, True, 'r')
        files = s - set(d['files'])
        files2 = set(d['files']) - s
        if files:
            print('增加文件: ', files)
        if files2:
            print('删除文件: ', files2)
        if files or files2:
            update(s)
            print('更新成功!')


if __name__ == "__main__":
    main()




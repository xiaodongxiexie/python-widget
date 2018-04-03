# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import os
import glob
import json
import datetime

def penetrate(root):
    for ele in glob.glob(os.path.join(root, '*')):
        if os.path.isdir(ele):
            yield from penetrate(os.path.abspath(ele))
        else:
            yield ele


def update(s, exists=False, mode='w'):
    with open('file_records.json', encoding='utf-8', mode=mode) as file:
        if not exists:
            json.dump({'datetime': str(datetime.datetime.now()),
                       'files': list(s)}, file, ensure_ascii=False, indent=10)
        else:
            return json.load(file)


def main(s=set(), root='.'):
    for path in penetrate(root):
        s.add(path)

    if not os.path.exists('file_records.json'):
        update(s)
    else:
        d = update(None, True, 'r')
        files = s - set(d['files'])
        print(files)
        update(s)


if __name__ == "__main__":
    main()




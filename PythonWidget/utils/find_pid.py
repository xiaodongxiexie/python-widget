# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import psutil
import os

"""
递归显示所有pid及对应name
"""
def ls_pidAndexe(pids, i=0):
    if not pids:
        return

    for pid in pids:
        if pid == 0:
            continue
        if psutil.pid_exists(pid):
            p = psutil.Process(pid)
            print('\t' * i, pid, p.name())
            children = p.children()
            seq = []
            for c in children:
                seq.append(c.pid)
            ls_pidAndexe(seq, i+1)

if __name__ == "__main__":
    pids = psutil.pids()
    ls_pidAndexe(pids)

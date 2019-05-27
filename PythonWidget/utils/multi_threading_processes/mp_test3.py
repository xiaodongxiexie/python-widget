# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-01-25 09:47:32
# @Last Modified by:   xiaodong
# @Last Modified time: 2018-01-25 09:51:06

from multiprocessing import Queue, Pool
import multiprocessing, time, random


def write(q):
    for value in list("ABCD"):
        print("Put %s to Queue!" % value)
        q.put(value)
        time.sleep(1)#random.random())


def read(q, lock):
    while True:
        lock.acquire()
        if not q.empty():
            value = q.get(True)
            print("Get %s from Queue" % value)
            time.sleep(1)#random.random())
        else:
            break
        lock.release()

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    q = manager.Queue()
    p = Pool()
    lock = manager.Lock()
    pw = p.apply_async(write, args=(q, ))
    pr = p.apply_async(read, args=(q, lock))
    # pw = p.apply(write, args=(q, ))
    # pr = p.apply(read, args=(q, lock))


    p.close()
    p.join()
    print()
    print('End')
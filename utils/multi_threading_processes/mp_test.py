# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-01-22 11:53:36
# @Last Modified by:   xiaodong
# @Last Modified time: 2018-01-23 11:17:57
import os
import json
import time
import queue
import random
import requests
import threading
import multiprocessing

q = queue.Queue()

path = r"C:\work\work\智能布局\服务器2\AutoLayout\go_on"
fullhouse = json.load(open(os.path.join(path, 'fullhouse.json'), encoding='utf-8'))
URL = "http://localhost:8026/AI/solutions/DR"

# -------------------------------------------------
def parse(full_house):
    """
    将全屋分为单个room逐个解析
    """
    seq = []
    addUserId = full_house['addUserId']
    dnaSolutionId = full_house['dnaSolutionId']
    solutionId = full_house['solutionId']

    for room in full_house['roomList']:
        init = {}
        init['addUserId'] = addUserId
        init['dnaSolutionId'] = dnaSolutionId
        init['solutionId'] = solutionId
        init['roomList'] = [room]
        seq.append(init)
    return seq


# -------------------------------------------------
def return_result(data):
    data = json.dumps(data)
    result = requests.post(URL, data=data)
    ret = result.json()
    q.put(ret)
    #print('status: ', ret)
    return ret


# -------------------------------------------------
class MyThread(threading.Thread):
    """
    获取多线程运行后返回结果
    """
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except:
            return None


# -------------------------------------------------
def timer(func):
    """
    统计耗时
    """
    def _wrapper(*args, **kwargs):
        start = time.clock()
        result = func(*args, **kwargs)
        end = time.clock()
        print(('%s'%func.__name__).center(60, '*'))
        print('Total time: ', end - start)
        print('\n\n')
        return result
    return _wrapper


# -------------------------------------------------
@timer
def pure(data, target):
    for member in data:
        target(member)


# -------------------------------------------------
@timer
def use_threads(data, target):
    """
    使用多线程测试
    """
    seq = []
    for member in data:
        t = MyThread(target, args=(member, ))
        seq.append(t)
        t.start()
    for t in seq:
        t.join()
        print(t.get_result())


# -------------------------------------------------
@timer
def use_multiprocessing(data, target):
    """
    使用多进程
    """
    for member in data:
        p = multiprocessing.Process(target=target, args=(member,))
        p.start()
    while not q.empty():
        print(q.get())


# -------------------------------------------------
@timer
def use_multi_pool(data, target, processes=5):
    """
    多进程带返回数据
    """
    p = multiprocessing.Pool(processes)
    rets = p.map(target, data)
    print(rets)


# -------------------------------------------------
if __name__ == "__main__":
    data = parse(fullhouse)
    random.shuffle(data)
    pure(data, return_result)
    # use_threads(data, return_result)
    # use_multi_pool(data, return_result, len(data))
    # use_multiprocessing(data, return_result)

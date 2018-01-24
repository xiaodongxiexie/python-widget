# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-01-22 14:41:37
# @Last Modified by:   xiaodong
# @Last Modified time: 2018-01-23 10:44:53
import time
import random
import threading
import multiprocessing


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
def per(sleep=3):
    time.sleep(sleep)
    return sleep


# -------------------------------------------------
def use_threading(target, args, count=3):
    start = time.clock()

    T = []
    rets = []
    for i in range(count):
        thread = MyThread(target, args=args)
        T.append(thread)
        thread.start()
    for t in T:
        t.join()
        rets.append(t.get_result())
    end = time.clock()
    print(rets)
    print('总耗时：', end - start)
    # return rets


# -------------------------------------------------
def use_multi_pool(target, args, processes):
    start = time.clock()
    p = multiprocessing.Pool(processes=processes)


    # 此处注意：
    # 多进程中的.map仅支持函数为单参数迭代
    result = p.map(target, args)

    print(result)
    end = time.clock()
    print('总耗时：', end - start)
    # return result


if __name__ == "__main__":

    start = time.clock()

    count = 2  # 循环次数
    sleep = 5  # sleep时间
    use_threading(per, (sleep,), count)
    # use_multi_pool(per, [sleep]*count, count)

    end = time.clock()
    print('Total time: ', end - start)

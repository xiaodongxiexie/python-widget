# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-12-04 13:28:45
# @Last Modified by:   xiaodong
# @Last Modified time: 2018-01-12 15:11:11
import time
import types
from contextlib import contextmanager

class Timer(object):
	def __init__(self, start=None):
		self.start = start if start is not None else time.time()
	def __enter__(self):
		return self
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.stop = time.time()
		self.cost = self.stop - self.start
		return exc_type is None

class TimerCost:
	def __init__(self, function):
		self.function = function

	def __call__(self, *args, **kwargs):
		start = time.time()
		result = self.function(*args, **kwargs)
		end = time.time()
		print ('Total time: %s s' % (end-start))
		return result
class Timeuse:
    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print("time use: ", self.end - self.start)


@contextmanager
def timeuse():
    try:
        start = time.perf_counter()
        yield
    finally:
        end = time.perf_counter()
        print("time use: ", end - start)


class Elapsed:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        end = time.perf_counter()
        logger.info("%s elapsed time: %d", self.func.__name__, end - start)
        return result

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@TimerCost
def p(a, b=10):
	time.sleep(2)
	return a ** b



"""A utility for timing."""

import time

import numpy as np


class Timer:

    def __init__(self, task_name="UntitledTask"):
        self.task_name = task_name
        self._duration_list = []
        self.now = None
        self.check_point = None
        self.is_timing = False
        self._count = 0

    def start(self):
        if not self.is_timing:
            self.check_point = time.time()
            self.is_timing = True

    def pause(self):
        if self.is_timing:
            self._duration_list.append(time.time() - self.check_point)
            self.is_timing = False
            self._count += 1

    def stop(self):
        self.pause()
        self.report()

    def report(self):
        print("[Timer] {} total: {:.4f} mean: {:.4f} count: {}".format(
            self.task_name, np.sum(self._duration_list),
            np.mean(self._duration_list), self._count))

    @property
    def duration(self):
        return np.sum(self._duration_list)

    @property
    def count(self):
        return self._count



if __name__ == '__main__':
	def test():
		time.sleep(10)
	with Timer() as timer:
		test()
	print (timer.cost)
	print (p(2))

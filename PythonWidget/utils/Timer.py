# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-12-04 13:28:45
# @Last Modified by:   xiaodong
# @Last Modified time: 2018-01-12 15:11:11
import time


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

@TimerCost
def p(a, b=10):
	time.sleep(2)
	return a ** b

if __name__ == '__main__':
	def test():
		time.sleep(10)
	with Timer() as timer:
		test()
	print (timer.cost)
	print (p(2))
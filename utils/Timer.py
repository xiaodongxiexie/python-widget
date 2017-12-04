# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-12-04 13:28:45
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2017-12-04 13:33:49
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

if __name__ == '__main__':
	def test():
		time.sleep(10)
	with Timer() as timer:
		test()
	print (timer.cost)
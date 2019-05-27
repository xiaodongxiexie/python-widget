# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-11-17 14:38:13
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2017-11-17 14:43:16
from functools import wraps

def cor(func):
	'''协程装饰器：避免每次调用都要先预激活
	'''
	@wraps(func)
	def execute_next(*args, **kwargs):
		result = func(*args, **kwargs)
		next(result)
		return result
	return execute_next

@cor
def test():
	index = 0
	total = 0
	avg = 0
	while True:
		infos = yield avg
		index += 1
		total += infos
		avg = total / index

if __name__ == '__main__':
	t = test()
	print (t.send(1))
	print (t.send(20))
	print (t.send(200))
	t.close()
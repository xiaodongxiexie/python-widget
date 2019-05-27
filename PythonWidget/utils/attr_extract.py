# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-11-16 14:05:58
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2017-11-16 14:46:56
def e(start='_', module='os'):
	module = __import__(module)
	def gen_attr():
		for attr in dir(module):
			if attr.startswith(start):
				yield attr
	yield from gen_attr()

def e2(start='', module='os'):
	module = __import__(module)
	yield from (attr for attr in dir(module) if attr.startswith(start))


if __name__ == '__main__':
	print (list(e()))
	print (list(e2('a')))
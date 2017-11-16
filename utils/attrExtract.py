# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-11-16 14:05:58
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2017-11-16 14:09:54
def e(start='_', module='os'):
	module = __import__(module)
	def gen_attr():
		for attr in dir(module):
			if attr.startswith(start):
				yield attr
	yield from gen_attr()


if __name__ == '__main__':
	print (list(e()))
# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-01-25 11:34:12
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-01-25 11:35:33
from traceback import format_exc

def test():
	try:1/0
	except:return format_exc()


if __name__ == "__main__":
	r = test()
	print(r)
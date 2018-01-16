# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-01-16 11:52:08
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-01-16 12:00:57
from functools import wraps
import traceback

def retry(retries=3):
	def _retry(func):
		@wraps(func)
		def _wrapper(*args, debug=False, **kwargs):
			index = 0
			result = None
			while index < retries:
				index += 1
				try:
					result = func(*args, **kwargs)
					if result:
						break
				except Exception as e:
					if debug:
						traceback.print_exc()
					else:pass
			return result
		return _wrapper
	return _retry


@retry(10)
def pprint(i):
	return 10 / i


import random


print(pprint(random.choice([0, 1])))
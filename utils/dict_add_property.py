# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-11-21 16:34:12
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-11-21 16:39:41
from collections import abc

class DictAddProperty:
	def __init__(self, mapping):
		self.__data = dict(mapping)

	def __getattr__(self, name):
		if hasattr(self.__data, name):
			return getattr(self.__data, name)
		else:
			return DictAddProperty.build(self.__data[name])

	@classmethod
	def build(cls, obj):
		if isinstance(obj, abc.Mapping):
			return cls(obj)
		elif isinstance(obj, abc.MutableSequence):
			return [cls.build(item) for item in obj]
		else:
			return obj

if __name__ == '__main__':
	test = {'a': 1, 'b': 2, 'c': 3}
	test2 = {'d': 4, 'e': 5, 'f': 6}
	test['g'] = test2
	t = DictAddProperty(test)
	print (t.a, t.b, t.g.d, t.g.e)
# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-01-18 16:19:07
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-01-18 18:01:30
from collections import abc

class FrozenJSON(object):
	def __init__(self, mapping):
		self.__data = dict(mapping)
	def __getattr__(self, name):
		if hasattr(self.__data, name):
			return getattr(self.__data, name)
		else:
			return FrozenJSON.build(self.__data[name])
	@classmethod
	def build(cls, obj):
		if isinstance(obj, abc.Mapping):
			return cls(obj)
		elif isinstance(obj, abc.MutableSequence):
			return [cls.build(item) for item in obj]
		else:
			return obj


if __name__ == "__main__":
	d = {}
	d2 = {'a': 1, 'b': 2}
	c3 = {'d': 3, 'e': 4}
	d2['key2'] = c3
	d['key1'] = d2
	data = FrozenJSON(d)
	print(data.key1.a)
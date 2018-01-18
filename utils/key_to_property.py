# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-01-18 16:19:07
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-01-18 19:31:00
from collections import abc
from keyword import iskeyword


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


class FrozenJSON2(object):
    def __new__(cls, arg):
        if isinstance(abc.Mapping, arg):
            return super().__new__(arg)
        elif isinstance(abc.MutableSequence, arg):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON2(self.__data[name])



if __name__ == "__main__":
    d = {}
    d2 = {'a': 1, 'b': 2}
    c3 = {'d': 3, 'e': 4}
    d2['key2'] = c3
    d['key1'] = d2
    data = FrozenJSON(d)
    print(data.key1.a)
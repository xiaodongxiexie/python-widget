# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/8/6

import sys
import types


class FuncAlreadyExistError(Exception):
    def __init__(self, func_name):
        self.func_name = func_name

    def __repr__(self):
        return f"{self.func_name} already existed"

    __str__ = __repr__


class Blueprint(type):
    def __new__(mcs, name, bases, d):
        if not hasattr(mcs, "__customization_storage__"):
            setattr(mcs, "__customization_storage__", {})
        for k, v in d.items():
            if not hasattr(v, "__customization_name__"):
                continue
            if getattr(v, "__customization_name__") != "customization":
                continue
            storage_key = ".".join([name, k])

            if storage_key in mcs.__customization_storage__:
                raise FuncAlreadyExistError(storage_key)
            else:
                mcs.__customization_storage__[storage_key] = v
        return super().__new__(mcs, name, bases, d)


class blueprint(metaclass=Blueprint):
    ...


class customization:

    def __init__(self, func: callable):
        self.func = func
        self.__customization_name__ = "customization"

    def __call__(self):
        return self.func()

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return types.MethodType(self, instance)


if __name__ == '__main__':

    class T(blueprint):
        @customization
        def test():
            return 0


    for func_name, func in (Blueprint.__customization_storage__).items():
        print(func())



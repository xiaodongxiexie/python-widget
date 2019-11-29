# coding: utf-8

import operator
import types
import sys


def named_tuple(classname, fieldnames):
    cls_dict = {name: property(operator.itemgetter(n))
                for n, name in enumerate(fieldnames)}
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError("Expected {} arguments".format(len(fieldnames)))
        return tuple.__new__(cls, args)
    
    cls_dict["__new__"] = __new__
    
    cls = types.new_class(classname, (tuple, ), {},
                            lambda ns: ns.update(cls_dict))
    cls.__module__ = sys._getframe(1).f_globals["__name__"]
    return cls
    
    

if __name__ == "__main__":
    Point = named_tuple("Point", ["x", "y"])
    p = Point(1, 2)
    print(p.x, p.y)

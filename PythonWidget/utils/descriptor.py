class Typed:

    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]
        
        
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate
    
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
        
'''
In [104]: Stock.name
Out[104]: <__main__.Typed at 0xa3df860>

In [105]: Stock('test', 1, 2.2).name
Out[105]: 'test'

In [106]: Stock('test', 1, 2.2).shares
Out[106]: 1

In [107]: Stock('test', 1, 2.2).price
Out[107]: 2.2
'''

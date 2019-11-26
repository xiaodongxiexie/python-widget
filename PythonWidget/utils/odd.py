class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError("Upper Case is not allowed")
        return super().__new__(cls, clsname, bases, clsdict)
        
class Root(metaclass=NoMixedCaseMeta):...


# ok
class Test(Root):
    def bar(self):...
    

# not ok
class Test(Root):
    def Bar(self):...

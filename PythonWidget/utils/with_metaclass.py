

def with_metaclass(meta, *bases):
    class metaclass(type):
        def __new__(metacls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(meta, "temporary_class", (), {})

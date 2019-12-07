class _NoValueType(object):
    """Special keyword value.

    The instance of this class may be used as the default value assigned to a
    deprecated keyword in order to check if it has been given a user defined
    value.

    This class was copied from NumPy.
    """
    __instance = None

    def __new__(cls):
        # ensure that only one instance exists
        if not cls.__instance:
            cls.__instance = super(_NoValueType, cls).__new__(cls)
        return cls.__instance

    # needed for python 2 to preserve identity through a pickle
    def __reduce__(self):
        return (self.__class__, ())

    def __repr__(self):
        return "<no value>"

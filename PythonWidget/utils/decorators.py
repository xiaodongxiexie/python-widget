#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Most of this code was obtained from the Python documentation online.

"""Decorator utility functions.

decorators:
- synchronized
- propertyx
- accepts
- returns
- singleton
- attrs
- deprecated
"""

import functools
import warnings
import threading
import sys
import types


def synchronized(lock=None):
    """Decorator that synchronizes a method or a function with a mutex lock.

    Example usage:

        @synchronized()
        def operation(self, a, b):
            ...
    """
    if lock is None:
        lock = threading.Lock()

    def wrapper(function):
        def new_function(*args, **kwargs):
            lock.acquire()
            try:
                return function(*args, **kwargs)
            finally:
                lock.release()

        return new_function

    return wrapper


def propertyx(function):
    """Decorator to easily create properties in classes.

    Example:

        class Angle(object):
            def __init__(self, rad):
                self._rad = rad

            @property
            def rad():
                def fget(self):
                    return self._rad
                def fset(self, angle):
                    if isinstance(angle, Angle):
                        angle = angle.rad
                    self._rad = float(angle)

    Arguments:
    - `function`: The function to be decorated.
    """
    keys = ('fget', 'fset', 'fdel')
    func_locals = {'doc': function.__doc__}

    def probe_func(frame, event, arg):
        if event == 'return':
            locals = frame.f_locals
            func_locals.update(dict((k, locals.get(k)) for k in keys))
            sys.settrace(None)
        return probe_func

    sys.settrace(probe_func)
    function()
    return property(**func_locals)


def accepts(*types):
    """Decorator to ensure that the decorated function accepts the given types as arguments.

    Example:
        @accepts(int, (int,float))
        @returns((int,float))
        def func(arg1, arg2):
            return arg1 * arg2
    """

    def check_accepts(f):
        assert len(types) == f.__code__.co_argcount

        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t),\
                    "arg %r does not match %s" % (a, t)
            return f(*args, **kwds)

        new_f.__name__ = f.__name__
        return new_f

    return check_accepts


def returns(rtype):
    """Decorator to ensure that the decorated function returns the given
    type as argument.

    Example:
        @accepts(int, (int,float))
        @returns((int,float))
        def func(arg1, arg2):
            return arg1 * arg2
    """

    def check_returns(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            assert isinstance(result, rtype),\
                "return value %r does not match %s" % (result, rtype)
            return result

        new_f.__name__ = f.__name__
        return new_f

    return check_returns


def singleton(cls):
    """Decorator to ensures a class follows the singleton pattern.

    Example:
        @singleton
        class MyClass:
            ...
    """
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


def attrs(**kwds):
    """Decorator to add attributes to a function.

    Example:

        @attrs(versionadded="2.2",
               author="Guido van Rossum")
        def mymethod(f):
            ...
    """

    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f

    return decorate


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.

    ## Usage examples ##
    @deprecated
    def my_func():
        pass

    @other_decorators_must_be_upper
    @deprecated
    def my_func():
        pass
    """

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.warn_explicit(
            "Call to deprecated function %(funcname)s." % {
            'funcname': func.__name__,
            },
            category=DeprecationWarning,
            filename=func.__code__.co_filename,
            lineno=func.__code__.co_firstlineno + 1
        )
        return func(*args, **kwargs)

    return new_func


def keyword_only(func):
    """
    A decorator that forces keyword arguments in the wrapped method.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 0:
            raise TypeError("Method %s only takes keyword arguments." % func.__name__)
        return func(**kwargs)
    notice = ".. Note:: This method requires all argument be specified by keyword.\n"
    wrapper.__doc__ = notice + wrapper.__doc__
    return wrapper


def deprecated(alternative=None, since=None):
    """
    Decorator for marking APIs deprecated in the docstring.

    :param func: A function to mark
    :returns Decorated function.
    """

    def deprecated_decorator(func):
        since_str = " since %s" % since if since else ""
        notice = (
            ".. Warning:: ``{function_name}`` is deprecated{since_string}. This method will be"
            " removed in a near future release.".format(
                function_name='.'.join([func.__module__, func.__name__]),
                since_string=since_str)
        )
        if alternative is not None and alternative.strip():
            notice += " Use ``%s`` instead." % alternative

        @wraps(func)
        def deprecated_func(*args, **kwargs):
            warnings.warn(notice, category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        if func.__doc__ is not None:
            deprecated_func.__doc__ = notice + "\n" + func.__doc__

        return deprecated_func

    return deprecated_decorator


class Elapsed:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        end = time.perf_counter()
        logger.info("%s elapsed time: %d", self.func.__name__, end - start)
        return result

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)
        
 
from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper

# Example use
@logged
def add(x, y):
    return x + y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')



_missing = object()

class locked_cached_property(object):
    """A decorator that converts a function into a lazy property.  The
    function wrapped is called the first time to retrieve the result
    and then that calculated result is used the next time you access
    the value.  Works like the one in Werkzeug but has a lock for
    thread safety.
    """

    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func
        self.lock = RLock()

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        with self.lock:
            value = obj.__dict__.get(self.__name__, _missing)
            if value is _missing:
                value = self.func(obj)
                obj.__dict__[self.__name__] = value
            return value
        
class cached_property(property):
    """
    A property that is only computed once per instance and then replaces
    itself with an ordinary attribute. Deleting the attribute resets the
    property.
    """

    def __init__(self, func: Callable) -> None:
        self.__doc__ = getattr(func, "__doc__")
        self.func = func

    def __get__(self, obj: Any, cls: Optional[type] = None) -> Any:
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value
   

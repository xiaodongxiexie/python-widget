import logging
from functools import partial, wraps

def logged(func=None, *, level=logging.DEBUG, name=None, msg=None):
    if func is None:
        # or
        # return lambda func: logged(func, level=level, name=name, msg=msg)
        return partial(logged, level=level, name=name, msg=msg)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = msg if msg else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper


# then you can use like this
@logged
def add(x, y):
    return x + y

# or you can use like this
@logged()
def add(x, y):
    return x + y

# or this
@logged(level=logging.CRITICAL, name="example")
def add(x, y):
    return x + y

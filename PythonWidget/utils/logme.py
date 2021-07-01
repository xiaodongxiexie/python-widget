# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2021/6/24

import logging
import functools


logger = logging.getLogger("helper.util")


def logme(f=None, *, level=logging.INFO, logger=logger):
    if f is None:
        return functools.partial(logme, level=level)

    _logger = functools.partial(logger.log, level)

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        _logger(
            "[input] [funcname]%s, [args] %s, [kwargs] %s",
            f.__name__,
            ",".join([str(obj) for obj in args]),
            ",".join(["{k}={v}".format(k=k, v=v) for k, v in kwargs.items()])
        )
        rs = f(*args, **kwargs)
        _logger("[output] %s", rs)
        return rs

    return wrap
 

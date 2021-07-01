# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2021/7/01

import time
import logging
from functools import wraps, partial


logger = logging.getLogger("helper.retry")


def retry(f: callable = None, max_retry_time: int = 3, wait_seconds: int = 0, allow_exception: tuple = (Exception, )):
    """
    用于网络异常等允许的错误进行失败重试
    :param f: 待调用函数
    :param max_retry_time:最大重试次数
    :param wait_seconds: 每次重试间隔秒数
    :param allow_exception:哪些异常允许重试
    :return:callable
    """
    if f is None:
        return partial(retry, max_retry_time=max_retry_time, wait_seconds=wait_seconds, allow_exception=allow_exception)

    @wraps(f)
    def wrapped(*args, **kwargs):
        ee = None
        for retry_time in range(max_retry_time):
            if wait_seconds > 0:
                time.sleep(wait_seconds)
            try:
                result = f(*args, **kwargs)
                return result
            except allow_exception as e:
                logger.exception(
                    "[retry][allow-exception] %s, [retry-number] %s",
                    type(e), retry_time + 1, exc_info=True
                )
                ee = e
                continue
        else:
            raise ee
    return wrapped


retryme = retry

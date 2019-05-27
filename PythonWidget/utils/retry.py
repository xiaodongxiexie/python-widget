# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-01-16 11:52:08
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-01-16 13:24:49
from functools import wraps
import traceback

def retry(retries=3, debug=False):
    def _retry(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            index = 0
            result = None
            while index < retries:
                index += 1
                try:
                    result = func(*args, **kwargs)
                    if result:
                        break
                except Exception as e:
                    if debug:
                        traceback.print_exc()
                    else:pass
            return result
        return _wrapper
    return _retry


@retry(10)
def do_something_unreliable():
    import random
    if random.randint(0, 10) > 1:
        raise IOError("failed!")
    else:
        return 'congratulations!'

if __name__ == "__main__":
    print(do_something_unreliable())
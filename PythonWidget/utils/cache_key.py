# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
"""
从扇贝看来的。
"""

DEFAULT_KEY_TYPES = (str, int, float, bool)


def norm_cache_key(v):
	if isinstance(v, type):
		return v.__name__
	if isinstance(v, bytes):
		return v.decode()
	if v is None or isinstance(v, DEFAULT_KEY_TYPES):
		return str(v)
	else:
		raise ValueError("only {} can be key".format(", ".join(map(lambda obj: obj.__name__, DEFAULT_KEY_TYPES))))


def default_key(f, *args, **kwargs):
	keys = [norm_cache_key(v) for v in args]
	keys += sorted(
		["{}={}".format(k, norm_cache_key(v))
		 for k, v in kwargs.items()]
		)
	return "default.{}.{}.{}".format(f.__module__,
								     f.__name__,
								     ".".join(keys)
									)


if __name__ == "__main__":
	def test(*args, **kwargs):
		pass

	print(default_key(test, 1, 2, 3, 4, a=1, b=2))
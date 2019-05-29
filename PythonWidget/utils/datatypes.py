# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
from itertools import repeat


def is_immutable(self):
	raise TypeError("{} objects are immutable".format(self.__class__.__name__))


class ImmutableDict(dict):
	_hash_cache = None

	@classmethod
	def fromkeys(cls, keys, value=None):
		return cls(zip(keys, repeat(value)))

	def __reduce_ex__(self, protocol):
		return type(self), (dict(self), )

	def __hash__(self):
		if self._hash_cache is not None:
			return self._hash_cache
		rv = self._hash_cache = hash(frozenset(self.items()))

	def setdefault(self, key, default=None):
		is_immutable(self)

	def update(self, *args, **kwargs):
		is_immutable(self)

	def pop(self, key, default=None):
		is_immutable(self)

	def popitem(self):
		is_immutable(self)

	def __setitem__(self, key, value):
		is_immutable(self)

	def __delitem__(self, key):
		is_immutable(self)

	def clear(self):
		is_immutable(self)

	def __repr__(self):
		return "{}({})".format(
			self.__class__.__name__,
			dict.__repr__(self),
			)

	def copy(self):
		return dict(self)

	def __copy__(self):
		return self


class ConstantsObject(ImmutableDict):

	def _-getattr__(self, name):
		return self[name]

	def __setattr__(self, name, value):
		self[name] = value

	def __dir__(self):
		return self.keys()

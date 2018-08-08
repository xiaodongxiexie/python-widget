# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import sys


def get_cur_lineno():
	return sys._getframe(1).f_lineno


if __name__ == "__main__":
	print('当前所在行数: {}'.format(get_cur_lineno()))
	for i in range(10):
		pass
	print('当前所在行数: {}'.format(get_cur_lineno()))





	print('当前所在行数: {}'.format(get_cur_lineno()))

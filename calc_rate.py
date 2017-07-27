# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-07-27 22:50:22
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-07-27 23:33:07
import pandas as pd

def calc_rate(start, end, price):
	'''
	start: 起始日期， 格式：月日，example：0727
	end： 同start
	price： 价格
	'''
	start = pd.to_datetime('2017%s' % start)
	end = pd.to_datetime('2017%s' % end)
	return int(price) * (( end - start).days)

if __name__ == '__main__':
	i = 1
	init = 0
	while i:
		if init == 0:
			start = input('输入起始日期： ')
		else:
			start = end
		end = input('输入终止日期： ')
		price = input('输入每日利息：')
		now = calc_rate(start, end, price)
		init += now
		print('当前利息为：', init, 'RMB', '\n')
		quit = input('是否继续: (y/n) ')
		if quit.replace(' ', '').startswith('n'):
			i = 0
			print('总利息为： ', init, 'RMB')

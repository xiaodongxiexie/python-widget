# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-07-27 22:50:22
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-07-28 00:02:44
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

def calc_quick(seq, price):
	assert len(seq) - 1 == len(price), '是不是忘了输入今天的日期！'
	init = 0.0
	for index, time in enumerate(seq[:-1]):
		start = pd.to_datetime('2017%s' % time)
		end = pd.to_datetime('2017%s' % seq[index+1])
		init += price[index] * ((end-start).days)
	print('总利息为： ', init, 'RMB')

def route(default=0):
	return 1 if not default else 0


if __name__ == '__main__':
	if route(1):
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
	else:
		#pass
		calc_quick(['0126', '0201', '0409', '0510', '0727'], [30, 60, 45, 60])


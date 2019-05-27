# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-07-28 00:14:15
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-07-28 00:17:20


f = lambda x: min(max(x, 0), 100)   #输入一个数字，若小于0， 则返回0，若大于100则返回100，否则返回自身
								    #类似于numpy.clip(x, 0, 100)

def (x):
	return 0 if x else 1            #三元路由
#coding: utf-8

#递归使用嵌套字典

from collections import defaultdict

def tree():
    return defaultdict(tree)
    
    
    
c = defaultdict(tree)

c['h']['username'] = 'xxx'

c['l']['username'] = 'xxxx'

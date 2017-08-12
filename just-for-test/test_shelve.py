#shelve是一个轻量级数据存储方式，类似与数据库

import shelve
import contextlib

#写入

#python 3
with shelve.open('test.db', writeback=True) as s:
    s['key1'] = {'int': 10, 'float': 10.24, 'string': 'just for test'}

#python 2
#利用contextlib.closing 实现with管理
with contextlib.closing(shelve.open('test.db', writeback=True) as s:
    s['key1'] = {'int': 10, 'float': 10.24, 'string': 'just for test'}
    
    
   

# -*- coding: utf-8 -*-
# @Author: liangxiaodong
# @Date:   2017-05-23 20:40:01
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-05-23 21:25:32

import os, sys
import　binascii
import pdir


print __file__  #用于输出当前文件路径
print sys.argv[0]  #输出相对路径
print os.path.abspath(sys.argv[0])  #输出绝对路径
print os.path.dirname(__file__)  #输出父目录
print os.urandom(10)  #随机输出10个二进制
print binascii.b2a_base64(os.urandom(10))  #将随机输出的10个二进制转换为ascii





# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import requests
import time

url = 'http://time.tianqi.com'
url2 = 'http://cgi.im.qq.com/cgi-bin/cgi_svrtime'
url3 = 'http://api.k780.com/?app=life.time&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json'

# nums = 0
# while nums < 100:
#     nums += 1
#     info = requests.get(url2)
#     print(info.text)
#     time.sleep(0.1)

info_0 = requests.get(url2)
info = requests.get(url3)

print(info_0.text)
print(info.json()['result']['datetime_1'])
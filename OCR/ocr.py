# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import os
from configparser import ConfigParser

from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'


conf = ConfigParser()
dirname = os.path.split(os.path.abspath(__file__))[0]

conf.read(os.path.join(dirname, 'baidu_keys.cfg'), encoding='utf-8')

APP_ID = conf.get('key', 'APP_ID')
API_KEY = conf.get('key', 'API_KEY')
SECRET_KEY = conf.get('key', 'SECRET_KEY')


client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('test.jpg')

""" 调用通用文字识别, 图片为远程url图片 """
#res=client.basicGeneralUrl(url);

""" 调用通用文字识别, 图片为本地图片 """
res=client.general(image)
num = 0
for ele in res['words_result']:
	# print(ele)
	print(ele['words'])
	num += 1
	if num > 20:
		break

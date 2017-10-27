# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-10-26 16:24:27
# @Last Modified by:   xiaodong
# @Last Modified time: 2017-10-26 16:25:04
def OpenURL(url):
# url = "http://192.168.10.34:8080/ai?cmd=load"
    import traceback
    import urllib.request
    from urllib.parse import quote
    url = quote(url,safe='/:?=')
#     print(url)
#     import urllib
#     print (urllib.parse.unquote(url))
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            #pass
            the_page = response.read()
            #print(the_page)
        return the_page
    except:
        return traceback.print_exc()


ai_ip = '192.168.20.72'
ai_port = 8090
ai_arg = 'cmd=match&topN=6&debug1=1'
#X = [[{'ot': '区域', 'oc': '卧室', 'x': 100, 'y': 0, 'z': 0, 'dx': 3580, 'dy': 3300, 'dz': 0, 'ori': [{'points': [{'x': 100, 'y': 0}, {'x': 3680, 'y': 0}, {'x': 3680, 'y': 3300}, {'x': 1550, 'y': 3300}, {'x': 1550, 'y': 3200}, {'x': 100, 'y': 3200}, {'x': 100, 'y': 0}]}]}, {'ot': '门窗', 'oc': '房门', 'x': 100, 'y': 3200, 'z': 0, 'dx': 1000, 'dy': 0, 'dz': 0, 'ori': [{'points': [{'x': 100, 'y': 3200}, {'x': 1100, 'y': 3200}]}]}, {'ot': '门窗', 'oc': '窗户', 'x': 1400, 'y': 0, 'z': 0, 'dx': 1000, 'dy': 0, 'dz': 0, 'ori': [{'points': [{'x': 1400, 'y': 0}, {'x': 2400, 'y': 0}]}]}]]
Y = [[{'id': 1, 'ot': '家具', 'oc': '电视柜', 'x': 0, 'y': 0, 'z': 0, 'dx': 880, 'dy': 1200, 'dz': 850, 'ori': {'seqNo': 1, 'skuId': 40245, 'name': 'n［联邦家私 轻时尚］ 桦木 人造板 (1R)懒人沙发', 'categoryId': 1044, 'classify': 'tv_cabinet', 'length': 1200, 'width': 880, 'height': 850, 'pakUrl': 'http://7xqguc.com2.z0.glb.clouddn.com/1506431545953-2-44157.pak', 'points': []}}, {'id': 2, 'ot': '家具', 'oc': '床头柜', 'x': 0, 'y': 0, 'z': 0, 'dx': 880, 'dy': 836, 'dz': 750, 'ori': {'seqNo': 2, 'skuId': 43169, 'name': 'n【联邦家私  新东方】中式  皮艺 沙发', 'categoryId': 1044, 'classify': 'bedstand', 'length': 836, 'width': 880, 'height': 750, 'pakUrl': 'http://7xqguc.com2.z0.glb.clouddn.com/1506431545953-2-44157.pak', 'points': []}}, {'id': 3, 'ot': '家具', 'oc': '床', 'x': 0, 'y': 0, 'z': 0, 'dx': 980, 'dy': 1630, 'dz': 950, 'ori': {'seqNo': 3, 'skuId': 44157, 'name': 'n【兴利 澳玛 珞美】美式  布艺 沙发', 'categoryId': 1045, 'classify': 'bed', 'length': 1630, 'width': 980, 'height': 950, 'pakUrl': 'http://7xqguc.com2.z0.glb.clouddn.com/1506431545953-2-44157.pak', 'points': []}}]]

#url="http://{}:{}/ai?{}&x={}&y={}".format(ai_ip,ai_port,ai_arg,X[0],Y[0])


for dx in range(2000, 5001, 100):
    for dy in range(2000, 5001, 100):
        X = [[{'ot': '区域', 'oc': '卧室', 'x': 100, 'y': 0, 'z': 0, 'dx': dx, 'dy': dy, 'dz': 0, 'ori': [{'points': [{'x': 100, 'y': 0}, {'x': 3680, 'y': 0}, {'x': 3680, 'y': 3300}, {'x': 1550, 'y': 3300}, {'x': 1550, 'y': 3200}, {'x': 100, 'y': 3200}, {'x': 100, 'y': 0}]}]}, {'ot': '门窗', 'oc': '房门', 'x': 100, 'y': 3200, 'z': 0, 'dx': 1000, 'dy': 0, 'dz': 0, 'ori': [{'points': [{'x': 100, 'y': 3200}, {'x': 1100, 'y': 3200}]}]}, {'ot': '门窗', 'oc': '窗户', 'x': 1400, 'y': 0, 'z': 0, 'dx': 1000, 'dy': 0, 'dz': 0, 'ori': [{'points': [{'x': 1400, 'y': 0}, {'x': 2400, 'y': 0}]}]}]] 
        url="http://{}:{}/ai?{}&x={}&y={}".format(ai_ip,ai_port,ai_arg,X[0],Y[0])
        infos = OpenURL(url)
        if len(infos) == 0:
            print ('无输出信息:dx: %s, dy: %s ' % (dx, dy))
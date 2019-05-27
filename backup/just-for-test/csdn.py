#-*-coding:utf8-*-

import urllib.request

from bs4 import BeautifulSoup
import re
import time
import random
import threading


# -------------------------------------------------------公用方法----------------------------------------------------
class CommanCalss:
    def __init__(self):
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
        self.testurl="www.baidu.com"

    def getresponse(self,url):
        req = urllib.request.Request(url, headers=self.header)
        resp = urllib.request.urlopen(req, timeout=5)
        content = resp.read().decode('utf-8', 'ignore')
        return content

    def getresponse_p(self,url, pro):
        proxy_support = urllib.request.ProxyHandler({"http": pro})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        # 访问
        Max_Num = 2
        for i in range(Max_Num):
            try:
                req = urllib.request.Request(url, headers=self.header)
                page = urllib.request.urlopen(req, timeout=3)
                pagecontent = page.read().decode('utf-8', 'ignore')
                break
            except:
                if i < Max_Num - 1:
                    continue
                else:
                    print("sorry,proxy error")
        return pagecontent

    #代理IP是否有用
    def _is_alive(self,proxy):
        try:
            proxy_support = urllib.request.ProxyHandler({"http": proxy})
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
            req = urllib.request.Request(self.url, headers=self.header)
            # 访问
            resp=urllib.request.urlopen(req,timeout=5)
            return True
        except:
            return False

# ------------------------------------------------------------
# 一、获取代理模块
# ------------------------------------------------------------

 # -------1.1、代理池-----------------------------------------
class ProxyPool:
    def __init__(self,proxy_finder):
        self.pool=[]
        self.proxy_finder=proxy_finder
        self.cominstan=CommanCalss()

    def get_proxies(self):
        self.pool=self.proxy_finder.find()
        for p in self.pool:
            if self.cominstan._is_alive(p):
                continue
            else:
                self.pool.remove(p)

    def get_one_proxy(self):
        return random.choice(self.pool)

    def writeToTxt(self,file_path):
        try:
            fp = open(file_path, "w+")
            for item in self.pool:
                fp.write(str(item) + "\n")
            fp.close()
        except IOError:
            print("fail to open file")

#--------1.2、获取代理方法---------------------------------------
#定义一个基类
class IProxyFinder(object):
    def __init__(self):
        self.pool = []

    def find(self):
        return

#西祠代理爬取
class XiciProxyFinder(IProxyFinder):
    def __init__(self, url):
        super(XiciProxyFinder,self).__init__()
        self.url=url
        self.cominstan = CommanCalss()

    def find(self):
        for i in range(1, 10):
            content = self.cominstan.getresponse(self.url + str(i))
            soup = BeautifulSoup(content)
            ips = soup.findAll('tr')
            for x in range(2, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                if tds == []:
                    continue
                ip_temp = tds[1].contents[0] + ":" + tds[2].contents[0]
                self.pool.append(ip_temp)
        time.sleep(1)
        return  self.pool

#---------1.3、测试---------------------------------------------
#finder = XiciProxyFinder("http://www.xicidaili.com/wn/")
#ppool_instance = ProxyPool(finder)
#ppool_instance.get_proxies()
#ppool_instance.writeToTxt("e:\\proxy.txt")



# ------------------------------------------------------------
# 二、刷访问量模块开始
# ------------------------------------------------------------
class AddPV:
    def __init__(self):
        self.pool=[]
        self.cominstan = CommanCalss()

    # -----2.1、获取代理--------------------------------------------
    # -----2.2.1从代理池中获取----------
    def getProxyList(self):
        finder = XiciProxyFinder("http://www.xicidaili.com/wn/")
        ppool_instance = ProxyPool(finder)
        ppool_instance.get_proxies()
        self.pool = ppool_instance.pool

    # -----2.2.2从文件中读取-----------
    def getProxyList(self, filename):
        f = open(filename, "r")
        lines = f.readlines()  # 读取全部内容
        for line in lines:
            self.pool.append(line[:-1])

    # -----2.2、刷访问量--------------------------------------------
    # -----2.2.1 刷单个博客页面-----------------------
    def visitOnePage(self, brushNum, url):
        for j in range(brushNum):
            try:
                pro = random.choice(self.pool)
                pageContent = self.cominstan.getresponse_p(url, pro)
                # 使用BeautifulSoup解析每篇博客的标题
                soup = BeautifulSoup(pageContent)
                blogTitle = str(soup.title.string)
                blogTitle = blogTitle[0:blogTitle.find('-')]
                viewnums = soup.find_all('span', class_='link_view')
                print(blogTitle, viewnums)
            except:
                #self.pool.remove(pro)
                continue
            time.sleep(0.5)  # 正常停顿，以免服务器拒绝访问

    # -----2.2.2、刷所有博客页面---------------------
    def getAllPages(self,username):
        # csdn首页
        urlBase = "http://blog.csdn.net"  # 需要将网址合并的部分
        # 自己的博客主页
        url = urlBase + "/" + username
        try:
            pagecontent = self.cominstan.getresponse(url)
            p = re.compile('/' + username + '/article/details/........')
            allfinds = p.findall(pagecontent)
            mypages = list(set(allfinds))
            for i in range(len(mypages)):
               mypages[i] = urlBase + mypages[i]
            return mypages
        except:
            print("寻找博客列表出错")

    def visitAllPages(self, brushNum, username):
        # 所有的页面都刷
        pagelist=self.getAllPages(username)
        for i in range(brushNum):
            page=random.choice(pagelist)
            self.visitOnePage(2, page)


# ------------------------------------------------------------
#三、运行程序
# ------------------------------------------------------------
#将代理保存在D盘，直接读，如果没保存，就运行一遍上面测试内容
csdn = AddPV()

def shuashua():
    #csdn.visitAllPages(10000,"xiaodongxiexie")             #刷你所有博客的浏览量 （输入你的CSDN博客ID）
    #csdn.visitOnePage(2000, "http://blog.csdn.net/xiaodongxiexie/article/details/78043681")     #刷你单篇博客的浏览量（输入你博客的链接地址）
    csdn.visitOnePage(2000, 'http://blog.csdn.net/xiaodongxiexie/article/details/78043681')
    time.sleep(1)

def main():
    threadpool=[]
    try:
        csdn.getProxyList("e:\\proxy.txt")
    except:
     finder = XiciProxyFinder("http://www.xicidaili.com/wn/")
     ppool_instance = ProxyPool(finder)
     ppool_instance.get_proxies()
     ppool_instance.writeToTxt("e:\\proxy.txt")
     csdn.getProxyList("e:\\proxy.txt")

    for i in range(30): #定义线程数
        th = threading.Thread(target=shuashua)
        threadpool.append(th)

    for th in threadpool:
        th.start()

    for th in threadpool :
        threading.Thread.join( th )

if __name__ == '__main__':
    main()

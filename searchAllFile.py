#coding: utf-8

#使用递归查找指定目录下所有文件，并美化输出
import os
import glob
def searchFile(root_path,flag=0):
    if glob.glob(os.path.join(root_path, '*')):
        for x in glob.glob(os.path.join(root_path, '*')):
            if flag >= 1:
                print '\t'*flag, x
            else:
                print x
            flag += 1
            searchFile(x, flag=flag)

if __name__ == '__main__':
    searchFile('.')

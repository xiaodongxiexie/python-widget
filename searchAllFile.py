#coding: utf-8

#使用递归查找指定目录下所有文件，并美化输出
import os
import glob
def searchFile(root_path,flag=0):
    if glob.glob(os.path.join(root_path, '*')):
        for x in glob.glob(os.path.join(root_path, '*')):
            if flag == 1:
                print '\t\t', x
            else:
                print x
            searchFile(x, flag=1)

if __name__ == '__main__':
    searchFile('.')

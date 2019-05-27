#coding: utf-8

import os
import tarfile
import zipfile

def zip2tar(root_path, name,to_name='test'):
    
    '''
    root_path: 压缩文件所在根目录
    name： 压缩文件名字（zip格式）
    '''
    #root_path = r'C:\Users\Administrator\Desktop\myfiles'
    #file_path = os.path.join(root_path, 'mymodel.zip')
    
    file_path = os.path.join(root_path, name+'.zip')

    with zipfile.ZipFile(file_path, 'r') as zzip:
        with tarfile.open(os.path.join(root_path, to_name+'.gz.tar'), 'w') as ttar:
            for ffile in zzip.namelist():
                if not os.path.isdir(ffile):
                #if not ffile.strip().endswith(r'/'):
                    zzip.extract(ffile, root_path)
                    ttar.add(os.path.join(root_path,ffile), arcname=ffile)


if __name__ == '__main__':

    root_path = raw_input(u'input root path: ')
    name = raw_input(u'input the zip name(without .zip): ')
    zip2tar(root_path, name)

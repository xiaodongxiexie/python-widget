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
            
            
#输出指定目录下所有文件大小总和，可选为MB或者GB
def check_memory(path, style='M'):
    i = 0
    for dirpath, dirname, filename in os.walk(path):
        for ii in filename:
            i += os.path.getsize(os.path.join(dirpath,ii))
    if style == 'M':
        memory = i / 1024. / 1024.
        print memory
        return memory 
    else:
        memory = i / 1024. / 1024./ 1024.
        print memory
        return memory
    
import ctypes
import os
import platform
import sys

#获取剩余空间内存大小
def get_free_space_mb(folder):
    """ Return folder/drive free space (in bytes)
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value/1024/1024/1024 
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize/1024/1024

if __name__ == '__main__':
    searchFile('.')
    check_memory('.', '')
    get_free_space_mb('.')

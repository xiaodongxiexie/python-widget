#coding: utf-8


import os
import glob
def searchFile(root_path):
    if glob.glob(os.path.join(root_path, '*')):
        for x in glob.glob(os.path.join(root_path, '*')):
            print x  
            searchFile(x)

#coding: utf-8

import os, glob, time

def search_all_files_return_by_time_reversed(path, reverse=True):
	return sorted(glob.glob(os.path.join(path, '*')), key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))), reverse=reverse)

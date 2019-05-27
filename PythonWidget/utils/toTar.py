#coding: utf-8


import tarfile
import glob


'''
doc: 将文件添加到压缩文件中
使用介绍：将该脚本拖入到要压缩文件所在的文件夹后启动即可完成压缩
注意：   会将所在文件夹所有文件（除该脚本或py文件外）压缩
'''

def toTar(name='test'):
	with tarfile.open('%s.gz.tar'%name, 'w') as f:
		for doc in glob.glob('*'):
			if 'py' not in doc:
				f.add(doc)

if __name__ == '__main__':

	toTar()

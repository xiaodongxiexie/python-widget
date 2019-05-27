#coding: utf-8


from shutil import copytree
from shutil import move
from os import chdir
from os.path import exists
from os.path import pardir
from os import makedirs
from os import removedirs
from os import rename


def create_directory(name):
	if exists(pardir+'\\'+name):
		print 'Foler already exists... Cannot Overwrite this'
	else:
		makedirs(pardir+'\\'+name)

def delete_directory(name):
	removedirs(name)


def rename_directory(direct, name):
	rename(direct, name)


def set_working_directory():
	chdir(pardir)


def backup_files(name_dir, folder):
	copytree(pardir, name_dir+':\\'+folder)

def move_folder(filename, name_dir, folder):
	if not exists(name_dir+':\\'+folder):
		makedirs(name_dir+':\\'+folder)
	move(filename, name_dir+':\\'+folder+'\\')



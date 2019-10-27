# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide

# ==============================================================
# __future__ 导入时必须放在最开始
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import


# 开发环境
# ==============================================================
# 

# 内置封装
# ==============================================================
import builtins


# python2 to python3
from six import string_stypes, iteritems, add_metaclass
from six.moves import map


# ==============================================================
# 系统操作

import os
import sysconfig
import sys
import platform                   # 可以查看终端情况（如版本情况)
import ctypes                     # python和C的混合编程工具
import subprocess


# 内置库（常用）
# ==============================================================
import itertools
from itertools import accumulate, chain, combinations, compress
from itertools import cycle, dropwhile, permutations, product
from itertools import zip_longest

import collections
from collections import abstractmethod, namedtuple
from collections import Counter, defaultdict
from collections import deque
from collections import OrderedDict

import logging
from logging.handlers import RotatingFileHandler

import functools
from functools import wraps, update_wrapper
from functools import partial

import random
from random import randint, random
from random import choice, sample

import math
from math import fsum, hypot, inf

import cmath
import decimal
# import cdemical
import fractions
import hashlib

import time
from time import perf_counter, clock

import datetime
from datetime import date, datetime, timedelta

import threading
from threading import Thread

import multiprocessing
from multiprocessing import Pool, Process

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

import contextlib

from copy import copy, deepcopy

from io import BytesIO
from inspect import signature


# Python 内存，CPU，IO管理
# ==============================================================
# pip install psutil
import psutil                     # 查看内存占用, CPU, IO等

# pip install pympler
import pympler                    # 查看Python对象内存行为

import gc                         # 垃圾回收


# Python对象追溯
# ==============================================================
import inspect


# Python 实现的单派模式
# ==============================================================
from functools import singledispatch
from multipledispatch import dispatch




# Python方法、属性操作
# ==============================================================
import operator
from operator import methodcaller
from operator import attrgetter, itemgetter, concat


# 编码及解析
# ==============================================================
import encodings                 # help(encodings) 关于所有Python内置编码方式
import chardet                   # 检测编码
import mimetypes                 # 检测文件MIME类型
import filetype                  # 类型推断
from unidedata import normalize, name

import base64
import hmac


# 文件路径处理
# ==============================================================
import os.path
import path
import pathlib
import pathlib2
import pathtools
import glob
import fnmatch
import codecs


# 文件详情(路径、内容, 文件操作等)
# ==============================================================
import glob
import fnmatch
import linecache
import filecmp                 # 文件差异比较

import csv
import h5py

# excel 读写
# pip install xlrd
import xlrd
# pip install xlwt
import xlwt
# pip install xlutils
from xlutils.copy import copy  # 用于 excel的复制操作

import xlsxwriter              # 支持excel写（较全操作，不支持读）

import shutil
import tempfile
import shelve

# pip install watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 给文件加锁
import fcntl

# pip install lockfile
from lockfile import LockFile     # 给文件加锁


# 错误追踪及异常捕捉
# ==============================================================
import trace                   # 用于命令行操作
import traceback

# pip install stackprinter
# github: https://github.com/cknd/stackprinter
import stackprinter            # 好用的debug追踪


# 重载
# ==============================================================
from imp import reload
from importlib import reload


# IO 相关
# ==============================================================
# pip install colorama
import colorma                  # 改变输出流背景颜色等
import fileinput
from io import StringIO
import readline
import pep8
import struct
import cPickle

# 内存占用优化
# ==============================================================
# https://github.com/pytries/hat-trie
# pip install hat-trie

# https://pypi.org/project/datrie/
# https://linux.thai.net/~thep/datrie/datrie.html
# pip install datrie

# pip install DAWG         # String data in a DAWG may take 
                           # 200x less memory than in a standard 
                           # Python dict and the raw lookup speed is comparable; 
                           # it also provides fast advanced methods like prefix search.

# pip install marisa-trie
import marisa_trie         # https://marisa-trie.readthedocs.io/en/latest/tutorial.html

# 警告处理
# ==============================================================
import warnings
warnings.filterwarnings("ignore") # 用于忽略警告内容，专治强迫症


# 包管理
# ==============================================================
import pkgutil
# pkgutil.get_importer(path_item)
# pkgutil.get_data(package, resource)


# 动态管理
# ==============================================================
import importlib              # 实现动态引入模块
#math = importlib.import_module('math')


# 常用第三方扩展
# ==============================================================
# pip install pdir2
import pdir

# pip install tqdm
import tqdm

#  pip install Faker
import faker                  # 生成虚假姓名、性别、地址、邮政编码等（支持中文）

# pip install mimesis
import mimesis                # 生成虚假姓名、性别、地址等（支持中文）

# pip install xpinyin
import xpinyin                # 将汉字转换为拼音（支持带声调）

# pip install pypinyin
import pypinyin               # 将汉字转换为拼音

# pip install sfz
import sfz                    # 解析大陆身份证信息（如所在地区、性别等）

#  pip install retrying
import retrying               # 自动尝试多次执行直到任务成功或达到设置条件

# pip install tqdm
import tqdm                   # 便捷查看循环执行进度

# pip install goto-statement
from goto import with_goto    # python实现的goto跳转（不适合多层循环）


# 爬虫相关
# ==============================================================
# pip install fake-useragent
import fake_useragent          # 生成虚假头部浏览器头部信息

import requests

# pip install grequests
import grequests               # 通过gevent 实现多线程的requests

import bs4
import urllib
import cookie
import html
from html import escape, unescape
import htmllib
import HTMLParser
import selenium
import webbrowser
import lassie
import tushare
import urlparse
import xml
import furl
import pyquery
import hyperlink
import parsel
import yarl

# pip install robobrowser
import robobrower                  # 可解析js


# scrapy
from scrapy.loader import ItemLoader     # 将xpath包装
from scrapy.loader.processors import MapCompose, Join  # 以函数链实现复杂功能

# pip install scrapy-redis
import scrapy_redis


# 定时任务/定时操作
# ==============================================================
# pip install schedule
import schedule

# pip install apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler

import sched


# 图形识别/图形处理
# ==============================================================
# pip install opencv-python
import cv2

import imghdr                   # 识别图形格式
import PIL

# pip install imagehash
import imagehash                # 图片指纹hash，用于相似图片检测/检索

# pip install pytesseract
import pytesseract              # 与openCV联合使用，做简单验证码识别等

# https://www.lfd.uci.edu/~gohlke/pythonlibs/#simpleitk
import SimpleITK as sitk

import skimage
from skimage import data, io, filters

import imagesize
import imghdr


# 格式相关
# ==============================================================
from pprint import pprint

# pip install PrettyTable
from prettytable import PrettyTable    # 美化表格输出

# pip install reprint
from reprint import output

# pip install uniout
import uniout

# pip install prettyprinter
from prettyprinter import cpprint

import textwrap                 # 修饰字符串输出格式
import fileinput
from reprlib import repr


# 字符串相关
# ==============================================================
import this                     # Python之禅
import string
import keyword                  # 保留关键字

import re

# pip install flashtext
from flashtext.keyword import KeywordProcessor

# pip install parse
from parse import findall, search

# pip install html2text
import html2text

# pip install colorama
import colorma                  # 改变输出流背景颜色等


# 字符串匹配
# ==============================================================
# pip install fuzzywuzzy
import fuzzywuzzy

# pip install pangu
import pangu                    # 分词处理

# pip install python-Levenshtein
import Levenshtein              # 斯文斯坦距离（字符串相似度比较）

# pip install textdistance
import textdistance             # 文本相似度比较

import difflib                  # 字符串相似度比较


# 排序算法
# ==============================================================
# pip install sortedcontainers
import sortedcontainers

# pip install sortedcollections
import sortedcollections       # 包含列表排序、集合排序、字典排序

# pip install algorithms
import algorithms

# pip install natsort
import natsort                 # 自然排序

# pip install funcy
from funcy import flatten, isa # 嵌套数组展平，各种迭代等

import bisect                  # 排序数组插入数据
import heapq                   # heapq.merge 有序列表快速合并


# Windows
# ==============================================================
import winreg


# 缓存
# ==============================================================
# pip install cachetools
import cachetools
from cachetools import lru_cache

from functools import lru_cache

from fastcache import lru_cache
from fastcache import clru_cache

import zict


# 装饰器
# ==============================================================
from functools import wraps, update_wrapper

import decorator


# 配置
# ==============================================================
import configparser
import yaml


# 命令行相关
# ==============================================================
import argparser                        # 命令行解析
import optparse                         # 解析命令行

# pip install fire
import fire                             # 生成命令行界面工具

# pip install click
import click                            # 通过装饰器进行命令行界面生成


# 枚举
# ==============================================================
import enum
from enum import Enum, unique


# 内置类型名目
# ==============================================================
import types
from types import MappingProxyType        # 可用来实现只读字典接口


# 类型标注
# ==============================================================
import typing
from typing import Any, AnyStr, Callable, ChainMap, Counter
from typing import Deque, DefaultDict, Dict, FrozenSet
from typing import Generator, Hashable, Iterable, Iterator
from typing import List, Mapping, MutableMapping, MutableSequence, MutableSet
from typing import NamedTuple, Optional
from typing import Sequence, Set, Sized
from typing import Text, Tuple, Union

# Data validation and settings management using python type hinting.
# pip install pydantic
from pydantic import BaseModel
from pydantic.dataclasses import dataclass

from dataclasses import dataclass


# 序列化 相关
# ==============================================================
import json

# pip install simplejson
import simplejson

# pip install ujson
import ujson

import pickle
import cPickle
import shelve
import marshal


# 压缩相关
# ==============================================================
import tarfile
import zipfile
import gzip
import zlib

import bz2


# http/ftp/...相关
# ==============================================================
import ftplib
import http
from http import HTTPStatus

import cgi
import ipaddress
import requests
import lassie
import urllib
import urllib2
import socket

import socketserver
from socketserver import BaseRequestHandler, UDPServer

import SimpleHTTPServer
import Cookie
import cookielib




# 数组、集合等
# ==============================================================
import array

import itertools
from itertools import accumulate, chain, product

from collections import defaultdict, OrderedDict, namedtuple



# 安全执行操作
# ==============================================================
import ast
from ast import literal_eval                 # 用于生产环境中取代`eval`
from jinja2 import escape


# 时间相关
# ==============================================================
import time
import datetime
import calendar

# pip install arrow
import arrow                                  # 便捷处理时间的库

# pip install pendulum
import pendulum                               # 可以计算给定日期过后的（年、月、日）后的具体日期



# pip install python-dateutil
import dateutil
from dateutil.parser import parse             # 强大的时间格式转换

import timeit                                 # 常用于计时


# 性能分析
# ==============================================================
import profile
import cProfile
import pstats

# pip install line_profiler                # 逐行分析代码耗时
# pip install memory_profiler              # 分析代码内存占用
# pip install coverage                     # 代码覆盖率检测


# 数据处理
# ==============================================================
import signal                                 # 信号相关

# pip install blinker
from blinker import signal

import random

# https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
import numpy
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#numexpr
import numexpr
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#numba
import numba
from numba import jit                        # 即时加速
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pandas
import pandas
from pandas import Series, DataFrame, Panel

# pip install dask
import dask                                   # 类似于spark的相似pandas接口的python包
from dask import dataframe as dd
from dask import array as da
from dask.distributed import Client
from dask import bag as db
# pip install dask-ml[complete]
# pip install dask-ml[xgboost]
# pip install dask-ml[tensorflow]



# pip install modin
import modin.pandas as pd
# pip install tablib
import tablib
from tablib import Dataset
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#statsmodels
import statstics
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
import scipy
# pip install pip install dicom
import dicom                                # 医疗数据处理包

# 多进程、多线程
# ==============================================================
import threading
from threading import Thread

import multiprocessing
from multiprocessing import Pool, Process

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

# pip install pip install gevent
import gevent
from gevent.monkey import patch_socket
from gevent.pool import Pool
patch_socket()

# pip install tomorrow
import tomorrow
from tomorrow import threads

import asyncio
import aiohttp
import asynchat


# 日志
# ==============================================================
import logging


# pip install logzero
import logzero

# pip install pysnooper
import pysnooper                                # 简单日志分析器


# 自动化测试
# ==============================================================
import nose
from unittest import TestCase


# 可视化
# ==============================================================
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.colors import cnames           # 导入颜色名字

from matplotlib import __version__, rcParams
from matplotlib._pylab_helpers import Gcf
from mpl_toolkits.mplot3d import Axes3D
import seaborn                                 # 基于matplotlib

# pip install ggplot
import ggplot

# pip install folium
import folium

# https://www.lfd.uci.edu/~gohlke/pythonlibs/#heatmap
import heatmap

# pip install missingno
import missingno                               # 查看数据缺失值（常与pandas一起用）

# pip install pygal
import pygal                                   # 绘制svg图

# pip install graphviz
# https://github.com/xflr6/graphviz
import graphviz                                # 绘制有向图等



# OCR
# ==============================================================
 # pip install baidu-aip
 from aip import AipOcr


# 金融指标及时间序列
# ==============================================================
import talib
import arch
import statsmodels
import patsy


# 机器学习、深度学习
# ==============================================================
# pip install minepy
from minepy import MINE                        # 计算相关性
import numpy as np
import numexpr
m = MINE()
x = np.random.uniform(-1, 1, 10000)
m.compute_score(x, x**2)
#print m.mic()

import pybrain
import sklearn
import imblearn                                # 机器学习中非平衡样本进行样本平衡（上采样、下采样等）

# pip install heampy
import heamy                                   # 用于融合模型（与sklearn联合使用）

# pip install lightgbm
import lightgbm

import xgboost

# pip install scikit-surprise
import surprise                                # 一个强化sklearn的包

import theano
import tensorflow as tf
import torch
# pip install visdom
from visdom import Visdom                      # pytorch 可视化工具

import keras

# Autograd can automatically differentiate native Python and Numpy code
# pip install autograd
import autograd.numpy as np
from autograd import grad

# pip install hyperopt   
import hyperopt                                # 用来机器学习/深度学习调参（优于RandomSearch,快于GridSearch)


# NLP（自然语言处理）
# ==============================================================
# pip install nltk
import nltk

# pip install gensim
import gensim

# pip install jieba
import jieba

# pip install snownlp
import snownlp

# pip install xpinyin
import xpinyin

# pip install pypinyin
import pypinyin


# 邮件
# ==============================================================
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import formatdate
from email import encoders
from smtplib import SMTP_SSL


# token 令牌等
# ==============================================================
import uuid
import hmac
import hashlib
import shortuuid
import secrets
import ssl

import getpass

# pip install bcrypt
import bcrypt                                # 用于密码加密

from cryptography.utils import int_from_bytes, int_to_bytes

from hashlib import md5, sha1, sha224, sha256, sha384, sha512


# 数据结构
# ==============================================================
from queue import PriorityQueue, LifoQueue


# 数据库
# ==============================================================
# pip install stomp.py
import stomp                                # MQ

import sqlite3
import pymongo
import pymysql
import psycopg2
import redis
import cx_Oracle as oracle

# pip install SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# pip install influxdb
from influxdb import InfluxDBClient        # 时序数据库

# pip install elasticsearch
import elasticsearch
from elasticsearch import helpers          # helpers.bulk(...) 批量插入
from elasticsearch.serializer import JSONSerializer
from elasticsearch.exceptions import NotFoundError, RequestError, TransportError

# pip install Whoosh
from whoosh import fields
from whoosh import index
from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED

# pip install pylibmc
import pylibmc                              # for Memcache

# pip install diskcache                     # SQLite和文件支持的缓存后端，具有比memcached和redis更快的查找功能.
import diskcache

# 支持mysql命令行提示
# pip install -U mycli
# https://github.com/dbcli/mycli

# pip install sqlparse
import sqlparse                             # 非验证式解析sql语句
import anydbm                               # python2
import whichdb                              # python2
import dbm                                  # pyhton3

# pip install python3-memcached
import memcache

# Web框架
# ==============================================================
import flask
from flask import Flask, request

# pip install pipenv                         # 用来创建虚拟环境
# pip install python-dotenv                  # 用来设置环境变量
# ------------
from flask_ckeditor import CKEditor, upload_success, upload_fail
from flask_dropzone import Dropzone
from flask_wtf.csrf import validate_csrf
from wtforms import ValidatoionError
# pip install flask_socketio                 # 用于websockets，由服务端通知(触发)客户端数据的更新
from flask_socketio import SocketIO, emit, send
# ------------

import django

import apistar

import bottle

import diesel

import tornado


# 抽象
# ==============================================================
import abc
from abc import abstractmethod

# 面向对象（实现别的语言的interface）
""" 接口在编程语言中指的是一个抽象类型，是抽象方法的集合，特点如下：
1、类通过继承接口的方式，来继承接口的抽象方法
2、接口并不是类（睢冉编写类和接口的方式很相似）
3、类描述对象的属性和方法（实现接口的类，必须实现接口内所描述的所有方法，否则必须声明为抽象类）
4、接口包含类要实现的方法（接口无法被实例化，但可以被实现）
总结：接口只定义规范，不负责具体实现（具体实现由具体的实现者完成）
"""
from zope.interface import Interface
from zope.interface.declarations import implementer


# git
# ==============================================================
# pip install GitPython
import git


# sklearn
# ==============================================================
# 处理缺失，数据扩展
from sklearn.preprocessing import Imputer, PolynomialFeatures
# 预处理
from sklearn.preprocessing import label_binarize, OneHotEncoder
# 向量化
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.feature_extraction import DictVectorizer
# sklearn 中有关降维
from sklearn.manifold import TSNE, Isomap, MDS
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
# 聚类
from sklearn.mixture import GMM

#----
from sklearn import random_projection
model = random_projection.SparseRandomProjection(n_components=2)
model.fit_transform(...)
#---
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis  #LDA
model = LinearDiscriminantAnalysis(n_components=2)
#---

# sklearn中特征选择
#---
from sklearn.feature_selection import chi2, SelectKBest
new_features = SelectKBest(chi2, k=2).fit_transform(old_x, y)
#---
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
estimator = LogisticRegression()
model = RFE(estimator, n_features_to_select=2).fit_transform(...)
#---
from sklearn.linear_model import RandomizedLogisticRegression
model = RandomizedLogisticRegression().fit(ix, iy)
#---
# 验证学习曲线，参数
from sklearn.model_selection import learning_curve, validation_curve

from sklearn import datasets
mnist = datasets.fetch_mldata('MNIST original')
x, y = mnist.data, mnist.target

#基于树模型
from sklearn.datasets import load_iris

iris = load_iris()
ix, iy = iris.data, iris.target
from sklearn.ensemble import ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.feature_selection import SelectFromModel

model1 = ExtraTreesClassifier()
model2 = GradientBoostingClassifier()
model1.fit(ix, iy)
model2.fit(ix, iy)
model1.feature_importances_
model2.feature_importances_
clf1 = SelectFromModel(model1, prefit=True)
clf2 = SelectFromModel(model2, prefit=True)
clf1.get_support()
clf2.get_support()

#---
# sklearn 交叉验证
from sklearn.cross_validation import cross_val_score
#cross_val_score(model, X, y, cv=10)
from sklearn.cross_validation import cross_val_predict
#cross_val_predict(model, X, y, cv=10)
from sklearn.cross_validation import LeaveOneOut
#scores = cross_val_score(model, X, y, cv=LeaveOneOut(len(X)))

# ---
from sklearn.pipeline import Pipeline, make_pipeline


# IPython
# ==============================================================
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'  #全部显示（不需要print）

from IPython import display
from IPython.display import Image

%matplotlib inline   #用于Jupyter notebook下显示matplotlib绘图
%matplotlib notebook  #同上，不过显示后的图像可以手动调整（执行拖动、保存等操作）


# 时区(国际化支持)
# ==============================================================
import locale
import pytz
import gettext


# 其他（待分类）
# ==============================================================
import distutils
import atexit
import ssl
import chunk
import compileall
import param
import binascii
import dis                   # 查看代码的编译
import parser                # python 内部解析器
import errno
import jdcal

# pip install astor
import astor                 # astor is designed to allow easy manipulation of Python source via the AST.

# pip install mmh3
import mmh3

from multiplesingdisisis import Dispatcher

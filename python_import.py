
# 系统操作
import os
import sys
#sys.modules.get(k, [d])
import platform  # 可以查看终端信息（如版本状况）
import psutil  # 查看内存占用情况
import inspect
import operator
# from operator import mathodcaller
import path
import traceback
import trace
import glob  # 对文件进行查找
# 跟glob比较像，不过可以用(fnmatch.fnmatch(file,
# pattern),fnmatch.fnmatchcase(file,pattern)一个大小写敏感一个则不）
import fnmatch
import linecache  # 读取任意文件的指定行  linecache.getline(file,line_number)
import filecmp  # 对文件或文件夹进行比较
import imp  # 里面有reload些啥
import fileinput   #有点像是input
import importlib  # 实现动态引入模块  #math = importlib.import_module('math')
import atexit  # 一个蛮有意思的内置模块，执行函数退出时的回调函数，先进后出
import ssl


# 包管理
import pkgutil

# pkgutil.get_importer(path_item)
# pkgutil.get_data(package, resource)


# 好用的工具
# pip install pdir2
import pdir  # dir的扩展
import tqdm  # 一个显示进度的小工具（bar）
import fake #- useragent  # 自动生成伪装header等信息
import faker  # 生成虚假信息，（可生成中文）
import mimesis  # pip install mimesis 生成虚假信息（可生成中文）
import xpinyin  #将汉字转换为拼音（甚至可以加声调） #pip install xpinyin
import pypinyin #汉字转换成拼音 #pip install pypinyin

# 错误忽略等
import retrying  # pip install retrying
# from retrying import retry   #忽略错误直到出现对的，这个很有用

# 图像识别
import cv2  # openCV
import imghdr  # 识别图像格式
import PIL

# 匹配
import fuzzywuzzy  # 字符串模糊匹配  pip install fuzzywuzzy
import pangu  # 分词处理 pip install pangu

# pip install pyfiglet
# cmd使用，pyfiglet + 字母，显示为趣味文字

# 算法及排序
import sortedcontainers  # pip install sortedcontainers
import bisect
import heapq #堆排序
import compiler   #from compiler.ast import flatten 可以将镶嵌列表展开，py3已舍弃该包
from funcy import flatten, isa  #pip install funcy


#缓存
from functools import lru_cache   #python3.2以后支持，一个用于缓存给定大小（可设置）的装饰器

# 一些格式
import string
import pprint
import textwrap   #可以修饰字符串输出格式
import fileinput
import weakref  #弱引用

import uniout  # 中文格式显示等，pip install uniout
import xpinyin  # 将汉字转换为拼音  # https://github.com/lxneng/xpinyin/

import readline
import pep8
import Queue
import decorator
import difflib
import struct
import this
import new
import keyword
import colorams  # 改变输出流背景、颜色等
import ctypes
import configparser   #python3读取配置

#特殊的split格式
import shlex

#动态导包
import importlib
from importlib import import_module

# ---------------------------------
import sys
# sys.modules[MODULE_NAME]
# __import__(MODULE_NAME)
# ---------------------------------


# 编码及解析
import encodings # help(encodings) 关于所有Python内置编码方式
import chardet  # 检查编码
import mimetypes  #检测文件MIME类型
import code
import codecs  # 与open一起使用，可以指定解码方式
from reprlib import repr
import typing

#+++++++++++++++++编码问题
from unicodedata import normalize, name
#+++++++++++++++++

import copy
import cPickle  # pickle的C版本，更快更好用
import csv
import xlrd  # 用于处理excel的库
import xlwt  # 用于处理excel的写操作
import encodings
import shutil  # 文件整体复制等操作
import base64
import hmac
import dis  # 查看代码的编译
import io
import temfile  #创建临时文件，关闭即销毁
import shelve  #存入存出操作，数据库

import json
import pickle
import shelve
import marshal

import re
# flashtext 是一个起到re作用的第三方包，针对大文件执行速度更快！
import flashtext #pip install flashtext


import tarfile  # 解压压缩包
import zipfile
import gzip
import zlib  # 压缩，py2.7支持str，py3必须转换为bytes后才可用
import parser
import bz2

import StringIO  #这两个python3已删除，可以通过io.StringIO来调用
import cStringIO

import ftplib
import binascii

import array


#py3
import builtins   #一些内置的range，map，zip等在该包中，可通过引用该包进行覆盖定义

#安全
import ast
from ast import liter_eval #比eval更安全，只执行一些安全的操作

#本地化
import locale

#命令行可使用
import optparse   #脚本使用增加参数

# 内置工具箱
import collections  # 一些内置如OrderDict，defaultdict等
import functools  # partial、wraps等
import itertools

import types
import typing
#from types import MappingProxyType
import errno

# 对时间的操作
import datetime
import dateutil  # 强大的时间格式转换
import time
import timeit  # 计时用
import calendar
import arrow  # pip install arrow  一个便捷处理时间的第三方库

# 控制异常输出
import warnings  # 结合filterwarnings('ignore')使用，专治强迫症
import tqdm  # 查看进度

# 数据处理
import signal
import random
import numbers
import nose
import hashlib
import math  #不支持负数的开方
import cdemical
import cmath  #支持负数的开方
import decimal
import fractions
import numpy
import numexpr
import numba
import numpy as np
import pandas
import pandas as pd
import scipy
import scipy as sp
import tablib  # pip install tablib 类似于pandas中dataframe格式
import dicom  # 医疗数据处理包
import statistics  # py3 一些处理中位数等数据统计包


#计算相关性
from minepy import MINE
import numpy as np
import numexpr
m = MINE()
x = np.random.uniform(-1, 1, 10000)
m.compute_score(x, x**2)
#print m.mic()


# 线程
import threading
import subprocess
import multiprocessing
import gevent  # 协成
import tomorrow  #pip install tomorrow, @thread(10) 一个30行的多线程代码修饰，灰常好用


# 日志记录
import logging
import logzero # pip install -U logzero 一个第三方包，记录日志

# 监控运行内存等
import pympler

# 垃圾回收
import gc


#事件调度
import sched

# 可视化
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn  # 基于matplotlib的一个美化
import folium  # 用于对地图可视化  pip install folium
import heatmap  # 热力图
import missingno  # pip install missingno 用来查看数据缺失值，与pandas一起用作数据分析，奇效
import pygal  # pip install pygal 可以用来画svg图，在浏览器中查看

# 图形化
import PIL
import cv2  # openCV
import SimpleITK as sitk  # 图像处理
import skimage

# 爬虫
#import fake - useragent  # pip install fake-useragent  生成伪装头部等信息
import requests
import grequests  # pip install grequests 一个利用gevent实现多线程的requests
import lassie
import tushare
import base64  # 编码
import urlparse
import xml
import furl  # pip install furl 处理url的库

# 金融指标以及时间序列
import talib
import arch
import statsmodels

# 机器学习及神经网络
import pybrain
import sklearn
import surprise  # pip install scikit-surprise, 一个强化sklearn的包
import theano  # 一个基于Cpython的数学处理包
import tensorflow as tf


# http交互
import http
# from http import HTTPStatus
import cgi
import ipaddress
import requests
import lassie  # pip install lassie 抓取网页，操作简单
import cgi  # 通用网关接口
import bs4
import urllib
import urllib2
import socket
import socketserver
# from socketserver import BaseRequestHandler, UDPServer
import SimpleHTTPserver
import contextlib2
import Cookie
import cookielib
import email
import htmllib
import HTMLParser
import httplib
import io
import lxml
import selenium
import webbrowser #打开指定web页面
import html

# token令牌等
import uuid
import hmac
import hashlib
import shortuuid  # pip install shortuuid #https://github.com/skorokithakis/shortuuid
import secrets  # py3 生成
import ssl

from types import MappingProxyType  #字典代理


from queue import PriorityQueue, LifoQueue


import secrets  # py3 生成密令等

# 密码
import getpass

# 单元测试
import unittest

# 数据库
import sqlite3
import pymongo
import pymysql
import redis
#python 2
import anydbm  #python2可用  value和key必须是字符串，其中value可为空
#python 3
import dbm
import whichdb  #python2可用


# 网络框架
import flask
from flask import Flask, request

# 抽象定义
import abc

# ---
# 处理缺失，数据扩展
from sklearn.preprocessing import Imputer, PolynomialFeatures


# ---
# 向量化
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.feature_extraction import DictVectorizer

# ---
from sklearn.preprocessing import label_binarize, OneHotEncoder


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


#IPython
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'  #全部显示（不需要print）

from IPython import display
from IPython.display import Image

import future_builtins
reload(sys)
sys.setdefaultencoding('utf-8')

warnings.filterwarnings('ignore')

from abc import abstractmethod
from abc import ABCMeta
import imp

from bs4 import BeautifulSoup as bs

from chardet.universaldetector import UniversalDetector

from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import namedtuple
from collections import ChainMap

from copy import deepcopy

from datetime import datetime
from datetime import timedelta


from dateutil.parser import parse

#__future__ 导入时必须放在最开始，否则会报错（这里只是做收集用，不要运行）
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from functools import partial
from functools import wraps
from itertools import (chain,
                       compress,
                       count,
                       cycle,
                       dropwhile,
                       ifilter,
                       ifilterfalse,
                       imap,
                       islice,  #可用于迭代器的切片
                       imap,
                       izip,
                       izip_longest,
                       permutations,
                       product,
                       repeat,
                       starmap,
                       takewhile)
from io import BytesIO
from inspect import signature

from matplotlib import pyplot as plt
from matplotlib.colors import cnames  # 导入颜色名字

from matplotlib import __version__, rcParams
from matplotlib._pylab_helpers import Gcf
from matplotlib.backend_bases import (RendererBase, GraphicsContextBase,
                                      FigureManagerBase, FigureCanvasBase)
from matplotlib.backends.backend_mixed import MixedModeRenderer
from matplotlib.cbook import (Bunch, is_string_like, get_realpath_and_stat,
                              is_writable_file_like, maxdict)
from matplotlib.figure import Figure
from matplotlib.font_manager import findfont, is_opentype_cff_font, get_font
from matplotlib.afm import AFM
import matplotlib.type1font as type1font
import matplotlib.dviread as dviread
from matplotlib.ft2font import (FIXED_WIDTH, ITALIC, LOAD_NO_SCALE,
                                LOAD_NO_HINTING, KERNING_UNFITTED)
from matplotlib.mathtext import MathTextParser
from matplotlib.transforms import Affine2D, BboxBase
from matplotlib.path import Path
from matplotlib import _path
from matplotlib import _png
from matplotlib import ttconv

from math import ceil, cos, floor, pi, sin

from multiprocessing import Process, Pool

from numpy import random
from numpy import polyfit, std, subtract, sqrt, log


from pandas import Series, DataFrame

from PIL import Image

from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import (FeedForwardNetwork,
                               LinearLayer, SigmoidLayer,
                               TanhLayer, SoftmaxLayer,
                               FullConnection)

from pybrain.supervied.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader


from pymongo import MongoClient

from pympler import asizeof
from pympler import tracker

from scipy.linalg import linalg
from scipy.misc import derivative  # 求导数
from scipy import stats
from scipy.stats import pearsonr  #皮尔森系数，可以用来检测线性相关
from scipy.stats import entropy #计算乡农熵


from sklearn.datasets import load_digits
from sklearn.datasets import load_iris
from sklearn.datasets import load_boston


from sklearn.cross_validation import KFold

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
from sklearn.linear_model import ARDRegression
from sklearn.linear_model import ElasticNet, ElasticNetCV
from sklearn.linear_model import Lasso, LassoCV
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import LassoLars, LassoLarsCV, LassoLarsIC
from sklearn.linear_model import MultiTaskElasticNet, MultiTaskElasticNetCV
from sklearn.linear_model import MultiTaskLasso, MultiTaskLassoCV
from sklearn.linear_model import OrthogonalMatchingPursuit, OrthogonalMatchingPursuitCV
from sklearn.linear_model import Ridge, Lasso
from sklearn.linear_model import Hinge

from sklearn.svm import SVC, SVR, LinearSVC, LinearSVR, libsvm

from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import TimeSeriesSplit

from sklearn.naive_bayes import GaussianNB, BaseNB, MultinomialNB

from sklearn.cluster import KMeans

from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

from sklearn.neighbors import (KDTree,
                               KNeighborsClassifier,
                               KNeighborsRegressor,
                               RadiusNeighborsClassifier,
                               RadiusNeighborsRegressor)

from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
from sklearn.ensemble import bagging, BaggingClassifier, BaseEnsemble
from sklearn.ensemble import ExtraTreesClassifier, ExtraTreesRegressor
from sklearn.ensemble import gradient_boosting, GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, RandomTreesEmbedding
from sklearn.ensemble import voting_classifier, VotingClassifier

from sklearn.preprocessing import (MaxAbsScaler,
                                   MinMaxScaler,
                                   normalize,
                                   PolynomialFeatures)
from sklearn.preprocessing import StandardScaler, scale

from sklearn.grid_search import RandomizedSearchCV, GridSearchCV

from sklearn.decomposition import PCA

from sklearn.externals import joblib

from sklearn.preprocessing import MinMaxScaler

from statistics import mean, median, mode
from statistics import variance, stdev  # 样本方差，样本标准差
from statistics import pvariance, pstdev  # 总体方差，总体标准差

from statsmodels import api as sm
from statsmodels.graphics.api import qqplot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARMA, ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, acf, pacf

from traceback import print_exc, format_exc

from threading import Thread

from tqdm import tqdm
from tqdm import trange

from urlparse import urlparse

from xml.etree.ElementTree import parse #解析xml

from xpinyin import Pinyin
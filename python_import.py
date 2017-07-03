
# 系统操作
import os
import sys
import platform  # 可以查看终端信息（如版本状况）
import psutil  # 查看内存占用情况
import inspect
import operator
import path
import traceback
import glob # 对文件进行查找
import fnmatch  #跟glob比较像，不过可以用(fnmatch.fnmatch(file, pattern),fnmatch.fnmatchcase(file,pattern)一个大小写敏感一个则不）
import linecache   #读取任意文件的指定行  linecache.getline(file,line_number)
import imp   #里面有reload些啥
import importlib   #实现动态引入模块

#好用的工具
#pip install pdir2
import pdir  #dir的扩展
import tqdm #一个显示进度的小工具（bar）
import fake-useragent  #自动生成伪装header等信息

#错误忽略等
import retrying  # pip install retrying
#from retrying import retry   #忽略错误直到出现对的，这个很有用


#一些格式
import string
import pprint
import readline
import pep8
import Queue
import decorator
import difflib
import struct
import this
import new
import keyword
import colorams  #改变输出流背景、颜色等


# 编码及解析
import chardet  #检查编码
import code
import codecs   #与open一起使用，可以指定解码方式
import copy
import cPickle #pickle的C版本，更快更好用
import csv
import encodings
import shutil  #文件整体复制等操作
import base64

import json
import pickle
import re
import tarfile  #解压压缩包
import zipfile
import gzip
import zlib   #压缩，py2.7支持str，py3必须转换为bytes后才可用
import parser
import StringIO
import cStringIO
import ftplib




# 内置工具箱
import collections  #一些内置如OrderDict，defaultdict等
import functools    #partial、wraps等
import itertools

import types
import errno

# 对时间的操作
import datetime
import dateutil  #强大的时间格式转换
import time
import timeit  #计时用
import calendar

# 控制异常输出
import warnings  #结合filterwarnings('ignore')使用，专治强迫症
import tqdm  # 查看进度

# 数据处理
import signal
import random
import numbers
import nose
import hashlib
import math
import cdemical
import cmath
import decimal
import fractions
import numpy
import numpy as np
import pandas
import pandas as pd
import scipy
import scipy as sp
import dicom  #医疗数据处理包


# 线程
import threading
import subprocess
import gevent  #协成


# 日志记录
import logging

#垃圾回收
import gc

# 数据库操作
import pymongo


# 可视化
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 图形化
import PIL
import cv2  # openCV
import SimpleITK as sitk   #图像处理
import skimage  

#爬虫
import fake-useragent # pip install fake-useragent  生成伪装头部等信息
import requests
import base64   #编码
import urlparse

# 金融指标以及时间序列
import talib
import arch
import statsmodels

# 机器学习及神经网络
import pybrain
import sklearn
import theano   #一个基于Cpython的数学处理包
import tensorflow as tf


# http交互
import requests
import cgi  # 通用网关接口
import bs4
import urllib
import urllib2
import socket
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

# token令牌等
import uuid
import hmac
import hashlib

# 单元测试
import unittest

# 数据库
import sqlite3
import pymongo


import future_builtins
reload(sys)
sys.setdefaultencoding('utf-8')

warnings.filterwarnings('ignore')

from bs4 import BeautifulSoup as bs

from chardet.universaldetector import UniversalDetector

from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import deque

from copy import deepcopy

from datetime import datetime
from datetime import timedelta


from dateutil.parser import parse

from __future__ import division

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
                       islice,
                       imap,
                       izip,
                       izip_longest,
                       permutations,
                       product,
                       repeat,
                       starmap,
                       takewhile)

from matplotlib import pyplot as plt

from numpy import random
from numpy import polyfit, std, subtract, sqrt, log


from pandas import Series, DataFrame

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

from scipy.linalg import linalg
from scipy.misc import derivative  # 求导数
from scipy import stats

from sklearn.datasets import load_digits
from sklearn.datasets import load_iris
from sklearn.datasetsi import load_boston


from sklearn.cross_validation import KFold

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.linear_model import Ridge, Lasso
from sklearn.linear_model import Hinge

from sklearn.svm import SVC, SVR, LinearSVC, LinearSVR, libsvm

from sklearn.naive_bayes import GaussianNB, BaseNB

from sklearn.cluster import KMeans

from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

from sklearn.neighbors import KDTree,
    KNeighborsClassifier, KNeighborsRegressor,
    RadiusNeighborsClassifier, RadiusNeighborsRegressor

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

from statsmodels import api as sm
from statsmodels.graphics.api import qqplot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARMA, ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, acf, pacf


from threading import Thread

from tqdm import tqdm
from tqdm import trange

from urlparse import urlparse

import os
import sys
import platform  # 可以查看终端信息（如版本状况）
import re
import codecs  # 读取文件时解决编码问题
import tarfile
import pickle
import cPickle
import functools
import datetime
import time
import collections
import dateutil  # 用来解析时间
import itertools
import warnings
import copy
import random
import csv
import math
import threading
import logging

import pymongo

import chardet
import numpy
import numpy as np
import pandas
import pandas as pd
import scipy
import scipy as sp
import matplotlib.pyplot as plt
import talib
import pybrain
import sklearn
import arch
import statsmodels

import tqdm
import psutil #查看内存占用情况

import request
import bs4
import urllib


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
import os
import sys
import platform
import re
import codecs
import tarfile
import pickle
import cPickle
import functools
import datetime
import time
import collections
import dateutil
import itertools
import warnings
import copy
import random
import csv
import math

import pymongo

from pymongo import MongoClient

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
import statsmodels


warnings.filterwarnings('ignore')


from __future__ import division

from copy import deepcopy

from matplotlib import pyplot as plt

from numpy import random
from numpy import polyfit, std, subtract, sqrt, log

from scipy.misc import derivative  #求导数

from pandas import Series, DataFrame

from functools import partial
from functools import wraps

from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import deque

from datetime import datetime
from datetime import timedelta


from dateutil.parser import parse

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


from statsmodels.tsa.arima_model import ARMA, ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf



from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, TanhLayer, SoftmaxLayer, FullConnection
from pybrain.supervied.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib



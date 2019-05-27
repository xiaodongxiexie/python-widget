#coding: utf-8


import numpy as np 
from scipy.stats import pearsonr

np.random.seed(0)
size = 300

x = np.random.normal(0, 1, size)
print 'Lower noise', pearsonr(x, x+np.random.normal(0,1, size))
print 'Higher noise', pearsonr(x, x + np.random.normal(0,10,size))

x = np.random.uniform(-1,1,100000)
print pearsonr(x, x**2)

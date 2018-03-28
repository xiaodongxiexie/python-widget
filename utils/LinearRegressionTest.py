#coding: utf-8

from sklearn.linear_model import LinearRegression
import numpy as np 
import warnings

warnings.filterwarnings('ignore')


np.random.seed(0)
size = 5000

X = np.random.normal(0, 1, (size, 3))
Y = X[:, 0] + 2 * X[:, 1] + np.random.normal(0,2,size)

lr = LinearRegression()
lr.fit(X, Y)

def pretty_print_linear(coefs, names=None, sort=False):
	if names == None:
		names = ['X%s' % x for x in range(len(coefs))]
	lst = zip(coefs, names)
	if sort:
		lst = sorted(lst, key=lambda x: -np.abs(x[0]))
	return ' + '.join('%s * %s' % (round(coef, 3), name) for coef, name in lst)

print 'Linear model:', pretty_print_linear(lr.coef_)

# for attr in dir(lr):
# 	if not attr.startswith('_'):
# 		if type(eval('lr.%s' % attr)) !='instancemethod':
# 			print attr, ' ' , eval('lr.%s' % attr)

size = 100
np.random.seed(seed=5)

X_seed = np.random.normal(0,1,size)

X1 = X_seed + np.random.normal(0,.1,size)
X2 = X_seed + np.random.normal(0,.1,size)
X3 = X_seed + np.random.normal(0,.1,size)

Y = X1 + X2 + X3 + np.random.normal(0, 1, size)
X = np.array([X1, X2, X3]).T

lr = LinearRegression()
lr.fit(X, Y)
print 'Linear model: ', pretty_print_linear(lr.coef_)


from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_boston

boston = load_boston()
scaler = StandardScaler()
X = scaler.fit_transform(boston['data'])
Y = boston.target 
names = boston.feature_names

lasso = Lasso(alpha=.3)
lasso.fit(X,Y)
print 'Lasso model: ', pretty_print_linear(lasso.coef_, names, sort=True)

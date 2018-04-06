import glob
import os, math, array, re

import numpy as np
import pandas as pd

import pandas as pd, numpy as np

import tqdm
import SimpleITK as sitk
import scipy.ndimage

from matplotlib import pyplot as plt
from matplotlib.colors import cnames
from mpl_toolkits.mplot3d import Axes3D

from pandas import Series, DataFrame

#%matplotlib inline



def resample(image, old_spacing, new_spacing=[1,1,1]):
    resize_factor = old_spacing / new_spacing
    new_real_shape = image.shape * resize_factor
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / image.shape
    new_spacing = old_spacing / real_resize_factor
    image = scipy.ndimage.interpolation.zoom(image, real_resize_factor, mode='nearest')
    return image, new_spacing  


addre_list = []
test_path = []

for addre in pd.read_csv(glob.glob('data/csv/train/*')[0]).ix[:, 0]:
    if addre in map(lambda x: os.path.split(x)[1][:10], glob.glob('data/train_set/*mhd')):
        addre_list.append(addre)  

for x in glob.glob('data/train_set/*mhd'):
    if os.path.split(x)[1][:10] in addre_list:
        test_path.append(x)
        
        
for path in tqdm.tqdm(set(sorted(test_path))):
    image_ = sitk.ReadImage(path)
    image_arr_ = sitk.GetArrayFromImage(image_)
    image_resample_, new_spacing = resample(image_arr_, np.array(image_.GetSpacing())[::-1]) #z,y,x需要转换
    with open('lxd/new_spacing.txt', 'a+') as f:
        f.write(path+': ')
        f.write(str(new_spacing))
        f.write('\n')
    save_path = 'lxd/%s.npy' % os.path.split(path)[1][:-4]

    np.save(save_path,image_resample_)

with open('lxd/new_spacing.txt', 'a+') as f:
    d = f.readlines()
    
ser = Series()
for i in d[5:]:
    trans = map(lambda x: float(x), re.findall('(\d\.\d*)', i.split(':')[-1].strip()[1:-1]))
    ser = ser.append(Series([trans], index=[i.split(':')[0]]))
    
    
ls_all_path = set(test_path)
data_anno = pd.read_csv(glob.glob('data/csv/train/*')[0])

    
ser_nodule_loc = Series()  #记录节点位置

for path in tqdm.tqdm(ls_all_path):
    if path in ser.index: 
        flag = os.path.split(path)[-1][:-4]
        
        new_image = np.load('lxd/%s.npy'%flag)
        new_spacing = ser[path]
        old_origin = sitk.ReadImage(path).GetOrigin()[::-1]
        
        current_data = data_anno[data_anno.seriesuid==os.path.split(path)[1][:-4]]
        
        for i in range(len(current_data)):
            data00 = current_data[i:i+1]
            nodule_center = data00.ix[:, 1:4].values[0][::-1]
            v_center = np.rint((nodule_center-old_origin)/new_spacing)
            v_center = np.array(v_center, dtype=int)
            ser_nodule_loc = ser_nodule_loc.append(Series([v_center], index=[path]))
print "DONE!"
ser_nodule_loc.to_csv('lxd/ser_nodule_loc.csv')


from collections import defaultdict

segment_dict = defaultdict(list)  #用来将每个三维立体切分为指定小块状并保存
labels = []  #用来保存每个切割的小块状label

for path in tqdm.tqdm(glob.glob('lxd/*.npy')):
    if 'data/train_set/%s.mhd'%os.path.split(path)[1][:-4] in ser_nodule_loc.index:
        arr_test = np.load(path)
        label_loc = ser_nodule_loc['data/train_set/%s.mhd'%os.path.split(path)[1][:-4]].values
        
        z, y, x = arr_test.shape
        
        if iterable(label_loc[0]):
            for i in range(40,z,40):
                for j in range(46,y,46):
                    for k in range(46,x,46):
                        segment_dict[os.path.split(path)[1][:-4]].append(arr_test[i-40:i, j-46:j,k-46:k])
                        
                        for loc in label_loc:
                            if (loc[0] in range(i-40,i)) and (loc[1] in range(j-46,j)) and (loc[2] in range(k-46,k)):
                                labels.append(1)
                                break
                        else:
                            labels.append(0)
        else:
            for i in range(40,z,40):
                for j in range(46,y,46):
                    for k in range(46,x,46):
                        segment_dict[os.path.split(path)[1][:-4]].append(arr_test[i-40:i, j-46:j,k-46:k])
                        if (label_loc[0] in range(i-40,i)) and (label_loc[1] in range(j-46,j)) and (label_loc[2] in range(k-46,k)):
                            labels.append(1)
                        else:
                            labels.append(0)    
                            
                            
def package(i=0, length=6, equal=False,name='001'):
    all_arr = np.zeros(84640)[None, :]
    all_label = np.zeros(1)[None, :]
    
    for value in tqdm.tqdm(segment_dict.values()[i:length+i]):
        per_arr = np.array([])
        per_label = np.array([])
        for per, label in zip(value,labels):
            per_arr = np.r_[per_arr,per.ravel()]
            per_label = np.r_[per_label, label]
        per_arr = per_arr.reshape([len(value), -1])
        per_label = per_label[:, None]
        
        all_arr = np.r_[all_arr, per_arr]
        all_label = np.r_[all_label, per_label]
        
        if equal:  #此处用于将长度全部调整为最大长度
            if per_arr.shape[0] < 800:
                arr_toAdd = np.zeros((800-per_arr.shape[0], 84640))
                label_toAdd = np.zeros((800-per_arr.shape[0],1))
            per_arr = np.r_[per_arr, arr_toAdd]
            per_label = np.r_[per_label, label_toAdd]  
    all_arr = np.delete(all_arr, 0, axis=0)
    all_label = np.delete(all_label, 0, axis=0)
    if not os.path.exists('lxd/tmp'):
        os.mkdir('lxd/tmp')
    np.save('lxd/tmp/tmp_feature%s.npy'%name, all_arr)
    np.save('lxd/tmp/tmp_label%s.npy'%name, all_label)
    
    
    
need = np.zeros(84640)[None, :]
for x, y in zip(sorted(glob.glob('lxd/tmp/tmp_feature*')), sorted(glob.glob('lxd/tmp/tmp_label*'))):
    need =  np.append(need, np.load(x)[list(np.where(np.load(y)==1)[0])], axis=0)
    
all_label_is_1 = np.delete(need, 0, axis=0)

test_arr = np.load('lxd/tmp/tmp_feature001.npy')
test_label = np.load('lxd/tmp/tmp_label001.npy')

test_arr2 = np.r_[test_arr, all_label_is_1]
test_label2 = np.r_[test_label, np.ones(all_label_is_1.shape[0])[:, None]]

trn_data  = test_arr2
trn_label = pd.get_dummies(Series(test_label2.ravel()))

trn_all = np.c_[trn_data, trn_label]



import tensorflow as tf

tf.reset_default_graph()

x = tf.placeholder(tf.float32, shape=[None,84640])
y = tf.placeholder(tf.float32, shape=[None, 2])

W = tf.Variable(tf.truncated_normal(shape=[84640, 2]))
b = tf.Variable(tf.truncated_normal(shape=[2]))

y_predict = tf.nn.softmax(tf.matmul(x, W) + b)
loss = tf.reduce_mean(tf.square(y-y_predict))

train_step = tf.train.AdamOptimizer(0.025).minimize(loss)

init = tf.global_variables_initializer()
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(init)    
    for i in range(100000):
        xx = np.random.permutation(trn_all)[:75]
        current_loss = sess.run(train_step, feed_dict={x: xx[:, :-2], y:xx[:, -2:]})
        show_loss = sess.run(loss, feed_dict={x: xx[:, :-2], y: xx[:, -2:]})
        if i % 2000 == 0:
            print 'Iter %05d: ' % i, 'Loss: ', show_loss
    total_loss = sess.run(train_step, feed_dict={x: trn_all[:, :-2], y: trn_all[:, -2:]})
    show_total_loss = sess.run(loss, feed_dict={x: trn_all[:, :-2], y: trn_all[:, -2:]})
    if not os.path.exists('lxd/model'):
        os.mkdir('lxd/model')
    saver_path = saver.save(sess, "lxd/model/model.ckpt")
    print '\n Total Loss: ', show_total_loss
print "Done!"


saver = tf.train.Saver()
i =0
ii = 0
with tf.Session() as sess:
    saver.restore(sess, "lxd/model/model.ckpt")
    accuracy = sess.run(tf.losses.absolute_difference(y_predict, trn_all[:, -2:]), feed_dict={x: trn_all[:, :-2]})
    print u'预测召回率： ', accuracy

    
    for index, (xx,yy) in enumerate(zip(trn_all[:, :-2], trn_all[:, -2:])):
        pre = sess.run(y_predict, feed_dict={x:xx[None, :]})

        if pre[0][1] == 1:
            i += 1
            if yy[1] == 1:
                ii +=1 

        #print sess.run(tf.matmul(x, W) + b, feed_dict={x: xx[None, :]})
        #if index > 200:
            #break
print u'预测结点次数：', i
print u'实际是结点次数：', ii
print u'实际测试集中共有结点个数： ', Series(trn_all[:, -2:][:, 1]).value_counts().get(1.0, 0)
print u'结点预测准确率: ', float(ii)/Series(trn_all[:, -2:][:, 1]).value_counts().get(1.0, 0) 


def val_package(i=0, length=5, name='001'):
    all_arr = np.zeros(84640)[None, :]
    
    for value in tqdm.tqdm(val_segment_dict.values()[i:length+i]):
        per_arr = np.array([])
        
        for per in value:
            per_arr = np.r_[per_arr,per.ravel()]

        per_arr = per_arr.reshape([len(value), -1])
        
        all_arr = np.r_[all_arr, per_arr]

    all_arr = np.delete(all_arr, 0, axis=0)
    
    if not os.path.exists('lxd/tmp/val'):
        os.mkdir('lxd/tmp/val')
    np.save('lxd/tmp/val/tmp_feature%s.npy'%name, all_arr)
    
    
for i in range(0, 40,5):
    val_package(i=i,length=5, name='00%s'%(i/5))
    
    
class ProcessFlow:
    
    def __init__(self,all_path, start, end): 
        self.all_path = all_path
        self.start = start
        self.end = end

    
    def predict(self):
        for index, npy in enumerate(self.all_path):# 为了输出统一，暂时列表每次放第一个并return
            arr = np.load(npy)
            
            import tensorflow as tf
        
            tf.reset_default_graph()    
            x = tf.placeholder(tf.float32, shape=[None,84640])
            y = tf.placeholder(tf.float32, shape=[None, 2])
            
            W = tf.Variable(tf.truncated_normal(shape=[84640, 2]))
            b = tf.Variable(tf.truncated_normal(shape=[2]))
            
            y_predict = tf.nn.softmax(tf.matmul(x, W) + b)
            
            saver = tf.train.Saver()
            
            with tf.Session() as sess:
                saver.restore(sess, "lxd/model/model.ckpt")    
                current_pre =  sess.run(y_predict, feed_dict={x: np.load(npy)})
            return current_pre
        
    def location(self):
        i = 0
        ser = Series([])
        for x in val_segment_dict.values()[self.start: self.end]:
        #for x in val_segment_dict.get(key, []):
            ser = ser.append(Series(len(x)))
        return ser.values, ser.cumsum().values
    
    def seg_prob(self,x,y):
        current_pre = self.predict()
        return np.where(current_pre[:, 1] == 1)[0][(x < np.where(current_pre[:, 1] == 1)[0]) & (np.where(current_pre[:, 1] == 1)[0] < y)]
    
    def search(self,loc, name, show=False):
        ii = -1
        z, y, x = np.load(glob.glob('lxd/val/%s.npy'%name)[0]).shape
        zz, yy, xx = sitk.ReadImage(glob.glob('data/val_subset00/%s*mhd'%name)[0]).GetOrigin()[::-1]
        for i in range(40,z,40):
            for j in range(46,y,46):
                for k in range(46,x,46):
                    #print (i/40, j/46, k/46)
                    ii += 1
                    if ii == loc:
                        if show:
                            print (40*(i/40-1)+20+zz, 46*(j/46-1)+23+yy, 46*(k/46-1)+23+xx)
                        return DataFrame({'coordZ':[40*(i/40-1)+20+zz] ,'coordY':[46*(j/46-1)+23+yy], 'coordX':[46*(k/46-1)+23+xx]})
                    
    def outputs(self):
        data = DataFrame()
        for index, num in enumerate(range(self.end-self.start)):
            loca, loc_cumsum = self.location()
            if index == 0:
                arr = self.seg_prob(0, loca[0])
            else:
                arr = self.seg_prob(loc_cumsum[index-1], loc_cumsum[index]) - loc_cumsum[index-1]
            for loc in tqdm.tqdm(arr):
                data = pd.concat([data, self.search(loc, val_segment_dict.keys()[self.start: self.end][num])])
                
            df = DataFrame()
            for col in data:
                df = pd.concat([df, data.groupby(col).mean().reset_index()], ignore_index=True)
            df.columns.name = val_segment_dict.keys()[self.start: self.end][num]
            
            if not os.path.exists('lxd/outputs'):
                os.mkdir('lxd/outputs')
            df.to_csv('lxd/outputs/%s.csv'%df.columns.name)

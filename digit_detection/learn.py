#!/usr/bin/python
# encoding: utf-8 -*-
# encoding=utf8
import glob
import numpy as np
import cv2
import os

#from sklearn.model_selection import train_test_split
from sklearn import datasets, svm ,metrics
from sklearn.metrics import accuracy_score
 
width=28
height=28
n_pixels=width*height

def create_dataset(path):
    data = np.arange(n_pixels).reshape(1,n_pixels)
    label = []
    for i in range(0,10):
        print "Loading number " + str(i) + " from " + path + " ."
        d = path + str(i) + '/*'
        fn = glob.glob(d)
        y = np.full(len(fn),i)
        label = np.insert(label,len(label),y)
    
        for f in fn:
            img = np.array(cv2.imread(f))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            img = cv2.resize(img,(width,height))
            img = img.reshape(-1 ,)
            data = np.insert(data,data.shape[0],img,axis=0)
    data = np.delete(data,0,0)
    return data,label

x_test,y_test   = create_dataset('images/dataset-test/')
x_train,y_train = create_dataset('images/dataset/')

print(x_test.shape)
print(y_test.shape)
print (x_train.shape)
print (y_train.shape)

clf = svm.LinearSVC()
clf.fit(x_train, y_train)

from sklearn.externals import joblib
joblib.dump(clf, 'digits.pkl')

model = joblib.load('digits.pkl')
y_pred = clf.predict(x_test)
print(accuracy_score(y_test,y_pred))
 


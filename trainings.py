import pandas as pd
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import os

#read the csv file using read_csv function of pandas
train = pd.read_csv('train.csv')
train.head() 

path=os.path.join(os.getcwd(),'BCCD','JPEGImages','BloodImage_00000.jpg')
#image=plt.imread(path)
#cv.imshow('image',image)
#cv.waitKey(0)

print(train['Image_names'].nunique())

print(train['cell_type'].value_counts())
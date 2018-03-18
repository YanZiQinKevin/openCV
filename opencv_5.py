#coding: utf-8
#直方图
import cv2

import matplotlib.pyplot as plt
imgpath="/Users/yanziqin/openCV/image/4.1.01.tiff"

img = cv2.imread(imgpath,0)
img =cv2.resize(img, (32,32),interpolation=cv2.INTER_NEAREST)
# INTER_NEAREST 最近插值法
# INTER_LINEAR 双线性差值
# INTER_AREA 像素区域关系
#INTER_CUBIC 4x4 


#                   image  channels		mask   histSize		ranges
hist = cv2.calcHist([img],   [0],      None,   [256],     [0,256])
ee =cv2.equalizeHist(img)
#cv2.imshow("equalizeHist",ee)
plt.figure()
plt.plot(hist)
plt.show()

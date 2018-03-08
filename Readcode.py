#coding=utf-8

import numpy as np
import cv2

# img 是原始图，image是识别一维码以后的图像
def QRcode(img,image):
  #eference：http://dsynflo.blogspot.in/2014/10/opencv-qr-code-detection-and-extraction.html
  img_G = cv2.GaussianBlur(img,(5,5),0)
  # ps 原本的subtract,Sobel 做出来不是个binary image,报错。索性用Canny了
  img_C = cv2.Canny(img_G,100,200)
  _,cnts, hierarchy = cv2.findContours(img_C, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  #print(len(cnts))
  hierarchy = hierarchy[0]
  box = []
  for i in range(len(cnts)):
    k = i
    c = 0
    while hierarchy[k][2] != -1:
        k = hierarchy[k][2]
        c = c + 1
    if c >= 5:
      #print("C")
      box.append(i)
  img_dc = image.copy()
  for i in box:

      cv2.drawContours(img_dc, cnts, i, (0, 0, 255), 3)
  cv2.imshow("Results",img_dc)
  
  return 0

def dBarcode(img):
  gradX = cv2.Sobel(img, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
  gradY = cv2.Sobel(img, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)

  gradient = cv2.subtract(gradX, gradY)
  gradient = cv2.convertScaleAbs(gradient)

  blurred = cv2.blur(gradient, (9, 9))
  (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
  #条形码形态 (25,5)
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25 , 5))

  closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
  #cv2.imshow("preoss", closed)
  #通过迭代去除，次数越大，去的范围越大
  closed = cv2.erode(closed, None, iterations = 15)
  closed = cv2.dilate(closed, None, iterations = 15)
  (_,cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # if no contours were found, return None
  if len(cnts) == 0:
    return None

  # otherwise, sort the contours by area and compute the rotated
  # bounding box of the largest contour
  cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
  
  return cnt


 #main
#摄像头开启 
#cap = cv2.VideoCapture(0)
while True:
  #image 版本
  image = cv2.imread('images.jpeg')


  #摄像头版本
  #ret, image = cap.read()
  cv2.imshow("OR", image)

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  
  #一维码检测
  c = dBarcode(gray)
  x,y,w,h = cv2.boundingRect(c)
  cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
  #cv2.putText(image,'Dbarcode', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0))
  
  #二维码检测
  QRcode(gray,image)

  #cv2.imshow("Results", image)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cv2.destroyAllWindows()

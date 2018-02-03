#coding=utf-8
#-*- coding:utf-8 -*-
#Haar Cascade for image & video object classification 
import numpy as np

import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, img = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    line= cv2.Canny(img,80,100)
    #cv2.imshow('windows1',line)
    face=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in face:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]

        f=u'Face'.encode('utf-8')
        #f='face'
        cv2.putText(img,f, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,255),2,cv2.LINE_AA)
        eyes=eye_cascade.detectMultiScale(roi_gray)
        i=0
        # w = eyes.shape[1]
        # h = eyes.shape[0]
        # ii = 0
        #let image get darker
        # for xi in xrange(0,w):
        #     for xj in xrange(0,h):
        #         #set the pixel value decrease to 20%
        #         eyes[xj,xi,0] = int(eyes[xj,xi,0]*1.2)
        #         eyes[xj,xi,1] = int(eyes[xj,xi,0]*1.2)
        #         eyes[xj,xi,2] = int(eyes[xj,xi,0]*1.2)
        for (ex,ey,ew,eh) in eyes:
            if i<2:
                cv2.putText(img,'Eye',(ex+400, ey+150),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)
                #img_eye=cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                i=i+1

                #print(img_eye)
           # cv2.putText(img,"eye", (ex,ey), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    # Display the resulting frame
    cv2.imshow('Y_face_recognition',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
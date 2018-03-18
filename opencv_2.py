#coding: utf-8


#image, Number, and NumPy
#Numpy= Numberical python
import cv2
import numpy as np
def main():

	img=np.zeros((512,512,3),np.uint8)
	#划线
	cv2.line(img,(0,99),(99,0),(255,0,0),2)
	#方块
	cv2.rectangle(img,(40,60),(200,170),(0,255,0),1)
	#圆
	cv2.circle(img,(60,60),10,(0,0,255),-1)
	#椭圆
	cv2.ellipse(img,(140,160), (50,20),0,0,360,(127,127,127),-1)

	#折线
	points =np.array([[80,2],[125,40],[179,19],[230,5],[30,50]],np.int32)
	points -points.reshape((-1,1,2))
	cv2.polylines(img,[points],True,(0,255,255))
	#string 
	text = 'Test Test'
	cv2.putText(img,text,(200,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0))

	#cv2.imshow('lne',img)
	# SIFT
	imgpath="/Users/yanziqin/openCV/image/4.1.01.tiff"
	img = cv2.imread(imgpath,cv2.IMREAD_COLOR)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imshow('orgin',img)

	detector = sift = cv2.xfeatures2d.SIFT_create()
	keypoints = detector.detect(gray, None)
	#img = cv2.drawKeypoints(gray,keypoints,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  
	print(len(keypoints))
	for k in keypoints:
		cv2.circle(img,(int(k.pt[0]),int(k.pt[1])),1,(0,0,255),-1)

	cv2.imshow('test',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()
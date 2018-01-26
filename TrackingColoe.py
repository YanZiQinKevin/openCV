import cv2
import numpy as np 
#BGR/RGB -> HSV
#Hue, Saturation, Value

def main():
	windowName= "Preview"
	cv2.namedWindow(windowName,cv2.WINDOW_NORMAL)
	cap=cv2.VideoCapture(0)

	if cap.isOpened():
		ret,frame=cap.read()
	else:
		ret = False

	while ret:
		ret,frame =cap.read()

		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

		#Blue 
		#low = np.array([100,50,50])
		#high = np.array([140,255,255])

		#green
		#low=np.array([40,50,50])
		#high= np.array([80,255,255])

		#red
		low=np.array([170,70,50])
		high=np.array([180,255,255])

		image_mask = cv2.inRange(hsv,low,high)

		output=cv2.bitwise_and(frame,frame,mask=image_mask)
		cv2.namedWindow('image_mask',cv2.WINDOW_NORMAL)
		cv2.resizeWindow('image_mask', 512,512)
		cv2.imshow('image_mask',image_mask)
		#print(image_mask)
		#org
		cv2.resizeWindow(windowName, 512,512)
		cv2.imshow(windowName,frame)
		#output
		cv2.namedWindow('output',cv2.WINDOW_NORMAL)
		cv2.resizeWindow('output', 512,512)
		cv2.imshow('output',output)
		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()
	cap.release()





main()
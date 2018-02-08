#coding=utf-8

import urllib
import cv2
import numpy as np 
import urllib2
import os 

def store_raw_images():
	neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04586581'
	neg_images_urls = urllib.urlopen(neg_images_link).read().decode('utf-8')

	if not os.path.exists('neg'):
		os.makedirs('neg')

	pic_num=0
	for i in neg_images_urls.split('\n'):
		try:
			pic_num= pic_num+1
			print(str(pic_num),i)
			urllib.urlretrieve(i,"neg/"+str(pic_num)+'.jpg')
			img=cv2.imread("neg/"+str(pic_num)+'/jpg',cv2.IMREAD_GRAYSCALE)
			resized_image=cv2.resize(img,(100,100))
			cv2.imwrite("neg/"+str(pic_num)+'/jpg',resized_image)
			
			

		except Exception as e:
			print(str(e))
	print("done")
store_raw_images()

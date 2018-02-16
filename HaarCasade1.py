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
def find_uplies():
	for file_type in ['neg']:
		for img in os.listdir(file_type):
			for ugly in os. listdir('uglies'):
				try:
					current_image_path =str(file_type)+'/'+str(img)
					ugly=cv2.imread('uglies/'+str(ugly))
					question = cv2.imread(current_image_path)
					if ugly.shape == question.shape and not (np.bitwise_xor(ugly,question).any()):
						print(current_image_path)
						os.remove(current_image_path)

				except Exception as e:
					print(str(e))

def create_post_n_neg():
	for file_type in ['neg']:
		for img in os.listdir(file_type):
			if file_type=='neg':
				line=file_type+'/'+img+'\n'
				with open('bg.txt','a') as f:
					f.write(line)

			elif file_type =='pos':
				line=file_type+'/'+img+'1 0 0 50 50\n'
				with open('info.dat','a') as f:
					f.write(line)

#store_raw_images()
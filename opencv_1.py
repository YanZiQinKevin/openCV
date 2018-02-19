#coding: utf-8


import cv2

def main():

	#reading and displaying the image
	imgpath="/Users/yanziqin/openCV/image/4.1.01.tiff"
	#imread: 1为彩色，0为黑白
	img = cv2.imread(imgpath,1)

	#Image = set of numbers
	print(img)
	#[ 42  46  52] = B G R
	#N dimensional arrays = composite data type

	print(img.dtype)
	print(img.shape)
	print(img.size)
	print(img.ndim)

	cv2.namedWindow('lne',cv2.WINDOW_AUTOSIZE)
	cv2.imshow('lne',img)

	#copy image
	#outpath="/Users/yanziqin/openCV/output/4.1.01.tiff"
	#cv2.imwrite(outpath,img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ =="__main__":
	main()
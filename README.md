## openCV

OpenCV learning code by Python  
## QRcode & dBarcode  
code: Readcode.py  
  In dBarcode recognition: It is easy to do. I used cv2.getStructuringElement to check out the rectangle as a kernel, and remove another noise. However, the QRcode is another case before I was wrong that I thought it's as easy as dBarcode. The QRcode,we need conform the THREE small rectangle frist. The way is 5 more times iteration of hierarchy. 
![image](https://github.com/YanZiQinKevin/openCV/blob/master/screenshoot/WX20180308-114126%402x.png)

(2018/3/8,USA)  
Reference: http://dsynflo.blogspot.in/2014/10/opencv-qr-code-detection-and-extraction.htm  

## Deconvolution:

deconvolution is an iterative algorithm for recovering an image which is blurred by a known point spread function (PSF). You can find the iterative algorithm steps in：https://en.wikipedia.org/wiki/Deconvolution
https://en.wikipedia.org/wiki/Richardson%E2%80%93Lucy_deconvolution

作用：把模糊画面还原， 在移动设备中，提高识别成功率：  
关于motion blur 的论文： http://www.cse.cuhk.edu.hk/%7Eleojia/projects/robust_deblur/index.html  
Wiener_deconvolution： https://en.wikipedia.org/wiki/Wiener_deconvolution  
opencv_4.py  
deconvolution.ipynb  

![image](https://github.com/YanZiQinKevin/openCV/blob/master/image/decon_shoot.png)


# color recognition
BGR->HSV
Example: Tracking the Blue pen

![TrackingColor](https://github.com/YanZiQinKevin/openCV/blob/master/image/screenshoot.png)



# Make Haar Cascade
1 Collect "Negative" or "background" image

2 collect or create "positive" images

3 Create a positive vector file by stitching   	  together all positives. 

> opencv_createsamples -img XXX.jpg -bg bg.txt -info .ist -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -num -1950

4 Train cascade

>  opencv_traincascade -data data -vec positives.vec -bg bg.txt -numP os 1800 -numNeg 900 -numStages 10 -w 20 -h 20

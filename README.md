# openCV

OpenCV learning code by Python

1，color recognition
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

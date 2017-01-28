from WebcamVideoStream import WebcamVideoStream
import numpy as np
import cv2
#import libraries and setup GPIO-pins
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

#Picture input-pin
GPIO.setup(2,GPIO.IN)

#Start/stop recording input-pin
GPIO.setup(4.GPIO.IN)


fps = 11
width = 640
height = 480
# Create VideoCapture objects
cap0 = WebcamVideoStream(fps, src=0).start()
cap1 = WebcamVideoStream(fps, src=1).start()

# Define the codec and create VideoWriter objects
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out0 = cv2.VideoWriter('cam0.avi', fourcc, fps, (width,height))
out1 = cv2.VideoWriter('cam1.avi', fourcc, fps, (width,height))
#Making sure that only one picture is taken
picturecount = 0

while(GPIO.input(2)==1 or GPIO.input(4)==1):
	
	#if take picture
	if(GPIO.input(2)==1 and picturecount=0):
		frame0 = cap0.read()
		frame1 = cap1.read()
		cv2.imwrite('picture0.png', frame0)
		cv2.imwrite('picture1.png', frame1)
		picturecount=1
        
		
	#if take video
	if(GPIO.input(4)):
		while(GPIO.input(4)):
			# read frames
			frame0 = cap0.read()
			frame1 = cap1.read()
			
			# write the frames
			out0.write(frame0)
			out1.write(frame1)
			
		
# Release everything if job is finished
cap0.stop()
cap1.stop()
out0.release()
out1.release()
cv2.destroyAllWindows()
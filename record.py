from WebcamVideoStream import WebcamVideoStream
import numpy as np
import cv2
import sys, getopt
import threading

import RPi.GPIO as GPIO
import os
import time

nCameras = 0
cap = [0]*(nCameras+1)
out = [0]*(nCameras+1)
frame = [0]*(nCameras+1)
	
picturecount = 0
videocount = 0

def do_every(interval, worker_func):
	if(GPIO.input(4)):
		threading.Timer(interval, do_every, [interval, worker_func]).start()
		worker_func()
	else:
		new_VideoWriters()
		recording = False
	
	
def take_picture():
	global frame, cap, nCameras, picturecount
	for i in range(0,nCameras):
		frame[i] = cap[i].read()
	for i in range(0,nCameras):
		cv2.imwrite('picture'+str(picturecount)+'_'+str(i)+'.png', frame[i])
				
def record_frame():
	global frame, cap, out
	# read frames
	for i in range(0,nCameras):
		frame[i] = cap[i].read()
				
	# write the frames
	for i in range(0,nCameras):
		out[i].write(frame[i])


def new_VideoWriters():
	global out, videocount
	for i in range(0,nCameras):
		out[i] = cv2.VideoWriter('video'+str(videocount)+'_'+str(i)+'.avi', fourcc, fps, (width,height))
	videocount += 1

def main(argv):

	global nCameras
	global cap, out, frame, picturecount, fourcc
	global fps, width, height
	
	try:
		opts, args = getopt.getopt(argv,"hn:")
	except getopt.GetoptError:
		print 'record.py -n <number_of_cameras>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'record.py -n <number_of_cameras>'
			sys.exit()
		elif opt in ("-n"):
			nCameras = arg
	
	if nCameras == 0:
		print 'record.py -n <number_of_cameras>'
		sys.exit()

		
	#Setup GPIO-pins
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	#Picture input-pin
	GPIO.setup(2,GPIO.IN)

	#Start/stop recording input-pin
	GPIO.setup(4,GPIO.IN)


	fps = 10
	width = 640
	height = 480
	

	# Create VideoCapture objects
	for i in range(0,nCameras):
		cap[i] = WebcamVideoStream(fps, src=i).start()

	# Define the codec and create VideoWriter objects
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	new_VideoWriters()
	
	recording = False

	while(1):
		
		#if take picture
		if(GPIO.input(2)):
			take_picture()
			picturecount += 1
			time.sleep(1)
			
				
		#if take video
		if(GPIO.input(4)):
			recording = True
			do_every(1/fps, record_frame)
			while(recording):
				pass
			
			
	# Release everything if job is finished
	for i in range(0,nCameras):
		cap[i].stop()
		out[i].release()
	cv2.destroyAllWindows()
	
if __name__ == "__main__":
   main(sys.argv[1:])
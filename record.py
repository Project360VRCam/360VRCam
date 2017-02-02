from WebcamVideoStream import WebcamVideoStream
import numpy as np
import cv2
import sys, getopt
import threading

import RPi.GPIO as GPIO
import os

def do_every(interval, worker_func):
	if(GPIO.input(4)):
		threading.Timer(interval, do_every, [interval, worker_func]).start()
	worker_func()
	
def take_picture():
	global frame, cap
	for i in range(0,nCameras):
				frame[i] = cap[i].read()
			for i in range(0,nCameras):
				cv2.imwrite('picture'+str(i)+'.png', frame[i])
				
def record_video():
	global frame, cap, out
	# read frames
	for i in range(0,nCameras):
		frame[i] = cap[i].read()
				
	# write the frames
	for i in range(0,nCameras):
		out[i].write(frame[i])
		

def main(argv):

	nCameras = ''
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
	
	if nCameras == '':
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
	
	cap = [0]*nCameras
	out = [0]*nCameras
	frame = [0]*nCameras

	# Create VideoCapture objects
	for i in range(0,nCameras)):
		cap[i] = WebcamVideoStream(fps, src=i).start()

	# Define the codec and create VideoWriter objects
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	for i in range(0,nCameras):
		out[i] = cv2.VideoWriter('cam'+str(i)+'.avi', fourcc, fps, (width,height))
	
	#Making sure that only one picture is taken
	picturecount = 0


	while(GPIO.input(2)==1 or GPIO.input(4)==1):
		
		#if take picture
		if(GPIO.input(2)):
			take_picture()
				
		#if take video
		if(GPIO.input(4)):
			do_every(1/fps, record_video)
			
			
	# Release everything if job is finished
	for i in range(0,nCameras):
		cap[i].stop()
		out[i].release()
	cv2.destroyAllWindows()
	
if __name__ == "__main__":
   main(sys.argv[1:])